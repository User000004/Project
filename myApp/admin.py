from django.contrib import admin
from .models import Photo, Video, Animal, Experiment, VideoRecording, Result 

admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Animal)
admin.site.register(Experiment)
admin.site.register(VideoRecording)
admin.site.register(Result)

