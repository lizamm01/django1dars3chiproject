from django.db import models
from django.utils import timezone

class Viloyat(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_bool = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Viloyat"
        verbose_name_plural = "VILOYATLAR"
        ordering = ['-created_at']

class Tuman(models.Model):
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_bool = models.BooleanField(default=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tuman"
        verbose_name_plural = "TUMANLAR"
        ordering = ['-created_at']

class Mahalla(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    is_bool = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mahalla"
        verbose_name_plural = "MAHALLALAR"
        ordering = ['-created_at']