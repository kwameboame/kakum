from django.db import models
from django.conf import settings
from apps.users.models import KAKUser
from django.utils import timezone
from s3direct.fields import S3DirectField
from django.db.models.signals import post_save
from django.dispatch import receiver
from boto.s3.connection import S3Connection
from cStringIO import StringIO
from PIL import Image as pil
import os
import pytz
from tinymce.models import HTMLField
from django.contrib.humanize.templatetags.humanize import naturaltime

utc = pytz.UTC


class Project(models.Model):

    date_created = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=10000, blank=True, null=True)
    has_expired = models.BooleanField(default=False)
    image = S3DirectField(dest='imgs', blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_number_of_issues(self):
        return self.myissues.all().count()

    def get_number_of_comments(self):
        myissues = self.myissues.all()
        total = 0
        for item in myissues:
            total += item.num_of_comments()
        return total

    def get_latest_issue(self):
        try:
            return self.myissues.all().latest('date_created')
        except:
            return None


class Issue(models.Model):

    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(KAKUser, related_name='mysubmissions')
    project = models.ForeignKey(Project, related_name='myissues')
    title = models.CharField(max_length=500, blank=True, null=True)
    description = HTMLField(blank=True, null=True)

    def get_images(self):
        return self.images.all()

    def get_first_image(self):
        try:
            return self.images.all()[0]
        except IndexError:
            return None

    def get_videos(self):
        return self.videos.all()

    def get_documents(self):
        return self.documents.all()

    def num_of_comments(self):
        return self.issue_comments.all().count()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Issues'


class IssueImage(models.Model):

    date_created = models.DateTimeField(default=timezone.now)
    issue = models.ForeignKey(Issue, related_name='images')
    image = S3DirectField(dest='imgs', blank=True, null=True)

    def __unicode__(self):
        return self.image


class RelevantLink(models.Model):

    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return self.title


class IssueVideo(models.Model):

    date_created = models.DateTimeField(default=timezone.now)
    issue = models.ForeignKey(Issue, related_name='videos')
    video = S3DirectField(dest='vids', blank=True, null=True)
    media_url = models.CharField(max_length=4000, blank=True, null=True)

    def __unicode__(self):
        return self.video


class IssueDocument(models.Model):

    date_created = models.DateTimeField(default=timezone.now)
    issue = models.ForeignKey(Issue, related_name='documents')
    document = S3DirectField(dest='docs', blank=True, null=True)
    cover_image = S3DirectField(dest='imgs', blank=True, null=True)
    media_url = models.CharField(max_length=4000, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return self.video


class CommentCategory(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'Comment Category'


class KnowledgeDocument(models.Model):

    project = models.ForeignKey(Project, related_name='knowledge_document')
    title = models.CharField(max_length=100)
    cover_image = S3DirectField(dest='imgs', blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    document = S3DirectField(dest='docs', blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    media_url = models.URLField(blank=True, null=True)
    show_on_homepage = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'Knowledge Docs'


class GalleryAlbum(models.Model):

    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'Gallery Albubm'


class GalleryPicture(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    image = S3DirectField(dest='imgs', blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    album = models.ForeignKey(GalleryAlbum, blank=True, null=True, related_name='my_gallery_pictures')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'Gallery Picture'


class GalleryVideo(models.Model):

    project = models.ForeignKey(Project, related_name='gallery_videos')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    video = S3DirectField(dest='vids', blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    media_url = models.CharField(max_length=4000, blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'Gallery Video'


class KnowledgeArticle(models.Model):

    project = models.ForeignKey(Project, related_name='knowledge_article')
    title = models.CharField(max_length=100)
    description = HTMLField(blank=True, null=True)
    image = S3DirectField(dest='imgs', blank=True, null=True)
    date_published = models.DateField(blank=True, null=True)
    media_url = models.URLField(blank=True, null=True)
    show_on_homepage = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'Knowledge Article'


class KnowledgeAudio(models.Model):

    project = models.ForeignKey(Project, related_name='knowledge_audio')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    audio = S3DirectField(dest='audios', blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    media_url = models.CharField(max_length=4000, blank=True, null=True)
    show_on_homepage = models.BooleanField(default=False)

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'Knowledge Audio'

    def __unicode__(self):
        return self.title


class IssueComment(models.Model):

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

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='my_comments'
    )
    issue = models.ForeignKey(Issue, related_name='issue_comments')
    timestamp = models.DateTimeField(default=timezone.now)
    comment = models.TextField(max_length=3000)
    rating = models.ForeignKey(CommentCategory)
    image = S3DirectField(dest='imgs', blank=True, null=True)
    video = S3DirectField(dest='vids', blank=True, null=True)
    audio = S3DirectField(dest='audios', blank=True, null=True)
    media_url = models.CharField(max_length=4000, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    input_channel = models.CharField(max_length=100, choices=MYCHOICES, null=True, blank=True)
    comment_type = models.CharField(max_length=100, choices=TYPE, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    archive_comment = models.BooleanField(default=False)
    issue_resolved = models.BooleanField(default=True)

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'Issue Comments'

    def __unicode__(self):
        return self.comment

    def get_elapsed_time(self):
        return naturaltime(self.timestamp)

    def get_rating(self):
        return self.rating_value.name

AWS_KEY = os.environ.get('AWS_S3_ACCESS_KEY_ID')
AWS_SECRET = os.environ.get('AWS_S3_SECRET_ACCESS_KEY')
BUCKET_NAME = 'afrstatic'


def start_compressing(theimage):
    conn = S3Connection(AWS_KEY, AWS_SECRET)
    bucket = conn.get_bucket(BUCKET_NAME)

    pic = bucket.get_key(theimage.split('https://s3.amazonaws.com/afrstatic/')[0])

    try:
        if pic.size > 100000:
            input_file = StringIO(pic.get_contents_as_string())

            img = pil.open(input_file)

            # ######### Resizing start #################

            basewidth = 700

            wpercent = (basewidth / float(img.size[0]))

            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), pil.Image.ANTIALIAS)

            # ############## Resizing Ends #####################

            tmp = StringIO()
            img.save(tmp, 'JPEG', optimize=True, quality=85)
            tmp.seek(0)

            output_data = tmp.getvalue()

            headers = dict()
            headers['Content-Type'] = 'image/jpeg'
            headers['Content-Length'] = str(len(output_data))
            pic.set_contents_from_string(output_data, headers=headers, policy='public-read')
            tmp.close()
            input_file.close()
            return True
        return 'File Size Less than 100KB'
    except:
        return 'Unable to do Compression'


@receiver(post_save, sender=IssueImage)
def compress_image(sender, instance=None, created=False, **kwargs):
    if created:
        try:
            if instance.image:
                start_compressing(str(instance.image))
        except:
            print 'Compression failed'


@receiver(post_save, sender=GalleryPicture)
def compress_image(sender, instance=None, created=False, **kwargs):
    if created:
        try:
            if instance.image:
                start_compressing(str(instance.image))
        except:
            print 'Compression failed'
