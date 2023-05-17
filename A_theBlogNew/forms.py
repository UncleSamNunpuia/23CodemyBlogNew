from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # these fields are from models.py ie db col name
        fields = ('post_title', 'author', 'post_content', 'image')
        widgets = {
            # lhs is the 'name' attr in the html
            'post_title': forms.TextInput(attrs={'class': 'container form-control'}),
            'author': forms.Select(attrs={'class': 'container form-select'}),
            'post_content': forms.Textarea(attrs={'class': 'container form-control f1'}),
            'image': forms.FileInput(attrs={'class': 'container form-control'})
        }
    # using this we change the display label for the fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].label = 'Writer'
        self.fields['post_title'].label = 'Thuziak Thupui'
        self.fields['post_content'].label = 'Post Content'
        self.fields['image'].label = 'Image Card'
