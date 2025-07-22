from app import create_app

app = create_app()

if __name__ == '__main__':
    import os
    port = int(os.getenv("FLASK_PORT", 5050))
    app.run(host='0.0.0.0', port=port, debug=False)
