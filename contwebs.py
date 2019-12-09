import requests

url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI"

querystring = {"autoCorrect":"false","pageNumber":"1","pageSize":"10","q":"Taylor Swift","safeSearch":"false"}

headers = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "fef48cce55mshe64593c6f6cb9d1p1e432fjsn524369dee2a4"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)