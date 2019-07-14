from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import PersonForm

def index(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = PersonForm()
    return render(request, 'app/index.html', {'form':form})
