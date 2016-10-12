from django import forms

# our new form
class submit(forms.Form):
    pair1 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')], initial = '1' )
    pair2 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')], initial = '1' )
    pair3 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')], initial = '1' )
    pair4 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')], initial = '1'  )
    pair5 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')], initial = '1'  )
    # pair6 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')], initial = '1'  )
    # pair7 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')], initial = '1'  )
    # pair8 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair9 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair10 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair11 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair12 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair13 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair14 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair15 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair16 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair17 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair18 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair19 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair20 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair21 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair9 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair9 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair9 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair9 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')
    # pair9 = forms.ChoiceField(required=True, widget = forms.RadioSelect, choices=[('1','Yes'),('2','No')] , initial = '1')


