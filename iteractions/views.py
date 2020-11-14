#Django
from django.template import loader
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

#model
from users.models import User, Profile
from iteractions.models import Relationship, Likes, Notification, Comment
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
    users = User.objects.all()
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



class MessagesViews(TemplateView):
	template_name = 'iteractions/messages.html'