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
    full_name = models.CharField(max_length=100, blank=True)
    usn = models.CharField(max_length=20, blank=True)
    department = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    email_notifications = models.BooleanField(default=True)
    achievement_alerts = models.BooleanField(default=True)
    profile_views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    studentName = models.CharField(max_length=255)
    usn = models.CharField(max_length=20)
    semester = models.CharField(max_length=2)
    email = models.EmailField()
    fatherName = models.CharField(max_length=255)
    motherName = models.CharField(max_length=255)
    address = models.TextField()
    parentContact = models.CharField(max_length=15)
    tenthPercentage = models.FloatField()
    tenthSchool = models.CharField(max_length=255)
    tenthBoard = models.CharField(max_length=100)
    tenthYear = models.IntegerField()
    pucPercentage = models.FloatField()
    pucCollege = models.CharField(max_length=255)
    pucBoard = models.CharField(max_length=100)
    pucYear = models.IntegerField()
    cgpa = models.FloatField()
    sem1_sgpa = models.FloatField(null=True, blank=True)
    sem2_sgpa = models.FloatField(null=True, blank=True)
    sem3_sgpa = models.FloatField(null=True, blank=True)
    sem4_sgpa = models.FloatField(null=True, blank=True)
    sem5_sgpa = models.FloatField(null=True, blank=True)
    sem6_sgpa = models.FloatField(null=True, blank=True)
    sem7_sgpa = models.FloatField(null=True, blank=True)
    sem8_sgpa = models.FloatField(null=True, blank=True)
    skills = models.TextField()
    certifications = models.TextField()
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.studentName}'s Portfolio"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
