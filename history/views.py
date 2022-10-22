from django.shortcuts import render



def index(request):
    context = {'segment': 'index'}
    return render(request, 'history/index.html', context)



