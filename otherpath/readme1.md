# 🎬 Movie Finder App (Python + API)

## 🎯 Goal

Build a CLI app that:

* Searches movies by name
* Fetches real data from an API
* Displays clean results like rating, year, and overview

You’ll learn:

* API requests in Python
* Query parameters
* Working with lists/dictionaries
* Basic filtering and UX design

---

# 🔌 API Used

We’ll use **OMDb API** (simple and beginner-friendly)

👉 [https://www.omdbapi.com/](https://www.omdbapi.com/)

### 🧾 Get an API key

* Go to the site
* Sign up for a free key
* Example key format: `apikey=123abc`

---

# 🧱 Step 1: Install Requests

```bash id="m1q8xa"
pip install requests
```

---

# 🟢 Version 1 — Basic Movie Search
If you are not able to get an API key I would give you mine
```python id="k8d2pq"
import requests

API_KEY = "your_api_key_here"
```

```python

def search_movie(title):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={title}"
    response = requests.get(url)
    return response.json()
```
Now, you receive the user input using`input()` for the name of the movie, and then it gets stored in the variable. You can call the variable anything you want

Then you use the function you created in the first step

```python

movie_name = input("Enter movie name: ")
data = search_movie(movie_name)
```
If it finds something similar, it then returns True if it's true, and then prints the movie
```python
if data["Response"] == "True":
    for movie in data["Search"]:
        print("\n🎬 Title:", movie["Title"])
        print("📅 Year:", movie["Year"])
        print("🎞️ Type:", movie["Type"])
```
```
else:
    print("❌ No movies found")
```

---

# 🟡 Version 2 — Better Details (Single Movie Info)

Now we fetch full movie details using IMDb ID.

```python id="x9r3lm"
import requests

API_KEY = "your_api_key_here"

def get_movie_details(imdb_id):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={imdb_id}&plot=short"
    response = requests.get(url)
    return response.json()

movie_name = input("Enter movie name: ")

search_url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={movie_name}"
search_data = requests.get(search_url).json()

if search_data["Response"] == "True":
    first_movie = search_data["Search"][0]
    movie_id = first_movie["imdbID"]

    details = get_movie_details(movie_id)

    print("\n🎬 Title:", details["Title"])
    print("📅 Year:", details["Year"])
    print("⭐ Rating:", details["imdbRating"])
    print("🎭 Genre:", details["Genre"])
    print("📝 Plot:", details["Plot"])
else:
    print("❌ Movie not found")
```

---

# 🟠 Version 3 — Interactive Movie Explorer

```python id="z2k7pn"
import requests

API_KEY = "your_api_key_here"

def search_movies(query):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={query}"
    return requests.get(url).json()

def get_details(imdb_id):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={imdb_id}&plot=short"
    return requests.get(url).json()

while True:
    query = input("\n🎬 Search movie (or type 'quit'): ")

    if query.lower() == "quit":
        print("Goodbye 👋")
        break

    data = search_movies(query)

    if data["Response"] == "True":
        movies = data["Search"][:5]  # top 5 results

        print("\n🔍 Results:")
        for i, m in enumerate(movies):
            print(f"{i+1}. {m['Title']} ({m['Year']})")

        choice = input("\nSelect a movie number: ")

        if choice.isdigit():
            idx = int(choice) - 1

            if 0 <= idx < len(movies):
                movie_id = movies[idx]["imdbID"]
                details = get_details(movie_id)

                print("\n🎬 --- Movie Details ---")
                print("Title:", details["Title"])
                print("Year:", details["Year"])
                print("Rating:", details["imdbRating"])
                print("Genre:", details["Genre"])
                print("Plot:", details["Plot"])
    else:
        print("❌ No results found")
```


