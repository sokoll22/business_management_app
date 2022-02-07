from django.db import models
from django.utils import timezone


# Create your models here.
class Employee(models.Model):
    created_at = models.DateTimeField(verbose_name='Дата внесения в базу', auto_now_add=timezone.now())  # автоматически записывает дату создания
    updated_at = models.DateTimeField(verbose_name='Последнее изменение', auto_now=timezone.now())  # автоматически записывает дату изменения
    employee_status = models.BooleanField(default=False, verbose_name='На смене/выходной')  # Статус работника(в штате, не в штате)
    job_status = models.ForeignKey('JobPosition', on_delete=models.PROTECT, null=True, verbose_name='Должность работника')  # Статус работника(в штате, не в штате)

    first_name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')

    position = models.CharField(max_length=64, blank=True, verbose_name='Должность')
    phone_number = models.IntegerField(verbose_name='Номер телефона')
    e_mail = models.EmailField(max_length=128)
    url = models.CharField(max_length=256, verbose_name='Ссылка на личную страницу')    # загрузить библиотеку URL,models.CharField поменять на другую

    rate = models.IntegerField(verbose_name='Ставка') #  stavka
    bonus = models.FloatField(default=0, verbose_name='Процент от кассы')
    bar_bonus = models.FloatField(default=0, verbose_name='Процент от бара')
    interest_50 = models.IntegerField(verbose_name='Чаевые 50%')  #  50 % ot uslug
    interest_bar = models.IntegerField(verbose_name='Процент с бара')  # % from bar1
    photo = models.ImageField(upload_to='media/image/employee_photo/%Y/%m/%d/', blank=True)
    video = models.FileField(upload_to='media/video/employee_video/%Y/%m/%d/', blank=True)
    # date_of_employment = models.DateField()
    # date_of_disemployment = models.DateField()
    reason_of_disemployment = models.TextField(max_length=256, verbose_name='Причина увольнения')       #причина увольнения
    notes = models.TextField(max_length=256, verbose_name='Заметки о сотруднике')                       #заметки о работнике

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.position.lower()}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Список сотрудников'
        ordering = ['-employee_status']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Статус в базе')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус в базе'
        verbose_name_plural = 'Статусы в базе'
        ordering = ['title']


class JobPosition(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Должность работника')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Список должностей'
        ordering = ['title']


