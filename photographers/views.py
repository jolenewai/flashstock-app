from django.shortcuts import render
from .models import Photographer
from .forms import PhotographerForm


def create_profile(request):
    form = PhotographerForm()
    return render(request, 'photographers/create_profile.template.html', {
        'form': form
    })

