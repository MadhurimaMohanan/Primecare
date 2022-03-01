from .models import P_user
from .models import P_Contact
from  rest_framework import serializers


class userSerializer(serializers.ModelSerializer):

    class Meta:
        model=P_user
        fields='__all__'

class contactSerializer(serializers.ModelSerializer):

    class Meta:
        model=P_Contact
        fields='__all__'