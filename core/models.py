from django.db import models



class Province(models.Model):
    name = models.CharField(max_length=56)
    slug = models.SlugField(max_length=56,null=True)
    tel_prefix = models.CharField(max_length=56,null=True)

    def __str__(self):
        return self.name

    def __iter__(self):
        yield self.name


class City(models.Model):
    # province = models.ForeignKey(Province,on_delete=models.CASCADE,related_name='cities',null=True)
    name = models.CharField(max_length=56)
    slug= models.SlugField(max_length=56,null=True)
    province_id = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def __iter__(self):
        yield self.name

class UserQuiz(models.Model):
    class MartialStatus(models.TextChoices):
        married = "M", ('متأهل')
        singel = "S", ('مجرد')

    class YesOrNo(models.TextChoices):
        yes = "Y", ('بله')
        no = "N", ('خیر')
    age = models.CharField(max_length=10,null=True,verbose_name="سن")
    martial_status = models.CharField(choices=MartialStatus, max_length=20, verbose_name='وضعیت تأهل')
    smoke = models.CharField(choices=YesOrNo, max_length=20, verbose_name='آیا سیگار مصرف میکنید؟')
    pain_sckelete = models.CharField(choices=YesOrNo, max_length=20,
                                     verbose_name="آیا سابقه دردهای عضلانی اسکلتی پیش از آن داشته اید ؟ ")
    pain_family_waist = models.CharField(choices=YesOrNo, max_length=20,
                                         verbose_name="آیا سابقه فامیلی درد کمر در فامیل درجه یک داشته اید؟")
    spain_sargery = models.CharField(choices=YesOrNo, max_length=20,
                                     verbose_name="آیا سابقه جراحی ستون فقرات در فامیل درجه یک داشته اید؟")
    back_pain_after_impact = models.CharField(choices=YesOrNo, max_length=20,
                                              verbose_name="آیا کمر درد شما به دنبال ضربه ایجاد شده است ؟")
    back_pain = models.CharField(max_length=20, verbose_name="چند روز از شروع کمر درد شما میگذرد؟")


class PageTwo(models.Model):
    class Tahsilat(models.TextChoices):
        e = "ابتدایی", ('ابتدایی')
        ci = "سیکل", ('سیکل')
        d = "دیپلم", ('دیپلم')
        f_d = "فوق دیپلم", ('فوق دیپلم')
        l = "لیسانس", ('لیسانس')
        f_l = "فوق لیسانس", ('فوق لیسانس')
        dr = "دکتری", ('دکتری')

    class AmountOfSleepChoices(models.TextChoices):
        GOOD = "خواب کافی دارم", ("خواب کافی دارم")
        BAD = "خوب نمیخوابم", ("خوب نمیخوابم")
        GORB = "گاهی خوب میخوابم و گاهی بد", ("گاهی خوب میخوابم و گاهی بد")

    province = models.ForeignKey(Province,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    tahsilat = models.CharField(choices=Tahsilat, max_length=50)
    weight = models.CharField(max_length=150, verbose_name="وزن")
    height = models.CharField(max_length=150, verbose_name="قد")
    time_goes = models.CharField(max_length=150, verbose_name="مدت زمان سپری شده از خدمت:")
    job = models.CharField(max_length=150, verbose_name="شغل")
    sleep = models.CharField(max_length=30, choices=AmountOfSleepChoices,
                             verbose_name="وضعیت خواب خود را چگونه میبینید؟")

    def __str__(self):
        return self.job


class PageThree(models.Model):
    class PAIN_WAIST(models.TextChoices):
        a = "0", ('۰۰-بدون درد')
        b = "1", ('۰۱-خیلی نرم')
        c = "2", ('۰۲-ناراحت کننده')
        d = "3", ('۰۳-قابل تحمل')
        e = "4", ('۰۴-پریشانی')
        f = "5", ('۰۵-بسیار ناراحت کننده')
        g = "6", ('۰۶-شدیدتر')
        h = "7", ('۰۷-خیلی شدید')
        i = "8", ('۰۸-کاملا وحشتناک')
        j = "9", ('۰۹-طاقت فرسا')
        k = "10", ('۱۰-وصف ناپذیر')

    pain_waist = models.CharField(choices=PAIN_WAIST, max_length=120)

    def __str__(self):
        return self.pain_waist


class UserResult(models.Model):
    age = models.CharField(max_length=10,null=True,verbose_name="سن")
    martial_status = models.CharField(max_length=55, verbose_name="وضعیت تأهل")
    province = models.CharField(max_length=75, verbose_name="محل سکونت/استان")
    city = models.CharField(max_length=75, verbose_name="محل سکونت/شهر")
    degree = models.CharField(max_length=75, verbose_name="مقطع تحصیلی")
    job = models.CharField(max_length=75, verbose_name="شغل پیش از شروع خدمت")
    weight = models.IntegerField(verbose_name="وزن")
    height = models.IntegerField(verbose_name="قد")
    bmi = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    time_goes = models.IntegerField(verbose_name="مدت زمان سپری شده از خدمت")
    smoke = models.CharField(max_length=12, verbose_name="آیا سیگار مصرف میکنید؟")
    sleep = models.CharField(max_length=75, verbose_name="وضعیت خواب ")
    history_skeleton_pain = models.CharField(max_length=11, verbose_name="سابقه ی درد های عصلانی استخوانی")
    spain_surgery = models.CharField(max_length=11, verbose_name="سابقه ی جراحی ستون فقرات")
    pain_family = models.CharField(max_length=11, verbose_name="سابقه فامیلی درد های عضلانی")
    back_pain_after_impact = models.CharField(max_length=11,
                                              verbose_name="آیا کمر درد شما به دنبال ضربه ایجاد شده است؟")
    back_pain = models.IntegerField(verbose_name="چند روز از شروع کمر درد شما میگذرد ؟")
    pain_waist = models.IntegerField()
    odi = models.IntegerField()
    disability_level = models.CharField(max_length=150)
    depression = models.CharField(max_length=57, verbose_name="افسردگی")
    anxiety = models.CharField(max_length=57, verbose_name="اضطراب")
    stress = models.CharField(max_length=57, verbose_name="استرس")
    chronic = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class UserResultFinal(models.Model):
    class PredictionChoices(models.TextChoices):
        chronic = "Chronic","chronic"
        acute = "Acute","acute"
    age = models.CharField(max_length=10,null=True,verbose_name="سن")
    martial_status = models.CharField(max_length=55, verbose_name="وضعیت تأهل",null=True,blank=True)
    province = models.CharField(max_length=75, verbose_name="محل سکونت/استان",null=True,blank=True)
    city = models.CharField(max_length=75, verbose_name="محل سکونت/شهر",null=True,blank=True)
    degree = models.CharField(max_length=75, verbose_name="مقطع تحصیلی",null=True,blank=True)
    job = models.CharField(max_length=75, verbose_name="شغل پیش از شروع خدمت",null=True,blank=True)
    weight = models.IntegerField(verbose_name="وزن",null=True,blank=True)
    height = models.IntegerField(verbose_name="قد",null=True,blank=True)
    bmi = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    time_goes = models.IntegerField(verbose_name="مدت زمان سپری شده از خدمت",null=True,blank=True)
    smoke = models.CharField(max_length=12, verbose_name="آیا سیگار مصرف میکنید؟",null=True,blank=True)
    sleep = models.CharField(max_length=75, verbose_name="وضعیت خواب ",null=True,blank=True)
    history_skeleton_pain = models.CharField(max_length=11, verbose_name="سابقه ی درد های عصلانی استخوانی",null=True,blank=True)
    spain_surgery = models.CharField(max_length=11, verbose_name="سابقه ی جراحی ستون فقرات",null=True,blank=True)
    pain_family = models.CharField(max_length=11, verbose_name="سابقه فامیلی درد های عضلانی",null=True,blank=True)
    back_pain_after_impact = models.CharField(max_length=11,
                                              verbose_name="آیا کمر درد شما به دنبال ضربه ایجاد شده است؟",null=True,blank=True)
    back_pain = models.IntegerField(verbose_name="چند روز از شروع کمر درد شما میگذرد ؟",null=True,blank=True)
    pain_waist = models.IntegerField(null=True,blank=True)
    odi = models.IntegerField(null=True,blank=True)
    disability_level = models.CharField(max_length=150,null=True,blank=True)
    depression = models.CharField(max_length=57, verbose_name="افسردگی",null=True,blank=True)
    anxiety = models.CharField(max_length=57, verbose_name="اضطراب",null=True,blank=True)
    stress = models.CharField(max_length=57, verbose_name="استرس",null=True,blank=True)
    prediction = models.CharField(choices=PredictionChoices,default=PredictionChoices.chronic,max_length=155,null=True,blank=True)
    percentage = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
