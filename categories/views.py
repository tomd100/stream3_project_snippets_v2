from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import VideoCategory
from .forms import VideoCategoryForm

from django.urls import reverse_lazy

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Category Views


class OwnObjectsMixin():
    def get_queryset(self):
        user = self.request.user
        return super(OwnObjectsMixin, self).get_queryset().filter(user=user)

class VideoCategoryListView(OwnObjectsMixin, ListView):
    model = VideoCategory
        
#-------------------------------------------------------------------------------

class CheckSubCatMixin(UserPassesTestMixin):
    def test_func(self):
        valid_action = True;
        if self.request.user.profile.sub_type == 0:
            valid_action = False;
        return valid_action;
        
    login_url = reverse_lazy('subscribe')
    def get_redirect_field_name(self):
        return None;
        

#-------------------------------------------------------------------------------  

class VideoCategoryCreateView(CheckSubCatMixin, CreateView):
    model = VideoCategory
    fields = ['category']
    success_url = reverse_lazy('video-list', kwargs={'cid': 0})
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(VideoCategoryCreateView, self).form_valid(form)
    
#-------------------------------------------------------------------------------

class VideoCategoryUpdateView(UpdateView):
    model = VideoCategory
    fields = ['category']
    success_url = reverse_lazy('video-list', kwargs={'cid': 0})
    
#-------------------------------------------------------------------------------    

class VideoCategoryDeleteView(DeleteView):
    model = VideoCategory
    success_url = reverse_lazy('video-list', kwargs={'cid': 0})

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------