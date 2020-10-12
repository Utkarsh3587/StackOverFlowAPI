# StackOverFlowAPI


This is example code for integrating Stack overFlow api with Django and Django rest framework using cache and throtling.

#How to run this app:

clone this repository
`
git clone https://github.com/Utkarsh3587/StackOverFlowAPI.git
`

Create Virtual Env
`
python3.7 -m venv api-env
source api-env/bin/activate
`

Move to the repo directory
`
cd stackoverflow
`
Install requirement file
`
pip install -r requirments.txt
python manage.py migrate
python manage.py runserver
`

#API
```
URL: localhost:8000/questions
Method: POST
Headers
Content-Type: application/json
JSON BODY Request Parameters - Search Questions based on given parameters
{
	"page":1,
	"pagesize":10,
	"sort": "activity",
	"fromdate": "2019-01-31",
	"todate": "2020-10-12",
	"q":"python",
	"accepted": false, 
	"answers":1,
	"body": "python",
	"closed":false,
	"migrated":false,
	"notoce":false,
	"nottaged":["ruby", "rails"],
	"tagged":["python", "django"],
	"title":"python",
	"view":1
}
```

Response: JSON Response contain a list of questions and attribute `has_more` to fetch more pages.
