#Django
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

#model
from users.models import User
from iteractions.models import Relationship
from posts.models import Project



# Create your views here.
@login_required
def follow(request, username, project_slug):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	if project_slug==username:
		return HttpResponseRedirect(reverse('users:detail', args=[username]))	
	elif project_slug==to_user.email:
		return redirect('iteractions:list_user')
	else:
		return HttpResponseRedirect(reverse('posts:detail_project', args=[project_slug]))
	
@login_required
def unfollow(request, username, project_slug):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	if project_slug==username:
		return HttpResponseRedirect(reverse('users:detail', args=[username]))	
	elif project_slug==to_user.email:
		return redirect('iteractions:list_user')
	else:
		return HttpResponseRedirect(reverse('posts:detail_project', args=[project_slug]))

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