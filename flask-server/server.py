from flask import Flask, request
from flask_cors import CORS
from lenses_manager import insert_lens

app = Flask(__name__)
CORS(app)

# API Routes
@app.route("/add_lens", methods=["POST"])
def add_lens():
    data = request.get_json()
    return insert_lens(data)
    
@app.route("/delete_lens", methods=["POST"])
def delete_lens():
    data = request.get_json()
    return delete_lens(data)

@app.route("/lens_data")
def lenses():
    return {"lens": ["Member1", "Member2", "Member3"]}


if __name__ == "__main__":
    app.run(debug=True)