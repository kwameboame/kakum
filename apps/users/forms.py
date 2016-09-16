from models import *
from apps.projects.models import Project
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms.utils import ErrorList
from django.contrib.auth import authenticate
from django.contrib.auth.forms import SetPasswordForm
from django.utils.datastructures import SortedDict


class DivErrorList(ErrorList):

    def __unicode__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return u''
        return u'%s' % ''.join([u'%s' % e for e in self])


class LoginForm(forms.Form):
    email = forms.CharField(label=(u'Email'),widget=forms.TextInput(attrs={'class':'form-control input-lg', 'data-parsley-type': 'email', 'placeholder': 'Email',}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': "form-control input-lg"}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(email=email,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError('invalid_login')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('inactive')
        return self.cleaned_data


class UserSettingForm(forms.ModelForm):
    class Meta:
        model = KAKUser
        fields = ['email', 'first_name', 'last_name', 'username']
        widgets = {
            'email': forms.TextInput(attrs={
                    'class':"form-control",
                    'maxlength':"100",
                }),
            'first_name': forms.TextInput(attrs={
                    'class':"form-control",
                    'maxlength':"50",
                }),
            'last_name': forms.TextInput(attrs={
                    'class':"form-control",
                    'maxlength':"50",
                }),
            'username': forms.TextInput(attrs={
                    'class':"form-control",
                    'maxlength':"50",
                }),
        }


class PasswordChangeForm(SetPasswordForm):
    """
    A form that lets a user change his/her password by entering
    their old password.
    """
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': _("Your old password was entered incorrectly. "
                                "Please enter it again."),
    })
    old_password = forms.CharField(label=_("Old password"),
                                   widget=forms.PasswordInput(render_value=False, attrs={'class':'form-control','placeholder': 'Old Password'}))
    new_password1 = forms.CharField(label=_("New password1"),
                                   widget=forms.PasswordInput(render_value=False, attrs={'class':'form-control','placeholder': 'Password'}))
    new_password2 = forms.CharField(label=_("New password2"),
                                   widget=forms.PasswordInput(render_value=False, attrs={'class':'form-control','placeholder': 'Confirm Password'}))

    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password

PasswordChangeForm.base_fields = SortedDict([
    (k, PasswordChangeForm.base_fields[k])
    for k in ['old_password', 'new_password1', 'new_password2']
])


class AdminEditForm(forms.ModelForm):

    STATUS_TYPES = (
        ('1', 'Super User'),
        ('2', 'Staff User'),
    )

    def __init__(self, *args, **kwargs):
        myproject = kwargs.pop('options')
        super(AdminEditForm, self).__init__(*args, **kwargs)
        self.fields['project'] = forms.ModelChoiceField(queryset=myproject, required=True, widget=forms.Select(attrs={'class': "form-control"}))

    project = forms.ModelChoiceField(queryset=Project.objects.none(),
                                     required=True,
                                     widget=forms.Select(attrs={'class': "form-control"}))

    is_admin = forms.ChoiceField(widget=forms.Select(attrs={'class' : "form-control",}), choices=STATUS_TYPES)

    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs=
        {'placeholder': 'e.g user@python.com', 'class' : "form-control",}))

    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs=
        {'placeholder': 'E.g. BEN001', 'class' : "form-control",}))

    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs=
        {'placeholder': 'Enter Firstname Here', 'class' : "form-control", }))

    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs=
        {'placeholder': 'Enter Last Name Here', 'class' : "form-control", }))

    class Meta:
        exclude = ('date_created', 'password', 'is_active', 'project_id')
        model = KAKUser


class AdminForm(forms.ModelForm):

    STATUS_TYPES = (
        ('1', 'Super User'),
        ('2', 'Staff User'),
    )

    def __init__(self, *args, **kwargs):
        myproject = kwargs.pop('options')
        super(AdminForm, self).__init__(*args, **kwargs)
        self.fields['project'] = forms.ModelChoiceField(queryset=myproject, required=True, widget=forms.Select(attrs={'class': "form-control"}))

    project = forms.ModelChoiceField(queryset=Project.objects.none(),
                                     required=True,
                                     widget=forms.Select(attrs={'class': "form-control"}))

    is_admin = forms.ChoiceField(widget=forms.Select(attrs={'class' : "form-control",}), choices=STATUS_TYPES)

    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs=
        {'placeholder': 'e.g user@python.com', 'class' : "form-control",}))

    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs=
        {'placeholder': 'E.g. BEN001', 'class' : "form-control",}))

    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs=
        {'placeholder': 'Enter Firstname Here', 'class' : "form-control", }))

    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs=
        {'placeholder': 'Enter Last Name Here', 'class' : "form-control", }))

    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': "form-control input-lg"}))

    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': "form-control input-lg"}))

    class Meta:
        exclude = ('date_created', 'is_active', 'project_id')
        model = KAKUser

    def clean_password(self):
        if 'password' in self.cleaned_data and 'password1' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password1']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data['password']

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            KAKUser.objects.get(username=username)
        except KAKUser.DoesNotExist:
            return username
        raise forms.ValidationError("This username has been assigned already, please select another.")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = KAKUser.objects.get(email=email)
            raise forms.ValidationError(u'Email "%s" is already in use.' % email)
        except KAKUser.DoesNotExist:
            return email

    def save(self, commit=True):
        user = super(AdminForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.project_id = Project.objects.get(name=self.cleaned_data['project']).id
        if commit:
            user.save()
        return user
