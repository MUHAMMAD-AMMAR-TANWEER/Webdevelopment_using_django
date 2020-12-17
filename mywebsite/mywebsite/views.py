# I created this file for editing and making the website
#to run the server type python manage.py runserver


from django.http import HttpResponse
from django.shortcuts import render




#to get the http response from server we use this
# def index(request):#We have to give a default parameter to the function
#     return HttpResponse("My name is Ammar")#We need to pass in this format
#
# def about(request):
#     return HttpResponse("I am Great in Machine learning")#This is second function which also displays on the page now here comes the third one
# def test_task(request):#We can display text files using this function so the challange has been solved
#     f = open('mywebsite/ammar.txt','r')
#     file_content = f.read()
#     f.close()
#     return HttpResponse(file_content, content_type="text/plain")
# #Now another challange occurs that is we have to put five links through which we can redirect
# def task2(request):#I put five links on my task2 page
#     return HttpResponse('''<h1>Muhammad Ammar</h1><a href="http://techphoenix.epizy.com/index/?i=1">Our website</a>
#     <a href="https://skrollo.com/">2 website</a>
#     <a href="https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py">3 website</a>
#     <a href="https://www.tensorflow.org/">4 website</a>
#     <a href="https://academy.tcm-sec.com/">5 website</a>''')
#############Above task is for video 6 now we will go to video 7
#We are building a documnet parser website and I have a challenge to add buttons to this website which will redirct to home page
# def index(request):
#     return HttpResponse("Home")
#
# def removepunc(request):
#     return HttpResponse('''<h1>remove punc</h1><a href="http://127.0.0.1:8000/"><button>Return Home</button></a>''')
#
# def capfirst(request):
#     return HttpResponse('''<h1>Capitalize letters</h1><a href="http://127.0.0.1:8000/"><button>Return Home</button></a>''')
#
# def newlineremove(request):
#     return HttpResponse('''<h1>line remover</h1><a href="http://127.0.0.1:8000/"><button>Return Home</button></a>''')
#
#
# def spaceremove(request):
#     return HttpResponse('''<h1>Space Remover</h1><a href="http://127.0.0.1:8000/"><button>Return Home</button></a>''')
#
# def charcount(request):
#     return HttpResponse('''<h1>Character Count</h1><a href="http://127.0.0.1:8000/"><button>Return Home</button></a>''')
#Above code is for video 7 now we are at video 8

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')#get the text in text box
    removepucc = request.GET.get('removepunc','off')#get the tick if ticked then on else off
    if removepucc == 'on':#if it is on then we perform backend
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("ERROR")

