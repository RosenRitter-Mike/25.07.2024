my_data: str = ("Michael Rozental Nof HaGalil");

print(f"Length of my str: {len(my_data)}");
print(f"Upper Case: {my_data.upper()}");
print(f"Lower Case: {my_data.lower()}");

print(f"my str starts with Michael: {my_data.startswith('Michael')}");
print(f"my str ends with Nof HaGalil: {my_data.endswith('Nof HaGalil')}");

x: list[str] = my_data.split(" ");
x[2] += " " + x[3];
x.pop();
print(x);

new_data: str = my_data.replace(" ", "*");
print(new_data);
x: list[str] = new_data.split("*");
x[2] += " " + x[3];
x.pop();
print(x);

print(f"centred str: {my_data.center(50,'=')}");
print(f"my str[3::]: {my_data[3::]}");
print(f"my str[:4:]: {my_data[:4:]}");
print(f"my str[1::2]: {my_data[1::2]}");

my_data = my_data.title();
print(f"my_data.title(): {my_data}");
