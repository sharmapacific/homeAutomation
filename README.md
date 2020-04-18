# homeAutomation

**Project SetUp -** 
```
  Do git clone - 
  git clone https://github.com/sharmapacific/homeAutomation.git

  Go inside the directory 
  cd homeAutomation

  Install Requirements
  pip install -r requirements.txt

  and Migrate Migrations
  python manage.py migrate
```

**Web console Commands to perform Scenarios**

01. To add a new device 
```
python manage.py add_device <device_name>
Exp - python manage.py add_device tv
```
02.	List All smart Device
``` 
python manage.py show_devices 

To List All OFF devices 
python manage.py show_devices 0 		- > To list out only OFF devices

To List All ON devices - 
python manage.py show_devices 1		- > To list out only ON devices
```
03. Perform an Operation on device
```   
python manage.py perform <device_name>  <action>	-> 0 for OFF , 1 for ON
Exp - python manage.py perform tv 1 
```
04.  Remove an installed device
```
python manage.py delete_device <device_name>
Exp - python manage.py delete_device tv

To Remove all installed devices - 
python manage.py delete_device
```

To View All Device Details from Django admin Panel - 
```
CreateSuperUser
python manage.py createsuperuser			Add UserName and Password

Runserver
python manage.py runserver

And Visit
http://127.0.0.1:8000/admin/device/deviceinfo/
```
