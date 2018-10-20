from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.contrib.staticfiles.templatetags.staticfiles import static

url = static('reciept.jpg')
# Create your views here.

def get_button_list(box=(860, 420, 1130, 640), n_buttons = 6, bgr=0.8, height=60, link_list=["page.html"]):
    coord_list = [[219, 912, 322, 1056]]
    return zip(link_list, coord_list)

def index(request):
    # latest_user = User.object.order_by('-pub_date')[:5]

    context = {
        "name" : "Jon",
        "button_list" : get_button_list(box=(860, 420, 1130, 640), n_buttons = 6, bgr=0.8, height=60),
        # "user list" : latest_user
    }
    return render(request, 'maxkiosk/index.html', context=context)

def page_1(request):
    context = {
        "text" : "Menu",
        "links" : {
            "Button1" : {"text" : "Health and services",
                "link" : "page_4a"},
            "Button2" : {"text" : "Health and services",
                "link" : "page_4a"}
        }
    }
    return render(request, 'maxkiosk/index.html', context=context)

def page_2(request):
    return render(request, 'maxkiosk/index.html')

def page_3(request):
    return render(request, 'maxkiosk/index.html')

def page_4a(request):
    context = {
        "text" : "Options...",
        "links" : {
            "Button1" : {"text" : "Print",
                "link" : "#"},
            "Button2" : {"text" : "",
                "link" : "#"},
            "Button3" : {"text" : "",
                "link" : "#"},
            "Button4" : {"text" : "",
                "link" : "#"},
            "Button5" : {"text" : "",
                "link" : "#"},
            "Button6" : {"text" : "Back",
                "link" : "page_3"}
        }
    }
    return render(request, 'maxkiosk/page_4a.html')

def page_4b(request):
    context = {
        "text" : "Options...",
        "links" : {
            "Button1" : {"text" : "Print",
                "link" : "#"},
            "Button2" : {"text" : "",
                "link" : "#"},
            "Button3" : {"text" : "",
                "link" : "#"},
            "Button4" : {"text" : "",
                "link" : "#"},
            "Button5" : {"text" : "",
                "link" : "#"},
            "Button6" : {"text" : "Back",
                "link" : "page_3"}
        }
    }
    return render(request, 'maxkiosk/page_4b.html')

def page_4c(request):
    context_4c = {
        "text": " ",
        "links": {
            "Button1": {"text": "Print",
                        "link": "page_4a"},
            "Button2": {"text": "Back",
                        "link": "page_4a"}
        }
    }
    return render(request, 'maxkiosk/index.html', context = context_4c)

def page_4d(request):
    return render(request, 'maxkiosk/index.html')

def page_4e(request):
    return render(request, 'maxkiosk/page_4e.html')

def page_5(request):
    return render(request, 'maxkiosk/page_5.html')

