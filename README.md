# E-Commerce Project

A comprehensive e-commerce application built with Django and Django REST Framework. This project includes JWT authentication and various modules for managing users, products, orders, and more.

## Features

- **User Management:** Register, authenticate, and manage users.
- **Product Catalog:** Add, update, and view products.
- **Order Processing:** Manage orders and order statuses.
- **Shopping Cart:** Add and remove items from the cart.
- **Payments:** Handle payment transactions.
- **Reviews:** Submit and view product reviews.
- **Shipping:** Manage shipping options and addresses.
- **Discounts:** Apply and manage discount codes.
- **Inventory Management:** Track product inventory levels.
- **Notifications:** Manage user notifications.

## React Frontend

The frontend of this project is built with React. You can find the React project repository here:

- [Scalable E-commerce Frontend](https://github.com/tanimomor/Scalable-Ecommerce-Fronend.git)


## Installation

### Prerequisites

- Python 3.8+
- Django 4.0+
- Django REST Framework
- djangorestframework-simplejwt

### Setting Up the Project

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/tanimomor/Scalable-Ecommerce.git
    cd your-repository
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```


## JWT Authentication

The application uses JWT for user authentication. To obtain a token:

- **Obtain Token:**

    ```bash
    curl -X POST http://localhost:8000/api/token/ -d '{"username": "your-username", "password": "your-password"}' -H "Content-Type: application/json"
    ```

- **Refresh Token:**

    ```bash
    curl -X POST http://localhost:8000/api/token/refresh/ -d '{"refresh": "your-refresh-token"}' -H "Content-Type: application/json"
    ```

Include the access token in the `Authorization` header for authenticated requests:

```bash
curl -X GET http://localhost:8000/some-protected-endpoint/ -H "Authorization: Bearer <your-access-token>"