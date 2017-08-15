from django.db import models
# Create your models here.

class Asistentes(models.Model):
	GENDER_CHOICES = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )
    TRABAJAS_EN_EDUCACION_CHOICES = (
        ('Si', 'Si'),
        ('No', 'No'),
    )
    NIVEL_CHOICES = (
        ('Pre', 'Preescolar'),
        ('Pri', 'Primaria'),
        ('Sec', 'Secundaria'),
        ('MSu', 'Media Superior'),
        ('Sup', 'Superior'),
        ('Pos', 'Posgrado'),
        ('NoF', 'No formal'),
    )
 	nombre = models.CharField(max_length=255)
 	apellido_paterno = models.CharField(max_length=255)
 	apellido_materno = models.CharField(max_length=255)
 	correo = models.EmailField()
 	sexo = models.CharField(max_length=1,choices=GENDER_CHOICES)
 	edad = models.CharField(max_length=2)
 	celular = models.CharField(max_length=10)
 	trabajas_en_educacion = models.CharField(max_length=2,choices=TRABAJAS_EN_EDUCACION_CHOICES)
 	institucion_de_procedencia = models.CharField(max_length=255,blank=True,null=True)
 	preescolar = models.BooleanField(default=False,blank=True,null=True)
 	primaria = models.BooleanField(default=False,blank=True,null=True)
 	secundaria = models.BooleanField(default=False,blank=True,null=True)
    media_superior = models.BooleanField(default=False,blank=True,null=True)
    superior = models.BooleanField(default=False,blank=True,null=True)
    posgrado = models.BooleanField(default=False,blank=True,null=True)
    no_formal = models.BooleanField(default=False,blank=True,null=True)
    ocupacion = models.CharField(max_length=255,blank=True,null=True)
    nombramiento = models.CharField(max_length=255,blank=True,null=True)
    te_gustaria_recibir_informacion = models.BooleanField()
    ceated = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nombre + self.apellido_paterno