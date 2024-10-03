from django.db import models


class Category(models.Model):  # категории рецептов
    category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.category}'


class Recips(models.Model):  # рецепты
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255, default='Название рецепта')
    text = models.TextField(default='Текст рецепта')
