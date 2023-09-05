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

Here are some examples how to perform various database operations using the python cli:

## Create

```ps
python .\python\cli\src\main.py --object '{"this":"is a test","some":"data"}' write-object
```

## Read All (List)

```ps
python .\python\cli\src\main.py  list-objects
```

## Update

```ps
python .\python\cli\src\main.py --filter '{"this":"is something else"}' --object   {"andd":"updated_5"}' update-object
```

## Delete

```ps
python .\python\cli\src\main.py --filter '{"this":"is something else"}' delete-objects
```
