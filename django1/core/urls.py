from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+[
    url(r'^login/$',LoginView.as_view(template_name='login.html'),name="login"),
    url(r'^register/$',views.register,name="register"),
    url(r'^home/$',views.home,name="home"),
    url(r'^logout/$',views.logout,name="logout"),
    url("",views.index,name="startpoint")
]
