from django.db import models

# Create your models here.
class PostTable(models.Model):
    postId = models.AutoField(primary_key=True, db_column='postID')
    userId = models.ForeignKey('user.UserTable', models.DO_NOTHING, db_column='userID')
    postTitle = models.CharField(max_length=255, null=False, db_column='postTitle')
    postContent = models.TextField(null=False, db_column='postContent')
    postCreatedAt = models.DateTimeField(auto_now_add=True, db_column='postCreatedAt')
    postUpdatedAt = models.DateTimeField(auto_now=True, db_column='postUpdatedAt')
    categoryId = models.ForeignKey('category.CategoryTable', models.DO_NOTHING, db_column='catID')

    def __str__(self):
        return self.postTitle
    class Meta:
        app_label = 'posts'
        db_table = 'postTable'
        # managed = False
        # verbose_name = 'Post'
        # verbose_name_plural = 'Posts'
        # ordering = ['postCreatedAt']