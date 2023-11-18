from django.db import models
from django.contrib.auth.models import User, UserManager, PermissionsMixin

from imagekit import processors
from imagekit.models import ProcessedImageField


class ProfileUser(User, PermissionsMixin):
    email_new = models.EmailField(max_length=70, null=True, blank=True)
    middle_name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    avatar = ProcessedImageField(
        upload_to='avatar/',
        processors=[processors.Transpose()],  # transpose - to fix the 90˚ rotation issue
        format='WEBP',
        options={'quality': 60},
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    
    @property
    def full_name(self):
        first_name = self.first_name if self.first_name else ''
        last_name = self.last_name if self.last_name else ''
        middle_name = self.middle_name if self.middle_name else ''
        full_name = f"{last_name} {first_name} {middle_name}".strip()
        return full_name if len(full_name) > 0 else _('Данные не заполнены!')

    objects = UserManager()
    
    def __str__(self):
        return self.email

    class Meta:
        # todo: delete?
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
