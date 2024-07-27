str1: str = " fun-day ";
print(f"string.strip(): {str1.strip()}");

str2: str = "hello";
print(f"str.isalpha(): {str2.isalpha()}");

str3: str = "777";
print(f"str.isdigit(): {str3.isdigit()}");

str4: str = "   ";
print(f"str.isspace(): {str4.isspace()}");

char_l: list[str] = ['N', 'I', 'N', 'J', 'A'];
str5: str = ''.join(char_l);
print(str5);

str6: str = '*'.join(char_l);
print(str6);

str7: str = "hELLo";
print(f"is e present in hELLo? {'e' in str7.lower()}");

my_word: str = input("Input a word: ");
w_list: list[str] = [c.upper() for c in my_word if c.isalpha()];
print(w_list);