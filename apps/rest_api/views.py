from rest_framework import viewsets
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import (HTTP_201_CREATED,
                                   HTTP_200_OK,
                                   HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND)
from apps.users.models import KAKUser
from apps.rest_api.serializers import *
from apps.projects.models import *
from rest_framework.pagination import PageNumberPagination


@api_view(['POST'])
@permission_classes((AllowAny,))
def login_user(request):
    """
    Email Login

    PARAMETERS

    email = Email of User
    
    password = Password

    """
    email = request.DATA.get('email', None)
    password = request.DATA.get('password', None)

    user = authenticate(email=email, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            user = UserSerializer(user)
            return Response(user.data, status=HTTP_200_OK)
        else:
            return Response({'detail': 'This account has been deactivated'}, status=HTTP_404_NOT_FOUND)
    else:
        return Response({'detail': 'Invalid email or password'}, status=HTTP_404_NOT_FOUND)


class UserSignUp(APIView):
    model = get_user_model()
    permission_classes = (AllowAny, )

    def post(self, request):
        """
        Email Sign Up

        PARAMETERS

        email = Email of User
        first_name = First Name of user
        last_name = Last Name of user
        password = Password

        """
        email = request.DATA.get('email', None)
        password = request.DATA.get('password', None)
        first_name = request.DATA.get('first_name', None)
        last_name = request.DATA.get('last_name', None)

        try:
            if email is not None and password is not None\
                    and first_name is not None\
                    and last_name is not None:

                user = KAKUser(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    username=email,
                )

                user.set_password(password)

                user.save()
                user = authenticate(email=user.email, password=password)
                login(request, user)

                user = UserSerializer(user)

                return Response(user.data, status=HTTP_201_CREATED)
            else:
                return Response({'detail': 'Please supply required parameters'}, status=HTTP_400_BAD_REQUEST)
        except:
            return Response({'detail': 'Email exist already'}, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_user(request):
    try:
        logout(request)
        return Response({'results': 'You have been successfully logged out'}, status=HTTP_200_OK)
    except:
        return Response({'detail': 'Sorry could not log you out'}, status=HTTP_400_BAD_REQUEST)


class CurrentUserProfile(APIView):

    def get(self, request, *args, **kwargs):
        user = request.user
        try:
            user = UserSerializer(user, context={'request': request})
            return Response({'me': user.data}, status=HTTP_200_OK)
        except:
            user = UserSerializer(user)
            return Response(user.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        user = request.user
        profile = request.DATA
        try:
            serializer = UserSerializer(user, context={'request': request}, data=profile, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({'results': serializer.data}, status=HTTP_200_OK)
        except:
            serializer = UserSerializer(profile, context={'request': request})
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserSocialSignUp(APIView):
    model = get_user_model()
    permission_classes = (AllowAny, )

    def post(self, request):
        """
        Social Media Sign Up

        PARAMETERS

        email = Email of User
        first_name = First Name of user
        last_name = Last Name of user
        profile_pic_url = Profile Pic Url

        """
        email = request.DATA.get('email', None)
        first_name = request.DATA.get('first_name', None)
        last_name = request.DATA.get('last_name', None)
        profile_pic_url = request.DATA.get('profile_pic_url', None)

        try:
            user = KAKUser.objects.get(email=email)
            user = UserSerializer(user)
            return Response(user.data, status=HTTP_200_OK)
        except KAKUser.DoesNotExist:
            if email is not None and first_name is not None\
                    and last_name is not None:
                try:
                    user = KAKUser(
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        sm_avatar=profile_pic_url,
                    )

                    user.save()
                    user = UserSerializer(user)

                    return Response(user.data, status=HTTP_201_CREATED)
                except:
                    return Response({'detail': 'User already exists'}, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'detail': 'Please supply required parameters'}, status=HTTP_400_BAD_REQUEST)#


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Fetches the details of a user

    """
    model = get_user_model()
    serializer_class = UserSerializer
    queryset = KAKUser.objects.all()


class ProjectDetail(APIView):

  def post(self, request, *args, **kwargs):
    """
    Fetches the details of a project

    PARAMETER

    project_id = ID of the project you are interested in

    """
    project_id = request.data.get('project_id', None)
    myproject = Project.objects.get(id=int(project_id))
    myprojects = ProjectSerializer(myproject, many=False)
    return Response({'results': myprojects.data}, status=HTTP_200_OK)


class IssueDetail(APIView):

  def post(self, request, *args, **kwargs):
    """
    Fetches the details of an issue

    PARAMETER

    issue_id = ID of the project you are interested in

    """
    issue_id = request.data.get('issue_id', None)
    myissue = Issue.objects.get(id=int(issue_id))
    myissues = IssueSerializer(myissue, many=False)
    return Response({'results': myissues.data}, status=HTTP_200_OK)



class GetIssues(APIView):

  def post(self, request, *args, **kwargs):
    """
    Fetches all issues of a project

    PARAMETER

    project_id = ID of the project you are interested in

    """
    project_id = request.data.get('project_id', None)
    myqueryset = Issue.objects.filter(project__id=int(project_id))
    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(myqueryset, request)
    serializer = IssueSerializer(result_page, context={'request': request}, many=True)
    return paginator.get_paginated_response(serializer.data)


class GetCommentRating(APIView):

  def post(self, request, *args, **kwargs):
    """
    Fetches comment rating types of an issue. This should be displayed to a user when commenting on a particular issue. It is issue specific

    PARAMETER

    issue_id = ID of an issue

    """
    issue_id = request.data.get('issue_id', None)
    myissue = CommentCategory.objects.filter(issue__id=int(issue_id))
    myissues = CommentCategorySerializer(myissue, many=True)
    return Response({'results': myissues.data}, status=HTTP_200_OK)


class GetIssueComments(APIView):

  def post(self, request, *args, **kwargs):
    """
    Fetches comments of an issue

    PARAMETER

    issue_id = ID of an issue

    """
    issue_id = request.data.get('issue_id', None)
    myqueryset = IssueComment.objects.filter(issue__id=int(issue_id))
    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(myqueryset, request)
    serializer = IssueCommentSerializer(result_page, context={'request': request}, many=True)
    return paginator.get_paginated_response(serializer.data)


class PostIssueComment(APIView):

  def post(self, request, *args, **kwargs):
    """
    Post a Comment for an isue

    PARAMETER

    issue_id = ID of an issue

    comment = Comment

    rating_id = Comment Category ID ( this should be fetched with /issues/get_comment_rating/ )

    """
    issue_id = request.data.get('issue_id', None)
    comment = request.data.get('comment', None)
    rating_id = request.data.get('rating_id', None)
    myqueryset = IssueComment.objects.create(issue=Issue.objects.get(id=int(issue_id)),
                                             comment=comment,
                                             author=request.user,
                                             rating_value=CommentCategory.objects.get(id=int(rating_id)))
    myissues = IssueCommentSerializer(myqueryset, many=False)
    return Response({'results': myissues.data}, status=HTTP_200_OK)


class MyKnowledgeAudio(APIView):

  def post(self, request, *args, **kwargs):
    """
    Fetch Audios from Knowledge Center

    PARAMETER

    project_id = ID of the project

    """
    project_id = request.data.get('project_id', None)
    myqueryset = KnowledgeAudio.objects.filter(project__id=int(project_id))
    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(myqueryset, request)
    serializer = AudioSerializer(result_page, context={'request': request}, many=True)
    return paginator.get_paginated_response(serializer.data)


class MyKnowledgeVideo(APIView):

  def post(self, request, *args, **kwargs):
    """
    Fetch Videos from Knowledge Center

    PARAMETER

    project_id = ID of the project

    """
    project_id = request.data.get('project_id', None)
    myqueryset = KnowledgeVideo.objects.filter(project__id=int(project_id))
    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(myqueryset, request)
    serializer = VideoSerializer(result_page, context={'request': request}, many=True)
    return paginator.get_paginated_response(serializer.data)


class MyKnowledgeArticle(APIView):

  def post(self, request, *args, **kwargs):
    """
    Fetch Articles from Knowledge Center

    PARAMETER

    project_id = ID of the project

    """
    project_id = request.data.get('project_id', None)
    myqueryset = KnowledgeArticle.objects.filter(project__id=int(project_id))
    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(myqueryset, request)
    serializer = ArticleSerializer(result_page, context={'request': request}, many=True)
    return paginator.get_paginated_response(serializer.data)


class MyKnowledgeDocument(APIView):

  def post(self, request, *args, **kwargs):
    """
    Fetch Documents from Knowledge Center

    PARAMETER

    project_id = ID of the project

    """
    project_id = request.data.get('project_id', None)
    myqueryset = KnowledgeDocument.objects.filter(project__id=int(project_id))
    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(myqueryset, request)
    serializer = DocumentSerializer(result_page, context={'request': request}, many=True)
    return paginator.get_paginated_response(serializer.data)
