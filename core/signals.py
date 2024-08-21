from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserResult
import pandas as pd


@receiver(post_save, sender=UserResult)
def create_exel_entry(sender,instance,created,**kwargs):
    if created:
        data={
            'id':instance.id,
            'وصعیت تأهل':instance.martial_status,
            'محل سکونت/استان':instance.province,
            'محل سکونت/شهر':instance.city,
            'تحصیلات':instance.degree,
            'شغل پیش از شروع خدمت':instance.job,
            'وزن':instance.weight,
            'قد':instance.height,
            'مدت زمان سپری شده از خدمت':instance.time_goes,
            'آیا سیگار مصرف میکنید؟':instance.smoke,
            'وضعیت خواب':instance.sleep,
            'سابقه ی درد های عضلانی استخوانی':instance.history_skeleton_pain,
            'سابقه جراحی ستون فقرات':instance.spain_surgery,
            'سابقه ی فامیلی درد های عضلانی':instance.pain_family,
            'آیا کمر درد به دنبال ضربه ایجاد شده است؟':instance.back_pain_after_impact,
            'چند روز از شروع درد میگذرد؟':instance.back_pain,
            'نمره به شدت درد':instance.pain_intensity_score,
            'pain_waist':instance.pain_waist,
            'odi':instance.odi,
            'disability_level':instance.disability_level,
            'افسردگی':instance.depression,
            'اضطراب':instance.anxiety,
            'استرس':instance.stress,
        }
        df = pd.DataFrame([data])
        try:
            existing_df = pd.read_excel('user_db.xlsx')
            existing_df = pd.concat([existing_df,df], ignore_index=True)
        except FileNotFoundError:
            existing_df = df

        existing_df.to_excel('user_db.xlsx',index=False)