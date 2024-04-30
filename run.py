from app import create_app

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    # Run the Flask application with host set to '0.0.0.0'
    app.run(host='0.0.0.0', debug=True)
    