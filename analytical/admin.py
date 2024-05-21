from django.contrib import admin

from .models import Analytical


@admin.register(Analytical)
class AnalyticalAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    list_filter = ["id", "name"]
    search_fields = ["name"]


