from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.contrib import messages



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    return render(request, 'dashboard/index.html', context)

def profile(request):
    context = {'segment': 'profile'}
    return render(request, 'dashboard/profile.html', context)

@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(
        request,
        messages.INFO,
        'You have been successfully logged out. Thank you ' +
        'for using reNgine.')


@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    messages.add_message(
        request,
        messages.INFO,
        'Hi @' +
        request.user.username +
        ' welcome back!')
