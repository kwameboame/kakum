from django.shortcuts import redirect, render_to_response, render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import Http404
from apps.projects.models import *
from forms import *


@login_required
def all_issues(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.user.is_admin == '1':
            issues = Issue.objects.all().order_by('-id')
        else:
            issues = Issue.objects.filter(project__id=int(request.user.project_id)).order_by('-id')
        if request.method == 'GET':
            return render_to_response('all_issues.html', {
                'issues': issues
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def project_issues(request, pk):
    if request.user.is_admin == '1':
        if request.method == 'GET':
            return render_to_response('associated.html', {
                'issues': Issue.objects.filter(project__id=int(pk)).order_by('-id'),
                'project_name': Project.objects.get(id=int(pk)).name
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def past(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'GET':
            return render_to_response('past.html',
                                      {'projects': Project.objects.filter(has_expired=True).order_by('-id')},
                                      context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def ongoing(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'GET':
            return render_to_response('ongoing.html',
                                      {'projects': Project.objects.filter(has_expired=False).order_by('-id')},
                                      context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def all_projects(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'GET':
            return render_to_response('all_projects.html', {
                'projects': Project.objects.all().order_by('-id')
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def all_articles(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.user.is_admin == '1':
            articles = KnowledgeArticle.objects.all().order_by('-id')

        elif request.user.is_admin == '2':
            articles = KnowledgeArticle.objects.filter(project__id=int(request.user.project_id)).order_by('-id')

        if request.method == 'GET':
            return render_to_response('all_articles.html', {
                'articles': articles,
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def all_documents(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.user.is_admin == '1':
            documents = KnowledgeDocument.objects.all().order_by('-id')

        elif request.user.is_admin == '2':
            documents = KnowledgeDocument.objects.filter(project__id=int(request.user.project_id)).order_by('-id')

        if request.method == 'GET':
            return render_to_response('all_documents.html', {
                'documents': documents,
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def all_albums(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        albums = GalleryAlbum.objects.all().order_by('-id')

        if request.method == 'GET':
            return render_to_response('all_albums.html', {
                'albums': albums,
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def all_videos(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        videos = GalleryVideo.objects.all().order_by('-id')
        if request.method == 'GET':
            return render_to_response('all_videos.html', {
                'videos': videos,
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def view_issue(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myIssue = Issue.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('detailed_issue.html', {'id': pk,
                                                              'myIssue': myIssue,
                                                              }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def view_project(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myprojects = Project.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('detailed_project.html', {'id': pk, 'myprojects': myprojects,
                                                                 }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def confirm_delete_project(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myproject = Project.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('confirm_delete_project.html', {'id': pk,
                                                    'myproject': myproject,
                                                                      }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def confirm_delete_issue(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myissue = Issue.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('confirm_delete_issue.html', {'id': pk, 'myissue': myissue},
                                      context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def delete_issue(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'POST':
            Issue.objects.get(id=int(pk)).delete()
            return redirect('/projects/all_issues/?deleted=True')
    else:
        raise Http404


@login_required
def delete_album(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'POST':
            GalleryAlbum.objects.get(id=int(pk)).delete()
            return redirect('/projects/all_albums/?deleted=True')
    else:
        raise Http404


@login_required
def delete_project(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'POST':
            Project.objects.get(id=int(pk)).delete()
            return redirect('/projects/all_projects/?deleted=True')
    else:
        raise Http404


@login_required
def add_issue(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'GET':
            projects = Project.objects.all()
            if request.user.is_admin == '1':
                form = IssueForm(error_class=DivErrorList, options=projects)
            else:
                form = IssueAdminForm(error_class=DivErrorList)
            choice_formset_video = ChoiceFormSetVideo(instance=Issue())
            choice_formset_image = ChoiceFormSetImage(instance=Issue())
            choice_formset_document = ChoiceFormSetDocument(instance=Issue())
            return render_to_response("add_issue.html", {
                "form": form,
                'choice_formset_image': choice_formset_image,
                'choice_formset_video': choice_formset_video,
                'choice_formset_document': choice_formset_document,
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            projects = Project.objects.all()
            if request.user.is_admin == '1':
                form = IssueForm(request.POST, error_class=DivErrorList, options=projects)
            else:
                form = IssueAdminForm(request.POST, error_class=DivErrorList)
            if form.is_valid():
                my_issue = form.save(commit=False)

                choice_formset_video = ChoiceFormSetVideo(request.POST, instance=my_issue)
                choice_formset_image = ChoiceFormSetImage(request.POST, instance=my_issue)
                choice_formset_document = ChoiceFormSetDocument(request.POST, instance=my_issue)

                if choice_formset_video.is_valid() and choice_formset_image.is_valid() and choice_formset_document.is_valid():
                    my_issue.author = request.user
                    if request.user.is_admin == '2':
                        myissue.project = Project.objects.get(id=int(request.user.project_id))
                    my_issue.save()
                    choice_formset_image.save()
                    choice_formset_video.save()
                    choice_formset_document.save()
                    return redirect('/projects/all_issues/?added=True')
                else:
                    return render_to_response("add_issue.html", {
                        "form": form,
                    }, context_instance=RequestContext(request))
            else:
                return render_to_response("add_issue.html", {
                    "form": form,
                }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def issue_detail(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myissue = Issue.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('issue_detail.html', {'myissue': myissue,
                                                            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def project_detail(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myproject = Project.objects.get(id=int(pk))
        myissues = myproject.myissues.all()
        if request.method == 'GET':
            return render_to_response('project_detail.html', {'myproject': myproject,
                                                              'myissues': myissues,
                                                              }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def add_project(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':

        if request.method == 'GET':
            form = ProjectForm(error_class=DivErrorList)
            return render_to_response("add_project.html", {
                "form": form,
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            form = ProjectForm(request.POST, error_class=DivErrorList)
            if form.is_valid():
                my_projects = form.save(commit=False)
                my_projects.author = request.user
                my_projects.save()
                return redirect('/projects/all_projects/?added=True')
            else:
                return render_to_response("add_project.html", {
                    "form": form,
                }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def edit_issue(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myinstance = Issue.objects.get(id=int(pk))
        if request.method == 'GET':
            projects = Project.objects.all()
            if request.user.is_admin == '1':
                form = IssueForm(error_class=DivErrorList, instance=myinstance, options=projects)
            else:
                form = IssueAdminForm(error_class=DivErrorList, instance=myinstance)
            choice_formset_video = ChoiceFormSetVideo(instance=myinstance)
            choice_formset_image = ChoiceFormSetImage(instance=myinstance)
            choice_formset_document = ChoiceFormSetDocument(instance=myinstance)
            return render_to_response("add_issue.html", {
                "form": form,
                'choice_formset_image': choice_formset_image,
                'choice_formset_video': choice_formset_video,
                'choice_formset_document': choice_formset_document,
                'id': pk,
                'edit': 'True'
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            projects = Project.objects.all()
            myinstance = Issue.objects.get(id=int(pk))
            if request.user.is_admin == '1':
                form = IssueForm(request.POST or None, instance=myinstance, error_class=DivErrorList, options=projects)
            else:
                form = IssueAdminForm(request.POST or None, instance=myinstance, error_class=DivErrorList)
            if form.is_valid():
                myinstance = form.save(commit=False)
                choice_formset_video = ChoiceFormSetVideo(request.POST or None, instance=myinstance)
                choice_formset_image = ChoiceFormSetImage(request.POST or None, instance=myinstance)
                choice_formset_document = ChoiceFormSetDocument(request.POST or None, instance=myinstance)
                if choice_formset_video.is_valid() and choice_formset_image.is_valid() and choice_formset_document.is_valid():
                    myinstance.save()
                    choice_formset_image.save()
                    choice_formset_video.save()
                    choice_formset_document.save()
                    return redirect('/projects/all_issues/?edited=True')
                else:
                    return render_to_response("add_issue.html", {
                        "form": form,
                    }, context_instance=RequestContext(request))
            else:
                projects = Project.objects.all()
                choice_formset_video = ChoiceFormSetVideo(instance=myinstance)
                choice_formset_image = ChoiceFormSetImage(instance=myinstance)
                choice_formset_document = ChoiceFormSetDocument(instance=myinstance)
                return render_to_response("add_issue.html", {
                    "form": form,
                    'choice_formset_image': choice_formset_image,
                    'choice_formset_video': choice_formset_video,
                    'choice_formset_document': choice_formset_document,
                    'id': pk,
                    'edit': 'True'
                }, context_instance=RequestContext(request))


@login_required
def edit_project(request, pk):
    if request.user.is_admin == '1':
        if request.method == 'GET':
            myinstance = Project.objects.get(id=int(pk))
            form = ProjectForm(error_class=DivErrorList, instance=myinstance)
            return render_to_response("add_project.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
                'myimage': myinstance.image
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            myinstance = Project.objects.get(id=int(pk))
            form = ProjectForm(request.POST or None, error_class=DivErrorList, instance=myinstance)
            if form.is_valid():
                my_projects = form.save(commit=False)
                my_projects.save()
                return redirect('/projects/all_projects/?edited=True')
            return render_to_response("add_project.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
                'myimage': myinstance.image
            }, context_instance=RequestContext(request))
    else:
        raise Http404


#VIDEO
@login_required
def add_video(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        projects = Project.objects.all()
        if request.method == 'GET':
            if request.user.is_admin == '1':
                form = GalleryVideoForm(error_class=DivErrorList, options=projects)
            else:
                form = GalleryVideoAdminForm(error_class=DivErrorList)
            return render_to_response("add_video.html", {
                "form": form,
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            if request.user.is_admin == '1':
                form = GalleryVideoForm(request.POST, error_class=DivErrorList, options=projects)
            else:
                form = GalleryVideoForm(request.POST, error_class=DivErrorList, options=projects)
            if form.is_valid():
                my_video = form.save(commit=False)
                if request.user.is_admin == '2':
                    my_video.project = Project.objects.get(id=int(request.user.project_id))
                my_video.save()
                return redirect('/projects/all_gallery/?added=True')
            else:
                return render_to_response("add_video.html", {
                    "form": form,
                }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def edit_video(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        projects = Project.objects.all()
        myinstance = GalleryVideo.objects.get(id=int(pk))
        if request.method == 'GET':
            if request.user.is_admin == '1':
                form = GalleryVideoForm(error_class=DivErrorList, instance=myinstance, options=projects)
            else:
                form = VideoForm(error_class=DivErrorList, instance=myinstance)
            return render_to_response("add_video.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            if request.user.is_admin == '1':
                form = GalleryVideoForm(request.POST or None, error_class=DivErrorList, instance=myinstance, options=projects)
            else:
                form = GalleryVideoForm(request.POST or None, error_class=DivErrorList, instance=myinstance)
            if form.is_valid():
                my_projects = form.save(commit=False)
                my_projects.save()
                return redirect('/projects/all_gallery/?edited=True')
            return render_to_response("add_video.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
            }, context_instance=RequestContext(request))
    else:
        raise Http404

#PICTURE
@login_required
def add_picture(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        projects = Project.objects.all()
        if request.method == 'GET':
            if request.user.is_admin == '1':
                form = GalleryPictureForm(error_class=DivErrorList, options=projects)
            else:
                form = GalleryPictureAdminForm(error_class=DivErrorList)
            return render_to_response("add_picture.html", {
                "form": form,
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            if request.user.is_admin == '1':
                form = GalleryPictureForm(request.POST, error_class=DivErrorList, options=projects)
            else:
                form = GalleryPictureForm(request.POST, error_class=DivErrorList, options=projects)
            if form.is_valid():
                my_video = form.save(commit=False)
                if request.user.is_admin == '2':
                    my_video.project = Project.objects.get(id=int(request.user.project_id))
                my_video.save()
                return redirect('/projects/all_gallery/?added=True')
            else:
                return render_to_response("add_picture.html", {
                    "form": form,
                }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def edit_picture(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        projects = Project.objects.all()
        myinstance = GalleryPicture.objects.get(id=int(pk))
        if request.method == 'GET':
            if request.user.is_admin == '1':
                form = GalleryPictureForm(error_class=DivErrorList, instance=myinstance, options=projects)
            else:
                form = VideoForm(error_class=DivErrorList, instance=myinstance)
            return render_to_response("add_video.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            if request.user.is_admin == '1':
                form = GalleryPictureForm(request.POST or None, error_class=DivErrorList, instance=myinstance, options=projects)
            else:
                form = GalleryPictureForm(request.POST or None, error_class=DivErrorList, instance=myinstance)
            if form.is_valid():
                my_projects = form.save(commit=False)
                my_projects.save()
                return redirect('/projects/all_gallery/?edited=True')
            return render_to_response("add_picture.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def confirm_delete_video(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myvideo = GalleryVideo.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('confirm_delete_video.html', {'id': pk, 'myvideo': myvideo},
                                      context_instance=RequestContext(request))
    else:
        raise Http404

@login_required
def confirm_delete_picture(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        mypicture = GalleryPicture.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('confirm_delete_picture.html', {'id': pk, 'mypicture': mypicture},
                                      context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def confirm_delete_album(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        mypicture = GalleryAlbum.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('confirm_delete_album.html', {'id': pk, 'myalbum': myalbum},
                                      context_instance=RequestContext(request))
    else:
        raise Http404

@login_required
def delete_video(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'POST':
            GalleryVideo.objects.get(id=int(pk)).delete()
            return redirect('/projects/all_gallery/?deleted=True')
    else:
        raise Http404


@login_required
def delete_picture(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'POST':
            GalleryPicture.objects.get(id=int(pk)).delete()
            return redirect('/projects/all_gallery/?deleted=True')
    else:
        raise Http404


@login_required
def view_video(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myvideo = GalleryVideo.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('detailed_video.html', {'id': pk, 'myvideo': myvideo,
                                                              }, context_instance=RequestContext(request))
    else:
        raise Http404

@login_required
def view_picture(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        mypicture = GalleryPicture.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('detailed_picture.html', {'id': pk, 'mypicture': mypicture,
                                                                }, context_instance=RequestContext(request))
    else:
        raise Http404


#AUDIO
@login_required
def add_audio(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        projects = Project.objects.all()
        if request.method == 'GET':
            if request.user.is_admin == '1':
                form = AudioForm(error_class=DivErrorList, options=projects)
            else:
                form = AudioForm(error_class=DivErrorList)
            return render_to_response("add_audio.html", {
                "form": form,
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            form = AudioForm(request.POST, error_class=DivErrorList, options=projects)

            if form.is_valid():
                my_audio = form.save(commit=False)
                if request.user.is_admin == '2':
                    my_audio.project = Project.objects.get(id=(request.user.project_id))
                my_audio.save()
                return redirect('/projects/all_videos/?added=True')
            else:
                return render_to_response("add_audio.html", {
                    "form": form,
                }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def edit_audio(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        projects = Project.objects.all()
        myinstance = KnowledgeAudio.objects.get(id=int(pk))
        if request.method == 'GET':
            if request.user.is_admin == '1':
                form = AudioForm(error_class=DivErrorList, instance=myinstance, options=projects)
            else:
                form = AudioForm(error_class=DivErrorList, instance=myinstance)
            return render_to_response("add_audio.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            if request.user.is_admin == '1':
                form = AudioForm(request.POST or None, error_class=DivErrorList, instance=myinstance, options=projects)
            else:
                form = AudioForm(request.POST or None, error_class=DivErrorList, instance=myinstance)
            if form.is_valid():
                my_projects = form.save(commit=False)
                my_projects.save()
                return redirect('/projects/all_videos/?edited=True')
            return render_to_response("add_audio.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def confirm_delete_audio(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myaudio = KnowledgeAudio.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('confirm_delete_audio.html', {'id': pk, 'myaudio': myaudio},
                                      context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def delete_audio(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'POST':
            KnowledgeAudio.objects.get(id=int(pk)).delete()
            return redirect('/projects/all_videos/?deleted=True')
    else:
        raise Http404


@login_required
def view_audio(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myaudio = KnowledgeAudio.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('detailed_audio.html', {'id': pk, 'myaudio': myaudio,
                                                                 }, context_instance=RequestContext(request))
    else:
        raise Http404


#DOCUMENT
@login_required
def add_document(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        projects = Project.objects.all()
        if request.method == 'GET':
            if request.user.is_admin == '1':
                form = DocumentForm(error_class=DivErrorList, options=projects)
            else:
                form = DocumentForm(error_class=DivErrorList)
            return render_to_response("add_document.html", {
                "form": form,
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            if request.user.is_admin == '1':
                form = DocumentForm(request.POST, error_class=DivErrorList, options=projects)
            else:
                form = DocumentForm(request.POST, error_class=DivErrorList)
            if form.is_valid():
                my_document = form.save(commit=False)
                if request.user.is_admin == '2':
                    my_document.project = Project.objects.get(id=int(request.user.project_id))
                my_document.save()
                return redirect('/projects/all_documents/?added=True')
            else:
                return render_to_response("add_document.html", {
                    "form": form,
                }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def edit_document(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        projects = Project.objects.all()
        myinstance = KnowledgeDocument.objects.get(id=int(pk))
        if request.method == 'GET':
            if request.user.is_admin == '1':
                form = DocumentForm(error_class=DivErrorList, instance=myinstance, options=projects)
            else:
                form = DocumentForm(error_class=DivErrorList, instance=myinstance)
            return render_to_response("add_document.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            if request.user.is_admin == '1':
                form = DocumentForm(request.POST or None, error_class=DivErrorList, instance=myinstance, options=projects)
            else:
                form = DocumentForm(request.POST or None, error_class=DivErrorList, instance=myinstance)
            if form.is_valid():
                my_projects = form.save(commit=False)
                my_projects.save()
                return redirect('/projects/all_documents/?edited=True')
            return render_to_response("add_document.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def confirm_delete_document(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        mydocument = KnowledgeDocument.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('confirm_delete_document.html', {'id': pk, 'mydocument': mydocument},
                                      context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def delete_document(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'POST':
            KnowledgeDocument.objects.get(id=int(pk)).delete()
            return redirect('/projects/all_documents/?deleted=True')
    else:
        raise Http404


@login_required
def view_document(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        mydocument = KnowledgeDocument.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('detailed_document.html', {'id': pk, 'mydocument': mydocument,
                                                                 }, context_instance=RequestContext(request))
    else:
        raise Http404


#ARTICLE
@login_required
def add_article(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        projects = Project.objects.all()
        if request.method == 'GET':
            if request.user.is_admin == '1':
                form = ArticleForm(error_class=DivErrorList, options=projects)
            else:
                form = ArticleForm(error_class=DivErrorList)
            return render_to_response("add_article.html", {
                "form": form,
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            if request.user.is_admin == '1':
                form = ArticleForm(request.POST, error_class=DivErrorList, options=projects)
            else:
                form = ArticleForm(request.POST, error_class=DivErrorList)
            if form.is_valid():
                my_article = form.save(commit=False)
                if request.user.is_admin == '2':
                    my_article.project = Project.objects.get(id=int(request.user.project_id))
                my_article.save()
                return redirect('/projects/all_articles/?added=True')
            else:
                return render_to_response("add_article.html", {
                    "form": form,
                }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def edit_article(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        projects = Project.objects.all()
        myinstance = KnowledgeArticle.objects.get(id=int(pk))
        if request.method == 'GET':
            if request.user.is_admin == '1':
                form = ArticleForm(error_class=DivErrorList, instance=myinstance, options=projects)
            else:
                form = ArticleForm(error_class=DivErrorList, instance=myinstance)
            return render_to_response("add_article.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            if request.user.is_admin == '1':
                form = ArticleForm(request.POST or None, error_class=DivErrorList, instance=myinstance, options=projects)
            else:
                form = ArticleForm(request.POST or None, error_class=DivErrorList, instance=myinstance)
            if form.is_valid():
                my_projects = form.save(commit=False)
                my_projects.save()
                return redirect('/projects/all_articles/?edited=True')
            return render_to_response("add_article.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def confirm_delete_article(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myarticle = KnowledgeArticle.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('confirm_delete_article.html', {'id': pk,
                                                                      'myarticle': myarticle
                                                                      },
                                      context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def delete_article(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'POST':
            KnowledgeArticle.objects.get(id=int(pk)).delete()
            return redirect('/projects/all_articles/?deleted=True')
    else:
        raise Http404


@login_required
def delete_category(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'POST':
            CommentCategory.objects.get(id=int(pk)).delete()
            return render_to_response('404.html', context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def delete_link(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'POST':
            RelevantLink.objects.get(id=int(pk)).delete()
            return render_to_response('404.html', context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def view_article(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myarticle = KnowledgeArticle.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('detailed_article.html', {'id': pk, 'myarticle': myarticle,
                                                                 }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def add_category(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myratings = CommentCategory.objects.all()
        if request.method == 'POST':
            CommentCategory.objects.create(name=request.POST['name'],
                                           value=request.POST['value'],
                                          )
            return render_to_response('add_rating.html', {'myratings': myratings,
                                                                 }, context_instance=RequestContext(request))

        return render_to_response('add_rating.html', {'myratings': myratings,
                                                                 }, context_instance=RequestContext(request))            

    else:
        raise Http404



@login_required
def add_relevant_links(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        mylinks = RelevantLink.objects.all()
        if request.method == 'POST':
            RelevantLink.objects.create(title=request.POST['title'],
                                        link=request.POST['link'],
                                          )
            mylinks = RelevantLink.objects.all()
            return render_to_response('add_relevant_links.html', {'mylinks': mylinks,
                                                                 }, context_instance=RequestContext(request))

        return render_to_response('add_relevant_links.html', {'mylinks': mylinks,
                                                                 }, context_instance=RequestContext(request))

    else:
        raise Http404


@login_required
def add_issue_comment(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'GET':
            issues = Issue.objects.all()
            ratings = CommentCategory.objects.all()
            form = IssueCommentForm(error_class=DivErrorList, options=ratings, issues=issues)
            return render_to_response("add_comment.html", {
                "form": form,
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            issues = Issue.objects.all()
            ratings = CommentCategory.objects.all()
            form = IssueCommentForm(request.POST, error_class=DivErrorList, options=ratings, issues=issues)
            if form.is_valid():
                my_comment = form.save(commit=False)
                my_comment.author = request.user
                my_comment.save()
                return redirect('/projects/all_comments/?added=True')
            else:
                return render_to_response("add_comment.html", {
                    "form": form,
                }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def issue_comment_detail(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        mycomment = IssueComment.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('comment_detail.html', {'mycomment': mycomment,
                                                           }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def edit_issue_comment(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myinstance = IssueComment.objects.get(id=int(pk))
        if request.method == 'GET':
            issues = Issue.objects.all()
            ratings = CommentCategory.objects.all()
            form = IssueCommentForm(error_class=DivErrorList, instance=myinstance, options=ratings, issues=issues)
            return render_to_response("add_comment.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            issues = Issue.objects.all()
            ratings = CommentCategory.objects.all()
            form = IssueCommentForm(request.POST or None, error_class=DivErrorList, instance=myinstance, options=ratings, issues=issues)
            if form.is_valid():
                my_projects = form.save(commit=False)
                my_projects.save()
                return redirect('/projects/all_comments/?edited=True')
            return render_to_response("add_comment.html", {
                "form": form,
                'id': pk,
                'edit': 'True',
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def confirm_delete_comment(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        mycomment = IssueComment.objects.get(id=int(pk))
        if request.method == 'GET':
            return render_to_response('confirm_delete_comment.html', {'id': pk, 'mycomment': mycomment},
                                      context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def delete_comment(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'POST':
            IssueComment.objects.get(id=int(pk)).delete()
            return redirect('/projects/all_comments/?deleted=True')
    else:
        raise Http404


@login_required
def resolve_comment(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'POST':
            mycomment = IssueComment.objects.get(id=int(pk))
            mycomment.issue_resolved = True
            mycomment.save()
            return redirect('/projects/view_comment/%s' % pk)
    else:
        raise Http404


@login_required
def all_comments(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'GET':
            return render_to_response('all_comments.html', {
                'comments': IssueComment.objects.all().order_by('-id'),
                'ratings': CommentCategory.objects.all()
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def filter_rating(request, name):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'GET':
            return render_to_response('all_comments.html', {
                'comments': IssueComment.objects.filter(rating__name=name).order_by('-id'),
                'ratings': CommentCategory.objects.all()
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def filter_ok(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'GET':
            return render_to_response('all_comments.html', {
                'comments': IssueComment.objects.filter(rating__value__gt=2).order_by('-id'),
                'ratings': CommentCategory.objects.all(),
                'filter' : 'comments with rating above 2'            
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def filter_resolved(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'GET':
            return render_to_response('all_comments.html', {
                'comments': IssueComment.objects.filter(issue_resolved=True, rating__value__lt=3).order_by('-id'),
                'ratings': CommentCategory.objects.all(),
                'filter' : 'resolved comments'
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def filter_unresolved(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'GET':
            return render_to_response('all_comments.html', {
                'comments': IssueComment.objects.filter(issue_resolved=False).order_by('-id'),
                'ratings': CommentCategory.objects.all(),
                'filter' : 'unresolved comments'
            }, context_instance=RequestContext(request))
    else:
        raise Http404

@login_required
def view_comments(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'GET':
            return render_to_response('all_comments.html', {
                'comments': IssueComment.objects.filter(issue__id=int(pk)).order_by('-id'),
            }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def projects_visualisations(request):
    if request.user.is_admin == '1':
        if request.user.is_authenticated():
            projects = Project.objects.all()
            num_of_issues = Issue.objects.all().count()
            num_of_comments = IssueComment.objects.all().count()
            comment_graph = {}
            issue_graph = {}
            rating_graph = {}
            channel_graph = {
                    'Web': IssueComment.objects.filter(input_channel='Web').count(),
                    'SMS': IssueComment.objects.filter(input_channel='SMS').count(),
                    'Email': IssueComment.objects.filter(input_channel='Email').count(),
                    'WhatsApp': IssueComment.objects.filter(input_channel='WhatsApp').count(),
                    'Facebook': IssueComment.objects.filter(input_channel='Facebook').count(),
                    'Twitter': IssueComment.objects.filter(input_channel='Twitter').count(),
                    'Offline': IssueComment.objects.filter(input_channel='Offline').count(),
            }

            myratings = CommentCategory.objects.all()
            if myratings:
                for item in myratings:
                    rating_graph[item.name] = IssueComment.objects.filter(rating__name=item.name).count()

            if num_of_comments > 0:
                for item in projects:
                    number_of_comments = item.get_number_of_comments()
                    mykey = '%s (%s)' % (item.name, number_of_comments)
                    comment_graph[mykey] = (float(number_of_comments) / 100) * num_of_comments
            if num_of_issues > 0:
                for item in projects:
                    number_of_issues = item.get_number_of_issues()
                    mykey = '%s (%s)' % (item.name, number_of_issues)
                    issue_graph[mykey] = (float(number_of_issues) / 100) * num_of_issues
            num_of_unresolved = IssueComment.objects.filter(issue_resolved=False).count()
            num_of_resolved = IssueComment.objects.filter(issue_resolved=True, rating__value__lt=3).count()
            latest = IssueComment.objects.all().order_by('-id')[:5]
            return render(request, 'projects_visualisation.html', {
                          'latest': latest,
                          'num_of_projects': projects.count(),
                          'num_of_issues': num_of_issues,
                          'num_of_comments': num_of_comments,
                          'num_of_resolved': num_of_resolved,
                          'num_of_unresolved': num_of_unresolved,
                          'projects': projects,
                          'comment_graph': comment_graph,
                          'issue_graph': issue_graph,
                          'rating_graph': rating_graph,
                          'channel_graph': channel_graph
                          }
                          )
        redirect('/login/')


@login_required
def projects_visualisations_details(request, pk):
    if request.user.is_admin == '1':
        if request.user.is_authenticated():
            projects = Project.objects.all()
            num_of_issues = Issue.objects.filter(project__id=int(pk)).count()
            num_of_comments = IssueComment.objects.filter(issue__project__id=int(pk)).count()
            comment_graph = {}
            rating_graph = {}
            channel_graph = {
                    'Web': IssueComment.objects.filter(input_channel='Web', issue__project__id=int(pk)).count(),
                    'SMS': IssueComment.objects.filter(input_channel='SMS', issue__project__id=int(pk)).count(),
                    'Email': IssueComment.objects.filter(input_channel='Email', issue__project__id=int(pk)).count(),
                    'WhatsApp': IssueComment.objects.filter(input_channel='WhatsApp', issue__project__id=int(pk)).count(),
                    'Facebook': IssueComment.objects.filter(input_channel='Facebook', issue__project__id=int(pk)).count(),
                    'Twitter': IssueComment.objects.filter(input_channel='Twitter', issue__project__id=int(pk)).count(),
                    'Offline': IssueComment.objects.filter(input_channel='Offline', issue__project__id=int(pk)).count(),
            }

            myratings = CommentCategory.objects.all()
            myproject = Project.objects.get(id=int(pk))
            if myratings:
                for item in myratings:
                    rating_graph[item.name] = IssueComment.objects.filter(rating__name=item.name, issue__project__id=int(pk)).count()

            if num_of_comments > 0:
                number_of_comments = Project.objects.get(id=int(pk)).get_number_of_comments()
                mykey = '%s (%s)' % (item.name, number_of_comments)
                comment_graph[mykey] = (float(number_of_comments) / 100) * num_of_comments

            num_of_unresolved = IssueComment.objects.filter(issue_resolved=False, issue__project__id=int(pk)).count()
            num_of_resolved = IssueComment.objects.filter(issue_resolved=True, issue__project__id=int(pk), rating__value__lt=3).count()
            latest = IssueComment.objects.all().order_by('-id')[:5]
            return render(request, 'visual_projects.html', {
                          'latest': latest,
                          'num_of_projects': projects.count(),
                          'num_of_issues': num_of_issues,
                          'num_of_comments': num_of_comments,
                          'num_of_resolved': num_of_resolved,
                          'num_of_unresolved': num_of_unresolved,
                          'projects': projects,
                          'rating_graph': rating_graph,
                          'channel_graph': channel_graph
                          }
                          )
        redirect('/login/')


@login_required
def issues_visualisations(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.user.is_authenticated():
            issues = Issue.objects.all()
            num_of_issues = Issue.objects.all().count()
            num_of_comments = IssueComment.objects.all().count()
            comment_graph = {}
            rating_graph = {}
            channel_graph = {
                    'Web': IssueComment.objects.filter(input_channel='Web').count(),
                    'SMS': IssueComment.objects.filter(input_channel='SMS').count(),
                    'Email': IssueComment.objects.filter(input_channel='Email').count(),
                    'WhatsApp': IssueComment.objects.filter(input_channel='WhatsApp').count(),
                    'Facebook': IssueComment.objects.filter(input_channel='Facebook').count(),
                    'Twitter': IssueComment.objects.filter(input_channel='Twitter').count(),
                    'Offline': IssueComment.objects.filter(input_channel='Offline').count(),
            }
            num_of_unresolved = IssueComment.objects.filter(issue_resolved=False).count()
            num_of_resolved = IssueComment.objects.filter(issue_resolved=True, rating__value__lt=3).count()
            latest = IssueComment.objects.all().order_by('-id')[:5]

            myratings = CommentCategory.objects.all()
            if myratings:
                for item in myratings:
                    rating_graph[item.name] = IssueComment.objects.filter(rating__name=item.name).count()
            if request.user.is_admin == '2':
                issues = Issue.objects.filter(project__id=request.user.project_id)
                num_of_issues = Issue.objects.filter(project__id=request.user.project_id).count()
                num_of_comments = IssueComment.objects.all(issue__project__id=request.user.project_id).count()
                channel_graph = {
                    'Web': IssueComment.objects.filter(input_channel='Web', issue__project__id=request.user.project_id).count(),
                    'SMS': IssueComment.objects.filter(input_channel='SMS', issue__project__id=request.user.project_id).count(),
                    'Email': IssueComment.objects.filter(input_channel='Email', issue__project__id=request.user.project_id).count(),
                    'WhatsApp': IssueComment.objects.filter(input_channel='WhatsApp', issue__project__id=request.user.project_id).count(),
                    'Facebook': IssueComment.objects.filter(input_channel='Facebook', issue__project__id=request.user.project_id).count(),
                    'Twitter': IssueComment.objects.filter(input_channel='Twitter', issue__project__id=request.user.project_id).count(),
                    'Offline': IssueComment.objects.filter(input_channel='Offline', issue__project__id=request.user.project_id).count(),
                }
                if myratings:
                    for item in myratings:
                        rating_graph[item.name] = IssueComment.objects.filter(rating__name=item.name, issue__project__id=request.user.project_id).count()
                num_of_unresolved = IssueComment.objects.filter(issue_resolved=False, issue__project__id=request.user.project_id).count()
                num_of_resolved = IssueComment.objects.filter(issue_resolved=True, issue__project__id=request.user.project_id, rating__value__lt=3).count()
                latest = IssueComment.objects.filter(issue__project__id=request.user.project_id).order_by('-id')[:5]

            if num_of_comments > 0:
                for item in issues:
                    number_of_comments = item.num_of_comments()
                    mykey = '%s (%s)' % (item.title, number_of_comments)
                    comment_graph[mykey] = (float(number_of_comments) / 100) * num_of_comments

            return render(request, 'issues_visualisations.html', {
                          'latest': latest,
                          'num_of_issues': num_of_issues,
                          'num_of_comments': num_of_comments,
                          'num_of_resolved': num_of_resolved,
                          'num_of_unresolved': num_of_unresolved,
                          'issues': issues,
                          'comment_graph': comment_graph,
                          'rating_graph': rating_graph,
                          'channel_graph': channel_graph}
                          )
        redirect('/login/')


@login_required
def issues_visualisations_details(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.user.is_authenticated():
            issues = Issue.objects.all()
            num_of_comments = IssueComment.objects.filter(issue__id=int(pk)).count()
            rating_graph = {}
            channel_graph = {
                    'Web': IssueComment.objects.filter(input_channel='Web', issue__id=int(pk)).count(),
                    'SMS': IssueComment.objects.filter(input_channel='SMS', issue__id=int(pk)).count(),
                    'Email': IssueComment.objects.filter(input_channel='Email', issue__id=int(pk)).count(),
                    'WhatsApp': IssueComment.objects.filter(input_channel='WhatsApp', issue__id=int(pk)).count(),
                    'Facebook': IssueComment.objects.filter(input_channel='Facebook', issue__id=int(pk)).count(),
                    'Twitter': IssueComment.objects.filter(input_channel='Twitter', issue__id=int(pk)).count(),
                    'Offline': IssueComment.objects.filter(input_channel='Offline', issue__id=int(pk)).count(),
            }
            print channel_graph
            num_of_unresolved = IssueComment.objects.filter(issue_resolved=False, issue__id=int(pk)).count()
            num_of_resolved = IssueComment.objects.filter(issue_resolved=True, issue__id=int(pk), rating__value__lt=3).count()
            latest = IssueComment.objects.all().order_by('-id')[:5]

            myratings = CommentCategory.objects.all()
            if myratings:
                for item in myratings:
                    rating_graph[item.name] = IssueComment.objects.filter(issue__id=int(pk), rating__name=item.name).count()
            if request.user.is_admin == '2':
                issues = Issue.objects.filter(project__id=request.user.project_id)
                num_of_comments = IssueComment.objects.all(issue__id=int(pk), issue__project__id=request.user.project_id).count()
                channel_graph = {
                    'Web': IssueComment.objects.filter(input_channel='Web', issue__project__id=request.user.project_id, issue__id=int(pk)).count(),
                    'SMS': IssueComment.objects.filter(input_channel='SMS', issue__project__id=request.user.project_id, issue__id=int(pk)).count(),
                    'Email': IssueComment.objects.filter(input_channel='Email', issue__project__id=request.user.project_id, issue__id=int(pk)).count(),
                    'WhatsApp': IssueComment.objects.filter(input_channel='WhatsApp', issue__project__id=request.user.project_id, issue__id=int(pk)).count(),
                    'Facebook': IssueComment.objects.filter(input_channel='Facebook', issue__project__id=request.user.project_id, issue__id=int(pk)).count(),
                    'Twitter': IssueComment.objects.filter(input_channel='Twitter', issue__project__id=request.user.project_id, issue__id=int(pk)).count(),
                    'Offline': IssueComment.objects.filter(input_channel='Offline', issue__project__id=request.user.project_id, issue__id=int(pk)).count(),
                }
                print channel_graph
                if myratings:
                    for item in myratings:
                        rating_graph[item.name] = IssueComment.objects.filter(rating__name=item.name, issue__project__id=request.user.project_id, issue__id=int(pk)).count()
                num_of_unresolved = IssueComment.objects.filter(issue_resolved=False, issue__project__id=request.user.project_id, issue__id=int(pk)).count()
                num_of_resolved = IssueComment.objects.filter(issue_resolved=True, issue__project__id=request.user.project_id, issue__id=int(pk), rating__value__lt=3).count()
                latest = IssueComment.objects.filter(issue__project__id=request.user.project_id).order_by('-id')[:5]
            myissue = Issue.objects.get(id=int(pk))

            return render(request, 'visual_issues.html', {
                          'latest': latest,
                          'num_of_comments': num_of_comments,
                          'num_of_resolved': num_of_resolved,
                          'num_of_unresolved': num_of_unresolved,
                          'issues': issues,
                          'rating_graph': rating_graph,
                          'channel_graph': channel_graph,
                          'myissue': myissue
                          }
                          )
        redirect('/login/')


@login_required
def add_album(request):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        if request.method == 'GET':
            form = GalleryAlbumForm(error_class=DivErrorList)
            choice_formset_picture = ChoiceFormSetPicture(instance=GalleryAlbum())
            return render_to_response("add_album.html", {
                "form": form,
                'choice_formset_picture': choice_formset_picture,
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            form = GalleryAlbumForm(request.POST, error_class=DivErrorList)
            if form.is_valid():
                my_issue = form.save(commit=False)
                choice_formset_picture = ChoiceFormSetPicture(request.POST, instance=my_issue)
                if choice_formset_picture.is_valid():
                    my_issue.save()
                    choice_formset_picture.save()
                    return redirect('/projects/all_albums/?added=True')
                else:
                    return render_to_response("add_album.html", {
                        "form": form,
                    }, context_instance=RequestContext(request))
            else:
                return render_to_response("add_album.html", {
                    "form": form,
                }, context_instance=RequestContext(request))
    else:
        raise Http404


@login_required
def edit_album(request, pk):
    if request.user.is_admin == '1' or request.user.is_admin == '2':
        myinstance = GalleryAlbum.objects.get(id=int(pk))
        if request.method == 'GET':
            form = GalleryAlbumForm(error_class=DivErrorList, instance=myinstance)
            choice_formset_picture = ChoiceFormSetPicture(instance=myinstance)
            return render_to_response("add_album.html", {
                "form": form,
                'choice_formset_picture': choice_formset_picture,
                'id': pk,
                'edit': 'True'
            }, context_instance=RequestContext(request))

        if request.method == 'POST':
            myinstance = GalleryAlbum.objects.get(id=int(pk))
            form = GalleryAlbumForm(request.POST or None, instance=myinstance, error_class=DivErrorList)
            if form.is_valid():
                myinstance = form.save(commit=False)
                choice_formset_picture = ChoiceFormSetPicture(request.POST or None, instance=myinstance)
                if choice_formset_picture.is_valid():
                    myinstance.save()
                    choice_formset_picture.save()
                    return redirect('/projects/all_albums/?edited=True')
                else:
                    return render_to_response("add_album.html", {
                        "form": form,
                        'choice_formset_picture': choice_formset_picture
                    }, context_instance=RequestContext(request))
            else:
                choice_formset_picture = ChoiceFormSetPicture(instance=myinstance)

                return render_to_response("add_album.html", {
                    "form": form,
                    'choice_formset_picture': choice_formset_picture,
                    'id': pk,
                    'edit': 'True'
                }, context_instance=RequestContext(request))
