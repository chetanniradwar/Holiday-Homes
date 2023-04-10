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


## postman link for all api links
[postman link](https://www.postman.com/chetan-kafqa/workspace/inkredo)