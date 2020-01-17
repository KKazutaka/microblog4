from django.db import models

class Blog(models.Model):
    content = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Maxim(models.Model):
    saying = models.TextField(max_length=300)

    def __str__(self):
        return self.saying

