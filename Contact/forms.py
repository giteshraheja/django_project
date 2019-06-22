from django import forms


class Contact_form(forms.Form):
    Name = forms.CharField(max_length=15, label='Name:',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}))
    Email_Id = forms.EmailField(label="Email Id:", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email-Id'}))
    yourmessage = forms.CharField(label='Your Message', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter Message'}))
