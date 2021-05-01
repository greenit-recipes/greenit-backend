# Greenit

Greenit is a social, economical and ecological solution to replace industrial production by homemade and local production. Our first mission is to lead a community which supports knowledge sharing for healthy consumptions and productions.

Our V1 is a recipe site, focussed on building a community around discovering, creating and sharing recipes with each other. 

Greenit places a high value on its reusability by the community and use of ethical tech, and is therefore FOSS whilst also avoiding using as many of Big Tech’s services as possible.


## Technologies

The progressive web app displays user-uploaded recipes sorted by categories and tags and is hosted on [DigitalOcean's](https://try.digitalocean.com/developer-brand-nofto/?utm_campaign=emea_brand-no-fto_kw_en_cpc&utm_adgroup=digitalocean_exact_exact&_keyword=digital%20ocean&_device=c&_adposition=&utm_content=conversion&utm_medium=cpc&utm_source=google&gclid=CjwKCAjwj6SEBhAOEiwAvFRuKPht-tyNGYt1NdkuSOOknBkfAxPBa8xCCiU0hH_GOQVUh6REBXUqRRoCm1cQAvD_BwE) servers. We use [plausible.io](https://plausible.io/) for analytics.

The frontend is built using the [Tailwind Framework](https://github.com/tailwindlabs/tailwindcss) on top of [React](https://reactjs.org/). [Apollo](https://github.com/apollographql) is used to handle GraphQL.

The backend is [Django](https://github.com/django/django)/[GraphQL](https://github.com/graphql) and the database [Postgres](https://www.postgresql.org/).

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
Create an .env file based on the sample.env provided and edit it to match your project's specs:
```bash
cp sample.env .env
```
```bash
# edit .env:
/*
SECRET_KEY= ...   <--- https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-SECRET_KEY
POSTGRES_DB_USERNAME= ... <--- The name of your database
POSTGRES_DB_PASS= ... <--- The password to your database
POSTGRES_DB_HOST= ... <--- Where your database is hosted, i.e. 127.0.0.1 if localhost
*/
```
Make sure the .env file is listed in your .gitignore file, so your access information isn't pushed to github.


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

