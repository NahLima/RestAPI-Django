from django.http import HttpResponse

# Create your views here.
def grades(request):
    if request.method == 'GET':
        return HttpResponse("My Grades!!!")