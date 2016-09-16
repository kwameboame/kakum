from django.shortcuts import render, redirect
from apps.users.forms import LoginForm, DivErrorList
from apps.users.models import KAKUser
from django.contrib.auth import login, authenticate, logout
from apps.projects.models import *
from django.core.mail import send_mail


def backend_home(request):
    if request.user.is_authenticated():
        return redirect('/users/dashboard/')
    next = request.GET.get('next')
    form = LoginForm()
    return render(request, 'home.html', {'form': form, 'next': next})


def frontend_home(request):
    issues = Issue.objects.filter(project__id=1).order_by('-id')[:3]
    document = KnowledgeDocument.objects.filter(project__id=1, show_on_homepage = True)[:4]
    return render(request,
                  'frontend_index.html',
                  {'issues': issues,
                   'document': document,
                   'relevant': RelevantLink.objects.all()
                   })


def about(request):
    return render(request, 'about.html')


def frontend_gallery_videos(request):
    videos = GalleryVideo.objects.all()
    return render(request, 'videos.html', {'videos': videos, 'relevant': RelevantLink.objects.all()})


def frontend_gallery_pictures(request):
    albums = GalleryAlbum.objects.all()
    return render(request, 'pictures.html', {'albums': albums, 'relevant': RelevantLink.objects.all()})


def frontend_documents(request):
    documents = KnowledgeDocument.objects.filter(project__id=1)
    return render(request, 'documents.html', {'documents': documents, 'relevant': RelevantLink.objects.all()})


def frontend_articles(request):
    articles = KnowledgeArticle.objects.filter(project__id=1).order_by('-date_published')
    return render(request, 'articles.html', {'articles': articles, 'relevant': RelevantLink.objects.all()})


def post_comment(request):
    if request.method == "POST":
        issue_id = request.POST['issue_id']
        comment = request.POST['comment']
        image = request.POST['image']
        video = request.POST['video']
        rating_id = request.POST['rating']
        media_url = request.POST.get('media_url', None)

        issue_resolved = True
        if CommentCategory.objects.get(id=int(rating_id)).value < 3:
            issue_resolved = False

        IssueComment.objects.create(issue=Issue.objects.get(id=int(issue_id)),
                                    image=image,
                                    video=video,
                                    comment=comment,
                                    input_channel='Web',
                                    author=request.user,
                                    media_url=media_url,
                                    issue_resolved=issue_resolved,
                                    rating=CommentCategory.objects.get(id=int(rating_id)))
        try:
            if CommentCategory.objects.get(id=int(rating_id)).value < 3:
                send_mail(
                    'New Issue Comment that needs attention',
                    comment,
                    'gidboa@gmail.com',
                    ['info@penplusbytes.org'],
                    fail_silently=False,
                )
        except:
            pass
        return redirect('/issues/%s' % issue_id)


def issues(request):
    issues = Issue.objects.filter(project__id=1)
    return render(request, 'issues.html', {'issues': issues, 'relevant': RelevantLink.objects.all()})


def issue_detail(request, pk):
    myissue = Issue.objects.get(id=int(pk))
    rating = CommentCategory.objects.all()
    videos = myissue.get_videos()
    images = myissue.get_images()
    documents = myissue.get_documents()
    return render(request, 'issue_detail_frontend.html', {'myissue': myissue,
                                                          'images': images,
                                                          'ratings': rating,
                                                          'documents': documents,
                                                          'relevant': RelevantLink.objects.all(),
                                                          'videos': videos})


def article_detail(request, pk):
    myarticle = KnowledgeArticle.objects.get(id=int(pk))
    myarticles = KnowledgeArticle.objects.all().order_by('-date_published').exclude(id=myarticle.id)[:4]
    return render(request, 'frontend_article_detail.html', {'myarticle': myarticle,'relevant': RelevantLink.objects.all(), 'myarticles': myarticles})


def login_view(request):
    next = request.GET.get('next')
    if request.user.is_authenticated():
        redirect('/issues/')

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
                return redirect('/issues/')
            else:
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})

    ''' user is not submitting any form, show the login form '''
    form = LoginForm()
    return render(request, 'login.html', {'form': form, 'next': next})


def register_view(request):
    next_param = request.GET.get('next')

    if request.user.is_authenticated():
        redirect('/issues/')

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        next_param = request.POST.get('next')

        try:
            KAKUser.objects.get(email=email)
            return render(request, 'register.html', {'next': next_param,
                                                     'error': 'Email Already Exist'
                                                     })
        except:
            user = KAKUser(
                email=email,
                username='username',
                first_name=first_name,
                last_name=last_name,
            )
            user.set_password(password)
            user.save()
            user = authenticate(email=user.email, password=password)
            login(request, user)
            if request.POST.get('next'):
                return redirect(request.POST.get('next'))
            return redirect('/issues/')

    return render(request, 'register.html', {'next': next_param})


def logout_view(request):
    logout(request)
    return redirect('/')


def google_register(request):

    if request.method == "POST":
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        image_url = request.POST.get('image_url')
        password = request.POST.get('password')

        try:
            KAKUser.objects.get(email=email)
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/issues/')
        except:
            user = KAKUser(
                email=email,
                username='username',
                first_name=first_name,
                last_name=last_name,
                sm_avatar=image_url
            )
            user.set_password(password)
            user.save()
            user = authenticate(email=user.email, password=password)
            login(request, user)
            return redirect('/issues/')

    return render(request, 'register.html')
