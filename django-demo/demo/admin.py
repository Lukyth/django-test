from django.contrib import admin

from demo.models import Bank
from demo.forms import BankForm
# Register your models here.

admin.site.register(Bank, BankForm)
# todo : register Unit model
