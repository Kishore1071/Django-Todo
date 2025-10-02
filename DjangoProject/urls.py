from django.contrib import admin
from django.urls import path
from Base.views import *

urlpatterns = [
    path('admin/', admin.site.urls),


    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='login'), name='logout'),

    path('', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_view'),
    path('task/create/', TaskCreate.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
]
