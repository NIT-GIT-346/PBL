from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Portfolio

DEPARTMENT_CHOICES = [
    ('CSE', 'Computer Science & Engineering'),
    ('ISE', 'Information Science & Engineering'),
    ('ECE', 'Electronics & Communication Engineering'),
    ('EEE', 'Electrical & Electronics Engineering'),
    ('ME', 'Mechanical Engineering'),
    ('CV', 'Civil Engineering')
]

SEMESTER_CHOICES = [
    ('', 'Select Semester'),  # Adding this as placeholder
    ('1', '1st Semester'),
    ('2', '2nd Semester'),
    ('3', '3rd Semester'),
    ('4', '4th Semester'),
    ('5', '5th Semester'),
    ('6', '6th Semester'),
    ('7', '7th Semester'),
    ('8', '8th Semester'),
]

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
            'placeholder': 'Enter your email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
            'placeholder': 'Enter your password'
        })
    )

class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=UserProfile.ROLE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
            'placeholder': 'Enter your email'
        })
    )
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
            'placeholder': 'Enter your full name'
        })
    )
    usn = forms.CharField(
        required=False,  # Make it optional initially
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
            'placeholder': 'Enter your USN'
        })
    )
    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary'
        })
    )
    semester = forms.ChoiceField(
        required=False,  # Make it optional initially
        choices=SEMESTER_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
            'placeholder': 'Enter your password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
            'placeholder': 'Confirm your password'
        })
    )

    class Meta:
        model = User
        fields = ['role', 'email', 'full_name', 'usn', 'department', 'semester', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        usn = cleaned_data.get('usn')
        semester = cleaned_data.get('semester')

        # If role is student, make USN and semester required
        if role == 'student':
            if not usn:
                self.add_error('usn', 'USN is required for students')
            if not semester:
                self.add_error('semester', 'Semester is required for students')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
            user.profile.role = self.cleaned_data['role']
            user.profile.full_name = self.cleaned_data['full_name']
            user.profile.department = self.cleaned_data['department']
            
            # Only set USN and semester for students
            if self.cleaned_data['role'] == 'student':
                user.profile.usn = self.cleaned_data['usn']
                user.profile.semester = self.cleaned_data['semester']
            
            user.profile.save()
        return user

class PortfolioForm(forms.ModelForm):
    skills = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
            'placeholder': 'List your technical and soft skills',
            'rows': '4'
        })
    )
    certifications = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
            'placeholder': 'List your certifications and courses',
            'rows': '4'
        })
    )
    projects = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
            'placeholder': 'Describe your projects',
            'rows': '4'
        })
    )
    achievements = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
            'placeholder': 'List your achievements and awards',
            'rows': '4'
        })
    )
    resume = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary'
        })
    )

    class Meta:
        model = Portfolio
        fields = ['skills', 'certifications', 'projects', 'achievements', 'resume'] 