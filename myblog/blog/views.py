from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm
from django.http import HttpResponseNotFound
import requests


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})


class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})


class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


def index(request):
    try:
        city = 'Obinitsa'
        params = {'q': city, 'units': 'metric', 'lang': 'ru', 'appid': '1912624fd*************f90fd4a0b'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        res = response.json()
        city_info = {'city': city, 'temp': round(res['main']['temp']), 'icon': res['weather'][0]['icon'], 'x': res['weather'][0]['description']}

    except:
        raise
    context = {'info': city_info}

    return render(request, 'blog/weather.html', context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Такой страницы нет</h1>')


