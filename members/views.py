from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    mymember1 = Member.objects.get(id=1)
    template = loader.get_template('all_members.html')
    context = {
        'mymembers' : mymembers,
        'mymember1' :mymember1,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymembero = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember' : mymembero, 
    }
    return HttpResponse(template.render(context, request))

def main(request): 
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mymembers, 
    }
    return HttpResponse(template.render(context, request))