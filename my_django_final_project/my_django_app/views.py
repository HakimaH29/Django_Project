from django.shortcuts import render, redirect
from django.http import HttpResponse
from my_django_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages

# These are our views The first one below is for our homepage, and I listed the motivational quotes.

def home(request):
    my_html_data = {"home_heading": "This is the Home Page of The Network!",
                    "home_para": "Welcome to the world of networking",
                    "my_dictionary": {
                                    "item_one":"The richest people in the world look for and build networks, everyone else looks for work.", 
                                    "item_two": "Your network is your net worth.",
                                    "item_three":"Opportunities don't happen. You create them." }}
    return render(request, 'home.html', my_html_data)
#This is the contact us form, where we can get the user's contact information when they are submitting the form to us.
def contact(request):
    if request.method == "POST":
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        country = request.POST.get("country")
        subject = request.POST.get("subject") 
        messages.success(request, "Thank you for contacting us. We value your feedback!")

    return render(request, 'contact.html')

def about_us(request):
    return render(request, 'about.html')

#This is where we are giving the commands to what the user will see during the registration process, in case the email  exists already or passswords don't match. 

def register(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        user_email = request.POST.get("useremail")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Password does not match! Please try again.")
            return render(request, 'register.html')
        
        if User.objects.filter(username = user_name).exists():
            messages.error(request, "The username already exists!")
            return render(request, 'register.html')
        
        if User.objects.filter(email = user_email).exists():
            messages.error(request, "The email already exists! Please go to the login page.")
            return render(request, 'register.html')
        
        user = User.objects.create_user(username = user_name, email = user_email, password = password1)
        user.save()

        login(request, user)

        messages.success(request, "You were registered successfully")
        return render(request, 'register.html')

    else:
        return render(request, 'register.html')
    
def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        user_password = request.POST.get("password")
        user = authenticate(request, username = user_name, password = user_password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('my_home')
        else:
            print("testing none")
            messages.error(request, "Either email or password is incorrect")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def user_profile(request):
    if request.method == "GET":
        User_Id = request.user.id
        print(User_Id, "my_user_id")
        user_profile_data = users_profile.objects.filter(user_id = User_Id).values()
        if user_profile_data:
            information = list(user_profile_data)[0]

            image_url = os.path.join(settings.MEDIA_URL, "profile_images", information["user_image"])

            user_profile_info = {
            "name": information["user_name"],
            "age":information["user_age"],
            "email":information["user_email"],
            "city":information["user_city"],
            "profile_image": image_url
            }
            return render(request, 'profile.html', user_profile_info)
        else:
            return render(request, 'profile_questions.html')
    if request.method == "POST":
        U_Id = request.user.id
        u_name = request.POST.get("u_name")
        u_city = request.POST.get("u_city")
        u_age = request.POST.get("u_age")
        u_email = request.POST.get("u_email")
        u_file = request.FILES["u_image"]

        file_name = u_file.name
        modified_file_name = file_name.replace(".", str(datetime.now()) + ".")

        user_profile_image_path = os.path.join(settings.MEDIA_ROOT, "profile_images", modified_file_name)

        with open(user_profile_image_path, "wb+") as destination:
            for chunk in u_file.chunks():
                destination.write(chunk)

        print(modified_file_name)

        profile_information = users_profile(user_id = U_Id,
                                            user_name = u_name,
                                            user_age = u_age,
                                            user_city = u_city,
                                            user_email = u_email,
                                            user_image = modified_file_name)
        
        profile_information.save()

        image_url = os.path.join(settings.MEDIA_URL, "profile_images", modified_file_name)

        user_profile_info = {
            "name": u_name,
            "age":u_age,
            "email":u_email,
            "city":u_city,
            "profile_image": image_url
        }

        return render(request, 'profile.html', user_profile_info) 