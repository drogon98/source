from django.urls import path
from django.contrib.auth.views import (LoginView,LogoutView,
     PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView)
from . import views

urlpatterns=[
   path('home/',views.home,name="home"),
   path('login/',LoginView.as_view(template_name="account/login.html"),name="login"),
   path('logout/',LogoutView.as_view(template_name="account/logout.html"),name="logout"),
   path('signup/',views.register,name="register"),
   path('change-profile/',views.change_profile,name="change_profile"),
   path('password-reset/',PasswordResetView.as_view(template_name="registration/password_reset.html")
           ,name="password_reset"),
   path('password-reset/done/',PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html")
           ,name="password_reset_done"),
   path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name=
       "registration/password_reset_confirm.html"),name="password_reset_confirm"),
   path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name=
        "registration/password_reset_complete.html"),name="password_reset_complete"),
]
