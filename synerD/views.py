from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
import pandas as pd
from django.contrib.auth import authenticate, login

from .models import *

def getusername(id):
    user = UserInfo.objects.filter(id=id)[0]
    user_fullname = user.firstname + " " + user.lastname
    return user_fullname
def getorgname(id):
    org = Organization.objects.filter(id=id)[0]
    return org.organizationname
def index(request):
    if(request.GET.get('logout')=='true'):
        request.session['staff'] = None

    template = loader.get_template('synerd/index.html')
    subscribers = pd.DataFrame(list(Subscriber.objects.all().values()))
    organizations = pd.DataFrame(list(Organization.objects.all().values()))
    context = {}
    if subscribers.__len__() > 0:
        subscribers['user_id'] = subscribers['user_id'].apply(getusername)
        subscribers = subscribers.rename(columns={'user_id': 'User',
                                              'subscriptiontypecode_id': 'Subscription Type',
                                              'servicecode_id':'Service Type',
                                              'startdate':'Start Date'
                                              })
        context['subdf'] = subscribers.to_html(table_id='sub_table', classes='table table-striped', index=False)

    if organizations.__len__() > 0:
        organizations = organizations.rename(columns={'organizationname':'Organization Name',
                                                      'description':'Description',
                                                      'datejoined':'Date Joined',
                                                  'address1':'Address',
                                                  'address2':'Address',
                                                  'city':'City',
                                                  'state':'State',
                                                  'zipcode':'Zip Code',
                                                  'phonenumber':'Phone Number'})
        context['memdf'] = organizations.to_html(table_id='org_table',classes='table table-striped',index=False)
    return render(request, 'synerd/index.html', context)

def signup(request):
    template = loader.get_template('synerd/signup.html')

    if request.method=="POST":
        user = UserInfo()
        user.username = request.POST.get('username')
        user.staff = request.POST.get('staff') == 'on'
        try:
            user.save()
        except IntegrityError:
            redirect("/signup?error=username")

        redirect("/login")
    return HttpResponse(template.render( request=request))


def log_in(request):
    template = loader.get_template('synerd/login.html')
    context = {}
    if request.method=="POST":
        username = request.POST.get('username')
        if UserInfo.objects.filter(username=username).__len__() is not 0:
            user = UserInfo.objects.filter(username=username)[0]
            if user is not None:
                print("user found")
                print(user.staff)
                if user.staff is True:
                    print("user staff")
                    request.session['staff'] = True
                # Redirect to a success page.
                    return redirect("/console")
                else:
                    print("user not staff")
                    request.session['staff'] = False
                    return redirect("/")
        context = {'error':'Username not found'}
    return HttpResponse(template.render( request=request, context=context))


def console(request):
    print(request.session['staff'] )
    if request.session['staff'] is False or request.session['staff'] is None:
        return redirect("/")
    template = loader.get_template('synerd/admin.html')

    return HttpResponse(template.render( request=request))

def office(request):
    template = loader.get_template('synerd/console/office.html')
    office = pd.DataFrame(list(Office.objects.all().values()))
    context = {}
    if request.method=="POST":
        newOffice =  Office()
        print(request.POST)
        if(request.POST.get('office_name') is not None):
            newOffice.officename = request.POST.get('office_name')
            newOffice.attribution = request.POST.get('attribution')
            if(request.POST.get('office_code')is not None):
                newOffice.id = request.POST.get('office_code')
            newOffice.save()
            office = pd.DataFrame(list(Office.objects.all().values()))

    context['officedf'] = office.to_html(table_id='office_table',classes='table table-striped',index=False)
    return HttpResponse(template.render( request=request, context=context))


def officer(request):
    template = loader.get_template('synerd/console/officer.html')

    if request.method=="POST":
        officer = Officer()
        if(request.POST.get('officer_subscriber_id')is not None):
            officer.subscriberid = request.POST.get('officer_subscriber_id')
        officer.officecode=request.POST.get('offcer_office_code')
        officer.startdate = request.POST.get('officer_start_date')
        officer.enddate = request.POST.get('offcer_end_date')
        officer.save()
    return HttpResponse(template.render( request=request))



def organization(request):
    template = loader.get_template('synerd/console/org.html')

    if request.method=="POST":
        org = Organization()
        org.id = request.POST.get("org_code")
        org.organizationname = request.POST.get("org_name")
        org.description= request.POST.get("org_description")
        org.datejoined = request.POST.get("date_joined")
        org.address1= request.POST.get("address1")
        org.address2= request.POST.get("address2")
        org.city = request.POST.get("city")
        org.state= request.POST.get("state")
        org.phonenumber= request.POST.get("org_phoneno")
        org.save()
    return HttpResponse(template.render( request=request))

def orgmember(request):
    template = loader.get_template('synerd/console/orgmember.html')

    if request.method=="POST":
        orgmember =  OrganizationMember()
        print(request.POST)
        if Organization.objects.filter(id=request.POST.get("org_code_mem")).__len__() is not 0 and Subscriber.objects.filter(id= request.POST.get("org_mem_subscriber_id")).__len__() is not 0:
            orgmember.organizationcode = Organization.objects.filter(id=request.POST.get("org_code_mem"))[0]
            orgmember.subscriberid = Subscriber.objects.filter(id= request.POST.get("org_mem_subscriber_id"))[0]
            orgmember.startdate = request.POST.get("mem_start_date")
            orgmember.enddate = request.POST.get("mem_end_date")
            orgmember.nativecountry= request.POST.get("native_country")
            orgmember.citizenship = request.POST.get("Citizenship")
            orgmember.isdelegate = (request.POST.get("delegate") == 'on')
            orgmember.save()
            redirect('/console')




    return HttpResponse(template.render( request=request))


def subscriber(request):
    template = loader.get_template('synerd/console/subscriber.html')

    if request.method=="POST":
        sub = Subscriber()
        sub.id = request.POST.get("subscriber_id")
        service = Service.objects.filter(id=request.POST.get('service_code'))
        sub.servicecode = service[0]
        subscriptiontype = SubscriptionType.objects.filter(id=request.POST.get('sub_type'))
        sub.subscriptiontypecode =  subscriptiontype[0]
        user = UserInfo.objects.filter(username=request.POST.get("username"))
        sub.user = user[0]
        sub.startdate=request.POST.get("sub_start_date")
        sub.save()
        redirect('/console')
    return HttpResponse(template.render( request=request))




from rest_framework import viewsets

from .backend.serializers import *

class SubscriberView(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberAPI

class OrganizationView(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationAPI


class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceAPI


class UserInfoView(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoAPI

class TransferredSubscriptionView(viewsets.ModelViewSet):
    queryset = TransferredSubscription.objects.all()
    serializer_class = TransferredSubscriptionAPI

class SubscriptionTypeView(viewsets.ModelViewSet):
    queryset = SubscriptionType.objects.all()
    serializer_class = SubscriptionTypeAPI


class OrganizationMemberView(viewsets.ModelViewSet):
    queryset = OrganizationMember.objects.all()
    serializer_class = OrganizationMemberAPI


class OfficerView(viewsets.ModelViewSet):
    queryset = Officer.objects.all()
    serializer_class = OfficerAPI

class OfficeView(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeAPI