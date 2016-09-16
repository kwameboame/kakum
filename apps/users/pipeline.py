from apps.users.models import KAKUser


def update_user_social_data(strategy, *args, **kwargs):

    if not kwargs['is_new']:
        return

    full_name = ''
    backend = kwargs['backend']

    user = kwargs['user']

    if backend.name == 'twitter':
        if kwargs.get('details'):
            full_name = kwargs['details'].get('fullname')

    user.first_name = full_name

    # if isinstance(backend, GoogleOAuth2):
    #     if response.get('image') and response['image'].get('url'):
    #         url = response['image'].get('url')
    #         ext = url.split('.')[-1]
    #         user.avatar.save(
    #            '{0}.{1}'.format('avatar', ext),
    #            ContentFile(urllib2.urlopen(url).read()),
    #            save=False
    #         )

    if backend.name == 'facebook':
        fbuid = kwargs['response']['id']
        image_url = 'http://graph.facebook.com/%s/picture?type=large' % fbuid
        user.sm_avatar = image_url

    if backend.name == 'twitter':
        email = '%s@twitter.com' % kwargs['response'].get('id')
        if not KAKUser.objects.filter(email=email).exists():
            user.email = email
        if kwargs['response'].get('profile_image_url'):
            image_url = kwargs['response'].get('profile_image_url')
            user.sm_avatar = str(image_url.split('_normal')[0]) + '.jpg'

    if backend.name == 'google-oauth2':
            url = kwargs['response']['image'].get('url')
            ext = url.split('.')[-1]
            user.sm_avatar = ext

    user.save()
