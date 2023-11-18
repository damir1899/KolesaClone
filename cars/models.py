from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel


class EngineTypeChoices(models.IntegerChoices):
    GASOLINE = 1, _('Бензин')
    DIESEL = 2, _('Дизель')
    GAS_GASOLINE = 3, _('Газ-бензин')
    GAS = 4, _('Газ')
    HYBRID = 5, _('Гибрид')
    ELECTRIC = 6, _('Электрический')
    
class TransmissionChoices(models.IntegerChoices):
    MANUAL = 1, _('Механическая')
    AUTOMATIC = 2, _('Автомат')
    TIPTRONIC = 3, _('Типтроник')
    VARIATOR = 4, _('Вариатор')
    ROBOT = 5, _('Робот')

class WheelLocationChoices(models.IntegerChoices):
    RIGHT = 1, _('Справа')
    LEFT = 2, _('Слева')
    
class DriveTypeChoices(models.IntegerChoices):
    FRONT = 1, _('Передний привод')
    REAR = 2, _('Задний привод')
    FULL = 3, _('Полный привод')
    

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
        
        
class CarModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, verbose_name='Марка')
    
    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
        
        
class CarGeneration(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Модель')
    date_from = models.DateField(verbose_name='Дата выпуска')
    date_to = models.DateField(verbose_name='Дата окончания выпуска', null=True, blank=True)
    image = models.ImageField(upload_to= 'generation', verbose_name='Изображение')
    
    class Meta:
        verbose_name = 'Поколение'
        verbose_name_plural = 'Поколения'
        
    
class Post():
    pass

