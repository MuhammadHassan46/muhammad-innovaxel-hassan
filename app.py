from flask import Flask, request, jsonify, render_template, redirect, abort
from models import db, URL, generate_short_code
from validators import is_valid_url
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/shorten', methods=['POST'])
def create_short_url():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400

    original_url = data['url']
    if not is_valid_url(original_url):
        return jsonify({'error': 'Invalid URL format'}), 400

    short_code = generate_short_code()
    new_url = URL(original_url=original_url, short_code=short_code)
    db.session.add(new_url)
    db.session.commit()
    return jsonify(new_url.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
