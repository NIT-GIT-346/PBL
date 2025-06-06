from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# UserProfile model
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    full_name = models.CharField(max_length=255)
    usn = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=100)
    semester = models.CharField(max_length=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name}'s Profile"

# Portfolio model
class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Personal Details
    studentName = models.CharField(max_length=255, null=True, blank=True)
    usn = models.CharField(max_length=20, null=True, blank=True)
    semester = models.CharField(max_length=2, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    fatherName = models.CharField(max_length=255, null=True, blank=True)
    motherName = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    parentContact = models.CharField(max_length=20, null=True, blank=True)

    # Academic Performance
    tenthPercentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    tenthSchool = models.CharField(max_length=255, null=True, blank=True)
    tenthBoard = models.CharField(max_length=100, null=True, blank=True)
    tenthYear = models.IntegerField(null=True, blank=True)

    pucPercentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    pucCollege = models.CharField(max_length=255, null=True, blank=True)
    pucBoard = models.CharField(max_length=100, null=True, blank=True)
    pucYear = models.IntegerField(null=True, blank=True)

    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    # UG Progress Report
    sem1_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem2_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem3_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem4_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem5_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem6_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem7_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem8_sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    # Additional Information
    skills = models.TextField(null=True, blank=True)
    certifications = models.TextField(null=True, blank=True)
    projects = models.TextField(null=True, blank=True)
    achievements = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.studentName}'s Portfolio" if self.studentName else f"{self.user.username}'s Portfolio"

# Signals
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

