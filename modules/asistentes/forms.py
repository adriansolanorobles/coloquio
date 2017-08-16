from django import forms
from django.forms import ModelForm
from .models import Asistentes

class AsistentesForm(ModelForm):
    class Meta:
        model = Asistentes
        fields = ('nombre','apellido_paterno','apellido_materno','correo','sexo','edad','celular','trabajas_en_educacion','institucion_de_procedencia','preescolar','primaria','secundaria','media_superior','superior','posgrado','no_formal','ocupacion','nombramiento','taller','te_gustaria_recibir_informacion','deseas_asistir_a_los_talleres')
        widgets = {
            'nombre': forms.TextInput(attrs=
                    {
                        "class": "form-control",                        
                        "placeholder":"Ej. Jorge Luis",
                    }
            ),
            'apellido_paterno': forms.TextInput(attrs=
                    {
                        'class': 'form-control',                        
                        "placeholder":"Ej. Martínez",
                    }
            ),
            'apellido_materno': forms.TextInput(attrs=
                    {
                        'class': 'form-control',
                        "placeholder":"Ej. Rodríguez",
                    }
            ),
            'correo': forms.EmailInput(attrs=
                    {
                        'class': 'form-control',
                        "placeholder":"Ej. jorge@micorreo.com",

                    }
            ),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs=
                    {
                        'class': 'form-control',
                        "placeholder":"Ej. 32",

                    }
            ),
            'celular': forms.TextInput(attrs=
                    {
                        'class': 'form-control',
                        "placeholder":"Ej. 5554630876",

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
                        "placeholder":"Ej. Instituto Politécnico Nacional",

                    }
            ),

            'ocupacion': forms.TextInput(attrs=
                    {
                        'class': 'form-control',
                        "placeholder":"Ej. Consultor",

                    }
            ),
            'nombramiento': forms.TextInput(attrs=
                    {
                        'class': 'form-control',
                        "placeholder":"Ej. Dr.",

                    }
            ),
            'taller': forms.Select(attrs={'class': 'form-control'}),

            'te_gustaria_recibir_informacion': forms.CheckboxInput(),
            
            'deseas_asistir_a_los_talleres': forms.Select(attrs=
                {
                    'class': 'form-control'
                }
            ),

        }