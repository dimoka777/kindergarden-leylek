from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView

from .models import Queue, Name, Group
from .forms import QueueForm, GroupChangeForm, GroupForm
from news.models import Post


class QueueListView(ListView, FormMixin):
    model = Queue
    form_class = GroupChangeForm
    template_name = 'queue/queue.html'
    success_url = reverse_lazy('queue')


class QueueCreateView(CreateView):
    model = Queue
    form_class = QueueForm
    template_name = 'queue/queue_new.html'
    success_url = reverse_lazy('queue')


class Queue1ListView(ListView):
    model = Queue
    template_name = 'group/group1.html'


class Queue2ListView(ListView):
    model = Queue
    template_name = 'group/group2.html'


class Queue3ListView(ListView):
    model = Queue
    template_name = 'group/group3.html'


class Queue4ListView(ListView):
    model = Queue
    template_name = 'group/group4.html'


class Queue5ListView(ListView):
    model = Queue
    template_name = 'group/group5.html'


class QueueUpdateView(UpdateView):
    model = Queue
    template_name = 'queue/queue_update.html'
    fields = ['choice_group']
    success_url = reverse_lazy('queue')


class QueueDetailView(DetailView):
    model = Queue
    template_name = 'queue/queue_detail.html'


class QueueDeleteView(DeleteView):
    model = Queue
    template_name = 'queue/queue_delete.html'
    success_url = reverse_lazy('queue')


class NameUpdateView(UpdateView):
    model = Name
    template_name = 'name_update.html'
    fields = ['garden_address', 'garden_phone', 'garden_email', 'garden_info', 'garden_start', 'garden_end',
              'garden_map_lon', 'garden_map_lat']
    success_url = reverse_lazy('home')


class NameListView(ListView):
    model = Name
    template_name = 'name.html'


class PostListView(ListView):
    model = Name
    template_name = 'base.html'


def groups_details(request, group_id):
    print(group_id)
    return render(request, 'base.html')


class GroupListView(ListView):
    model = Group
    template_name = 'group/group.html'


class GroupDetailView(DetailView):
    model = Group
    template_name = 'group/group_detail.html'


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'group/group_delete.html'
    success_url = reverse_lazy('group')


class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'group/group_edit.html'
    fields = ['group_name', 'group_year_from', 'group_year_to', 'about_text',
              'group_reg', 'group_teachers', 'group_img']
    success_url = reverse_lazy('group')


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'group/group_new.html'
    success_url = reverse_lazy('group')


class PanelAdmin(ListView):
    model = Post
    template_name = 'panel_admin.html'
