from django.contrib.auth.models import UserManager


class EnhancedUserManager(UserManager):
    """Enhanced User Manager
    """
    def is_setup_administrator(self):
        return self.filter(is_superuser=True).first()
