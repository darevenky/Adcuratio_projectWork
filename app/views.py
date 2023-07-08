from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from rest_framework.viewsets import ViewSet
from app.serializers import *
from rest_framework.response import Response
# Create your views here.

def HomePage(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username' : username}
        return render(request, 'HomePage.html', d)
    return render(request, 'HomePage.html')

def Registration(request):
    ufo=UserForm()
    d={'ufo':ufo}

    if request.method=='POST':
        ufd=UserForm(request.POST)
        if ufd.is_valid():
            NSUO=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()

            return HttpResponse('<h5>Successfully Registered <h5>')
        else:
            return HttpResponse('not valid')
    
    return render(request, 'registration.html', d)

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('HomePage'))
        else:
            return HttpResponse('Invalid username or password') 
        
    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('HomePage'))


class CreateBirds(CreateView):
    template_name='birds.html'
    form_class=BirdsForm

    def form_valid(self,form):
        form.save()
        return HttpResponseRedirect(reverse('list'))
    
@login_required
def list(request):
    if request.session.get('username'):
            ADO=Birds.objects.all()
            SJD=BirdsSeriallizer(ADO,many=True)
            d={'data':SJD.data}
            return render(request,'list.html',d)


class BirdsData(ViewSet):

    def list(self,request):
        if request.session.get('username'):
            ADO=Birds.objects.all()
            SJD=BirdsSeriallizer(ADO,many=True)
            d={'data':SJD.data}
            return render(request,'list.html',d)

    def retrieve(self,request,pk):
        TO=Birds.objects.get(pk=pk)
        SDO=BirdsSeriallizer(TO)
        return Response(SDO.data)
        
    def create(self,request):
        so=BirdsSeriallizer(data=request.data)
        if so.is_valid():
            so.save()
            return Response({'success':'Birds is created'})
        else:
            return Response({'failed':'failed'})

    def update(self,request,pk):
        SPO=Birds.objects.get(pk=pk)
        SPD=BirdsSeriallizer(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Bird is updated'})
        else:
            return Response({'Failed':'Bird is Not Updated'})
    
    def partial_update(self,request,pk):
        SPO=Birds.objects.get(pk=pk)
        SPD=BirdsSeriallizer(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Bird is updated'})
        else:
            return Response({'Failed':'Bird is Not Updated'})
    def destroy(self,request,pk):
        Birds.objects.get(pk=pk).delete()
        return Response({'Deleted':'Bird is deleted'})
    


@login_required
def details(request):
    Bd=Birds.objects.all()
    d={'bd':Bd}
    return render(request, 'details.html', d)