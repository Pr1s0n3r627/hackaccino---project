#Enter modules
import requests
import csv
#Connector
class CSVConnector:
    def __init__(self, file_path):
        self.file_path = file_path
#Read data
    def read_data(self, state):
        """
        Read temperature, humidity, and wind speed data for a given state from the CSV file.
        
        Parameters:
        state (str): The name of the state.
        
        Returns:
        tuple: Three lists containing temperature, humidity, and wind speed data.
        """
#Defining work for variable
        lower_limit_temperature,upper_limit_temperature,lower_limit_humidity,upper_limit_humidity,ll_wind_speed,ul_wind_speed=0,0,0,0,0,0
#Defining work for reading data
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['State'] == state:
                    lower_limit_temperature= int(row['LLT'])
                    upper_limit_temperature = int(row['ULT'])
                    lower_limit_humidity = int(row['LLH'])
                    upper_limit_humidity = int(row['LLT'])
                    ll_wind_speed = int(row['LLW'])
                    ul_wind_speed = int(row['ULW'])
        
        if not lower_limit_humidity:
            return None, None, None
        else:
            return lower_limit_humidity, upper_limit_humidity, lower_limit_temperature, upper_limit_temperature,ll_wind_speed,ul_wind_speed
#Give recommandation
def redcon(file_path,state):
    crop = ""
    with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["State"]==state:
                    crop = row["Crop"]
    return crop
#Get user pH
def ph(area):
    d={"Rice":5.6,"Sugar Cane":5.5,"Oak":5.6,"Wasteland":5.5,"Forest":4.2,"Build-up":4.3,"Cotton":6.25,"Fruits":3.5,"Tea":7,"Vegetables":6.5,"Cashew":6.5,"Apples":6.5,"Rubber":5.25,"Soybean":6.5,"Wheat":6.5}
    ph = eval(input("Enter the pH level:"))
    field_type = input("Enter what the field is used for:")
    if ph > d[field_type] :
        if ph-d[field_type]>=1:
            print("You loose on more than '10%-50%' of your yield")
            print("You should use :- Ammonium sulfate , Elemental sulfur , 	Sulfur-coated urea , Aluminum.\n In the concentration of 75:150:75:15 per acre.")
            print("Ammonium sulfate = ", area*75 ," pounds.\n","Elemental sulfur = ", area*150 ," pounds.\n","sulfur-coated = ", area*75 ," pounds.\n","Aluminum = ", area*15 ," pounds.\n")
        else:
            print("You loose on more than '1%' of your yield")
            print("Just use organic matter and you are good to go.")
    elif d[field_type] > ph:
        if d[field_type]-ph >= 1:
            print("You loose on more than '10%-50%' of your yield")
            print("You should use :- Agricultural lime, Dolomitic lime, Wood ash, Gypsum, Calcium carbonate.\n In the concentration of 3000:3000:750:750:750 per acre.")
            print("Agricultural lime = ", area*3000 ," pounds.\n","Dolomitic lime = ", area*3000 ," pounds.\n","Wood ash = ", area*750 ," pounds.\n","Gypsum = ", area*750 ," pounds.\n","Calcium carbonate = ", area*750 ," pounds.\n")
        else:
            print("You loose on more than '1%' of your yield")
            print("Just use organic matter and you are good to go.")
    else:
        print("You have the perfect concentration for the soil.")
#Get weather function
def get_weather(api_key, state):
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={state}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_description = data['current']['weather_descriptions'][0]
        temperature = data['current']['temperature']
        humidity = data['current']['humidity']
        wind_speed = data['current']['wind_speed']
        return {
            'weather_description': weather_description,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed
        }
    else:
        return None
#Compare portion
def compare(weather_data, llh,llt,ulh,ult,ulw,llw):
    if int(weather_data['temperature']) > ult:
        print("You have to reduce temperature")
    elif int(weather_data["temperature"]) < llt:
        print("You have to increase temperature")
    elif int(weather_data["humidity"]) > ulh :
        print("You have to decrease humidity")
    elif int(weather_data["humidity"]) < llh:
        print("You have to increase the humidity")
    elif int(weather_data["wind_speed"]) > ulw:
        print("You have to decrease the wind pressure")
    elif int(weather_data["wind_speed"]) < llw:
        print("You have to increase the wind pressure")
    else:
        print("You have the prefect condition to have the best crops")
#Main entry of the file 
def main():
    file_path = 'Data.csv'  # Replace with the path to your CSV file
    connector = CSVConnector(file_path)

    state = input("Enter the state name: ")
    lower_limit_temperature,upper_limit_temperature,lower_limit_humidity,upper_limit_humidity,ll_wind_speed,ul_wind_speed = connector.read_data(state)

    area = eval(input("Enter the area of your field in acre"))
    ph(area)
    Best_crop = redcon(file_path,state)
    print("The best crop for you guys are: ",Best_crop)
    if lower_limit_humidity is None:
        print("No data found for the state.")
    api_key = '6f9c6496403400f57c4fded4f46cad0c'  # Replace 'YOUR_API_KEY' with your actual API key
    weather_data = get_weather(api_key, state)
    compare(weather_data, lower_limit_humidity, lower_limit_temperature, upper_limit_humidity, upper_limit_temperature, ul_wind_speed, ll_wind_speed)
#Enter the function
if __name__ == "__main__":
    main()
