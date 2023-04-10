# inkredo_assessment

## Project Setup for Mac

1. install brew using `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

2. install pipenv globally using `brew install pipenv`

3. install postgres using `brew install postgres`

4. On terminal `createuser -s postgres
psql -U postgres` to create 'postgres' user with password 'postgres'`

5. on termial write `psql` to open postgres command terminal

6. switch to postgress user if user is not postgres by `psql -U postgres`

7. on psql `CREATE DATABASE holidayhomes;` to create holidayhomes database

8. create a project folder `inkredo_assessment`

9. clone the git repo locally using `git clone https://github.com/chetanniradwar/inkredo_assessment.git` in that folder

10. in current folder run `pipenv shell` to create virtual environment

11. `pipenv install` to install all the project dependencies

12. then, `cd holiday_homes` folder inside which `manage.py` file is there.

13. run `python manage.py migrate` to migrate all migrations and create table in the database

14. run `python manage.py runserver` to run the development servser on 8000 port


## Postman link for all api links
- [postman link](https://www.postman.com/chetan-kafqa/workspace/inkredo)

- please open collection documentation for more details.
- [documentation link](https://www.postman.com/chetan-kafqa/workspace/inkredo/documentation/20803750-a01fa905-83de-41b8-b177-960ddeec5826?entity=request-20803750-81fe1dff-960f-4bba-94f3-18f934684fac&branch=&version=)


## Technologies Used
- `djangorestframework` - to make REST apis in django
- `pipenv` - for making virtual environment
- `requests` - to make https requests using python
- `json` - to convert json to python dictionary and vice versa
- `pytest` - for writing unit test cases

## Assumption made
- Assuming that owner wants to give availability data of future dates also, I made separate table as HomeDetail
- Assuming that there can be variation in rent price and checkin time and checkout time for each date I added these field in HomeDetail table.
- Added some extra fields in tables that are required in realtime environment
- Assuming that there can be multiple pictures of the single home / room, made pictures field as ArrayField to store list of urls
- Assuming that there can be separate set of pictures for each room of the home, and seperate set for home, hence added picture field in both Room table and HolidayHome table

