from django.contrib import admin

class BankForm(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
