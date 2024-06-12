# Django WebSocket Chat

![Django](https://img.shields.io/badge/Django-3.0-green)
![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![WebSocket](https://img.shields.io/badge/WebSocket-Protocol-orange)

A simple real-time chat application built with Django and WebSocket protocol.

## Features

- Real-time messaging using WebSocket protocol.
- User authentication and authorization.
- Public and private chat rooms.
- Typing indicators and message status (sent, delivered, read).
- Responsive design for both desktop and mobile.

## Requirements

- Python 3.6 or higher
- Django 3.0 or higher

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Mohammadshekari/django_websocket
    cd django_websocket
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv env
    source env/bin/activate   # For Unix/Linux
    .\env\Scripts\activate   # For Windows
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```sh
    python manage.py migrate
    ```

5. Run the development server:

    ```sh
    python manage.py runserver
    ```

6. Access the chat application at `http://127.0.0.1:8000`.

## Usage

1. Register a new account or log in with existing credentials.
2. Join public chat rooms or create your own private rooms.
3. Start chatting with other users in real-time.
4. View the online status and typing indicators of other users.
5. Enjoy seamless messaging experience with WebSocket technology.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes and commit them (`git commit -am 'Add feature/improvement'`).
4. Push to the branch (`git push origin feature/improvement`).
5. Create a new pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
