from rest_framework.permissions import BasePermission

class IsCustomer(BasePermission):
    def has_persmission(self, request, view):
        return(
            request.user.is_authenticated
            and request.user.role == 'CUSTOMER'
        ) 

class IsDealer(BasePermission):
    def has_permission(self, request, view):
        return(
            request.user.is_authenticated
            and request.user.role == 'DEALER'
        )

class IsBusiness(BasePermission):
    def has_permission(self, request, view):
        return(
            request.user.is_authenticated 
            and request.user.role == 'BUSINESS'
        )

class isAdmin (BasePermission):
    def has_permission(self, request, view):
        return(
            request.user.is_authenticated
            and request.user.is_staff
        )