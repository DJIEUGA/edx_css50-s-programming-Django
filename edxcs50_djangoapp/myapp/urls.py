from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    # path('<str:name>', views.greet, name='greet'),
    path('singlepage', views.singlepage, name='singlepage'),
    path('singlepage/sections/<int:num>', views.section, name='section'),
]