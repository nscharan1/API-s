import requests

print("Please enter your Origin and Destination ?")
userinput1=input("Enter your Origin: ");
userinput2=input("Enter your Destination: ");

url = "https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v1/prices/cheap"

querystring = {"destination":userinput1,"origin":userinput2,"currency":"USD","page":"None"}

headers = {
    'x-rapidapi-host': "travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com",
    'x-rapidapi-key': "83a69214c6msh70b62fd60e4fd1ep1a3f19jsn6b278bdadb79",
    'x-access-token': "a4dd61ae0300a50da722075244ad7089"
    }

response = requests.get(url, headers=headers, params=querystring)


print(response.text)