from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def insert_dept(request):
    dno = input('enter deptno : ')
    dna = input('enter the dept name : ')
    loc = input('enter the loc : ')
    DO = dept.objects.get_or_create(deptno = dno,dname = dna,loc=loc)
    if DO[1]:
        return HttpResponse('one record is inserted into dept ')
    else:
        return HttpResponse('this record is alredy exist')
def insert_emp(request):
    dn = input('deptno : ')
    eno = input('empno : ')
    en = input('ename : ')
    j = input('job : ')
    hd = input('hiredate : ')
    sal = input('sal : ')
    comm = input('comm : ')
    mg = input('mgr or (leav block for NULL) : ')
    QTO = dept.objects.filter(deptno = dn)
    if QTO:
        TO = QTO[0]
        EM = emp.objects.get_or_create(deptno =TO,mgr = mg,comm = comm,sal = sal,hiredate = hd,job = j,ename = en ,empno = eno)
        d = {'emps':emp.objects.all()}

        return render(request,'display_emp.html',d)
    else:
        return HttpResponse('this record is alredy exist')
def display_dept(request):
    depts=dept.objects.all()
    d={'depts':depts}
    return render(request,'display_dept.html',d)
def display_emp(request):
    emps=emp.objects.order_by('hiredate')
    d={'emps':emps}
    return render(request,'display_emp.html',d)




