from django.contrib.auth.models import User
from .models import Palette
from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username', "")
        password = data.get('password', "")
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user']=user
                else:
                    msg='user not active'
                    exceptions.ValidationError(msg)
            else:
                msg="user not valid"
                exceptions.ValidationError(msg)
        
        else:
            msg = "field can't empty"
            raise exceptions.ValidationError(msg)
        return data

class PaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields =[
            'url',
            'color_name',
            'color_domain_one',
            'color_domain_two',
            'color_accent_one',
            'color_accent_two',
            'status'
        ]