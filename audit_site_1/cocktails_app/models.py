from django.db import models


# Create your models here.
class Cocktail(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название коктейля')
    is_active = models.BooleanField(default=False, verbose_name='Наличие на баре')
    description = models.TextField(blank=True, default=True, verbose_name='Описание')
    photo = models.ImageField(
        upload_to='audit_site_1/media/image/cocktails_photo/%Y/%m/%d/'
    )
    bar_price = models.IntegerField(verbose_name='Цена в меню')
    employee_price = models.IntegerField(verbose_name='Доля сотрудника')
    club_price = models.IntegerField(verbose_name='Доля клуба')
    customer_price = models.IntegerField(default=0, verbose_name='Доля заказчика(заведения)')

    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Вид коктейля')

    def __str__(self):
        return f'{self.name} {self.bar_price}'

    class Meta:
        verbose_name = 'Коктейль'
        verbose_name_plural = 'Список коктейлей'
        ordering = ['id']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Вид коктейля')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вид коктейля'
        verbose_name_plural = 'Виды коктейлей'
        ordering = ['title']
