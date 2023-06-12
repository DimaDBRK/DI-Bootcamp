from rest_framework import permissions
from .models import DepartmentAdmin

# class IsOwner(permissions.BasePermission):
    
#     def has_object_permission(self, request, view, obj):
        
#         #check method is safe: GET, HEAD, OPTIONS
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         elif request.user == obj.author:
#             return True
#         else:
#             return False

class IsDepartmentAdmin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        user = request.user if request.user.is_authenticated else None
        print(user)
        check = DepartmentAdmin.objects.filter(author=user).exists()
       
        if check: #check if it is attribute
            return True
        else:
             return False
        