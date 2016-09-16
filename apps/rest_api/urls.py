from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from apps.rest_api.views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = patterns(
    '',
    url(r'^users/login/$', login_user),
    url(r'^projects/get_project_details/$', ProjectDetail.as_view()),
    url(r'^projects/get_issue_details/$', IssueDetail.as_view()),
    url(r'^projects/get_issues/$', GetIssues.as_view()),
    url(r'^issues/get_issue_comments/$', GetIssueComments.as_view()),
    url(r'^issues/post_issue_comment/$', PostIssueComment.as_view()),
    url(r'^issues/get_rating/$', GetCommentRating.as_view()),
    url(r'^projects/get_knowledge_audios/$', MyKnowledgeAudio.as_view()),
    url(r'^projects/get_knowledge_videos/$', MyKnowledgeVideo.as_view()),
    url(r'^projects/get_knowledge_articles/$', MyKnowledgeArticle.as_view()),
    url(r'^projects/get_knowledge_documents/$', MyKnowledgeDocument.as_view()),
    url(r'^users/signup/$', UserSignUp.as_view()),
    url(r'^users/me/$', CurrentUserProfile.as_view()),
    # url(r'^users/upload-avatar/$', UserAvatar.as_view()),
    url(r'^users/get-auth-token/$', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^', include(router.urls)),
)
