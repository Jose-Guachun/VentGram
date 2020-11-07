#Django
from django.shortcuts import render
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView
#model
from users.models import User
from posts.models import Project
from iteractions.models import Relationship, Likes, Notification

# Create your views here.
def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	messages.success(request, f'sigues a {username}')
	return redirect('posts:feed')

def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	messages.success(request, f'Ya no sigues a {username}')
	return redirect('posts:feed')

@login_required
def like(request, project_id):
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
	return HttpResponseRedirect(reverse('posts:feed'))

def ShowNOtifications(request):
	user = request.user
	notifications = Notification.objects.filter(user=user).order_by('-date')
	Notification.objects.filter(user=user, is_seen=False).update(is_seen=True)

	template = loader.get_template('iteractions/notifications.html')

	context = {
		'notifications': notifications,
	}

	return HttpResponse(template.render(context, request))

def DeleteNotification(request, noti_id):
	user = request.user
	Notification.objects.filter(id=noti_id, user=user).delete()
	return redirect('show-notifications')


def CountNotifications(request):
	count_notifications = 0
	if request.user.is_authenticated:
		count_notifications = Notification.objects.filter(user=request.user, is_seen=False).count()

	return {'count_notifications':count_notifications}
	



class NotificationsViews(TemplateView):
	template_name = 'iteractions/notifications.html'

class MessagesViews(TemplateView):
	template_name = 'iteractions/messages.html'