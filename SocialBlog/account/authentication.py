from django.contrib.auth.models import User

class EmailAuthBackend:

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email = username)
            if user.check_password(password):
                return user
            return None
        except(User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        user = User.objects.get(pk = user_id)
        if user:
            return user
        return None
            