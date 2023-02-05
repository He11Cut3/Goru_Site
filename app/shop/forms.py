from django import forms
from .models import Comment, OrderItem

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['create_at', 'product', 'email']
        widgets = {
            'name': forms.Textarea(attrs={'placeholder': 'Имя'}),
            'message': forms.Textarea(attrs={'placeholder': 'Сообщение'})
        }

class AddQuantityForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']