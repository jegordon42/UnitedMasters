from flask import Flask, request, json, render_template

app = Flask(__name__) 

@app.route("/") 
def index(): 
    return render_template('index.html')

@app.route("/shortenURL", methods = ['POST']) 
def shortenURL(): 
    urlToShorten = request.json['URL']
    
    #Get the count of how many URLs are stored on the client's browser as cookies
    countOfURLsGenerated = int(request.cookies.get('countOfURLsGenerated'))
    if not countOfURLsGenerated:
        countOfURLsGenerated = 0
    countOfURLsGenerated += 1

    #Use the count of Urls generated as an 'Unique Id'
    urlID = str(countOfURLsGenerated)

    #generate short URL
    shortenedURL = 'https://joe.com/' + urlID

    return json.dumps({'shortenedURL' : shortenedURL, 'countOfURLsGenerated' : countOfURLsGenerated})

@app.route("/getOriginalURL", methods = ['POST']) 
def getOriginalURL(): 
    shortenedURL = request.json['URL']
     
    urlID = shortenedURL[len('https://joe.com/'):]

    #get the URL from the client's browser (which we are using as a 'database')
    originalURL = request.cookies.get(urlID)

    #if the URL is found, send it back
    result = {}
    if originalURL:
        result['originalURL'] = originalURL

    return json.dumps(result)

if __name__ == '__main__': 
   app.run(host='0.0.0.0',port="8000",debug=True)