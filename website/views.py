from django.shortcuts import render
from website.forms import ContactForm
from django.contrib import messages


def index_view(request):
    return render(request, "website/index.html")

def about_view(request):
    return render(request, "website/about.html")

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = "Anonymous"
            contact.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket is submitted successfully.')
        else:
            messages.add_message(request, messages.ERROR, 'Your ticket is not submitted.')
    form = ContactForm()
    return render(request, "website/contact.html", {"form": form})
