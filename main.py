from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- PAGE ROUTES ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('abouts.html')

@app.route('/tech-lab')
def tech_lab():
    return render_template('tech-lab.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/opportunities')
def opportunities():
    return render_template('opportunities-hub.html')

@app.route('/initiatives/girls')
def anthoninah():
    return render_template('anthoninas-initiative.html')

@app.route('/initiatives/men')
def wilson():
    return render_template('wilsons-initiative.html')

@app.route('/tutor')
def tutor():
    return render_template('tutor.html')

@app.route('/support')
def support():
    return render_template('support-us.html')

# --- FORM HANDLING ---

@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    if request.method == 'POST':
        # Retrieve data from the form fields in enroll.html
        name = request.form.get('name')
        email = request.form.get('email')
        initiative = request.form.get('initiative')
        
        # For now, we print to the console to verify it works
        print(f"--- NEW ENROLLMENT ---")
        print(f"Student: {name}\nEmail: {email}\nProgram: {initiative}")
        
        # Redirect to a success page or back home
        return "<h1>Enrollment Successful!</h1><p>We will contact you soon.</p><a href='/'>Return Home</a>"
    
    return render_template('enroll.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        print(f"MESSAGE FROM {name}: {message}")
        return redirect(url_for('index'))
    return render_template('contactus.html')

# --- ERROR HANDLING ---
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The UEFI Lab hasn't built this room yet.</p>", 404

if __name__ == '__main__':
    # debug=True automatically restarts the server when you save changes
    app.run(debug=True, port=5000)