from django.urls import path
from . import views



urlpatterns = [
 path('register/', views.register_user, name='register_user'),
 path('', views.about, name='about'),
 path('login/', views.login_user, name='login'),
 path('logout/', views.logout_user, name='logout_user'),
 path('details', views.details, name='details'),
 path('update/<int:id>', views.Update, name='update'),
path('delete/<int:id>', views.Delete, name='delete'),
]
