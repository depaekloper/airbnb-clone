from django import forms


class AddCommnetForm(forms.Form):

    message = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"placeholder": "Add a Commnet"})
    )
