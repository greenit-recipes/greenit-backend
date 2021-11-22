from django.db import models

class CommentRecipe(models.Model):
    recipe = models.ForeignKey('recipe.Recipe', on_delete=models.CASCADE, related_name='comment_recipe')
    likes = models.ManyToManyField(
        'user.User',
        related_name='comment_like'
    )
    comment = models.TextField(max_length=512, default='')
    author = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='comment_author')
    created_at = models.DateTimeField(auto_now_add=True, null=True)