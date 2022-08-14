from django import forms


class sign_up_form(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(max_length=254, label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label='Confirm Password')

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     confirm_password = cleaned_data.get('confirm_password')

    #     if password != confirm_password:
    #         raise forms.ValidationError('Password does not match')
    #     return cleaned_data


class log_in_form(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class adding_project_form(forms.Form):
    title = forms.CharField(max_length=200, label='Title')
    description = forms.CharField(label='Description', widget=forms.Textarea)
    image = forms.URLField(label='Image Link')
    Projectlink = forms.URLField(label='Project Link')
    ProjectPageExists = forms.BooleanField(
        label='Project Page Exists', required=False)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     confirm_password = cleaned_data.get('confirm_password')

    #     if password != confirm_password:
    #         raise forms.ValidationError('Password does not match')
    #     return cleaned_data
