# Setup

## Creating a new environment

```
conda env create -f environment.yml
```

## Activate an environment

```
conda activate mongodb-demo
```

## Updating an environment

```
conda env update -f environment.yml
```

## Starting mongo-db container:

You will ned to create an env-file in /python/cli/.env with the
following content:

```
MONGO_ROOT_USER<INSERT YOUR ROOT USERNAME HERE>
MONGO_ROOT_PASSWORD=<INSERT YOUR PASSWORD HERE>
```

Then run:

```
docker-compose --env-file ./.env up -d
```

# Simple CRUD Operations (CLI)

## Set Database and collection

To define on which db and collection to work, we can use the CLI-Arguments --database/-d and --collection/-c. If undefined, the default values of "test-database" and "test-collection" will be used.

Here are some examples how to perform various database operations using the python cli:

## Create

```ps
python .\python\src\cli\main.py --object '{"this":"is a test","some":"data"}' write-object
python .\python\src\cli\main.py -d new-db -c new-collection -o '{"this":"is another test","some":"different data"}' write-object
```

## Read All (List)

```ps
python .\python\src\cli\main.py  list-objects
```

## Update

```ps
python .\python\src\cli\main.py --filter '{"this":"is something else"}' --object   '{"andd":"updated_5"}' update-object
```

## Delete

```ps
python .\python\src\cli\main.py --filter '{"this":"is something else"}' delete-objects
```

# REST with FastAPI and Swagger

Starting a local server:

```ps
cd ./python/src/api/
python -m uvicorn main:app --reload
```

Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to see the swagger(openAPI) page.

# Move all to Docker

## Preparations

Lock packages for linux:

```ps
conda install --channel=conda-forge --name=base conda-lock
conda-lock -p linux-64 -f environment.yml -k explicit --filename-template 'environment-{platform}.lock'
```

## Docker Compose

Start stack:

```ps
cd ./python
docker-compose up -d
```

Stop stack:

```ps
docker-compose down
```

Force rebuild:

```ps
docker-compose build
```
