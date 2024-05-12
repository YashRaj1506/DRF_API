from django.urls import path
from .import views


urlpatterns = [
    path('',views.endpoints),
    path('advocates/', views.advocate_list),
    # path('advocates/<str:username>/', views.advocate_details, name="advocates"),
    path('advocates/<str:username>/', views.AdvocateDetail.as_view(), name="advocates"),
    # path('add_advocate/')
    path('companies/', views.companies_list),



]


#comapnies


#GET /advocates
#POST /advocates

#GET /advocates/:id
#PUT /advocates/:id
#DELETE /advocates/:id

