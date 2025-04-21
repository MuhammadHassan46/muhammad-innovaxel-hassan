
# URL Shortening Service – Innovaxel Take-Home Assignment

A RESTful API service built with Flask to shorten long URLs, retrieve original URLs, update, delete, and track usage statistics.

---

## 📌 Features

- ✅ Shorten long URLs to unique short codes
- 🔁 Retrieve original URL from a short code
- ✏️ Update an existing shortened URL
- ❌ Delete a short URL entry
- 📊 Get access statistics (number of times a short URL has been used)

---

## ⚙️ Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL (via SQLAlchemy ORM)

---

## 🚀 API Endpoints

### 1. Create Short URL  
**POST** `/shorten`

#### Request:
```json
{
  "url": "https://example.com"
}
```

#### Response:
```json
{
  "id": 1,
  "url": "https://example.com",
  "shortCode": "abc123",
  "createdAt": "2024-04-20T14:30:00Z",
  "updatedAt": "2024-04-20T14:30:00Z"
}
```

---

### 2. Retrieve Original URL  
**GET** `/shorten/<short_code>`

#### Response:
```json
{
  "id": 1,
  "url": "https://example.com",
  "shortCode": "abc123",
  "createdAt": "2024-04-20T14:30:00Z",
  "updatedAt": "2024-04-20T14:30:00Z"
}
```

---

### 3. Update Short URL  
**PUT** `/shorten/<short_code>`

#### Request:
```json
{
  "url": "https://newdomain.com"
}
```

#### Response:
```json
{
  "id": 1,
  "url": "https://newdomain.com",
  "shortCode": "abc123",
  "createdAt": "2024-04-20T14:30:00Z",
  "updatedAt": "2024-04-20T15:00:00Z"
}
```

---

### 4. Delete Short URL  
**DELETE** `/shorten/<short_code>`

#### Response:
- `204 No Content` if successfully deleted
- `404 Not Found` if not found

---

### 5. Get URL Statistics  
**GET** `/shorten/<short_code>/stats`

#### Response:
```json
{
  "id": 1,
  "url": "https://example.com",
  "shortCode": "abc123",
  "createdAt": "2024-04-20T14:30:00Z",
  "updatedAt": "2024-04-20T14:30:00Z",
  "accessCount": 3
}
```

---

## 🛠️ Setup Instructions

### Clone the repository
```bash
git clone https://github.com/<your-github-username>/muhammad-innovaxel-hassan.git
cd muhammad-innovaxel-hassan
```

### Install dependencies
```bash
pip install flask flask-sqlalchemy cryptography
```

### Run the server
```bash
python app.py
```

> The server will start on `http://127.0.0.1:5000`

---

## 📂 Project Structure

```
flask_url_shortener/
├── app.py             # Main app logic
├── models.py          # Database model
├── config.py          # Helper for db configuration
├── validators.py      # Helper to validate urls
├── validators.py      # Helper to validate urls
└── static
    ├── css      # Folder for css styleseets (empty)
    └── js       # Folder for js files (empty)
└── templates
    └── index.html      # Front End
└── README.md
```

## 🙋‍♂️ Author

**Muhammad Hassan Zahid**  
Email: *[muhammadhassanzahid4@gmail.com]*  
GitHub: [https://github.com/MuhammadHassan46]

---

## 📌 Notes

- Authentication/authorization not required for this assignment.
- Fully functional via Postman or any REST client.

---

## 🧪 Sample Testing via curl (optional)

```bash
curl -X POST http://127.0.0.1:5000/shorten -H "Content-Type: application/json" -d "{\"url\": \"https://dev.mysql.com/downloads/"}"
```

