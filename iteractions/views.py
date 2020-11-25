#Django
from django.template import loader, RequestContext
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib import messages
from django.urls import reverse

#model
from users.models import User, Profile
from iteractions.models import Relationship, Likes, Notification, Comment, Message
from posts.models import Project



# Create your views here.
@login_required
def follow(request, username, project_slug):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()

	notify = Notification(sender=current_user, user=to_user_id, notification_type=3)
	notify.save()
	if project_slug==username:
		return HttpResponseRedirect(reverse('users:detail', args=[username]))	
	elif project_slug==to_user.email:
		return redirect('iteractions:list_user')
	else:
		return HttpResponseRedirect(reverse('posts:detail_project', args=[project_slug, 0]))
	
@login_required
def unfollow(request, username, project_slug):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()

	notify = Notification.objects.filter(sender=current_user, user=to_user_id, notification_type=3)
	notify.delete()
	if project_slug==username:
		return HttpResponseRedirect(reverse('users:detail', args=[username]))	
	elif project_slug==to_user.email:
		return redirect('iteractions:list_user')
	else:
		return HttpResponseRedirect(reverse('posts:detail_project', args=[project_slug, 0]))

@login_required
def UserListView(request,**kwargs):
    busqueda = request.POST.get("buscar")
    users = User.objects.all().order_by('username')
    if busqueda:
        users = User.objects.filter(
            Q(username__icontains = busqueda) | 
            Q(email__icontains = busqueda) 
        ).distinct()	
    paginator=Paginator(users, 6)
    page=request.GET.get('page')
    users=paginator.get_page(page)
    return render(request, 'iteractions/list_users.html', {'users':users})

@login_required
def like(request, project_id,  project_slug):
	user = request.user
	post = Project.objects.get(id=project_id)
	current_likes = post.likes
	liked = Likes.objects.filter(user=user, post=post).count()

	if not liked:
		like = Likes.objects.create(user=user, post=post)
		current_likes = current_likes + 1
	else:
		Likes.objects.filter(user=user, post=post).delete()
		current_likes = current_likes - 1
	
	post.likes = current_likes
	post.save()
	if post.url == project_slug:
		return HttpResponseRedirect(reverse('posts:detail_project', args=[project_slug, 0]))
	elif post.id == int(project_slug):
		return HttpResponseRedirect(reverse('posts:feed'))
	else:
		return HttpResponseRedirect(reverse('posts:list_project'))


@login_required
def ShowNOtifications(request):
	user = request.user
	notifications = Notification.objects.filter(user=user).order_by('-date')
	Notification.objects.filter(user=user, is_seen=False).update(is_seen=True)

	template = loader.get_template('iteractions/notifications.html')

	context = {
		'notifications': notifications,
	}

	return HttpResponse(template.render(context, request))

@login_required
def DeleteNotification(request, noti_id):
	user = request.user
	Notification.objects.filter(id=noti_id, user=user).delete()
	return redirect('iteractions:notification')


def CountNotifications(request):
	count_notifications = 0
	if request.user.is_authenticated:
		count_notifications = Notification.objects.filter(user=request.user, is_seen=False).count()
	return {'count_notifications':count_notifications}


def DeleteComments(request, comment_id, url):
	projects = Project.objects.get(url=url)
	
	comment = Comment.objects.get(id=comment_id)
	Comment.objects.filter(id=comment_id, user= comment.user, post=comment.post).delete()

	count=projects.count_comments-1
	Project.objects.filter(url=url).update(count_comments=count)
    
	return HttpResponseRedirect(reverse('posts:detail_project', args=[url, 0]))
	

@login_required
def favorite(request, post_id, position):
	user = request.user
	post = Project.objects.get(id=post_id)
	profile = Profile.objects.get(user=user)
	url=post.url

	if profile.favorites.filter(id=post_id).exists():
		profile.favorites.remove(post)

	else:
		profile.favorites.add(post)
	if position != 0:
		return HttpResponseRedirect(reverse('posts:detail_project', args=[url, 0]))
	else:
		return HttpResponseRedirect(reverse('users:detail', args=[user.username]))

@login_required
def Inbox(request, username):
	messages = Message.get_messages(user=request.user)
	active_direct = None
	directs = None

	if username != request.user.username:
		if messages:
			message = messages[0]
			active_direct = message['user'].username
			directs = Message.objects.filter(user=request.user, recipient=message['user'])
			directs.update(is_read=True)
			for message in messages:
				if message['user'].username == active_direct :
					message['unread'] = 0
	
	active_direct = User.objects.get(username=username)

	

	context = {
		'directs': directs,
		'messages': messages,
		'active_direct': active_direct,
		'username':username,

		}

	template = loader.get_template('iteractions/messages.html')

	return HttpResponse(template.render(context, request))

@login_required
def Directs(request, username):
	user = request.user
	messages = Message.get_messages(user=user)
	active_direct = User.objects.get(username=username)
	directs = Message.objects.filter(user=user, recipient__username=username)
	directs.update(is_read=True)

	for message in messages:
		if message['user'].username == username:
			message['unread'] = 0

	context = {
		'directs': directs,
		'messages': messages,
		'active_direct':active_direct,
	}

	template = loader.get_template('iteractions/messages.html')

	return HttpResponse(template.render(context, request))

@login_required
def SendDirect(request):
	from_user = request.user
	to_user_username = request.POST.get('to_user')
	body = request.POST.get('body')
	if body!='':
		if request.method == 'POST':
			to_user = User.objects.get(username=to_user_username)
			Message.send_message(from_user, to_user, body)
			return HttpResponseRedirect(reverse('iteractions:messages', args=[to_user_username]))
		else:
			HttpResponseBadRequest()
	else:
		return HttpResponseRedirect(reverse('iteractions/messages.html', args=[to_user_username]))

@login_required
def NewConversation(request, username):
	from_user = request.user
	body=''
	try:
		to_user = User.objects.get(username=username)
		
	except Exception as e:
		return redirect('iteractions:list_user')
	messages = Message.objects.filter(sender=from_user, recipient=to_user).exists()

	if not messages:
		if from_user != to_user:
			Message.send_message(from_user, to_user, body)

	return HttpResponseRedirect(reverse('iteractions:messages', args=[username]))


def DeleteConversation(request,  recipient):
	user=request.user
	Message.objects.filter(user=user, recipient= recipient).delete()
    
	return HttpResponseRedirect(reverse('iteractions:messages', args=[request.user.username]))


def checkDirects(request):
	directs_count = 0
	if request.user.is_authenticated:
		mensajes=Message.objects.filter(user=request.user, is_read=False)
		for mensaje in mensajes:
			if mensaje.body != '':
				directs_count+=1

	return {'directs_count':directs_count}


    