
import sys

def divide_text_equally(text, n):
    return [text[i:i+n] for i in range(0, len(text), n)]

def main(text):
    for shift in range(8):
        print(f'Shift width: {shift}')
        text = text[shift:]
        for char_8byte in divide_text_equally(text, 8):
            acill_codes = divide_text_equally(char_8byte, 2)
            for code in acill_codes[::-1]:
                deci = int(code, 16)
                if 32 <= deci < 127:
                    print(chr(deci), end='')
                else:
                    print("_", end='')
        print()
        print()

if __name__ == '__main__':
    main(sys.argv[1])