# StackOverFlowAPI

Django and Python3 Application using StackOverflow API for searching questions in StackOverflow (ref: https://api.stackexchange.com/docs/advanced-search)

- Search questions using all available search parameters
- List the results with pagination
- Cache Stackoverflow API data
- Apply throtlling to user requests

## How to run this app:

```
git clone https://github.com/Utkarsh3587/StackOverFlowAPI.git
python3.7 -m venv api-env
source api-env/bin/activate
cd stackoverflow
pip install -r requirments.txt
python manage.py migrate
python manage.py runserver
```

## API

```
URL: localhost:8000/questions/
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
	"body": "python;",
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
