from django.conf.urls import patterns, url


urlpatterns = patterns('',

    url(r'^all_issues/$', 'apps.projects.views.all_issues', name="all_issues"),
    url(r'^all_albums/$', 'apps.projects.views.all_albums', name="all_albums"),
    url(r'^all_videos/$', 'apps.projects.views.all_videos', name="all_videos"),
    url(r'^add_issue/$', 'apps.projects.views.add_issue', name="add_issue"),

    url(r'^view_issue/(?P<pk>\d+)/$', 'apps.projects.views.view_issue', name="view_issue"),
    url(r'^edit_issue/(?P<pk>\d+)/$', 'apps.projects.views.edit_issue', name="edit_issue"),
    url(r'^issue_detail/(?P<pk>\d+)/$', 'apps.projects.views.issue_detail', name="issue_detail"),

    url(r'^all_documents/$', 'apps.projects.views.all_documents', name="all_documents"),
    url(r'^all_articles/$', 'apps.projects.views.all_articles', name="all_articles"),

    url(r'^add_rating/$', 'apps.projects.views.add_category', name="add_rating"),
    url(r'^add_relevant_links/$', 'apps.projects.views.add_relevant_links', name="add_relevant_links"),
    url(r'^delete_category/(?P<pk>\d+)/$', 'apps.projects.views.delete_category', name="delete_category"),
    url(r'^delete_link/(?P<pk>\d+)/$', 'apps.projects.views.delete_link', name="delete_link"),

    url(r'^view_comments/(?P<pk>\d+)/$', 'apps.projects.views.view_comments', name="view_comments"),

    url(r'^filter_rating/(?P<name>\w+)/$', 'apps.projects.views.filter_rating', name="filter_rating"),
    url(r'^filter_ok/$', 'apps.projects.views.filter_ok', name="filter_ok"),
    url(r'^filter_resolved/$', 'apps.projects.views.filter_resolved', name="filter_resolved"),
    url(r'^filter_unresolved/$', 'apps.projects.views.filter_unresolved', name="filter_unresolved"),

    #video
    url(r'^add_video/$', 'apps.projects.views.add_video', name="add_video"),
    url(r'^edit_video/(?P<pk>\d+)/$', 'apps.projects.views.edit_video', name="edit_video"),
    url(r'^view_video/(?P<pk>\d+)/$', 'apps.projects.views.view_video', name="view_video"),
    url(r'^delete_video/(?P<pk>\d+)/$', 'apps.projects.views.delete_video', name="delete_video"),
    url(r'^confirm_delete_video/(?P<pk>\d+)/$', 'apps.projects.views.confirm_delete_video', name="confirm_delete_video"),

    url(r'^add_album/$', 'apps.projects.views.add_album', name="add_album"),
    url(r'^edit_album/(?P<pk>\d+)/$', 'apps.projects.views.edit_album', name="edit_album"),
    # url(r'^view_picture/(?P<pk>\d+)/$', 'apps.projects.views.view_picture', name="view_picture"),
    url(r'^delete_album/(?P<pk>\d+)/$', 'apps.projects.views.delete_album', name="delete_album"),
    url(r'^confirm_delete_album/(?P<pk>\d+)/$', 'apps.projects.views.confirm_delete_album', name="confirm_delete_album"),
    #audio
    url(r'^add_audio/$', 'apps.projects.views.add_audio', name="add_audio"),
    url(r'^edit_audio/(?P<pk>\d+)/$', 'apps.projects.views.edit_audio', name="edit_audio"),
    url(r'^view_audio/(?P<pk>\d+)/$', 'apps.projects.views.view_audio', name="view_audio"),
    url(r'^delete_audio/(?P<pk>\d+)/$', 'apps.projects.views.delete_audio', name="delete_audio"),
    url(r'^confirm_delete_audio/(?P<pk>\d+)/$', 'apps.projects.views.confirm_delete_audio', name="confirm_delete_audio"),

    #document
    url(r'^add_document/$', 'apps.projects.views.add_document', name="add_document"),
    url(r'^edit_document/(?P<pk>\d+)/$', 'apps.projects.views.edit_document', name="edit_document"),
    url(r'^view_document/(?P<pk>\d+)/$', 'apps.projects.views.view_document', name="view_document"),
    url(r'^delete_document/(?P<pk>\d+)/$', 'apps.projects.views.delete_document', name="delete_document"),
    url(r'^confirm_delete_document/(?P<pk>\d+)/$', 'apps.projects.views.confirm_delete_document', name="confirm_delete_document"),

    #article
    url(r'^add_article/$', 'apps.projects.views.add_article', name="add_article"),
    url(r'^edit_article/(?P<pk>\d+)/$', 'apps.projects.views.edit_article', name="edit_article"),
    url(r'^view_article/(?P<pk>\d+)/$', 'apps.projects.views.view_article', name="view_article"),
    url(r'^delete_article/(?P<pk>\d+)/$', 'apps.projects.views.delete_article', name="delete_article"),
    url(r'^confirm_delete_article/(?P<pk>\d+)/$', 'apps.projects.views.confirm_delete_article', name="confirm_delete_article"),

    #project
    url(r'^add_project/$', 'apps.projects.views.add_project', name="add_project"),
    url(r'^all_projects/$', 'apps.projects.views.all_projects', name="all_project"),
    url(r'^ongoing/$', 'apps.projects.views.ongoing', name="ongoing"),
    url(r'^past/$', 'apps.projects.views.past', name="past"),
    url(r'^view_project/(?P<pk>\d+)/$', 'apps.projects.views.view_project', name="view_project"),
    url(r'^edit_project/(?P<pk>\d+)/$', 'apps.projects.views.edit_project', name="edit_project"),
    url(r'^project_detail/(?P<pk>\d+)/$', 'apps.projects.views.project_detail', name="project_detail"),
    url(r'^project_issues/(?P<pk>\d+)/$', 'apps.projects.views.project_issues', name="project_issues"),

    # DELETING THINGS
    url(r'^delete_issue/(?P<pk>\d+)/$', 'apps.projects.views.delete_issue', name="delete_issue"),
    url(r'^confirm_delete_issue/(?P<pk>\d+)/$', 'apps.projects.views.confirm_delete_issue', name="confirm_delete_issue"),
    url(r'^delete_project/(?P<pk>\d+)/$', 'apps.projects.views.delete_project', name="delete_project"),
    url(r'^confirm_delete_project/(?P<pk>\d+)/$', 'apps.projects.views.confirm_delete_project', name="confirm_delete_project"),

    #issue comment
    url(r'^add_issue_comment/$', 'apps.projects.views.add_issue_comment', name="add_issue_comment"),
    url(r'^edit_comment/(?P<pk>\d+)/$', 'apps.projects.views.edit_issue_comment', name="edit_comment"),
    url(r'^view_comment/(?P<pk>\d+)/$', 'apps.projects.views.issue_comment_detail', name="view_comment"),
    url(r'^delete_comment/(?P<pk>\d+)/$', 'apps.projects.views.delete_comment', name="delete_comment"),
    url(r'^confirm_delete_comment/(?P<pk>\d+)/$', 'apps.projects.views.confirm_delete_comment', name="confirm_delete_comment"),
    url(r'^resolve_comment/(?P<pk>\d+)/$', 'apps.projects.views.resolve_comment', name="resolve_comment"),

    url(r'^all_comments/$', 'apps.projects.views.all_comments', name="all_comments"),
    url(r'^projects_visualisations/$', 'apps.projects.views.projects_visualisations', name="projects_visualisations"),
    url(r'^issues_visualisations/$', 'apps.projects.views.issues_visualisations', name="issues_visualisations"),

    url(r'^projects_visualisations/(?P<pk>\d+)/$', 'apps.projects.views.projects_visualisations_details', name="projects_visualisations_details"),
    url(r'^issues_visualisations/(?P<pk>\d+)/$', 'apps.projects.views.issues_visualisations_details', name="issues_visualisations_details"),
)
