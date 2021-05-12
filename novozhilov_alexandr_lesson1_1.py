duration = int(input("Введите длительность в секундах: "))

if duration >= 86_400:
    secs = duration % 60
    minutes = duration % 3_600 // 60
    hours = duration % 86_400 // 3600
    days = duration // 86_400
    print("В введённом вами количестве секунд ", days, " день(ей), ", hours, " час(ов) ", minutes, " минут(ы) и ", secs, " секунд(ы).")

elif duration >= 3600:
    secs = duration % 60
    minutes = duration % 3_600 // 60
    hours = duration // 3600
    print("В введённом вами количестве секунд ", hours, " час(ов) ", minutes, " минут(ы) и ", secs, " секунд(ы).")

elif duration >= 60:
    minutes = duration // 60
    secs = duration % 60
    print("В введённом вами количестве секунд ", minutes, " минут(ы) и ", secs, " секунд(ы).")

else:
    print("В введёном вами количестве всего лишь ", duration, " секунд(ы).")
