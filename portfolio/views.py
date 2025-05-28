from django.shortcuts import render, redirect, get_object_or_404
from .models import Certificate, Profile, Skill, Experience, Project, BlogPost, ContactMessage
from django.core.mail import EmailMessage
from django.conf import settings

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.filter(featured=True)
    return render(request, 'portfolio/home.html', {'profile': profile, 'projects': projects})

def about(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all()

    frontend_skills = Skill.objects.filter(category='Frontend')
    backend_skills = Skill.objects.filter(category='Backend')
    other_skills = Skill.objects.filter(category='Other')

    return render(request, 'portfolio/about.html', {
        'profile': profile,
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
        'other_skills': other_skills,
        'experiences': experiences,
    })

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def resume(request):
    profile = Profile.objects.first()
    return render(request, 'portfolio/resume.html', {'profile': profile})

def certificate(request):
    certificates = Certificate.objects.all()
    return render(request, 'portfolio/certificate.html', {'certificates': certificates})

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'portfolio/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'portfolio/blog_detail.html', {'post': post})

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if first_name and last_name and email and message:
            ContactMessage.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                message=message
            )

            subject = f"New Contact Message from {first_name} {last_name}"
            full_message = f"From: {first_name} {last_name} <{email}>\n\nMessage:\n{message}"

            email_msg = EmailMessage(
                subject=subject,
                body=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email]
            )
            email_msg.send(fail_silently=False)

            return render(request, 'portfolio/contact.html', {
                'success': True,
            })

        return render(request, "portfolio/contact.html", {
            "error": "Please fill in all fields."
        })

    return render(request, 'portfolio/contact.html')
