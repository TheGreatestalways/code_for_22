from django.shortcuts import render
from django.http import HttpResponse

#
# def index(request):
#     return HttpResponse('Answer')


def index(request):
    return render(request, 'index.html')
# Create your views here.

def top_sellers(request):
    return render(request, 'top-sellers.html')

# Унаследуйте шаблон «top-sellers.html» от
# шаблона «base.html». По аналогии с шаблоном «index.html» уберите
# лишнее и наполните {% block content %} контентом данного шаблона.
# Также Поменяйте все доступные (указанные в url-ах) ссылки в шаблонах
# «index.html» и «top-sellers.html»
# на новые при помощи шаблон-тега {% url <> %}.