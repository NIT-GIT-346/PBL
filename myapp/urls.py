from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('portfolio/add/', views.portfolio_form_view, name='portfolio_form'),
    path('portfolio/save/', views.save_portfolio, name='save_portfolio'),
    path('portfolio/get/', views.get_portfolio, name='get_portfolio'),
    path('portfolio/download/', views.download_portfolio, name='download_portfolio'),
    path('settings/', views.settings_view, name='settings'),
    path('settings/profile/', views.update_profile, name='update_profile'),
    path('settings/password/', views.update_password, name='update_password'),
    path('settings/notifications/', views.update_notifications, name='update_notifications'),
    path('form/', views.portfolio_form, name='portfolio_form'),
]