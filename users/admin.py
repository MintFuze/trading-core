from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (  # type: ignore[operator]
        (
            "Trading",
            {
                "fields": (
                    "role",
                    "balance",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (  # type: ignore[operator]
        (
            "Trading",
            {
                "fields": (
                    "role",
                    "balance",
                )
            },
        ),
    )
