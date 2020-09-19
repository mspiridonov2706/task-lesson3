import csv
from collections import Counter

def main():
    street = []
    with open('bus_stop.csv', 'r', encoding='cp1251') as f:

        reader = csv.DictReader(f, delimiter=';')

        for row in reader:
            street.append(row["Street"])
    
    most_common_street = Counter(street).most_common(2)
    list_street = most_common_street[1]
    list_street = list(list_street)

    print(f'Улица "{list_street[0]}" встречается {list_street[1]} раз')

if __name__ == "__main__":
    main()
