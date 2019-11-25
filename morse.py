from morse_dict import morsecode
import winsound
import time


def short_beep():
    frequency = 1500
    duration = 100
    winsound.Beep(frequency, duration)


def long_beep():
    frequency = 1500
    duration = 400
    winsound.Beep(frequency, duration)


def translate_to_morsecode(text):
    text = text.upper()
    output = str()
    for b in text:
        output = output + morsecode[(b)]
    return output


def sound_my_code(code, text):
    show_chars = str()
    print("Sounding: ",code)
    for (c, s) in zip(code, text):
        show_chars += s
        print(f"Sounded: {show_chars}", end='\r')
        if c == ".":
            short_beep()
        elif c == "-":
            long_beep()
        else:
            print(f"Non beep char: {s}")

        if s.isspace():
            time.sleep(3.0)


if __name__ == "__main__":
    is_running = True
    while is_running:
        print("Please select your option:")
        print("1) Morse")
        print("2) Continous SOS")
        print("3) Exit")
        select = input(">")
        if select == '1':
            typed = input("Enter text to morse: ")
            code = translate_to_morsecode(typed.strip())
            sound_my_code(code, typed)
        elif select == '2':
            while 1:
                sound_my_code(translate_to_morsecode("SOS"))
                time.sleep(1.0)
        elif select == '3':
            is_running = False
        else:
            print("Invalid selection!")
