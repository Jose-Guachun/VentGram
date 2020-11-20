from django.db import models
from posts.models import Project
from users.models import User 
from iteractions.models import Notification

from django.db.models.signals import post_save, post_delete

class Comment(models.Model):
	post = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def user_comment_post(sender, instance, *args, **kwargs):
		comment = instance
		post = comment.post
		text_preview = comment.body[:90]
		sender = comment.user
		if post.user != sender:
			notify = Notification(post=post, sender=sender, user=post.user, text_preview=text_preview ,notification_type=2)
			notify.save()

	def user_del_comment_post(sender, instance, *args, **kwargs):
		like = instance
		post = like.post
		sender = like.user

		notify = Notification.objects.filter(post=post, sender=sender, notification_type=2)
		notify.delete()

#Comment
post_save.connect(Comment.user_comment_post, sender=Comment)
post_delete.connect(Comment.user_del_comment_post, sender=Comment)