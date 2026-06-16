# from django.shortcuts import render



# def home(request):
#     return render(request,'index.html',{'name':'antony_venis','mass':'django_king'})



# def add(request):
#     a=int(request.POST['num1'])
#     b=int(request.POST['num2'])
#     c=a+b
#     return render(request,'result.html',{'result':c})


from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Item

class ItemListView(ListView):
    model = Item
    template_name = "index.html"
    context_object_name = "items"
    ordering = ["-id"]
    extra_context = {"name": "crud demo"}

class ItemCreateView(CreateView):
    model = Item
    fields = ["name","description"]
    template_name = "item_form.html"
    success_url = reverse_lazy("item_list")
    extra_context = {"name": "crud demo", "page_title": "Create Item"}

class ItemUpdateView(UpdateView):
    model = Item
    fields = ["name", "description"]
    template_name = "item_form.html"
    success_url = reverse_lazy("item_list")
    extra_context = {"name": "crud demo", "page_title": "Update Item"}

class ItemDeleteView(DeleteView):
    model = Item
    template_name = "item_confirm_delete.html"
    success_url = reverse_lazy("item_list")
    extra_context = {"name": "crud demo", "page_title": "Delete Item"}