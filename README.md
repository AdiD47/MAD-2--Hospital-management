Hospital Management Dashboard

A simple, multi-functional hospital dashboard web application built with Flask. This project provides separate dashboard views for Admins, Doctors, and Patients, each tailored to their specific roles and needs. The application is designed based on the initial wireframes to provide a clean and intuitive user interface.
Features

    Three Distinct User Roles:

        Admin Dashboard: View and manage doctors, patients, and appointments. Includes a form to add new doctors to the system.

        Doctor Dashboard: View upcoming appointments and a list of assigned patients.

        Patient Dashboard: View upcoming appointments and a detailed personal medical history.

    Modular and Extendable: Built with a clean structure that's easy to understand and build upon.

    Styled Interface: A clean and modern user interface styled with CSS, focusing on usability and clarity.

    Simulation Ready: Uses sample data directly in the Python code to simulate a database, making it easy to run and test without any database setup.

Tech Stack

    Backend: Python, Flask

    Frontend: HTML, CSS

    Templating: Jinja2


Setup and Installation

Follow these steps to get the application running on your local machine.
1. Prerequisites

    Python 3.x

    pip (Python package installer)

2. Clone the Repository

Clone this repository to your local machine:

git clone [https://github.com/your-username/hospital-dashboard.git](https://github.com/your-username/hospital-dashboard.git)
cd hospital-dashboard

3. Create a Virtual Environment (Recommended)

It's a good practice to create a virtual environment to manage project dependencies.

    On macOS/Linux:

    python3 -m venv venv
    source venv/bin/activate

    On Windows:

    python -m venv venv
    .\venv\Scripts\activate

4. Install Dependencies

Install the required packages using the requirements.txt file. For this project, it's just Flask.

pip install Flask

(You can also create a requirements.txt file with the content Flask and run pip install -r requirements.txt)
5. Run the Application

Start the Flask development server:

python app.py

The application will be running at https://www.google.com/search?q=http://127.0.0.1:5000. Open this URL in your web browser to view the dashboard. By default, it will redirect to the Admin dashboard.
Usage

    Admin View: Navigate to http://127.0.0.1:5000/admin

    Doctor View: Navigate to http://127.0.0.1:5000/doctor

    Patient View: Navigate to http://127.0.0.1:5000/patient

Future Improvements

This is a foundational version of the application. Here are some features that can be added to make it more robust:

    Database Integration: Replace the sample data with a proper database like SQLite, PostgreSQL, or MySQL.

    User Authentication: Implement a full login/registration system with password hashing and session management.

    Dynamic Data: Connect the "update" and "delete" buttons to the backend to perform real database operations.

    API Endpoints: Create a RESTful API to allow for a decoupled frontend (e.g., using React or Vue.js).

    Enhanced Doctor Features: Implement the "Provide Availability" feature with a calendar system.

    Appointment Booking: Allow patients to book new appointments with available doctors.
