# OWASP TOP 10- Web App Security- Broken Access control- Lab2

This is a simple web application designed for learning and practicing web application security, focusing on the broken access control vulnerability. The lab includes a Flask web app with an intentionally vulnerable API.

## Vulnerability Description

The main vulnerability in this lab is Permitting viewing or editing someone else's account, by providing its unique identifier (insecure direct object references).

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/web-app-security-lab.git
    ```

2. Navigate to the project directory:

    ```bash
    cd web-app-security-lab
    ```

3. Create a Python virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the Flask web app:

    ```bash
    python app.py
    ```

The web app will be accessible at http://localhost:5000/.

## Usage

- Visit http://localhost:5000/ .
- Click on a book title to see detailed information about the book.
- Note: Users are not allowed to add or delete books; the lab intentionally exposes vulnerabilities for educational purposes.
- Find Flag.

## Disclaimer

This lab is intended for educational purposes only. Ensure that you have proper authorization before using it, and do not perform any actions that violate the law or terms of service. Be responsible and ethical in your use of this lab.

## Acknowledgments

- The web app is built using Flask.
- Inspired by security training platforms and labs.
