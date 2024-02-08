from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, Sassy, Nonchalant, anxious, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html', )
    return HttpResponse("<a href='/rango/'>Back to Index</a>")