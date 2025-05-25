# django-ecommerce
django e-commerce  website

# django-ecommerce
django e-commerce  website

#### The technology used in the project:

    -Django.
    -stripe to handel the payment.
    -Bootstrap to handel the style and make the website responsive.
    -mysql database.
    -crispy_forms for the forms style.


### how to make it work

##### create python venv
    python -m venv venv
    
##### activate the venv

###### on Linux & Mac
    
    source venv/bin/activate

###### on Windows    
    
    source venv/Scripts/activate

##### clone the Repositories

    git clone "https://github.com/mohamedhw/django-e.git"

##### install the requirements

    pip install -r requirements.txt

##### run the local server

    cd src
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

