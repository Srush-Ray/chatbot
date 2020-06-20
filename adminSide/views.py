from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from .models import qa
from django.contrib.auth.models import auth
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            print(user)
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
def home(request):
    all_qna=qa.objects.all()    
    return render(request, 'home.html',{'qas':all_qna})

def add(request):
    if(request.method=='POST'):
        question=request.POST['question']
        answer=request.POST['answer']
        if len(question)==0 or len(answer)==0:
                messages.info(request,'Empty values not allowed')
                return redirect('/add')
        else:
            save_qa=qa(question=question,answer=answer)
            try:
                save_qa.save()
                print('saved')
                return redirect('/home')
            except expression as identifier:
                messages.info(request,'try again could not save')
                return redirect('/add')
    else:
        return render(request,'add.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/login')


def delete(request,id=None):
    if id is not None:
        deleteqa=qa.objects.filter(id=id)
        deleteqa.delete()
    else:
        messages.info(request,'id not received')
        return redirect('/home')


def load(request,id=None):
    if id is not None:
        updateqa=qa.objects.get(id=id)
        return render(request,'update.html',{'updateqa':updateqa})
    else:
        messages.info(request,'id not received')
        return redirect('/home')
    
    

def update(request,uid):
    print ( 'in update')
    if(request.method=='POST'):
        question=request.POST['question']
        answer=request.POST['answer']
        # id=request.POST['id']
        if len(question)==0 or len(answer)==0 or len(id)==0:
            messages.info(request,'Empty values not allowed')
            return redirect('/load/<id>/')
        else:
            updateqa=qa.objects.get(id=uid)
            updateqa.question=question
            updateqa.answer=answer
            # updateqa=qa(question=question,answer=answer)
            try:
                updateqa.save()
                print('update')
                return redirect('/home')
            except expression as identifier:
                messages.info(request,'try again could not save')
                return redirect('/load/<id>')
    else:
        return redirect('/home')
