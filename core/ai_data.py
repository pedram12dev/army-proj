import random
import warnings
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pickle
# from .models import UserResultFinal


# Ignore all warnings
warnings.filterwarnings('ignore')
df = pd.read_excel('user_db.xlsx', engine='openpyxl')

# Renaming columns
df.rename(columns={
    'وصعیت تأهل': 'marital',
    'محل سکونت/استان': 'province',
    'محل سکونت/شهر': 'city',
    'تحصیلات': 'educate',
    'شغل پیش از شروع خدمت': 'job',
    'وزن': 'weight',
    'قد': 'height',
    'مدت زمان سپری شده از خدمت': 'time_military',
    'آیا سیگار مصرف میکنید؟': 'smoke',
    'وضعیت خواب': 'sleep_state',
    'سابقه ی درد های عضلانی استخوانی': 'eskelete_pain',
    'سابقه جراحی ستون فقرات': 'operate',
    'سابقه ی فامیلی درد های عضلانی': 'family_pain',
    'آیا کمر درد به دنبال ضربه ایجاد شده است؟': 'backpain_bit',
    'چند روز از شروع درد میگذرد؟': 'back_pain_time',
    'pain_waist': 'pain_waste',
    'odi': 'ODI',
    'disability_level': 'Disability Level',
    'افسردگی': 'depression',
    'اضطراب': 'anxiety',
    'استرس': 'stress'
}, inplace=True)

# Display the updated DataFrame
print(df.columns)

order = ['marital', 'province', 'city', 'educate', 'job', 'weight', 'height',
         'time_military', 'smoke', 'sleep_state', 'eskelete_pain', 'operate', 'family_pain',
         'backpain_bit', 'back_pain_time', 'pain_waste', 'ODI', 'Disability Level', 'depression', 'anxiety',
         'stress']

print(len(order))
# Sort the DataFrame columns based on the order list
sorted_df = df.reindex(columns=order)

print(sorted_df.shape)
df = sorted_df.copy()
print(df.dtypes)


class DataPreprocessor:
    def __init__(self):
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

temp = df.iloc[: , :]
# print(temp.shape)

# print(df.head())

# Select all integer columns and convert them to float64
df[df.select_dtypes(include=['int']).columns] = df.select_dtypes(include=['int']).astype('float64')

# Display the updated data types
print("Updated Data Types:\n", df.dtypes)
temp = df.tail(1)
# Initialize and fit the preprocessor
preprocessor = DataPreprocessor()
X_train = preprocessor.transform(temp)
print(X_train.shape)
t = X_train[0].reshape(1 , -1)
# Load the model from the file
with open('random_forest_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Use the loaded model to make predictions
predictions = loaded_model.predict(t)
print(predictions)
data_result_str = predictions
predictions = loaded_model.predict_proba(t)
print(predictions[0])

data_result = predictions




