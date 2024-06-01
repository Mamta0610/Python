from django.urls import path
from . import views

urlpatterns = [
     path('', views.list_page,name="list"),
     path('<int:id>', views.detail_page,name="detail"),
    path('rangelist/', views.student_range_list_view),
    path('studentlist/', views.StudentListView),
    path('index', views.index,name="index"),
    path('add/',views.add,name="add"),
    path("addrec/",views.addrec,name="addrec"),
    path('delete/<int:id>/',views.delete,name="delete"),
   
]