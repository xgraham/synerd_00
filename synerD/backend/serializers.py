from rest_framework.generics import (ListCreateAPIView)
from synerD.models import *
from rest_framework import serializers


class UserInfoAPI(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"

class TransferredSubscriptionAPI(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransferredSubscription
        fields = "__all__"

class SubscriptionTypeAPI(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = "__all__"

class SubscriberAPI(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"

class ServiceAPI(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class OrganizationAPI(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"

class OrganizationMemberAPI(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrganizationMember
        fields = "__all__"


class OfficerAPI(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Officer
        fields = "__all__"

class OfficeAPI(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"
