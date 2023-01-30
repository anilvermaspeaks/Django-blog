from django.shortcuts import render

# Create your views here.


def starting_page(request):
    return render(request, "blog/index.html")


def posts(requests):
    pass


def post_detail(request):
    pass
