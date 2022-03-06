from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *
# Create your views here.
class Index(View):
    def get(self,request):
        contact=Contact.objects.all()
        context={'number':contact}
        return render(request,'index.html',context)
class AddContact(View):
    def get(self,request):
        form=AddContactForm()
        context={'form':form}
        return render(request,'add.html',context)
    def post(self,request):
        form=AddContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
class EditContact(View):
    def get(self,request,id):
        contact=Contact.objects.get(id=id)
        form=AddContactForm(instance=contact)
        context={'contact':contact,'form':form}
        return render(request,'edit.html',context)
    def post(self,request,id):
        contact=Contact.objects.get(id=id)
        form=AddContactForm(request.POST,instance=contact)
        if form.is_valid():
            form.save()
        return redirect('index')