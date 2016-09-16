from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from forms import LoginForm, DivErrorList, PasswordChangeForm
from django.http import Http404
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from apps.users.models import *
from apps.projects.models import *
from forms import AdminForm, AdminEditForm
from datetime import datetime


@login_required
def logout_view(request):
  logout(request)
  return redirect('/')


@login_required
def dashboard(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.user.is_authenticated():
            today = datetime.today()
            projects = Project.objects.all()
            num_of_users = KAKUser.objects.filter(is_admin='0').count()
            num_of_issues = Issue.objects.all().count()
            num_of_comments = IssueComment.objects.all().count()
            project_name = ''
            if request.user.is_admin == '2':
                project_name = Project.objects.get(id=request.user.project_id)
                num_of_users = IssueComment.objects.filter(issue__project__id=int(request.user.project_id), author__is_admin='0').count()
                num_of_issues = Issue.objects.filter(project__id=int(request.user.project_id)).count()
                num_of_comments = IssueComment.objects.filter(issue__project__id=int(request.user.project_id)).count()
            issues = ''
            if request.user.is_admin == '2':
                issues = Issue.objects.filter(project__id=int(request.user.project_id))
            web_count = IssueComment.objects.filter(timestamp__year=today.year, timestamp__month=today.month,
                                                               timestamp__day=today.day, input_channel='web').count()
            results = IssueComment.objects.filter(timestamp__year=today.year, timestamp__month=today.month,
                                                        timestamp__day=today.day)
            social_count = results.filter(Q(input_channel='Facebook')|
                                         Q(input_channel='Twitter')|
                                         Q(input_channel='Whatsapp')).count()
            offline_count = IssueComment.objects.filter(timestamp__year=today.year, timestamp__month=today.month,
                                                               timestamp__day=today.day, input_channel='Offline').count()
            latest = IssueComment.objects.all().order_by('-id')[:5]
            return render(request, 'index.html', {
                          'latest': latest,
                          'num_of_projects': projects.count(),
                          'num_of_users':num_of_users,
                          'num_of_issues': num_of_issues,
                          'num_of_comments': num_of_comments,
                          'issues': issues,
                          'web_count': web_count,
                          'social_count': social_count,
                          'offline_count': offline_count,
                          'project_name': project_name,
                          'projects': projects})
        redirect('/login/')


def login_view(request):
    next = request.GET.get('next')
    if request.user.is_authenticated():
        redirect('/users/dashboard/')

    if request.method == "POST":
        form = LoginForm(request.POST, error_class=DivErrorList)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            userobject = authenticate(email=email, password=password)
            if userobject is not None and userobject.is_active:
                login(request, userobject)
                if request.POST.get('next'):
                    return redirect(request.POST.get('next'))
                return redirect('/users/dashboard/')
            else:
                return render(request, 'home.html', {'form': form})
        else:
            return render(request, 'home.html', {'form': form})

    ''' user is not submitting any form, show the login form '''
    form = LoginForm()
    return render(request, 'home.html', {'form': form, 'next': next})



@sensitive_post_parameters()
@csrf_protect
@login_required
def password_change(request,
                    template_name='registration/password_change_form.html',
                    post_change_redirect=None,
                    password_change_form=PasswordChangeForm,
                    current_app=None, extra_context=None):
    if post_change_redirect is None:
        post_change_redirect = reverse('password_change_done')
    else:
        post_change_redirect = resolve_url(post_change_redirect)
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


@login_required
def password_change_done(request,
                         template_name='registration/password_change_done.html',
                         current_app=None, extra_context=None):
    context = {}
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


@login_required
def user_list(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myusers = KAKUser.objects.all().order_by('-id')
        if request.method == 'GET':
            return render_to_response('userlist.html', {'myusers': myusers,
                }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def admin_list(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myusers = KAKUser.objects.filter(is_admin='2').order_by('-id')
        if request.method == 'GET':
            return render_to_response('user_list.html', {'myusers': myusers,
                }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def user_detail(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myuser = KAKUser.objects.get(id=pk)
        if request.method == 'GET':
            return render_to_response('user_detail.html', {'myuser': myuser,
                }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def confirm_delete_admin(request, pk):
    if request.user.is_admin == '1':
        myuser = KAKUser.objects.get(id=pk)
        if request.method == 'GET':
            return render_to_response('confirm_delete_admin.html', {'id': pk, 'myuser': myuser,
                }, context_instance=RequestContext(request))
    else:
        redirect('/users/dashboard/')


@login_required
def delete_admin(request, pk):
    if request.user.is_admin == '1':
        if request.method == 'POST':
            KAKUser.objects.get(id=pk).delete()
            return redirect('/users/all_admin/?deleted=True')
    else:
        redirect('/users/dashboard/')


@login_required
def create_admin(request):
    if request.user.is_admin == '1':
        if request.method == 'GET':
            projects = Project.objects.all()
            form = AdminForm(error_class=DivErrorList, options=projects)
            return render_to_response("add_admin.html", {
                "form": form,
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            projects = Project.objects.all()
            form = AdminForm(request.POST, error_class=DivErrorList, options=projects)
            if form.is_valid():
                my_issue = form.save(commit=False)
                if request.POST['is_admin'] == '2':
                    my_issue.is_superuser = True
                my_issue.save()
                return redirect('/users/all_admin/?added=True')
            else:
                return render_to_response("add_admin.html", {
                    "form": form,
                }, context_instance=RequestContext(request))
    else:
        redirect('/public_forums/')


@login_required
def edit_admin(request, pk):
    if request.user.is_admin == '1':
        if request.method == 'GET':
            myinstance = KAKUser.objects.get(id=int(pk))
            project = Project.objects.get(id=int(myinstance.project_id))
            projects = Project.objects.all()
            form = AdminEditForm(error_class=DivErrorList, instance=myinstance, options=projects)
            return render_to_response("edit_admin.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
                'project': project.name
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            myinstance = KAKUser.objects.get(id=int(pk))
            projects = Project.objects.all()
            form = AdminEditForm(request.POST or None, error_class=DivErrorList, instance=myinstance, options=projects)
            if form.is_valid():
                my_Issue = form.save(commit=False)
                my_Issue.save()
                return redirect('/users/all_admin/?edited=True')
            else:
                return render_to_response("edit_admin.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
                }, context_instance=RequestContext(request))
    else:
        redirect('/public_forums/')


def handler500(request):
    return render(request, '500.html')

def handler404(request):
    return render(request, '404.html')
