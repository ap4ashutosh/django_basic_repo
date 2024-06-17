from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'ap4ashutosh',
        'title': 'Django 101',
        'content': 'First posted content',
        'date': '09-02-2021'
    },
    {
        'author': 'arhat j',
        'title': 'Flask 101',
        'content': 'First posted content',
        'date': '16-02-2021'
    }
]


def home(request):
    context = {'posts':posts}
    return render(request, 'blog/templates.html', context)

def about(request):
    # return HttpResponse('<h1>Blog about</h1>')
    return render(request, 'blog/about.html', {'title':'about'})