from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Portfolio

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
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
            'placeholder': 'Enter your email'
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
    role = forms.ChoiceField(
        choices=UserProfile.ROLE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary'
        })
    )
    department = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
            'placeholder': 'Enter your department'
        })
    )
    designation = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
            'placeholder': 'Enter your designation'
        })
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'role', 'department', 'designation']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']  # Use email as username
        if commit:
            user.save()
            # Update the user profile
            user.profile.full_name = self.cleaned_data['full_name']
            user.profile.usn = self.cleaned_data['usn']
            user.profile.department = self.cleaned_data['department']
            user.profile.phone = self.cleaned_data['phone']
            user.profile.address = self.cleaned_data['address']
            user.profile.save()
        return user

class PortfolioForm(forms.ModelForm):
    studentName = forms.CharField(required=True)
    usn = forms.CharField(required=True)
    semester = forms.ChoiceField(choices=[(str(i), f"{i}st Semester") for i in range(1, 9)], required=True)
    email = forms.EmailField(required=True)
    fatherName = forms.CharField(required=True)
    motherName = forms.CharField(required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    parentContact = forms.CharField(required=True)
    tenthPercentage = forms.FloatField(required=True)
    tenthSchool = forms.CharField(required=True)
    tenthBoard = forms.CharField(required=True)
    tenthYear = forms.IntegerField(required=True)
    pucPercentage = forms.FloatField(required=True)
    pucCollege = forms.CharField(required=True)
    pucBoard = forms.CharField(required=True)
    pucYear = forms.IntegerField(required=True)
    cgpa = forms.FloatField(required=True)
    sem1_sgpa = forms.FloatField(required=False)
    sem2_sgpa = forms.FloatField(required=False)
    sem3_sgpa = forms.FloatField(required=False)
    sem4_sgpa = forms.FloatField(required=False)
    sem5_sgpa = forms.FloatField(required=False)
    sem6_sgpa = forms.FloatField(required=False)
    sem7_sgpa = forms.FloatField(required=False)
    sem8_sgpa = forms.FloatField(required=False)
    skills = forms.CharField(widget=forms.Textarea, required=True)
    certifications = forms.CharField(widget=forms.Textarea, required=True)
    resume = forms.FileField(required=False)

    class Meta:
        model = Portfolio
        fields = [
            'studentName', 'usn', 'semester', 'email', 'fatherName', 'motherName',
            'address', 'parentContact', 'tenthPercentage', 'tenthSchool', 'tenthBoard',
            'tenthYear', 'pucPercentage', 'pucCollege', 'pucBoard', 'pucYear',
            'cgpa', 'sem1_sgpa', 'sem2_sgpa', 'sem3_sgpa', 'sem4_sgpa',
            'sem5_sgpa', 'sem6_sgpa', 'sem7_sgpa', 'sem8_sgpa',
            'skills', 'certifications', 'resume'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
                'placeholder': 'Enter project title'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
                'placeholder': 'Describe your project',
                'rows': '4'
            }),
            'technologies': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
                'placeholder': 'e.g., Python, Django, React'
            }),
            'project_url': forms.URLInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary',
                'placeholder': 'https://github.com/username/project'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary'
            })
        } 