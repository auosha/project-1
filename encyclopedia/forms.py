from django import forms


class EntryCreateForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(
        widget=forms.Textarea(attrs={'style': 'height:100px'})
    )

class EntryEditForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'style': 'height:100px'})
    )
