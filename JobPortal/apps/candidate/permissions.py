from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    # # def has_permission(self, request, view):
    # #     print('hoh')
    # #     if request.user.is_authenticated:
    # #         return True
    # #     return False
    #
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return
        return obj.user == request.user
    #     # print('here')
    #     # if request.user.is_superuser:
    #     #     print(1)
    #     #     return True
    #     #
    #     # if request.user == obj.user:
    #     #     print(2)
    #     #     return True
    #     #
    #     # return False
    #

    # def has_permission(self, request, view):
    #     return False