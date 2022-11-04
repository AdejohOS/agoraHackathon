from django.urls import path
from . views import  ApiEndpoints, AdvocateList, AdvocateDetail


urlpatterns = [
   
    path('', ApiEndpoints.as_view()),

    path('advocates/', AdvocateList.as_view(), name='advocate_list'),
    path('advocates/<str:pk>/', AdvocateDetail.as_view(), name='advocate_detail'),
    

]