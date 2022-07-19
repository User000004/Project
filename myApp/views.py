from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from .models import Photo, Video, Animal, Experiment, VideoRecording, Result 
from .forms import Test_Form
from pathlib import Path
import os

def new_entry(request):
  if request.method == 'POST' and request.FILES['pictureInput']:
    upload = request.FILES['pictureInput']
    fss = FileSystemStorage()
    file = fss.save(upload.name, upload)
    file_url = fss.url(file)
    video = Video()
    video.f=file
    video.save()
    return render(request, 'myApp/page1.html', {'file_url': file_url})
  return render(request, 'myApp/page1.html')
    
def show_list(request):
  videos = Video.objects.all()
  return render(request, 'myApp/page2.html', {'videos': videos})

def experiments(request):
  animal1 = Animal()
  animal1.animal_type = 'mouse'
  animal1.save()
  animal2 = Animal()
  animal2.animal_type = 'rat'
  animal2.save()
  experiments = Experiment.objects.all().order_by('-experiment_date')
  return render(request, 'myApp/experiments.html', {'experiments': experiments})

def experiment_info(request, pk):
  videos = VideoRecording.objects.filter(experiment_id=pk)
  experiment = get_object_or_404(Experiment, experiment_id=pk)
  return render(request, 'myApp/experiment_info.html', {'videos': videos, 'experiment': experiment})

def experiment_new(request):
  if request.method == 'POST':
    experiment = Experiment()
    experiment.experiment_name = request.POST.get('inputName')
    experiment.experiment_date = request.POST.get('inputDate')
    if request.POST.get('inputDescription') != '':
      experiment.experiment_description = request.POST.get('inputDescription')
    experiment.time_after_experiment = request.POST.get('inputTimeAfterExperiment')
    if request.POST.get('inputAmountofIrradiatedAnimals') != '':
      experiment.count_irradiated_animals = request.POST.get('inputAmountofIrradiatedAnimals')
    if request.POST.get('inputAmountofUnirradiatedAnimals') != '':
      experiment.count_unirradiated_animals = request.POST.get('inputAmountofUnirradiatedAnimals')
    experiment.animal_id = get_object_or_404(Animal, animal_type=request.POST.get('inputType'))
    experiment.save()
    experiment.experiment_path = 'Experiment_'+str(experiment.experiment_id)+'/'
    if experiment.experiment_name == '':
      experiment.experiment_name = 'Experiment_'+str(experiment.experiment_id)
    experiment.save()
    files = request.FILES.getlist('inputFiles')
    for i in files:
      fss = FileSystemStorage('media/'+experiment.experiment_path)
      file = fss.save(i.name, i)
      file_url = fss.url(file)
      video = VideoRecording()
      video.video_name = experiment.experiment_name+'.Video_'
      video.experiment_id = experiment
      video.video_url = file_url
      video.save()
      video.video_name = experiment.experiment_name+'.Video_'+str(video.video_id)
      video.save()
      result = Result()
      result.video_id = video
      result.result_path = experiment.experiment_path+'Result_to_video_'+str(video.video_id)
      result.save()
    experiments = Experiment.objects.all().order_by('-experiment_date')
    return render(request, 'myApp/experiments.html', {'experiments': experiments})
  animals = Animal.objects.all()
  return render(request, 'myApp/experiment_new.html', {'animals': animals})

def video_new(request, pk):
  if request.method == 'POST':
    videos = VideoRecording.objects.filter(experiment_id=pk)
    upload = request.FILES['inputFile']
    experiment = get_object_or_404(Experiment, experiment_id=pk)
    fss = FileSystemStorage('media/'+experiment.experiment_path)
    file = fss.save(upload.name, upload)
    file_url = fss.url(file)
    video = VideoRecording()
    video.video_name = request.POST.get('inputName')
    video.experiment_id = experiment
    if request.POST.get('inputDescription') != '':
      video.video_description = request.POST.get('inputDescription')
    video.video_url = file_url
    if request.POST.get('inputType') == 'irradiated':
      video.animal_irradiated = True
    else:
      video.animal_irradiated = False
    video.save()
    if video.video_name == '':
      video.video_name = experiment.experiment_name+'.Video_'+str(video.video_id)
    video.save()
    result = Result()
    result.video_id = video
    result.result_path = experiment.experiment_path+'Result_to_video_'+str(video.video_id)
    result.save()
    videos = VideoRecording.objects.filter(experiment_id=pk)
    return render(request, 'myApp/experiment_info.html', {'videos': videos, 'experiment': experiment})
  experiment = get_object_or_404(Experiment, experiment_id=pk)
  return render(request, 'myApp/video_new.html', {'experiment': experiment})
  

def experiment_edit(request, pk):
  if request.method == 'POST':
    experiment=get_object_or_404(Experiment, experiment_id=pk)
    experiment.experiment_name = request.POST.get('inputName')
    experiment.experiment_date = request.POST.get('inputDate')
    if request.POST.get('inputDescription') != '':
      experiment.experiment_description = request.POST.get('inputDescription')
    else:
      experiment.experiment_description = 'no description'
    experiment.time_after_experiment = request.POST.get('inputTimeAfterExperiment')
    if request.POST.get('inputAmountofIrradiatedAnimals') != '':
      experiment.count_irradiated_animals = request.POST.get('inputAmountofIrradiatedAnimals')
    if request.POST.get('inputAmountofUnirradiatedAnimals') != '':
      experiment.count_unirradiated_animals = request.POST.get('inputAmountofUnirradiatedAnimals')
    experiment.animal_id = get_object_or_404(Animal, animal_type=request.POST.get('inputType'))
    experiment.save()
    experiment.experiment_path = 'Experiment_'+str(experiment.experiment_id)+'/'
    if experiment.experiment_name == '':
      experiment.experiment_name = 'Experiment_'+str(experiment.experiment_id)
    experiment.save()

    experiment = get_object_or_404(Experiment, experiment_id=pk)
    videos = VideoRecording.objects.filter(experiment_id=pk)
    return render(request, 'myApp/experiment_info.html', {'videos': videos, 'experiment': experiment})
  experiment = get_object_or_404(Experiment, experiment_id=pk)
  animals = Animal.objects.all()
  return render(request, 'myApp/experiment_edit.html', {'experiment': experiment, 'animals': animals})


def video_info(request, pk, pk2):
  experiment = experiment = get_object_or_404(Experiment, experiment_id=pk)
  video = get_object_or_404(VideoRecording, video_id=pk2)
  return render(request, 'myApp/video_info.html', {'experiment': experiment, 'video': video})

def video_edit(request, pk, pk2):
  if request.method == 'POST':
    experiment = experiment = get_object_or_404(Experiment, experiment_id=pk)
    video = get_object_or_404(VideoRecording, video_id=pk2)
    video.video_name = request.POST.get('inputName')
    if request.POST.get('inputDescription') == '':
      video.video_description = 'no description'
    else:
      video.video_description = request.POST.get('inputDescription')
    if request.POST.get('inputType') == 'irradiated':
      video.animal_irradiated = True
    else:
      video.animal_irradiated = False
    video.save()
    if video.video_name == '':
      video.video_name = experiment.experiment_name+'.Video_'+str(video.video_id)
    video.save()
    return render(request, 'myApp/video_info.html', {'experiment': experiment, 'video': video})
    
  video = get_object_or_404(VideoRecording, video_id=pk2)
  return render(request, 'myApp/video_edit.html', {'video': video})

"""
  videos = VideoRecording.objects.filter(experiment_id=pk)
  return render(request, 'myApp/experiment_info.html', {'videos': videos})


https://overcoder.net/q/16987/%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF-%D0%BA-%D1%84%D0%B0%D0%B9%D0%BB%D0%B0%D0%BC-%D0%BC%D0%B5%D0%B4%D0%B8%D0%B0-%D0%B2-django

"""










