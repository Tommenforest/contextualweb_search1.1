import requests #install from: http://docs.python-requests.org/en/master/

#Replace the following string value with your valid X-RapidAPI-Key.
Your_X_RapidAPI_Key = "fef48cce55mshe64593c6f6cb9d1p1e432fjsn524369dee2a4";

#The query parameters: (update according to your search query)
q = "Trump%20foreign%20policy" #the search query
fromPublishDate = "01062016"
toPublishDate = "01082018"
pageNumber = 2 #the number of requested page
pageSize = 20 #the size of a page
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



    #An example: Output the webpage url, title and published date:
    lasti = ("Url: %s. Title: %s. Published Date:%s." % (url, title, datePublished))
    print(lasti)
    file = open("tiedosto2.json", "a")
    file.write(str(lasti))
    file.close()