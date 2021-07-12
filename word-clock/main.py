def clear_screen():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def time_in_words(hours, minutes): 
    words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'ninteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23: 'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine'}

    quarters = {0: f"{words[hours]} o' clock", 15: f"quarter past {words[hours]}", 30: f"half past {words[hours]}", 45: f"quarter to {words[hours+1]}"}

    if (minutes % 15) == 0:
        return quarters[minutes]
    elif minutes < 30:
        return f"{words[minutes]} minute{'s' * (minutes != 1)} past {words[hours]}"
    else: 
        minutes = 60 - minutes
        return f"{words[minutes]} minute{'s' * (minutes != 1)} to {words[hours+1]}"

if __name__ == "__main__":
    clear_screen()

    print("Let's convert you time into words!\n")
    print("Enter hours and minutes (seperated by space).")
    print("When you're done, press Enter [↵].\n")

    while True:
        input_time = input("> ").strip()
        try:
            hours, minutes = [int(n) for n in input_time.split()]
        except:
            print()
            break
        print(time_in_words(hours, minutes))
