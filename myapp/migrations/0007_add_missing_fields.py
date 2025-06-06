from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20250606_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
    ] 