from . import views
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True,template_name='login.html', extra_context={"active_tab":"login"}), 
        name='login'),
    path('register/', views.signup, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), 
        name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'),name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'),name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
     auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'),name='password_reset_complete')
]