import requests

apiurl = "https://commonchemistry.cas.org/api"

def search_compounds(query, page=1):
    """Search compounds by name, CAS RN, or molecular formula."""
    try:
        response = requests.get(f"{apiurl}/search?q={query}&page={page}")
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

def get_compound_details(cas_rn):
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
    search_compounds(query)
    get_compound_details(cas_rn)

if __name__ == '__main__':
    main()