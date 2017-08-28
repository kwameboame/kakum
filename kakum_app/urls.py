from django.conf.urls import include, url, handler404, handler500
from django.contrib.auth import views as kakum_app_views
from apps.projects import views as kakum_app_views
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = [
    url(r'^$', 'kakum_app.views.frontend_home', name='frontend_home'),
    url(r'^backend/$', 'kakum_app.views.backend_home', name='backend_home'),
    url(r'^gallery/videos/$', 'kakum_app.views.frontend_gallery_videos', name='frontend_videos'),
    url(r'^gallery/pictures/$', 'kakum_app.views.frontend_gallery_pictures', name='frontend_pictures'),
    url(r'^user_login/$', 'kakum_app.views.login_view', name='login_view'),
    url(r'^user_logout/$', 'kakum_app.views.logout_view', name='logout_view'),
    url(r'^google_register/$', 'kakum_app.views.google_register', name='google_register'),
    url(r'^post_comment/$', 'kakum_app.views.post_comment', name='post_comment'),
    url(r'^user_register/$', 'kakum_app.views.register_view', name='register_view'),
    # url(r'^knowledge_center/audios/$', 'kakum_app.views.frontend_audios', name='frontend_audios'),
    url(r'^knowledge_center/articles/$', 'kakum_app.views.frontend_articles', name='frontend_articles'),
    url(r'^knowledge_center/documents/$', 'kakum_app.views.frontend_documents', name='frontend_documents'),
    url(r'^issues/(?P<pk>\d+)/$', 'kakum_app.views.issue_detail', name='issue_detail'),
    url(r'^articles/(?P<pk>\d+)/$', 'kakum_app.views.article_detail', name='article_detail'),
    url(r'^issues/$', 'kakum_app.views.issues', name='issues'),
    url(r'^about/$', 'kakum_app.views.about', name='about'),
    url(r'^users/', include('apps.users.urls')),

    url(r'^projects/', include('apps.projects.urls')),
    url(r'^login/$', 'apps.users.views.login_view', name="login"),
    url(r'^s3direct/', include('s3direct.urls')),
    url(r'^api/v1.0/', include('apps.rest_api.urls', namespace='api')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^tinymce/', include('tinymce.urls')),

    #python social auth things
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

    #change password
    url(r'^password_change/$', 'apps.users.views.password_change', name='password_change'),
    url(r'^password_change_done/$', 'apps.users.views.password_change_done', name='password_change_done'),

    #password change
    url(r'^resetpassword/passwordsent/$','django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^resetpassword/$','django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$','django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$','django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^direct/$', TemplateView.as_view, {'template': 'direct.html','extra_context':{'showDirect':True}}),
]

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
        )

handler404 = 'apps.users.views.handler404'

handler500 = 'apps.users.views.handler500'
