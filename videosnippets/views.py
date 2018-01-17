from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
# from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from django.views.generic.edit import FormMixin
from django.http import Http404

import re

from .models import Snippet
from videos.models import Video
from .forms import SnippetSaveForm

#-------------------------------------------------------------------------------

class FormListView(FormMixin, ListView):
    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        
       # From BaseListView
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        
        # if not allow_empty and len(self.object_list) == 0:
        #     raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
        #                   % {'class_name': self.__class__.__name__})

        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
        
class SnippetListView(FormListView):
    form_class = SnippetSaveForm;
    # template_name = 'snippet_list.html'
    # context_object_name = 'snippet_list'
    # model = Snippet
    
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
        return Snippet.objects.filter(video = self.video).order_by('id')
    
#-------------------------------------------------------------------------------

def snippet_control(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    data = {
        'id': snippet.id,
        'title': snippet.title,
        'start': snippet.start,
        'end': snippet.end,
        'jump': snippet.jump
    }
    return JsonResponse(data, safe=False)

#-------------------------------------------------------------------------------

def snippet_save(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    video_id = snippet.video_id
    video = get_object_or_404(Video, pk=video_id);
    if request.method == 'POST':
        form = SnippetSaveForm(request.POST, instance = snippet)
        if form.is_valid():
            snippet = form.save(commit = False);
            snippet.save();
            data={};
            data['title'] = snippet.title
        else:
            print(form.errors)
    return redirect('snippet-list', video_id, snippet_id)

#-------------------------------------------------------------------------------

class SnippetCreateView(CreateView):
    model = Snippet
    fields = ['title', 'video', 'start']

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
