from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'oasis/index.html')

def about(request):
    return render(request, 'oasis/about.html')

def services(request):
    return render(request, 'oasis/services.html')

def production(request):
    return render(request, 'oasis/production.html')

def contact(request):
    if request.method == "POST":
        contact_fname = request.POST['fname']
        contact_lname = request.POST['lname']
        contact_email = request.POST['email']
        contact_message = request.POST['message']

        send_mail(
            contact_fname, 
            contact_message,
            contact_email,
            ['info@oasispetroleumllc.com'],
            fail_silently = False,
        )


        return render(request, 'oasis/contact.html', {'contact_fname' : contact_fname})


    else:
        return render(request, 'oasis/contact.html')
