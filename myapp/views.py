from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string, get_template
from .forms import LoginForm, RegisterForm, PortfolioForm
from .models import UserProfile, Portfolio
import logging
# from weasyprint import HTML  # Temporarily commented out
import tempfile
from django.db.models import Count
from django.utils import timezone

logger = logging.getLogger(__name__)

# Define choices
SEMESTER_CHOICES = [
    ('', 'Select Semester'),
    ('1', '1st Semester'),
    ('2', '2nd Semester'),
    ('3', '3rd Semester'),
    ('4', '4th Semester'),
    ('5', '5th Semester'),
    ('6', '6th Semester'),
    ('7', '7th Semester'),
    ('8', '8th Semester'),
]

# Create your views here.
@login_required
def portfolio_form(request):
    try:
        portfolio = Portfolio.objects.get(user=request.user)
        print("Loading portfolio for user:", request.user.username)
        print("Portfolio data:", {
            'studentName': portfolio.studentName,
            'usn': portfolio.usn,
            'email': portfolio.email,
            # Add more fields as needed
        })
    except Portfolio.DoesNotExist:
        portfolio = None
        print("No existing portfolio found")

    context = {
        'portfolio': portfolio,
        'semester_choices': SEMESTER_CHOICES
    }
    return render(request, 'form.html', context)

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'landing.html')

def logout_view(request):
    print(f"Logout request received. Method: {request.method}")  # Debug print
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
        return JsonResponse({'success': True, 'redirect_url': '/'})
    elif request.method == 'GET':
        logout(request)
        return redirect('home')
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

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
                messages.success(request, f'Welcome back, {user.profile.full_name}!')
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
            login(request, user)
            messages.success(request, f'Welcome, {user.profile.full_name}!')
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
    
    if user_profile.role == 'teacher':
        # Get all student portfolios with their related user profiles and project counts
        portfolios = Portfolio.objects.select_related(
            'user', 
            'user__profile'
        ).filter(
            user__profile__role='student'
        ).annotate(
            project_count=Count('projects')
        ).order_by('-updated_at')
        
        context = {
            'portfolios': portfolios,
            'user_profile': user_profile
        }
        return render(request, 'teacher_dashboard.html', context)
    else:
        try:
            portfolio = Portfolio.objects.get(user=request.user)
        except Portfolio.DoesNotExist:
            portfolio = None
            
        context = {
            'user_profile': user_profile,
            'portfolio': portfolio
        }
        return render(request, 'dashboard.html', context)

@login_required
def portfolio_form_view(request):
    if request.user.profile.role == 'teacher':
        messages.error(request, 'Teachers cannot create portfolios.')
        return redirect('dashboard')

    try:
        portfolio = Portfolio.objects.get(user=request.user)
    except Portfolio.DoesNotExist:
        portfolio = None

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            if 'resume' in request.FILES:
                portfolio.resume = request.FILES['resume']
            portfolio.save()
            messages.success(request, 'Portfolio saved successfully!')
            return redirect('dashboard')
    else:
        form = PortfolioForm(instance=portfolio)

    context = {
        'form': form,
        'portfolio': portfolio,
        'is_edit': portfolio is not None
    }
    return render(request, 'portfolio_form.html', context)

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
    if request.method != 'POST':
        return JsonResponse({'status': 'error',
                             'message': 'Invalid request method'}, status=405)

    try:
        # Get existing portfolio or create a new one
        portfolio, _ = Portfolio.objects.get_or_create(user=request.user)

        # ---------- Simple text / choice fields ----------
        simple_fields = [
            'studentName', 'usn', 'semester', 'email',
            'fatherName', 'motherName', 'address', 'parentContact',
            'tenthSchool', 'tenthBoard', 'tenthYear',
            'pucCollege', 'pucBoard', 'pucYear',
            'skills', 'certifications', 'projects', 'achievements',
        ]
        for field in simple_fields:
            if field in request.POST:
                setattr(portfolio, field, request.POST.get(field) or None)

        # ---------- Decimal / numeric fields ----------
        numeric_fields = ['tenthPercentage', 'pucPercentage', 'cgpa']
        for field in numeric_fields:
            value = request.POST.get(field, '').strip()
            if value:
                try:
                    setattr(portfolio, field, float(value))
                except ValueError:
                    # Ignore bad numeric input but keep processing
                    continue

        # ---------- SGPA loop (sem1_sgpa … sem8_sgpa) ----------
        for i in range(1, 9):
            field = f'sem{i}_sgpa'
            value = request.POST.get(field, '').strip()
            if value:
                try:
                    setattr(portfolio, field, float(value))
                except ValueError:
                    continue

        # ---------- File upload (resume) ----------
        if 'resume' in request.FILES:
            portfolio.resume = request.FILES['resume']

        portfolio.save()

        # ---------- Sync basic info back to UserProfile ----------
        profile = request.user.profile
        profile.full_name = portfolio.studentName or profile.full_name
        profile.usn = portfolio.usn or profile.usn
        profile.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Portfolio saved successfully',
            'data': {
                'studentName': portfolio.studentName,
                'usn': portfolio.usn,
                'semester': portfolio.semester,
                'email': portfolio.email,
                'cgpa': portfolio.cgpa,
                # include more fields if your front-end needs them
            }
        })

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


# ──────────────────────────────────────────────────────────────────────
# SHOW THE LOGGED-IN USER'S PORTFOLIO (student view)
# ──────────────────────────────────────────────────────────────────────
@login_required
def portfolio_view(request):
    try:
        portfolio = Portfolio.objects.get(user=request.user)
    except Portfolio.DoesNotExist:
        portfolio = None

    context = {
        'portfolio': portfolio,
        'semester_choices': SEMESTER_CHOICES,
    }
    return render(request, 'form.html', context)


# ──────────────────────────────────────────────────────────────────────
# AJAX END-POINT TO GET PORTFOLIO CONTENT SNIPPET
# ──────────────────────────────────────────────────────────────────────
@login_required
def get_portfolio(request):
    try:
        portfolio = Portfolio.objects.get(user=request.user)
    except Portfolio.DoesNotExist:
        portfolio = None

    html = render_to_string('portfolio_content.html', {
        'portfolio': portfolio,
        'user_profile': request.user.profile,
    })
    return JsonResponse({'html': html})


# ──────────────────────────────────────────────────────────────────────
# DOWNLOAD PORTFOLIO AS PDF (placeholder HTML response for now)
# ──────────────────────────────────────────────────────────────────────
@login_required
def download_portfolio(request):
    try:
        portfolio = Portfolio.objects.get(user=request.user)
    except Portfolio.DoesNotExist:
        messages.error(request, 'Portfolio not found.')
        return redirect('dashboard')

    template = get_template('portfolio_pdf.html')
    html_string = template.render({
        'portfolio': portfolio,
        'user_profile': request.user.profile,
    })
    return HttpResponse(html_string, content_type='text/html')
    # Replace with real PDF logic later


# ──────────────────────────────────────────────────────────────────────
# TEACHER-ONLY VIEW OF A STUDENT’S PORTFOLIO
# ──────────────────────────────────────────────────────────────────────
@login_required
def view_portfolio(request, portfolio_id):
    if request.user.profile.role != 'teacher':
        messages.error(request, 'Only teachers can view student portfolios.')
        return redirect('dashboard')

    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    context = {
        'portfolio': portfolio,
        'user_profile': portfolio.user.profile,
        'view_only': True,
    }
    return render(request, 'form.html', context)
