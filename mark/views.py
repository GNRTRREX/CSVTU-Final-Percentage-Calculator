from django import http
from django.db import models
from django.http import HttpResponse, request 
from django.shortcuts import render
from mark.models import Ex

def home(request):
    return render(request,'home.html')

def fill(request):
    return render(request,'index.html')

def mark(request):

    F_name = request.GET.get('fname')
    L_name = request.GET.get('lname')
    Name = F_name+" "+L_name
    total = 0
    c1 = []
    c2 = 0
    for i in range(1,9):
        a = int(request.GET.get(f'sem{i}'))
        print(a)
        total += a
        if i < 3:
            c2 = (a/800)*100
        else:
            c2 = (a/1000)*100
        c1.append(c2)
    total1 = 0
    j = 0
    print(c1)
    for i in c1:
        j += i
        total1 = j/8
    percent = (total/7600)*100
    if percent >= 75:
        div = 'Fisrt Division(Honors)'
    elif percent >= 60:
        div = 'Fisrt Division'
    else:
        div = 'Second Division'
    perrr = str(percent)[slice(5)]
    tottt = str(total1)[slice(5)]
    print(perrr)
    Ex_user = Ex(user_name = Name, user_total = total,user_percent = f"{perrr}%({tottt}%)",user_division = div)
    Ex_user.save()
    prms = {'name':f"{Name}", 'total': total, 'per':f'Your aggregate persentage is {perrr}%({tottt}%)', 'div':div}
    return render(request,'mark.html',prms)

def users(request):
    user1 = Ex.objects.all()
    prs = {'user':user1}
    return render(request,'users.html',prs)
def about(request):
    return render(request,'about.html')