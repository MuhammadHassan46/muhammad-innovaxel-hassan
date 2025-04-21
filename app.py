from flask import Flask, request, jsonify, render_template, redirect, abort
from models import db, URL, generate_short_code
from validators import is_valid_url
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    urls = URL.query.all()  # Fetch all saved URLs from the database
    return render_template('index.html', urls=urls)

# Redirect route
@app.route('/<short_code>')
def redirect_to_url(short_code):
    url_data = URL.query.filter_by(short_code=short_code).first()
    if url_data:
        url_data.access_count += 1
        db.session.commit()
        return redirect(url_data.original_url)
    return abort(404)

# API Routes
@app.route('/shorten', methods=['POST'])
def create_short_url():
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400
    
    original_url = data['url']
    
    if not is_valid_url(original_url):
        return jsonify({'error': 'Invalid URL format'}), 400
    
    # Generate a unique short code
    short_code = generate_short_code()
    
    # Create new URL record
    new_url = URL(original_url=original_url, short_code=short_code)
    db.session.add(new_url)
    db.session.commit()
    
    return jsonify(new_url.to_dict()), 201

@app.route('/shorten/<short_code>', methods=['GET'])
def get_original_url(short_code):
    url_data = URL.query.filter_by(short_code=short_code).first()
    
    if not url_data:
        return jsonify({'error': 'URL not found'}), 404
    
    return jsonify(url_data.to_dict()), 200

@app.route('/shorten/<short_code>', methods=['PUT'])
def update_url(short_code):
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400
    
    original_url = data['url']
    
    if not is_valid_url(original_url):
        return jsonify({'error': 'Invalid URL format'}), 400
    
    url_data = URL.query.filter_by(short_code=short_code).first()
    
    if not url_data:
        return jsonify({'error': 'URL not found'}), 404
    
    url_data.original_url = original_url
    db.session.commit()
    
    return jsonify(url_data.to_dict()), 200

@app.route('/shorten/<short_code>', methods=['DELETE'])
def delete_url(short_code):
    url_data = URL.query.filter_by(short_code=short_code).first()
    
    if not url_data:
        return jsonify({'error': 'URL not found'}), 404
    
    db.session.delete(url_data)
    db.session.commit()
    
    return '', 204

@app.route('/shorten/<short_code>/stats', methods=['GET'])
def get_url_stats(short_code):
    url_data = URL.query.filter_by(short_code=short_code).first()
    
    if not url_data:
        return jsonify({'error': 'URL not found'}), 404
    
    return jsonify(url_data.to_dict()), 200

if __name__ == '__main__':
    app.run(debug=True)