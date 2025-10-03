from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'  


users = {
    'admin': {'password': 'admin123', 'role': 'admin', 'name': 'Administrator'},
    'doctor1': {'password': 'doctor123', 'role': 'doctor', 'name': 'Dr. Abcde'},
    'patient1': {'password': 'patient123', 'role': 'patient', 'name': 'Mr. Jklmn'}
}
doctors = [
    {"id": 1, "name": "Dr. Abcde", "department": "Cardiology"},
    {"id": 2, "name": "Dr. Pqrst", "department": "Neurology"},
    {"id": 3, "name": "Dr. Xyzw", "department": "Oncology"},
]

patients = [
    {"id": 101, "name": "Mr. Jklmn"},
    {"id": 102, "name": "Mrs. Opqrs"},
]

appointments = [
    {
        "id": 1001,
        "patient_name": "Mr. Jklmn",
        "doctor_name": "Dr. Abcde",
        "department": "Cardiology",
        "date": "2025-10-28",
        "time": "10:00 AM"
    },
    {
        "id": 1002,
        "patient_name": "Mrs. Opqrs",
        "doctor_name": "Dr. Pqrst",
        "department": "Neurology",
        "date": "2025-10-28",
        "time": "11:30 AM"
    },
]

# --- Authentication Decorator ---
def login_required(role=None):
    """Decorator to require login and optionally check for specific role."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'username' not in session:
                flash('Please login to access this page.', 'warning')
                return redirect(url_for('login'))
            if role and session.get('role') != role:
                flash('You do not have permission to access this page.', 'danger')
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# --- Routes ---

@app.route('/')
def home():
    """Redirects based on user role or to login if not logged in."""
    if 'username' in session:
        role = session.get('role')
        if role == 'admin':
            return redirect(url_for('admin_dashboard'))
        elif role == 'doctor':
            return redirect(url_for('doctor_dashboard'))
        elif role == 'patient':
            return redirect(url_for('patient_dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles user login."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')
        
        # Validate credentials
        if username in users and users[username]['password'] == password:
            if users[username]['role'] == role:
                # Set session
                session['username'] = username
                session['role'] = role
                session['name'] = users[username]['name']
                flash(f'Welcome, {users[username]["name"]}!', 'success')
                
                # Redirect based on role
                if role == 'admin':
                    return redirect(url_for('admin_dashboard'))
                elif role == 'doctor':
                    return redirect(url_for('doctor_dashboard'))
                elif role == 'patient':
                    return redirect(url_for('patient_dashboard'))
            else:
                flash('Invalid role selected for this account.', 'danger')
        else:
            flash('Invalid username or password.', 'danger')
    
    return render_template('login_page.html')

@app.route('/logout')
def logout():
    """Logs out the user."""
    session.clear()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles user registration."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')
        name = request.form.get('name')
        
        # Check if username already exists
        if username in users:
            flash('Username already exists. Please choose another.', 'danger')
        else:
            # Add new user
            users[username] = {
                'password': password,
                'role': role,
                'name': name
            }
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register_page.html')


@app.route('/admin')
@login_required(role='admin')
def admin_dashboard():
    """Renders the admin dashboard with all data."""
    return render_template('admin_dashboard.html', doctors=doctors, patients=patients, appointments=appointments)

@app.route('/admin/add_doctor', methods=['POST'])
@login_required(role='admin')
def add_doctor():
    """Handles the form submission for adding a new doctor."""
    if request.method == 'POST':
        new_id = max([d['id'] for d in doctors]) + 1 if doctors else 1
        new_doctor = {
            'id': new_id,
            'name': request.form['name'],
            'department': request.form['department']
        }
        doctors.append(new_doctor)
        flash('Doctor added successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/doctor')
@login_required(role='doctor')
def doctor_dashboard():
    """Renders the doctor's dashboard (with sample data for now)."""
    # In a real app, you'd filter this by the logged-in doctor
    assigned_patients = patients
    upcoming_appointments = appointments
    return render_template('doctor_dashboard.html', appointments=upcoming_appointments, patients=assigned_patients)

@app.route('/patient')
@login_required(role='patient')
def patient_dashboard():
    """Renders the patient's dashboard (with sample data for now)."""
    # In a real app, you'd filter this by the logged-in patient
    upcoming_appointments = appointments
    patient_history = [
        {"visit_no": 1, "type": "In-person", "tests": "ECG", "diagnosis": "Abnormal", "prescription": "Medicine 1"},
        {"visit_no": 2, "type": "In-person", "tests": "ECG", "diagnosis": "Normal", "prescription": "Exercise daily"},
    ]
    return render_template('Patient_Dashboard.html', appointments=upcoming_appointments, history=patient_history)


if __name__ == '__main__':
    app.run(debug=True)