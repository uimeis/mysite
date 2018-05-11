from django.db import models

# Create your models here.

class Blog(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(default='default.png', upload_to='images/')
    title = models.CharField(default='博客标题', max_length=50)


    def __str__(self):
        return self.title