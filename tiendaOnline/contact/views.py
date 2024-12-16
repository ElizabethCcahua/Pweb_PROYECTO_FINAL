from django.shortcuts import render, redirect
from .forms import ContactForm

from django.core.mail import send_mail

def contact(request):
    contactForm = ContactForm()

    if request.method=="POST":
        contactForm = ContactForm(data=request.POST)
        if contactForm.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            try:
                send_mail(
                    'Mensaje desde App Django',
                    "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(name,email,message),
                    email,
                    ["hheaxshop@gmail.com"],
                    fail_silently=False
                )
                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?notvalid")
            
    return render(request, 'contact/contact.html', {'contactForm' : contactForm})