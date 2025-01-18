from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title



class Comment(models.Model):
    message = models.TextField(blank=False, null=False)
    blog = models.ForeignKey(to=Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.message


class CommentLike(models.Model):
    comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.comment.message



