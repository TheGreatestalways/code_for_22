from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Advertisement
from .forms import AdvertisementForm


# def index(request):
#     return ('УспешнHttpResponseо!')


def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context=context)


def top_sellers(request):
    return render(request, 'top-sellers.html')


def adv_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            # advertisement.user = User.objects.all()[0] альтернатива
            advertisement.save()
            url = reverse('main_page')
            return redirect(url)
    elif request.method == "GET":
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context=context)

