from django.urls import include, path
from rest_framework import routers
from .. import views

router = routers.DefaultRouter()
router.register(r'UserInfo', views.UserInfoView)
router.register(r'TransferredSubscription', views.TransferredSubscriptionView)
router.register(r'SubscriptionType', views.SubscriptionTypeView)
router.register(r'Subscriber', views.SubscriberView)
router.register(r'Service', views.ServiceView)
router.register(r'OrganizationMember', views.OrganizationMemberView)
router.register(r'Organization', views.OrganizationView)
router.register(r'Officer', views.OfficerView)
router.register(r'Office', views.OfficeView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]