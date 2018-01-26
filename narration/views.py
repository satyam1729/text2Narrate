from django.shortcuts import render
from .forms import ContentForm
from django.utils import timezone
# Create your views here.
def home(request):
    if request.method == "POST":
        form=ContentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()    
    else:    
        form=ContentForm()
    return render(request, "narration/home.html", {"form":form})
