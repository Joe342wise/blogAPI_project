from django.db import models

# Create your models here.
class CommentTable(models.Model):
    commentId = models.AutoField(primary_key=True, db_column='commentID')
    postId = models.ForeignKey('posts.PostTable', on_delete=models.CASCADE, db_column='postID')
    userId = models.ForeignKey('user.UserTable', on_delete=models.CASCADE, db_column='userID')
    content = models.TextField(db_column='commentContent')
    createdTime = models.DateTimeField(db_column='commentCreatedAt')
    
    def __str__(self):
        return self.content
    
    class Meta:
        app_label = 'comment'
        db_table = 'tblComment'
