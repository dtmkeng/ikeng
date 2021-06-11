from django.contrib import admin
from core.models.profile import Profile
from core.models.subscriber import SubscriberModel


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ["name"]


@admin.register(SubscriberModel)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email",)
    search_fields = [
        "email",
    ]
