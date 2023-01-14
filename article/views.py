from django.shortcuts import render


def show_articles(request):
    return render(request, 'index.html')
