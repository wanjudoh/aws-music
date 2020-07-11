from django.shortcuts import render, redirect
from .models import Music
from .forms import MusicForm

# Create your views here.
def main(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save(commit=False)
            music.save()
            return redirect('main')
    else:
        musics = Music.objects.all
        form = MusicForm()
        return render(request, 'main.html', {'form': form, 'musics': musics})