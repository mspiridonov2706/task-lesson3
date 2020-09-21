import csv
from datetime import datetime

def main():
    dict_1 = {"name": '', "RepairOfEscalators": '' }
    dt_now = datetime.now()
    with open('metro_station.csv', 'r', encoding='cp1251') as f:

        reader = csv.DictReader(f, delimiter=';')
        date_esc = []
        for row in reader:
            if row["RepairOfEscalators"] == '':
                continue
            else:
                #print(f'{row["ID"]}\t{row["Name"]}\t{row["RepairOfEscalators"]}')
                dict_1['name'] = row['Name']
                dict_1['RepairOfEscalators'] = row['RepairOfEscalators']
                #print(dict_1)
        #print(dict_1)
                date = dict_1['RepairOfEscalators'].split('-')
                #print(date)
                for date_str in date:
                    if ';' in date_str:
                        date_str_2 = date_str.split(';')
                        for x in date_str_2:
                            date_dt_2 = datetime.strptime(x, '%d.%m.%Y')
                            if dt_now < date_dt_2:
                                print(date_dt_2)
                            else:
                                continue
                        continue
                    date_dt = datetime.strptime(date_str, '%d.%m.%Y')
                    if dt_now < date_dt:
                        print(f'В настоящее время на станции "{dict_1["name"]}" проходит ремонт эскалатора')
                    else:
                        continue              

if __name__ == "__main__":
    main()
