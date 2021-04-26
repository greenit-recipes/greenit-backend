# Greenit

Greenit is a social, economical and ecological solution to replace industrial production by homemade and local production. Our first mission is to lead a community which supports knowledge sharing for healthy consumptions and productions.

Greenit places a high value on its reusability by the community and use of ethical tech, and is therefore FOSS whilst also avoiding using as many of Big Tech’s services as possible.

## Technologies

The progressive web app is built using the [Tailwind Framework](https://github.com/tailwindlabs/tailwindcss) on top of [React](https://reactjs.org/). [Apollo](https://github.com/apollographql) is used to handle GraphQL from the frontend.  

The backend is [Django](https://github.com/django/django) and the database [Postgres](https://www.postgresql.org/).

## Contributing

This project is in an early stage. If you are interested in contributing, feel free to reach out to [liam.going@code.berlin](mailto:liam.going@code.berlin) or [aarnav.bos@code.berlin](mailto:aarnav.bos@code.berlin).

## Development

Install ```greenit-backend``` for development with the following commands:

```bash
git clone https://github.com/greenit-recipes/greenit-backend.git
python3 -m venv env
source env/bin/activate
cd greenit-backend
pip install -r requirements.txt
```
Migrate and launch the development server:

```bash
cd greenit-backend
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

### Running Tests

```bash
cd greenit-backend
./manage.py test
```

