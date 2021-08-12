import requests

TOKKEN_ID = "cd6626556f5d2d363f47d58897b01737"  
URL_BASE = "http://api.openweathermap.org/data/2.5/weather"


def input_city():
    return input("Write city: ")


def send_req_openweather(city):
    params = { 
       "q": city,
        "units": "metric", 
        "appid": TOKKEN_ID 
    }

    return requests.get(URL_BASE, params) 


def make_result_text(resp_openweather, city):
    resp_openweather_json = resp_openweather.json()
    main_data = resp_openweather_json.get("main") 
   
    result_text = f"Now the temperature in {city} is {main_data.get('temp')} degrees C \n"
    result_text += f"Today the temperature ranges from {main_data.get('temp_min')} to {main_data.get('temp_max')} C"
    
    return result_text


def write_in_file(result_text): 
    file = open('test_weather.txt', 'w')
    file.write(result_text)
    file.close()


if __name__ == "__main__": 
    city = input_city()
    resp_openweather = send_req_openweather(city)
    result_text = make_result_text(resp_openweather, city)
    write_in_file(result_text)
