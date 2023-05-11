from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # these fields are from models.py ie db col name
        fields = ('post_title', 'author', 'post_content', 'image')
        widgets = {
            # lhs is the 'name' attr in the html
            'post_title': forms.TextInput(attrs={'class': 'container'}),
            'author': forms.Select(attrs={'class': 'container'}),
            'contentaVaMak': forms.Textarea(attrs={'class': 'container'})
        }
    # using this we change the display label for the fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].label = 'Writer'
        self.fields['post_title'].label = 'Post Title'
        self.fields['post_content'].label = 'Post Body'
