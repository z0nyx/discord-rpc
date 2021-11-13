from pypresence import Presence
 
RPC = Presence("") #id application
btns = [
    {
        "label": "",  #название кнопки 
        "url": "" #ссылка
    },
    {
        "label": "", #название кнопки 
        "url": "" #ссылка
    }
]

RPC.connect()
RPC.update(
    state="", #самый нижний текст
    details="", #второй поле с текстом (под названием игры)
    buttons=btns,
    large_image="1", #название большого изображения 
    small_image="2", #название маленького изображения
    large_text="", #текст большой картинки (при наведении)
    small_text="" #текст маленькой картинки (при наведении)
)
input()