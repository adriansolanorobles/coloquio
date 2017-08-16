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
	DAT_CHOICES = (
        ('Si', 'Si'),
        ('No', 'No'),
	)
	TALLERES_CHOICES = (
        ('t1', 'Taller 1: El entrenamiento de la Atención Plena para el manejo del estrés. [Turno matutino]'),
        ('t2', 'Taller 2: El entrenamiento de la Atención Plena para el manejo del estrés. [Turno vespertino]'),
        ('t3', 'Taller 3: Conectar desde la igualdad. Género y Mindfulness.'),
        ('t4', 'Taller 4: Prácticas contemplativas para la consciencia plena.'),
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
	preescolar = models.NullBooleanField(default=False)
	primaria = models.NullBooleanField(default=False)
	secundaria = models.NullBooleanField(default=False)
	media_superior = models.NullBooleanField(default=False)
	superior = models.NullBooleanField(default=False)
	posgrado = models.NullBooleanField(default=False)
	no_formal = models.NullBooleanField(default=False)
	ocupacion = models.CharField(max_length=255,blank=True,null=True)
	nombramiento = models.CharField(max_length=255,blank=True,null=True)
	taller = models.CharField(max_length=255, choices=TALLERES_CHOICES)
	te_gustaria_recibir_informacion = models.BooleanField()
	deseas_asistir_a_los_talleres = models.CharField(max_length=2,choices=DAT_CHOICES,blank=True,null=True)
	ceated = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.nombre + self.apellido_paterno