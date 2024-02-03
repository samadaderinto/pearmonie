from django.urls import path

from app.views import (
    BudgetViewSet,
    ExpenseViewSet,
    Logout,
    Login,
    register,
)

from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('register/', register, name="register"),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('login/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    
    path("users/expenses/", ExpenseViewSet.as_view(), name="expense"),
    path("users/budget/", BudgetViewSet.as_view(), name="budget")

]
