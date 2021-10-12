from django.shortcuts import render

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
