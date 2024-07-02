from django.urls import path

from userapp import views
from userapp.views import *

urlpatterns = [
    path('create/', DestinationCreateview.as_view(), name='create'),
    path('detail/<int:pk>/', DestinationDetail.as_view(), name='detail'),
    path('update/<int:pk>/', DestinationUpdateview.as_view(), name='update'),
    path('delete/<int:pk>/', DestinationDelete.as_view(), name='delete'),
    path('', views.home, name='home'),
    path('destination',views.destination,name='destination'),
    path('create_destination',views.create_destination,name='create_destination'),
    path('destdetail/<int:destination_id>/',views.destdetail,name='destdetail'),
    path('updatedetail/<int:destination_id>/', views.update_detail, name='update_detail'),
    path('updatedest/<int:destination_id>/', views.update_destination, name='update_destination'),
    path('deletedest/<int:destination_id>/', views.destination_delete, name='deletedest'),

]
