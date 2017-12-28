from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
# from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

import re

from .models import Snippet
from videos.models import Video
from .forms import SnippetDetailForm

#-------------------------------------------------------------------------------

class SnippetListView(ListView):
    template_name = 'snippet_list.html'
    context_object_name = 'snippet_list'
    model = Snippet
    
    def get_context_data(self, **kwargs):
        video_id = self.kwargs['vid']
        snippet_id = self.kwargs['sid']
        context = super(SnippetListView, self).get_context_data(**kwargs)
        context.update({
            'video': get_object_or_404(Video, pk=video_id),
        })
        if int(snippet_id) > 0:
            context.update({
                'snippet': get_object_or_404(Snippet, pk=snippet_id),
            })
        return context
        
    def get_queryset(self):
        video_id = self.kwargs['vid']
        self.video = get_object_or_404(Video, pk=video_id)
        return Snippet.objects.filter(video = self.video)
    
#-------------------------------------------------------------------------------

def get_snippet_title(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    data = {
        'title': snippet.title,
        'start': snippet.start,
        'end': snippet.end,
        'jump': snippet.jump
    }
    return JsonResponse(data, safe=False)

#-------------------------------------------------------------------------------

class SnippetCreateView(CreateView):
    model = Snippet
    fields = ['title', 'video']

    def get_initial(self):
        return { 'video': self.kwargs['pk'] }
 
    def get_success_url(self):
        video_id = self.kwargs['pk']
        snippet_id = self.object.id
        success_url = reverse_lazy('snippet-list', args=(video_id, snippet_id))
        return success_url    

#-------------------------------------------------------------------------------

class SnippetUpdateView(UpdateView):
    model = Snippet
    fields = ['title']
    
    def get_success_url(self):
        snippet = get_object_or_404(Snippet, pk=self.kwargs['pk']);
        snippet_id = snippet.id
        video_id = snippet.video_id
        success_url = reverse_lazy('snippet-list', args=(video_id, snippet_id,))
        return success_url

#-------------------------------------------------------------------------------

class SnippetDeleteView(DeleteView):
    model = Snippet

    def get_success_url(self):
        snippet = get_object_or_404(Snippet, pk=self.kwargs['pk']);
        snippet_id = 0
        video_id = snippet.video_id
        success_url = reverse_lazy('snippet-list', args=(video_id, snippet_id,))
        return success_url

#-------------------------------------------------------------------------------
