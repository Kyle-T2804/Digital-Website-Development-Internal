# import the create_app function
from website import create_app

# run create app function as main

if __name__ == "__main__":
    app = create_app()
    app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB
    app.run(debug=True)
