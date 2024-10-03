![My Skills](https://skillicons.dev/icons?i=py,django,ai,sklearn,git,sqlite,js,html,jquery,css)


## در مورد پروژه 
پرسشنامه ی تجزیه و تحلیل درد های عضلانی،کمردرد،استرس،اضطراب،افسردگی با استفاده از ai   <br />
هر کدام از سوالات مطرح شده داخل پرسشنامه دارای امتیاز میباشد که در آخر برای محاسبه و پردازش برای aiارسال میشود و جوابهای داده شده تحلیل و جواب متناسب به صورت خودکار برای کاربر نمایش داده میشود 
	
## تکنولوژي های استفاده شده : 

* Python version: 3.10
* Django version: 5.0.8
* Matplotlib version: 3.9
* Numpy version: 1.26
* Pandas version: 2.2
* Scikit-learn version: 1.2
* Joblib version: 1.4

	
## نحوه ی نصب و استفاده
برای اجرای برنامه کامندهای زیر را اجرا کنید:

```
$ git clone https://github.com/pedram12dev/army-proj.git
```
create virtual environment on your system and:
```
$ cd {to project dir}
```
enable venv and:
```
$ pip install -r requirements.txt 
```
به دلیل استفاده از فایل json برای شهر و استان های ایران لازم هست که اسکریپت های نوشته شده رو اجرا کنید سپس با fixturesهای جنگو کل داده های آپدیت شده رو داخل دیتابیس اعمال کنید.
برای راحتی استفاده، اسکریپت ها اجرا شده و فایلهای نهایی json داخل پروژه قرار داده شده و کافیه دستورات زیر را به ترتیب اجرا کنید : 
```
$ python manage.py migrate
$ python manage.py loaddata provinces.json
$ python manage.py loaddata cities.json
```
بعد از اجرای دستورات بالا شهر و استان های ایران به دیتابیس اضافه شده اند و بعد از ساخت superuserمیتوانید داخل پنل admin به اطلاعات درسترسی داشته باشید 
```
$ python manage.py createsuperuser
```
```
$ python manage.py makemigrations
$ python manage.py migrate
```
و درنهایت کافیه پروژه رو اجرا و استفاده کنید 
```
$ python manage.py runserver
```
UI/UX Designer: Mehrana Abian <br />
Frontend Developer : Hossein Hossein <br />
Backend Developer: Pedram Najafi <br />
AI Engineer : Rezvan Sangcheshmeh