from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('portfolio/add/', views.portfolio_form_view, name='portfolio_form'),
    path('portfolio/save/', views.save_portfolio, name='save_portfolio'),
    path('settings/', views.settings_view, name='settings'),
    path('settings/profile/', views.update_profile, name='update_profile'),
    path('settings/password/', views.update_password, name='update_password'),
    path('settings/notifications/', views.update_notifications, name='update_notifications'),
    path('form/', views.portfolio_form, name='portfolio_form'),
]