from django.contrib import admin
from app.models import Activity, Tag, ActivityTag, UserSelection
# Register your models here.

admin.site.register(Activity)
admin.site.register(Tag)
admin.site.register(ActivityTag)
admin.site.register(UserSelection)

