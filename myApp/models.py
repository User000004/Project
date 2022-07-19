from django.db import models
from django.utils import timezone
import pickle

class Animal(models.Model):
  animal_id = models.AutoField(primary_key = True)
  animal_type = models.CharField(max_length=200)

class Experiment(models.Model):
  experiment_id = models.AutoField(primary_key = True)
  experiment_name = models.CharField(max_length=200)
  experiment_date = models.DateTimeField(default = timezone.now)
  experiment_description = models.TextField(default="no description")
  experiment_path = models.URLField('exp' + str(experiment_id))
  time_after_experiment = models.IntegerField()
  count_irradiated_animals = models.IntegerField()
  count_unirradiated_animals = models.IntegerField()
  animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)

  def animals(self):
    if self.animal_id.animal_type == "rat":
      return "rats"
    elif self.animal_id.animal_type == "mouse":
      return "mice"
    else:
      return "unknown"

  def getTime_rfc3339(self):
    year = str(self.experiment_date.year)
    month = str(self.experiment_date.month)
    if len(month)==1:
      month = '0'+month
    day = str(self.experiment_date.day)
    if len(day)==1:
      day = '0'+day
    hour = str(self.experiment_date.hour)
    if len(hour)==1:
      hour = '0'+hour
    minute = str(self.experiment_date.minute)
    if len(minute)==1:
      minute = '0'+minute
    return year+'-'+month+'-'+day+'T'+hour+':'+minute

class VideoRecording(models.Model):
  video_id = models.AutoField(primary_key = True)
  video_name = models.CharField(max_length=200)
  experiment_id = models.ForeignKey(Experiment, on_delete=models.CASCADE)
  video_description = models.TextField(default = "no description")
  video_url = models.TextField()
  animal_irradiated = models.BooleanField(null=True)

  def get_irradiated(self):
    if self.animal_irradiated == True:
      return 'irradiated'
    elif self.animal_irradiated == False:
      return 'unirradiated'
    else:
      return 'none'
     
    

class Result(models.Model):
  result_id = models.AutoField(primary_key = True)
  result_path = models.URLField()
  video_id = models.ForeignKey(VideoRecording, on_delete=models.CASCADE)












