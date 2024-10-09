from __init__ import create_app
from views import views

app = create_app()
app.register_blueprint(views)

if __name__ == '__main__':
    app.run(debug=True) 