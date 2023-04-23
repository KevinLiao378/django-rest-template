from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = [
        (
            "个人信息",
            {
                "fields": (
                    "username",
                    "email",
                    "password",
                    "last_login",
                    "date_joined",
                )
            },
        ),
        (
            "权限",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    ]
    list_display = [
        "username",
        "email",
        "is_active",
        "last_login",
    ]
    search_fields = ["username"]
    readonly_fields = ["username", "last_login", "date_joined"]
