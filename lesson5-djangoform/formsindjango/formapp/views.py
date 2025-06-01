from django.shortcuts import render,redirect
from .form import ContactForm


#home page view function
def home_view(request):
    return render(request, 'formapp/home.html')

#contact view function to handle contact form
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()  
            return redirect('contact-success')
        
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'formapp/contact.html',context )



#success view function to show success message

def contact_success_view(request):
    return render(request, 'formapp/success.html')
  
