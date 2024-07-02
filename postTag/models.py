from django.db import models

# Create your models here.
class PostTagTable(models.Model):
    postId = models.ForeignKey('posts.PostTable', on_delete=models.CASCADE, db_column='postID')
    tagId = models.ForeignKey('tag.TagTable', on_delete=models.CASCADE, db_column='tagID')

    class Meta:
        app_lable = 'postTag'
        db_table = 'tblPostTag'