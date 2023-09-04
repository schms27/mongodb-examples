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
