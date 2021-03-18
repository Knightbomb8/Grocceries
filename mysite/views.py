from django.shortcuts import render

from django.http import HttpResponse

from core import localdata

# Create your views here.


def homepage(request):
    return render(request, 'registration/login.html')


def accountInfoPage(request):
    return render(request, 'profile/accountinfo.html')


def loginRedirect(request):

    # store the logged in account to localdata
    localdata.LocalData.account = request.user.account
    print(localdata.LocalData.account.user.username)

    # redirect to appropriate page
    return render(request, 'test.html')


def registerPage(request):
    return render(request, 'account/registered.html')


def storeFinderPage(request):
    return render(request, 'map/storelocator.html')


def simple_function(request):
    print("\nthis is a simple function\n")
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
