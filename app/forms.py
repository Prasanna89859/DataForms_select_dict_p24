from django import forms


g=[['MALE','Male'],['FEMALE','FEMALE']]
A=[['PYTHON','python'],['Django','Djago'],['SQL','SQL'],['API','API']]

class Nameform(forms.Form):
    Sname=forms.CharField()
    Sage=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':00,'rows':00}))
    gender=forms.ChoiceField(choices=g)
    #gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=A)
    #course=forms.MultipleChoiceField(choices=A,widget=forms.CheckboxSelectMultiple)


