# import the create_app function
from website import create_app

# run create app function as main

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
