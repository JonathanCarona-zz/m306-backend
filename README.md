# m306-backend
## Getting Started

### Installing Dependencies

#### Python 3.7.3

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./flaskr` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app;
export FLASK_ENV=development
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

# API Documentation
## Getting Started
- Base URL by default `http://127.0.0.1:5000/`
- Authentication: This version of the application requires authentication. Authentication Service from Auth0 was used

## Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}
```

The API has the following Handlers for errors:
- 400: Bad Request
- 401: Unauthorized
- 404: Not Found
- 405: Method Not Allowed
- 422: Unprocessable
- 500: Internal Server Error
- AuthError: Custom error trown when authentication is not in order

## Endpoints

### GET /jetons/<id>
- Returns jeton parameters of `jeton`, which contains the user id, jeton amount und jeton factor.
- Request need to have a bearer token that includes the permission "get:jetons"
- Sample: `http://127.0.0.1:5000/jetons/1`
```
{
    "success": True,
    "jeton_amount": 2000,
    "user_id": 1,
    "factor": 1.5
}
```

### POST /jetons
- Creates a new jeton in the db (currently an ini file), the request includes a user_id and jeton_amount
- Request need to have a bearer token that includes the permission "post:jetons"
- Sample Request
```
{
    "user_id": "nerglnlksdjnaföo4n32ne2k",
    "jeton_amount": 10000
}
```

- This request will return as following
```
{
    "success": True,
    "new_jeton": 10000
}
```

### PATCH /jetons
- Creates a new jeton in the db (currently an ini file), the request has to include a user_id and jeton_amount but only the jeton_amount will be edited
- Request need to have a bearer token that includes the permission "patch:jetons"
- Sample Request
```
{
    "jeton_amount": 10000
}
```

- This request will return as following
```
{
    "success": True,
    "new_jeton": 10000
}
```

### PATCH /payment/<paymentmethod>
- Creates a new jeton in the db (currently an ini file), the request includes a user_id and jeton_amount
- Request need to have a bearer token that includes the permission "patch:payment"
- Sample Request
```
{
    "user_id": "nerglnlksdjnaföo4n32ne2k",
    "jeton_amount": 10000
}
```

- This request will return as following
```
{
    "success": True,
    "new_jeton": 10000
}
```


# Testing Authentication

Test your endpoints with [Postman](https://getpostman.com). 
- Register a new user - assign the "player" role.
- Sign into the account and make note of the JWT.
- Import the postman collection `./tests/m306-casino.postman_collection.json`
- Right-clicking the collection folder for player, navigate to the authorization tab, and including the JWT in the token field.
- Run the collection and correct any errors.