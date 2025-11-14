from django.db import models

class Main(models.Model):
    rasm = models.ImageField(upload_to='media')
    tavsif = models.TextField(blank=True)
    haqida = models.CharField(max_length=200)
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.haqida
    
    
    class Meta:
        verbose_name = 'Main'
        verbose_name_plural = 'Mening Narsalarim'