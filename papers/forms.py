import re
from django import forms
from django.contrib.auth.models import User


class SearchForm(forms.Form):
  key = forms.CharField(max_length=100)
  