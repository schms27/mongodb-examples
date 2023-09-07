## Set User Secret

You need to set the following user secret to be able to connect to the database:

```
dotnet user-secrets set "BookStoreDatabase:ConnectionString" "mongodb://<YOUR_MONGODB_ADMIN_PASSWORD>:<YOUR_MONGODB_ADMIN_PASSWORD>@mongodb.service:27017"
```
