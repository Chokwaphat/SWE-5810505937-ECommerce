from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.shortcuts import render


# Create your views here.
@login_required
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']
        print token
    template = 'checkout.html'
    return render(request, template, context)
