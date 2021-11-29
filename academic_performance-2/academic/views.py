from django.db.models import Count
from django.shortcuts import render,redirect
from . models import Adminlogin,AddFaculty_Model,AddStudent_Model,Internal_Model
from . forms import AddFaculty_ModelCreate,AddStudent_ModelCreate,Internal_ModelCreate
import sys
from .markspredict import passPrediction , cnsmarksPredict, umlmarksPredict,mcmarksPredict,hbdmarksPredict,stmmarksPredict

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def login(request):

    if request.method == "POST":
        
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            
            print("Hello world",username,password)
            #print("retive from database",Adminlogin.objects.get(username))
            enter=Adminlogin.objects.get(username=username,password=password)

            print(enter.id)
            request.session["name"]=enter.id 


            return redirect('AdminHome')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass


    return render(request,'login.html')

def flogin(request):
    if request.method == "POST":

        
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            print("Hello world",email,password)
            #print("retive from database",Adminlogin.objects.get(username))
            enter=AddFaculty_Model.objects.get(email=email,password=password)

            print(enter.id)
            request.session["name"]=enter.id 

            


            return redirect('FacultyHome')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass

    return render(request,'flogin.html')

def slogin(request):

    if request.method == "POST":
        
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            print("Hello world",email,password)
            #print("retive from database",Adminlogin.objects.get(username))
            enter=AddStudent_Model.objects.get(email=email,password=password)

            print(enter.id)
            request.session["id"]=enter.id 
            request.session["email"]=email
            request.session["name"]=enter.fullname


            return redirect('StudentHome')
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Unexpected error:", sys.exc_info()[1])
            print("Unexpected error:", sys.exc_info()[2])
            pass

    return render(request,'slogin.html')


def contact(request):
    return render(request,'contact.html')

def AdminHome(request):
    return render(request,'AdminHome.html')

def StudentHome(request):

    name=request.session["name"]
   
    return render(request,'StudentHome.html',{"name":name})

def Vsmarks(request):
    
    id=request.session["id"]
    try:
        enter=Internal_Model.objects.get(rollno_id=id)

        df=[]
        df.append(enter.cns)
        df.append(enter.uml)
        df.append(enter.mc)
        df.append(enter.stm)
        df.append(enter.hbd)
        df.append(enter.attendance)

    except:
        pass

    return render(request,'Vsmarks.html',{'df':df})




def FacultyHome(request):

    return render(request,'FacultyHome.html')


def AddFaculty(request):

    upload=AddFaculty_ModelCreate()

    if request.method=='POST':
        
        upload=AddFaculty_ModelCreate(request.POST,request.FILES)

        if upload.is_valid():

            upload.save()

            return redirect('AddFaculty')
        
    else:
        
        return render(request,'AddFaculty.html',{'upload_form':upload})


    
def update_faculty(request,f_id):

    f_id=int(f_id)

    print("The fid is ",f_id)

    try:
        f_sel=AddFaculty_Model.objects.get(id=f_id)
    
    except AddFaculty_Model.DoesNotExist:
        return redirect('index')

    f_form=AddFaculty_ModelCreate(request.POST or None, instance=f_sel)

    if f_form.is_valid():

        f_form.save()

        return redirect('AddFaculty')
    
    return render(request,'AddFaculty.html',{'upload_form':f_form})


def delete_faculty(request,f_id):

    f_id=int(f_id)
    try:

        f_sel=AddFaculty_Model.objects.get(id=f_id)

    except AddFaculty_Model.DoesNotExist:
        pass

    f_sel.delete()
    return redirect('ViewFaculty')


    

def ViewFaculty(request):

     obj=AddFaculty_Model.objects.all()

     return render(request,'ViewFaculty.html',{'obj':obj})

def AddStudent(request):

    upload_std=AddStudent_ModelCreate()
    if request.method=='POST':
        
        upload_std=AddStudent_ModelCreate(request.POST,request.FILES)

        if upload_std.is_valid():
            upload_std.save()
            return redirect('AddStudent')
        
    else:
        
        return render(request,'AddStudent.html',{'upload_form1':upload_std})


def update_student(request,s_id):

    s_id=int(s_id)

    print("The sid is ",s_id)

    try:
        s_sel=AddStudent_Model.objects.get(id=s_id)
    
    except AddStudent_Model.DoesNotExist:
        return redirect('index')

    s_form=AddStudent_ModelCreate(request.POST or None, instance=s_sel)

    if s_form.is_valid():

        s_form.save()

        return redirect('AddStudent')
    
    return render(request,'AddStudent.html',{'upload_form1':s_form})


def delete_student(request,s_id):

    s_id=int(s_id)
    try:

        s_sel=Student_Model.objects.get(id=s_id)

    except AddStudent_Model.DoesNotExist:
        pass

    s_sel.delete()
    return redirect('ViewStudent')

def deleteInternalMarks(request,i_id):

    i_id=int(i_id)

    try:
        

        i_IM=Internal_Model.objects.get(id=i_id)

    except Internal_Model.DoesNotExist:
        pass

    i_IM.delete()
    return redirect('ViewInternalMarks')




def ViewStudent(request):

    obj=AddStudent_Model.objects.all()

    return render(request,'ViewStudent.html',{'obj':obj})


def AddInternalMarks(request):

    upload=Internal_ModelCreate()

    if request.method=='POST':
        
        upload=Internal_ModelCreate(request.POST,request.FILES)

        if upload.is_valid():
            upload.save()
            return redirect('AddInternalMarks')
        
    else:
        
        return render(request,'AddInternalMarks.html',{'upload_form':upload})

def ViewInternalMarks(request):

    obj=Internal_Model.objects.all()

    return render(request,'ViewInternalMarks.html',{'obj':obj})

def update_internal(request,i_id):

    i_id=int(i_id)

    print("The iid is ",i_id)

    try:
        i_sel=Internal_Model.objects.get(id=i_id)
    
    except Internal_Model.DoesNotExist:
        return redirect('index')

    i_form=Internal_ModelCreate(request.POST or None, instance=i_sel)

    if i_form.is_valid():

        i_form.save()

        return redirect('AddInternalMarks')
    
    return render(request,'AddInternalMarks.html',{'upload_form':i_form})

def PredictStatus(request):

    return render(request,'PredictStatus.html')

def ViewPassPredict(request):

    obj=Internal_Model.objects.all()
    test=[]

    for v in obj:
        d=[]
        d.append(v.cns)
        d.append(v.uml)
        d.append(v.mc)
        d.append(v.stm)
        d.append(v.hbd)
        d.append(v.attendance)
        test.append(d)
    
    print(test)

    classifier=passPrediction()

    predicted= classifier.predict(test).tolist()

    print("The prediction value is ",predicted[0])

    x = [1, 2, 3]
    y = [4, 5, 6]
    result=[]
    for i, j in zip(obj,predicted):
       disk=str(i.rollno_id)+" "+str(j)
       result.append(disk)
    


    return render(request,'ViewPassPredict.html',{'result':result})

def ViewMarksCNS(request):

    obj=Internal_Model.objects.all()

    test=[]

    for v in obj:
        d=[]
        d.append(v.cns)
        d.append(v.attendance)
        test.append(d)
    
    print(test)

    model=cnsmarksPredict()

    predicted= model.predict(test).tolist()

    print("The prediction value is ",predicted[0])

    result=[]
    for i, j in zip(obj,predicted):
       j=int(j)
       disk=str(i.rollno)+" "+str(j)
       result.append(disk)
    
    return render(request,'ViewMarksCNS.html',{'result':result})

def ViewMarksUML(request):

    obj=Internal_Model.objects.all()

    test=[]

    for v in obj:
        d=[]
        d.append(v.uml)
        d.append(v.attendance)
        test.append(d)
    
    print(test)

    model=umlmarksPredict()

    predicted= model.predict(test).tolist()

    print("The prediction value is ",predicted[0])

    result=[]
    for i, j in zip(obj,predicted):
       j=int(j)
       disk=str(i.rollno)+" "+str(j)
       result.append(disk)
    
    return render(request,'ViewMarksUML.html',{'result':result})
    

def ViewMarksMC(request):

    obj=Internal_Model.objects.all()

    test=[]

    for v in obj:
        d=[]
        d.append(v.mc)
        d.append(v.attendance)
        test.append(d)
    
    print(test)
          
    model=mcmarksPredict()

    predicted= model.predict(test).tolist()

    print("The prediction value is ",predicted[0])

    result=[]
    for i, j in zip(obj,predicted):
       j=int(j)
       disk=str(i.rollno)+" "+str(j)
       result.append(disk)
    
    return render(request,'ViewMarksMC.html',{'result':result})


def ViewMarksSTM(request):

    obj=Internal_Model.objects.all()

    test=[]

    for v in obj:
        d=[]
        d.append(v.stm)
        d.append(v.attendance)
        test.append(d)
    
    print(test)

    model=stmmarksPredict()

    predicted= model.predict(test).tolist()

    print("The prediction value is ",predicted[0])

    result=[]
    for i, j in zip(obj,predicted):
       j=int(j)
       disk=str(i.rollno)+" "+str(j)
       result.append(disk)
    
    return render(request,'ViewMarksSTM.html',{'result':result})

def ViewMarksHBD(request):

    obj=Internal_Model.objects.all()

    test=[]

    for v in obj:
        d=[]
        d.append(v.hbd)
        d.append(v.attendance)
        test.append(d)
    
    print(test)

    model=hbdmarksPredict()

    predicted= model.predict(test).tolist()

    print("The prediction value is ",predicted[0])

    result=[]
    for i, j in zip(obj,predicted):
       j=int(j)
       disk=str(i.rollno)+" "+str(j)
       result.append(disk)
    
    return render(request,'ViewMarksHBD.html',{'result':result})


def ViewMarksPredict(request):
    return render(request,'ViewMarksPredict.html')