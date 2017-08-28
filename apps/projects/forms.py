from .models import *
from django import forms
from django.forms.utils import ErrorList
from django.forms import widgets
from apps.projects.models import *
from s3direct.widgets import S3DirectWidget
from django.forms.models import inlineformset_factory
from bootstrap3_datetime.widgets import DateTimePicker
from tinymce.widgets import TinyMCE


class CustomDateInput(widgets.TextInput):
    input_type = 'date'


class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return u''
        return u'%s' % ''.join([u'%s' % e for e in self])


class ProjectForm(forms.ModelForm):

    name = forms.CharField(widget=widgets.TextInput(attrs=
        {'placeholder': 'Project Name', 'class': "form-control", }))

    description = forms.CharField(required=True, widget=forms.Textarea(attrs=
        {'placeholder': 'Description of Project here', 'class' : "form-control", }))

    image = forms.URLField(required=False, widget=S3DirectWidget(dest='imgs'))

    class Meta:
        exclude = ('date_created', )
        model = Project


class IssueForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        myproject = kwargs.pop('options')
        super(IssueForm, self).__init__(*args, **kwargs)
        self.fields['project'] = forms.ModelChoiceField(queryset=myproject, required=True, widget=forms.Select(attrs=
        {'class': "form-control"}))

    project = forms.ModelChoiceField(queryset=Project.objects.none(),
                                     required=True,
                                     widget=forms.Select(attrs={'class': "form-control"}))

    title = forms.CharField(widget=widgets.TextInput(attrs=
        {'placeholder': 'Issue Title', 'class': "form-control", }))

    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 15, 'class': "form-control"}))

    class Meta:
        exclude = ('author', 'date_created',)
        model = Issue


class IssueAdminForm(forms.ModelForm):

    title = forms.CharField(widget=widgets.TextInput(attrs=
        {'placeholder': 'Issue Title', 'class': "form-control", }))

    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 15, 'class': "form-control"}))

    class Meta:
        exclude = ('author', 'project', 'date_created',)
        model = Issue


MAX_CHOICES = 3

ChoiceFormSetVideo = inlineformset_factory(Issue,
                IssueVideo,
                can_delete=False,
                extra=MAX_CHOICES,
                exclude=('date_created',),
                widgets={'video': forms.URLField(widget=S3DirectWidget(dest='vids')),
                }
            )


ChoiceFormSetImage = inlineformset_factory(Issue,
                    IssueImage,
                    can_delete=False,
                    extra=MAX_CHOICES,
                    exclude=('date_created',),
                    widgets={'image': forms.URLField(widget=S3DirectWidget(dest='imgs')),
                    }
                )


ChoiceFormSetDocument = inlineformset_factory(Issue,
                    IssueDocument,
                    can_delete=False,
                    extra=MAX_CHOICES,
                    exclude=('date_created', 'media_url'),
                    widgets={'document': forms.URLField(widget=S3DirectWidget(dest='docs')),
                             'cover_image': forms.URLField(widget=S3DirectWidget(dest='imgs')),
                             'title': widgets.TextInput(attrs={'class': "form-control", }),
                    }
                )


class CommentCategoryForm(forms.ModelForm):

    name = forms.CharField(widget=widgets.TextInput(attrs=
        {'placeholder': 'Name', 'class': "form-control", }))

    value = forms.IntegerField(required=True, widget=forms.TextInput(attrs=
        {'placeholder': 'Value', 'class': "form-control", }))

    class Meta:
        fields = ('name', 'value')
        model = CommentCategory


class DocumentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        myproject = kwargs.pop('options')
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['project'] = forms.ModelChoiceField(queryset=myproject, required=True, widget=forms.Select(attrs={'class': "form-control"}))

    project = forms.ModelChoiceField(queryset=Project.objects.none(),
                                     required=True,
                                     widget=forms.Select(attrs={'class': "form-control"}))

    title = forms.CharField(widget=widgets.TextInput(attrs=
        {'placeholder': 'Document Title', 'class': "form-control", }))

    description = forms.CharField(required=True, widget=forms.Textarea(attrs=
        {'placeholder': 'Description of Document', 'class': "form-control", }))

    document = forms.URLField(required=False, widget=S3DirectWidget(dest='docs'))

    cover_image = forms.URLField(required=False, widget=S3DirectWidget(dest='imgs'))

    media_url = forms.URLField(required=False, widget=widgets.Textarea(attrs=
        {'placeholder': 'Paste download link, if media is external', 'class': "form-control", }))

    class Meta:
        exclude = ('date_created',)
        model = KnowledgeDocument


class DocumentAdminForm(forms.ModelForm):

    title = forms.CharField(widget=widgets.TextInput(attrs=
        {'placeholder': 'Document Title', 'class': "form-control", }))

    description = forms.CharField(required=True, widget=forms.Textarea(attrs=
        {'placeholder': 'Description of Document', 'class' : "form-control", }))

    document = forms.URLField(required=False, widget=S3DirectWidget(dest='docs'))

    media_url = forms.URLField(required=False, widget=widgets.Textarea(attrs=
        {'placeholder': 'Paste download link, if media is external', 'class': "form-control", }))

    class Meta:
        exclude = ('date_created', 'project')
        model = KnowledgeDocument


class GalleryVideoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        myproject = kwargs.pop('options')
        super(GalleryVideoForm, self).__init__(*args, **kwargs)
        self.fields['project'] = forms.ModelChoiceField(queryset=myproject, required=True, widget=forms.Select(attrs={'class': "form-control"}))

    project = forms.ModelChoiceField(queryset=Project.objects.none(),
                                     required=True,
                                     widget=forms.Select(attrs={'class': "form-control"}))

    title = forms.CharField(widget=widgets.TextInput(attrs=
        {'placeholder': 'Video Title', 'class': "form-control", }))

    description = forms.CharField(required=True, widget=forms.Textarea(attrs=
        {'placeholder': 'Description of Video', 'class' : "form-control", }))

    video = forms.URLField(required=False, widget=S3DirectWidget(dest='vids'))

    image = forms.URLField(required=False, widget=S3DirectWidget(dest='imgs'))

    media_url = forms.CharField(required=False, widget=widgets.Textarea(attrs=
        {'placeholder': 'Paste youtube embed code if applicable', 'class': "form-control", }))

    class Meta:
        exclude = ('date_created',)
        model = GalleryVideo


class GalleryVideoAdminForm(forms.ModelForm):

    title = forms.CharField(widget=widgets.TextInput(attrs=
        {'placeholder': 'Video Title', 'class': "form-control", }))

    description = forms.CharField(required=True, widget=forms.Textarea(attrs=
        {'placeholder': 'Description of Video', 'class' : "form-control", }))

    video = forms.URLField(required=False, widget=S3DirectWidget(dest='vids'))

    media_url = forms.CharField(required=False, widget=widgets.Textarea(attrs=
        {'placeholder': 'Paste youtube embed code if applicable', 'class': "form-control", }))

    class Meta:
        exclude = ('date_created', 'project')
        model = GalleryVideo



class GalleryPictureForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        myproject = kwargs.pop('options')
        super(GalleryPictureForm, self).__init__(*args, **kwargs)
        self.fields['project'] = forms.ModelChoiceField(queryset=myproject, required=True, widget=forms.Select(attrs={'class': "form-control"}))

    project = forms.ModelChoiceField(queryset=Project.objects.none(),
                                     required=True,
                                     widget=forms.Select(attrs={'class': "form-control"}))

    title = forms.CharField(widget=widgets.TextInput(attrs=
        {'placeholder': 'Picture Title', 'class': "form-control", }))

    description = forms.CharField(required=True, widget=forms.Textarea(attrs=
        {'placeholder': 'Description of picture', 'class' : "form-control", }))

    image = forms.URLField(required=False, widget=S3DirectWidget(dest='imgs'))

    class Meta:
        exclude = ('date_created',)
        model = GalleryPicture



class GalleryPictureAdminForm(forms.ModelForm):

    title = forms.CharField(widget=widgets.TextInput(attrs=
        {'placeholder': 'Document Title', 'class': "form-control", }))

    description = forms.CharField(required=True, widget=forms.Textarea(attrs=
        {'placeholder': 'Description of Document', 'class' : "form-control", }))

    image = forms.URLField(required=False, widget=S3DirectWidget(dest='imgs'))

    class Meta:
        exclude = ('date_created', 'project',)
        model = GalleryPicture


class ArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        myproject = kwargs.pop('options')
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['project'] = forms.ModelChoiceField(queryset=myproject, required=True, widget=forms.Select(attrs={'class': "form-control"}))

    project = forms.ModelChoiceField(queryset=Project.objects.none(),
                                     required=True,
                                     widget=forms.Select(attrs={'class': "form-control"}))

    title = forms.CharField(widget=widgets.TextInput(attrs=
        {'placeholder': 'Article Title', 'class': "form-control", }))

    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 15, 'class': "form-control"}))

    image = forms.URLField(required=False, widget=S3DirectWidget(dest='imgs'))

    media_url = forms.URLField(required=False, widget=widgets.Textarea(attrs=
        {'placeholder': 'Paste link, if media is external', 'class': "form-control", }))

    date_published = forms.DateField(required=True, widget=DateTimePicker(options={"format": "YYYY-MM-DD"}))

    class Meta:
        fields = ['date_published', 'image', 'media_url', 'description', 'title', 'project']
        model = KnowledgeArticle
        date_publishedOptions = {
            'format': 'dd/mm/yyyy',
            'autoclose': True,
            'showMeridian' : True,
            'todayBtn': True,
        }


class ArticleAdminForm(forms.ModelForm):

    title = forms.CharField(widget=widgets.TextInput(attrs=
        {'placeholder': 'Article Title', 'class': "form-control", }))

    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 15, 'class': "form-control"}))

    image = forms.URLField(required=False, widget=S3DirectWidget(dest='imgs'))

    media_url = forms.URLField(required=False, widget=widgets.Textarea(attrs=
        {'placeholder': 'Paste link, if media is external', 'class': "form-control", }))

    date_published = forms.DateField(required=True, widget=DateTimePicker(options={"format": "YYYY-MM-DD"}))

    class Meta:
        exclude = ('project', )
        model = KnowledgeArticle
        date_publishedOptions = {
            'format': 'dd/mm/yyyy',
            'autoclose': True,
            'showMeridian': True,
            'todayBtn': True,
        }


class AudioForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        myproject = kwargs.pop('options')
        super(AudioForm, self).__init__(*args, **kwargs)
        self.fields['project'] = forms.ModelChoiceField(queryset=myproject, required=True, widget=forms.Select(attrs={'class': "form-control"}))

    project = forms.ModelChoiceField(queryset=Project.objects.none(),
                                     required=True,
                                     widget=forms.Select(attrs={'class': "form-control"}))

    title = forms.CharField(widget=widgets.TextInput(attrs=
        {'placeholder': 'Article Title', 'class': "form-control", }))

    description = forms.CharField(required=True, widget=forms.Textarea(attrs=
        {'placeholder': 'Description of Article', 'class': "form-control", }))

    audio = forms.URLField(required=False, widget=S3DirectWidget(dest='audios'))

    media_url = forms.CharField(required=False, widget=widgets.Textarea(attrs=
        {'placeholder': 'Paste youtube embed code if applicable', 'class': "form-control", }))

    class Meta:
        exclude = ('date_created',)
        model = KnowledgeAudio


class AudioAdminForm(forms.ModelForm):

    title = forms.CharField(widget=widgets.TextInput(attrs=
        {'placeholder': 'Article Title', 'class': "form-control", }))

    description = forms.CharField(required=True, widget=forms.Textarea(attrs=
        {'placeholder': 'Description of Article', 'class': "form-control", }))

    audio = forms.URLField(required=False, widget=S3DirectWidget(dest='audios'))

    media_url = forms.CharField(required=False, widget=widgets.Textarea(attrs=
        {'placeholder': 'Paste youtube embed code if applicable', 'class': "form-control", }))

    class Meta:
        exclude = ('date_created', 'project')
        model = KnowledgeAudio


class IssueCommentForm(forms.ModelForm):

    MYCHOICES = (
                 ('Web', 'Web'),
                 ('SMS', 'SMS'),
                 ('Email', 'Email'),
                 ('WhatsApp', 'WhatsApp'),
                 ('Facebook', 'Facebook'),
                 ('Twitter', 'Twitter'),
                 ('Offline', 'Offline'),
    )

    TYPE = (
            ('Complaint', 'Complaint'),
            ('Suggestion', 'Suggestion'),
            ('Endorsement', 'Endorsement'),
            ('Irrelevant', 'Irrelevant'),
    )

    def __init__(self, *args, **kwargs):
        myrating = kwargs.pop('options')
        myissues = kwargs.pop('issues')
        super(IssueCommentForm, self).__init__(*args, **kwargs)
        self.fields['rating'] = forms.ModelChoiceField(queryset=myrating,
                                                       required=True,
                                                       widget=forms.Select(attrs={'class': "form-control"}))

        self.fields['issue'] = forms.ModelChoiceField(queryset=myissues,
                                                      required=True,
                                                      widget=forms.Select(attrs={'class': "form-control"}))

    issue = forms.ModelChoiceField(queryset=Issue.objects.none(),
                                   required=True,
                                   widget=forms.Select(attrs={'class': "form-control"}))

    rating = forms.ModelChoiceField(queryset=CommentCategory.objects.none(),
                                    required=True,
                                    widget=forms.Select(attrs={'class': "form-control"}))

    comment = forms.CharField(required=True, widget=forms.Textarea(attrs=
        {'placeholder': 'Comment', 'class': "form-control", }))

    audio = forms.URLField(required=False, widget=S3DirectWidget(dest='audios'))

    image = forms.URLField(required=False, widget=S3DirectWidget(dest='imgs'))

    video = forms.URLField(required=False, widget=S3DirectWidget(dest='vids'))

    media_url = forms.CharField(required=False, widget=widgets.Textarea(attrs=
        {'placeholder': 'Paste youtube embed code if applicable', 'class': "form-control", }))

    input_channel = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': "form-control", 'data-parsley-group':"wizard-step-1"}), choices=MYCHOICES)

    comment_type = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': "form-control", 'data-parsley-group':"wizard-step-1"}), choices=TYPE)

    location = forms.CharField(required=False, widget=widgets.TextInput(attrs=
        {'placeholder': 'e.g. Adenta', 'class': "form-control", }))

    latitude = forms.CharField(required=False, widget=widgets.TextInput(attrs=
        {'placeholder': 'e.g. -0.45', 'class': "form-control", }))

    longitude = forms.CharField(required=False, widget=widgets.TextInput(attrs=
        {'placeholder': 'e.g. -0.45', 'class': "form-control", }))

    class Meta:
        exclude = ('author', 'timestamp')
        model = IssueComment


class RelevantLinkForm(forms.ModelForm):

    title = forms.CharField(widget=widgets.TextInput(attrs=
        {'placeholder': 'Issue Title', 'class': "form-control", }))

    link = forms.CharField(required=True, widget=forms.TextInput(attrs=
        {'placeholder': 'Link', 'class': "form-control", }))

    class Meta:
        fields = ['title', 'link', ]
        model = RelevantLink


MAX_CHOICES = 15


class GalleryAlbumForm(forms.ModelForm):

    title = forms.CharField(widget=widgets.TextInput(attrs={'placeholder': 'Album Title', 'class': "form-control", }))

    class Meta:
        exclude = ('date_created',)
        model = GalleryAlbum


ChoiceFormSetPicture = inlineformset_factory(GalleryAlbum,
                GalleryPicture,
                can_delete=False,
                extra=MAX_CHOICES,
                exclude=('date_created', 'description'),
                widgets={'image': forms.URLField(widget=S3DirectWidget(dest='vids')),
                         'title': widgets.TextInput(attrs={'class': "form-control", }),
                }
            )
