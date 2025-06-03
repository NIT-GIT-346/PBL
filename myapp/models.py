from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

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

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    studentName = models.CharField(max_length=255, blank=True, null=True)
    usn = models.CharField(max_length=20, blank=True, null=True)
    semester = models.CharField(max_length=2, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fatherName = models.CharField(max_length=255, blank=True, null=True)
    motherName = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    parentContact = models.CharField(max_length=15, blank=True, null=True)
    tenthPercentage = models.FloatField(blank=True, null=True)
    tenthSchool = models.CharField(max_length=255, blank=True, null=True)
    tenthBoard = models.CharField(max_length=100, blank=True, null=True)
    tenthYear = models.IntegerField(blank=True, null=True)
    pucPercentage = models.FloatField(blank=True, null=True)
    pucCollege = models.CharField(max_length=255, blank=True, null=True)
    pucBoard = models.CharField(max_length=100, blank=True, null=True)
    pucYear = models.IntegerField(blank=True, null=True)
    cgpa = models.FloatField(null=True, blank=True)
    sem1_sgpa = models.FloatField(null=True, blank=True)
    sem2_sgpa = models.FloatField(null=True, blank=True)
    sem3_sgpa = models.FloatField(null=True, blank=True)
    sem4_sgpa = models.FloatField(null=True, blank=True)
    sem5_sgpa = models.FloatField(null=True, blank=True)
    sem6_sgpa = models.FloatField(null=True, blank=True)
    sem7_sgpa = models.FloatField(null=True, blank=True)
    sem8_sgpa = models.FloatField(null=True, blank=True)
    skills = models.TextField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Portfolio"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
