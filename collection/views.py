from django.shortcuts import render



def index(request):
    context = {'segment': 'index'}
    return render(request, 'collection/index.html', context)



