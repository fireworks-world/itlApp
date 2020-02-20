from django.contrib import admin

from . import models

admin.site.register(models.ArticleTable)
admin.site.register(models.Likes)
admin.site.register(models.Poll)
admin.site.register(models.Information)
admin.site.register(models.Welcome)
admin.site.register(models.Feedback)
admin.site.register(models.Summer)
admin.site.register(models.Internship)
admin.site.register(models.Coder)