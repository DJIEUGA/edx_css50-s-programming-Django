from django.shortcuts import render       
from django.http import Http404, HttpResponse, JsonResponse
import time

# Create your views here.

def index(request):
    return render(request, 'home/index.html')
def greet(request, name):
    return render(request, 'home/greet.html', {
        'name': name.capitalize()
    })

def singlepage(request):
    return render(request, 'singlepage/index.html')

texts = [ 
    'Text 1 lorem ipsomjsddjsdsjdhjdjsdjsdskjdsjdjsdjsdsjdskjd ssdjslkdjsaodids sdkshdkjshdsajdsad skdusdsahd sdksadhaksdsd sdsuhdsdjoiaddjpoisdpsa sidhsad', 
    'Text 2 sth ewiajd uasodosdodsdnsjdssdh sdaabaawiwdajwowpapjad didioeiurb ju nythsaodalaufewij uwaiuiefnaaioL uufeyuejhifkweorijn uiueiuffe iuifeuowq;foijaoffhufn hguaygif', 
    'Text 3 uo ooduhf trhetjj dudospweijffueu duwiiwkfdjnnookdihf yrieodnhussaodfjfnfuffnf idjdodihnkkdndhdhdijusjsodsj usjsoseydhjkwlewfjdkfkdfkjsijslkjdldourdifjdkudfdfjdnf',
    ]
def section(request, num):
    if 1 <= num <= 3:
       return HttpResponse(texts[num - 1])
    else:
        raise Http404('No such section')
    

def posts_view(request):
    return render(request, 'posts/index.html')

def posts(request):

    # Get start and end points
    start = int(request.GET.get('start') or 0)
    end = int(request.GET.get('end') or (start + 9))

    # Generate list of posts
    data = []
    for i in range(start, end+1):
        data.append(f'Post #{i}')

    # Artificially delay speed of response
    time.sleep(1) 

    # Return list of posts
    return JsonResponse({
        'posts': data
    })