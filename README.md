## Tpay 코딩테스트
**tpay 코딩테스트를 위한 repository입니다.**

### Django 실행 방법
```
$git clone https://github.com/parkhongbeen/tpay_test

$pyenv virtualenv 가상환경명     #가상환경생성(가상 개발 환경에 따라 상이할 수 있음)
    
$pyenv local 가상환경명		#clone받은 폴더내에 적용
    
$pip install -r requirements.txt

$python manage.py makemigrations

$python manage.py migrate

$python manage.py runserver
```

### Docker 실행 방법
- dockerfile이 있는곳에서 명령어를 실행합니다.
```
$docker pull django

$docker build -t tpay .

$docker run -it -p 8000:8000 --volume tpay_test --name tpaycontainer tpay
```

### API 테스트, Postman Export결과
- Postman Export파일: Tpay Test.postman_collection.json
- Postman URL: Postman URL
- DRF_yasg: http://127.0.0.1:8000/doc/ (접속 예시 화면)
https://user-images.githubusercontent.com/53684676/91666662-89748700-eb39-11ea-9398-bcdb4b18674c.png
