from django.contrib import admin

# Register your models here.
from modelserializer_app.models import Account,HighScore
admin.site.register(Account)
admin.site.register(HighScore)