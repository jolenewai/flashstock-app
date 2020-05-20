from django.shortcuts import render
from .models import Photographer
from .forms import PhotographerForm


def sign_up(request):
    form = PhotographerForm()
    return render(request, 'photographers/signup.template.html', {
        'form': form
    })

