import random

# مقدمه بازی
print("به بازی ماجراجویی مبتنی بر متن خوش آمدید!")
print("شما در وسط یک جنگل ایستاده‌اید. دو مسیر پیش روی شماست: یکی به سمت چپ و دیگری به سمت راست.")
health = 100  # مقدار اولیه سلامتی کاربر

# گرفتن انتخاب کاربر
choice = input("آیا می‌خواهید به چپ بروید یا به راست؟ (چپ/راست) ")

# منطق شرطی برای پیگیری انتخاب کاربر
if choice == "چپ":
    print("شما به سمت چپ رفتید و به یک خانه قدیمی رسیدید. در خانه باز است.")
    choice2 = input("آیا می‌خواهید وارد خانه شوید؟ (بله/خیر) ")
    if choice2 == "بله":
        # اضافه کردن یک اتفاق تصادفی
        if random.randint(1, 2) == 1:
            print("در داخل خانه، یک تله وجود داشت! سلامتی شما کاهش یافت.")
            health -= 30
            print(f"سلامتی شما: {health}")
        else:
            print("شما یک گنج پیدا کردید و یک کیت کمک‌های اولیه! سلامتی شما افزایش یافت.")
            health += 20
            print(f"سلامتی شما: {health}")
    else:
        print("یک طوفان شروع شد و شما آسیب دیدید.")
        health -= 40
        print(f"سلامتی شما: {health}")

elif choice == "راست":
    print("شما به سمت راست رفتید و با یک خرس برخورد کردید!")
    choice2 = input("آیا می‌خواهید با خرس بجنگید؟ (بله/خیر) ")
    if choice2 == "بله":
        print("خرس خیلی قوی بود و شما شکست خوردید، اما توانستید فرار کنید.")
        health -= 50
        print(f"سلامتی شما: {health}")
    else:
        print("شما با احتیاط فرار کردید و به امان برسید.")
else:
    print("انتخاب نامعتبر. لطفا فقط 'چپ' یا 'راست' را وارد کنید.")

# افزودن پایان بازی بر اساس سلامتی
if health <= 0:
    print("شما به شدت آسیب دیده‌اید و نمی‌توانید ادامه دهید. بازی تمام شد.")
else:
    print("ماجراجویی شما ادامه دارد...")

print("متشکریم که بازی ما را امتحان کردید!")