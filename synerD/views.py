from django.http import HttpResponse
from django.template import loader

from .models import *


def index(request):
    template = loader.get_template('synerd/index.html')

    return HttpResponse(template.render( request=request))

def login(request):
    template = loader.get_template('synerd/login.html')

    return HttpResponse(template.render( request=request))

def console(request):
    template = loader.get_template('synerd/admin.html')

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