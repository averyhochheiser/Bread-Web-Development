from website import create_app # can do this bc website is python package (__init__), importing runs all data in __init__.py

app = create_app()

if __name__ == '__main__': # only execute next line if we run the file, not if we import
    app.run(debug=True)


