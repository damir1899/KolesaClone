from django.db import models
from common.models import BaseModel


class EngineTypeChoices(models.IntegerChoices):
    GASOLINE = 1, _('Бензин')


class Category(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Название')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'
    
class CarType(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    
    class Meta:
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузовы'
    

class CountryManufacturer(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    
    class Meta:
        verbose_name = 'Страна производителя'
        verbose_name_plural = 'Страны производителей'
    
    
class CarBrand(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    country = models.ForeignKey(CountryManufacturer, on_delete=models.PROTECT, verbose_name='Страна')
    
    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'
    

