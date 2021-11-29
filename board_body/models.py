from django.db import models



class Post(models.Model):
    image = models.ImageField(upload_to='post_images')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    categories = models.ManyToManyField('Categories', related_name='cate_post')
    condition = models.ManyToManyField('Condition', related_name='cond_post')
    number = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name}'


class Categories(models.Model):
    cate = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.cate}'


class Condition(models.Model):
    cond = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.cond}'

