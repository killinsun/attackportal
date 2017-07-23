from django.db import models

class Portal(models.Model):
    user        =   models.ForeignKey('auth.User')
    firstName   =   models.CharField(max_length=32)
    lastName    =   models.CharField(max_length=32)
    vmName      =   models.CharField(max_length=32)
    vmOsName    =   models.CharField(max_length=32)

    def deployVM(self):
        self.vmName


    
