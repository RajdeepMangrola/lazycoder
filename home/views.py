from django.shortcuts import render,HttpResponse
from home.models import Contact
# Create your views here.
def index(request):
    context = {"variable":"This is sent."}
    return render(request,"index.html",context)
    # return HttpResponse("this is home.")
def about(request):
    return render(request,"about.html")
    # return HttpResponse("this is about.")
def service(request):
    return render(request,"service.html")
def contact(request):
    if request.method =="POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        contact = Contact(firstname=firstname,lastname=lastname,email=email,city=city,state=state,zipcode=zipcode)
        contact.save()
    return render(request,"contact.html")