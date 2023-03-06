import random 

random_number = random.randint(1, 100) # 1과 100 사이의 정수값 반환

game_count = 1

while True:
    try:
        my_number = int(input("1~100 사이의 숫자를 입력하세요 : "))

        if my_number > random_number:
            print("Down")
        elif my_number < random_number:
            print("Up")
        elif my_number == random_number:
            print(f"Congratulation! {game_count} Tried.")
            break
        game_count += 1
    except:
        print("Error! Try again")