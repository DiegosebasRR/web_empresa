from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        content= request.POST.get('content', '')
        email = EmailMessage(
            "La Cafferiera: Nuevo mensaje de  contacto",
            "De {} <{}>\n\nEscribio\n\n{}".format(name,email,content),
            "no-contestar@inbox.mailtrap.io",
            ["diego123xdxp@gmail.com"],
            reply_to=[email]
        )
        try:
            email.send()
            return redirect(reverse('contact')+'?ok')
        except:
            return redirect(reverse('contact')+'?fail')
    return render(request, 'contact/contact.html',{'form':contact_form} )        