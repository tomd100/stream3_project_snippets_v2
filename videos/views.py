from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Video
from .forms import VideoForm
from categories.models import VideoCategory

from django.urls import reverse_lazy

#-------------------------------------------------------------------------------
# Video Views

class VideoListView(ListView):
    model = Video

    def get_context_data(self, **kwargs):
        category_id = self.kwargs['cid']
        category_id = int(category_id)
        context = super(VideoListView, self).get_context_data(**kwargs)
        if category_id == 9999:
            context['video_list'] = Video.objects.all().filter(category=0)
        elif category_id > 0:
            context['video_list'] = Video.objects.all().filter(category=category_id)
        context.update({
            'videocategory_list': VideoCategory.objects.all(),
        })
        return context
        
    def get_queryset(self):
        self.videocategory = VideoCategory.objects.all()
        return Video.objects.all()

#-------------------------------------------------------------------------------

class VideoCreateView(CreateView):
    model = Video
    fields = ['title', 'category', 'url']
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        url = self.object.url
        yt_id = getYouTubeId(url)
        if yt_id != -1:
            self.object.yt_id = yt_id;
            self.object.user = self.request.user
            self.object.save()
            return HttpResponseRedirect(reverse_lazy('video-list', kwargs={'cid': 0}))
        else:
            messages.success(self.request, "Not a valid YouTube URL", extra_tags='danger') 
            return HttpResponseRedirect(reverse_lazy('video-add'))
        

#-------------------------------------------------------------------------------

class VideoUpdateView(UpdateView):
    model = Video
    fields = ['title', 'category', 'url']
    success_url = reverse_lazy('video-list', kwargs={'cid': 0})
    
#-------------------------------------------------------------------------------

class VideoDeleteView(DeleteView):
    model = Video
    success_url = reverse_lazy('video-list', kwargs={'cid': 0})

#-------------------------------------------------------------------------------

def getYouTubeId(url):
    url1 = url.split("v=", 1)
    if len(url1) == 1:
        return -1
    else:
        url2 = url1[1].split("?",1)
        url3 = url2[0].split("&",1)
        yt_id = str(url3[0])
        return  yt_id
        
#-------------------------------------------------------------------------------
