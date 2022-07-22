from django import forms
from .models import Book
import os

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=('name','resume','linkedin',) 
    def __init__(self, *args, **kwargs):
        print("well it reached in forms.py")
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['resume'].required = True

    def validate_file_extension(value):
        print("it was here to check extentions") 
        ext = os.path.splitext(value.name)[1]
        valid_extensions = ['.pdf','.doc','.docx']
        if not ext in valid_extensions:
            raise ValidationError(u'File not supported!')
