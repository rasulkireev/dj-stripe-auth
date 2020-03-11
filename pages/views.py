from django.http import HttpResponse
from django.template import loader
from django.conf import settings

def index(request):
    template = loader.get_template('home.html')
    context = {
        'stripe_public': settings.STRIPE_TEST_PUBLIC_KEY,
    }
    return HttpResponse(template.render(context, request))
