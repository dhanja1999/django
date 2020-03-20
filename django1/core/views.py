from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from .forms import App_user_form,User_form
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from .models import Applicationuser
from django.db.models import Q 
# Create your views here.

def index(request):
    return render(request,'one.html')


def register(request):
    register_form_appuser = App_user_form()
    register_form_djangouser = User_form()
    context ={'appuser':register_form_appuser,'djangouser':register_form_djangouser}
    
    if request.method == "POST":
        register_form_appuser = App_user_form(request.POST,request.FILES)
        register_form_djangouser = User_form(request.POST)
        
        if register_form_appuser.is_valid() and register_form_djangouser.is_valid():
            user_django = register_form_djangouser.save()
            user_app = register_form_appuser.save(commit=False)
            
            user_app.user = user_django
            
            user_app = register_form_appuser.save(commit=True)
            return HttpResponseRedirect(reverse('login'))
        else:
            context['appuser']=register_form_appuser
            context['djangouser']=register_form_djangouser
    
    return render(request,'register.html',context)
            
@login_required
def home(request):
    context={}
    obj = Applicationuser.objects.all()
    search_query = request.GET.get('search',None)
    if search_query:
        obj = obj.filter(Q(user__username__icontains =search_query)|
                         Q(user_satus__icontains =search_query)|
                         Q(rating__icontains =search_query))
    context['userlist']=obj
    return render(request,'Logedin.html',context)

@login_required
def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse('startpoint'))