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
  
3. [Authentication](#authentication)
   

     
5. [API Endpoints](#api-endpoints)
   * Endpoint 1: /api/register/
   * Method: POST
   * Description: Retrieve a list of resources.
   * Request: None
   * Response:

     ```
     {
       "id": 1,
       "email": "samd@gmail.com",
       "first_name": "samaad",
       "phone": "+2349021162144",
       "created": "2024-02-05T11:42:37.269971Z",
       "updated": "2024-02-05T11:42:37.269996Z"
        }
     ```

   * Endpoint 2: /api/login/
   * Method: POST
   * Description: Retrieve a list of resources.
   * Request: None
   * Response:

     ```
     {
          "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNzc0MjA0NiwiaWF0IjoxNzA3MTM3MjQ2LCJ dummy qdGkiOiJhNTU1Y2JlZmExMmY0ZmU3ODc2MDIxYzRiZjg0OWJmNCIsInVzZXJfaWQiOjF9.wFY2h1WZTiSqogGi1s7WyJ0BM4WhoAxVFXL86ovPVyk",
          "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3Mzk2NDQ2LCJpYXQiOjE3MDcxMzcyNDYsImp0aSI6 dummy IjEwMGRjNDc2NTE2MDRkZDBhMWQ1NTdlYmM2YmEwYzQyIiwidXNlcl9pZCI6MX0.m169D0RoesCZMjrOMWoIYvIv6b5iw_ySUygU1Bd_hQY"
      }
     ```


   * Endpoint 3: /api/logout/
   * Method: POST
   * Description: Retrieve a list of resources.
   * Request: None
   * Response: None


   * Endpoint 4: /api/login/refresh/
   * Method: POST
   * Description: Retrieve a list of resources.
   * Request: None
   * Response:

     ```
     {
          "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3Mzk2NDQ2LCJpYXQiOjE3MDcxMzcyNDYsImp0aSI6 dummy IjEwMGRjNDc2NTE2MDRkZDBhMWQ1NTdlYmM2YmEwYzQyIiwidXNlcl9pZCI6MX0.m169D0RoesCZMjrOMWoIYvIv6b5iw_ySUygU1Bd_hQY"
      }
     ```

   * Endpoint 5: /api/user/expense/
   * Method: POST
   * Description: Retrieve a list of resources.
   * Request: None
   * Response:

     ```
     {
          "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3Mzk2NDQ2LCJpYXQiOjE3MDcxMzcyNDYsImp0aSI6 dummy IjEwMGRjNDc2NTE2MDRkZDBhMWQ1NTdlYmM2YmEwYzQyIiwidXNlcl9pZCI6MX0.m169D0RoesCZMjrOMWoIYvIv6b5iw_ySUygU1Bd_hQY"
      }
     ```
     
   * Endpoint 6: /api/user/expense/all/
   * Method: POST
   * Description: Retrieve a list of resources.
   * Request: None
   * Response:

     ```
     {
          "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3Mzk2NDQ2LCJpYXQiOjE3MDcxMzcyNDYsImp0aSI6 dummy IjEwMGRjNDc2NTE2MDRkZDBhMWQ1NTdlYmM2YmEwYzQyIiwidXNlcl9pZCI6MX0.m169D0RoesCZMjrOMWoIYvIv6b5iw_ySUygU1Bd_hQY"
      } 
     
   * Endpoint 7: /api/user/budget/
   * Method: POST
   * Description: Retrieve a list of resources.
   * Request: None
   * Response:

     ```
     {
          "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3Mzk2NDQ2LCJpYXQiOjE3MDcxMzcyNDYsImp0aSI6 dummy IjEwMGRjNDc2NTE2MDRkZDBhMWQ1NTdlYmM2YmEwYzQyIiwidXNlcl9pZCI6MX0.m169D0RoesCZMjrOMWoIYvIv6b5iw_ySUygU1Bd_hQY"
      }

     
   * Endpoint 8: /api/user/budget/all/
   * Method: POST
   * Description: Retrieve a list of resources.
   * Request: None
   * Response:

     ```
     {
          "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3Mzk2NDQ2LCJpYXQiOjE3MDcxMzcyNDYsImp0aSI6 dummy IjEwMGRjNDc2NTE2MDRkZDBhMWQ1NTdlYmM2YmEwYzQyIiwidXNlcl9pZCI6MX0.m169D0RoesCZMjrOMWoIYvIv6b5iw_ySUygU1Bd_hQY"
      }
   ```

6. [Database Models](#database-models)
   
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
       
