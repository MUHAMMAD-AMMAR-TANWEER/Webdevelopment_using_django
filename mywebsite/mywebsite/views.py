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
# def index(request):
#     return render(request, 'index.html')
# def removepunc(request):
#
#     #now we get the response which user submit in the form through below command
#     djreturns = request.GET.get('text','defaut')
#     print(djreturns)
#     return HttpResponse("remove punc")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")
#The above code is for video ten and eleven now its time to code for real video twelve
def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')#Line to get text from the form
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numberremover = request.POST.get('numberremover', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                if not (djtext[index] == " "):
                    analyzed = analyzed + char

            elif not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (
            removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and numberremover != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')