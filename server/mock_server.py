from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock user data with sample profiles
user_data = {
    "John Doe": {
        "name": "John Doe",
        "occupation": "Software Engineer",
        "social_media": {
            "LinkedIn": "https://linkedin.com/in/johndoe",
            "Twitter": "@johndoe",
            "Instagram": "@johndoe_ig"
        }
    },
    "Jane Smith": {
        "name": "Jane Smith",
        "occupation": "Data Scientist",
        "social_media": {
            "LinkedIn": "https://linkedin.com/in/janesmith",
            "Twitter": "@janesmith",
            "Instagram": "@janesmith_ig"
        }
    }
}

@app.route('/get_user_info', methods=['GET'])
def get_user_info():
    name = request.args.get('name')
    user_info = user_data.get(name, {
        "name": "Unknown",
        "occupation": "N/A",
        "social_media": {
            "LinkedIn": "N/A",
            "Twitter": "N/A",
            "Instagram": "N/A"
        }
    })
    return jsonify(user_info)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
