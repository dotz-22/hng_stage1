## **Number Classification API**

This is a Django REST API that classifies numbers based on mathematical properties and provides a fun fact using the Numbers API.

Features

✅ Checks if a number is prime, perfect, or Armstrong.
✅ Determines if the number is even or odd.
✅ Computes the sum of its digits.
✅ Fetches a fun fact from the Numbers API.
✅ Returns responses in JSON format.

## **API Endpoint**

GET /api/classify-number/?number=<integer>

Example Request:

GET https://your-app-name.onrender.com/api/classify-number/?number=371

Example Response (200 OK)

{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371."
}

Error Response (400 Bad Request)

{
    "error": true,
    "message": "Invalid input. Provide a valid integer."
}
## **Installation Guide**

1. Clone the Repository
 ```bash
git clone https://github.com/yourusername/number-classification-api.git
cd number-classification-api
```

2. Set Up a Virtual Environment
 ```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```
3. Install Dependencies
 ```bash
pip install -r requirements.txt
```

4. Run the Server
 ```bash
python manage.py runserver
```
Your API will be available at:

http://127.0.0.1:8000/api/classify-number/?number=371


## **Backlink to HNG**
 ```bash
- https://hng.tech/hire/python-developers
```