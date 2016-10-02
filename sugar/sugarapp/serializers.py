from rest_framework import serializers
from sugarapp.models import Baby, Daddy


class BabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Baby
        fields = ('id', 'first_name', 'last_name')

class DaddySerializer(serializers.ModelSerializer):
    class Meta:
        model = Daddy
        fields = ('id', 'first_name', 'last_name')