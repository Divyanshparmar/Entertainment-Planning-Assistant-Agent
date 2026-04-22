import json

def load_data():
    with open("knowledge_base/data.json", "r") as f:
        return json.load(f)

def fetch_movies():
    data = load_data()
    return [movie["name"] for movie in data["movies"]]

def get_ratings():
    data = load_data()
    return {movie["name"]: movie["rating"] for movie in data["movies"]}

def analyze_reviews():
    return "Reviews analyzed successfully"

def generate_summary():
    return "Summary generated for movies"

# Event functions (extra use case)
def select_event():
    return "Event selected"

def book_venue():
    return "Venue booked"

def send_invitations():
    return "Invitations sent"

def finalize_schedule():
    return "Event schedule finalized"