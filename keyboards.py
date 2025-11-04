from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

def webAppKeyboard():
    web_app_info = WebAppInfo(url="https://stably-aboveboard-vireo.cloudpub.ru/")
    web_app_button = KeyboardButton(text="Запуск приложения", web_app=web_app_info)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[web_app_button]],  
        resize_keyboard=True,        
        one_time_keyboard=True       
    )

    return keyboard