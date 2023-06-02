import requests

def main():
    people = requests.get('http://api.open-notify.org/astros.json')
    print(people.text)

if __name__ == "__main__":
    main()