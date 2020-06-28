from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist 

class EmailBackend(ModelBackend):

    def authenticate(self, request, username, password,**kwargs):
        user = get_user_model()
        try:
            user = User.objects.get(email = username)
            if user.check_password(password):
                return user
            else:
                return None   
        except ObjectDoesNotExist:
            return None
                              


    def get_user(self, user_id):
        user = get_user_model
        try:
            user = User.objects.get(pk = user_id)
            return user
        except:
            return None
