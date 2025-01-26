import json
from http.server import BaseHTTPRequestHandler

# Load the data from the JSON file
with open("data.json") as f:
    students_data = json.load(f)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        from urllib.parse import parse_qs, urlparse

        query = parse_qs(urlparse(self.path).query)
        names = query.get("name", [])

        # Fetch marks for the given names
        marks = [
            next((student["marks"] for student in students_data if student["name"] == name), None)
            for name in names
        ]

        # Respond with JSON
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"marks": marks}).encode("utf-8"))
