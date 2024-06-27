from app import create_app
from app.views import bp as main_bp

app = create_app()
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
