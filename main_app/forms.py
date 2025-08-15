from django import forms 
from .models import Category, Issue

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', ]

class IssueReportingForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control text-center',
        'placeholder': 'Enter your issue title',
    }))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
            'class': 'form-control text-center',
        }),
        empty_label=" -- -Select Issue's Category- -- "
    )
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Product Description',
        'rows': 3
    }))

    class Meta:
        model = Issue
        fields = ['title', 'description', 'category']


class IssueUpdateForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'status', 'category', 'reported_by']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Disable all fields except 'status'
        for field_name in self.fields:
            if field_name != 'status':
                self.fields[field_name].disabled = True
