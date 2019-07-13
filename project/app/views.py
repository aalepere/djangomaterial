from django.shortcuts import render
from django.http import HttpResponse
from .models import Test

def index(request):
    list_input = Test.objects.all()
    context = {'list_input':list_input}
    return render(request, 'app/index.html', context)
