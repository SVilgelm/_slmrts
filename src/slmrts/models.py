# -*- coding: utf-8 -*-
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from phonenumber_field.modelfields import PhoneNumberField


class Bouquet(models.Model):
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, )
    name = models.CharField(verbose_name='Название', max_length=100, unique=True, blank=False, null=False)
    cost = models.DecimalField(verbose_name='Цена', max_digits=7, decimal_places=2, null=False)
    note = models.TextField(verbose_name='Примечание')
    is_stock = models.BooleanField(verbose_name='В наличии', default=False, null=False, blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Букет'
        verbose_name_plural = u'Букеты'
        ordering = ('-created',)


class Photo(models.Model):
    bouquet = models.ForeignKey(Bouquet, verbose_name='Букет', null=False)
    original_image = models.ImageField(verbose_name='Фотография', upload_to='photos')
    big_image = ImageSpecField(
        processors=[
            ResizeToFill(480, 480),
        ],
        image_field='original_image',
        format='JPEG',
        options={'quality': 90},
    )
    small_image = ImageSpecField(
        processors=[
            ResizeToFill(128, 128)
        ],
        image_field='original_image',
        format='JPEG',
        options={'quality': 60},
    )

    class Meta:
        verbose_name = u'Фотография'
        verbose_name_plural = u'Фотографии'


class Client(models.Model):
    email = models.EmailField(verbose_name='Email', unique=True)
    phone = PhoneNumberField(verbose_name='Телефон', null=False, blank=False)
    name = models.CharField(verbose_name='ФИО', max_length=100, null=False, blank=False)
    code = models.CharField(verbose_name='Код', max_length=32, null=False, blank=False, unique=True)


class Order(models.Model):
    STATUS_WAIT = 'wait'
    STATUS_IN_PROCESS = 'in_process'
    STATUS_DONE = 'done'
    STATUS_CANCELED = 'canceled'
    STATUS_GIVEN = 'given'
    STATUS_CHOICES = (
        (STATUS_WAIT, 'Ожидает'),
        (STATUS_IN_PROCESS, 'В процессе'),
        (STATUS_DONE, 'Готово'),
        (STATUS_GIVEN, 'Отдано'),
        (STATUS_CANCELED, 'Отменено'),
    )
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=False, blank=False)
    changed = models.DateTimeField(verbose_name='Дата изменения', auto_now=True, null=False, blank=False)
    client = models.ForeignKey(Client, verbose_name='Клиент', null=True)
    bouquet = models.ForeignKey(Bouquet, verbose_name='Букет', null=False)
    date = models.DateField(verbose_name='Дата изготовления', null=False, blank=False)
    status = models.CharField(verbose_name='Статус', max_length=30, choices=STATUS_CHOICES,
        default=STATUS_WAIT, null=False, blank=False
    )
    note = models.TextField(verbose_name='Примечание')
