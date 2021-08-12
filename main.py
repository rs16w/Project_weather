import requests

# Вот эти secrets лучше хранить в переменных окружения или в Config накрайняк
TOKKEN_ID = "cd6626556f5d2d363f47d58897b01737"
URL_BASE = "http://api.openweathermap.org/data/2.5/weather"


# Лучше писать пример для пользователя, аля "Write city (example: Moscow): "
# Название метода лучше: get_input_city()
def get_input_city():
    return input("Write city: ")


# В современном Python очень рекомендуется использовать указание типизации
def send_req_openweather(search_city: str) -> dict:
    params: dict = {
        "q": search_city,
        "units": "metric",
        "appid": TOKKEN_ID
    }

    return requests.get(URL_BASE, params).json()


def generate_text_for_log(response: dict, search_city: str) -> str:
    main_data: dict = response.get("main", "")
    # Лучше вот эти получатели данных `main_data.get('temp', '')` в переменные сохранять

    result: str = f"Now the temperature in {search_city} is {main_data.get('temp', '')} degrees C \n"
    result += f"Today the temperature ranges from " \
              f"{main_data.get('temp_min', '')} to {main_data.get('temp_max', '')} C "

    return result


# Через with безопасней и кода меньше
def write_in_file(text: str):
    with open('test_weather.txt', 'w') as file:
        file.write(text)


if __name__ == "__main__":
    city: str = get_input_city()
    resp: dict = send_req_openweather(search_city=city)
    result: str = generate_text_for_log(response=resp, search_city=city)
    write_in_file(text=result)
