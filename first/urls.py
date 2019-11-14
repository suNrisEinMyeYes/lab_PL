from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve


from . import views

urlpatterns = [
    re_path(r'upload$',views.upload),
    re_path(r'upload/$',views.upload), 
	re_path(r'create/$',views.create),
	re_path(r'create$',views.create),
    re_path(r'delete/$',views.delete),
	re_path(r'delete$',views.delete),
	re_path(r'downlo/$',views.downlo),
	re_path(r'downlo$',views.downlo),
    re_path(r'^', views.index),
	#path('', views.index, name = 'index'),
	#path(r'^api-auth/', include('rest_framework.urls')),
        #re_path(r'^.*', )
]
