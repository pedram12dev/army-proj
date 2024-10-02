from django import forms
from .models import UserQuiz, PageTwo, PageThree
from .models import Province, City


class UserQuizForm(forms.Form):
    # CHOICES = [
    #     ('Y', 'بله'),
    #     ('N', 'خیر'),
    # ]
    age = forms.CharField()
    martial_status = forms.CharField(widget=forms.Select)
    smoke = forms.CharField(widget=forms.RadioSelect)
    pain_sckelete = forms.CharField(widget=forms.RadioSelect)
    pain_family_waist = forms.CharField(widget=forms.RadioSelect)
    spain_sargery = forms.CharField(widget=forms.RadioSelect)
    back_pain_after_impact = forms.CharField(widget=forms.RadioSelect)
    back_pain = forms.CharField()
    pain_sckelete_number = forms.CharField()

    # class Meta:
    #     model = UserQuiz
    #     fields = (
    #         'martial_status', 'smoke', 'pain_sckelete', 'pain_family_waist', 'spain_sargery', 'back_pain_after_impact',
    #         'back_pain')


class PageTwoForm(forms.ModelForm):


    class Meta:
        model = PageTwo
        fields = ('province','city','tahsilat','weight','height','time_goes','job','sleep')
        widgets ={
            'province': forms.Select(attrs={'class':'select-options'}),
            'city': forms.Select(attrs={'class':'select-options'}),
            'tahsilat': forms.Select(attrs={'class':'select-options'}),
            'sleep': forms.Select(attrs={'class':'select-options'}),
            'job': forms.TextInput(attrs={'class':'input-page2','placeholder':'ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ  شغل'}),
            'time_goes': forms.TextInput(attrs={'class':'input-page2','placeholder':'ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ  روز'}),

        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        if 'province' in self.data:
            try:
                province_id = int(self.data.get('province'))
                self.fields['city'].queryset = City.objects.filter(province_id=province_id).order_by('name')
            except (ValueError, TypeError):
                pass

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
