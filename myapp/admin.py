from django.contrib import admin

from .models import CustomUser,Story,StoryLike,StoryComment,StoryShare

  # Import the correct view


admin.site.register(CustomUser)
admin.site.register(Story)
admin.site.register(StoryLike)
admin.site.register(StoryComment)
admin.site.register(StoryShare)
