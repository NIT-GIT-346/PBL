from django.shortcuts import render, redirect
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
        # Get all student portfolios with their related user profiles
        portfolios = Portfolio.objects.select_related(
            'user', 
            'user__profile'
        ).filter(
            user__profile__role='student'
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
def portfolio_view(request):
    print("\n=== Loading Portfolio View ===")
    print("User:", request.user.username)
    
    try:
        portfolio = Portfolio.objects.get(user=request.user)
        print("Found portfolio with data:", {
            'studentName': portfolio.studentName,
            'usn': portfolio.usn,
            'email': portfolio.email,
            'fatherName': portfolio.fatherName,
            'motherName': portfolio.motherName,
            'address': portfolio.address,
            'parentContact': portfolio.parentContact,
            'tenthPercentage': portfolio.tenthPercentage,
            'tenthSchool': portfolio.tenthSchool,
            'tenthBoard': portfolio.tenthBoard,
            'tenthYear': portfolio.tenthYear,
            'pucPercentage': portfolio.pucPercentage,
            'pucCollege': portfolio.pucCollege,
            'pucBoard': portfolio.pucBoard,
            'pucYear': portfolio.pucYear,
            'cgpa': portfolio.cgpa,
            'skills': portfolio.skills,
            'certifications': portfolio.certifications,
            'sem1_sgpa': portfolio.sem1_sgpa,
            'sem2_sgpa': portfolio.sem2_sgpa,
            'sem3_sgpa': portfolio.sem3_sgpa,
            'sem4_sgpa': portfolio.sem4_sgpa,
            'sem5_sgpa': portfolio.sem5_sgpa,
            'sem6_sgpa': portfolio.sem6_sgpa,
            'sem7_sgpa': portfolio.sem7_sgpa,
            'sem8_sgpa': portfolio.sem8_sgpa
        })
    except Portfolio.DoesNotExist:
        portfolio = None
        print("No portfolio found for user")

    context = {
        'portfolio': portfolio,
        'semester_choices': SEMESTER_CHOICES
    }
    return render(request, 'form.html', context)

@login_required
def get_portfolio(request):
    """Return portfolio data as HTML for AJAX loading"""
    try:
        portfolio = Portfolio.objects.get(user=request.user)
    except Portfolio.DoesNotExist:
        portfolio = None
    
    html = render_to_string('portfolio_content.html', {
        'portfolio': portfolio,
        'user_profile': request.user.profile
    })
    return JsonResponse({'html': html})

@login_required
def download_portfolio(request):
    """Generate and download portfolio as PDF"""
    try:
        portfolio = Portfolio.objects.get(user=request.user)
    except Portfolio.DoesNotExist:
        messages.error(request, 'Portfolio not found.')
        return redirect('dashboard')

    # Render the template with portfolio data
    template = get_template('portfolio_pdf.html')
    html_string = template.render({
        'portfolio': portfolio,
        'user_profile': request.user.profile
    })

    # Temporarily return a simple response instead of PDF
    response = HttpResponse(html_string, content_type='text/html')
    return response
    
    # PDF generation code commented out temporarily
    # pdf_file = HTML(string=html_string).write_pdf()
    # response = HttpResponse(pdf_file, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="portfolio.pdf"'
    # return response

@login_required
def save_portfolio(request):
    if request.method == 'POST':
        print("\n=== DEBUG: Portfolio Save Process ===")
        print("User:", request.user.username)
        print("POST data received:", request.POST)

        try:
            portfolio = Portfolio.objects.get(user=request.user)
            print("Found existing portfolio for user")
        except Portfolio.DoesNotExist:
            portfolio = None
            print("Creating new portfolio")

        # Create/update portfolio directly
        if portfolio is None:
            portfolio = Portfolio(user=request.user)
        
        # Update fields directly
        fields = [
            'studentName', 'usn', 'semester', 'email', 'fatherName', 'motherName',
            'address', 'parentContact', 'tenthPercentage', 'tenthSchool',
            'tenthBoard', 'tenthYear', 'pucPercentage', 'pucCollege',
            'pucBoard', 'pucYear', 'cgpa', 'skills', 'certifications'
        ]
        
        for field in fields:
            if field in request.POST:
                print(f"Setting {field} = {request.POST[field]}")
                setattr(portfolio, field, request.POST[field])

        # Handle SGPA fields
        for i in range(1, 9):
            field = f'sem{i}_sgpa'
            value = request.POST.get(field, '')
            print(f"Processing {field} = {value}")  # Debug print
            if value.strip():  # Only set if value is not empty
                try:
                    float_value = float(value)
                    print(f"Setting {field} = {float_value}")
                    setattr(portfolio, field, float_value)
                except ValueError:
                    print(f"Invalid value for {field}: {value}")
                    continue

        try:
            portfolio.save()
            print("Portfolio saved successfully")
            print("Saved data:", {
                'studentName': portfolio.studentName,
                'usn': portfolio.usn,
                'email': portfolio.email,
                'skills': portfolio.skills,
                'certifications': portfolio.certifications,
                'sem1_sgpa': portfolio.sem1_sgpa,
                'sem2_sgpa': portfolio.sem2_sgpa,
                'sem3_sgpa': portfolio.sem3_sgpa,
                'sem4_sgpa': portfolio.sem4_sgpa,
                'sem5_sgpa': portfolio.sem5_sgpa,
                'sem6_sgpa': portfolio.sem6_sgpa,
                'sem7_sgpa': portfolio.sem7_sgpa,
                'sem8_sgpa': portfolio.sem8_sgpa
            })
            
            return JsonResponse({
                'status': 'success',
                'message': 'Portfolio saved successfully',
                'data': {
                    'studentName': portfolio.studentName,
                    'usn': portfolio.usn,
                    'email': portfolio.email,
                    'semester': portfolio.semester,
                    'fatherName': portfolio.fatherName,
                    'motherName': portfolio.motherName,
                    'address': portfolio.address,
                    'parentContact': portfolio.parentContact,
                    'tenthPercentage': portfolio.tenthPercentage,
                    'tenthSchool': portfolio.tenthSchool,
                    'tenthBoard': portfolio.tenthBoard,
                    'tenthYear': portfolio.tenthYear,
                    'pucPercentage': portfolio.pucPercentage,
                    'pucCollege': portfolio.pucCollege,
                    'pucBoard': portfolio.pucBoard,
                    'pucYear': portfolio.pucYear,
                    'cgpa': portfolio.cgpa,
                    'skills': portfolio.skills,
                    'certifications': portfolio.certifications,
                    'sem1_sgpa': portfolio.sem1_sgpa,
                    'sem2_sgpa': portfolio.sem2_sgpa,
                    'sem3_sgpa': portfolio.sem3_sgpa,
                    'sem4_sgpa': portfolio.sem4_sgpa,
                    'sem5_sgpa': portfolio.sem5_sgpa,
                    'sem6_sgpa': portfolio.sem6_sgpa,
                    'sem7_sgpa': portfolio.sem7_sgpa,
                    'sem8_sgpa': portfolio.sem8_sgpa
                }
            })
        except Exception as e:
            print("Error saving portfolio:", str(e))
            return JsonResponse({
                'status': 'error',
                'message': f'Error saving portfolio: {str(e)}'
            }, status=500)

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=405)
