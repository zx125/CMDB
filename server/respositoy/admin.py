from django.contrib import admin

# Register your models here.

from respositoy import models

admin.site.register(models.Server)
admin.site.register(models.Disk)
admin.site.register(models.UserProfile)
admin.site.register(models.UserGroup)
admin.site.register(models.Memory)
admin.site.register(models.ErrorLog)
admin.site.register(models.AssetRecord)
admin.site.register(models.BusinessUnit)
admin.site.register(models.NIC)
admin.site.register(models.Tag)
admin.site.register(models.IDC)




