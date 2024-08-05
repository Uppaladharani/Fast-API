from fastapi import FastAPI

app = FastAPI()  #it is instance of the clss(fastapi)

food_items = {
    'indian': ["bajji", "samosa", "dosa"],
    'american': ["hot dog", "apple pie", "kfc"],
    'italian': ["pizza", "taco"],
    'korean':[" kimchi","chap chae","sushi"]
}

@app.get("/food-items/{cuisine}")  # End point
async def get_food_items(cuisine: str):  # Function name changed  as get_food_items
    return food_items.get(cuisine, "Cuisine not found")# if cuisine is not found then it will result as cuisine not found
