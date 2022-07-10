import json

# curl -H "Accept: application/json" -H "Content-Type: application/json" -o wikt-irish-prefixes.json 'https://en.wiktionary.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Irish_prefixes&cmprop=title&format=json'

def run():
    with open("wikt-irish-prefixes.json", "r") as f:
        pref = json.load(f)
    with open("wikt-irish-prefixes.txt", "w") as f:
        for prefix in pref["query"]["categorymembers"]:
            if prefix["ns"] == 0:
                f.write(f"{prefix['title'].replace('-', '')}\n")
        # Seemingly FGB and Wikt only list ur- as a prefix
        # but not úr, even thought they list úrscéal, etc.
        # similarly bonn vs bun, and oir vs iar
        f.write("úr\n")
        f.write("bonn\n")
        f.write("oir\n")
        # Common compound word starters
        f.write("croí\n")
        f.write("lámh\n")
        f.write("teang\n")
        f.write("sráid\n")
        f.write("tráth\n")
        f.write("céad\n")
        # FGB has these
        f.write("leith\n")
        f.write("rí\n")
        # This seems to only be the long form
        f.write("gear\n")

if __name__ == "__main__":
    run()
