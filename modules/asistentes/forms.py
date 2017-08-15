from django import forms
from django.forms import ModelForm
from .models import Asistentes

class AsistentesForm(ModelForm):
    class Meta:
        model = Asistentes
        fields = ('nombre','apellido_paterno','apellido_materno','correo','sexo','edad','celular','trabajas_en_educacion','institucion_de_procedencia','preescolar','primaria','secundaria','media_superior','superior','posgrado','no_formal','ocupacion','nombramiento','taller','te_gustaria_recibir_informacion')
        widgets = {
            'nombre': forms.TextInput(attrs=
                    {
                        "class": "form-control",
                        "pattern":"^([a-zA-Z]+(?:\.)?(?:(?:'| )[a-zA-Z]+(?:\.)?)*)$",
                    }
            ),
            'apellido_paterno': forms.TextInput(attrs=
                    {
                        'class': 'form-control',
                        "pattern":"^([a-zA-Z]+(?:\.)?(?:(?:'| )[a-zA-Z]+(?:\.)?)*)$",
                    }
            ),
            'apellido_materno': forms.TextInput(attrs=
                    {
                        'class': 'form-control',
                        "pattern":"^([a-zA-Z]+(?:\.)?(?:(?:'| )[a-zA-Z]+(?:\.)?)*)$",
                    }
            ),
            'correo': forms.EmailInput(attrs=
                    {
                        'class': 'form-control',

                    }
            ),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs=
                    {
                        'class': 'form-control',

                    }
            ),
            'celular': forms.TextInput(attrs=
                    {
                        'class': 'form-control',

                    }
            ),
            'trabajas_en_educacion': forms.Select(attrs={'class': 'form-control'}),
            'preescolar': forms.CheckboxInput(),
            'primaria': forms.CheckboxInput(),
            'secundaria': forms.CheckboxInput(),
            'media_superior': forms.CheckboxInput(),
            'superior': forms.CheckboxInput(),
            'posgrado': forms.CheckboxInput(),
            'no_formal': forms.CheckboxInput(),
            'institucion_de_procedencia': forms.TextInput(attrs=
                    {
                        'class': 'form-control',

                    }
            ),

            'ocupacion': forms.TextInput(attrs=
                    {
                        'class': 'form-control',

                    }
            ),
            'nombramiento': forms.TextInput(attrs=
                    {
                        'class': 'form-control',

                    }
            ),
            'taller': forms.Select(attrs={'class': 'form-control'}),

            'te_gustaria_recibir_informacion': forms.CheckboxInput(),

        }