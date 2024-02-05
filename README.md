# pearmonie


1. [Installation](#installation)
   To install required libraries and dependencies. run:
   * pip install -r requirements.txt
  
     
2. [API Endpoints](#api-endpoints)
   
   * path('register/', register, name="register"),
   * path('login/', Login.as_view(), name='login'),
   * path('logout/', Logout.as_view(), name='logout'),
   * path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     
   * path("users/expense/", ExpenseViewSet.as_view(), name="expense"),
   * path("users/expense/all/", ExpensesViewSet.as_view(), name="expenses"),
     
   * path("users/budget/", BudgetViewSet.as_view(), name="budget"),
   * path("users/budget/all/", BudgetsViewSet.as_view(), name="budgets"),
