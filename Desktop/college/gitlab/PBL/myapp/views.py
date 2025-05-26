from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, RegisterForm, PortfolioForm
from .models import UserProfile, Portfolio
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'landing.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.profile.full_name or user.email}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(
                user=user,
                role=form.cleaned_data['role'],
                department=form.cleaned_data['department'],
                designation=form.cleaned_data['designation']
            )
            login(request, user)
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard_view(request):
    user_profile = request.user.profile
    
    # Check user role and redirect to appropriate dashboard
    if user_profile.role == 'teacher':
        portfolios = Portfolio.objects.all().select_related('user__profile').order_by('-created_at')
        return render(request, 'teacher_dashboard.html', {
            'portfolios': portfolios
        })
    else:
        # Student dashboard
        portfolio_entries = Portfolio.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'dashboard.html', {
            'user_profile': user_profile,
            'portfolio_entries': portfolio_entries
        })

@login_required
def portfolio_form_view(request):
    try:
        portfolio = Portfolio.objects.get(user=request.user)
        is_edit = request.GET.get('edit', '').lower() == 'true'
    except Portfolio.DoesNotExist:
        portfolio = None
        is_edit = False

    print("DEBUG is_edit:", is_edit, "request.GET:", request.GET)  # Debug print

    # If viewing as teacher
    if request.user.profile.role == 'teacher' and request.GET.get('view'):
        try:
            portfolio = Portfolio.objects.get(id=request.GET.get('view'))
            is_edit = False
        except Portfolio.DoesNotExist:
            messages.error(request, 'Portfolio not found')
            return redirect('dashboard')

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            if 'resume' in request.FILES:
                portfolio.resume = request.FILES['resume']
            portfolio.save()
            return redirect('dashboard')
    else:
        form = PortfolioForm(instance=portfolio)

    context = {
        'form': form,
        'portfolio': portfolio,
        'is_edit': is_edit,
        'semester_choices': [
            ('1', '1st Semester'),
            ('2', '2nd Semester'),
            ('3', '3rd Semester'),
            ('4', '4th Semester'),
            ('5', '5th Semester'),
            ('6', '6th Semester'),
            ('7', '7th Semester'),
            ('8', '8th Semester'),
        ]
    }
    return render(request, 'form.html', context)

@login_required
def settings_view(request):
    return render(request, 'settings.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        profile = request.user.profile
        profile.full_name = request.POST.get('full_name', '')
        profile.usn = request.POST.get('usn', '')
        profile.department = request.POST.get('department', '')
        profile.phone = request.POST.get('phone', '')
        profile.address = request.POST.get('address', '')
        profile.save()
        messages.success(request, 'Profile updated successfully!')
    return redirect('settings')

@login_required
def update_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if not request.user.check_password(current_password):
            messages.error(request, 'Current password is incorrect.')
        elif new_password != confirm_password:
            messages.error(request, 'New passwords do not match.')
        else:
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, 'Password updated successfully!')
    return redirect('settings')

@login_required
def update_notifications(request):
    if request.method == 'POST':
        profile = request.user.profile
        profile.email_notifications = request.POST.get('email_notifications') == 'on'
        profile.achievement_alerts = request.POST.get('achievement_alerts') == 'on'
        profile.save()
        messages.success(request, 'Notification preferences updated successfully!')
    return redirect('settings')

@login_required
def save_portfolio(request):
    if request.method == 'POST':
        try:
            portfolio = Portfolio.objects.get(user=request.user)
            form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        except Portfolio.DoesNotExist:
            form = PortfolioForm(request.POST, request.FILES)

        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            if 'resume' in request.FILES:
                portfolio.resume = request.FILES['resume']
            portfolio.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

from django.shortcuts import render

def form_view(request):
    return render(request, 'form.html')

