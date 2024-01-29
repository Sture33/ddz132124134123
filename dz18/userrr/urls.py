from django.urls import path

from userrr import views

urlpatterns = [
    path('', views.StartPage, name='start'),
    path('sign-up/', views.SignUpView.as_view(), name='sign_up'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.Logout, name='logout')
]