from django.shortcuts import render
from .forms import ContentForm
from django.utils import timezone
from hparams import hparams, hparams_debug_string
from synthesizer import Synthesizer
import os
# Create your views here.

#print(type(post.title))            
synthesizer = Synthesizer()
hparams.parse("")
cwd = os.getcwd()
checkpoint=cwd+"/narration/saved_model/tacotron-20170720/model.ckpt"
print(checkpoint)
synthesizer.load(checkpoint)


def home(request):
    if request.method == "POST":
        form=ContentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            synthesizer.synthesize(post.text,post.title)
            post.created_date = timezone.now()
            post.save()
    else:    
        form=ContentForm()
    return render(request, "narration/home.html", {"form":form})
