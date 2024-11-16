import requests

apiurl = "https://commonchemistry.cas.org/api"

def search_compounds(self, query):
    """Search compounds by name, CAS RN, or molecular formula."""
    try:
        response = requests.get(f"{apiurl}/search?q={query}")
        if response.status_code == 200:
            results = response.json()
            if results:
                return results
            else:
                return "No results found."
        else:
            return f"Error: Unable to fetch data. Status Code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"

def get_compound_details(self, cas_rn):
    """Get detailed information about a compound."""
    try:
        response = requests.get(f"{apiurl}/detail?rn={cas_rn}")
        if response.status_code == 200:
            details = response.json()
            return details
        else:
            return f"Error: Unable to fetch data. Status Code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    search_compounds(self, query)
    get_compound_details(self, cas_rn)

    if __name__ == '__main__':
        main()