from django.db import models


class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='product', blank=True)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    image = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class TelegramUserModel(models.Model):
    tg_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tg_id}'

    class Meta:
        verbose_name = 'Telegram user'
        verbose_name_plural = 'Telegram users'


STATUS = (
    ('Kutilmoqda', 'Kutilmoqda'),
    ('Bekor Qilindi', 'Bekor Qilindi'),
    ('Tasdiqlandi', 'Tasdiqlandi'),
    ('Yuborildi', 'Yuborildi'),
    ('Yetkazildi', 'Yetkazildi'),
)


class OrderModel(models.Model):
    user = models.ForeignKey(TelegramUserModel, on_delete=models.CASCADE)
    product = models.TextField()
    price = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True, blank=True)
    number = models.CharField(max_length=15)
    order = models.CharField(max_length=50, choices=STATUS, default='Kutilmoqda')
    kuryer = models.CharField(max_length=255, null=True, blank=True)
    date = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'


class KorzinaModel(models.Model):
    user_id = models.IntegerField()
    product = models.CharField(max_length=255)
    count = models.IntegerField()
    price = models.FloatField()
