import requests #install from: http://docs.python-requests.org/en/master/

#Replace the following string value with your valid X-RapidAPI-Key.
Your_X_RapidAPI_Key = "fef48cce55mshe64593c6f6cb9d1p1e432fjsn524369dee2a4";

#The query parameters: (update according to your search query)
q = "Taylor%20Swift" #the search query
pageNumber = 1 #the number of requested page
pageSize = 10 #the size of a page
autoCorrect = True #autoCorrectspelling
safeSearch = False #filter results for adult content

response=requests.get("https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI?q={}&amp;pageNumber={}&amp;pageSize={}&amp;autocorrect={}&amp;safeSearch={}".format(q, pageNumber, pageSize, autoCorrect,safeSearch),
headers={
"X-RapidAPI-Key": "fef48cce55mshe64593c6f6cb9d1p1e432fjsn524369dee2a4"
}
).json()

#Get the numer of items returned
totalCount = response["totalCount"];

#Get the list of most frequent searches related to the input search query
relatedSearch = response["relatedSearch"]

#Go over each resulting item
for webPage in response["value"]:

#Get the web page metadata
    url = webPage["url"]
    title = webPage["title"]
    description = webPage["description"]
    keywords = webPage["keywords"]
    provider = webPage["provider"]["name"]
    datePublished = webPage["datePublished"]

    #Get the web page image (if exists)
    imageUrl = webPage["image"]["url"]
    imageHeight = webPage["image"]["height"]
    imageWidth = webPage["image"]["width"]

    thumbnail = webPage["image"]["thumbnail"]
    thumbnailHeight = webPage["image"]["thumbnailHeight"]
    thumbnailWidth = webPage["image"]["thumbnailWidth"]

    #An example: Output the webpage url, title and published date:
    print("Url: %s. Title: %s. Published Date:%s." % (url, title, datePublished))