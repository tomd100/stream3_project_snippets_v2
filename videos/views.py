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
        user = self.request.user
        category_id = self.kwargs['cid']
        category_id = int(category_id)
        context = super(VideoListView, self).get_context_data(**kwargs)
        if category_id == 9999:
            context['video_list'] = Video.objects.all().filter(user=user, category=None)
        elif category_id > 0:
            context['video_list'] = Video.objects.all().filter(user=user, category=category_id)
        context.update({
            'videocategory_list': VideoCategory.objects.all().filter(user=user),
        })
        return context
        
    def get_queryset(self):
        user = self.request.user
        self.videocategory = VideoCategory.objects.all().filter(user=user)
        return Video.objects.all().filter(user=user)

#-------------------------------------------------------------------------------

class RequestFormKwargsMixin(object):
    """
    CBV mixin which puts the request into the form kwargs.
    Note: Using this mixin requires you to pop the `request` kwarg
    out of the dict in the super of your form's `__init__`.
    """
    def get_form_kwargs(self):
      kwargs = super(RequestFormKwargsMixin, self).get_form_kwargs()
      # Update the existing form kwargs dict with the request's user.
      kwargs.update({"request": self.request})
      return kwargs

class VideoCreateView(RequestFormKwargsMixin, CreateView):
    model = Video
    form_class = VideoForm
    # fields = ['title', 'category', 'url']
    
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

class VideoUpdateView(RequestFormKwargsMixin, UpdateView):
    model = Video
    form_class = VideoForm
    success_url = reverse_lazy('video-list', kwargs={'cid': 0})
    
#-------------------------------------------------------------------------------

class VideoDeleteView(DeleteView):
    model = Video
    success_url = reverse_lazy('video-list', kwargs={'cid': 0})

#-------------------------------------------------------------------------------

def getYouTubeId(url):
    yt_url = url.split("v=", 1)
    if len(yt_url) == 1:
        yt_url = url.split("/youtu.be/", 1)
        if len(yt_url) == 1:
            return -1
    yt_url = yt_url[1].split("?",1)
    yt_url = yt_url[0].split("&",1)
    yt_id = str(yt_url[0])
    return  yt_id
        
#-------------------------------------------------------------------------------
