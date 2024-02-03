from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework import serializers


from app.models import Budget, Expense, User


class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "phone",
            "password",
            "created",
            "updated",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            user.make_password(self.password)
            user.save()

            return user


class EmailTokenSerializer(TokenObtainSerializer):
    username_field = User.EMAIL_FIELD
    
class CustomTokenSerializer(EmailTokenSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data
    
    
    
class ExpenseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Expense
        fields = [
            "id",
            "user",
            "category",
            "description",
            "amount",
            "date"
        ]
        
        
        
class BudgetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Budget
        fields = [
            "id",
            "user",
            "category",
            "amount"
        ]
    