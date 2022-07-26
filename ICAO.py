from csv import reader

class ICAO(object):
    def find_ICAO(str):
        with open('static\ICAO.csv' 'r', encoding="utf8") as read_obj:
            csv_reader = reader(read_obj)
            for row in csv_reader:
                if (row[0] in str):
                    return row[1]
