# palettes
  ### project install:
    1. clone project
    2. cd projectname
    3. run pip install -r requirements/dev.txt
    4. run python manage.py makemigratons
    5. run python manage.py migrates
    6. run python manage.py runserver
 
 ### urls
  1. homepage: http://127.0.0.1:8000/
  2. adminpage: http://127.0.0.1:8000/admin
  3. get all palettes: http://127.0.0.1:8000/api/palettes/  only can view, to add new palettes need login or give token in header
  4. get single palttes: http://127.0.0.1:8000/api/palettes/1/
  5. update, delete: http://127.0.0.1:8000/api/palettes/1/ with user token and data in header
  6. search: http://127.0.0.1:8000/api/palettes?color_name=colorname  also can seach color domain, accents
  7. get token by passing username password in body: http://127.0.0.1:8000/api/v1/auth/login
    

