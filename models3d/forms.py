from django import forms
from .models import Model3D

class Model3DForm(forms.ModelForm):
    class Meta:
        model = Model3D
        fields = ['title', 'description', 'category', 'model_file', 'preview_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'model_file': forms.FileInput(attrs={'class': 'form-control'}),
            'preview_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_model_file(self):
        file = self.cleaned_data.get('model_file')
        allowed_types = ['.stl', '.obj', '.fbx', '.glb', '.3mf']
        if file:
            ext = file.name.lower().split('.')[-1]
            if f".{ext}" not in allowed_types:
                raise forms.ValidationError("Разрешени формати са: STL, OBJ, FBX, GLB, 3MF")
        return file
