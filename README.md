# 📝 Django Blog Website

> This project was built as part of the **"Building an API Using Django"** course at [Tuwaiq Academy](https://tuwaiq.edu.sa/).

---

## 📖 About the Project

A simple blog web application built with **Django** that allows users to browse blog posts, view post details, explore categories, and read comments — all served through Django views and templates.

---

## 🚀 Features

- View a list of all registered users
- Browse all blog posts with clickable titles
- View full details of a specific blog post
- Browse all categories
- View all comments with their associated post IDs

---

## 🗂️ Project Structure

```
project/
│
├── templates/
│   ├── master.html        # Base template (layout)
│   ├── main.html          # Homepage
│   ├── blogs.html         # List of all blog posts
│   ├── blogdetails.html   # Single blog post detail
│   ├── users.html         # List of all users
│   ├── comments.html      # List of all comments
│   └── categories.html    # List of all categories
│
└── views.py               # All view functions
```

---

## ⚙️ Views & URLs

| View           | Description                        |
|----------------|------------------------------------|
| `main`         | Renders the homepage               |
| `users`        | Lists all users                    |
| `blogs`        | Lists all blog post titles         |
| `blogdetails`  | Shows details of a specific post   |
| `comments`     | Lists all comments                 |
| `categories`   | Lists all categories               |

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Templating:** Django Template Language (DTL)
- **Database:** Django ORM (models: `User`, `Post`, `Comment`, `Category`)

---

## 🏁 Getting Started

### Prerequisites

- Python 3.x
- Django

### Installation

```bash
# Clone the repository
git clone https://github.com/MohammedAlrehaili/BlogWebsite.git
cd BlogWebsite

# Install dependencies
pip install django

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

Then open your browser and go to: `http://127.0.0.1:8000/`

---

## 🎓 Course Info

This project was developed as part of the **"Building an API Using Django"** course
