# Flask Mongo RESTful API

## Running
Build containers
`docker-compose-up -d --build`

Import the first user to MongoDB
```
docker exec -it mongodb mongoimport --db flask --collection user --type json --file /init.json --jsonArray
```


## Building the assets
`cd app && npm run build`

Access `http://0.0.0.0:5000`

## API

Get token
```
curl -XPOST -H "Content-type: application/json" -d '{"username": "admin","password": "admin"}' http://0.0.0.0:5000/api/v1/login
```


## API documentation
Access `http://0.0.0.0:5000/apidocs/`




Enjoy :)
