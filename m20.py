import requests
a = requests.get("https://mymodernmet.com/wp/wp-content/uploads/2021/11/cute-white-duck-runs-2021-new-york-city-marathon-1.gif")
file = open ("duck.png" ,"wb")
file.write(a.content)
file.close()

