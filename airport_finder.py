import requests

url = "https://cometari-airportsfinder-v1.p.rapidapi.com/api/airports/by-text"

querystring = {"text":"detroit"}

headers = {
    'x-rapidapi-host': "cometari-airportsfinder-v1.p.rapidapi.com",
    'x-rapidapi-key': "83a69214c6msh70b62fd60e4fd1ep1a3f19jsn6b278bdadb79"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

