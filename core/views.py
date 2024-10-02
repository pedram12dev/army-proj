from django.shortcuts import render, redirect
from django.views import View
from .forms import (
    UserQuizForm, PageTwoForm, PageThreeForm, PageFourForm, PageFiveForm, PageSixForm, PageSevenForm, PageEightForm,
    PageNineForm, PageTenForm, PageElevenForm, PageTwelveForm, PageThirteenForm
)
from utils import *
import json
from .disability import determine_disability_level, determine_stress_level, determine_anxiety_level, \
    determine_depression_level
from .models import UserResult,UserResultFinal
from django.http import FileResponse
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
import warnings
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pickle
# from .ai_data import data_result

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

    # def post(self):
    #     return redirect('core:page_one')


class PageOneView(View):
    form_class = UserQuizForm

    def get(self, request):
        form = self.form_class
        return render(request, 'page_one.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            request.session['page_one'] = {
                'age': cd['age'],
                'martial_status': cd['martial_status'],
                'smoke': cd['smoke'],
                'pain_family_waist': cd['pain_family_waist'],
                'spain_sargery': cd['spain_sargery'],
                'back_pain_after_impact': cd['back_pain_after_impact'],
                'back_pain': cd['back_pain'],
                'pain_sckelete_number': cd['pain_sckelete_number'],
                'pain_sckelete': cd['pain_sckelete']
            }
            print(request.session['page_one'])
            return redirect('core:page_two')
        return render(request, 'page_one.html')


class PageTwoView(View):
    form_class = PageTwoForm

    def get(self, request):
        form = self.form_class
        return render(request, 'page_two.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # print(cd)
            # value = cd['province'], cd['city'], cd['tahsilat'], cd['weight'], cd[
            #     'height'],cd['time_goes'], cd['job'], cd['sleep']
            for value in cd['province']:
                province = value

            for value in cd['city']:
                city = value

            request.session['page_two'] = {
                'tahsilat': cd['tahsilat'],
                'weight': cd['weight'],
                'height': cd['height'],
                'time_goes': cd['time_goes'],
                'job': cd['job'],
                'sleep': cd['sleep'],
                'province': province,
                'city': city
            }

            print(request.session['page_two'])
            return redirect('core:page_three')
        return render(request, 'page_two.html', {'form': form})


class PageThreeView(View):
    form_class = PageThreeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'page_three.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for key in labels_page_three:
                if key == cd['pain_waist']:
                    k = int(key)

            request.session['page_three'] = {
                'key': k
            }
            print(request.session['page_three'])
            return redirect('core:page_four')
        return render(request, 'page_three.html', {'form': form})


class PageFourView(View):
    form_class = PageFourForm

    def get(self, request):
        form = self.form_class
        return render(request, 'page_four.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for key, value in labels_page_four.items():
                if key == cd['answer']:
                    k = int(key)
                    val = value
            result = k
            request.session['page_four'] = {
                'key': result,
                'answer_str': val,
                'result': result
            }

            # init_number = form.answer +1
            # print(init_number)
            print(request.session['page_four'])
            return redirect('core:page_five')
        return render(request, 'page_four.html', {'form': form})


class PageFiveView(View):
    form_class = PageFiveForm

    def get(self, request):
        form = self.form_class
        return render(request, 'page_five.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for key, value in labels_page_five.items():
                if key == cd['answer_1']:
                    k = int(key)
                    val = value

            for key, value in labels_page_five_2.items():
                if key == cd['answer_2']:
                    k_2 = int(key)
                    val_2 = value

            result = request.session['page_four']
            oswestry = k + k_2 + result['key']
            print(oswestry)
            print(result)
            request.session['page_five'] = {
                'oswestry_1': oswestry,
                'answer_str_1': val,
                'answer_str_2': val_2,
                'result': result,
            }

            print(request.session['page_five'])
            return redirect('core:page_six')
        return render(request, 'page_five.html', {'form': form})


class PageSixView(View):
    form_class = PageSixForm

    def get(self, request):
        form = self.form_class
        return render(request, 'page_six.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for key, value in labels_page_six.items():
                if key == cd['answer_1']:
                    k = int(key)
                    val = value

            for key, value in labels_page_six_2.items():
                if key == cd['answer_2']:
                    k_2 = int(key)
                    val_2 = value

            result = request.session['page_five']
            oswestry = k + k_2 + result['oswestry_1']
            print(oswestry)

            request.session['page_six'] = {
                'oswestry_2': oswestry,
                'key_2': k_2,
                'answer_str_1': val,
                'answer_str_2': val_2,

            }
            print(request.session['page_six'])
            return redirect('core:page_seven')
        return render(request, 'page_six.html', {'form': form})


class PageSevenView(View):
    form_class = PageSevenForm

    def get(self, request):
        form = self.form_class
        return render(request, 'page_seven.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for key, value in labels_page_seven.items():
                if key == cd['answer_1']:
                    k = int(key)
                    val = value

            for key, value in labels_page_seven_2.items():
                if key == cd['answer_2']:
                    k_2 = int(key)
                    val_2 = value
            result = request.session['page_six']
            oswestry = k + k_2 + result['oswestry_2']
            print(oswestry)
            request.session['page_seven'] = {
                'oswestry_3': oswestry,
                'key_2': k_2,
                'answer_str_1': val,
                'answer_str_2': val_2,

            }
            print(request.session['page_seven'])
            return redirect('core:page_eight')
        return render(request, 'page_seven.html', {'form': form})


class PageEightView(View):
    form_class = PageEightForm

    def get(self, request):
        form = self.form_class
        return render(request, 'page_eight.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for key, value in labels_page_eight.items():
                if key == cd['answer_1']:
                    k = int(key)
                    val = value

            for key, value in labels_page_eight_2.items():
                if key == cd['answer_2']:
                    k_2 = int(key)
                    val_2 = value

            result = request.session['page_seven']
            oswestry = k + k_2 + result['oswestry_3']
            print(oswestry)
            request.session['page_eight'] = {
                'oswestry_4': oswestry,
                'key_2': k_2,
                'answer_str_1': val,
                'answer_str_2': val_2,

            }
            print(request.session['page_eight'])
            return redirect('core:page_nine')
        return render(request, 'page_eight.html', {'form': form})


class PageNineView(View):
    form_class = PageNineForm

    def get(self, request):
        form = self.form_class
        return render(request, 'page_nine.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for key, value in labels_page_nine.items():
                if key == cd['answer_1']:
                    k = int(key)
                    val = value

            result = request.session['page_eight']
            score = k + result['oswestry_4']
            print(score)
            final_result = determine_disability_level(score)
            print(final_result)
            request.session['page_nine'] = {
                'oswestry_result': final_result,
                'score_result': score,

            }
            print(request.session['page_nine'])
            return redirect('core:page_ten')
        return render(request, 'page_nine.html', {'form': form})


class PageTenView(View):
    form_class = PageTenForm

    def get(self, request):
        form = self.form_class
        return render(request, 'page_ten.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for key in labels_for_page_answer_1:
                if key == cd['answer_1']:
                    k_1 = int(key)
            for key in labels_for_page_answer_2:
                if key == cd['answer_2']:
                    k_2 = int(key)
            for key in labels_for_page_answer_3:
                if key == cd['answer_3']:
                    k_3 = int(key)
            for key in labels_for_page_answer_4:
                if key == cd['answer_4']:
                    k_4 = int(key)
            for key in labels_for_page_answer_5:
                if key == cd['answer_5']:
                    k_5 = int(key)
            stress_result = k_3 + k_5
            anxiety_result = k_2 + k_4
            depression_result = k_1
            request.session['page_ten'] = {
                'stress_1': stress_result,
                'anxiety_1': anxiety_result,
                'depression_1': depression_result
            }
            print(request.session['page_ten'])
            return redirect('core:page_eleven')
        return render(request, 'page_ten.html', {'form': form})


class PageElevenView(View):
    form_class = PageElevenForm

    def get(self, request):
        form = self.form_class
        return render(request, 'page_eleven.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for key in labels_for_page_answer_1:
                if key == cd['answer_1']:
                    k_1 = int(key)
            for key in labels_for_page_answer_2:
                if key == cd['answer_2']:
                    k_2 = int(key)
            for key in labels_for_page_answer_3:
                if key == cd['answer_3']:
                    k_3 = int(key)
            for key in labels_for_page_answer_4:
                if key == cd['answer_4']:
                    k_4 = int(key)
            for key in labels_for_page_answer_5:
                if key == cd['answer_5']:
                    k_5 = int(key)
            for key in labels_for_page_answer_6:
                if key == cd['answer_6']:
                    k_6 = int(key)

            result = request.session['page_ten']
            stress_result = k_5 + result['stress_1']
            anxiety_result = k_2 + k_4 + result['anxiety_1']
            depression_result = k_1 + k_3 + k_6 + result['depression_1']
            request.session['page_eleven'] = {
                'stress_2': stress_result,
                'anxiety_2': anxiety_result,
                'depression_2': depression_result
            }
            print(request.session['page_eleven'])
            return redirect('core:page_twelve')
        return render(request, 'page_eleven.html', {'form': form})


class PageTwelveView(View):
    form_class = PageTwelveForm

    def get(self, request):
        form = self.form_class
        return render(request, 'page_twelve.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for key in labels_for_page_answer_1:
                if key == cd['answer_1']:
                    k_1 = int(key)
            for key in labels_for_page_answer_2:
                if key == cd['answer_2']:
                    k_2 = int(key)
            for key in labels_for_page_answer_3:
                if key == cd['answer_3']:
                    k_3 = int(key)
            for key in labels_for_page_answer_4:
                if key == cd['answer_4']:
                    k_4 = int(key)
            for key in labels_for_page_answer_5:
                if key == cd['answer_5']:
                    k_5 = int(key)
            for key in labels_for_page_answer_6:
                if key == cd['answer_6']:
                    k_6 = int(key)

            result = request.session['page_eleven']
            stress_result = k_2 + k_5 + k_6 + result['stress_2']
            anxiety_result = k_4 + result['anxiety_2']
            depression_result = k_1 + k_3 + result['depression_2']
            request.session['page_twelve'] = {
                'stress_3': stress_result,
                'anxiety_3': anxiety_result,
                'depression_3': depression_result
            }
            print(request.session['page_twelve'])
            return redirect('core:page_thirteen')
        return render(request, 'page_twelve.html', {'form': form})


class PageThirteenView(View):
    form_class = PageThirteenForm

    def get(self, request):
        form = self.form_class
        return render(request, 'page_thirteen.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for key in labels_for_page_answer_1:
                if key == cd['answer_1']:
                    k_1 = int(key)
            for key in labels_for_page_answer_2:
                if key == cd['answer_2']:
                    k_2 = int(key)
            for key in labels_for_page_answer_3:
                if key == cd['answer_3']:
                    k_3 = int(key)
            for key in labels_for_page_answer_4:
                if key == cd['answer_4']:
                    k_4 = int(key)

            result = request.session['page_twelve']

            stress_result = k_4 + result['stress_3']
            anxiety_result = k_2 + k_3 + result['anxiety_3']
            depression_result = k_1 + result['depression_3']

            finally_stress_result = determine_stress_level(stress_result)
            finally_anxiety_result = determine_anxiety_level(anxiety_result)
            finally_depression_result = determine_depression_level(depression_result)
            request.session['page_thirteen'] = {
                'stress_4': stress_result,
                'anxiety_4': anxiety_result,
                'depression_4': depression_result,
                'final_stress_result': finally_stress_result,
                'final_anxiety_result': finally_anxiety_result,
                'final_depression_result': finally_depression_result,
            }
            page_one_session = request.session['page_one']
            page_two_session = request.session['page_two']
            page_three_session = request.session['page_three']
            page_nine_session = request.session['page_nine']
            page_thirteen_session = request.session['page_thirteen']
            data_record = {
                'age': [page_one_session['age'],page_one_session['age']],
                'marital': [page_one_session['martial_status'],page_one_session['martial_status']],
                'educate': [page_two_session['tahsilat'],page_two_session['tahsilat']],
                'job':[page_two_session['job'],page_two_session['job']],
                'weight':[page_two_session['weight'],page_two_session['weight']],
                'height': [page_two_session['height'],page_two_session['height']],
                'time_military': [page_two_session['time_goes'],page_two_session['time_goes']],
                'smoke': [page_one_session['smoke'],page_one_session['smoke']],
                'sleep_state': [page_two_session['sleep'],page_two_session['sleep']],
                'eskelete_pain':[page_one_session['pain_sckelete'],page_one_session['pain_sckelete']],
                'operate':[page_one_session['spain_sargery'],page_one_session['spain_sargery']],
                'family_pain':[page_one_session['pain_family_waist'],page_one_session['pain_family_waist']],
                'backpain_bit':[page_one_session['back_pain_after_impact'],page_one_session['back_pain_after_impact']],
                'back_pain_time':[page_one_session['back_pain'],page_one_session['back_pain']],
                'pain_waste':[page_three_session['key'],page_three_session['key']],
                'ODI':[page_nine_session['score_result'],page_nine_session['score_result']],
                'Disability Level': [page_nine_session['oswestry_result'],page_nine_session['oswestry_result']],
                'depression':[page_thirteen_session['final_depression_result'],page_thirteen_session['final_depression_result']],
                'anxiety':[page_thirteen_session['final_anxiety_result'],page_thirteen_session['final_anxiety_result']],
                'stress': [page_thirteen_session['final_stress_result'],page_thirteen_session['final_stress_result']],
            }
            
            df = pd.DataFrame.from_dict(data_record)
            
            

            df.drop('age' , axis=1, inplace=True)
            
            
            
            
            class DataPreprocessor:
                def init(self):
                    self.scaler = MinMaxScaler()
                    self.encoder = OneHotEncoder(handle_unknown='ignore')
                    self.column_transformer = None
            
                def fit(self, X, save_path='preprocessor.joblib'):
                    # Ensure all categorical columns are of type string
                    categorical_cols = X.select_dtypes(include=['object']).columns
                    for col in categorical_cols:
                        X[col] = X[col].astype(str)
            
                    # Identify numerical columns
                    numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
            
                    # Create a column transformer for preprocessing
                    self.column_transformer = ColumnTransformer(
                        transformers=[
                            ('num', self.scaler, numerical_cols),
                            ('cat', self.encoder, categorical_cols)
                        ]
                    )
            
                    # Fit the column transformer
                    self.column_transformer.fit(X)
            
                    # Save the fitted preprocessor
                    joblib.dump(self.column_transformer, save_path)
            
                def transform(self, X):
                    # Ensure all categorical columns are of type string
                    categorical_cols = X.select_dtypes(include=['object']).columns
                    for col in categorical_cols:
                        X[col] = X[col].astype(str)
            
                    # Load the saved preprocessor
                    self.column_transformer = joblib.load('preprocessor.joblib')
            
                    return self.column_transformer.transform(X)
            
                def fit_transform(self, X, save_path='preprocessor.joblib'):
                    self.fit(X, save_path)
                    return self.transform(X)
            
                def load(self, save_path='preprocessor.joblib'):
                    self.column_transformer = joblib.load(save_path)
                    
            df[df.select_dtypes(include=['int']).columns] = df.select_dtypes(include=['int']).astype('float64')
            
            temp = df.copy()
            temp = df.tail(1)
          
            # Initialize and fit the preprocessor
            preprocessor = DataPreprocessor()
            X_train = preprocessor.transform(temp)

            
            t = X_train[-1].reshape(1 , -1)
            # Load the model from the file
            with open('random_forest_model.pkl', 'rb') as file:
                loaded_model = pickle.load(file)
            
            predictions = loaded_model.predict_proba(t)
            
            data_result = predictions
            request.session['page_final'] = {
                'data_result': data_result.tolist(),
                }
            
            UserResult.objects.create(
                age = page_one_session['age'],
                martial_status=page_one_session['martial_status'],
                province=page_two_session['province'],
                city=page_two_session['city'],
                degree=page_two_session['tahsilat'],
                job=page_two_session['job'],
                weight=page_two_session['weight'],
                height=page_two_session['height'],
                time_goes=page_two_session['time_goes'],
                smoke=page_one_session['smoke'],
                sleep=page_two_session['sleep'],
                history_skeleton_pain=page_one_session['pain_sckelete'],
                spain_surgery=page_one_session['spain_sargery'],
                pain_family=page_one_session['pain_family_waist'],
                back_pain_after_impact=page_one_session['back_pain_after_impact'],
                back_pain=page_one_session['back_pain'],
                pain_waist=page_three_session['key'],
                odi=page_nine_session['score_result'],
                disability_level=page_nine_session['oswestry_result'],
                depression=page_thirteen_session['final_depression_result'],
                anxiety=page_thirteen_session['final_anxiety_result'],
                stress=page_thirteen_session['final_stress_result'],
                chronic = data_result,
            )
            
            return redirect('core:page_fourteen')
        return render(request, 'page_thirteen.html', {'form': form})


class PageFourteenView(View):

    def get(self, request):
        return render(request, 'page_fourteen.html')

    def post(self, request):
        page_one_session = request.session['page_one']
        page_two_session = request.session['page_two']
        page_three_session = request.session['page_three']
        page_nine_session = request.session['page_nine']
        page_thirteen_session = request.session['page_thirteen']
        data_result = request.session['page_final']
        data_result = data_result['data_result']
        
        
        if request.method == 'POST':
            UserResultFinal.objects.create(
                age=page_one_session['age'],
                martial_status=page_one_session['martial_status'],
                province=page_two_session['province'],
                city=page_two_session['city'],
                degree=page_two_session['tahsilat'],
                job=page_two_session['job'],
                weight=page_two_session['weight'],
                height=page_two_session['height'],
                time_goes=page_two_session['time_goes'],
                smoke=page_one_session['smoke'],
                sleep=page_two_session['sleep'],
                history_skeleton_pain=page_one_session['pain_sckelete'],
                spain_surgery=page_one_session['spain_sargery'],
                pain_family=page_one_session['pain_family_waist'],
                back_pain_after_impact=page_one_session['back_pain_after_impact'],
                back_pain=page_one_session['back_pain'],
                pain_waist=page_three_session['key'],
                odi=page_nine_session['score_result'],
                disability_level=page_nine_session['oswestry_result'],
                depression=page_thirteen_session['final_depression_result'],
                anxiety=page_thirteen_session['final_anxiety_result'],
                stress=page_thirteen_session['final_stress_result'],
                percentage=data_result,
            )
            del request.session['page_one']
            del request.session['page_two']
            del request.session['page_three']
            del request.session['page_nine']
            del request.session['page_thirteen']
            
            return redirect('core:page_fifteen')
        return render(request, 'page_fourteen.html')


class PageFifteenView(View):
    form_class = ...

    def get(self, request):
        chronic = UserResultFinal.objects.last()
        value = chronic.percentage
        data= value.replace('[', '').replace(']','').replace(',','').split(' ')
        # had = int(float(data[1]) *100)
        mozmen = int(float(data[1]) *100)
        result =""
        if mozmen >= 71:
            result = " کمر درد شما در آینده مزمن خواهد شد"
        else:
            result =  'شما به کمر درد حاد مبتلا شده اید '
        
        return render(request, 'page_fifteen.html', {'result':result})

    def post(self, request):
        if request.method == 'POST':
            return redirect('core:page_sixteen')
        return render(request, 'page_fifteen.html')


class PageSixteenView(View):

    def get(self, request):
        return render(request, 'page_sixteen.html')

    def post(self, request):
        pass


class AdminDataView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'admin_page.html')

    def post(self, request):
        if request.method == 'POST':
            return redirect('core:download_data')


def download_file(request, file_name):
    file_path = settings.BASE_DIR / file_name
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = 'attachment; filename="%s"' % file_name
    return response


from django.http import JsonResponse
from .models import City

def get_cities_by_province(province_id):
    cities = City.objects.filter(province_id=province_id)
    return cities
def get_cities(request):
    if request.is_ajax():
        try:
            province_id = int(request.GET.get('province_id'))
            cities = get_cities_by_province(province_id=province_id).order_by('name')
            print(cities)
            return JsonResponse({'cities': list(cities.values('name','id'))})
        except (ValueError, City.DoesNotExist):
            return JsonResponse({'error': 'Invalid province ID'})





