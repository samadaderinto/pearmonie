from django.contrib import admin

from app.models import Budget, Expense, User

# Register your models here.

admin.site.register(User)
admin.site.register(Expense)
admin.site.register(Budget)