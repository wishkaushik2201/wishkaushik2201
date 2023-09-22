import email
import re
from unicodedata import name
from django.forms import EmailField
from django.shortcuts import redirect, render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from .models import registraion,product,category


# Create your views here.
def home(request):
    return render(request,'home.html')
def mybook(request):
    return render(request,'mybook.html')
def wishlist(request):
    return render(request,'wishlist.html')
def subscription(request):
    return render(request,'subscription.html')
def login_in(request):
    error_msg=None
    if request.method=="POST":
        emailfield=request.POST.get("emailfield")
        passwordfield=request.POST.get("passwordfield")
        # print(email)
        # print(pssd)
        try:
            fetch_email=registraion.objects.get(email=emailfield)

            # fetch_email=login_user.objects.get(passw1=pssd)
            if (fetch_email.email==emailfield):
                
                flag = check_password(passwordfield, fetch_email.password1)
                if flag:
                    request.session['emailfield'] = fetch_email.email
                    request.session['customer_id']=fetch_email.id
                    return render(request,'home.html',{'fetch_email.email': fetch_email.email })
                else:
                    error_msg = "Please Enter valid password"
                    return render(request, 'home.html', {'error_msg': error_msg})
        except:
            error_msg = "Please Enter valid Email"
            return redirect(request,"login/")
    return HttpResponse(fetch_email.emailfield, fetch_email.password1)
def login(request):
    return render(request,"login.html")
def signup(request):
    if request.method=="Post":
        emailfield = request.POST.get('emailfield')
        passwordfield= request.POST.get('passwordfield')
        lname=request.POST.get('lname')
        fname=request.POST.get('fname')
        mobileno=request.POST.get('mobileno')
        dateofbirth=request.POST.get('dateofbirth')
        gender=request.POST.get('gender')
        # print(username,passw)
        try:
            fetch_email=registraion.objects.get(email=emailfield)
            if fetch_email:
                error_msg="Alerady exist"
                return render(request,"home.html",{"error_msg":error_msg})
        except:
            contact=registraion(email=emailfield, password1=make_password(passwordfield), lname=lname, fname=fname, mobileno=mobileno,dateofbirth=dateofbirth,gender=gender)
            contact.save()
            print("-------------------")
            # send_mail(
            #     "subject is here",
            #     'here is the message.',
            #     "sharma.vishal.2201@gmail.com",
            #     ["vs42653@gmail.com"]
            # )
            return HttpResponseRedirect("home/")
    # return render(request,'home')
    return render(request,'registration.html')
def reg(request):
    return render(request,"registration.html")
def logout(request):
    request.session.clear()
    print("----------logout Sucssess---------------------")
    return redirect('home')
