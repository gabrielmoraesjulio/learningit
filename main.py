phanthoms = {
    "Joker": {
        "name": "Ren Amamiya",
        "age": 17,
        "arcana": "Fool",
        "persona": {
            "name": "Arsène",
            "awaken": "Satanael"
        }
    },
    "Mona": {
        "name": "Morgana",
        "age": "???",
        "arcana": "Magician",
        "persona": {
            "name": "Zorro",
            "awaken": "Mercurius"
        }
    },
    "Skull": {
        "name": "Ryuji Sakamoto",
        "age": 17,
        "arcana": "Chariot",
        "persona": {
            "name": "Captain Kidd",
            "awaken": "Seiten Taisei"
        }
    },
    "Panther": {
        "name": "Anne Takamaki",
        "age": 17,
        "arcana": "Lovers",
        "persona": {
            "name": "Carmen",
            "awaken": "Hecate"
        }
    },
    "Fox": {
        "name": "Yusuke Kitagawa",
        "age": 17,
        "arcana": "Emperor",
        "persona": {
            "name": "Goemon",
            "awaken": "Kamu Susano-o"
        }
    },
    "Queen": {
        "name": "Makoto Niijima",
        "age": 17,
        "arcana": "Priestess",
        "persona": {
            "name": "Johanna",
            "awaken": "Anat"
        }
    },
    "Oracle": {
        "name": "Futaba Sakura",
        "age": 17,
        "arcana": "Hermit",
        "persona": {
            "name": "Necronomicon",
            "awaken": "Prometheus"
        }
    },
    "Noir": {
        "name": "Haru Okumura",
        "age": 17,
        "arcana": "Empress",
        "persona": {
            "name": "Milady",
            "awaken": "Astarte"
        }
    },
    "Crow": {
        "name": "Goro Akechi",
        "age": 17,
        "arcana": "Justice",
        "persona": {
            "name": "Loki",
            "awaken": "Hereward"
        }
    },
    "Violet": {
        "name": "Sumire Yoshizawa",
        "age": 15,
        "arcana": "Faith",
        "persona": {
            "name": "Cendrillon",
            "awaken": "Vanadis"
        }
    },
}


print("Informations about the Phanthom Thieves of Hearts...")
for phanthoms, data in phanthoms.items():
    print(phanthoms)
    for key, value in data.items():
        if isinstance(value, dict):
            print(f" {key}:")
            for persona_key, persona_value in value.items():
                print(f"    {persona_key}: {persona_value}")
        else:
            print(f" {key}: {value}")