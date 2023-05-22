from django.urls import path, include
from rest_framework import routers
from practitioners.api.v1.views import PractitionerViewSet

# Create your views here.

# router = routers.DefaultRouter()
# router.register(r'', PractitionerViewSet, 'practitioners')
# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('', PractitionerViewSet.as_view())
]
