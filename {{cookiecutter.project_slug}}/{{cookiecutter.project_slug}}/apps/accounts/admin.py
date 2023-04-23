from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = [
        "username",
        "email",
        "is_active",
        "last_login",
    ]
    search_fields = ["username"]
    readonly_fields = ["username", "last_login", "date_joined"]
