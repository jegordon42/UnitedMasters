# Welcome To Joe's URL Shortener and thank you for considering me for your team!

This is a fully operational flask web app that utilizes jinja to render a web page.

In order to shorten a URL and then restore it back to it's original,
we have to generate a unique identifier for the URL and create a key value pair, 
where the key is the unique identifier and the value is the original URL.
We then have to store the key value pair somewhere so we can retrieve the original
at a later time. 

Gaps/Things to Improve:
1. I use the client's cookies to store the URLs when it should be a database. 
2. I use a counter to generate an identifier when it should be a hash function based on the original URL.

I spent about 2 hours creating this.

# Running the Web App
Prerequisite: Python3 is installed (I havent tested this with another version)

1. Open the UnitedMasters directory in your command prompt
2. Run the following command: Pip3 install -r requirements.txt
3. Run the following command: Python3 app.py
4. Open the following URL in your browser: localhost:8000/
