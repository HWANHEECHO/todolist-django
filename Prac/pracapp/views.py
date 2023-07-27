from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.



def index(request):
    pracs = pracclass.objects.all()
    print('From DB:', pracs)
    content = {'pracs' : pracs}
    return render(request, 'pracapp/index.html', content)

def createPrac(request):
    user_input_str = request.POST['todoContent']
    print('todoContent: ' + user_input_str)

    # return HttpResponse("Practice" + user_input_str)
    
    new_prac = pracclass(content = user_input_str)
    new_prac.save()

    return HttpResponseRedirect(reverse('index'))

def deletePrac(request):
    delete_prac_id = request.GET['todoNum']
    print("삭제할 prac의 ID", delete_prac_id)

    prac = pracclass.objects.get(id = delete_prac_id)
    prac.delete()

    return HttpResponseRedirect(reverse('index'))