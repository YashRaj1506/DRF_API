from django.urls import path
from .import views


urlpatterns = [
    path('',views.endpoints),
    path('advocates/', views.advocate_list),
    path('advocates/<str:username>/', views.advocate_details),
    # path('add_advocate/')

]


#GET /advocates
#POST /advocates

#GET /advocates/:id
#PUT /advocates/:id
#DELETE /advocates/:id

