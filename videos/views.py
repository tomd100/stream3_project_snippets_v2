from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Video
from .forms import VideoForm

from django.urls import reverse_lazy

#-------------------------------------------------------------------------------

class VideoListView(ListView):
    model = Video
    # paginate_by = 5

#-------------------------------------------------------------------------------

class VideoCreateView(CreateView):
    model = Video
    fields = ['title', 'url']
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        url = self.object.url
        yt_id = getYouTubeId(url)
        if yt_id != -1:
            self.object.yt_id = yt_id;
            self.object.user = self.request.user
            self.object.save()
            return HttpResponseRedirect(reverse_lazy('video-list'))
        else:
            messages.success(self.request, "Not a valid YouTube URL", extra_tags='danger') 
            return HttpResponseRedirect(reverse_lazy('video-add'))
        

#-------------------------------------------------------------------------------

class VideoUpdateView(UpdateView):
    model = Video
    fields = ['title', 'url']
    success_url = reverse_lazy('video-list')
    
#-------------------------------------------------------------------------------

class VideoDeleteView(DeleteView):
    model = Video
    success_url = reverse_lazy('video-list')

    # def post(self, request, *args, **kwargs):
    #     if "cancel" in request.POST:
    #         return HttpResponseRedirect(reverse_lazy('video-list'))
    #     else:
    #         return super(VideoDeleteView, self).post(request, *args, **kwargs)
            
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