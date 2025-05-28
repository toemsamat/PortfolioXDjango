from django.db import models
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    name = models.CharField(max_length=100)
    headline = models.CharField(max_length=200)
    bio = models.TextField()
    profile_picture = CloudinaryField('image', folder='profiles/')
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=100, blank=True)
    resume = models.FileField(upload_to='resume/', blank=True)
    
    github = models.URLField(blank=True)
    github_icon = models.CharField(max_length=100, default="fab fa-github", blank=True)
    github_color = models.CharField(max_length=20, default="#333", blank=True)

    linkedin = models.URLField(blank=True)
    linkedin_icon = models.CharField(max_length=100, default="fab fa-linkedin", blank=True)
    linkedin_color = models.CharField(max_length=20, default="#0A66C2", blank=True)

    twitter = models.URLField(blank=True)
    twitter_icon = models.CharField(max_length=100, default="fab fa-twitter", blank=True)
    twitter_color = models.CharField(max_length=20, default="#1DA1F2", blank=True)

    instagram = models.URLField(blank=True)
    instagram_icon = models.CharField(max_length=100, default="fab fa-instagram", blank=True)
    instagram_color = models.CharField(max_length=20, default="#C13584", blank=True)

    facebook = models.URLField(blank=True)
    facebook_icon = models.CharField(max_length=100, default="fab fa-facebook-f", blank=True)
    facebook_color = models.CharField(max_length=20, default="#1877F2", blank=True)


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=50)
    percentage = models.PositiveIntegerField(help_text="Skill level as a percentage (0-100)")
    icon_class = models.CharField(max_length=100, blank=True, help_text="Font Awesome class (e.g., 'fab fa-html5')")
    icon_color = models.CharField(max_length=20, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.percentage}%"


class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image', folder='projects/')
    github_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)
    tech_stack = models.CharField(max_length=255)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = CloudinaryField('image', folder='certificates/', blank=True, null=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cover_image = CloudinaryField('image', folder='blog/', blank=True)
    slug = models.SlugField(unique=True)


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
