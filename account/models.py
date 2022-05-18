from django.db import models

# Create your models here.
def _create_user(self, email, password, **kwargs):
    if not email:
        raise ValueError('The given email must be set!')
    email = self.normalize_email(email=email)
    user = self.model(email=email, **kwargs)
    user.create_activation_code()
    user.set_password(password)
    user.save(using=self._db)
    return user
