from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


from app.models import Budget, Expense, User
from app.permissions import AccessPolicies
from app.serilalizers import BudgetSerializer, CustomTokenSerializer, ExpenseSerializer, UserSerializer
from app.utils import auth_token



# Create your views here.

@api_view(["POST"])
@permission_classes((AccessPolicies,))
def register(request):
    data = JSONParser().parse(request)
    
    if User.objects.filter(email=data["email"]).exists():
        return Response({"error": "Email already registered"}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(**data)
    serializer = UserSerializer(user)
    token = auth_token(user)
   
    return Response(serializer.data, headers={"Authorization": token}, status=status.HTTP_201_CREATED)
            
            
class Login(TokenObtainPairView, generics.GenericAPIView):
    serializer_class = CustomTokenSerializer
    permission_classes = (AccessPolicies,)

    
class ExpenseViewSet(GenericAPIView):
    permission_classes = (AccessPolicies,)

    def post(self, request, *args, **kwargs):
        data = request.data
        budget = get_object_or_404(Budget, user=data.get("user"), category=request.data.get("category"))
        amount = data.get("amount")
        serializer = ExpenseSerializer(data=data)
        
        if serializer.is_valid():
            if amount <= budget.amount:
                budget -= amount
                budget.save()
            else:
                Response({"message": "Insufficient Balance"}, status=status.HTTP_400_BAD_REQUEST)
        
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
      
        expense = get_object_or_404(Expense,user=request.data.get("user"), category=request.data.get("category"))
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        data = request.data
        expense = get_object_or_404(Expense,user=data.get("user"),category=request.data.get("category"))
        serializer = ExpenseSerializer(expense, data=data)
        if serializer.is_valid():
           serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def delete(self, request, *args, **kwargs):
    
        expense = get_object_or_404(Expense,user=request.data.get("user"), category=request.data.get("category"))
        expense.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
     
        
class ExpensesViewSet(GenericAPIView):
       def get(self, request, *args, **kwargs):

        expenses = Expense.objects.filter(
            user=request.data.get("user"))
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
class BudgetViewSet(GenericAPIView):
    permission_classes = (AccessPolicies,)

    def post(self, request, *args, **kwargs):
    
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
    def get(self, request, *args, **kwargs):

        expense = get_object_or_404(Budget,user=request.data.get("user"),category=request.data.get("category"))
        serializer = BudgetSerializer(expense)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        data = request.data
        expense = get_object_or_404(Budget,user=request.data.get("user"),category=request.data.get("category"))
        serializer = BudgetSerializer(expense, data=data)
        if serializer.is_valid():
           serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    
    def delete(self, request, *args, **kwargs):
       
        expense = get_object_or_404(Budget,user=request.data.get("user"), id=request.data.get("user"),category=request.data.get("category"))
        expense.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
     
    
class BudgetsViewSet(GenericAPIView):   
    def get(self, request, *args, **kwargs):

        expenses = Budget.objects.filter(
            user=request.data.get("user"))
        serializer = BudgetSerializer(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)            
        
class Logout(GenericAPIView):
    permission_classes = (AccessPolicies,)

    def post(self, request, *args, **kwargs):
        try:
            RefreshToken(request.data["refresh"]).blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)