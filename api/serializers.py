from shop.models import Product
from rest_framework import serializers
from account.models import ShopUser


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 'description', 'new_price']


class ShopUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = ['phone', 'first_name', 'last_name', 'date_joined']


class UerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = ['phone', 'first_name', 'last_name', 'address', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = ShopUser(phone=validated_data['phone'], first_name=validated_data['first_name'],
        last_name=validated_data['last_name'], address=validated_data['address']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
