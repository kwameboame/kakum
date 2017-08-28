from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token
from datetime import datetime
from django.conf import settings
from django.core import validators
from s3direct.fields import S3DirectField
import re
from django.utils import timezone
from random import randrange


class KAKUserManager(BaseUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_active=True, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user('02000000', email, password, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user

    # def create_user(self, email, username, first_name, last_name, password=None):
    #     """
    #     Creates and saves a User with the given email,
    #     first_name, last_name and password.
    #     """
    #     if not email:
    #         raise ValueError('Users must have an email address')

    #     user = self.model(
    #         email=email,
    #         username=username,
    #         first_name=first_name,
    #         last_name=last_name
    #     )

    #     user.set_password(password)
    #     user.save(using=self._db)

    #     return user

    # def create_superuser(self, email, username, password, first_name, last_name):
    #     """
    #     Creates and saves a superuser with the given email, password,
    #     first_name and last_name.
    #     """
    #     user = self.create_user(email,
    #                             password=password,
    #                             username=username,
    #                             first_name=first_name,
    #                             last_name=last_name)
    #     user.is_admin = True
    #     user.save(using=self._db)
    #     return user

def unique_code():
    CHARSET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LENGTH = 10
    new_code = ''
    for i in range(LENGTH):
        new_code += CHARSET[randrange(0, len(CHARSET))]
    return '%s@gmail.com' % new_code



class KAKUser(AbstractBaseUser):
    TODAY = datetime.now()

    TODAY_PATH = TODAY.strftime("%Y/%m/%d/%H:%M:%S")

    USER_DIR = 'NEW_CACHES/AVATARS/' + TODAY_PATH + '/'

    STATUS_TYPES = (
        ('1', 'Super User'),
        ('0', 'Normal User'),
        ('2', 'Staff User'),
    )

    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
        default=unique_code(),
    )
    username = models.CharField(
        verbose_name=_('username'),
        max_length=100,
        default='02000000'
    )
    first_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    project_id = models.CharField(blank=True, null=True, max_length=1000)
    is_admin = models.CharField(max_length=100, default='0', choices=STATUS_TYPES)
    date_created = models.DateTimeField(default=timezone.now)
    avatar = S3DirectField(dest='imgs', blank=True, null=True)
    sm_avatar = models.URLField(
        blank=True,
        default=None,
        null=True,
        verbose_name=_('Social Media Avatar')
    )

    objects = KAKUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return '''{} {}'''.format(self.first_name, self.last_name)

    def get_avatar(self):
        if self.sm_avatar:
            return self.sm_avatar
        return self.avatar

    def get_short_name(self):
        return self.first_name

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return '''{} {}'''.format(self.first_name, self.last_name)

    class Meta:
        ordering = ('id', 'first_name',)
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def save(self, *args, **kwargs):
        self.email = unique_code()
        super(KAKUser, self).save(*args, **kwargs)

@receiver(post_save, sender=KAKUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
