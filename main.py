phanthoms = {
    "Joker": {
        "name": "Ren Amamiya",
        "age": 17,
        "arcana": "Fool",
        "persona": "Arsène"
    },
    "Mona": {
        "name": "Morgana",
        "age": "???",
        "arcana": "Magician",
        "persona": "Zorro"
    },
    "Skull": {
        "name": "Ryuji Sakamoto",
        "age": 17,
        "arcana": "Chariot",
        "persona": "Captain Kidd"
    },
}


print("Informations about the Phanthom Thieves of Hearts...")
for phanthoms, data in phanthoms.items():
    for key, value in data.items():
        print(f" {key}: {value}")