from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Snippet
from videos.models import Video
from .forms import SnippetForm

from django.urls import reverse_lazy

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

class SnippetDetailView(DetailView):
    model = Snippet

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
#-------------------------------------------------------------------------------


# def view_video(request, video_id, snippet_id = '0'):
#     video = get_object_or_404(Video, pk=video_id)
#     yt_id = video.yt_id;
#     snippets = Snippet.objects.filter(video_id = video.id)
#     if snippet_id == '0':
#         snippet = Snippet()
#         snippet.id = 0
#         form = SnippetForm(initial={'snippet': snippet, 'title':'', 'start': video.start, 'end': video.end, 'jump': '2'})
#     else:
#         snippet = get_object_or_404(Snippet, pk=snippet_id)
#         form = SnippetForm(initial={'title': snippet.title, 'start': snippet.start, 'end': snippet.end, 'jump': snippet.jump})
#     return render(request, "view_video.html", {"video": video, 'yt_id': yt_id, 'snippet':snippet, "snippets": snippets, "form": form})
    
# #-------------------------------------------------------------------------------

# def add_snippet(request, video_id, snippet_id ):
#     video = get_object_or_404(Video, pk = video_id);
#     snippets = Snippet.objects.filter(video = video)
#     if snippet_id == '0':
#         form = SnippetForm(request.POST);
#         if form.is_valid():
#             snippet = form.save(commit = False);
#             snippet.video = video
#             snippet.save()
#     else:
#         snippet = get_object_or_404(Snippet, pk=snippet_id);
#         form = SnippetForm(request.POST, instance = snippet);
#         if form.is_valid():
#             form.save()
#     return redirect('view_video', video_id, snippet_id)

# #-------------------------------------------------------------------------------

# def delete_snippet(request, video_id, snippet_id ):
#     snippet = Snippet.objects.filter(pk = snippet_id)
#     Snippet.objects.filter(pk=snippet_id).delete();
#     snippet_id = 0
#     return redirect('view_video', video_id, snippet_id) 

# #-------------------------------------------------------------------------------
