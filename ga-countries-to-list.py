import csv

# curl 'https://gitlab.com/flaxandteal/inward-map/-/raw/master/public/countries-ga-url.csv'

def run():
    with open("countries-ga-url.csv", "r") as f:
        rows = csv.reader(f, delimiter=",")
        next(rows)
        for row in rows:
            print(row)

if __name__ == "__main__":
    run()
