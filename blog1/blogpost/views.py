import datetime

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from .models import BlogPost
# Create your views here.


def archive(request):
    now = datetime.datetime.now()
    url = reverse("blogpost:archive")
    posts = BlogPost.objects.all()

    return render_to_response("archive.html", locals())