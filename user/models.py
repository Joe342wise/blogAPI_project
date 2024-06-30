from django.db import models

# Create your models here.
class UserTable(models.Model):
    userId = models.AutoField(primary_key=True, db_column='userId')
    username = models.CharField(max_length=50, null=False, db_column='userName')
    email = models.CharField(max_length=255, null=False, db_column='userEmail')
    password = models.CharField(max_length=100, null=False, db_column='userPassword')    
    created_at = models.DateTimeField(auto_now_add=True, db_column='userCreatedAt')

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'user'
        db_table = 'tblUser'