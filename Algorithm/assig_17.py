import random


def up_down_game():
    number_to_guess = random.randint(1, 1000000)
    attempts = 0
    low, high = 1, 1000000

    print("컴퓨터가 1부터 100 사이의 숫자를 맞춰봅니다.")

    while True:
        guess = (low + high) // 2
        attempts += 1
        print(f"컴퓨터의 추측: {guess}")

        if guess < number_to_guess:
            print("업!")
            low = guess + 1
        elif guess > number_to_guess:
            print("다운!")
            high = guess - 1
        else:
            print(f"맞췄습니다! 숫자는 {guess}였습니다. 시도 횟수: {attempts}")
            break


if __name__ == "__main__":
    up_down_game()
