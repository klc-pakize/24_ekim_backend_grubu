from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_staff)
    
        # if request.method == 'GET':
        #     return True
        
        # return bool(request.user and request.user.is_staff)
    

class IsOwnerAndStaffOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return bool(request.user and request.user.is_staff and (obj.user == request.user))