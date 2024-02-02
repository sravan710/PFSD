from django.db import models


# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, blank=False, unique=True)  # blank mean the name should not be empty
    password = models.CharField(max_length=12, blank=False)

    class Meta:
        db_table = "admin_table"

    def str(self):
        return self.username