from django.shortcuts import render


def mian_page(request):
    return render(request, 'articles/index.html')
