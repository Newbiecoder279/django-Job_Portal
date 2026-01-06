from django import forms
from . models import PostJob

class PostJobForm(forms.ModelForm):
    class Meta:
        model = PostJob
        fields = ['title', 'job_type','job_location','short_descrption']