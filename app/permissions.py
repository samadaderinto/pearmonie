from rest_access_policy import AccessPolicy


# all views with permitted users in json


class AccessPolicies(AccessPolicy):
    statements = [
        {
            "action": [
                "register",
                "Login",
            ],
            "principal": "*",
            "effect": "allow",
        },
        {
            "action": [
                "Logout",
                "BudgetViewSet",
                "ExpenseViewSet",
                "ExpensesViewSet",
                "BudgetsViewSet"
                
               
            ],
            "principal": ["authenticated"],
            "effect": "allow"
        },
       
    ]