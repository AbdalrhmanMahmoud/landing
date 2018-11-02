from  django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View, CreateView, DetailView
from django.shortcuts import render
from newsletter.forms import JoinForm
from .models import Page


class HomeView(CreateView, SuccessMessageMixin):
    template_name = 'home.html'
    form_class = JoinForm
    success_url = '/'

    def get_context_data(self,*args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['object'] = Page.objects.filter(featured=True).first()
        return context

    def get_success_message(self, cleaned_data):
        # print(cleaned_data)
        # return "thanks bro"
        return SuccessMessageMixin

class PageDetailView(DetailView):
    queryset = Page.objects.filter(active=True)
    model = Page
    template_name = 'home.html'

def about(request):
	return render(request, "about.html")
















