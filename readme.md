# CoffeeDB

[ER-Diagram @ Link](https://drive.google.com/file/d/1UXQQlDAK7-t0nZcIUJpLK2xFRa1-58By/view?usp=sharing)

## Common Usage

#### Starting the project

sudo docker-compose up --build -d

#### Running commands in container

sudo docker exec -it coffeBackend /bin/bash


## SQL

### Setting good settings

.mode columns

.headers on


#### Example query

select * 
from coffee_drinker inner join coffee_tasting
on coffee_drinker.userID = coffee_tasting.user_fk_id;