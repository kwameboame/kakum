from django.contrib import admin
from .models import *

admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(IssueComment)
admin.site.register(IssueImage)
admin.site.register(IssueVideo)
admin.site.register(CommentCategory)
admin.site.register(KnowledgeDocument)
admin.site.register(GalleryVideo)
admin.site.register(GalleryPicture)
admin.site.register(KnowledgeArticle)
admin.site.register(KnowledgeAudio)
admin.site.register(GalleryAlbum)
