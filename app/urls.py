from django.urls import path

from app.views import (
    BudgetViewSet,
    BudgetsViewSet,
    ExpenseViewSet,
    ExpensesViewSet,
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
    
    path("user/expense/", ExpenseViewSet.as_view(), name="expense"),
    path("user/expense/all/", ExpensesViewSet.as_view(), name="expenses"),
    
    path("user/budget/", BudgetViewSet.as_view(), name="budget"),
    path("user/budget/all/", BudgetsViewSet.as_view(), name="budgets"),
    

]
