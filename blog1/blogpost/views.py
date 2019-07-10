from django.shortcuts import render_to_response

# Create your views here.
from .models import BlogPost


def archive(request):
    posts = BlogPost.objects.all()
    return render_to_response("archive.html", locals())