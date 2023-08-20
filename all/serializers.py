from rest_framework import serializers

from .models import *


class TelegramRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUserModel
        fields = '__all__'


class ServiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUserModel
        fields = '__all__'


class KorzinaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = KorzinaModel
        fields = '__all__'