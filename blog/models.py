from django.db import models

# Create your models here.
# 게시글 내용
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    # TextField의 Text는 많을 글을 의미한다. (제한이 없다.)
    # CharField의 Char는 글자수에 제한이 있다.

    # 왜 구분을 했는냐?
    # ---> 필요한 정보를 찾을 때 편리하다.
    # ---> 용량면으로 이점이 있다.

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blog_post'


    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'