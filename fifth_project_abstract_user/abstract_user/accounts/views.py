from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User
from django.core.mail import send_mail
from django.http import HttpResponse
import random

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator




def send_test_mail(request):
    # send_mail(
    #     subject="Rehamn : This is the testing otp verification",
    #     message="SMTP connection is working", 
    #     from_email="tirupathiraosesapu@gmail.com",
    #     recipient_list=["tirupathistr@gmail.com", "tirupathiraosesapu@gmail.com", "tarunpediredla9966@gmail.com"],
    #     # ["tirupathistr@gmail.com"],
    #     fail_silently=False
    #     )
    otp = random.randint(100000,999999)
    print(otp)
    return HttpResponse("Email sent succcesffully")
        


# Create your views here.
def register_view(request):
    
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        mobile_number = request.POST.get("number")
        password = request.POST.get("password")
        
        if not email or not username or not mobile_number or not password:
            return render(request, "register.html", {"error":"All fields are required"})
        
        if User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists():
            return render(request, "register.html", {"error":"Username and email is already existed"})
        
        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {"error":"Email already existed"})
        
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error":"Username is already existed"})
        
        if User.objects.filter(mobile_number=mobile_number).exists():
                    return render(request, "register.html", {"error":"Mobile number is already existed"})
                
        otp_value = random.randint(100000, 999999)
        print(otp_value)
        print(username, password, email)
        user = User.objects.create_user(username=username, mobile_number=mobile_number, email=email, password=password, role="user")
        user.otp = otp_value
        user.is_active = False
        user.save()
        
        send_mail(
            subject="Employee Management Registration : OTP Verification",
            message=f"Your OTP is {otp_value}", 
            from_email="tirupathiraosesapu@gmail.com",
            recipient_list=[email],
            fail_silently=False
            )
        
        return redirect(f"/verify-otp/{user.id}", {"user":user})
        
    return render(request, "register.html")

def verify_otp_view(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        entered_otp = request.POST.get("manula-otp")
        
        if user.otp == entered_otp:
            user.is_verified = True
            user.is_active = True
            user.otp = None
            user.save()
            
            return redirect("/login/")
    return render(request, "verify.html", {"user":user})
        
def resent_otp_view(request, id):
    user = User.objects.get(id=id)
    
    otp_value = str(random.randint(100000, 999999))
    user.otp = otp_value
    user.save()
    
    send_mail(
            subject="Employee Management Registration : OTP Verification",
            message=f"Your OTP is {otp_value}", 
            from_email="tirupathiraosesapu@gmail.com",
            recipient_list=[user.email],
            fail_silently=False
    )
    return redirect(f"/verify-otp/{user.id}/", {"id":{user.id}})
   
def forgot_password_view(request):
    if request.method == "POST":
        email_value = request.POST.get("email")
        
        try:
            user = User.objects.get(email=email_value)
        except User.DoesNotExist:
            return render(request, "forgot_password.html", {"error":"User not found"})
        
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        print(uid)
        print(token)
        
        reset_link = f"http://127.0.0.1:8000/reset-password/{uid}/{token}/"
        
        send_mail("Reset Password", f"Reset Password link : \n {reset_link}", "tirupathiraosesapu@gmail.com", [email_value])
        return render(request, "forgot_password.html", {"success":"Email sent succefuuly, Please check you rmail"})

    return render(request, "forgot_password.html")
 

def reset_password_view(request, uid, token):
    uid_value = urlsafe_base64_decode(uid).decode()
    user = User.objects.get(pk=uid_value)
    
    if not default_token_generator.check_token(user, token):
        return render(request, "reset_password.html", {"error":"Invalid token"})
    
    if request.method == "POST":
        new_password = request.POST.get("new_pass")
        confirm_password = request.POST.get("confirm_pass")
        
        if new_password != confirm_password:
            return render(request, "reset_password.html", {"error":"New password is not matched"})
        
        user.set_password(new_password)
        user.save()
        return redirect("/login/")
            
            
    
    
    return render(request, "reset_password.html")

def login_view(request):
    
    if request.method == "POST":
        input_email = request.POST.get("email_value")
        input_password = request.POST.get("password_value")
        print(input_password, input_email)
        if not input_email or not input_password:
            return render(request, "login.html", {"error":"All fields are required"})
        
        user = authenticate(request, username=input_email, password= input_password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html",{"error":"Invalid Credentials"} )            
        
    return render(request, "login.html")

@login_required
def dashboard_view(request):
    return render(request, "index.html")

@login_required
def change_password_view(request):
    if request.method == "POST":
        old_password = request.POST.get("old_pass")
        new_password = request.POST.get("new_pass")
        confirm_password = request.POST.get("confirm_pass")
        
        print(old_password, new_password, confirm_password)
        
        user = request.user
        
        if not user.check_password(old_password):
            return render(request, "change_password.html", {"error":"Old password is not matched"})
        
        if new_password != confirm_password:
            return render(request, "change_password.html", {"error":"New password is not matched"})
        
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)
        return redirect("/")
    
    return render(request, "change_password.html")




def logout_view(request):
    logout(request)
    return redirect("/login/")