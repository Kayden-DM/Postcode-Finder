import requests


def get_postcode():
    postcode = input("Enter a post code in the UK: ").upper().strip()
    return postcode


def postcode_data(postcode):
    clean = postcode.replace(" ", "")
    url = f"https://api.postcodes.io/postcodes/{clean}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException:
        print("API not found.")
        return None

    if data.get("status") != 200:
        print(f"{postcode} not found.")
        return None

    return data.get("result", {})


def display_result(result):
    print("=====POSTCODE INFO=====")
    print(f"Postcode:  {result.get('postcode', 'N/A')}")
    print(f"Country:   {result.get('country', 'N/A')}")
    print(f"Region:    {result.get('region', 'N/A')}")
    print(f"Latitude:  {result.get('latitude', 'N/A')}")
    print(f"Longitude: {result.get('longitude', 'N/A')}")


def main():
    print("=====POSTCODE INFO FINDER=====")
    print("Look up any postcode to find out information about it.")

    while True:
        postcode = get_postcode()
        result = postcode_data(postcode)
        if result:
            display_result(result)
            break
        else:
            print("Try entering the postcode again.\n")

    again = input("Would you like to search up more postcodes? (y/n) ").lower().strip()
    if again == "y":
        main()
    elif again == "n":
        exit()
    else:
        print("Try again. ")
        return again

if __name__ == "__main__":
    main()