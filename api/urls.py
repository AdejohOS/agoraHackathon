from django.urls import path
from . views import AdvocateList, AdvocateDetail
from . import views

urlpatterns = [
   
    path('', views.ApiEndpoints),

    path('advocates/', AdvocateList.as_view(), name='advocate_list'),
    path('advocates/<int:pk>/', AdvocateDetail.as_view(), name='advocate_detail'),

]