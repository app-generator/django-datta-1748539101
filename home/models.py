# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Parcelas(models.Model):

    #__Parcelas_FIELDS__
    nc = models.TextField(max_length=255, null=True, blank=True)
    titular = models.TextField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)

    #__Parcelas_FIELDS__END

    class Meta:
        verbose_name        = _("Parcelas")
        verbose_name_plural = _("Parcelas")


class Reporte(models.Model):

    #__Reporte_FIELDS__
    titulo = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.TextField(max_length=255, null=True, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True, default=timezone.now)
    estado = models.CharField(max_length=255, null=True, blank=True)
    parcelas = models.ForeignKey(Parcelas, on_delete=models.CASCADE)

    #__Reporte_FIELDS__END

    class Meta:
        verbose_name        = _("Reporte")
        verbose_name_plural = _("Reporte")


class Concepto(models.Model):

    #__Concepto_FIELDS__
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE)
    parcela = models.ForeignKey(Parcelas, on_delete=models.CASCADE)
    unidades = models.IntegerField(null=True, blank=True)
    pozos = models.IntegerField(null=True, blank=True)
    instmenor = models.IntegerField(null=True, blank=True)
    instmayor = models.IntegerField(null=True, blank=True)
    instespecial = models.IntegerField(null=True, blank=True)

    #__Concepto_FIELDS__END

    class Meta:
        verbose_name        = _("Concepto")
        verbose_name_plural = _("Concepto")



#__MODELS__END
