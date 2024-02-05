# pearmonie


1. [Installation](#installation)
   To install required libraries and dependencies. run:
   ```
   pip install -r requirements.txt
   ```
2. [Usage](#usage)
   To run the project(start the server), you run the following code:
   ```
   python manage.py runserver
   ```
  
     
4. [API Endpoints](#api-endpoints)
   
   ```
   path('register/', register, name="register")
   path('login/', Login.as_view(), name='login')
   
   path('logout/', Logout.as_view(), name='logout')
   path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh')
     
   path("users/expense/", ExpenseViewSet.as_view(), name="expense")
   path("users/expense/all/", ExpensesViewSet.as_view(), name="expenses")
     
   path("users/budget/", BudgetViewSet.as_view(), name="budget")
   path("users/budget/all/", BudgetsViewSet.as_view(), name="budgets")
   ```

5. [Database Models](#database-models)
   
   ```
   class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(region="US")
    password = models.CharField(max_length=90)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","phone", "password"]

    objects = UserManager()
       
   
   class Expense(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       category = models.CharField(max_length=40)
       description = models.TextField(max_length=60)
       amount = models.IntegerField(validators=[MinValueValidator(1)])
       date = models.DateTimeField(auto_now_add=True)
       
   
   
   class Budget(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       category = models.CharField(max_length=40)
       amount = models.IntegerField(default=0, validators=[MinValueValidator(0)])
   ```
       
