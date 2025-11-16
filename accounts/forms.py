from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# ----------------------
# Formulario de registro
# ----------------------
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# ----------------------
# Formulario de edición de perfil
# ----------------------
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
