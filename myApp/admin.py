from django.contrib import admin
from .models import Animal, Experiment, VideoRecording, Result 

admin.site.register(Animal)
admin.site.register(Experiment)
admin.site.register(VideoRecording)
admin.site.register(Result)

