from django.http import HttpResponse
import datetime
from django.template import Template, Context

def hello(request):
    return HttpResponse("Hello World") 

def homepage(request):
    return HttpResponse("This is home page")

def timenow(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    html = t.render(Context({"current_date": now}))
    return HttpResponse(html)
