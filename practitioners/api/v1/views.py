# from rest_framework import viewsets
from rest_framework import generics

from practitioners.api.v1.serializers import PractitionerSerializer
from practitioners.models import Practitioners


# class PractitionerViewSet(viewsets.ModelViewSet):
#     queryset = Practitioners.objects.all()
#     serializer_class = PractitionerSerializer

class PractitionerViewSet(generics.ListCreateAPIView):
    queryset = Practitioners.objects.all()
    serializer_class = PractitionerSerializer
    permission_classes=[]
