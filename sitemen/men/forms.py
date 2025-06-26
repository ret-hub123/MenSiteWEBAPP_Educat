from django import forms
from .models import Category, Men


class AddPostMen(forms.ModelForm):
    cat = forms.ModelChoiceField(Category.objects.all(), empty_label="Выберите категорию", widget=
                                 forms.Select(attrs={'class': 'form-input-cat'}), label="Категория")
    photo = forms.ImageField( label="Прикрепить фото",widget=
                             forms.FileInput(attrs={'class': 'form-input-photo'}))

    class Meta:
        model = Men
        fields = ['title', 'slug', 'content', 'is_publish', 'photo', 'cat']
        labels = {
            'title': "Заголовок",
            'content': "Контент",
            'is_publish': "Опубликовать? -  ",

        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'class': 'form-input-area'}),
            'is_publish': forms.CheckboxInput(attrs={'class': 'form-input'}),

        }



