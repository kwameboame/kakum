from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login/$', 'apps.users.views.login_view', name="login"),
    url(r'^logout/$', 'apps.users.views.logout_view', name="logout"),
    url(r'^dashboard/$', 'apps.users.views.dashboard', name="dashboard"),
    url(r'^all_admin/$', 'apps.users.views.admin_list', name="admin_list"),
    url(r'^users_list/$', 'apps.users.views.user_list', name="user_list"),
    url(r'^user_detail/(?P<pk>\d+)/$', 'apps.users.views.user_detail', name="user_detail"),
    url(r'^delete_admin/(?P<pk>\d+)/$', 'apps.users.views.delete_admin', name="delete_admin"),
    url(r'^confirm_delete_admin/(?P<pk>\d+)/$', 'apps.users.views.confirm_delete_admin', name="confirm_delete_admin"),
    url(r'^create_admin/$', 'apps.users.views.create_admin', name="create_admin"),
    url(r'^edit_admin/(?P<pk>\d+)/$', 'apps.users.views.edit_admin', name="edit_admin"),
)
