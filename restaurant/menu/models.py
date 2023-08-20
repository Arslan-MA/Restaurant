from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"


class Dish(models.Model):
    name = models.CharField(max_length=80)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.category} - {self.price}"

    def get_absolut_url(self):
        return f"/dish/{self.pk}"
