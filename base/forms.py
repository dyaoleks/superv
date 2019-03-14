from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from laws . models import *


class ObjectTypeForm(forms.ModelForm):
    class Meta:
        model = ObjectType

        exclude = [""]