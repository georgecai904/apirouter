from django.db import models

class SoraGenStyle(models.Model):
    style = models.CharField(max_length=255, unique=True, verbose_name="风格 (Style)")
    promptA = models.TextField(verbose_name="提示词A (Prompt A)")

    class Meta:
        verbose_name = "SoraGen 风格"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.style

class SoraGenProductSeed(models.Model):
    productSeed = models.CharField(max_length=255, unique=True, verbose_name="产品种子 (Product Seed)")
    promptB = models.TextField(verbose_name="提示词B (Prompt B)")

    class Meta:
        verbose_name = "SoraGen 产品种子"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.productSeed
