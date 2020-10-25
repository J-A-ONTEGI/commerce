from .models import Bid, Category, Comment, CustomUser, Listing
from django import forms


class AddListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'starting_bid', 'id', 'img_url', 'description','category']
        widgets = {
            'id': forms.HiddenInput(),
            'description': forms.Textarea(attrs={
                'columns': 50,
                'rows': 10
            }),
           }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 1,
                'width': 100
            })
        }


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model: Category
        fields = ['id', 'name', 'parent_id']
        widgets = {
            'id': forms.HiddenInput(),
        }
