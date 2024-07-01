from django.db import models

# Create your models here.
class CategoryTable(models.Model):
    catigoryId = models.AutoField(primary_key=True, db_column='catID')
    catigoryName = models.CharField(max_length=50, null=False, db_column='catName')

    def __str__(self):
        return self.catigoryName
    
    class Meta:
        app_label = 'category'
        db_table = 'tblCategory'
        # managed = True
        # verbose_name = 'Category'
        # verbose_name_plural = 'Categories'
        # ordering = ['catigoryName']