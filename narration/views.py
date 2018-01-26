from django.shortcuts import render
from .forms import ContentForm

# Create your views here.
def home(request):
    form=ContentForm()
    return render(request, "narration/home.html", {"form":form})
