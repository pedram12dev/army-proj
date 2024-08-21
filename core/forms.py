from django import forms
from .models import UserQuiz, PageTwo, PageThree
from .models import Province, City


class UserQuizForm(forms.Form):
    # CHOICES = [
    #     ('Y', 'بله'),
    #     ('N', 'خیر'),
    # ]
    martial_status = forms.CharField(widget=forms.Select,required=False)
    smoke = forms.CharField(widget=forms.RadioSelect,required=False)
    pain_sckelete = forms.CharField(widget=forms.RadioSelect,required=False)
    pain_family_waist = forms.CharField(widget=forms.RadioSelect,required=False)
    spain_sargery = forms.CharField(widget=forms.RadioSelect,required=False)
    back_pain_after_impact = forms.CharField(widget=forms.RadioSelect,required=False)
    back_pain = forms.CharField(required=False)
    pain_sckelete_number = forms.CharField(required=False)

    # class Meta:
    #     model = UserQuiz
    #     fields = (
    #         'martial_status', 'smoke', 'pain_sckelete', 'pain_family_waist', 'spain_sargery', 'back_pain_after_impact',
    #         'back_pain')


class PageTwoForm(forms.ModelForm):
    # province = forms.ModelChoiceField(queryset=Province.objects.all(), to_field_name='name',empty_label="لطفا استان خود را نتخاب کنید")
    # city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name='name',empty_label="لطفا شهر خود را نتخاب کنید")
    # city = forms.CharField(widget=forms.Select)
    # tahsilat = forms.ChoiceField(choices=PageTwo.Tahsilat)
    # weight = forms.CharField()
    # height = forms.CharField()
    # job = forms.CharField()
    # time_goes = forms.CharField()
    # sleep = forms.ChoiceField(choices=PageTwo.AmountOfSleepChoices)

    class Meta:
        model = PageTwo
        fields = ('province','city','tahsilat','weight','height','time_goes','job','sleep')
        widgets ={
            'province': forms.Select(attrs={'class':'select-options'}),
            'city': forms.Select(attrs={'class':'select-options'}),
            'tahsilat': forms.Select(attrs={'class':'select-options'}),
            'sleep': forms.Select(attrs={'class':'select-options'}),
            'job': forms.TextInput(attrs={'class':'input-page2','placeholder':'ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ  شغل'}),
            'time_goes': forms.TextInput(attrs={'class':'input-page2','placeholder':'ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ  عدد'}),

        }

class PageThreeForm(forms.ModelForm):


    class Meta:
        model = PageThree
        fields = ('pain_waist',)
        widgets ={
            'pain_waist': forms.Select(attrs={'class':'select-options-pageThree'})
        }


class PageFourForm(forms.Form):
    answer = forms.CharField(widget=forms.RadioSelect,required=False)

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['answer'].initial = 0


class PageFiveForm(forms.Form):
    answer_1 = forms.CharField(widget=forms.RadioSelect)
    answer_2 = forms.CharField(widget=forms.RadioSelect)

class PageSixForm(forms.Form):
    answer_1 = forms.CharField(widget=forms.RadioSelect)
    answer_2 = forms.CharField(widget=forms.RadioSelect)


class PageSevenForm(forms.Form):
    answer_1 = forms.CharField(widget=forms.RadioSelect)
    answer_2 = forms.CharField(widget=forms.RadioSelect)


class PageEightForm(forms.Form):
    answer_1 = forms.CharField(widget=forms.RadioSelect)
    answer_2 = forms.CharField(widget=forms.RadioSelect)


class PageNineForm(forms.Form):
    answer_1 = forms.CharField(widget=forms.RadioSelect)

class PageTenForm(forms.Form):
    answer_1 = forms.CharField(widget=forms.RadioSelect)
    answer_2 = forms.CharField(widget=forms.RadioSelect)
    answer_3 = forms.CharField(widget=forms.RadioSelect)
    answer_4 = forms.CharField(widget=forms.RadioSelect)
    answer_5 = forms.CharField(widget=forms.RadioSelect)


class PageElevenForm(forms.Form):
    answer_1 = forms.CharField(widget=forms.RadioSelect)
    answer_2 = forms.CharField(widget=forms.RadioSelect)
    answer_3 = forms.CharField(widget=forms.RadioSelect)
    answer_4 = forms.CharField(widget=forms.RadioSelect)
    answer_5 = forms.CharField(widget=forms.RadioSelect)
    answer_6 = forms.CharField(widget=forms.RadioSelect)


class PageTwelveForm(forms.Form):
    answer_1 = forms.CharField(widget=forms.RadioSelect)
    answer_2 = forms.CharField(widget=forms.RadioSelect)
    answer_3 = forms.CharField(widget=forms.RadioSelect)
    answer_4 = forms.CharField(widget=forms.RadioSelect)
    answer_5 = forms.CharField(widget=forms.RadioSelect)
    answer_6 = forms.CharField(widget=forms.RadioSelect)


class PageThirteenForm(forms.Form):
    answer_1 = forms.CharField(widget=forms.RadioSelect)
    answer_2 = forms.CharField(widget=forms.RadioSelect)
    answer_3 = forms.CharField(widget=forms.RadioSelect)
    answer_4 = forms.CharField(widget=forms.RadioSelect)
