from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserResultFinal
import pandas as pd


@receiver(post_save, sender=UserResultFinal)
def create_exel_user_result_final(sender, instance, created, **kwargs):
    if created:
        result = instance.percentage
        result_final = str(result).replace('[','').replace(']','').replace(',','').split(' ')
        chronic = int(float(result_final[1]) *100)
        if chronic >= 71:
            instance.prediction = "chronic"
        else:
            instance.prediction = "acute"
        data = {
            'id': instance.id,
            'age': instance.age,
            'martial_status': instance.martial_status,
            'province': instance.province,
            'city': instance.city,
            'degree': instance.degree,
            'job': instance.job,
            'weight': instance.weight,
            'height': instance.height,
            'time_goes': instance.time_goes,
            'smoke': instance.smoke,
            'sleep': instance.sleep,
            'history_skeleton_pain': instance.history_skeleton_pain,
            'spain_surgery': instance.spain_surgery,
            'pain_family': instance.pain_family,
            'back_pain_after_impact': instance.back_pain_after_impact,
            'back_pain': instance.back_pain,
            'pain_waist': instance.pain_waist,
            'odi': instance.odi,
            'disability_level': instance.disability_level,
            'depression': instance.depression,
            'anxiety': instance.anxiety,
            'stress': instance.stress,
            'prediction': instance.prediction,
            'percentage': chronic,
        }
        df = pd.DataFrame([data])
        try:
            existing_df = pd.read_excel('final_result.xlsx')
            existing_df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            existing_df = df

        existing_df.to_excel('final_result.xlsx', index=False)