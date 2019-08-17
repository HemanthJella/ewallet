from django.urls import path,include, re_path
from . import views
from .views import Pdf

app_name = 'trans'
urlpatterns = [
    re_path('^$', views.many, name="trans.many"),
    path('send/', views.new, name="trans.mail"),
    path('render/pdf/', Pdf.as_view(),name='trans.down'),

]
