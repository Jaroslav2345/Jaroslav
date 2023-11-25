import requests
import streamlit as st

def get_all_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1000"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemon_list = data["results"]
        jmena_pokemonu = []
        for pokemon in pokemon_list:
            jmena_pokemonu.append(pokemon["name"].capitalize())
        
        return jmena_pokemonu
    else:
        st.error(f"Chyba {response.status_code}: {response.text}")
        return None
    
st.title("Pokemon API")
pokemon_names = get_all_pokemon()

with st.form("formular"):
    pokemon_name = st.selectbox("Zadejte jméno", pokemon_names)
    tlacitko = st.form_submit_button("Hledej")
if tlacitko:
    pokemon_name = pokemon_name.lower() 
    url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    odpoved = requests.get(url_pokemon)
    odpoved_json = odpoved.json()
    
    adresa_obrazku = odpoved_json["sprites"]["other"]["official-artwork"]["front_default"]

    
    st.image(adresa_obrazku, width=400)










