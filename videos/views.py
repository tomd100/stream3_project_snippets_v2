from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Video
from .forms import VideoForm

from django.urls import reverse_lazy


class VideoListView(ListView):
    model = Video
    # paginate_by = 5

class VideoCreateView(CreateView):
    model = Video
    fields = ['title', 'url']

class VideoUpdateView(UpdateView):
    model = Video
    fields = ['title', 'url']

class VideoDeleteView(DeleteView):
    model = Video
    success_url = reverse_lazy('video-list')