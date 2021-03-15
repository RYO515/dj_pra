from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    returnobject = HttpResponse('<h1>hello world</h1>')
    return returnobject

class HelloworldView(TemplateView):
    template_name = 'hello.html'