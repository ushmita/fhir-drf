from django.db import transaction

from rest_framework import serializers
from practitioners.models import Practitioners
from qualifications.models import Qualifications
from communications.models import Communications


class QualificationSerializer():
    class Meta:
        model = Qualifications
        fields = ['id', 'code', 'period', 'issuer']
        read_only_fields = ['id']


class CommunicationSerializer():
    class Meta:
        model = Communications
        fields = ['language', 'preffered']
        read_only_fields = ['id']


class PractitionerSerializer(serializers.ModelSerializer):
    language = serializers.CharField(write_only=True)
    preffered = serializers.BooleanField(write_only=True)
    code = serializers.CharField(write_only=True)
    period = serializers.IntegerField(write_only=True)
    issuer = serializers.CharField(write_only=True)

    class Meta:
        model = Practitioners
        fields = ['id', 'name', 'active', 'period', 'language', 'issuer', 'preffered', 'code',
                  'telecom', 'gender', 'birth_date', 'deceased', 'address', 'photo', 'communication', 'qualification']
        depth = 1

    @transaction.atomic
    def create(self, validated_data):
        print(validated_data.get('language'))
        language = validated_data.pop('language')
        preffered = validated_data.pop('preffered')
        code = validated_data.pop('code')
        period = validated_data.pop('period')
        issuer = validated_data.pop('issuer')

        practitioner = Practitioners.objects.create(**validated_data)
        communication = Communications.objects.create(
            language=language,
            preffered=preffered,
            practitioner=practitioner
        )

        qualification = Qualifications.objects.create(
            code=code,
            period=period,
            issuer=issuer,
            practitioners=practitioner
        )

        return practitioner
