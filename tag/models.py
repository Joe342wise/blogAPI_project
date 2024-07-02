from django.db import models

# Create your models here.
class TagTable(models.Model):
    tagId = models.AutoField(primary_key=True, db_column='tagID')
    tagName = models.CharField(max_length=50, null=False, db_column='tagName')

    def __str__(self):
        return self.tagName
    
    class Meta:
        app_lable = 'tag'
        db_table = 'tblTag'
