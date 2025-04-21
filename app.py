from flask import Flask, render_template, redirect, abort
from models import db, URL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    urls = URL.query.all()
    return render_template('index.html', urls=urls)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url_data = URL.query.filter_by(short_code=short_code).first()
    if url_data:
        url_data.access_count += 1
        db.session.commit()
        return redirect(url_data.original_url)
    return abort(404)

if __name__ == '__main__':
    app.run(debug=True)
