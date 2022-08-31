from django import forms
from django.contrib.auth import get_user_model
from user_profile.models import Name

User = get_user_model()


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(
        label="أسم المستخدم",
        max_length=30,
        help_text="لا يجب أن يحتوي أسم المستخدم علي مسافات",
    )
    date_of_birth = forms.DateField(widget=forms.DateInput, label="تاريخ الميلاد")
    email = forms.EmailField(label="البريد الإلكتروني")
    password1 = forms.CharField(
        label="كلمة المرور",
        widget=forms.PasswordInput(),
        min_length=8,
        help_text="كلمة المرور يجب أن تحتوي على 8 أحرف علي الأقل",
    )

    password2 = forms.CharField(
        label="تأكيد كلمة المرور", widget=forms.PasswordInput(), min_length=8
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "date_of_birth",
            "password1",
            "password2",
        )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] != cd["password2"]:
            raise forms.ValidationError("كلمة المرور غير متطابقة !")
        return cd["password2"]

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd["username"]).exists():
            raise forms.ValidationError("يوجد مستخدم مسجل بهذا الأسم")

        return cd["username"]

    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd["email"]).exists():
            raise forms.ValidationError("هذا البريد موجود بالفعل")

        return cd["email"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label="البريد الإلكتروني")
    date_of_birth = forms.DateField(label="تاريخ الميلاد")

    class Meta:
        model = User
        fields = ("email", "date_of_birth")


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label="اسمك")
    last_name = forms.CharField(label="اسم العائلة")

    class Meta:
        model = Name
        fields = ("first_name", "last_name")
