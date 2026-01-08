from django.shortcuts import get_object_or_404, render, redirect
from . forms import PostJobForm
from django.utils.text import slugify
from . models import PostJob
# Create your views here.

def job_post_view(request):
    if request.method == 'POST':
        form = PostJobForm(request.POST)
        if form.is_valid():
           job = form.save(commit=False)
           title = form.cleaned_data['title']
           job.slug = slugify(title)+'-'+str(job.id)
           job.save()
           return redirect('dashboard')
    else:
        form = PostJobForm()

    context  = {
        'form':form
    }

    return render(request, 'post_jobs.html', context)



def show_job_details(request,pk):
    job = get_object_or_404(PostJob,pk=pk)
    context = {
        'job':job
    }
    return render(request,'job_details.html',context)
           