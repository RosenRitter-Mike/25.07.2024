import random as rd

capital_list: list[str] = [
    'Kabul', 'Tirana', 'Algiers', 'Andorra la Vella', 'Luanda', 'Saint John\'s', 'Buenos Aires', 'Yerevan',
    'Canberra', 'Vienna', 'Baku', 'Nassau', 'Manama', 'Dhaka', 'Bridgetown', 'Minsk', 'Brussels', 'Belmopan',
    'Porto-Novo', 'Thimphu', 'Sucre', 'Sarajevo', 'Gaborone', 'Brasília', 'Bandar Seri Begawan', 'Sofia',
    'Ouagadougou', 'Gitega', 'Praia', 'Phnom Penh', 'Yaoundé', 'Ottawa', 'Bangui', 'N\'Djamena', 'Santiago',
    'Beijing', 'Bogotá', 'Moroni', 'Brazzaville', 'Kinshasa', 'San José', 'Zagreb', 'Havana', 'Nicosia',
    'Prague', 'Copenhagen', 'Djibouti', 'Roseau', 'Santo Domingo', 'Quito', 'Cairo', 'San Salvador', 'Malabo',
    'Asmara', 'Tallinn', 'Mbabane', 'Addis Ababa', 'Palikir', 'Suva', 'Helsinki', 'Paris', 'Libreville',
    'Banjul', 'Tbilisi', 'Berlin', 'Accra', 'Athens', 'Saint George\'s', 'Guatemala City', 'Conakry', 'Bissau',
    'Georgetown', 'Port-au-Prince', 'Tegucigalpa', 'Budapest', 'Reykjavík', 'New Delhi', 'Jakarta',
    'Baghdad', 'Dublin', 'Jerusalem', 'Rome', 'Kingston', 'Tokyo', 'Amman', 'Nur-Sultan', 'Nairobi', 'Tarawa',
    'Pyongyang', 'Seoul', 'Kuwait City', 'Bishkek', 'Vientiane', 'Riga', 'Beirut', 'Maseru', 'Monrovia', 'Tripoli',
    'Vaduz', 'Vilnius', 'Luxembourg', 'Antananarivo', 'Lilongwe', 'Kuala Lumpur', 'Malé', 'Bamako', 'Valletta',
    'Majuro', 'Nouakchott', 'Port Louis', 'Mexico City', 'Palau', 'Chisinau', 'Monaco', 'Ulaanbaatar', 'Podgorica',
    'Rabat', 'Maputo', 'Naypyidaw', 'Windhoek', 'Yaren', 'Kathmandu', 'Amsterdam', 'Wellington', 'Managua',
    'Niamey', 'Abuja', 'Skopje', 'Oslo', 'Muscat', 'Islamabad', 'Ngerulmud', 'Panama City', 'Port Moresby',
    'Asunción', 'Lima', 'Manila', 'Warsaw', 'Lisbon', 'Doha', 'Bucharest', 'Moscow', 'Kigali', 'Basseterre',
    'Castries', 'Kingstown', 'Apia', 'San Marino', 'São Tomé', 'Riyadh', 'Dakar', 'Belgrade', 'Victoria',
    'Freetown', 'Singapore', 'Bratislava', 'Ljubljana', 'Honiara', 'Mogadishu', 'Pretoria', 'Juba', 'Madrid',
    'Colombo', 'Khartoum', 'Paramaribo', 'Stockholm', 'Bern', 'Damascus', 'Taipei', 'Dushanbe', 'Dodoma',
    'Bangkok', 'Lomé', 'Nukuʻalofa', 'Port of Spain', 'Tunis', 'Ankara', 'Ashgabat', 'Funafuti', 'Kampala',
    'Kyiv', 'Abu Dhabi', 'London', 'Washington, D.C.', 'Montevideo', 'Tashkent', 'Port Vila', 'Vatican City',
    'Caracas', 'Hanoi', 'Sanaa', 'Lusaka', 'Harare'
]

answer: str = rd.choice(capital_list);
guess: str = "";
g_num: int = 0;

for _ in range(len(answer)):
    guess += "_";

guess_b: list[str] = [c for c in guess];

while guess != answer:
    letter: str = input("Guess a letter: ");
    if letter.isdigit() or len(letter) > 1:
        print(f"{letter} is not a valid letter, it will not be counted as a guess, guess again!!")
    else:
        g_num += 1;

        for i in range(len(answer)):
            if letter == answer[i].lower() or letter == answer[i].upper():
                guess_b[i] = answer[i];

        guess = ''.join(guess_b);
        print(guess);

print(f"great work! you have guessed the city {answer} in {g_num} guesses!")
