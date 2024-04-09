from django.http import HttpResponse

def index(request):
    return HttpResponse("Just trying out Django...")
