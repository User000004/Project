from django import forms
from .models import Photo

class Test_Form(forms.Form):
  test_name = Photo
  fields = ('image',)
