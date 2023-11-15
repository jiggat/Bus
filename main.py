import requests
from bs4 import BeautifulSoup

def scrape_bus_info(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements with class "single-visit__name"
        bus_name_elements = soup.find_all('p', class_='single-visit__name')[:5]

        # Find all elements with class "single-visit__description"
        description_elements = soup.find_all('p', class_='single-visit__description')[:5]

        # Find all elements with class "single-visit__time--expected"
        time_elements = soup.find_all('div', class_='single-visit__time single-visit__time--expected')[:5]

        # Check if the number of elements is the same for Bus Names, Descriptions, and Times
        if len(bus_name_elements) == len(description_elements) == len(time_elements):
            # Loop through each element and print the information
            for i in range(len(bus_name_elements)):
                bus_name = bus_name_elements[i].text.strip()
                description = description_elements[i].text.strip()
                departure_time = time_elements[i].text.strip()

                print(f"--------------\n[{bus_name}] -> [{description}] \n[{departure_time}]\n---------------")
        else:

            print("Number of elements for Bus Names, Descriptions, and Times is not consistent.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


url = 'https://www.morebus.co.uk/stops/1290DOB21073'


Run_code = input("""

-v0.1 J.G
 __ __    ___  ____   ___   ____          __   ___   __ __  ____  ______      ____   ___   
|  |  |  /  _]|    \ /   \ |    \        /  ] /   \ |  |  ||    \|      |    |    \ |   \  
|  |  | /  [_ |  D  )     ||  _  |      /  / |     ||  |  ||  D  )      |    |  D  )|    \ 
|  _  ||    _]|    /|  O  ||  |  |     /  /  |  O  ||  |  ||    /|_|  |_|    |    / |  D  |
|  |  ||   [_ |    \|     ||  |  |    /   \_ |     ||  :  ||    \  |  |      |    \ |     |
|  |  ||     ||  .  \     ||  |  |    \     ||     ||     ||  .  \ |  |      |  .  \|     |
|__|__||_____||__|\_|\___/ |__|__|     \____| \___/  \__,_||__|\_| |__|      |__|\_||_____|
                                                                                          
1. View times                                                       3. Change Bus stop 
2. Exit    

===> """)

if Run_code == "1":
   scrape_bus_info(url)

elif Run_code == '3':
    print("under Construction")

else:
    pass


