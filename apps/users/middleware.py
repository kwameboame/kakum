from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from django.shortcuts import render
from social.exceptions import AuthCanceled


class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if type(exception) == AuthCanceled:
            return render(request, "login.html", {'cancelled': 'True'})
        else:
            pass
