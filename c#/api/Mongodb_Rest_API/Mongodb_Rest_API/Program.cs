using Mongodb_Rest_API.Models;
using Mongodb_Rest_API.Services;


var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.Configure<DatabaseSettings>(
    builder.Configuration.GetSection("BookStoreDatabase")
    );

builder.Services.AddSingleton<BooksService>();


// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.MapGet("/books", async (BooksService service) => await service.GetAsync())
.WithOpenApi();

app.MapGet("/book/{id}", async (string id, BooksService service) => await service.GetAsync(id))
.WithOpenApi();

app.MapPost("/book", async (Book book, BooksService service) => await service.CreateAsync(book))
.WithOpenApi();

app.MapPut("/book/{id}", async (string id, Book book, BooksService service) => await service.UpdateAsync(id, book))
.WithOpenApi();

app.MapDelete("/book/{id}", async (string id, BooksService service) => await service.RemoveAsync(id))
.WithOpenApi();

app.Run();

internal record WeatherForecast(DateOnly Date, int TemperatureC, string? Summary)
{
    public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
}
