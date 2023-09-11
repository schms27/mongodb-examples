# GridFS

## Working with mongofiles cli

You will need to have DatabaseTools cli installed and in your path:

1. winget install --id=MongoDB.DatabaseTools -e
2. add to path

```
mongofiles --port 27000 --authenticationDatabase admin -u mongodbuser -d testprotocols put ..\testdata\Test_Data_10.5MB.pdf
```

```
mongofiles --port 27000 --authenticationDatabase admin -u mongodbuser -d testprotocols list
```

```
mongofiles --port 27000 --authenticationDatabase admin -u mongodbuser -d testprotocols get ..\testdata\Test_Data_10.5MB.pdf --local .\downloaded_file.pdf
```
