'''
Програма радить, що робити далі. 
Вона може надрукувати один з трьох рядків - "Вчитися!", "Грати!", "Гуляти!", 
Запитуючи, чи зроблені уроки і гарна погода.


Напишіть програму: спочатку задається питання, чи зроблені уроки. 
Якщо відповідь "так", то програма запитує, чи гарна погода. 
Якщо на питання про уроки ми отримали відповідь "ні", потрібно надрукувати "Вчитися!". 
Якщо на питання про хорошу погоду отримана відповідь "так", програма друкує "Гуляти!",
Інакше (значить, погода погана) - друкує "Грати!".
'''
homework_done = input("Чи зроблені уроки? (так/ні): ")

if homework_done.lower() == "так":
    good_weather = input("Чи гарна погода? (так/ні): ")
    
    if good_weather.lower() == "так":
        print("Гуляти!")
    else:
        print("Грати!")
else:
    print("Вчитися!")
