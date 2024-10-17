#check if the library requests and bs4 are installed
try:
    import requests
    from bs4 import BeautifulSoup
    
except ImportError:
    #if not, install it
    import os
    os.system("pip install requests beautifulsoup4")
    import requests
    from bs4 import BeautifulSoup
    

def dollar_A_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["euro", "dollar A", "dollar C", "livre", "yen"]:
        raise ValueError("L'unité doit être 'euro', 'dollar A','dollar C', 'livre', 'yen'")

    case = {
        "euro": value * 0.92,
        "dollar A": value,
        "dollar C": value * 1.38,
        "livre": value * 0.76,
        "yen": value * 149.24,
    }

    return case[unit]


def euro_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["euro", "dollar A", "dollar C", "livre", "yen"]:
        raise ValueError("L'unité doit être 'euro', 'dollar A','dollar C', 'livre', 'yen'")
    
    dollar_A = 1.09

    case = {
        "euro": value,
        "dollar A": value * dollar_A,
        "dollar C": dollar_A_to(unit="dollar C", value=value * dollar_A),
        "livre": dollar_A_to(unit="livre", value=value * dollar_A),
        "yen": dollar_A_to(unit="yen", value=value * dollar_A),
    }

    return case[unit]

def dollar_C_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["euro", "dollar A", "dollar C", "livre", "yen"]:
        raise ValueError("L'unité doit être 'euro', 'dollar A','dollar C', 'livre', 'yen'")
    
    dollar_A = 0.72

    case = {
        "euro": dollar_A_to(unit="euro", value=value * dollar_A),
        "dollar A": value * dollar_A,
        "dollar C": value,
        "livre": dollar_A_to(unit="livre", value=value * dollar_A),
        "yen": dollar_A_to(unit="yen", value=value * dollar_A),
    }

    return case[unit]

def livre_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["euro", "dollar A", "dollar C", "livre", "yen"]:
        raise ValueError("L'unité doit être 'euro', 'dollar A','dollar C', 'livre', 'yen'")
    
    dollar_A = 1.31

    case = {
        "euro": dollar_A_to(unit="euro", value=value * dollar_A),
        "dollar A": value * dollar_A,
        "dollar C": dollar_A_to(unit="dollar C", value=value * dollar_A),
        "livre": value,
        "yen": dollar_A_to(unit="yen", value=value * dollar_A),
    }

    return case[unit]

def yen_to(*, unit, value):
    if not isinstance(value, (int, float)):
        raise TypeError("La valeur doit être un nombre")
    if value < 0:
        raise ValueError("La valeur ne peut pas être négative")
    if unit not in ["euro", "dollar A", "dollar C", "livre", "yen"]:
        raise ValueError("L'unité doit être 'euro', 'dollar A','dollar C', 'livre', 'yen'")
    
    Yens = 1000 #pour avoir un truc cohérent
    dollar_A = 6.71

    case = {
        "euro": dollar_A_to(unit="euro", value=value/Yens * dollar_A),
        "dollar A": value/Yens * dollar_A,
        "dollar C": dollar_A_to(unit="dollar C", value=value/Yens * dollar_A),
        "livre": dollar_A_to(unit="livre", value=value/Yens * dollar_A),
        "yen": value,
    }

    return case[unit]


def get_exchange_rate():
    precisions = 100000000

    url = "https://www.google.com/search?q="+str(precisions)+"EUR+to+USD"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        #raise SystemExit(err)
        print("Http Error, try again later")

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the exchange rate value on the Google search results page
    rate = soup.find("span", class_="DFlfde SwHCTb").text
    #print(rate) #10\u202f912\u202f500,00
    rate = rate.replace("\u202f", "")
    rate = rate.replace(",", ".")
    rate = rate.replace(" ", "")

    return float(rate)/precisions



if __name__=="__main__":
    import math
    assert dollar_A_to(unit="euro", value=1) == 0.92
    assert dollar_A_to(unit="dollar A", value=1) == 1
    assert dollar_A_to(unit="dollar C", value=1) == 1.38
    assert dollar_A_to(unit="livre", value=1) == 0.76
    assert dollar_A_to(unit="yen", value=1) == 149.24

    assert euro_to(unit="euro", value=1) == 1
    assert euro_to(unit="dollar A", value=1) == 1.09
    assert math.isclose(euro_to(unit="dollar C", value=1), 1.51, rel_tol=1e-2)
    assert math.isclose(euro_to(unit="livre", value=1), 0.83, rel_tol=1e-2)
    assert math.isclose(euro_to(unit="yen", value=1), 162.80, rel_tol=1e-2)

    assert math.isclose(dollar_C_to(unit="euro", value=1), 0.66, rel_tol=1e-2)
    assert dollar_C_to(unit="dollar A", value=1) == 0.72
    assert dollar_C_to(unit="dollar C", value=1) == 1
    assert math.isclose(dollar_C_to(unit="livre", value=1), 0.55, rel_tol=1e-2)
    assert math.isclose(dollar_C_to(unit="yen", value=1), 108.33, rel_tol=1e-2)

    assert math.isclose(livre_to(unit="euro", value=1), 1.20, rel_tol=1e-2)
    assert livre_to(unit="dollar A", value=1) == 1.31
    assert math.isclose(livre_to(unit="dollar C", value=1), 1.81, rel_tol=1e-2)
    assert livre_to(unit="livre", value=1) == 1
    assert math.isclose(livre_to(unit="yen", value=1), 195.10, rel_tol=1e-2)

    assert math.isclose(yen_to(unit="euro", value=1000), 6.14, rel_tol=1e-2)
    assert yen_to(unit="dollar A", value=1000) == 6.71
    assert math.isclose(yen_to(unit="dollar C", value=1000), 9.27, rel_tol=1e-2)
    assert math.isclose(yen_to(unit="livre", value=1000), 5.13, rel_tol=1e-2)
    assert yen_to(unit="yen", value=1000) == 1000

    print("All tests passed")

    #print(get_exchange_rate())

    


