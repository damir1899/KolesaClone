from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from auth_user.models import ProfileUser


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
    
class ColorChoices(models.IntegerChoices):
    WHITE = 1, _('Белый')
    GREEN = 2, _('Зеленый')
    BLACK = 3, _('Черный')
    BLUE = 4, _('Синий')
    ORANGE = 5, _('Оранжевый')
    RED = 6, _('Красный')
    

class Category(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Название')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'
    
    def __str__(self) -> str:
        return self.name
    
class CarType(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    
    class Meta:
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузовы'
        
    def __str__(self) -> str:
        return f'{self.name} {self.category}'
    

class CountryManufacturer(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    
    class Meta:
        verbose_name = 'Страна производителя'
        verbose_name_plural = 'Страны производителей'
        
    def __str__(self) -> str:
        return self.name
    
    
class CarBrand(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    country = models.ForeignKey(CountryManufacturer, on_delete=models.PROTECT, verbose_name='Страна')
    
    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'
        
    def __str__(self) -> str:
        return f'{self.name} {self.country}'
        
        
class CarModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, verbose_name='Марка')
    
    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
        
    def __str__(self) -> str:
        return f'{self.name} {self.brand}'
        
        
class CarGeneration(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Модель')
    car_type = models.ForeignKey(CarType, on_delete=models.PROTECT, verbose_name='Кузов')
    date_from = models.DateField(verbose_name='Дата выпуска')
    date_to = models.DateField(verbose_name='Дата окончания выпуска', null=True, blank=True)
    image = models.ImageField(upload_to= 'generation', verbose_name='Изображение')
    
    class Meta:
        verbose_name = 'Поколение'
        verbose_name_plural = 'Поколения'
        
    def __str__(self) -> str:
        return f'{self.model.brand} {self.model} {self.name} {self.date_from} {self.date_to}'
    
    
class CarModification(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Модификация')
    generation = models.ForeignKey(CarGeneration, on_delete=models.PROTECT, verbose_name='Поколение')
    horses_power = models.PositiveIntegerField(verbose_name='Лошадиные силы')
    engine_type = models.IntegerField(choices=EngineTypeChoices.choices, verbose_name='Тип двигателя')
    engine_volume = models.PositiveIntegerField(max_length=20, verbose_name='Обьем двигателя')
    transmission = models.IntegerField(choices=TransmissionChoices.choices, verbose_name='Коробка передач')
    drive_type = models.IntegerField(choices=DriveTypeChoices.choices, verbose_name='Привод')
        
        
class City(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        
    def __str__(self) -> str:
        return self.name
    

class File(BaseModel):
    file_name = models.TextField()
    file_size = models.PositiveBigIntegerField(help_text='File size in bytes')
    uploaded_by = models.ForeignKey(ProfileUser, null=True, on_delete=models.SET_NULL, related_name='files')
    local_file = models.FileField(upload_to='files/', null=True, blank=True)
    s3_url = models.TextField(null=False, blank=True)

    @property
    def url(self):
        return self.local_file.url if self.local_file else self.s3_url

    def to_dict(self):
        return {
            'id': self.id,
            'file_name': self.file_name,
            'file_size': self.file_size,
            'url': self.url,
        }

    def __str__(self):
        return self.file_name
        
    
class Post(BaseModel):
    author = models.ForeignKey(ProfileUser, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    car = models.ForeignKey(CarModification, on_delete=models.PROTECT, verbose_name='Модификация')
    description = models.TextField(verbose_name='Описание')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='Город')
    kilometrage = models.PositiveBigIntegerField(verbose_name='Пробег')
    wheel = models.IntegerField(choices=WheelLocationChoices.choices, default=WheelLocationChoices.LEFT, verbose_name='Расположение руля')
    is_cleared = models.BooleanField(verbose_name='Растаможен')
    color = models.IntegerField(choices=ColorChoices.choices, verbose_name='Цвет')
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    
    
    

