from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# def home(request):
#     html = '''
#     <html>
#     <body>
#     <h1>Asosiy sahifa</h1>
#     <h3>Asosiy sahifa</h3>
#     <h6>Asosiy sahifa</h6>
#     <p>Salom saytimizga xush kelibsiz</p>
#     </body>
#     </html>
#     '''
#     return HttpResponse(html)


def home(request):

    return render(request, 'main/home.html')

def salom():
    print('Salom')

def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')