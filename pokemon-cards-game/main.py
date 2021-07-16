from random import sample
from random import choice

pokemons = [
    {
        "name": "bulbasaur",
        "types": [
            "grass",
            "poison"
        ],
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "attack+": 65,
        "defense+": 65,
        "speed": 45,
        "total": 318
    },
    {
        "name": "ivysaur",
        "types": [
            "grass",
            "poison"
        ],
        "hp": 60,
        "attack": 62,
        "defense": 63,
        "attack+": 80,
        "defense+": 80,
        "speed": 60,
        "total": 405
    },
    {
        "name": "venusaur",
        "types": [
            "grass",
            "poison"
        ],
        "hp": 80,
        "attack": 82,
        "defense": 83,
        "attack+": 100,
        "defense+": 100,
        "speed": 80,
        "total": 525
    },
    {
        "name": "charmander",
        "types": [
            "fire"
        ],
        "hp": 39,
        "attack": 52,
        "defense": 43,
        "attack+": 60,
        "defense+": 50,
        "speed": 65,
        "total": 309
    },
    {
        "name": "charmeleon",
        "types": [
            "fire"
        ],
        "hp": 58,
        "attack": 64,
        "defense": 58,
        "attack+": 80,
        "defense+": 65,
        "speed": 80,
        "total": 405
    },
    {
        "name": "charizard",
        "types": [
            "fire",
            "flying"
        ],
        "hp": 78,
        "attack": 84,
        "defense": 78,
        "attack+": 109,
        "defense+": 85,
        "speed": 100,
        "total": 534
    },
    {
        "name": "squirtle",
        "types": [
            "water"
        ],
        "hp": 44,
        "attack": 48,
        "defense": 65,
        "attack+": 50,
        "defense+": 64,
        "speed": 43,
        "total": 314
    },
    {
        "name": "wartortle",
        "types": [
            "water"
        ],
        "hp": 59,
        "attack": 63,
        "defense": 80,
        "attack+": 65,
        "defense+": 80,
        "speed": 58,
        "total": 405
    },
    {
        "name": "blastoise",
        "types": [
            "water"
        ],
        "hp": 79,
        "attack": 83,
        "defense": 100,
        "attack+": 85,
        "defense+": 105,
        "speed": 78,
        "total": 530
    },
    {
        "name": "caterpie",
        "types": [
            "bug"
        ],
        "hp": 45,
        "attack": 30,
        "defense": 35,
        "attack+": 20,
        "defense+": 20,
        "speed": 45,
        "total": 195
    },
    {
        "name": "metapod",
        "types": [
            "bug"
        ],
        "hp": 50,
        "attack": 20,
        "defense": 55,
        "attack+": 25,
        "defense+": 25,
        "speed": 30,
        "total": 205
    },
    {
        "name": "butterfree",
        "types": [
            "bug",
            "flying"
        ],
        "hp": 60,
        "attack": 45,
        "defense": 50,
        "attack+": 90,
        "defense+": 80,
        "speed": 70,
        "total": 395
    },
    {
        "name": "weedle",
        "types": [
            "bug",
            "poison"
        ],
        "hp": 40,
        "attack": 35,
        "defense": 30,
        "attack+": 20,
        "defense+": 20,
        "speed": 50,
        "total": 195
    },
    {
        "name": "kakuna",
        "types": [
            "bug",
            "poison"
        ],
        "hp": 45,
        "attack": 25,
        "defense": 50,
        "attack+": 25,
        "defense+": 25,
        "speed": 35,
        "total": 205
    },
    {
        "name": "beedrill",
        "types": [
            "bug",
            "poison"
        ],
        "hp": 65,
        "attack": 90,
        "defense": 40,
        "attack+": 45,
        "defense+": 80,
        "speed": 75,
        "total": 395
    },
    {
        "name": "pidgey",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 40,
        "attack": 45,
        "defense": 40,
        "attack+": 35,
        "defense+": 35,
        "speed": 56,
        "total": 251
    },
    {
        "name": "pidgeotto",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 63,
        "attack": 60,
        "defense": 55,
        "attack+": 50,
        "defense+": 50,
        "speed": 71,
        "total": 349
    },
    {
        "name": "pidgeot",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 83,
        "attack": 80,
        "defense": 75,
        "attack+": 70,
        "defense+": 70,
        "speed": 101,
        "total": 479
    },
    {
        "name": "rattata",
        "types": [
            "normal"
        ],
        "hp": 30,
        "attack": 56,
        "defense": 35,
        "attack+": 25,
        "defense+": 35,
        "speed": 72,
        "total": 253
    },
    {
        "name": "raticate",
        "types": [
            "normal"
        ],
        "hp": 55,
        "attack": 81,
        "defense": 60,
        "attack+": 50,
        "defense+": 70,
        "speed": 97,
        "total": 413
    },
    {
        "name": "spearow",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 40,
        "attack": 60,
        "defense": 30,
        "attack+": 31,
        "defense+": 31,
        "speed": 70,
        "total": 262
    },
    {
        "name": "fearow",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 65,
        "attack": 90,
        "defense": 65,
        "attack+": 61,
        "defense+": 61,
        "speed": 100,
        "total": 442
    },
    {
        "name": "ekans",
        "types": [
            "poison"
        ],
        "hp": 35,
        "attack": 60,
        "defense": 44,
        "attack+": 40,
        "defense+": 54,
        "speed": 55,
        "total": 288
    },
    {
        "name": "arbok",
        "types": [
            "poison"
        ],
        "hp": 60,
        "attack": 95,
        "defense": 69,
        "attack+": 65,
        "defense+": 79,
        "speed": 80,
        "total": 448
    },
    {
        "name": "pikachu",
        "types": [
            "electric"
        ],
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "attack+": 50,
        "defense+": 50,
        "speed": 90,
        "total": 320
    },
    {
        "name": "raichu",
        "types": [
            "electric"
        ],
        "hp": 60,
        "attack": 90,
        "defense": 55,
        "attack+": 90,
        "defense+": 80,
        "speed": 110,
        "total": 485
    },
    {
        "name": "sandshrew",
        "types": [
            "ground"
        ],
        "hp": 50,
        "attack": 75,
        "defense": 85,
        "attack+": 20,
        "defense+": 30,
        "speed": 40,
        "total": 300
    },
    {
        "name": "sandslash",
        "types": [
            "ground"
        ],
        "hp": 75,
        "attack": 100,
        "defense": 110,
        "attack+": 45,
        "defense+": 55,
        "speed": 65,
        "total": 450
    },
    {
        "name": "nidoran\u2640",
        "types": [
            "poison"
        ],
        "hp": 55,
        "attack": 47,
        "defense": 52,
        "attack+": 40,
        "defense+": 40,
        "speed": 41,
        "total": 275
    },
    {
        "name": "nidorina",
        "types": [
            "poison"
        ],
        "hp": 70,
        "attack": 62,
        "defense": 67,
        "attack+": 55,
        "defense+": 55,
        "speed": 56,
        "total": 365
    },
    {
        "name": "nidoqueen",
        "types": [
            "poison",
            "ground"
        ],
        "hp": 90,
        "attack": 92,
        "defense": 87,
        "attack+": 75,
        "defense+": 85,
        "speed": 76,
        "total": 505
    },
    {
        "name": "nidoran\u2642",
        "types": [
            "poison"
        ],
        "hp": 46,
        "attack": 57,
        "defense": 40,
        "attack+": 40,
        "defense+": 40,
        "speed": 50,
        "total": 273
    },
    {
        "name": "nidorino",
        "types": [
            "poison"
        ],
        "hp": 61,
        "attack": 72,
        "defense": 57,
        "attack+": 55,
        "defense+": 55,
        "speed": 65,
        "total": 365
    },
    {
        "name": "nidoking",
        "types": [
            "poison",
            "ground"
        ],
        "hp": 81,
        "attack": 102,
        "defense": 77,
        "attack+": 85,
        "defense+": 75,
        "speed": 85,
        "total": 505
    },
    {
        "name": "clefairy",
        "types": [
            "fairy"
        ],
        "hp": 70,
        "attack": 45,
        "defense": 48,
        "attack+": 60,
        "defense+": 65,
        "speed": 35,
        "total": 323
    },
    {
        "name": "clefable",
        "types": [
            "fairy"
        ],
        "hp": 95,
        "attack": 70,
        "defense": 73,
        "attack+": 95,
        "defense+": 90,
        "speed": 60,
        "total": 483
    },
    {
        "name": "vulpix",
        "types": [
            "fire"
        ],
        "hp": 38,
        "attack": 41,
        "defense": 40,
        "attack+": 50,
        "defense+": 65,
        "speed": 65,
        "total": 299
    },
    {
        "name": "ninetales",
        "types": [
            "fire"
        ],
        "hp": 73,
        "attack": 76,
        "defense": 75,
        "attack+": 81,
        "defense+": 100,
        "speed": 100,
        "total": 505
    },
    {
        "name": "jigglypuff",
        "types": [
            "normal",
            "fairy"
        ],
        "hp": 115,
        "attack": 45,
        "defense": 20,
        "attack+": 45,
        "defense+": 25,
        "speed": 20,
        "total": 270
    },
    {
        "name": "wigglytuff",
        "types": [
            "normal",
            "fairy"
        ],
        "hp": 140,
        "attack": 70,
        "defense": 45,
        "attack+": 85,
        "defense+": 50,
        "speed": 45,
        "total": 435
    },
    {
        "name": "zubat",
        "types": [
            "poison",
            "flying"
        ],
        "hp": 40,
        "attack": 45,
        "defense": 35,
        "attack+": 30,
        "defense+": 40,
        "speed": 55,
        "total": 245
    },
    {
        "name": "golbat",
        "types": [
            "poison",
            "flying"
        ],
        "hp": 75,
        "attack": 80,
        "defense": 70,
        "attack+": 65,
        "defense+": 75,
        "speed": 90,
        "total": 455
    },
    {
        "name": "oddish",
        "types": [
            "grass",
            "poison"
        ],
        "hp": 45,
        "attack": 50,
        "defense": 55,
        "attack+": 75,
        "defense+": 65,
        "speed": 30,
        "total": 320
    },
    {
        "name": "gloom",
        "types": [
            "grass",
            "poison"
        ],
        "hp": 60,
        "attack": 65,
        "defense": 70,
        "attack+": 85,
        "defense+": 75,
        "speed": 40,
        "total": 395
    },
    {
        "name": "vileplume",
        "types": [
            "grass",
            "poison"
        ],
        "hp": 75,
        "attack": 80,
        "defense": 85,
        "attack+": 110,
        "defense+": 90,
        "speed": 50,
        "total": 490
    },
    {
        "name": "paras",
        "types": [
            "bug",
            "grass"
        ],
        "hp": 35,
        "attack": 70,
        "defense": 55,
        "attack+": 45,
        "defense+": 55,
        "speed": 25,
        "total": 285
    },
    {
        "name": "parasect",
        "types": [
            "bug",
            "grass"
        ],
        "hp": 60,
        "attack": 95,
        "defense": 80,
        "attack+": 60,
        "defense+": 80,
        "speed": 30,
        "total": 405
    },
    {
        "name": "venonat",
        "types": [
            "bug",
            "poison"
        ],
        "hp": 60,
        "attack": 55,
        "defense": 50,
        "attack+": 40,
        "defense+": 55,
        "speed": 45,
        "total": 305
    },
    {
        "name": "venomoth",
        "types": [
            "bug",
            "poison"
        ],
        "hp": 70,
        "attack": 65,
        "defense": 60,
        "attack+": 90,
        "defense+": 75,
        "speed": 90,
        "total": 450
    },
    {
        "name": "diglett",
        "types": [
            "ground"
        ],
        "hp": 10,
        "attack": 55,
        "defense": 25,
        "attack+": 35,
        "defense+": 45,
        "speed": 95,
        "total": 265
    },
    {
        "name": "dugtrio",
        "types": [
            "ground"
        ],
        "hp": 35,
        "attack": 100,
        "defense": 50,
        "attack+": 50,
        "defense+": 70,
        "speed": 120,
        "total": 425
    },
    {
        "name": "meowth",
        "types": [
            "normal"
        ],
        "hp": 40,
        "attack": 45,
        "defense": 35,
        "attack+": 40,
        "defense+": 40,
        "speed": 90,
        "total": 290
    },
    {
        "name": "persian",
        "types": [
            "normal"
        ],
        "hp": 65,
        "attack": 70,
        "defense": 60,
        "attack+": 65,
        "defense+": 65,
        "speed": 115,
        "total": 440
    },
    {
        "name": "psyduck",
        "types": [
            "water"
        ],
        "hp": 50,
        "attack": 52,
        "defense": 48,
        "attack+": 65,
        "defense+": 50,
        "speed": 55,
        "total": 320
    },
    {
        "name": "golduck",
        "types": [
            "water"
        ],
        "hp": 80,
        "attack": 82,
        "defense": 78,
        "attack+": 95,
        "defense+": 80,
        "speed": 85,
        "total": 500
    },
    {
        "name": "mankey",
        "types": [
            "fighting"
        ],
        "hp": 40,
        "attack": 80,
        "defense": 35,
        "attack+": 35,
        "defense+": 45,
        "speed": 70,
        "total": 305
    },
    {
        "name": "primeape",
        "types": [
            "fighting"
        ],
        "hp": 65,
        "attack": 105,
        "defense": 60,
        "attack+": 60,
        "defense+": 70,
        "speed": 95,
        "total": 455
    },
    {
        "name": "growlithe",
        "types": [
            "fire"
        ],
        "hp": 55,
        "attack": 70,
        "defense": 45,
        "attack+": 70,
        "defense+": 50,
        "speed": 60,
        "total": 350
    },
    {
        "name": "arcanine",
        "types": [
            "fire"
        ],
        "hp": 90,
        "attack": 110,
        "defense": 80,
        "attack+": 100,
        "defense+": 80,
        "speed": 95,
        "total": 555
    },
    {
        "name": "poliwag",
        "types": [
            "water"
        ],
        "hp": 40,
        "attack": 50,
        "defense": 40,
        "attack+": 40,
        "defense+": 40,
        "speed": 90,
        "total": 300
    },
    {
        "name": "poliwhirl",
        "types": [
            "water"
        ],
        "hp": 65,
        "attack": 65,
        "defense": 65,
        "attack+": 50,
        "defense+": 50,
        "speed": 90,
        "total": 385
    },
    {
        "name": "poliwrath",
        "types": [
            "water",
            "fighting"
        ],
        "hp": 90,
        "attack": 95,
        "defense": 95,
        "attack+": 70,
        "defense+": 90,
        "speed": 70,
        "total": 510
    },
    {
        "name": "abra",
        "types": [
            "psychic"
        ],
        "hp": 25,
        "attack": 20,
        "defense": 15,
        "attack+": 105,
        "defense+": 55,
        "speed": 90,
        "total": 310
    },
    {
        "name": "kadabra",
        "types": [
            "psychic"
        ],
        "hp": 40,
        "attack": 35,
        "defense": 30,
        "attack+": 120,
        "defense+": 70,
        "speed": 105,
        "total": 400
    },
    {
        "name": "alakazam",
        "types": [
            "psychic"
        ],
        "hp": 55,
        "attack": 50,
        "defense": 45,
        "attack+": 135,
        "defense+": 95,
        "speed": 120,
        "total": 500
    },
    {
        "name": "machop",
        "types": [
            "fighting"
        ],
        "hp": 70,
        "attack": 80,
        "defense": 50,
        "attack+": 35,
        "defense+": 35,
        "speed": 35,
        "total": 305
    },
    {
        "name": "machoke",
        "types": [
            "fighting"
        ],
        "hp": 80,
        "attack": 100,
        "defense": 70,
        "attack+": 50,
        "defense+": 60,
        "speed": 45,
        "total": 405
    },
    {
        "name": "machamp",
        "types": [
            "fighting"
        ],
        "hp": 90,
        "attack": 130,
        "defense": 80,
        "attack+": 65,
        "defense+": 85,
        "speed": 55,
        "total": 505
    },
    {
        "name": "bellsprout",
        "types": [
            "grass",
            "poison"
        ],
        "hp": 50,
        "attack": 75,
        "defense": 35,
        "attack+": 70,
        "defense+": 30,
        "speed": 40,
        "total": 300
    },
    {
        "name": "weepinbell",
        "types": [
            "grass",
            "poison"
        ],
        "hp": 65,
        "attack": 90,
        "defense": 50,
        "attack+": 85,
        "defense+": 45,
        "speed": 55,
        "total": 390
    },
    {
        "name": "victreebel",
        "types": [
            "grass",
            "poison"
        ],
        "hp": 80,
        "attack": 105,
        "defense": 65,
        "attack+": 100,
        "defense+": 70,
        "speed": 70,
        "total": 490
    },
    {
        "name": "tentacool",
        "types": [
            "water",
            "poison"
        ],
        "hp": 40,
        "attack": 40,
        "defense": 35,
        "attack+": 50,
        "defense+": 100,
        "speed": 70,
        "total": 335
    },
    {
        "name": "tentacruel",
        "types": [
            "water",
            "poison"
        ],
        "hp": 80,
        "attack": 70,
        "defense": 65,
        "attack+": 80,
        "defense+": 120,
        "speed": 100,
        "total": 515
    },
    {
        "name": "geodude",
        "types": [
            "rock",
            "ground"
        ],
        "hp": 40,
        "attack": 80,
        "defense": 100,
        "attack+": 30,
        "defense+": 30,
        "speed": 20,
        "total": 300
    },
    {
        "name": "graveler",
        "types": [
            "rock",
            "ground"
        ],
        "hp": 55,
        "attack": 95,
        "defense": 115,
        "attack+": 45,
        "defense+": 45,
        "speed": 35,
        "total": 390
    },
    {
        "name": "golem",
        "types": [
            "rock",
            "ground"
        ],
        "hp": 80,
        "attack": 120,
        "defense": 130,
        "attack+": 55,
        "defense+": 65,
        "speed": 45,
        "total": 495
    },
    {
        "name": "ponyta",
        "types": [
            "fire"
        ],
        "hp": 50,
        "attack": 85,
        "defense": 55,
        "attack+": 65,
        "defense+": 65,
        "speed": 90,
        "total": 410
    },
    {
        "name": "rapidash",
        "types": [
            "fire"
        ],
        "hp": 65,
        "attack": 100,
        "defense": 70,
        "attack+": 80,
        "defense+": 80,
        "speed": 105,
        "total": 500
    },
    {
        "name": "slowpoke",
        "types": [
            "water",
            "psychic"
        ],
        "hp": 90,
        "attack": 65,
        "defense": 65,
        "attack+": 40,
        "defense+": 40,
        "speed": 15,
        "total": 315
    },
    {
        "name": "slowbro",
        "types": [
            "water",
            "psychic"
        ],
        "hp": 95,
        "attack": 75,
        "defense": 110,
        "attack+": 100,
        "defense+": 80,
        "speed": 30,
        "total": 490
    },
    {
        "name": "magnemite",
        "types": [
            "electric",
            "steel"
        ],
        "hp": 25,
        "attack": 35,
        "defense": 70,
        "attack+": 95,
        "defense+": 55,
        "speed": 45,
        "total": 325
    },
    {
        "name": "magneton",
        "types": [
            "electric",
            "steel"
        ],
        "hp": 50,
        "attack": 60,
        "defense": 95,
        "attack+": 120,
        "defense+": 70,
        "speed": 70,
        "total": 465
    },
    {
        "name": "farfetch'd",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 52,
        "attack": 90,
        "defense": 55,
        "attack+": 58,
        "defense+": 62,
        "speed": 60,
        "total": 377
    },
    {
        "name": "doduo",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 35,
        "attack": 85,
        "defense": 45,
        "attack+": 35,
        "defense+": 35,
        "speed": 75,
        "total": 310
    },
    {
        "name": "dodrio",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 60,
        "attack": 110,
        "defense": 70,
        "attack+": 60,
        "defense+": 60,
        "speed": 110,
        "total": 470
    },
    {
        "name": "seel",
        "types": [
            "water"
        ],
        "hp": 65,
        "attack": 45,
        "defense": 55,
        "attack+": 45,
        "defense+": 70,
        "speed": 45,
        "total": 325
    },
    {
        "name": "dewgong",
        "types": [
            "water",
            "ice"
        ],
        "hp": 90,
        "attack": 70,
        "defense": 80,
        "attack+": 70,
        "defense+": 95,
        "speed": 70,
        "total": 475
    },
    {
        "name": "grimer",
        "types": [
            "poison"
        ],
        "hp": 80,
        "attack": 80,
        "defense": 50,
        "attack+": 40,
        "defense+": 50,
        "speed": 25,
        "total": 325
    },
    {
        "name": "muk",
        "types": [
            "poison"
        ],
        "hp": 105,
        "attack": 105,
        "defense": 75,
        "attack+": 65,
        "defense+": 100,
        "speed": 50,
        "total": 500
    },
    {
        "name": "shellder",
        "types": [
            "water"
        ],
        "hp": 30,
        "attack": 65,
        "defense": 100,
        "attack+": 45,
        "defense+": 25,
        "speed": 40,
        "total": 305
    },
    {
        "name": "cloyster",
        "types": [
            "water",
            "ice"
        ],
        "hp": 50,
        "attack": 95,
        "defense": 180,
        "attack+": 85,
        "defense+": 45,
        "speed": 70,
        "total": 525
    },
    {
        "name": "gastly",
        "types": [
            "ghost",
            "poison"
        ],
        "hp": 30,
        "attack": 35,
        "defense": 30,
        "attack+": 100,
        "defense+": 35,
        "speed": 80,
        "total": 310
    },
    {
        "name": "haunter",
        "types": [
            "ghost",
            "poison"
        ],
        "hp": 45,
        "attack": 50,
        "defense": 45,
        "attack+": 115,
        "defense+": 55,
        "speed": 95,
        "total": 405
    },
    {
        "name": "gengar",
        "types": [
            "ghost",
            "poison"
        ],
        "hp": 60,
        "attack": 65,
        "defense": 60,
        "attack+": 130,
        "defense+": 75,
        "speed": 110,
        "total": 500
    },
    {
        "name": "onix",
        "types": [
            "rock",
            "ground"
        ],
        "hp": 35,
        "attack": 45,
        "defense": 160,
        "attack+": 30,
        "defense+": 45,
        "speed": 70,
        "total": 385
    },
    {
        "name": "drowzee",
        "types": [
            "psychic"
        ],
        "hp": 60,
        "attack": 48,
        "defense": 45,
        "attack+": 43,
        "defense+": 90,
        "speed": 42,
        "total": 328
    },
    {
        "name": "hypno",
        "types": [
            "psychic"
        ],
        "hp": 85,
        "attack": 73,
        "defense": 70,
        "attack+": 73,
        "defense+": 115,
        "speed": 67,
        "total": 483
    },
    {
        "name": "krabby",
        "types": [
            "water"
        ],
        "hp": 30,
        "attack": 105,
        "defense": 90,
        "attack+": 25,
        "defense+": 25,
        "speed": 50,
        "total": 325
    },
    {
        "name": "kingler",
        "types": [
            "water"
        ],
        "hp": 55,
        "attack": 130,
        "defense": 115,
        "attack+": 50,
        "defense+": 50,
        "speed": 75,
        "total": 475
    },
    {
        "name": "voltorb",
        "types": [
            "electric"
        ],
        "hp": 40,
        "attack": 30,
        "defense": 50,
        "attack+": 55,
        "defense+": 55,
        "speed": 100,
        "total": 330
    },
    {
        "name": "electrode",
        "types": [
            "electric"
        ],
        "hp": 60,
        "attack": 50,
        "defense": 70,
        "attack+": 80,
        "defense+": 80,
        "speed": 150,
        "total": 490
    },
    {
        "name": "exeggcute",
        "types": [
            "grass",
            "psychic"
        ],
        "hp": 60,
        "attack": 40,
        "defense": 80,
        "attack+": 60,
        "defense+": 45,
        "speed": 40,
        "total": 325
    },
    {
        "name": "exeggutor",
        "types": [
            "grass",
            "psychic"
        ],
        "hp": 95,
        "attack": 95,
        "defense": 85,
        "attack+": 125,
        "defense+": 75,
        "speed": 55,
        "total": 530
    },
    {
        "name": "cubone",
        "types": [
            "ground"
        ],
        "hp": 50,
        "attack": 50,
        "defense": 95,
        "attack+": 40,
        "defense+": 50,
        "speed": 35,
        "total": 320
    },
    {
        "name": "marowak",
        "types": [
            "ground"
        ],
        "hp": 60,
        "attack": 80,
        "defense": 110,
        "attack+": 50,
        "defense+": 80,
        "speed": 45,
        "total": 425
    },
    {
        "name": "hitmonlee",
        "types": [
            "fighting"
        ],
        "hp": 50,
        "attack": 120,
        "defense": 53,
        "attack+": 35,
        "defense+": 110,
        "speed": 87,
        "total": 455
    },
    {
        "name": "hitmonchan",
        "types": [
            "fighting"
        ],
        "hp": 50,
        "attack": 105,
        "defense": 79,
        "attack+": 35,
        "defense+": 110,
        "speed": 76,
        "total": 455
    },
    {
        "name": "lickitung",
        "types": [
            "normal"
        ],
        "hp": 90,
        "attack": 55,
        "defense": 75,
        "attack+": 60,
        "defense+": 75,
        "speed": 30,
        "total": 385
    },
    {
        "name": "koffing",
        "types": [
            "poison"
        ],
        "hp": 40,
        "attack": 65,
        "defense": 95,
        "attack+": 60,
        "defense+": 45,
        "speed": 35,
        "total": 340
    },
    {
        "name": "weezing",
        "types": [
            "poison"
        ],
        "hp": 65,
        "attack": 90,
        "defense": 120,
        "attack+": 85,
        "defense+": 70,
        "speed": 60,
        "total": 490
    },
    {
        "name": "rhyhorn",
        "types": [
            "ground",
            "rock"
        ],
        "hp": 80,
        "attack": 85,
        "defense": 95,
        "attack+": 30,
        "defense+": 30,
        "speed": 25,
        "total": 345
    },
    {
        "name": "rhydon",
        "types": [
            "ground",
            "rock"
        ],
        "hp": 105,
        "attack": 130,
        "defense": 120,
        "attack+": 45,
        "defense+": 45,
        "speed": 40,
        "total": 485
    },
    {
        "name": "chansey",
        "types": [
            "normal"
        ],
        "hp": 250,
        "attack": 5,
        "defense": 5,
        "attack+": 35,
        "defense+": 105,
        "speed": 50,
        "total": 450
    },
    {
        "name": "tangela",
        "types": [
            "grass"
        ],
        "hp": 65,
        "attack": 55,
        "defense": 115,
        "attack+": 100,
        "defense+": 40,
        "speed": 60,
        "total": 435
    },
    {
        "name": "kangaskhan",
        "types": [
            "normal"
        ],
        "hp": 105,
        "attack": 95,
        "defense": 80,
        "attack+": 40,
        "defense+": 80,
        "speed": 90,
        "total": 490
    },
    {
        "name": "horsea",
        "types": [
            "water"
        ],
        "hp": 30,
        "attack": 40,
        "defense": 70,
        "attack+": 70,
        "defense+": 25,
        "speed": 60,
        "total": 295
    },
    {
        "name": "seadra",
        "types": [
            "water"
        ],
        "hp": 55,
        "attack": 65,
        "defense": 95,
        "attack+": 95,
        "defense+": 45,
        "speed": 85,
        "total": 440
    },
    {
        "name": "goldeen",
        "types": [
            "water"
        ],
        "hp": 45,
        "attack": 67,
        "defense": 60,
        "attack+": 35,
        "defense+": 50,
        "speed": 63,
        "total": 320
    },
    {
        "name": "seaking",
        "types": [
            "water"
        ],
        "hp": 80,
        "attack": 92,
        "defense": 65,
        "attack+": 65,
        "defense+": 80,
        "speed": 68,
        "total": 450
    },
    {
        "name": "staryu",
        "types": [
            "water"
        ],
        "hp": 30,
        "attack": 45,
        "defense": 55,
        "attack+": 70,
        "defense+": 55,
        "speed": 85,
        "total": 340
    },
    {
        "name": "starmie",
        "types": [
            "water",
            "psychic"
        ],
        "hp": 60,
        "attack": 75,
        "defense": 85,
        "attack+": 100,
        "defense+": 85,
        "speed": 115,
        "total": 520
    },
    {
        "name": "mr.",
        "types": [
            "psychic",
            "fairy"
        ],
        "hp": 40,
        "attack": 45,
        "defense": 65,
        "attack+": 100,
        "defense+": 120,
        "speed": 90,
        "total": 460
    },
    {
        "name": "scyther",
        "types": [
            "bug",
            "flying"
        ],
        "hp": 70,
        "attack": 110,
        "defense": 80,
        "attack+": 55,
        "defense+": 80,
        "speed": 105,
        "total": 500
    },
    {
        "name": "jynx",
        "types": [
            "ice",
            "psychic"
        ],
        "hp": 65,
        "attack": 50,
        "defense": 35,
        "attack+": 115,
        "defense+": 95,
        "speed": 95,
        "total": 455
    },
    {
        "name": "electabuzz",
        "types": [
            "electric"
        ],
        "hp": 65,
        "attack": 83,
        "defense": 57,
        "attack+": 95,
        "defense+": 85,
        "speed": 105,
        "total": 490
    },
    {
        "name": "magmar",
        "types": [
            "fire"
        ],
        "hp": 65,
        "attack": 95,
        "defense": 57,
        "attack+": 100,
        "defense+": 85,
        "speed": 93,
        "total": 495
    },
    {
        "name": "pinsir",
        "types": [
            "bug"
        ],
        "hp": 65,
        "attack": 125,
        "defense": 100,
        "attack+": 55,
        "defense+": 70,
        "speed": 85,
        "total": 500
    },
    {
        "name": "tauros",
        "types": [
            "normal"
        ],
        "hp": 75,
        "attack": 100,
        "defense": 95,
        "attack+": 40,
        "defense+": 70,
        "speed": 110,
        "total": 490
    },
    {
        "name": "magikarp",
        "types": [
            "water"
        ],
        "hp": 20,
        "attack": 10,
        "defense": 55,
        "attack+": 15,
        "defense+": 20,
        "speed": 80,
        "total": 200
    },
    {
        "name": "gyarados",
        "types": [
            "water",
            "flying"
        ],
        "hp": 95,
        "attack": 125,
        "defense": 79,
        "attack+": 60,
        "defense+": 100,
        "speed": 81,
        "total": 540
    },
    {
        "name": "lapras",
        "types": [
            "water",
            "ice"
        ],
        "hp": 130,
        "attack": 85,
        "defense": 80,
        "attack+": 85,
        "defense+": 95,
        "speed": 60,
        "total": 535
    },
    {
        "name": "ditto",
        "types": [
            "normal"
        ],
        "hp": 48,
        "attack": 48,
        "defense": 48,
        "attack+": 48,
        "defense+": 48,
        "speed": 48,
        "total": 288
    },
    {
        "name": "eevee",
        "types": [
            "normal"
        ],
        "hp": 55,
        "attack": 55,
        "defense": 50,
        "attack+": 45,
        "defense+": 65,
        "speed": 55,
        "total": 325
    },
    {
        "name": "vaporeon",
        "types": [
            "water"
        ],
        "hp": 130,
        "attack": 65,
        "defense": 60,
        "attack+": 110,
        "defense+": 95,
        "speed": 65,
        "total": 525
    },
    {
        "name": "jolteon",
        "types": [
            "electric"
        ],
        "hp": 65,
        "attack": 65,
        "defense": 60,
        "attack+": 110,
        "defense+": 95,
        "speed": 130,
        "total": 525
    },
    {
        "name": "flareon",
        "types": [
            "fire"
        ],
        "hp": 65,
        "attack": 130,
        "defense": 60,
        "attack+": 95,
        "defense+": 110,
        "speed": 65,
        "total": 525
    },
    {
        "name": "porygon",
        "types": [
            "normal"
        ],
        "hp": 65,
        "attack": 60,
        "defense": 70,
        "attack+": 85,
        "defense+": 75,
        "speed": 40,
        "total": 395
    },
    {
        "name": "omanyte",
        "types": [
            "rock",
            "water"
        ],
        "hp": 35,
        "attack": 40,
        "defense": 100,
        "attack+": 90,
        "defense+": 55,
        "speed": 35,
        "total": 355
    },
    {
        "name": "omastar",
        "types": [
            "rock",
            "water"
        ],
        "hp": 70,
        "attack": 60,
        "defense": 125,
        "attack+": 115,
        "defense+": 70,
        "speed": 55,
        "total": 495
    },
    {
        "name": "kabuto",
        "types": [
            "rock",
            "water"
        ],
        "hp": 30,
        "attack": 80,
        "defense": 90,
        "attack+": 55,
        "defense+": 45,
        "speed": 55,
        "total": 355
    },
    {
        "name": "kabutops",
        "types": [
            "rock",
            "water"
        ],
        "hp": 60,
        "attack": 115,
        "defense": 105,
        "attack+": 65,
        "defense+": 70,
        "speed": 80,
        "total": 495
    },
    {
        "name": "aerodactyl",
        "types": [
            "rock",
            "flying"
        ],
        "hp": 80,
        "attack": 105,
        "defense": 65,
        "attack+": 60,
        "defense+": 75,
        "speed": 130,
        "total": 515
    },
    {
        "name": "snorlax",
        "types": [
            "normal"
        ],
        "hp": 160,
        "attack": 110,
        "defense": 65,
        "attack+": 65,
        "defense+": 110,
        "speed": 30,
        "total": 540
    },
    {
        "name": "articuno",
        "types": [
            "ice",
            "flying"
        ],
        "hp": 90,
        "attack": 85,
        "defense": 100,
        "attack+": 95,
        "defense+": 125,
        "speed": 85,
        "total": 580
    },
    {
        "name": "zapdos",
        "types": [
            "electric",
            "flying"
        ],
        "hp": 90,
        "attack": 90,
        "defense": 85,
        "attack+": 125,
        "defense+": 90,
        "speed": 100,
        "total": 580
    },
    {
        "name": "moltres",
        "types": [
            "fire",
            "flying"
        ],
        "hp": 90,
        "attack": 100,
        "defense": 90,
        "attack+": 125,
        "defense+": 85,
        "speed": 90,
        "total": 580
    },
    {
        "name": "dratini",
        "types": [
            "dragon"
        ],
        "hp": 41,
        "attack": 64,
        "defense": 45,
        "attack+": 50,
        "defense+": 50,
        "speed": 50,
        "total": 300
    },
    {
        "name": "dragonair",
        "types": [
            "dragon"
        ],
        "hp": 61,
        "attack": 84,
        "defense": 65,
        "attack+": 70,
        "defense+": 70,
        "speed": 70,
        "total": 420
    },
    {
        "name": "dragonite",
        "types": [
            "dragon",
            "flying"
        ],
        "hp": 91,
        "attack": 134,
        "defense": 95,
        "attack+": 100,
        "defense+": 100,
        "speed": 80,
        "total": 600
    },
    {
        "name": "mewtwo",
        "types": [
            "psychic"
        ],
        "hp": 106,
        "attack": 110,
        "defense": 90,
        "attack+": 154,
        "defense+": 90,
        "speed": 130,
        "total": 680
    },
    {
        "name": "mew",
        "types": [
            "psychic"
        ],
        "hp": 100,
        "attack": 100,
        "defense": 100,
        "attack+": 100,
        "defense+": 100,
        "speed": 100,
        "total": 600
    },
    {
        "name": "chikorita",
        "types": [
            "grass"
        ],
        "hp": 45,
        "attack": 49,
        "defense": 65,
        "attack+": 49,
        "defense+": 65,
        "speed": 45,
        "total": 318
    },
    {
        "name": "bayleef",
        "types": [
            "grass"
        ],
        "hp": 60,
        "attack": 62,
        "defense": 80,
        "attack+": 63,
        "defense+": 80,
        "speed": 60,
        "total": 405
    },
    {
        "name": "meganium",
        "types": [
            "grass"
        ],
        "hp": 80,
        "attack": 82,
        "defense": 100,
        "attack+": 83,
        "defense+": 100,
        "speed": 80,
        "total": 525
    },
    {
        "name": "cyndaquil",
        "types": [
            "fire"
        ],
        "hp": 39,
        "attack": 52,
        "defense": 43,
        "attack+": 60,
        "defense+": 50,
        "speed": 65,
        "total": 309
    },
    {
        "name": "quilava",
        "types": [
            "fire"
        ],
        "hp": 58,
        "attack": 64,
        "defense": 58,
        "attack+": 80,
        "defense+": 65,
        "speed": 80,
        "total": 405
    },
    {
        "name": "typhlosion",
        "types": [
            "fire"
        ],
        "hp": 78,
        "attack": 84,
        "defense": 78,
        "attack+": 109,
        "defense+": 85,
        "speed": 100,
        "total": 534
    },
    {
        "name": "totodile",
        "types": [
            "water"
        ],
        "hp": 50,
        "attack": 65,
        "defense": 64,
        "attack+": 44,
        "defense+": 48,
        "speed": 43,
        "total": 314
    },
    {
        "name": "croconaw",
        "types": [
            "water"
        ],
        "hp": 65,
        "attack": 80,
        "defense": 80,
        "attack+": 59,
        "defense+": 63,
        "speed": 58,
        "total": 405
    },
    {
        "name": "feraligatr",
        "types": [
            "water"
        ],
        "hp": 85,
        "attack": 105,
        "defense": 100,
        "attack+": 79,
        "defense+": 83,
        "speed": 78,
        "total": 530
    },
    {
        "name": "sentret",
        "types": [
            "normal"
        ],
        "hp": 35,
        "attack": 46,
        "defense": 34,
        "attack+": 35,
        "defense+": 45,
        "speed": 20,
        "total": 215
    },
    {
        "name": "furret",
        "types": [
            "normal"
        ],
        "hp": 85,
        "attack": 76,
        "defense": 64,
        "attack+": 45,
        "defense+": 55,
        "speed": 90,
        "total": 415
    },
    {
        "name": "hoothoot",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 60,
        "attack": 30,
        "defense": 30,
        "attack+": 36,
        "defense+": 56,
        "speed": 50,
        "total": 262
    },
    {
        "name": "noctowl",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 100,
        "attack": 50,
        "defense": 50,
        "attack+": 86,
        "defense+": 96,
        "speed": 70,
        "total": 452
    },
    {
        "name": "ledyba",
        "types": [
            "bug",
            "flying"
        ],
        "hp": 40,
        "attack": 20,
        "defense": 30,
        "attack+": 40,
        "defense+": 80,
        "speed": 55,
        "total": 265
    },
    {
        "name": "ledian",
        "types": [
            "bug",
            "flying"
        ],
        "hp": 55,
        "attack": 35,
        "defense": 50,
        "attack+": 55,
        "defense+": 110,
        "speed": 85,
        "total": 390
    },
    {
        "name": "spinarak",
        "types": [
            "bug",
            "poison"
        ],
        "hp": 40,
        "attack": 60,
        "defense": 40,
        "attack+": 40,
        "defense+": 40,
        "speed": 30,
        "total": 250
    },
    {
        "name": "ariados",
        "types": [
            "bug",
            "poison"
        ],
        "hp": 70,
        "attack": 90,
        "defense": 70,
        "attack+": 60,
        "defense+": 70,
        "speed": 40,
        "total": 400
    },
    {
        "name": "crobat",
        "types": [
            "poison",
            "flying"
        ],
        "hp": 85,
        "attack": 90,
        "defense": 80,
        "attack+": 70,
        "defense+": 80,
        "speed": 130,
        "total": 535
    },
    {
        "name": "chinchou",
        "types": [
            "water",
            "electric"
        ],
        "hp": 75,
        "attack": 38,
        "defense": 38,
        "attack+": 56,
        "defense+": 56,
        "speed": 67,
        "total": 330
    },
    {
        "name": "lanturn",
        "types": [
            "water",
            "electric"
        ],
        "hp": 125,
        "attack": 58,
        "defense": 58,
        "attack+": 76,
        "defense+": 76,
        "speed": 67,
        "total": 460
    },
    {
        "name": "pichu",
        "types": [
            "electric"
        ],
        "hp": 20,
        "attack": 40,
        "defense": 15,
        "attack+": 35,
        "defense+": 35,
        "speed": 60,
        "total": 205
    },
    {
        "name": "cleffa",
        "types": [
            "fairy"
        ],
        "hp": 50,
        "attack": 25,
        "defense": 28,
        "attack+": 45,
        "defense+": 55,
        "speed": 15,
        "total": 218
    },
    {
        "name": "igglybuff",
        "types": [
            "normal",
            "fairy"
        ],
        "hp": 90,
        "attack": 30,
        "defense": 15,
        "attack+": 40,
        "defense+": 20,
        "speed": 15,
        "total": 210
    },
    {
        "name": "togepi",
        "types": [
            "fairy"
        ],
        "hp": 35,
        "attack": 20,
        "defense": 65,
        "attack+": 40,
        "defense+": 65,
        "speed": 20,
        "total": 245
    },
    {
        "name": "togetic",
        "types": [
            "fairy",
            "flying"
        ],
        "hp": 55,
        "attack": 40,
        "defense": 85,
        "attack+": 80,
        "defense+": 105,
        "speed": 40,
        "total": 405
    },
    {
        "name": "natu",
        "types": [
            "psychic",
            "flying"
        ],
        "hp": 40,
        "attack": 50,
        "defense": 45,
        "attack+": 70,
        "defense+": 45,
        "speed": 70,
        "total": 320
    },
    {
        "name": "xatu",
        "types": [
            "psychic",
            "flying"
        ],
        "hp": 65,
        "attack": 75,
        "defense": 70,
        "attack+": 95,
        "defense+": 70,
        "speed": 95,
        "total": 470
    },
    {
        "name": "mareep",
        "types": [
            "electric"
        ],
        "hp": 55,
        "attack": 40,
        "defense": 40,
        "attack+": 65,
        "defense+": 45,
        "speed": 35,
        "total": 280
    },
    {
        "name": "flaaffy",
        "types": [
            "electric"
        ],
        "hp": 70,
        "attack": 55,
        "defense": 55,
        "attack+": 80,
        "defense+": 60,
        "speed": 45,
        "total": 365
    },
    {
        "name": "ampharos",
        "types": [
            "electric"
        ],
        "hp": 90,
        "attack": 75,
        "defense": 85,
        "attack+": 115,
        "defense+": 90,
        "speed": 55,
        "total": 510
    },
    {
        "name": "bellossom",
        "types": [
            "grass"
        ],
        "hp": 75,
        "attack": 80,
        "defense": 95,
        "attack+": 90,
        "defense+": 100,
        "speed": 50,
        "total": 490
    },
    {
        "name": "marill",
        "types": [
            "water",
            "fairy"
        ],
        "hp": 70,
        "attack": 20,
        "defense": 50,
        "attack+": 20,
        "defense+": 50,
        "speed": 40,
        "total": 250
    },
    {
        "name": "azumarill",
        "types": [
            "water",
            "fairy"
        ],
        "hp": 100,
        "attack": 50,
        "defense": 80,
        "attack+": 60,
        "defense+": 80,
        "speed": 50,
        "total": 420
    },
    {
        "name": "sudowoodo",
        "types": [
            "rock"
        ],
        "hp": 70,
        "attack": 100,
        "defense": 115,
        "attack+": 30,
        "defense+": 65,
        "speed": 30,
        "total": 410
    },
    {
        "name": "politoed",
        "types": [
            "water"
        ],
        "hp": 90,
        "attack": 75,
        "defense": 75,
        "attack+": 90,
        "defense+": 100,
        "speed": 70,
        "total": 500
    },
    {
        "name": "hoppip",
        "types": [
            "grass",
            "flying"
        ],
        "hp": 35,
        "attack": 35,
        "defense": 40,
        "attack+": 35,
        "defense+": 55,
        "speed": 50,
        "total": 250
    },
    {
        "name": "skiploom",
        "types": [
            "grass",
            "flying"
        ],
        "hp": 55,
        "attack": 45,
        "defense": 50,
        "attack+": 45,
        "defense+": 65,
        "speed": 80,
        "total": 340
    },
    {
        "name": "jumpluff",
        "types": [
            "grass",
            "flying"
        ],
        "hp": 75,
        "attack": 55,
        "defense": 70,
        "attack+": 55,
        "defense+": 95,
        "speed": 110,
        "total": 460
    },
    {
        "name": "aipom",
        "types": [
            "normal"
        ],
        "hp": 55,
        "attack": 70,
        "defense": 55,
        "attack+": 40,
        "defense+": 55,
        "speed": 85,
        "total": 360
    },
    {
        "name": "sunkern",
        "types": [
            "grass"
        ],
        "hp": 30,
        "attack": 30,
        "defense": 30,
        "attack+": 30,
        "defense+": 30,
        "speed": 30,
        "total": 180
    },
    {
        "name": "sunflora",
        "types": [
            "grass"
        ],
        "hp": 75,
        "attack": 75,
        "defense": 55,
        "attack+": 105,
        "defense+": 85,
        "speed": 30,
        "total": 425
    },
    {
        "name": "yanma",
        "types": [
            "bug",
            "flying"
        ],
        "hp": 65,
        "attack": 65,
        "defense": 45,
        "attack+": 75,
        "defense+": 45,
        "speed": 95,
        "total": 390
    },
    {
        "name": "wooper",
        "types": [
            "water",
            "ground"
        ],
        "hp": 55,
        "attack": 45,
        "defense": 45,
        "attack+": 25,
        "defense+": 25,
        "speed": 15,
        "total": 210
    },
    {
        "name": "quagsire",
        "types": [
            "water",
            "ground"
        ],
        "hp": 95,
        "attack": 85,
        "defense": 85,
        "attack+": 65,
        "defense+": 65,
        "speed": 35,
        "total": 430
    },
    {
        "name": "espeon",
        "types": [
            "psychic"
        ],
        "hp": 65,
        "attack": 65,
        "defense": 60,
        "attack+": 130,
        "defense+": 95,
        "speed": 110,
        "total": 525
    },
    {
        "name": "umbreon",
        "types": [
            "dark"
        ],
        "hp": 95,
        "attack": 65,
        "defense": 110,
        "attack+": 60,
        "defense+": 130,
        "speed": 65,
        "total": 525
    },
    {
        "name": "murkrow",
        "types": [
            "dark",
            "flying"
        ],
        "hp": 60,
        "attack": 85,
        "defense": 42,
        "attack+": 85,
        "defense+": 42,
        "speed": 91,
        "total": 405
    },
    {
        "name": "slowking",
        "types": [
            "water",
            "psychic"
        ],
        "hp": 95,
        "attack": 75,
        "defense": 80,
        "attack+": 100,
        "defense+": 110,
        "speed": 30,
        "total": 490
    },
    {
        "name": "misdreavus",
        "types": [
            "ghost"
        ],
        "hp": 60,
        "attack": 60,
        "defense": 60,
        "attack+": 85,
        "defense+": 85,
        "speed": 85,
        "total": 435
    },
    {
        "name": "unown",
        "types": [
            "psychic"
        ],
        "hp": 48,
        "attack": 72,
        "defense": 48,
        "attack+": 72,
        "defense+": 48,
        "speed": 48,
        "total": 336
    },
    {
        "name": "wobbuffet",
        "types": [
            "psychic"
        ],
        "hp": 190,
        "attack": 33,
        "defense": 58,
        "attack+": 33,
        "defense+": 58,
        "speed": 33,
        "total": 405
    },
    {
        "name": "girafarig",
        "types": [
            "normal",
            "psychic"
        ],
        "hp": 70,
        "attack": 80,
        "defense": 65,
        "attack+": 90,
        "defense+": 65,
        "speed": 85,
        "total": 455
    },
    {
        "name": "pineco",
        "types": [
            "bug"
        ],
        "hp": 50,
        "attack": 65,
        "defense": 90,
        "attack+": 35,
        "defense+": 35,
        "speed": 15,
        "total": 290
    },
    {
        "name": "forretress",
        "types": [
            "bug",
            "steel"
        ],
        "hp": 75,
        "attack": 90,
        "defense": 140,
        "attack+": 60,
        "defense+": 60,
        "speed": 40,
        "total": 465
    },
    {
        "name": "dunsparce",
        "types": [
            "normal"
        ],
        "hp": 100,
        "attack": 70,
        "defense": 70,
        "attack+": 65,
        "defense+": 65,
        "speed": 45,
        "total": 415
    },
    {
        "name": "gligar",
        "types": [
            "ground",
            "flying"
        ],
        "hp": 65,
        "attack": 75,
        "defense": 105,
        "attack+": 35,
        "defense+": 65,
        "speed": 85,
        "total": 430
    },
    {
        "name": "steelix",
        "types": [
            "steel",
            "ground"
        ],
        "hp": 75,
        "attack": 85,
        "defense": 200,
        "attack+": 55,
        "defense+": 65,
        "speed": 30,
        "total": 510
    },
    {
        "name": "snubbull",
        "types": [
            "fairy"
        ],
        "hp": 60,
        "attack": 80,
        "defense": 50,
        "attack+": 40,
        "defense+": 40,
        "speed": 30,
        "total": 300
    },
    {
        "name": "granbull",
        "types": [
            "fairy"
        ],
        "hp": 90,
        "attack": 120,
        "defense": 75,
        "attack+": 60,
        "defense+": 60,
        "speed": 45,
        "total": 450
    },
    {
        "name": "qwilfish",
        "types": [
            "water",
            "poison"
        ],
        "hp": 65,
        "attack": 95,
        "defense": 85,
        "attack+": 55,
        "defense+": 55,
        "speed": 85,
        "total": 440
    },
    {
        "name": "scizor",
        "types": [
            "bug",
            "steel"
        ],
        "hp": 70,
        "attack": 130,
        "defense": 100,
        "attack+": 55,
        "defense+": 80,
        "speed": 65,
        "total": 500
    },
    {
        "name": "shuckle",
        "types": [
            "bug",
            "rock"
        ],
        "hp": 20,
        "attack": 10,
        "defense": 230,
        "attack+": 10,
        "defense+": 230,
        "speed": 5,
        "total": 505
    },
    {
        "name": "heracross",
        "types": [
            "bug",
            "fighting"
        ],
        "hp": 80,
        "attack": 125,
        "defense": 75,
        "attack+": 40,
        "defense+": 95,
        "speed": 85,
        "total": 500
    },
    {
        "name": "sneasel",
        "types": [
            "dark",
            "ice"
        ],
        "hp": 55,
        "attack": 95,
        "defense": 55,
        "attack+": 35,
        "defense+": 75,
        "speed": 115,
        "total": 430
    },
    {
        "name": "teddiursa",
        "types": [
            "normal"
        ],
        "hp": 60,
        "attack": 80,
        "defense": 50,
        "attack+": 50,
        "defense+": 50,
        "speed": 40,
        "total": 330
    },
    {
        "name": "ursaring",
        "types": [
            "normal"
        ],
        "hp": 90,
        "attack": 130,
        "defense": 75,
        "attack+": 75,
        "defense+": 75,
        "speed": 55,
        "total": 500
    },
    {
        "name": "slugma",
        "types": [
            "fire"
        ],
        "hp": 40,
        "attack": 40,
        "defense": 40,
        "attack+": 70,
        "defense+": 40,
        "speed": 20,
        "total": 250
    },
    {
        "name": "magcargo",
        "types": [
            "fire",
            "rock"
        ],
        "hp": 60,
        "attack": 50,
        "defense": 120,
        "attack+": 90,
        "defense+": 80,
        "speed": 30,
        "total": 430
    },
    {
        "name": "swinub",
        "types": [
            "ice",
            "ground"
        ],
        "hp": 50,
        "attack": 50,
        "defense": 40,
        "attack+": 30,
        "defense+": 30,
        "speed": 50,
        "total": 250
    },
    {
        "name": "piloswine",
        "types": [
            "ice",
            "ground"
        ],
        "hp": 100,
        "attack": 100,
        "defense": 80,
        "attack+": 60,
        "defense+": 60,
        "speed": 50,
        "total": 450
    },
    {
        "name": "corsola",
        "types": [
            "water",
            "rock"
        ],
        "hp": 65,
        "attack": 55,
        "defense": 95,
        "attack+": 65,
        "defense+": 95,
        "speed": 35,
        "total": 410
    },
    {
        "name": "remoraid",
        "types": [
            "water"
        ],
        "hp": 35,
        "attack": 65,
        "defense": 35,
        "attack+": 65,
        "defense+": 35,
        "speed": 65,
        "total": 300
    },
    {
        "name": "octillery",
        "types": [
            "water"
        ],
        "hp": 75,
        "attack": 105,
        "defense": 75,
        "attack+": 105,
        "defense+": 75,
        "speed": 45,
        "total": 480
    },
    {
        "name": "delibird",
        "types": [
            "ice",
            "flying"
        ],
        "hp": 45,
        "attack": 55,
        "defense": 45,
        "attack+": 65,
        "defense+": 45,
        "speed": 75,
        "total": 330
    },
    {
        "name": "mantine",
        "types": [
            "water",
            "flying"
        ],
        "hp": 85,
        "attack": 40,
        "defense": 70,
        "attack+": 80,
        "defense+": 140,
        "speed": 70,
        "total": 485
    },
    {
        "name": "skarmory",
        "types": [
            "steel",
            "flying"
        ],
        "hp": 65,
        "attack": 80,
        "defense": 140,
        "attack+": 40,
        "defense+": 70,
        "speed": 70,
        "total": 465
    },
    {
        "name": "houndour",
        "types": [
            "dark",
            "fire"
        ],
        "hp": 45,
        "attack": 60,
        "defense": 30,
        "attack+": 80,
        "defense+": 50,
        "speed": 65,
        "total": 330
    },
    {
        "name": "houndoom",
        "types": [
            "dark",
            "fire"
        ],
        "hp": 75,
        "attack": 90,
        "defense": 50,
        "attack+": 110,
        "defense+": 80,
        "speed": 95,
        "total": 500
    },
    {
        "name": "kingdra",
        "types": [
            "water",
            "dragon"
        ],
        "hp": 75,
        "attack": 95,
        "defense": 95,
        "attack+": 95,
        "defense+": 95,
        "speed": 85,
        "total": 540
    },
    {
        "name": "phanpy",
        "types": [
            "ground"
        ],
        "hp": 90,
        "attack": 60,
        "defense": 60,
        "attack+": 40,
        "defense+": 40,
        "speed": 40,
        "total": 330
    },
    {
        "name": "donphan",
        "types": [
            "ground"
        ],
        "hp": 90,
        "attack": 120,
        "defense": 120,
        "attack+": 60,
        "defense+": 60,
        "speed": 50,
        "total": 500
    },
    {
        "name": "porygon2",
        "types": [
            "normal"
        ],
        "hp": 85,
        "attack": 80,
        "defense": 90,
        "attack+": 105,
        "defense+": 95,
        "speed": 60,
        "total": 515
    },
    {
        "name": "stantler",
        "types": [
            "normal"
        ],
        "hp": 73,
        "attack": 95,
        "defense": 62,
        "attack+": 85,
        "defense+": 65,
        "speed": 85,
        "total": 465
    },
    {
        "name": "smeargle",
        "types": [
            "normal"
        ],
        "hp": 55,
        "attack": 20,
        "defense": 35,
        "attack+": 20,
        "defense+": 45,
        "speed": 75,
        "total": 250
    },
    {
        "name": "tyrogue",
        "types": [
            "fighting"
        ],
        "hp": 35,
        "attack": 35,
        "defense": 35,
        "attack+": 35,
        "defense+": 35,
        "speed": 35,
        "total": 210
    },
    {
        "name": "hitmontop",
        "types": [
            "fighting"
        ],
        "hp": 50,
        "attack": 95,
        "defense": 95,
        "attack+": 35,
        "defense+": 110,
        "speed": 70,
        "total": 455
    },
    {
        "name": "smoochum",
        "types": [
            "ice",
            "psychic"
        ],
        "hp": 45,
        "attack": 30,
        "defense": 15,
        "attack+": 85,
        "defense+": 65,
        "speed": 65,
        "total": 305
    },
    {
        "name": "elekid",
        "types": [
            "electric"
        ],
        "hp": 45,
        "attack": 63,
        "defense": 37,
        "attack+": 65,
        "defense+": 55,
        "speed": 95,
        "total": 360
    },
    {
        "name": "magby",
        "types": [
            "fire"
        ],
        "hp": 45,
        "attack": 75,
        "defense": 37,
        "attack+": 70,
        "defense+": 55,
        "speed": 83,
        "total": 365
    },
    {
        "name": "miltank",
        "types": [
            "normal"
        ],
        "hp": 95,
        "attack": 80,
        "defense": 105,
        "attack+": 40,
        "defense+": 70,
        "speed": 100,
        "total": 490
    },
    {
        "name": "blissey",
        "types": [
            "normal"
        ],
        "hp": 255,
        "attack": 10,
        "defense": 10,
        "attack+": 75,
        "defense+": 135,
        "speed": 55,
        "total": 540
    },
    {
        "name": "raikou",
        "types": [
            "electric"
        ],
        "hp": 90,
        "attack": 85,
        "defense": 75,
        "attack+": 115,
        "defense+": 100,
        "speed": 115,
        "total": 580
    },
    {
        "name": "entei",
        "types": [
            "fire"
        ],
        "hp": 115,
        "attack": 115,
        "defense": 85,
        "attack+": 90,
        "defense+": 75,
        "speed": 100,
        "total": 580
    },
    {
        "name": "suicune",
        "types": [
            "water"
        ],
        "hp": 100,
        "attack": 75,
        "defense": 115,
        "attack+": 90,
        "defense+": 115,
        "speed": 85,
        "total": 580
    },
    {
        "name": "larvitar",
        "types": [
            "rock",
            "ground"
        ],
        "hp": 50,
        "attack": 64,
        "defense": 50,
        "attack+": 45,
        "defense+": 50,
        "speed": 41,
        "total": 300
    },
    {
        "name": "pupitar",
        "types": [
            "rock",
            "ground"
        ],
        "hp": 70,
        "attack": 84,
        "defense": 70,
        "attack+": 65,
        "defense+": 70,
        "speed": 51,
        "total": 410
    },
    {
        "name": "tyranitar",
        "types": [
            "rock",
            "dark"
        ],
        "hp": 100,
        "attack": 134,
        "defense": 110,
        "attack+": 95,
        "defense+": 100,
        "speed": 61,
        "total": 600
    },
    {
        "name": "lugia",
        "types": [
            "psychic",
            "flying"
        ],
        "hp": 106,
        "attack": 90,
        "defense": 130,
        "attack+": 90,
        "defense+": 154,
        "speed": 110,
        "total": 680
    },
    {
        "name": "ho-oh",
        "types": [
            "fire",
            "flying"
        ],
        "hp": 106,
        "attack": 130,
        "defense": 90,
        "attack+": 110,
        "defense+": 154,
        "speed": 90,
        "total": 680
    },
    {
        "name": "celebi",
        "types": [
            "psychic",
            "grass"
        ],
        "hp": 100,
        "attack": 100,
        "defense": 100,
        "attack+": 100,
        "defense+": 100,
        "speed": 100,
        "total": 600
    },
    {
        "name": "treecko",
        "types": [
            "grass"
        ],
        "hp": 40,
        "attack": 45,
        "defense": 35,
        "attack+": 65,
        "defense+": 55,
        "speed": 70,
        "total": 310
    },
    {
        "name": "grovyle",
        "types": [
            "grass"
        ],
        "hp": 50,
        "attack": 65,
        "defense": 45,
        "attack+": 85,
        "defense+": 65,
        "speed": 95,
        "total": 405
    },
    {
        "name": "sceptile",
        "types": [
            "grass"
        ],
        "hp": 70,
        "attack": 85,
        "defense": 65,
        "attack+": 105,
        "defense+": 85,
        "speed": 120,
        "total": 530
    },
    {
        "name": "torchic",
        "types": [
            "fire"
        ],
        "hp": 45,
        "attack": 60,
        "defense": 40,
        "attack+": 70,
        "defense+": 50,
        "speed": 45,
        "total": 310
    },
    {
        "name": "combusken",
        "types": [
            "fire",
            "fighting"
        ],
        "hp": 60,
        "attack": 85,
        "defense": 60,
        "attack+": 85,
        "defense+": 60,
        "speed": 55,
        "total": 405
    },
    {
        "name": "blaziken",
        "types": [
            "fire",
            "fighting"
        ],
        "hp": 80,
        "attack": 120,
        "defense": 70,
        "attack+": 110,
        "defense+": 70,
        "speed": 80,
        "total": 530
    },
    {
        "name": "mudkip",
        "types": [
            "water"
        ],
        "hp": 50,
        "attack": 70,
        "defense": 50,
        "attack+": 50,
        "defense+": 50,
        "speed": 40,
        "total": 310
    },
    {
        "name": "marshtomp",
        "types": [
            "water",
            "ground"
        ],
        "hp": 70,
        "attack": 85,
        "defense": 70,
        "attack+": 60,
        "defense+": 70,
        "speed": 50,
        "total": 405
    },
    {
        "name": "swampert",
        "types": [
            "water",
            "ground"
        ],
        "hp": 100,
        "attack": 110,
        "defense": 90,
        "attack+": 85,
        "defense+": 90,
        "speed": 60,
        "total": 535
    },
    {
        "name": "poochyena",
        "types": [
            "dark"
        ],
        "hp": 35,
        "attack": 55,
        "defense": 35,
        "attack+": 30,
        "defense+": 30,
        "speed": 35,
        "total": 220
    },
    {
        "name": "mightyena",
        "types": [
            "dark"
        ],
        "hp": 70,
        "attack": 90,
        "defense": 70,
        "attack+": 60,
        "defense+": 60,
        "speed": 70,
        "total": 420
    },
    {
        "name": "zigzagoon",
        "types": [
            "normal"
        ],
        "hp": 38,
        "attack": 30,
        "defense": 41,
        "attack+": 30,
        "defense+": 41,
        "speed": 60,
        "total": 240
    },
    {
        "name": "linoone",
        "types": [
            "normal"
        ],
        "hp": 78,
        "attack": 70,
        "defense": 61,
        "attack+": 50,
        "defense+": 61,
        "speed": 100,
        "total": 420
    },
    {
        "name": "wurmple",
        "types": [
            "bug"
        ],
        "hp": 45,
        "attack": 45,
        "defense": 35,
        "attack+": 20,
        "defense+": 30,
        "speed": 20,
        "total": 195
    },
    {
        "name": "silcoon",
        "types": [
            "bug"
        ],
        "hp": 50,
        "attack": 35,
        "defense": 55,
        "attack+": 25,
        "defense+": 25,
        "speed": 15,
        "total": 205
    },
    {
        "name": "beautifly",
        "types": [
            "bug",
            "flying"
        ],
        "hp": 60,
        "attack": 70,
        "defense": 50,
        "attack+": 100,
        "defense+": 50,
        "speed": 65,
        "total": 395
    },
    {
        "name": "cascoon",
        "types": [
            "bug"
        ],
        "hp": 50,
        "attack": 35,
        "defense": 55,
        "attack+": 25,
        "defense+": 25,
        "speed": 15,
        "total": 205
    },
    {
        "name": "dustox",
        "types": [
            "bug",
            "poison"
        ],
        "hp": 60,
        "attack": 50,
        "defense": 70,
        "attack+": 50,
        "defense+": 90,
        "speed": 65,
        "total": 385
    },
    {
        "name": "lotad",
        "types": [
            "water",
            "grass"
        ],
        "hp": 40,
        "attack": 30,
        "defense": 30,
        "attack+": 40,
        "defense+": 50,
        "speed": 30,
        "total": 220
    },
    {
        "name": "lombre",
        "types": [
            "water",
            "grass"
        ],
        "hp": 60,
        "attack": 50,
        "defense": 50,
        "attack+": 60,
        "defense+": 70,
        "speed": 50,
        "total": 340
    },
    {
        "name": "ludicolo",
        "types": [
            "water",
            "grass"
        ],
        "hp": 80,
        "attack": 70,
        "defense": 70,
        "attack+": 90,
        "defense+": 100,
        "speed": 70,
        "total": 480
    },
    {
        "name": "seedot",
        "types": [
            "grass"
        ],
        "hp": 40,
        "attack": 40,
        "defense": 50,
        "attack+": 30,
        "defense+": 30,
        "speed": 30,
        "total": 220
    },
    {
        "name": "nuzleaf",
        "types": [
            "grass",
            "dark"
        ],
        "hp": 70,
        "attack": 70,
        "defense": 40,
        "attack+": 60,
        "defense+": 40,
        "speed": 60,
        "total": 340
    },
    {
        "name": "shiftry",
        "types": [
            "grass",
            "dark"
        ],
        "hp": 90,
        "attack": 100,
        "defense": 60,
        "attack+": 90,
        "defense+": 60,
        "speed": 80,
        "total": 480
    },
    {
        "name": "taillow",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 40,
        "attack": 55,
        "defense": 30,
        "attack+": 30,
        "defense+": 30,
        "speed": 85,
        "total": 270
    },
    {
        "name": "swellow",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 60,
        "attack": 85,
        "defense": 60,
        "attack+": 75,
        "defense+": 50,
        "speed": 125,
        "total": 455
    },
    {
        "name": "wingull",
        "types": [
            "water",
            "flying"
        ],
        "hp": 40,
        "attack": 30,
        "defense": 30,
        "attack+": 55,
        "defense+": 30,
        "speed": 85,
        "total": 270
    },
    {
        "name": "pelipper",
        "types": [
            "water",
            "flying"
        ],
        "hp": 60,
        "attack": 50,
        "defense": 100,
        "attack+": 95,
        "defense+": 70,
        "speed": 65,
        "total": 440
    },
    {
        "name": "ralts",
        "types": [
            "psychic",
            "fairy"
        ],
        "hp": 28,
        "attack": 25,
        "defense": 25,
        "attack+": 45,
        "defense+": 35,
        "speed": 40,
        "total": 198
    },
    {
        "name": "kirlia",
        "types": [
            "psychic",
            "fairy"
        ],
        "hp": 38,
        "attack": 35,
        "defense": 35,
        "attack+": 65,
        "defense+": 55,
        "speed": 50,
        "total": 278
    },
    {
        "name": "gardevoir",
        "types": [
            "psychic",
            "fairy"
        ],
        "hp": 68,
        "attack": 65,
        "defense": 65,
        "attack+": 125,
        "defense+": 115,
        "speed": 80,
        "total": 518
    },
    {
        "name": "surskit",
        "types": [
            "bug",
            "water"
        ],
        "hp": 40,
        "attack": 30,
        "defense": 32,
        "attack+": 50,
        "defense+": 52,
        "speed": 65,
        "total": 269
    },
    {
        "name": "masquerain",
        "types": [
            "bug",
            "flying"
        ],
        "hp": 70,
        "attack": 60,
        "defense": 62,
        "attack+": 100,
        "defense+": 82,
        "speed": 80,
        "total": 454
    },
    {
        "name": "shroomish",
        "types": [
            "grass"
        ],
        "hp": 60,
        "attack": 40,
        "defense": 60,
        "attack+": 40,
        "defense+": 60,
        "speed": 35,
        "total": 295
    },
    {
        "name": "breloom",
        "types": [
            "grass",
            "fighting"
        ],
        "hp": 60,
        "attack": 130,
        "defense": 80,
        "attack+": 60,
        "defense+": 60,
        "speed": 70,
        "total": 460
    },
    {
        "name": "slakoth",
        "types": [
            "normal"
        ],
        "hp": 60,
        "attack": 60,
        "defense": 60,
        "attack+": 35,
        "defense+": 35,
        "speed": 30,
        "total": 280
    },
    {
        "name": "vigoroth",
        "types": [
            "normal"
        ],
        "hp": 80,
        "attack": 80,
        "defense": 80,
        "attack+": 55,
        "defense+": 55,
        "speed": 90,
        "total": 440
    },
    {
        "name": "slaking",
        "types": [
            "normal"
        ],
        "hp": 150,
        "attack": 160,
        "defense": 100,
        "attack+": 95,
        "defense+": 65,
        "speed": 100,
        "total": 670
    },
    {
        "name": "nincada",
        "types": [
            "bug",
            "ground"
        ],
        "hp": 31,
        "attack": 45,
        "defense": 90,
        "attack+": 30,
        "defense+": 30,
        "speed": 40,
        "total": 266
    },
    {
        "name": "ninjask",
        "types": [
            "bug",
            "flying"
        ],
        "hp": 61,
        "attack": 90,
        "defense": 45,
        "attack+": 50,
        "defense+": 50,
        "speed": 160,
        "total": 456
    },
    {
        "name": "shedinja",
        "types": [
            "bug",
            "ghost"
        ],
        "hp": 1,
        "attack": 90,
        "defense": 45,
        "attack+": 30,
        "defense+": 30,
        "speed": 40,
        "total": 236
    },
    {
        "name": "whismur",
        "types": [
            "normal"
        ],
        "hp": 64,
        "attack": 51,
        "defense": 23,
        "attack+": 51,
        "defense+": 23,
        "speed": 28,
        "total": 240
    },
    {
        "name": "loudred",
        "types": [
            "normal"
        ],
        "hp": 84,
        "attack": 71,
        "defense": 43,
        "attack+": 71,
        "defense+": 43,
        "speed": 48,
        "total": 360
    },
    {
        "name": "exploud",
        "types": [
            "normal"
        ],
        "hp": 104,
        "attack": 91,
        "defense": 63,
        "attack+": 91,
        "defense+": 73,
        "speed": 68,
        "total": 490
    },
    {
        "name": "makuhita",
        "types": [
            "fighting"
        ],
        "hp": 72,
        "attack": 60,
        "defense": 30,
        "attack+": 20,
        "defense+": 30,
        "speed": 25,
        "total": 237
    },
    {
        "name": "hariyama",
        "types": [
            "fighting"
        ],
        "hp": 144,
        "attack": 120,
        "defense": 60,
        "attack+": 40,
        "defense+": 60,
        "speed": 50,
        "total": 474
    },
    {
        "name": "azurill",
        "types": [
            "normal",
            "fairy"
        ],
        "hp": 50,
        "attack": 20,
        "defense": 40,
        "attack+": 20,
        "defense+": 40,
        "speed": 20,
        "total": 190
    },
    {
        "name": "nosepass",
        "types": [
            "rock"
        ],
        "hp": 30,
        "attack": 45,
        "defense": 135,
        "attack+": 45,
        "defense+": 90,
        "speed": 30,
        "total": 375
    },
    {
        "name": "skitty",
        "types": [
            "normal"
        ],
        "hp": 50,
        "attack": 45,
        "defense": 45,
        "attack+": 35,
        "defense+": 35,
        "speed": 50,
        "total": 260
    },
    {
        "name": "delcatty",
        "types": [
            "normal"
        ],
        "hp": 70,
        "attack": 65,
        "defense": 65,
        "attack+": 55,
        "defense+": 55,
        "speed": 90,
        "total": 400
    },
    {
        "name": "sableye",
        "types": [
            "dark",
            "ghost"
        ],
        "hp": 50,
        "attack": 75,
        "defense": 75,
        "attack+": 65,
        "defense+": 65,
        "speed": 50,
        "total": 380
    },
    {
        "name": "mawile",
        "types": [
            "steel",
            "fairy"
        ],
        "hp": 50,
        "attack": 85,
        "defense": 85,
        "attack+": 55,
        "defense+": 55,
        "speed": 50,
        "total": 380
    },
    {
        "name": "aron",
        "types": [
            "steel",
            "rock"
        ],
        "hp": 50,
        "attack": 70,
        "defense": 100,
        "attack+": 40,
        "defense+": 40,
        "speed": 30,
        "total": 330
    },
    {
        "name": "lairon",
        "types": [
            "steel",
            "rock"
        ],
        "hp": 60,
        "attack": 90,
        "defense": 140,
        "attack+": 50,
        "defense+": 50,
        "speed": 40,
        "total": 430
    },
    {
        "name": "aggron",
        "types": [
            "steel",
            "rock"
        ],
        "hp": 70,
        "attack": 110,
        "defense": 180,
        "attack+": 60,
        "defense+": 60,
        "speed": 50,
        "total": 530
    },
    {
        "name": "meditite",
        "types": [
            "fighting",
            "psychic"
        ],
        "hp": 30,
        "attack": 40,
        "defense": 55,
        "attack+": 40,
        "defense+": 55,
        "speed": 60,
        "total": 280
    },
    {
        "name": "medicham",
        "types": [
            "fighting",
            "psychic"
        ],
        "hp": 60,
        "attack": 60,
        "defense": 75,
        "attack+": 60,
        "defense+": 75,
        "speed": 80,
        "total": 410
    },
    {
        "name": "electrike",
        "types": [
            "electric"
        ],
        "hp": 40,
        "attack": 45,
        "defense": 40,
        "attack+": 65,
        "defense+": 40,
        "speed": 65,
        "total": 295
    },
    {
        "name": "manectric",
        "types": [
            "electric"
        ],
        "hp": 70,
        "attack": 75,
        "defense": 60,
        "attack+": 105,
        "defense+": 60,
        "speed": 105,
        "total": 475
    },
    {
        "name": "plusle",
        "types": [
            "electric"
        ],
        "hp": 60,
        "attack": 50,
        "defense": 40,
        "attack+": 85,
        "defense+": 75,
        "speed": 95,
        "total": 405
    },
    {
        "name": "minun",
        "types": [
            "electric"
        ],
        "hp": 60,
        "attack": 40,
        "defense": 50,
        "attack+": 75,
        "defense+": 85,
        "speed": 95,
        "total": 405
    },
    {
        "name": "volbeat",
        "types": [
            "bug"
        ],
        "hp": 65,
        "attack": 73,
        "defense": 75,
        "attack+": 47,
        "defense+": 85,
        "speed": 85,
        "total": 430
    },
    {
        "name": "illumise",
        "types": [
            "bug"
        ],
        "hp": 65,
        "attack": 47,
        "defense": 75,
        "attack+": 73,
        "defense+": 85,
        "speed": 85,
        "total": 430
    },
    {
        "name": "roselia",
        "types": [
            "grass",
            "poison"
        ],
        "hp": 50,
        "attack": 60,
        "defense": 45,
        "attack+": 100,
        "defense+": 80,
        "speed": 65,
        "total": 400
    },
    {
        "name": "gulpin",
        "types": [
            "poison"
        ],
        "hp": 70,
        "attack": 43,
        "defense": 53,
        "attack+": 43,
        "defense+": 53,
        "speed": 40,
        "total": 302
    },
    {
        "name": "swalot",
        "types": [
            "poison"
        ],
        "hp": 100,
        "attack": 73,
        "defense": 83,
        "attack+": 73,
        "defense+": 83,
        "speed": 55,
        "total": 467
    },
    {
        "name": "carvanha",
        "types": [
            "water",
            "dark"
        ],
        "hp": 45,
        "attack": 90,
        "defense": 20,
        "attack+": 65,
        "defense+": 20,
        "speed": 65,
        "total": 305
    },
    {
        "name": "sharpedo",
        "types": [
            "water",
            "dark"
        ],
        "hp": 70,
        "attack": 120,
        "defense": 40,
        "attack+": 95,
        "defense+": 40,
        "speed": 95,
        "total": 460
    },
    {
        "name": "wailmer",
        "types": [
            "water"
        ],
        "hp": 130,
        "attack": 70,
        "defense": 35,
        "attack+": 70,
        "defense+": 35,
        "speed": 60,
        "total": 400
    },
    {
        "name": "wailord",
        "types": [
            "water"
        ],
        "hp": 170,
        "attack": 90,
        "defense": 45,
        "attack+": 90,
        "defense+": 45,
        "speed": 60,
        "total": 500
    },
    {
        "name": "numel",
        "types": [
            "fire",
            "ground"
        ],
        "hp": 60,
        "attack": 60,
        "defense": 40,
        "attack+": 65,
        "defense+": 45,
        "speed": 35,
        "total": 305
    },
    {
        "name": "camerupt",
        "types": [
            "fire",
            "ground"
        ],
        "hp": 70,
        "attack": 100,
        "defense": 70,
        "attack+": 105,
        "defense+": 75,
        "speed": 40,
        "total": 460
    },
    {
        "name": "torkoal",
        "types": [
            "fire"
        ],
        "hp": 70,
        "attack": 85,
        "defense": 140,
        "attack+": 85,
        "defense+": 70,
        "speed": 20,
        "total": 470
    },
    {
        "name": "spoink",
        "types": [
            "psychic"
        ],
        "hp": 60,
        "attack": 25,
        "defense": 35,
        "attack+": 70,
        "defense+": 80,
        "speed": 60,
        "total": 330
    },
    {
        "name": "grumpig",
        "types": [
            "psychic"
        ],
        "hp": 80,
        "attack": 45,
        "defense": 65,
        "attack+": 90,
        "defense+": 110,
        "speed": 80,
        "total": 470
    },
    {
        "name": "spinda",
        "types": [
            "normal"
        ],
        "hp": 60,
        "attack": 60,
        "defense": 60,
        "attack+": 60,
        "defense+": 60,
        "speed": 60,
        "total": 360
    },
    {
        "name": "trapinch",
        "types": [
            "ground"
        ],
        "hp": 45,
        "attack": 100,
        "defense": 45,
        "attack+": 45,
        "defense+": 45,
        "speed": 10,
        "total": 290
    },
    {
        "name": "vibrava",
        "types": [
            "ground",
            "dragon"
        ],
        "hp": 50,
        "attack": 70,
        "defense": 50,
        "attack+": 50,
        "defense+": 50,
        "speed": 70,
        "total": 340
    },
    {
        "name": "flygon",
        "types": [
            "ground",
            "dragon"
        ],
        "hp": 80,
        "attack": 100,
        "defense": 80,
        "attack+": 80,
        "defense+": 80,
        "speed": 100,
        "total": 520
    },
    {
        "name": "cacnea",
        "types": [
            "grass"
        ],
        "hp": 50,
        "attack": 85,
        "defense": 40,
        "attack+": 85,
        "defense+": 40,
        "speed": 35,
        "total": 335
    },
    {
        "name": "cacturne",
        "types": [
            "grass",
            "dark"
        ],
        "hp": 70,
        "attack": 115,
        "defense": 60,
        "attack+": 115,
        "defense+": 60,
        "speed": 55,
        "total": 475
    },
    {
        "name": "swablu",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 45,
        "attack": 40,
        "defense": 60,
        "attack+": 40,
        "defense+": 75,
        "speed": 50,
        "total": 310
    },
    {
        "name": "altaria",
        "types": [
            "dragon",
            "flying"
        ],
        "hp": 75,
        "attack": 70,
        "defense": 90,
        "attack+": 70,
        "defense+": 105,
        "speed": 80,
        "total": 490
    },
    {
        "name": "zangoose",
        "types": [
            "normal"
        ],
        "hp": 73,
        "attack": 115,
        "defense": 60,
        "attack+": 60,
        "defense+": 60,
        "speed": 90,
        "total": 458
    },
    {
        "name": "seviper",
        "types": [
            "poison"
        ],
        "hp": 73,
        "attack": 100,
        "defense": 60,
        "attack+": 100,
        "defense+": 60,
        "speed": 65,
        "total": 458
    },
    {
        "name": "lunatone",
        "types": [
            "rock",
            "psychic"
        ],
        "hp": 90,
        "attack": 55,
        "defense": 65,
        "attack+": 95,
        "defense+": 85,
        "speed": 70,
        "total": 460
    },
    {
        "name": "solrock",
        "types": [
            "rock",
            "psychic"
        ],
        "hp": 90,
        "attack": 95,
        "defense": 85,
        "attack+": 55,
        "defense+": 65,
        "speed": 70,
        "total": 460
    },
    {
        "name": "barboach",
        "types": [
            "water",
            "ground"
        ],
        "hp": 50,
        "attack": 48,
        "defense": 43,
        "attack+": 46,
        "defense+": 41,
        "speed": 60,
        "total": 288
    },
    {
        "name": "whiscash",
        "types": [
            "water",
            "ground"
        ],
        "hp": 110,
        "attack": 78,
        "defense": 73,
        "attack+": 76,
        "defense+": 71,
        "speed": 60,
        "total": 468
    },
    {
        "name": "corphish",
        "types": [
            "water"
        ],
        "hp": 43,
        "attack": 80,
        "defense": 65,
        "attack+": 50,
        "defense+": 35,
        "speed": 35,
        "total": 308
    },
    {
        "name": "crawdaunt",
        "types": [
            "water",
            "dark"
        ],
        "hp": 63,
        "attack": 120,
        "defense": 85,
        "attack+": 90,
        "defense+": 55,
        "speed": 55,
        "total": 468
    },
    {
        "name": "baltoy",
        "types": [
            "ground",
            "psychic"
        ],
        "hp": 40,
        "attack": 40,
        "defense": 55,
        "attack+": 40,
        "defense+": 70,
        "speed": 55,
        "total": 300
    },
    {
        "name": "claydol",
        "types": [
            "ground",
            "psychic"
        ],
        "hp": 60,
        "attack": 70,
        "defense": 105,
        "attack+": 70,
        "defense+": 120,
        "speed": 75,
        "total": 500
    },
    {
        "name": "lileep",
        "types": [
            "rock",
            "grass"
        ],
        "hp": 66,
        "attack": 41,
        "defense": 77,
        "attack+": 61,
        "defense+": 87,
        "speed": 23,
        "total": 355
    },
    {
        "name": "cradily",
        "types": [
            "rock",
            "grass"
        ],
        "hp": 86,
        "attack": 81,
        "defense": 97,
        "attack+": 81,
        "defense+": 107,
        "speed": 43,
        "total": 495
    },
    {
        "name": "anorith",
        "types": [
            "rock",
            "bug"
        ],
        "hp": 45,
        "attack": 95,
        "defense": 50,
        "attack+": 40,
        "defense+": 50,
        "speed": 75,
        "total": 355
    },
    {
        "name": "armaldo",
        "types": [
            "rock",
            "bug"
        ],
        "hp": 75,
        "attack": 125,
        "defense": 100,
        "attack+": 70,
        "defense+": 80,
        "speed": 45,
        "total": 495
    },
    {
        "name": "feebas",
        "types": [
            "water"
        ],
        "hp": 20,
        "attack": 15,
        "defense": 20,
        "attack+": 10,
        "defense+": 55,
        "speed": 80,
        "total": 200
    },
    {
        "name": "milotic",
        "types": [
            "water"
        ],
        "hp": 95,
        "attack": 60,
        "defense": 79,
        "attack+": 100,
        "defense+": 125,
        "speed": 81,
        "total": 540
    },
    {
        "name": "castform",
        "types": [
            "normal"
        ],
        "hp": 70,
        "attack": 70,
        "defense": 70,
        "attack+": 70,
        "defense+": 70,
        "speed": 70,
        "total": 420
    },
    {
        "name": "kecleon",
        "types": [
            "normal"
        ],
        "hp": 60,
        "attack": 90,
        "defense": 70,
        "attack+": 60,
        "defense+": 120,
        "speed": 40,
        "total": 440
    },
    {
        "name": "shuppet",
        "types": [
            "ghost"
        ],
        "hp": 44,
        "attack": 75,
        "defense": 35,
        "attack+": 63,
        "defense+": 33,
        "speed": 45,
        "total": 295
    },
    {
        "name": "banette",
        "types": [
            "ghost"
        ],
        "hp": 64,
        "attack": 115,
        "defense": 65,
        "attack+": 83,
        "defense+": 63,
        "speed": 65,
        "total": 455
    },
    {
        "name": "duskull",
        "types": [
            "ghost"
        ],
        "hp": 20,
        "attack": 40,
        "defense": 90,
        "attack+": 30,
        "defense+": 90,
        "speed": 25,
        "total": 295
    },
    {
        "name": "dusclops",
        "types": [
            "ghost"
        ],
        "hp": 40,
        "attack": 70,
        "defense": 130,
        "attack+": 60,
        "defense+": 130,
        "speed": 25,
        "total": 455
    },
    {
        "name": "tropius",
        "types": [
            "grass",
            "flying"
        ],
        "hp": 99,
        "attack": 68,
        "defense": 83,
        "attack+": 72,
        "defense+": 87,
        "speed": 51,
        "total": 460
    },
    {
        "name": "chimecho",
        "types": [
            "psychic"
        ],
        "hp": 75,
        "attack": 50,
        "defense": 80,
        "attack+": 95,
        "defense+": 90,
        "speed": 65,
        "total": 455
    },
    {
        "name": "absol",
        "types": [
            "dark"
        ],
        "hp": 65,
        "attack": 130,
        "defense": 60,
        "attack+": 75,
        "defense+": 60,
        "speed": 75,
        "total": 465
    },
    {
        "name": "wynaut",
        "types": [
            "psychic"
        ],
        "hp": 95,
        "attack": 23,
        "defense": 48,
        "attack+": 23,
        "defense+": 48,
        "speed": 23,
        "total": 260
    },
    {
        "name": "snorunt",
        "types": [
            "ice"
        ],
        "hp": 50,
        "attack": 50,
        "defense": 50,
        "attack+": 50,
        "defense+": 50,
        "speed": 50,
        "total": 300
    },
    {
        "name": "glalie",
        "types": [
            "ice"
        ],
        "hp": 80,
        "attack": 80,
        "defense": 80,
        "attack+": 80,
        "defense+": 80,
        "speed": 80,
        "total": 480
    },
    {
        "name": "spheal",
        "types": [
            "ice",
            "water"
        ],
        "hp": 70,
        "attack": 40,
        "defense": 50,
        "attack+": 55,
        "defense+": 50,
        "speed": 25,
        "total": 290
    },
    {
        "name": "sealeo",
        "types": [
            "ice",
            "water"
        ],
        "hp": 90,
        "attack": 60,
        "defense": 70,
        "attack+": 75,
        "defense+": 70,
        "speed": 45,
        "total": 410
    },
    {
        "name": "walrein",
        "types": [
            "ice",
            "water"
        ],
        "hp": 110,
        "attack": 80,
        "defense": 90,
        "attack+": 95,
        "defense+": 90,
        "speed": 65,
        "total": 530
    },
    {
        "name": "clamperl",
        "types": [
            "water"
        ],
        "hp": 35,
        "attack": 64,
        "defense": 85,
        "attack+": 74,
        "defense+": 55,
        "speed": 32,
        "total": 345
    },
    {
        "name": "huntail",
        "types": [
            "water"
        ],
        "hp": 55,
        "attack": 104,
        "defense": 105,
        "attack+": 94,
        "defense+": 75,
        "speed": 52,
        "total": 485
    },
    {
        "name": "gorebyss",
        "types": [
            "water"
        ],
        "hp": 55,
        "attack": 84,
        "defense": 105,
        "attack+": 114,
        "defense+": 75,
        "speed": 52,
        "total": 485
    },
    {
        "name": "relicanth",
        "types": [
            "water",
            "rock"
        ],
        "hp": 100,
        "attack": 90,
        "defense": 130,
        "attack+": 45,
        "defense+": 65,
        "speed": 55,
        "total": 485
    },
    {
        "name": "luvdisc",
        "types": [
            "water"
        ],
        "hp": 43,
        "attack": 30,
        "defense": 55,
        "attack+": 40,
        "defense+": 65,
        "speed": 97,
        "total": 330
    },
    {
        "name": "bagon",
        "types": [
            "dragon"
        ],
        "hp": 45,
        "attack": 75,
        "defense": 60,
        "attack+": 40,
        "defense+": 30,
        "speed": 50,
        "total": 300
    },
    {
        "name": "shelgon",
        "types": [
            "dragon"
        ],
        "hp": 65,
        "attack": 95,
        "defense": 100,
        "attack+": 60,
        "defense+": 50,
        "speed": 50,
        "total": 420
    },
    {
        "name": "salamence",
        "types": [
            "dragon",
            "flying"
        ],
        "hp": 95,
        "attack": 135,
        "defense": 80,
        "attack+": 110,
        "defense+": 80,
        "speed": 100,
        "total": 600
    },
    {
        "name": "beldum",
        "types": [
            "steel",
            "psychic"
        ],
        "hp": 40,
        "attack": 55,
        "defense": 80,
        "attack+": 35,
        "defense+": 60,
        "speed": 30,
        "total": 300
    },
    {
        "name": "metang",
        "types": [
            "steel",
            "psychic"
        ],
        "hp": 60,
        "attack": 75,
        "defense": 100,
        "attack+": 55,
        "defense+": 80,
        "speed": 50,
        "total": 420
    },
    {
        "name": "metagross",
        "types": [
            "steel",
            "psychic"
        ],
        "hp": 80,
        "attack": 135,
        "defense": 130,
        "attack+": 95,
        "defense+": 90,
        "speed": 70,
        "total": 600
    },
    {
        "name": "regirock",
        "types": [
            "rock"
        ],
        "hp": 80,
        "attack": 100,
        "defense": 200,
        "attack+": 50,
        "defense+": 100,
        "speed": 50,
        "total": 580
    },
    {
        "name": "regice",
        "types": [
            "ice"
        ],
        "hp": 80,
        "attack": 50,
        "defense": 100,
        "attack+": 100,
        "defense+": 200,
        "speed": 50,
        "total": 580
    },
    {
        "name": "registeel",
        "types": [
            "steel"
        ],
        "hp": 80,
        "attack": 75,
        "defense": 150,
        "attack+": 75,
        "defense+": 150,
        "speed": 50,
        "total": 580
    },
    {
        "name": "latias",
        "types": [
            "dragon",
            "psychic"
        ],
        "hp": 80,
        "attack": 80,
        "defense": 90,
        "attack+": 110,
        "defense+": 130,
        "speed": 110,
        "total": 600
    },
    {
        "name": "latios",
        "types": [
            "dragon",
            "psychic"
        ],
        "hp": 80,
        "attack": 90,
        "defense": 80,
        "attack+": 130,
        "defense+": 110,
        "speed": 110,
        "total": 600
    },
    {
        "name": "kyogre",
        "types": [
            "water"
        ],
        "hp": 100,
        "attack": 100,
        "defense": 90,
        "attack+": 150,
        "defense+": 140,
        "speed": 90,
        "total": 670
    },
    {
        "name": "groudon",
        "types": [
            "ground"
        ],
        "hp": 100,
        "attack": 150,
        "defense": 140,
        "attack+": 100,
        "defense+": 90,
        "speed": 90,
        "total": 670
    },
    {
        "name": "rayquaza",
        "types": [
            "dragon",
            "flying"
        ],
        "hp": 105,
        "attack": 150,
        "defense": 90,
        "attack+": 150,
        "defense+": 90,
        "speed": 95,
        "total": 680
    },
    {
        "name": "jirachi",
        "types": [
            "steel",
            "psychic"
        ],
        "hp": 100,
        "attack": 100,
        "defense": 100,
        "attack+": 100,
        "defense+": 100,
        "speed": 100,
        "total": 600
    },
    {
        "name": "deoxys",
        "types": [
            "psychic"
        ],
        "hp": 50,
        "attack": 150,
        "defense": 50,
        "attack+": 150,
        "defense+": 50,
        "speed": 150,
        "total": 600
    },
    {
        "name": "turtwig",
        "types": [
            "grass"
        ],
        "hp": 55,
        "attack": 68,
        "defense": 64,
        "attack+": 45,
        "defense+": 55,
        "speed": 31,
        "total": 318
    },
    {
        "name": "grotle",
        "types": [
            "grass"
        ],
        "hp": 75,
        "attack": 89,
        "defense": 85,
        "attack+": 55,
        "defense+": 65,
        "speed": 36,
        "total": 405
    },
    {
        "name": "torterra",
        "types": [
            "grass",
            "ground"
        ],
        "hp": 95,
        "attack": 109,
        "defense": 105,
        "attack+": 75,
        "defense+": 85,
        "speed": 56,
        "total": 525
    },
    {
        "name": "chimchar",
        "types": [
            "fire"
        ],
        "hp": 44,
        "attack": 58,
        "defense": 44,
        "attack+": 58,
        "defense+": 44,
        "speed": 61,
        "total": 309
    },
    {
        "name": "monferno",
        "types": [
            "fire",
            "fighting"
        ],
        "hp": 64,
        "attack": 78,
        "defense": 52,
        "attack+": 78,
        "defense+": 52,
        "speed": 81,
        "total": 405
    },
    {
        "name": "infernape",
        "types": [
            "fire",
            "fighting"
        ],
        "hp": 76,
        "attack": 104,
        "defense": 71,
        "attack+": 104,
        "defense+": 71,
        "speed": 108,
        "total": 534
    },
    {
        "name": "piplup",
        "types": [
            "water"
        ],
        "hp": 53,
        "attack": 51,
        "defense": 53,
        "attack+": 61,
        "defense+": 56,
        "speed": 40,
        "total": 314
    },
    {
        "name": "prinplup",
        "types": [
            "water"
        ],
        "hp": 64,
        "attack": 66,
        "defense": 68,
        "attack+": 81,
        "defense+": 76,
        "speed": 50,
        "total": 405
    },
    {
        "name": "empoleon",
        "types": [
            "water",
            "steel"
        ],
        "hp": 84,
        "attack": 86,
        "defense": 88,
        "attack+": 111,
        "defense+": 101,
        "speed": 60,
        "total": 530
    },
    {
        "name": "starly",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 40,
        "attack": 55,
        "defense": 30,
        "attack+": 30,
        "defense+": 30,
        "speed": 60,
        "total": 245
    },
    {
        "name": "staravia",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 55,
        "attack": 75,
        "defense": 50,
        "attack+": 40,
        "defense+": 40,
        "speed": 80,
        "total": 340
    },
    {
        "name": "staraptor",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 85,
        "attack": 120,
        "defense": 70,
        "attack+": 50,
        "defense+": 60,
        "speed": 100,
        "total": 485
    },
    {
        "name": "bidoof",
        "types": [
            "normal"
        ],
        "hp": 59,
        "attack": 45,
        "defense": 40,
        "attack+": 35,
        "defense+": 40,
        "speed": 31,
        "total": 250
    },
    {
        "name": "bibarel",
        "types": [
            "normal",
            "water"
        ],
        "hp": 79,
        "attack": 85,
        "defense": 60,
        "attack+": 55,
        "defense+": 60,
        "speed": 71,
        "total": 410
    },
    {
        "name": "kricketot",
        "types": [
            "bug"
        ],
        "hp": 37,
        "attack": 25,
        "defense": 41,
        "attack+": 25,
        "defense+": 41,
        "speed": 25,
        "total": 194
    },
    {
        "name": "kricketune",
        "types": [
            "bug"
        ],
        "hp": 77,
        "attack": 85,
        "defense": 51,
        "attack+": 55,
        "defense+": 51,
        "speed": 65,
        "total": 384
    },
    {
        "name": "shinx",
        "types": [
            "electric"
        ],
        "hp": 45,
        "attack": 65,
        "defense": 34,
        "attack+": 40,
        "defense+": 34,
        "speed": 45,
        "total": 263
    },
    {
        "name": "luxio",
        "types": [
            "electric"
        ],
        "hp": 60,
        "attack": 85,
        "defense": 49,
        "attack+": 60,
        "defense+": 49,
        "speed": 60,
        "total": 363
    },
    {
        "name": "luxray",
        "types": [
            "electric"
        ],
        "hp": 80,
        "attack": 120,
        "defense": 79,
        "attack+": 95,
        "defense+": 79,
        "speed": 70,
        "total": 523
    },
    {
        "name": "budew",
        "types": [
            "grass",
            "poison"
        ],
        "hp": 40,
        "attack": 30,
        "defense": 35,
        "attack+": 50,
        "defense+": 70,
        "speed": 55,
        "total": 280
    },
    {
        "name": "roserade",
        "types": [
            "grass",
            "poison"
        ],
        "hp": 60,
        "attack": 70,
        "defense": 65,
        "attack+": 125,
        "defense+": 105,
        "speed": 90,
        "total": 515
    },
    {
        "name": "cranidos",
        "types": [
            "rock"
        ],
        "hp": 67,
        "attack": 125,
        "defense": 40,
        "attack+": 30,
        "defense+": 30,
        "speed": 58,
        "total": 350
    },
    {
        "name": "rampardos",
        "types": [
            "rock"
        ],
        "hp": 97,
        "attack": 165,
        "defense": 60,
        "attack+": 65,
        "defense+": 50,
        "speed": 58,
        "total": 495
    },
    {
        "name": "shieldon",
        "types": [
            "rock",
            "steel"
        ],
        "hp": 30,
        "attack": 42,
        "defense": 118,
        "attack+": 42,
        "defense+": 88,
        "speed": 30,
        "total": 350
    },
    {
        "name": "bastiodon",
        "types": [
            "rock",
            "steel"
        ],
        "hp": 60,
        "attack": 52,
        "defense": 168,
        "attack+": 47,
        "defense+": 138,
        "speed": 30,
        "total": 495
    },
    {
        "name": "burmy",
        "types": [
            "bug"
        ],
        "hp": 40,
        "attack": 29,
        "defense": 45,
        "attack+": 29,
        "defense+": 45,
        "speed": 36,
        "total": 224
    },
    {
        "name": "wormadam",
        "types": [
            "bug",
            "grass"
        ],
        "hp": 60,
        "attack": 59,
        "defense": 85,
        "attack+": 79,
        "defense+": 105,
        "speed": 36,
        "total": 424
    },
    {
        "name": "mothim",
        "types": [
            "bug",
            "flying"
        ],
        "hp": 70,
        "attack": 94,
        "defense": 50,
        "attack+": 94,
        "defense+": 50,
        "speed": 66,
        "total": 424
    },
    {
        "name": "combee",
        "types": [
            "bug",
            "flying"
        ],
        "hp": 30,
        "attack": 30,
        "defense": 42,
        "attack+": 30,
        "defense+": 42,
        "speed": 70,
        "total": 244
    },
    {
        "name": "vespiquen",
        "types": [
            "bug",
            "flying"
        ],
        "hp": 70,
        "attack": 80,
        "defense": 102,
        "attack+": 80,
        "defense+": 102,
        "speed": 40,
        "total": 474
    },
    {
        "name": "pachirisu",
        "types": [
            "electric"
        ],
        "hp": 60,
        "attack": 45,
        "defense": 70,
        "attack+": 45,
        "defense+": 90,
        "speed": 95,
        "total": 405
    },
    {
        "name": "buizel",
        "types": [
            "water"
        ],
        "hp": 55,
        "attack": 65,
        "defense": 35,
        "attack+": 60,
        "defense+": 30,
        "speed": 85,
        "total": 330
    },
    {
        "name": "floatzel",
        "types": [
            "water"
        ],
        "hp": 85,
        "attack": 105,
        "defense": 55,
        "attack+": 85,
        "defense+": 50,
        "speed": 115,
        "total": 495
    },
    {
        "name": "cherubi",
        "types": [
            "grass"
        ],
        "hp": 45,
        "attack": 35,
        "defense": 45,
        "attack+": 62,
        "defense+": 53,
        "speed": 35,
        "total": 275
    },
    {
        "name": "cherrim",
        "types": [
            "grass"
        ],
        "hp": 70,
        "attack": 60,
        "defense": 70,
        "attack+": 87,
        "defense+": 78,
        "speed": 85,
        "total": 450
    },
    {
        "name": "shellos",
        "types": [
            "water"
        ],
        "hp": 76,
        "attack": 48,
        "defense": 48,
        "attack+": 57,
        "defense+": 62,
        "speed": 34,
        "total": 325
    },
    {
        "name": "gastrodon",
        "types": [
            "water",
            "ground"
        ],
        "hp": 111,
        "attack": 83,
        "defense": 68,
        "attack+": 92,
        "defense+": 82,
        "speed": 39,
        "total": 475
    },
    {
        "name": "ambipom",
        "types": [
            "normal"
        ],
        "hp": 75,
        "attack": 100,
        "defense": 66,
        "attack+": 60,
        "defense+": 66,
        "speed": 115,
        "total": 482
    },
    {
        "name": "drifloon",
        "types": [
            "ghost",
            "flying"
        ],
        "hp": 90,
        "attack": 50,
        "defense": 34,
        "attack+": 60,
        "defense+": 44,
        "speed": 70,
        "total": 348
    },
    {
        "name": "drifblim",
        "types": [
            "ghost",
            "flying"
        ],
        "hp": 150,
        "attack": 80,
        "defense": 44,
        "attack+": 90,
        "defense+": 54,
        "speed": 80,
        "total": 498
    },
    {
        "name": "buneary",
        "types": [
            "normal"
        ],
        "hp": 55,
        "attack": 66,
        "defense": 44,
        "attack+": 44,
        "defense+": 56,
        "speed": 85,
        "total": 350
    },
    {
        "name": "lopunny",
        "types": [
            "normal"
        ],
        "hp": 65,
        "attack": 76,
        "defense": 84,
        "attack+": 54,
        "defense+": 96,
        "speed": 105,
        "total": 480
    },
    {
        "name": "mismagius",
        "types": [
            "ghost"
        ],
        "hp": 60,
        "attack": 60,
        "defense": 60,
        "attack+": 105,
        "defense+": 105,
        "speed": 105,
        "total": 495
    },
    {
        "name": "honchkrow",
        "types": [
            "dark",
            "flying"
        ],
        "hp": 100,
        "attack": 125,
        "defense": 52,
        "attack+": 105,
        "defense+": 52,
        "speed": 71,
        "total": 505
    },
    {
        "name": "glameow",
        "types": [
            "normal"
        ],
        "hp": 49,
        "attack": 55,
        "defense": 42,
        "attack+": 42,
        "defense+": 37,
        "speed": 85,
        "total": 310
    },
    {
        "name": "purugly",
        "types": [
            "normal"
        ],
        "hp": 71,
        "attack": 82,
        "defense": 64,
        "attack+": 64,
        "defense+": 59,
        "speed": 112,
        "total": 452
    },
    {
        "name": "chingling",
        "types": [
            "psychic"
        ],
        "hp": 45,
        "attack": 30,
        "defense": 50,
        "attack+": 65,
        "defense+": 50,
        "speed": 45,
        "total": 285
    },
    {
        "name": "stunky",
        "types": [
            "poison",
            "dark"
        ],
        "hp": 63,
        "attack": 63,
        "defense": 47,
        "attack+": 41,
        "defense+": 41,
        "speed": 74,
        "total": 329
    },
    {
        "name": "skuntank",
        "types": [
            "poison",
            "dark"
        ],
        "hp": 103,
        "attack": 93,
        "defense": 67,
        "attack+": 71,
        "defense+": 61,
        "speed": 84,
        "total": 479
    },
    {
        "name": "bronzor",
        "types": [
            "steel",
            "psychic"
        ],
        "hp": 57,
        "attack": 24,
        "defense": 86,
        "attack+": 24,
        "defense+": 86,
        "speed": 23,
        "total": 300
    },
    {
        "name": "bronzong",
        "types": [
            "steel",
            "psychic"
        ],
        "hp": 67,
        "attack": 89,
        "defense": 116,
        "attack+": 79,
        "defense+": 116,
        "speed": 33,
        "total": 500
    },
    {
        "name": "bonsly",
        "types": [
            "rock"
        ],
        "hp": 50,
        "attack": 80,
        "defense": 95,
        "attack+": 10,
        "defense+": 45,
        "speed": 10,
        "total": 290
    },
    {
        "name": "mime",
        "types": [
            "psychic",
            "fairy"
        ],
        "hp": 20,
        "attack": 25,
        "defense": 45,
        "attack+": 70,
        "defense+": 90,
        "speed": 60,
        "total": 310
    },
    {
        "name": "happiny",
        "types": [
            "normal"
        ],
        "hp": 100,
        "attack": 5,
        "defense": 5,
        "attack+": 15,
        "defense+": 65,
        "speed": 30,
        "total": 220
    },
    {
        "name": "chatot",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 76,
        "attack": 65,
        "defense": 45,
        "attack+": 92,
        "defense+": 42,
        "speed": 91,
        "total": 411
    },
    {
        "name": "spiritomb",
        "types": [
            "ghost",
            "dark"
        ],
        "hp": 50,
        "attack": 92,
        "defense": 108,
        "attack+": 92,
        "defense+": 108,
        "speed": 35,
        "total": 485
    },
    {
        "name": "gible",
        "types": [
            "dragon",
            "ground"
        ],
        "hp": 58,
        "attack": 70,
        "defense": 45,
        "attack+": 40,
        "defense+": 45,
        "speed": 42,
        "total": 300
    },
    {
        "name": "gabite",
        "types": [
            "dragon",
            "ground"
        ],
        "hp": 68,
        "attack": 90,
        "defense": 65,
        "attack+": 50,
        "defense+": 55,
        "speed": 82,
        "total": 410
    },
    {
        "name": "garchomp",
        "types": [
            "dragon",
            "ground"
        ],
        "hp": 108,
        "attack": 130,
        "defense": 95,
        "attack+": 80,
        "defense+": 85,
        "speed": 102,
        "total": 600
    },
    {
        "name": "munchlax",
        "types": [
            "normal"
        ],
        "hp": 135,
        "attack": 85,
        "defense": 40,
        "attack+": 40,
        "defense+": 85,
        "speed": 5,
        "total": 390
    },
    {
        "name": "riolu",
        "types": [
            "fighting"
        ],
        "hp": 40,
        "attack": 70,
        "defense": 40,
        "attack+": 35,
        "defense+": 40,
        "speed": 60,
        "total": 285
    },
    {
        "name": "lucario",
        "types": [
            "fighting",
            "steel"
        ],
        "hp": 70,
        "attack": 110,
        "defense": 70,
        "attack+": 115,
        "defense+": 70,
        "speed": 90,
        "total": 525
    },
    {
        "name": "hippopotas",
        "types": [
            "ground"
        ],
        "hp": 68,
        "attack": 72,
        "defense": 78,
        "attack+": 38,
        "defense+": 42,
        "speed": 32,
        "total": 330
    },
    {
        "name": "hippowdon",
        "types": [
            "ground"
        ],
        "hp": 108,
        "attack": 112,
        "defense": 118,
        "attack+": 68,
        "defense+": 72,
        "speed": 47,
        "total": 525
    },
    {
        "name": "skorupi",
        "types": [
            "poison",
            "bug"
        ],
        "hp": 40,
        "attack": 50,
        "defense": 90,
        "attack+": 30,
        "defense+": 55,
        "speed": 65,
        "total": 330
    },
    {
        "name": "drapion",
        "types": [
            "poison",
            "dark"
        ],
        "hp": 70,
        "attack": 90,
        "defense": 110,
        "attack+": 60,
        "defense+": 75,
        "speed": 95,
        "total": 500
    },
    {
        "name": "croagunk",
        "types": [
            "poison",
            "fighting"
        ],
        "hp": 48,
        "attack": 61,
        "defense": 40,
        "attack+": 61,
        "defense+": 40,
        "speed": 50,
        "total": 300
    },
    {
        "name": "toxicroak",
        "types": [
            "poison",
            "fighting"
        ],
        "hp": 83,
        "attack": 106,
        "defense": 65,
        "attack+": 86,
        "defense+": 65,
        "speed": 85,
        "total": 490
    },
    {
        "name": "carnivine",
        "types": [
            "grass"
        ],
        "hp": 74,
        "attack": 100,
        "defense": 72,
        "attack+": 90,
        "defense+": 72,
        "speed": 46,
        "total": 454
    },
    {
        "name": "finneon",
        "types": [
            "water"
        ],
        "hp": 49,
        "attack": 49,
        "defense": 56,
        "attack+": 49,
        "defense+": 61,
        "speed": 66,
        "total": 330
    },
    {
        "name": "lumineon",
        "types": [
            "water"
        ],
        "hp": 69,
        "attack": 69,
        "defense": 76,
        "attack+": 69,
        "defense+": 86,
        "speed": 91,
        "total": 460
    },
    {
        "name": "mantyke",
        "types": [
            "water",
            "flying"
        ],
        "hp": 45,
        "attack": 20,
        "defense": 50,
        "attack+": 60,
        "defense+": 120,
        "speed": 50,
        "total": 345
    },
    {
        "name": "snover",
        "types": [
            "grass",
            "ice"
        ],
        "hp": 60,
        "attack": 62,
        "defense": 50,
        "attack+": 62,
        "defense+": 60,
        "speed": 40,
        "total": 334
    },
    {
        "name": "abomasnow",
        "types": [
            "grass",
            "ice"
        ],
        "hp": 90,
        "attack": 92,
        "defense": 75,
        "attack+": 92,
        "defense+": 85,
        "speed": 60,
        "total": 494
    },
    {
        "name": "weavile",
        "types": [
            "dark",
            "ice"
        ],
        "hp": 70,
        "attack": 120,
        "defense": 65,
        "attack+": 45,
        "defense+": 85,
        "speed": 125,
        "total": 510
    },
    {
        "name": "magnezone",
        "types": [
            "electric",
            "steel"
        ],
        "hp": 70,
        "attack": 70,
        "defense": 115,
        "attack+": 130,
        "defense+": 90,
        "speed": 60,
        "total": 535
    },
    {
        "name": "lickilicky",
        "types": [
            "normal"
        ],
        "hp": 110,
        "attack": 85,
        "defense": 95,
        "attack+": 80,
        "defense+": 95,
        "speed": 50,
        "total": 515
    },
    {
        "name": "rhyperior",
        "types": [
            "ground",
            "rock"
        ],
        "hp": 115,
        "attack": 140,
        "defense": 130,
        "attack+": 55,
        "defense+": 55,
        "speed": 40,
        "total": 535
    },
    {
        "name": "tangrowth",
        "types": [
            "grass"
        ],
        "hp": 100,
        "attack": 100,
        "defense": 125,
        "attack+": 110,
        "defense+": 50,
        "speed": 50,
        "total": 535
    },
    {
        "name": "electivire",
        "types": [
            "electric"
        ],
        "hp": 75,
        "attack": 123,
        "defense": 67,
        "attack+": 95,
        "defense+": 85,
        "speed": 95,
        "total": 540
    },
    {
        "name": "magmortar",
        "types": [
            "fire"
        ],
        "hp": 75,
        "attack": 95,
        "defense": 67,
        "attack+": 125,
        "defense+": 95,
        "speed": 83,
        "total": 540
    },
    {
        "name": "togekiss",
        "types": [
            "fairy",
            "flying"
        ],
        "hp": 85,
        "attack": 50,
        "defense": 95,
        "attack+": 120,
        "defense+": 115,
        "speed": 80,
        "total": 545
    },
    {
        "name": "yanmega",
        "types": [
            "bug",
            "flying"
        ],
        "hp": 86,
        "attack": 76,
        "defense": 86,
        "attack+": 116,
        "defense+": 56,
        "speed": 95,
        "total": 515
    },
    {
        "name": "leafeon",
        "types": [
            "grass"
        ],
        "hp": 65,
        "attack": 110,
        "defense": 130,
        "attack+": 60,
        "defense+": 65,
        "speed": 95,
        "total": 525
    },
    {
        "name": "glaceon",
        "types": [
            "ice"
        ],
        "hp": 65,
        "attack": 60,
        "defense": 110,
        "attack+": 130,
        "defense+": 95,
        "speed": 65,
        "total": 525
    },
    {
        "name": "gliscor",
        "types": [
            "ground",
            "flying"
        ],
        "hp": 75,
        "attack": 95,
        "defense": 125,
        "attack+": 45,
        "defense+": 75,
        "speed": 95,
        "total": 510
    },
    {
        "name": "mamoswine",
        "types": [
            "ice",
            "ground"
        ],
        "hp": 110,
        "attack": 130,
        "defense": 80,
        "attack+": 70,
        "defense+": 60,
        "speed": 80,
        "total": 530
    },
    {
        "name": "porygon-z",
        "types": [
            "normal"
        ],
        "hp": 85,
        "attack": 80,
        "defense": 70,
        "attack+": 135,
        "defense+": 75,
        "speed": 90,
        "total": 535
    },
    {
        "name": "gallade",
        "types": [
            "psychic",
            "fighting"
        ],
        "hp": 68,
        "attack": 125,
        "defense": 65,
        "attack+": 65,
        "defense+": 115,
        "speed": 80,
        "total": 518
    },
    {
        "name": "probopass",
        "types": [
            "rock",
            "steel"
        ],
        "hp": 60,
        "attack": 55,
        "defense": 145,
        "attack+": 75,
        "defense+": 150,
        "speed": 40,
        "total": 525
    },
    {
        "name": "dusknoir",
        "types": [
            "ghost"
        ],
        "hp": 45,
        "attack": 100,
        "defense": 135,
        "attack+": 65,
        "defense+": 135,
        "speed": 45,
        "total": 525
    },
    {
        "name": "froslass",
        "types": [
            "ice",
            "ghost"
        ],
        "hp": 70,
        "attack": 80,
        "defense": 70,
        "attack+": 80,
        "defense+": 70,
        "speed": 110,
        "total": 480
    },
    {
        "name": "rotom",
        "types": [
            "electric",
            "ghost"
        ],
        "hp": 50,
        "attack": 50,
        "defense": 77,
        "attack+": 95,
        "defense+": 77,
        "speed": 91,
        "total": 440
    },
    {
        "name": "uxie",
        "types": [
            "psychic"
        ],
        "hp": 75,
        "attack": 75,
        "defense": 130,
        "attack+": 75,
        "defense+": 130,
        "speed": 95,
        "total": 580
    },
    {
        "name": "mesprit",
        "types": [
            "psychic"
        ],
        "hp": 80,
        "attack": 105,
        "defense": 105,
        "attack+": 105,
        "defense+": 105,
        "speed": 80,
        "total": 580
    },
    {
        "name": "azelf",
        "types": [
            "psychic"
        ],
        "hp": 75,
        "attack": 125,
        "defense": 70,
        "attack+": 125,
        "defense+": 70,
        "speed": 115,
        "total": 580
    },
    {
        "name": "dialga",
        "types": [
            "steel",
            "dragon"
        ],
        "hp": 100,
        "attack": 120,
        "defense": 120,
        "attack+": 150,
        "defense+": 100,
        "speed": 90,
        "total": 680
    },
    {
        "name": "palkia",
        "types": [
            "water",
            "dragon"
        ],
        "hp": 90,
        "attack": 120,
        "defense": 100,
        "attack+": 150,
        "defense+": 120,
        "speed": 100,
        "total": 680
    },
    {
        "name": "heatran",
        "types": [
            "fire",
            "steel"
        ],
        "hp": 91,
        "attack": 90,
        "defense": 106,
        "attack+": 130,
        "defense+": 106,
        "speed": 77,
        "total": 600
    },
    {
        "name": "regigigas",
        "types": [
            "normal"
        ],
        "hp": 110,
        "attack": 160,
        "defense": 110,
        "attack+": 80,
        "defense+": 110,
        "speed": 100,
        "total": 670
    },
    {
        "name": "giratina",
        "types": [
            "ghost",
            "dragon"
        ],
        "hp": 150,
        "attack": 100,
        "defense": 120,
        "attack+": 100,
        "defense+": 120,
        "speed": 90,
        "total": 680
    },
    {
        "name": "cresselia",
        "types": [
            "psychic"
        ],
        "hp": 120,
        "attack": 70,
        "defense": 120,
        "attack+": 75,
        "defense+": 130,
        "speed": 85,
        "total": 600
    },
    {
        "name": "phione",
        "types": [
            "water"
        ],
        "hp": 80,
        "attack": 80,
        "defense": 80,
        "attack+": 80,
        "defense+": 80,
        "speed": 80,
        "total": 480
    },
    {
        "name": "manaphy",
        "types": [
            "water"
        ],
        "hp": 100,
        "attack": 100,
        "defense": 100,
        "attack+": 100,
        "defense+": 100,
        "speed": 100,
        "total": 600
    },
    {
        "name": "darkrai",
        "types": [
            "dark"
        ],
        "hp": 70,
        "attack": 90,
        "defense": 90,
        "attack+": 135,
        "defense+": 90,
        "speed": 125,
        "total": 600
    },
    {
        "name": "shaymin",
        "types": [
            "grass"
        ],
        "hp": 100,
        "attack": 100,
        "defense": 100,
        "attack+": 100,
        "defense+": 100,
        "speed": 100,
        "total": 600
    },
    {
        "name": "arceus",
        "types": [
            "normal"
        ],
        "hp": 120,
        "attack": 120,
        "defense": 120,
        "attack+": 120,
        "defense+": 120,
        "speed": 120,
        "total": 720
    },
    {
        "name": "victini",
        "types": [
            "psychic",
            "fire"
        ],
        "hp": 100,
        "attack": 100,
        "defense": 100,
        "attack+": 100,
        "defense+": 100,
        "speed": 100,
        "total": 600
    },
    {
        "name": "snivy",
        "types": [
            "grass"
        ],
        "hp": 45,
        "attack": 45,
        "defense": 55,
        "attack+": 45,
        "defense+": 55,
        "speed": 63,
        "total": 308
    },
    {
        "name": "servine",
        "types": [
            "grass"
        ],
        "hp": 60,
        "attack": 60,
        "defense": 75,
        "attack+": 60,
        "defense+": 75,
        "speed": 83,
        "total": 413
    },
    {
        "name": "serperior",
        "types": [
            "grass"
        ],
        "hp": 75,
        "attack": 75,
        "defense": 95,
        "attack+": 75,
        "defense+": 95,
        "speed": 113,
        "total": 528
    },
    {
        "name": "tepig",
        "types": [
            "fire"
        ],
        "hp": 65,
        "attack": 63,
        "defense": 45,
        "attack+": 45,
        "defense+": 45,
        "speed": 45,
        "total": 308
    },
    {
        "name": "pignite",
        "types": [
            "fire",
            "fighting"
        ],
        "hp": 90,
        "attack": 93,
        "defense": 55,
        "attack+": 70,
        "defense+": 55,
        "speed": 55,
        "total": 418
    },
    {
        "name": "emboar",
        "types": [
            "fire",
            "fighting"
        ],
        "hp": 110,
        "attack": 123,
        "defense": 65,
        "attack+": 100,
        "defense+": 65,
        "speed": 65,
        "total": 528
    },
    {
        "name": "oshawott",
        "types": [
            "water"
        ],
        "hp": 55,
        "attack": 55,
        "defense": 45,
        "attack+": 63,
        "defense+": 45,
        "speed": 45,
        "total": 308
    },
    {
        "name": "dewott",
        "types": [
            "water"
        ],
        "hp": 75,
        "attack": 75,
        "defense": 60,
        "attack+": 83,
        "defense+": 60,
        "speed": 60,
        "total": 413
    },
    {
        "name": "samurott",
        "types": [
            "water"
        ],
        "hp": 95,
        "attack": 100,
        "defense": 85,
        "attack+": 108,
        "defense+": 70,
        "speed": 70,
        "total": 528
    },
    {
        "name": "patrat",
        "types": [
            "normal"
        ],
        "hp": 45,
        "attack": 55,
        "defense": 39,
        "attack+": 35,
        "defense+": 39,
        "speed": 42,
        "total": 255
    },
    {
        "name": "watchog",
        "types": [
            "normal"
        ],
        "hp": 60,
        "attack": 85,
        "defense": 69,
        "attack+": 60,
        "defense+": 69,
        "speed": 77,
        "total": 420
    },
    {
        "name": "lillipup",
        "types": [
            "normal"
        ],
        "hp": 45,
        "attack": 60,
        "defense": 45,
        "attack+": 25,
        "defense+": 45,
        "speed": 55,
        "total": 275
    },
    {
        "name": "herdier",
        "types": [
            "normal"
        ],
        "hp": 65,
        "attack": 80,
        "defense": 65,
        "attack+": 35,
        "defense+": 65,
        "speed": 60,
        "total": 370
    },
    {
        "name": "stoutland",
        "types": [
            "normal"
        ],
        "hp": 85,
        "attack": 110,
        "defense": 90,
        "attack+": 45,
        "defense+": 90,
        "speed": 80,
        "total": 500
    },
    {
        "name": "purrloin",
        "types": [
            "dark"
        ],
        "hp": 41,
        "attack": 50,
        "defense": 37,
        "attack+": 50,
        "defense+": 37,
        "speed": 66,
        "total": 281
    },
    {
        "name": "liepard",
        "types": [
            "dark"
        ],
        "hp": 64,
        "attack": 88,
        "defense": 50,
        "attack+": 88,
        "defense+": 50,
        "speed": 106,
        "total": 446
    },
    {
        "name": "pansage",
        "types": [
            "grass"
        ],
        "hp": 50,
        "attack": 53,
        "defense": 48,
        "attack+": 53,
        "defense+": 48,
        "speed": 64,
        "total": 316
    },
    {
        "name": "simisage",
        "types": [
            "grass"
        ],
        "hp": 75,
        "attack": 98,
        "defense": 63,
        "attack+": 98,
        "defense+": 63,
        "speed": 101,
        "total": 498
    },
    {
        "name": "pansear",
        "types": [
            "fire"
        ],
        "hp": 50,
        "attack": 53,
        "defense": 48,
        "attack+": 53,
        "defense+": 48,
        "speed": 64,
        "total": 316
    },
    {
        "name": "simisear",
        "types": [
            "fire"
        ],
        "hp": 75,
        "attack": 98,
        "defense": 63,
        "attack+": 98,
        "defense+": 63,
        "speed": 101,
        "total": 498
    },
    {
        "name": "panpour",
        "types": [
            "water"
        ],
        "hp": 50,
        "attack": 53,
        "defense": 48,
        "attack+": 53,
        "defense+": 48,
        "speed": 64,
        "total": 316
    },
    {
        "name": "simipour",
        "types": [
            "water"
        ],
        "hp": 75,
        "attack": 98,
        "defense": 63,
        "attack+": 98,
        "defense+": 63,
        "speed": 101,
        "total": 498
    },
    {
        "name": "munna",
        "types": [
            "psychic"
        ],
        "hp": 76,
        "attack": 25,
        "defense": 45,
        "attack+": 67,
        "defense+": 55,
        "speed": 24,
        "total": 292
    },
    {
        "name": "musharna",
        "types": [
            "psychic"
        ],
        "hp": 116,
        "attack": 55,
        "defense": 85,
        "attack+": 107,
        "defense+": 95,
        "speed": 29,
        "total": 487
    },
    {
        "name": "pidove",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 50,
        "attack": 55,
        "defense": 50,
        "attack+": 36,
        "defense+": 30,
        "speed": 43,
        "total": 264
    },
    {
        "name": "tranquill",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 62,
        "attack": 77,
        "defense": 62,
        "attack+": 50,
        "defense+": 42,
        "speed": 65,
        "total": 358
    },
    {
        "name": "unfezant",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 80,
        "attack": 115,
        "defense": 80,
        "attack+": 65,
        "defense+": 55,
        "speed": 93,
        "total": 488
    },
    {
        "name": "blitzle",
        "types": [
            "electric"
        ],
        "hp": 45,
        "attack": 60,
        "defense": 32,
        "attack+": 50,
        "defense+": 32,
        "speed": 76,
        "total": 295
    },
    {
        "name": "zebstrika",
        "types": [
            "electric"
        ],
        "hp": 75,
        "attack": 100,
        "defense": 63,
        "attack+": 80,
        "defense+": 63,
        "speed": 116,
        "total": 497
    },
    {
        "name": "roggenrola",
        "types": [
            "rock"
        ],
        "hp": 55,
        "attack": 75,
        "defense": 85,
        "attack+": 25,
        "defense+": 25,
        "speed": 15,
        "total": 280
    },
    {
        "name": "boldore",
        "types": [
            "rock"
        ],
        "hp": 70,
        "attack": 105,
        "defense": 105,
        "attack+": 50,
        "defense+": 40,
        "speed": 20,
        "total": 390
    },
    {
        "name": "gigalith",
        "types": [
            "rock"
        ],
        "hp": 85,
        "attack": 135,
        "defense": 130,
        "attack+": 60,
        "defense+": 80,
        "speed": 25,
        "total": 515
    },
    {
        "name": "woobat",
        "types": [
            "psychic",
            "flying"
        ],
        "hp": 65,
        "attack": 45,
        "defense": 43,
        "attack+": 55,
        "defense+": 43,
        "speed": 72,
        "total": 323
    },
    {
        "name": "swoobat",
        "types": [
            "psychic",
            "flying"
        ],
        "hp": 67,
        "attack": 57,
        "defense": 55,
        "attack+": 77,
        "defense+": 55,
        "speed": 114,
        "total": 425
    },
    {
        "name": "drilbur",
        "types": [
            "ground"
        ],
        "hp": 60,
        "attack": 85,
        "defense": 40,
        "attack+": 30,
        "defense+": 45,
        "speed": 68,
        "total": 328
    },
    {
        "name": "excadrill",
        "types": [
            "ground",
            "steel"
        ],
        "hp": 110,
        "attack": 135,
        "defense": 60,
        "attack+": 50,
        "defense+": 65,
        "speed": 88,
        "total": 508
    },
    {
        "name": "audino",
        "types": [
            "normal"
        ],
        "hp": 103,
        "attack": 60,
        "defense": 86,
        "attack+": 60,
        "defense+": 86,
        "speed": 50,
        "total": 445
    },
    {
        "name": "timburr",
        "types": [
            "fighting"
        ],
        "hp": 75,
        "attack": 80,
        "defense": 55,
        "attack+": 25,
        "defense+": 35,
        "speed": 35,
        "total": 305
    },
    {
        "name": "gurdurr",
        "types": [
            "fighting"
        ],
        "hp": 85,
        "attack": 105,
        "defense": 85,
        "attack+": 40,
        "defense+": 50,
        "speed": 40,
        "total": 405
    },
    {
        "name": "conkeldurr",
        "types": [
            "fighting"
        ],
        "hp": 105,
        "attack": 140,
        "defense": 95,
        "attack+": 55,
        "defense+": 65,
        "speed": 45,
        "total": 505
    },
    {
        "name": "tympole",
        "types": [
            "water"
        ],
        "hp": 50,
        "attack": 50,
        "defense": 40,
        "attack+": 50,
        "defense+": 40,
        "speed": 64,
        "total": 294
    },
    {
        "name": "palpitoad",
        "types": [
            "water",
            "ground"
        ],
        "hp": 75,
        "attack": 65,
        "defense": 55,
        "attack+": 65,
        "defense+": 55,
        "speed": 69,
        "total": 384
    },
    {
        "name": "seismitoad",
        "types": [
            "water",
            "ground"
        ],
        "hp": 105,
        "attack": 95,
        "defense": 75,
        "attack+": 85,
        "defense+": 75,
        "speed": 74,
        "total": 509
    },
    {
        "name": "throh",
        "types": [
            "fighting"
        ],
        "hp": 120,
        "attack": 100,
        "defense": 85,
        "attack+": 30,
        "defense+": 85,
        "speed": 45,
        "total": 465
    },
    {
        "name": "sawk",
        "types": [
            "fighting"
        ],
        "hp": 75,
        "attack": 125,
        "defense": 75,
        "attack+": 30,
        "defense+": 75,
        "speed": 85,
        "total": 465
    },
    {
        "name": "sewaddle",
        "types": [
            "bug",
            "grass"
        ],
        "hp": 45,
        "attack": 53,
        "defense": 70,
        "attack+": 40,
        "defense+": 60,
        "speed": 42,
        "total": 310
    },
    {
        "name": "swadloon",
        "types": [
            "bug",
            "grass"
        ],
        "hp": 55,
        "attack": 63,
        "defense": 90,
        "attack+": 50,
        "defense+": 80,
        "speed": 42,
        "total": 380
    },
    {
        "name": "leavanny",
        "types": [
            "bug",
            "grass"
        ],
        "hp": 75,
        "attack": 103,
        "defense": 80,
        "attack+": 70,
        "defense+": 80,
        "speed": 92,
        "total": 500
    },
    {
        "name": "venipede",
        "types": [
            "bug",
            "poison"
        ],
        "hp": 30,
        "attack": 45,
        "defense": 59,
        "attack+": 30,
        "defense+": 39,
        "speed": 57,
        "total": 260
    },
    {
        "name": "whirlipede",
        "types": [
            "bug",
            "poison"
        ],
        "hp": 40,
        "attack": 55,
        "defense": 99,
        "attack+": 40,
        "defense+": 79,
        "speed": 47,
        "total": 360
    },
    {
        "name": "scolipede",
        "types": [
            "bug",
            "poison"
        ],
        "hp": 60,
        "attack": 100,
        "defense": 89,
        "attack+": 55,
        "defense+": 69,
        "speed": 112,
        "total": 485
    },
    {
        "name": "cottonee",
        "types": [
            "grass",
            "fairy"
        ],
        "hp": 40,
        "attack": 27,
        "defense": 60,
        "attack+": 37,
        "defense+": 50,
        "speed": 66,
        "total": 280
    },
    {
        "name": "whimsicott",
        "types": [
            "grass",
            "fairy"
        ],
        "hp": 60,
        "attack": 67,
        "defense": 85,
        "attack+": 77,
        "defense+": 75,
        "speed": 116,
        "total": 480
    },
    {
        "name": "petilil",
        "types": [
            "grass"
        ],
        "hp": 45,
        "attack": 35,
        "defense": 50,
        "attack+": 70,
        "defense+": 50,
        "speed": 30,
        "total": 280
    },
    {
        "name": "lilligant",
        "types": [
            "grass"
        ],
        "hp": 70,
        "attack": 60,
        "defense": 75,
        "attack+": 110,
        "defense+": 75,
        "speed": 90,
        "total": 480
    },
    {
        "name": "basculin",
        "types": [
            "water"
        ],
        "hp": 70,
        "attack": 92,
        "defense": 65,
        "attack+": 80,
        "defense+": 55,
        "speed": 98,
        "total": 460
    },
    {
        "name": "sandile",
        "types": [
            "ground",
            "dark"
        ],
        "hp": 50,
        "attack": 72,
        "defense": 35,
        "attack+": 35,
        "defense+": 35,
        "speed": 65,
        "total": 292
    },
    {
        "name": "krokorok",
        "types": [
            "ground",
            "dark"
        ],
        "hp": 60,
        "attack": 82,
        "defense": 45,
        "attack+": 45,
        "defense+": 45,
        "speed": 74,
        "total": 351
    },
    {
        "name": "krookodile",
        "types": [
            "ground",
            "dark"
        ],
        "hp": 95,
        "attack": 117,
        "defense": 80,
        "attack+": 65,
        "defense+": 70,
        "speed": 92,
        "total": 519
    },
    {
        "name": "darumaka",
        "types": [
            "fire"
        ],
        "hp": 70,
        "attack": 90,
        "defense": 45,
        "attack+": 15,
        "defense+": 45,
        "speed": 50,
        "total": 315
    },
    {
        "name": "darmanitan",
        "types": [
            "fire"
        ],
        "hp": 105,
        "attack": 140,
        "defense": 55,
        "attack+": 30,
        "defense+": 55,
        "speed": 95,
        "total": 480
    },
    {
        "name": "maractus",
        "types": [
            "grass"
        ],
        "hp": 75,
        "attack": 86,
        "defense": 67,
        "attack+": 106,
        "defense+": 67,
        "speed": 60,
        "total": 461
    },
    {
        "name": "dwebble",
        "types": [
            "bug",
            "rock"
        ],
        "hp": 50,
        "attack": 65,
        "defense": 85,
        "attack+": 35,
        "defense+": 35,
        "speed": 55,
        "total": 325
    },
    {
        "name": "crustle",
        "types": [
            "bug",
            "rock"
        ],
        "hp": 70,
        "attack": 105,
        "defense": 125,
        "attack+": 65,
        "defense+": 75,
        "speed": 45,
        "total": 485
    },
    {
        "name": "scraggy",
        "types": [
            "dark",
            "fighting"
        ],
        "hp": 50,
        "attack": 75,
        "defense": 70,
        "attack+": 35,
        "defense+": 70,
        "speed": 48,
        "total": 348
    },
    {
        "name": "scrafty",
        "types": [
            "dark",
            "fighting"
        ],
        "hp": 65,
        "attack": 90,
        "defense": 115,
        "attack+": 45,
        "defense+": 115,
        "speed": 58,
        "total": 488
    },
    {
        "name": "sigilyph",
        "types": [
            "psychic",
            "flying"
        ],
        "hp": 72,
        "attack": 58,
        "defense": 80,
        "attack+": 103,
        "defense+": 80,
        "speed": 97,
        "total": 490
    },
    {
        "name": "yamask",
        "types": [
            "ghost"
        ],
        "hp": 38,
        "attack": 30,
        "defense": 85,
        "attack+": 55,
        "defense+": 65,
        "speed": 30,
        "total": 303
    },
    {
        "name": "cofagrigus",
        "types": [
            "ghost"
        ],
        "hp": 58,
        "attack": 50,
        "defense": 145,
        "attack+": 95,
        "defense+": 105,
        "speed": 30,
        "total": 483
    },
    {
        "name": "tirtouga",
        "types": [
            "water",
            "rock"
        ],
        "hp": 54,
        "attack": 78,
        "defense": 103,
        "attack+": 53,
        "defense+": 45,
        "speed": 22,
        "total": 355
    },
    {
        "name": "carracosta",
        "types": [
            "water",
            "rock"
        ],
        "hp": 74,
        "attack": 108,
        "defense": 133,
        "attack+": 83,
        "defense+": 65,
        "speed": 32,
        "total": 495
    },
    {
        "name": "archen",
        "types": [
            "rock",
            "flying"
        ],
        "hp": 55,
        "attack": 112,
        "defense": 45,
        "attack+": 74,
        "defense+": 45,
        "speed": 70,
        "total": 401
    },
    {
        "name": "archeops",
        "types": [
            "rock",
            "flying"
        ],
        "hp": 75,
        "attack": 140,
        "defense": 65,
        "attack+": 112,
        "defense+": 65,
        "speed": 110,
        "total": 567
    },
    {
        "name": "trubbish",
        "types": [
            "poison"
        ],
        "hp": 50,
        "attack": 50,
        "defense": 62,
        "attack+": 40,
        "defense+": 62,
        "speed": 65,
        "total": 329
    },
    {
        "name": "garbodor",
        "types": [
            "poison"
        ],
        "hp": 80,
        "attack": 95,
        "defense": 82,
        "attack+": 60,
        "defense+": 82,
        "speed": 75,
        "total": 474
    },
    {
        "name": "zorua",
        "types": [
            "dark"
        ],
        "hp": 40,
        "attack": 65,
        "defense": 40,
        "attack+": 80,
        "defense+": 40,
        "speed": 65,
        "total": 330
    },
    {
        "name": "zoroark",
        "types": [
            "dark"
        ],
        "hp": 60,
        "attack": 105,
        "defense": 60,
        "attack+": 120,
        "defense+": 60,
        "speed": 105,
        "total": 510
    },
    {
        "name": "minccino",
        "types": [
            "normal"
        ],
        "hp": 55,
        "attack": 50,
        "defense": 40,
        "attack+": 40,
        "defense+": 40,
        "speed": 75,
        "total": 300
    },
    {
        "name": "cinccino",
        "types": [
            "normal"
        ],
        "hp": 75,
        "attack": 95,
        "defense": 60,
        "attack+": 65,
        "defense+": 60,
        "speed": 115,
        "total": 470
    },
    {
        "name": "gothita",
        "types": [
            "psychic"
        ],
        "hp": 45,
        "attack": 30,
        "defense": 50,
        "attack+": 55,
        "defense+": 65,
        "speed": 45,
        "total": 290
    },
    {
        "name": "gothorita",
        "types": [
            "psychic"
        ],
        "hp": 60,
        "attack": 45,
        "defense": 70,
        "attack+": 75,
        "defense+": 85,
        "speed": 55,
        "total": 390
    },
    {
        "name": "gothitelle",
        "types": [
            "psychic"
        ],
        "hp": 70,
        "attack": 55,
        "defense": 95,
        "attack+": 95,
        "defense+": 110,
        "speed": 65,
        "total": 490
    },
    {
        "name": "solosis",
        "types": [
            "psychic"
        ],
        "hp": 45,
        "attack": 30,
        "defense": 40,
        "attack+": 105,
        "defense+": 50,
        "speed": 20,
        "total": 290
    },
    {
        "name": "duosion",
        "types": [
            "psychic"
        ],
        "hp": 65,
        "attack": 40,
        "defense": 50,
        "attack+": 125,
        "defense+": 60,
        "speed": 30,
        "total": 370
    },
    {
        "name": "reuniclus",
        "types": [
            "psychic"
        ],
        "hp": 110,
        "attack": 65,
        "defense": 75,
        "attack+": 125,
        "defense+": 85,
        "speed": 30,
        "total": 490
    },
    {
        "name": "ducklett",
        "types": [
            "water",
            "flying"
        ],
        "hp": 62,
        "attack": 44,
        "defense": 50,
        "attack+": 44,
        "defense+": 50,
        "speed": 55,
        "total": 305
    },
    {
        "name": "swanna",
        "types": [
            "water",
            "flying"
        ],
        "hp": 75,
        "attack": 87,
        "defense": 63,
        "attack+": 87,
        "defense+": 63,
        "speed": 98,
        "total": 473
    },
    {
        "name": "vanillite",
        "types": [
            "ice"
        ],
        "hp": 36,
        "attack": 50,
        "defense": 50,
        "attack+": 65,
        "defense+": 60,
        "speed": 44,
        "total": 305
    },
    {
        "name": "vanillish",
        "types": [
            "ice"
        ],
        "hp": 51,
        "attack": 65,
        "defense": 65,
        "attack+": 80,
        "defense+": 75,
        "speed": 59,
        "total": 395
    },
    {
        "name": "vanilluxe",
        "types": [
            "ice"
        ],
        "hp": 71,
        "attack": 95,
        "defense": 85,
        "attack+": 110,
        "defense+": 95,
        "speed": 79,
        "total": 535
    },
    {
        "name": "deerling",
        "types": [
            "normal",
            "grass"
        ],
        "hp": 60,
        "attack": 60,
        "defense": 50,
        "attack+": 40,
        "defense+": 50,
        "speed": 75,
        "total": 335
    },
    {
        "name": "sawsbuck",
        "types": [
            "normal",
            "grass"
        ],
        "hp": 80,
        "attack": 100,
        "defense": 70,
        "attack+": 60,
        "defense+": 70,
        "speed": 95,
        "total": 475
    },
    {
        "name": "emolga",
        "types": [
            "electric",
            "flying"
        ],
        "hp": 55,
        "attack": 75,
        "defense": 60,
        "attack+": 75,
        "defense+": 60,
        "speed": 103,
        "total": 428
    },
    {
        "name": "karrablast",
        "types": [
            "bug"
        ],
        "hp": 50,
        "attack": 75,
        "defense": 45,
        "attack+": 40,
        "defense+": 45,
        "speed": 60,
        "total": 315
    },
    {
        "name": "escavalier",
        "types": [
            "bug",
            "steel"
        ],
        "hp": 70,
        "attack": 135,
        "defense": 105,
        "attack+": 60,
        "defense+": 105,
        "speed": 20,
        "total": 495
    },
    {
        "name": "foongus",
        "types": [
            "grass",
            "poison"
        ],
        "hp": 69,
        "attack": 55,
        "defense": 45,
        "attack+": 55,
        "defense+": 55,
        "speed": 15,
        "total": 294
    },
    {
        "name": "amoonguss",
        "types": [
            "grass",
            "poison"
        ],
        "hp": 114,
        "attack": 85,
        "defense": 70,
        "attack+": 85,
        "defense+": 80,
        "speed": 30,
        "total": 464
    },
    {
        "name": "frillish",
        "types": [
            "water",
            "ghost"
        ],
        "hp": 55,
        "attack": 40,
        "defense": 50,
        "attack+": 65,
        "defense+": 85,
        "speed": 40,
        "total": 335
    },
    {
        "name": "jellicent",
        "types": [
            "water",
            "ghost"
        ],
        "hp": 100,
        "attack": 60,
        "defense": 70,
        "attack+": 85,
        "defense+": 105,
        "speed": 60,
        "total": 480
    },
    {
        "name": "alomomola",
        "types": [
            "water"
        ],
        "hp": 165,
        "attack": 75,
        "defense": 80,
        "attack+": 40,
        "defense+": 45,
        "speed": 65,
        "total": 470
    },
    {
        "name": "joltik",
        "types": [
            "bug",
            "electric"
        ],
        "hp": 50,
        "attack": 47,
        "defense": 50,
        "attack+": 57,
        "defense+": 50,
        "speed": 65,
        "total": 319
    },
    {
        "name": "galvantula",
        "types": [
            "bug",
            "electric"
        ],
        "hp": 70,
        "attack": 77,
        "defense": 60,
        "attack+": 97,
        "defense+": 60,
        "speed": 108,
        "total": 472
    },
    {
        "name": "ferroseed",
        "types": [
            "grass",
            "steel"
        ],
        "hp": 44,
        "attack": 50,
        "defense": 91,
        "attack+": 24,
        "defense+": 86,
        "speed": 10,
        "total": 305
    },
    {
        "name": "ferrothorn",
        "types": [
            "grass",
            "steel"
        ],
        "hp": 74,
        "attack": 94,
        "defense": 131,
        "attack+": 54,
        "defense+": 116,
        "speed": 20,
        "total": 489
    },
    {
        "name": "klink",
        "types": [
            "steel"
        ],
        "hp": 40,
        "attack": 55,
        "defense": 70,
        "attack+": 45,
        "defense+": 60,
        "speed": 30,
        "total": 300
    },
    {
        "name": "klang",
        "types": [
            "steel"
        ],
        "hp": 60,
        "attack": 80,
        "defense": 95,
        "attack+": 70,
        "defense+": 85,
        "speed": 50,
        "total": 440
    },
    {
        "name": "klinklang",
        "types": [
            "steel"
        ],
        "hp": 60,
        "attack": 100,
        "defense": 115,
        "attack+": 70,
        "defense+": 85,
        "speed": 90,
        "total": 520
    },
    {
        "name": "tynamo",
        "types": [
            "electric"
        ],
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "attack+": 45,
        "defense+": 40,
        "speed": 60,
        "total": 275
    },
    {
        "name": "eelektrik",
        "types": [
            "electric"
        ],
        "hp": 65,
        "attack": 85,
        "defense": 70,
        "attack+": 75,
        "defense+": 70,
        "speed": 40,
        "total": 405
    },
    {
        "name": "eelektross",
        "types": [
            "electric"
        ],
        "hp": 85,
        "attack": 115,
        "defense": 80,
        "attack+": 105,
        "defense+": 80,
        "speed": 50,
        "total": 515
    },
    {
        "name": "elgyem",
        "types": [
            "psychic"
        ],
        "hp": 55,
        "attack": 55,
        "defense": 55,
        "attack+": 85,
        "defense+": 55,
        "speed": 30,
        "total": 335
    },
    {
        "name": "beheeyem",
        "types": [
            "psychic"
        ],
        "hp": 75,
        "attack": 75,
        "defense": 75,
        "attack+": 125,
        "defense+": 95,
        "speed": 40,
        "total": 485
    },
    {
        "name": "litwick",
        "types": [
            "ghost",
            "fire"
        ],
        "hp": 50,
        "attack": 30,
        "defense": 55,
        "attack+": 65,
        "defense+": 55,
        "speed": 20,
        "total": 275
    },
    {
        "name": "lampent",
        "types": [
            "ghost",
            "fire"
        ],
        "hp": 60,
        "attack": 40,
        "defense": 60,
        "attack+": 95,
        "defense+": 60,
        "speed": 55,
        "total": 370
    },
    {
        "name": "chandelure",
        "types": [
            "ghost",
            "fire"
        ],
        "hp": 60,
        "attack": 55,
        "defense": 90,
        "attack+": 145,
        "defense+": 90,
        "speed": 80,
        "total": 520
    },
    {
        "name": "axew",
        "types": [
            "dragon"
        ],
        "hp": 46,
        "attack": 87,
        "defense": 60,
        "attack+": 30,
        "defense+": 40,
        "speed": 57,
        "total": 320
    },
    {
        "name": "fraxure",
        "types": [
            "dragon"
        ],
        "hp": 66,
        "attack": 117,
        "defense": 70,
        "attack+": 40,
        "defense+": 50,
        "speed": 67,
        "total": 410
    },
    {
        "name": "haxorus",
        "types": [
            "dragon"
        ],
        "hp": 76,
        "attack": 147,
        "defense": 90,
        "attack+": 60,
        "defense+": 70,
        "speed": 97,
        "total": 540
    },
    {
        "name": "cubchoo",
        "types": [
            "ice"
        ],
        "hp": 55,
        "attack": 70,
        "defense": 40,
        "attack+": 60,
        "defense+": 40,
        "speed": 40,
        "total": 305
    },
    {
        "name": "beartic",
        "types": [
            "ice"
        ],
        "hp": 95,
        "attack": 130,
        "defense": 80,
        "attack+": 70,
        "defense+": 80,
        "speed": 50,
        "total": 505
    },
    {
        "name": "cryogonal",
        "types": [
            "ice"
        ],
        "hp": 80,
        "attack": 50,
        "defense": 50,
        "attack+": 95,
        "defense+": 135,
        "speed": 105,
        "total": 515
    },
    {
        "name": "shelmet",
        "types": [
            "bug"
        ],
        "hp": 50,
        "attack": 40,
        "defense": 85,
        "attack+": 40,
        "defense+": 65,
        "speed": 25,
        "total": 305
    },
    {
        "name": "accelgor",
        "types": [
            "bug"
        ],
        "hp": 80,
        "attack": 70,
        "defense": 40,
        "attack+": 100,
        "defense+": 60,
        "speed": 145,
        "total": 495
    },
    {
        "name": "stunfisk",
        "types": [
            "ground",
            "electric"
        ],
        "hp": 109,
        "attack": 66,
        "defense": 84,
        "attack+": 81,
        "defense+": 99,
        "speed": 32,
        "total": 471
    },
    {
        "name": "mienfoo",
        "types": [
            "fighting"
        ],
        "hp": 45,
        "attack": 85,
        "defense": 50,
        "attack+": 55,
        "defense+": 50,
        "speed": 65,
        "total": 350
    },
    {
        "name": "mienshao",
        "types": [
            "fighting"
        ],
        "hp": 65,
        "attack": 125,
        "defense": 60,
        "attack+": 95,
        "defense+": 60,
        "speed": 105,
        "total": 510
    },
    {
        "name": "druddigon",
        "types": [
            "dragon"
        ],
        "hp": 77,
        "attack": 120,
        "defense": 90,
        "attack+": 60,
        "defense+": 90,
        "speed": 48,
        "total": 485
    },
    {
        "name": "golett",
        "types": [
            "ground",
            "ghost"
        ],
        "hp": 59,
        "attack": 74,
        "defense": 50,
        "attack+": 35,
        "defense+": 50,
        "speed": 35,
        "total": 303
    },
    {
        "name": "golurk",
        "types": [
            "ground",
            "ghost"
        ],
        "hp": 89,
        "attack": 124,
        "defense": 80,
        "attack+": 55,
        "defense+": 80,
        "speed": 55,
        "total": 483
    },
    {
        "name": "pawniard",
        "types": [
            "dark",
            "steel"
        ],
        "hp": 45,
        "attack": 85,
        "defense": 70,
        "attack+": 40,
        "defense+": 40,
        "speed": 60,
        "total": 340
    },
    {
        "name": "bisharp",
        "types": [
            "dark",
            "steel"
        ],
        "hp": 65,
        "attack": 125,
        "defense": 100,
        "attack+": 60,
        "defense+": 70,
        "speed": 70,
        "total": 490
    },
    {
        "name": "bouffalant",
        "types": [
            "normal"
        ],
        "hp": 95,
        "attack": 110,
        "defense": 95,
        "attack+": 40,
        "defense+": 95,
        "speed": 55,
        "total": 490
    },
    {
        "name": "rufflet",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 70,
        "attack": 83,
        "defense": 50,
        "attack+": 37,
        "defense+": 50,
        "speed": 60,
        "total": 350
    },
    {
        "name": "braviary",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 100,
        "attack": 123,
        "defense": 75,
        "attack+": 57,
        "defense+": 75,
        "speed": 80,
        "total": 510
    },
    {
        "name": "vullaby",
        "types": [
            "dark",
            "flying"
        ],
        "hp": 70,
        "attack": 55,
        "defense": 75,
        "attack+": 45,
        "defense+": 65,
        "speed": 60,
        "total": 370
    },
    {
        "name": "mandibuzz",
        "types": [
            "dark",
            "flying"
        ],
        "hp": 110,
        "attack": 65,
        "defense": 105,
        "attack+": 55,
        "defense+": 95,
        "speed": 80,
        "total": 510
    },
    {
        "name": "heatmor",
        "types": [
            "fire"
        ],
        "hp": 85,
        "attack": 97,
        "defense": 66,
        "attack+": 105,
        "defense+": 66,
        "speed": 65,
        "total": 484
    },
    {
        "name": "durant",
        "types": [
            "bug",
            "steel"
        ],
        "hp": 58,
        "attack": 109,
        "defense": 112,
        "attack+": 48,
        "defense+": 48,
        "speed": 109,
        "total": 484
    },
    {
        "name": "deino",
        "types": [
            "dark",
            "dragon"
        ],
        "hp": 52,
        "attack": 65,
        "defense": 50,
        "attack+": 45,
        "defense+": 50,
        "speed": 38,
        "total": 300
    },
    {
        "name": "zweilous",
        "types": [
            "dark",
            "dragon"
        ],
        "hp": 72,
        "attack": 85,
        "defense": 70,
        "attack+": 65,
        "defense+": 70,
        "speed": 58,
        "total": 420
    },
    {
        "name": "hydreigon",
        "types": [
            "dark",
            "dragon"
        ],
        "hp": 92,
        "attack": 105,
        "defense": 90,
        "attack+": 125,
        "defense+": 90,
        "speed": 98,
        "total": 600
    },
    {
        "name": "larvesta",
        "types": [
            "bug",
            "fire"
        ],
        "hp": 55,
        "attack": 85,
        "defense": 55,
        "attack+": 50,
        "defense+": 55,
        "speed": 60,
        "total": 360
    },
    {
        "name": "volcarona",
        "types": [
            "bug",
            "fire"
        ],
        "hp": 85,
        "attack": 60,
        "defense": 65,
        "attack+": 135,
        "defense+": 105,
        "speed": 100,
        "total": 550
    },
    {
        "name": "cobalion",
        "types": [
            "steel",
            "fighting"
        ],
        "hp": 91,
        "attack": 90,
        "defense": 129,
        "attack+": 90,
        "defense+": 72,
        "speed": 108,
        "total": 580
    },
    {
        "name": "terrakion",
        "types": [
            "rock",
            "fighting"
        ],
        "hp": 91,
        "attack": 129,
        "defense": 90,
        "attack+": 72,
        "defense+": 90,
        "speed": 108,
        "total": 580
    },
    {
        "name": "virizion",
        "types": [
            "grass",
            "fighting"
        ],
        "hp": 91,
        "attack": 90,
        "defense": 72,
        "attack+": 90,
        "defense+": 129,
        "speed": 108,
        "total": 580
    },
    {
        "name": "tornadus",
        "types": [
            "flying"
        ],
        "hp": 79,
        "attack": 115,
        "defense": 70,
        "attack+": 125,
        "defense+": 80,
        "speed": 111,
        "total": 580
    },
    {
        "name": "thundurus",
        "types": [
            "electric",
            "flying"
        ],
        "hp": 79,
        "attack": 115,
        "defense": 70,
        "attack+": 125,
        "defense+": 80,
        "speed": 111,
        "total": 580
    },
    {
        "name": "reshiram",
        "types": [
            "dragon",
            "fire"
        ],
        "hp": 100,
        "attack": 120,
        "defense": 100,
        "attack+": 150,
        "defense+": 120,
        "speed": 90,
        "total": 680
    },
    {
        "name": "zekrom",
        "types": [
            "dragon",
            "electric"
        ],
        "hp": 100,
        "attack": 150,
        "defense": 120,
        "attack+": 120,
        "defense+": 100,
        "speed": 90,
        "total": 680
    },
    {
        "name": "landorus",
        "types": [
            "ground",
            "flying"
        ],
        "hp": 89,
        "attack": 125,
        "defense": 90,
        "attack+": 115,
        "defense+": 80,
        "speed": 101,
        "total": 600
    },
    {
        "name": "kyurem",
        "types": [
            "dragon",
            "ice"
        ],
        "hp": 125,
        "attack": 130,
        "defense": 90,
        "attack+": 130,
        "defense+": 90,
        "speed": 95,
        "total": 660
    },
    {
        "name": "keldeo",
        "types": [
            "water",
            "fighting"
        ],
        "hp": 91,
        "attack": 72,
        "defense": 90,
        "attack+": 129,
        "defense+": 90,
        "speed": 108,
        "total": 580
    },
    {
        "name": "meloetta",
        "types": [
            "normal",
            "psychic"
        ],
        "hp": 100,
        "attack": 77,
        "defense": 77,
        "attack+": 128,
        "defense+": 128,
        "speed": 90,
        "total": 600
    },
    {
        "name": "genesect",
        "types": [
            "bug",
            "steel"
        ],
        "hp": 71,
        "attack": 120,
        "defense": 95,
        "attack+": 120,
        "defense+": 95,
        "speed": 99,
        "total": 600
    },
    {
        "name": "chespin",
        "types": [
            "grass"
        ],
        "hp": 56,
        "attack": 61,
        "defense": 65,
        "attack+": 48,
        "defense+": 45,
        "speed": 38,
        "total": 313
    },
    {
        "name": "quilladin",
        "types": [
            "grass"
        ],
        "hp": 61,
        "attack": 78,
        "defense": 95,
        "attack+": 56,
        "defense+": 58,
        "speed": 57,
        "total": 405
    },
    {
        "name": "chesnaught",
        "types": [
            "grass",
            "fighting"
        ],
        "hp": 88,
        "attack": 107,
        "defense": 122,
        "attack+": 74,
        "defense+": 75,
        "speed": 64,
        "total": 530
    },
    {
        "name": "fennekin",
        "types": [
            "fire"
        ],
        "hp": 40,
        "attack": 45,
        "defense": 40,
        "attack+": 62,
        "defense+": 60,
        "speed": 60,
        "total": 307
    },
    {
        "name": "braixen",
        "types": [
            "fire"
        ],
        "hp": 59,
        "attack": 59,
        "defense": 58,
        "attack+": 90,
        "defense+": 70,
        "speed": 73,
        "total": 409
    },
    {
        "name": "delphox",
        "types": [
            "fire",
            "psychic"
        ],
        "hp": 75,
        "attack": 69,
        "defense": 72,
        "attack+": 114,
        "defense+": 100,
        "speed": 104,
        "total": 534
    },
    {
        "name": "froakie",
        "types": [
            "water"
        ],
        "hp": 41,
        "attack": 56,
        "defense": 40,
        "attack+": 62,
        "defense+": 44,
        "speed": 71,
        "total": 314
    },
    {
        "name": "frogadier",
        "types": [
            "water"
        ],
        "hp": 54,
        "attack": 63,
        "defense": 52,
        "attack+": 83,
        "defense+": 56,
        "speed": 97,
        "total": 405
    },
    {
        "name": "greninja",
        "types": [
            "water",
            "dark"
        ],
        "hp": 72,
        "attack": 95,
        "defense": 67,
        "attack+": 103,
        "defense+": 71,
        "speed": 122,
        "total": 530
    },
    {
        "name": "bunnelby",
        "types": [
            "normal"
        ],
        "hp": 38,
        "attack": 36,
        "defense": 38,
        "attack+": 32,
        "defense+": 36,
        "speed": 57,
        "total": 237
    },
    {
        "name": "diggersby",
        "types": [
            "normal",
            "ground"
        ],
        "hp": 85,
        "attack": 56,
        "defense": 77,
        "attack+": 50,
        "defense+": 77,
        "speed": 78,
        "total": 423
    },
    {
        "name": "fletchling",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 45,
        "attack": 50,
        "defense": 43,
        "attack+": 40,
        "defense+": 38,
        "speed": 62,
        "total": 278
    },
    {
        "name": "fletchinder",
        "types": [
            "fire",
            "flying"
        ],
        "hp": 62,
        "attack": 73,
        "defense": 55,
        "attack+": 56,
        "defense+": 52,
        "speed": 84,
        "total": 382
    },
    {
        "name": "talonflame",
        "types": [
            "fire",
            "flying"
        ],
        "hp": 78,
        "attack": 81,
        "defense": 71,
        "attack+": 74,
        "defense+": 69,
        "speed": 126,
        "total": 499
    },
    {
        "name": "scatterbug",
        "types": [
            "bug"
        ],
        "hp": 38,
        "attack": 35,
        "defense": 40,
        "attack+": 27,
        "defense+": 25,
        "speed": 35,
        "total": 200
    },
    {
        "name": "spewpa",
        "types": [
            "bug"
        ],
        "hp": 45,
        "attack": 22,
        "defense": 60,
        "attack+": 27,
        "defense+": 30,
        "speed": 29,
        "total": 213
    },
    {
        "name": "vivillon",
        "types": [
            "bug",
            "flying"
        ],
        "hp": 80,
        "attack": 52,
        "defense": 50,
        "attack+": 90,
        "defense+": 50,
        "speed": 89,
        "total": 411
    },
    {
        "name": "litleo",
        "types": [
            "fire",
            "normal"
        ],
        "hp": 62,
        "attack": 50,
        "defense": 58,
        "attack+": 73,
        "defense+": 54,
        "speed": 72,
        "total": 369
    },
    {
        "name": "pyroar",
        "types": [
            "fire",
            "normal"
        ],
        "hp": 86,
        "attack": 68,
        "defense": 72,
        "attack+": 109,
        "defense+": 66,
        "speed": 106,
        "total": 507
    },
    {
        "name": "flab\u00e9b\u00e9",
        "types": [
            "fairy"
        ],
        "hp": 44,
        "attack": 38,
        "defense": 39,
        "attack+": 61,
        "defense+": 79,
        "speed": 42,
        "total": 303
    },
    {
        "name": "floette",
        "types": [
            "fairy"
        ],
        "hp": 54,
        "attack": 45,
        "defense": 47,
        "attack+": 75,
        "defense+": 98,
        "speed": 52,
        "total": 371
    },
    {
        "name": "florges",
        "types": [
            "fairy"
        ],
        "hp": 78,
        "attack": 65,
        "defense": 68,
        "attack+": 112,
        "defense+": 154,
        "speed": 75,
        "total": 552
    },
    {
        "name": "skiddo",
        "types": [
            "grass"
        ],
        "hp": 66,
        "attack": 65,
        "defense": 48,
        "attack+": 62,
        "defense+": 57,
        "speed": 52,
        "total": 350
    },
    {
        "name": "gogoat",
        "types": [
            "grass"
        ],
        "hp": 123,
        "attack": 100,
        "defense": 62,
        "attack+": 97,
        "defense+": 81,
        "speed": 68,
        "total": 531
    },
    {
        "name": "pancham",
        "types": [
            "fighting"
        ],
        "hp": 67,
        "attack": 82,
        "defense": 62,
        "attack+": 46,
        "defense+": 48,
        "speed": 43,
        "total": 348
    },
    {
        "name": "pangoro",
        "types": [
            "fighting",
            "dark"
        ],
        "hp": 95,
        "attack": 124,
        "defense": 78,
        "attack+": 69,
        "defense+": 71,
        "speed": 58,
        "total": 495
    },
    {
        "name": "furfrou",
        "types": [
            "normal"
        ],
        "hp": 75,
        "attack": 80,
        "defense": 60,
        "attack+": 65,
        "defense+": 90,
        "speed": 102,
        "total": 472
    },
    {
        "name": "espurr",
        "types": [
            "psychic"
        ],
        "hp": 62,
        "attack": 48,
        "defense": 54,
        "attack+": 63,
        "defense+": 60,
        "speed": 68,
        "total": 355
    },
    {
        "name": "meowstic",
        "types": [
            "psychic"
        ],
        "hp": 74,
        "attack": 48,
        "defense": 76,
        "attack+": 83,
        "defense+": 81,
        "speed": 104,
        "total": 466
    },
    {
        "name": "honedge",
        "types": [
            "steel",
            "ghost"
        ],
        "hp": 45,
        "attack": 80,
        "defense": 100,
        "attack+": 35,
        "defense+": 37,
        "speed": 28,
        "total": 325
    },
    {
        "name": "doublade",
        "types": [
            "steel",
            "ghost"
        ],
        "hp": 59,
        "attack": 110,
        "defense": 150,
        "attack+": 45,
        "defense+": 49,
        "speed": 35,
        "total": 448
    },
    {
        "name": "aegislash",
        "types": [
            "steel",
            "ghost"
        ],
        "hp": 60,
        "attack": 50,
        "defense": 140,
        "attack+": 50,
        "defense+": 140,
        "speed": 60,
        "total": 500
    },
    {
        "name": "spritzee",
        "types": [
            "fairy"
        ],
        "hp": 78,
        "attack": 52,
        "defense": 60,
        "attack+": 63,
        "defense+": 65,
        "speed": 23,
        "total": 341
    },
    {
        "name": "aromatisse",
        "types": [
            "fairy"
        ],
        "hp": 101,
        "attack": 72,
        "defense": 72,
        "attack+": 99,
        "defense+": 89,
        "speed": 29,
        "total": 462
    },
    {
        "name": "swirlix",
        "types": [
            "fairy"
        ],
        "hp": 62,
        "attack": 48,
        "defense": 66,
        "attack+": 59,
        "defense+": 57,
        "speed": 49,
        "total": 341
    },
    {
        "name": "slurpuff",
        "types": [
            "fairy"
        ],
        "hp": 82,
        "attack": 80,
        "defense": 86,
        "attack+": 85,
        "defense+": 75,
        "speed": 72,
        "total": 480
    },
    {
        "name": "inkay",
        "types": [
            "dark",
            "psychic"
        ],
        "hp": 53,
        "attack": 54,
        "defense": 53,
        "attack+": 37,
        "defense+": 46,
        "speed": 45,
        "total": 288
    },
    {
        "name": "malamar",
        "types": [
            "dark",
            "psychic"
        ],
        "hp": 86,
        "attack": 92,
        "defense": 88,
        "attack+": 68,
        "defense+": 75,
        "speed": 73,
        "total": 482
    },
    {
        "name": "binacle",
        "types": [
            "rock",
            "water"
        ],
        "hp": 42,
        "attack": 52,
        "defense": 67,
        "attack+": 39,
        "defense+": 56,
        "speed": 50,
        "total": 306
    },
    {
        "name": "barbaracle",
        "types": [
            "rock",
            "water"
        ],
        "hp": 72,
        "attack": 105,
        "defense": 115,
        "attack+": 54,
        "defense+": 86,
        "speed": 68,
        "total": 500
    },
    {
        "name": "skrelp",
        "types": [
            "poison",
            "water"
        ],
        "hp": 50,
        "attack": 60,
        "defense": 60,
        "attack+": 60,
        "defense+": 60,
        "speed": 30,
        "total": 320
    },
    {
        "name": "dragalge",
        "types": [
            "poison",
            "dragon"
        ],
        "hp": 65,
        "attack": 75,
        "defense": 90,
        "attack+": 97,
        "defense+": 123,
        "speed": 44,
        "total": 494
    },
    {
        "name": "clauncher",
        "types": [
            "water"
        ],
        "hp": 50,
        "attack": 53,
        "defense": 62,
        "attack+": 58,
        "defense+": 63,
        "speed": 44,
        "total": 330
    },
    {
        "name": "clawitzer",
        "types": [
            "water"
        ],
        "hp": 71,
        "attack": 73,
        "defense": 88,
        "attack+": 120,
        "defense+": 89,
        "speed": 59,
        "total": 500
    },
    {
        "name": "helioptile",
        "types": [
            "electric",
            "normal"
        ],
        "hp": 44,
        "attack": 38,
        "defense": 33,
        "attack+": 61,
        "defense+": 43,
        "speed": 70,
        "total": 289
    },
    {
        "name": "heliolisk",
        "types": [
            "electric",
            "normal"
        ],
        "hp": 62,
        "attack": 55,
        "defense": 52,
        "attack+": 109,
        "defense+": 94,
        "speed": 109,
        "total": 481
    },
    {
        "name": "tyrunt",
        "types": [
            "rock",
            "dragon"
        ],
        "hp": 58,
        "attack": 89,
        "defense": 77,
        "attack+": 45,
        "defense+": 45,
        "speed": 48,
        "total": 362
    },
    {
        "name": "tyrantrum",
        "types": [
            "rock",
            "dragon"
        ],
        "hp": 82,
        "attack": 121,
        "defense": 119,
        "attack+": 69,
        "defense+": 59,
        "speed": 71,
        "total": 521
    },
    {
        "name": "amaura",
        "types": [
            "rock",
            "ice"
        ],
        "hp": 77,
        "attack": 59,
        "defense": 50,
        "attack+": 67,
        "defense+": 63,
        "speed": 46,
        "total": 362
    },
    {
        "name": "aurorus",
        "types": [
            "rock",
            "ice"
        ],
        "hp": 123,
        "attack": 77,
        "defense": 72,
        "attack+": 99,
        "defense+": 92,
        "speed": 58,
        "total": 521
    },
    {
        "name": "sylveon",
        "types": [
            "fairy"
        ],
        "hp": 95,
        "attack": 65,
        "defense": 65,
        "attack+": 110,
        "defense+": 130,
        "speed": 60,
        "total": 525
    },
    {
        "name": "hawlucha",
        "types": [
            "fighting",
            "flying"
        ],
        "hp": 78,
        "attack": 92,
        "defense": 75,
        "attack+": 74,
        "defense+": 63,
        "speed": 118,
        "total": 500
    },
    {
        "name": "dedenne",
        "types": [
            "electric",
            "fairy"
        ],
        "hp": 67,
        "attack": 58,
        "defense": 57,
        "attack+": 81,
        "defense+": 67,
        "speed": 101,
        "total": 431
    },
    {
        "name": "carbink",
        "types": [
            "rock",
            "fairy"
        ],
        "hp": 50,
        "attack": 50,
        "defense": 150,
        "attack+": 50,
        "defense+": 150,
        "speed": 50,
        "total": 500
    },
    {
        "name": "goomy",
        "types": [
            "dragon"
        ],
        "hp": 45,
        "attack": 50,
        "defense": 35,
        "attack+": 55,
        "defense+": 75,
        "speed": 40,
        "total": 300
    },
    {
        "name": "sliggoo",
        "types": [
            "dragon"
        ],
        "hp": 68,
        "attack": 75,
        "defense": 53,
        "attack+": 83,
        "defense+": 113,
        "speed": 60,
        "total": 452
    },
    {
        "name": "goodra",
        "types": [
            "dragon"
        ],
        "hp": 90,
        "attack": 100,
        "defense": 70,
        "attack+": 110,
        "defense+": 150,
        "speed": 80,
        "total": 600
    },
    {
        "name": "klefki",
        "types": [
            "steel",
            "fairy"
        ],
        "hp": 57,
        "attack": 80,
        "defense": 91,
        "attack+": 80,
        "defense+": 87,
        "speed": 75,
        "total": 470
    },
    {
        "name": "phantump",
        "types": [
            "ghost",
            "grass"
        ],
        "hp": 43,
        "attack": 70,
        "defense": 48,
        "attack+": 50,
        "defense+": 60,
        "speed": 38,
        "total": 309
    },
    {
        "name": "trevenant",
        "types": [
            "ghost",
            "grass"
        ],
        "hp": 85,
        "attack": 110,
        "defense": 76,
        "attack+": 65,
        "defense+": 82,
        "speed": 56,
        "total": 474
    },
    {
        "name": "pumpkaboo",
        "types": [
            "ghost",
            "grass"
        ],
        "hp": 49,
        "attack": 66,
        "defense": 70,
        "attack+": 44,
        "defense+": 55,
        "speed": 51,
        "total": 335
    },
    {
        "name": "gourgeist",
        "types": [
            "ghost",
            "grass"
        ],
        "hp": 65,
        "attack": 90,
        "defense": 122,
        "attack+": 58,
        "defense+": 75,
        "speed": 84,
        "total": 494
    },
    {
        "name": "bergmite",
        "types": [
            "ice"
        ],
        "hp": 55,
        "attack": 69,
        "defense": 85,
        "attack+": 32,
        "defense+": 35,
        "speed": 28,
        "total": 304
    },
    {
        "name": "avalugg",
        "types": [
            "ice"
        ],
        "hp": 95,
        "attack": 117,
        "defense": 184,
        "attack+": 44,
        "defense+": 46,
        "speed": 28,
        "total": 514
    },
    {
        "name": "noibat",
        "types": [
            "flying",
            "dragon"
        ],
        "hp": 40,
        "attack": 30,
        "defense": 35,
        "attack+": 45,
        "defense+": 40,
        "speed": 55,
        "total": 245
    },
    {
        "name": "noivern",
        "types": [
            "flying",
            "dragon"
        ],
        "hp": 85,
        "attack": 70,
        "defense": 80,
        "attack+": 97,
        "defense+": 80,
        "speed": 123,
        "total": 535
    },
    {
        "name": "xerneas",
        "types": [
            "fairy"
        ],
        "hp": 126,
        "attack": 131,
        "defense": 95,
        "attack+": 131,
        "defense+": 98,
        "speed": 99,
        "total": 680
    },
    {
        "name": "yveltal",
        "types": [
            "dark",
            "flying"
        ],
        "hp": 126,
        "attack": 131,
        "defense": 95,
        "attack+": 131,
        "defense+": 98,
        "speed": 99,
        "total": 680
    },
    {
        "name": "zygarde",
        "types": [
            "dragon",
            "ground"
        ],
        "hp": 108,
        "attack": 100,
        "defense": 121,
        "attack+": 81,
        "defense+": 95,
        "speed": 95,
        "total": 600
    },
    {
        "name": "diancie",
        "types": [
            "rock",
            "fairy"
        ],
        "hp": 50,
        "attack": 100,
        "defense": 150,
        "attack+": 100,
        "defense+": 150,
        "speed": 50,
        "total": 600
    },
    {
        "name": "hoopa",
        "types": [
            "psychic",
            "ghost"
        ],
        "hp": 80,
        "attack": 110,
        "defense": 60,
        "attack+": 150,
        "defense+": 130,
        "speed": 70,
        "total": 600
    },
    {
        "name": "volcanion",
        "types": [
            "fire",
            "water"
        ],
        "hp": 80,
        "attack": 110,
        "defense": 120,
        "attack+": 130,
        "defense+": 90,
        "speed": 70,
        "total": 600
    },
    {
        "name": "rowlet",
        "types": [
            "grass",
            "flying"
        ],
        "hp": 68,
        "attack": 55,
        "defense": 55,
        "attack+": 50,
        "defense+": 50,
        "speed": 42,
        "total": 320
    },
    {
        "name": "dartrix",
        "types": [
            "grass",
            "flying"
        ],
        "hp": 78,
        "attack": 75,
        "defense": 75,
        "attack+": 70,
        "defense+": 70,
        "speed": 52,
        "total": 420
    },
    {
        "name": "decidueye",
        "types": [
            "grass",
            "ghost"
        ],
        "hp": 78,
        "attack": 107,
        "defense": 75,
        "attack+": 100,
        "defense+": 100,
        "speed": 70,
        "total": 530
    },
    {
        "name": "litten",
        "types": [
            "fire"
        ],
        "hp": 45,
        "attack": 65,
        "defense": 40,
        "attack+": 60,
        "defense+": 40,
        "speed": 70,
        "total": 320
    },
    {
        "name": "torracat",
        "types": [
            "fire"
        ],
        "hp": 65,
        "attack": 85,
        "defense": 50,
        "attack+": 80,
        "defense+": 50,
        "speed": 90,
        "total": 420
    },
    {
        "name": "incineroar",
        "types": [
            "fire",
            "dark"
        ],
        "hp": 95,
        "attack": 115,
        "defense": 90,
        "attack+": 80,
        "defense+": 90,
        "speed": 60,
        "total": 530
    },
    {
        "name": "popplio",
        "types": [
            "water"
        ],
        "hp": 50,
        "attack": 54,
        "defense": 54,
        "attack+": 66,
        "defense+": 56,
        "speed": 40,
        "total": 320
    },
    {
        "name": "brionne",
        "types": [
            "water"
        ],
        "hp": 60,
        "attack": 69,
        "defense": 69,
        "attack+": 91,
        "defense+": 81,
        "speed": 50,
        "total": 420
    },
    {
        "name": "primarina",
        "types": [
            "water",
            "fairy"
        ],
        "hp": 80,
        "attack": 74,
        "defense": 74,
        "attack+": 126,
        "defense+": 116,
        "speed": 60,
        "total": 530
    },
    {
        "name": "pikipek",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 35,
        "attack": 75,
        "defense": 30,
        "attack+": 30,
        "defense+": 30,
        "speed": 65,
        "total": 265
    },
    {
        "name": "trumbeak",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 55,
        "attack": 85,
        "defense": 50,
        "attack+": 40,
        "defense+": 50,
        "speed": 75,
        "total": 355
    },
    {
        "name": "toucannon",
        "types": [
            "normal",
            "flying"
        ],
        "hp": 80,
        "attack": 120,
        "defense": 75,
        "attack+": 75,
        "defense+": 75,
        "speed": 60,
        "total": 485
    },
    {
        "name": "yungoos",
        "types": [
            "normal"
        ],
        "hp": 48,
        "attack": 70,
        "defense": 30,
        "attack+": 30,
        "defense+": 30,
        "speed": 45,
        "total": 253
    },
    {
        "name": "gumshoos",
        "types": [
            "normal"
        ],
        "hp": 88,
        "attack": 110,
        "defense": 60,
        "attack+": 55,
        "defense+": 60,
        "speed": 45,
        "total": 418
    },
    {
        "name": "grubbin",
        "types": [
            "bug"
        ],
        "hp": 47,
        "attack": 62,
        "defense": 45,
        "attack+": 55,
        "defense+": 45,
        "speed": 46,
        "total": 300
    },
    {
        "name": "charjabug",
        "types": [
            "bug",
            "electric"
        ],
        "hp": 57,
        "attack": 82,
        "defense": 95,
        "attack+": 55,
        "defense+": 75,
        "speed": 36,
        "total": 400
    },
    {
        "name": "vikavolt",
        "types": [
            "bug",
            "electric"
        ],
        "hp": 77,
        "attack": 70,
        "defense": 90,
        "attack+": 145,
        "defense+": 75,
        "speed": 43,
        "total": 500
    },
    {
        "name": "crabrawler",
        "types": [
            "fighting"
        ],
        "hp": 47,
        "attack": 82,
        "defense": 57,
        "attack+": 42,
        "defense+": 47,
        "speed": 63,
        "total": 338
    },
    {
        "name": "crabominable",
        "types": [
            "fighting",
            "ice"
        ],
        "hp": 97,
        "attack": 132,
        "defense": 77,
        "attack+": 62,
        "defense+": 67,
        "speed": 43,
        "total": 478
    },
    {
        "name": "oricorio",
        "types": [
            "fire",
            "flying"
        ],
        "hp": 75,
        "attack": 70,
        "defense": 70,
        "attack+": 98,
        "defense+": 70,
        "speed": 93,
        "total": 476
    },
    {
        "name": "cutiefly",
        "types": [
            "bug",
            "fairy"
        ],
        "hp": 40,
        "attack": 45,
        "defense": 40,
        "attack+": 55,
        "defense+": 40,
        "speed": 84,
        "total": 304
    },
    {
        "name": "ribombee",
        "types": [
            "bug",
            "fairy"
        ],
        "hp": 60,
        "attack": 55,
        "defense": 60,
        "attack+": 95,
        "defense+": 70,
        "speed": 124,
        "total": 464
    },
    {
        "name": "rockruff",
        "types": [
            "rock"
        ],
        "hp": 45,
        "attack": 65,
        "defense": 40,
        "attack+": 30,
        "defense+": 40,
        "speed": 60,
        "total": 280
    },
    {
        "name": "lycanroc",
        "types": [
            "rock"
        ],
        "hp": 75,
        "attack": 115,
        "defense": 65,
        "attack+": 55,
        "defense+": 65,
        "speed": 112,
        "total": 487
    },
    {
        "name": "wishiwashi",
        "types": [
            "water"
        ],
        "hp": 45,
        "attack": 20,
        "defense": 20,
        "attack+": 25,
        "defense+": 25,
        "speed": 40,
        "total": 175
    },
    {
        "name": "mareanie",
        "types": [
            "poison",
            "water"
        ],
        "hp": 50,
        "attack": 53,
        "defense": 62,
        "attack+": 43,
        "defense+": 52,
        "speed": 45,
        "total": 305
    },
    {
        "name": "toxapex",
        "types": [
            "poison",
            "water"
        ],
        "hp": 50,
        "attack": 63,
        "defense": 152,
        "attack+": 53,
        "defense+": 142,
        "speed": 35,
        "total": 495
    },
    {
        "name": "mudbray",
        "types": [
            "ground"
        ],
        "hp": 70,
        "attack": 100,
        "defense": 70,
        "attack+": 45,
        "defense+": 55,
        "speed": 45,
        "total": 385
    },
    {
        "name": "mudsdale",
        "types": [
            "ground"
        ],
        "hp": 100,
        "attack": 125,
        "defense": 100,
        "attack+": 55,
        "defense+": 85,
        "speed": 35,
        "total": 500
    },
    {
        "name": "dewpider",
        "types": [
            "water",
            "bug"
        ],
        "hp": 38,
        "attack": 40,
        "defense": 52,
        "attack+": 40,
        "defense+": 72,
        "speed": 27,
        "total": 269
    },
    {
        "name": "araquanid",
        "types": [
            "water",
            "bug"
        ],
        "hp": 68,
        "attack": 70,
        "defense": 92,
        "attack+": 50,
        "defense+": 132,
        "speed": 42,
        "total": 454
    },
    {
        "name": "fomantis",
        "types": [
            "grass"
        ],
        "hp": 40,
        "attack": 55,
        "defense": 35,
        "attack+": 50,
        "defense+": 35,
        "speed": 35,
        "total": 250
    },
    {
        "name": "lurantis",
        "types": [
            "grass"
        ],
        "hp": 70,
        "attack": 105,
        "defense": 90,
        "attack+": 80,
        "defense+": 90,
        "speed": 45,
        "total": 480
    },
    {
        "name": "morelull",
        "types": [
            "grass",
            "fairy"
        ],
        "hp": 40,
        "attack": 35,
        "defense": 55,
        "attack+": 65,
        "defense+": 75,
        "speed": 15,
        "total": 285
    },
    {
        "name": "shiinotic",
        "types": [
            "grass",
            "fairy"
        ],
        "hp": 60,
        "attack": 45,
        "defense": 80,
        "attack+": 90,
        "defense+": 100,
        "speed": 30,
        "total": 405
    },
    {
        "name": "salandit",
        "types": [
            "poison",
            "fire"
        ],
        "hp": 48,
        "attack": 44,
        "defense": 40,
        "attack+": 71,
        "defense+": 40,
        "speed": 77,
        "total": 320
    },
    {
        "name": "salazzle",
        "types": [
            "poison",
            "fire"
        ],
        "hp": 68,
        "attack": 64,
        "defense": 60,
        "attack+": 111,
        "defense+": 60,
        "speed": 117,
        "total": 480
    },
    {
        "name": "stufful",
        "types": [
            "normal",
            "fighting"
        ],
        "hp": 70,
        "attack": 75,
        "defense": 50,
        "attack+": 45,
        "defense+": 50,
        "speed": 50,
        "total": 340
    },
    {
        "name": "bewear",
        "types": [
            "normal",
            "fighting"
        ],
        "hp": 120,
        "attack": 125,
        "defense": 80,
        "attack+": 55,
        "defense+": 60,
        "speed": 60,
        "total": 500
    },
    {
        "name": "bounsweet",
        "types": [
            "grass"
        ],
        "hp": 42,
        "attack": 30,
        "defense": 38,
        "attack+": 30,
        "defense+": 38,
        "speed": 32,
        "total": 210
    },
    {
        "name": "steenee",
        "types": [
            "grass"
        ],
        "hp": 52,
        "attack": 40,
        "defense": 48,
        "attack+": 40,
        "defense+": 48,
        "speed": 62,
        "total": 290
    },
    {
        "name": "tsareena",
        "types": [
            "grass"
        ],
        "hp": 72,
        "attack": 120,
        "defense": 98,
        "attack+": 50,
        "defense+": 98,
        "speed": 72,
        "total": 510
    },
    {
        "name": "comfey",
        "types": [
            "fairy"
        ],
        "hp": 51,
        "attack": 52,
        "defense": 90,
        "attack+": 82,
        "defense+": 110,
        "speed": 100,
        "total": 485
    },
    {
        "name": "oranguru",
        "types": [
            "normal",
            "psychic"
        ],
        "hp": 90,
        "attack": 60,
        "defense": 80,
        "attack+": 90,
        "defense+": 110,
        "speed": 60,
        "total": 490
    },
    {
        "name": "passimian",
        "types": [
            "fighting"
        ],
        "hp": 100,
        "attack": 120,
        "defense": 90,
        "attack+": 40,
        "defense+": 60,
        "speed": 80,
        "total": 490
    },
    {
        "name": "wimpod",
        "types": [
            "bug",
            "water"
        ],
        "hp": 25,
        "attack": 35,
        "defense": 40,
        "attack+": 20,
        "defense+": 30,
        "speed": 80,
        "total": 230
    },
    {
        "name": "golisopod",
        "types": [
            "bug",
            "water"
        ],
        "hp": 75,
        "attack": 125,
        "defense": 140,
        "attack+": 60,
        "defense+": 90,
        "speed": 40,
        "total": 530
    },
    {
        "name": "sandygast",
        "types": [
            "ghost",
            "ground"
        ],
        "hp": 55,
        "attack": 55,
        "defense": 80,
        "attack+": 70,
        "defense+": 45,
        "speed": 15,
        "total": 320
    },
    {
        "name": "palossand",
        "types": [
            "ghost",
            "ground"
        ],
        "hp": 85,
        "attack": 75,
        "defense": 110,
        "attack+": 100,
        "defense+": 75,
        "speed": 35,
        "total": 480
    },
    {
        "name": "pyukumuku",
        "types": [
            "water"
        ],
        "hp": 55,
        "attack": 60,
        "defense": 130,
        "attack+": 30,
        "defense+": 130,
        "speed": 5,
        "total": 410
    },
    {
        "name": "type:",
        "types": [
            "normal"
        ],
        "hp": 95,
        "attack": 95,
        "defense": 95,
        "attack+": 95,
        "defense+": 95,
        "speed": 59,
        "total": 534
    },
    {
        "name": "silvally",
        "types": [
            "normal"
        ],
        "hp": 95,
        "attack": 95,
        "defense": 95,
        "attack+": 95,
        "defense+": 95,
        "speed": 95,
        "total": 570
    },
    {
        "name": "minior",
        "types": [
            "rock",
            "flying"
        ],
        "hp": 60,
        "attack": 60,
        "defense": 100,
        "attack+": 60,
        "defense+": 100,
        "speed": 60,
        "total": 440
    },
    {
        "name": "komala",
        "types": [
            "normal"
        ],
        "hp": 65,
        "attack": 115,
        "defense": 65,
        "attack+": 75,
        "defense+": 95,
        "speed": 65,
        "total": 480
    },
    {
        "name": "turtonator",
        "types": [
            "fire",
            "dragon"
        ],
        "hp": 60,
        "attack": 78,
        "defense": 135,
        "attack+": 91,
        "defense+": 85,
        "speed": 36,
        "total": 485
    },
    {
        "name": "togedemaru",
        "types": [
            "electric",
            "steel"
        ],
        "hp": 65,
        "attack": 98,
        "defense": 63,
        "attack+": 40,
        "defense+": 73,
        "speed": 96,
        "total": 435
    },
    {
        "name": "mimikyu",
        "types": [
            "ghost",
            "fairy"
        ],
        "hp": 55,
        "attack": 90,
        "defense": 80,
        "attack+": 50,
        "defense+": 105,
        "speed": 96,
        "total": 476
    },
    {
        "name": "bruxish",
        "types": [
            "water",
            "psychic"
        ],
        "hp": 68,
        "attack": 105,
        "defense": 70,
        "attack+": 70,
        "defense+": 70,
        "speed": 92,
        "total": 475
    },
    {
        "name": "drampa",
        "types": [
            "normal",
            "dragon"
        ],
        "hp": 78,
        "attack": 60,
        "defense": 85,
        "attack+": 135,
        "defense+": 91,
        "speed": 36,
        "total": 485
    },
    {
        "name": "dhelmise",
        "types": [
            "ghost",
            "grass"
        ],
        "hp": 70,
        "attack": 131,
        "defense": 100,
        "attack+": 86,
        "defense+": 90,
        "speed": 40,
        "total": 517
    },
    {
        "name": "jangmo-o",
        "types": [
            "dragon"
        ],
        "hp": 45,
        "attack": 55,
        "defense": 65,
        "attack+": 45,
        "defense+": 45,
        "speed": 45,
        "total": 300
    },
    {
        "name": "hakamo-o",
        "types": [
            "dragon",
            "fighting"
        ],
        "hp": 55,
        "attack": 75,
        "defense": 90,
        "attack+": 65,
        "defense+": 70,
        "speed": 65,
        "total": 420
    },
    {
        "name": "kommo-o",
        "types": [
            "dragon",
            "fighting"
        ],
        "hp": 75,
        "attack": 110,
        "defense": 125,
        "attack+": 100,
        "defense+": 105,
        "speed": 85,
        "total": 600
    },
    {
        "name": "tapu",
        "types": [
            "electric",
            "fairy"
        ],
        "hp": 70,
        "attack": 115,
        "defense": 85,
        "attack+": 95,
        "defense+": 75,
        "speed": 130,
        "total": 570
    },
    {
        "name": "cosmog",
        "types": [
            "psychic"
        ],
        "hp": 43,
        "attack": 29,
        "defense": 31,
        "attack+": 29,
        "defense+": 31,
        "speed": 37,
        "total": 200
    },
    {
        "name": "cosmoem",
        "types": [
            "psychic"
        ],
        "hp": 43,
        "attack": 29,
        "defense": 131,
        "attack+": 29,
        "defense+": 131,
        "speed": 37,
        "total": 400
    },
    {
        "name": "solgaleo",
        "types": [
            "psychic",
            "steel"
        ],
        "hp": 137,
        "attack": 137,
        "defense": 107,
        "attack+": 113,
        "defense+": 89,
        "speed": 97,
        "total": 680
    },
    {
        "name": "lunala",
        "types": [
            "psychic",
            "ghost"
        ],
        "hp": 137,
        "attack": 113,
        "defense": 89,
        "attack+": 137,
        "defense+": 107,
        "speed": 97,
        "total": 680
    },
    {
        "name": "nihilego",
        "types": [
            "rock",
            "poison"
        ],
        "hp": 109,
        "attack": 53,
        "defense": 47,
        "attack+": 127,
        "defense+": 131,
        "speed": 103,
        "total": 570
    },
    {
        "name": "buzzwole",
        "types": [
            "bug",
            "fighting"
        ],
        "hp": 107,
        "attack": 139,
        "defense": 139,
        "attack+": 53,
        "defense+": 53,
        "speed": 79,
        "total": 570
    },
    {
        "name": "pheromosa",
        "types": [
            "bug",
            "fighting"
        ],
        "hp": 71,
        "attack": 137,
        "defense": 37,
        "attack+": 137,
        "defense+": 37,
        "speed": 151,
        "total": 570
    },
    {
        "name": "xurkitree",
        "types": [
            "electric"
        ],
        "hp": 83,
        "attack": 89,
        "defense": 71,
        "attack+": 173,
        "defense+": 71,
        "speed": 83,
        "total": 570
    },
    {
        "name": "celesteela",
        "types": [
            "steel",
            "flying"
        ],
        "hp": 97,
        "attack": 101,
        "defense": 103,
        "attack+": 107,
        "defense+": 101,
        "speed": 61,
        "total": 570
    },
    {
        "name": "kartana",
        "types": [
            "grass",
            "steel"
        ],
        "hp": 59,
        "attack": 181,
        "defense": 131,
        "attack+": 59,
        "defense+": 31,
        "speed": 109,
        "total": 570
    },
    {
        "name": "guzzlord",
        "types": [
            "dark",
            "dragon"
        ],
        "hp": 223,
        "attack": 101,
        "defense": 53,
        "attack+": 97,
        "defense+": 53,
        "speed": 43,
        "total": 570
    },
    {
        "name": "necrozma",
        "types": [
            "psychic"
        ],
        "hp": 97,
        "attack": 107,
        "defense": 101,
        "attack+": 127,
        "defense+": 89,
        "speed": 79,
        "total": 600
    },
    {
        "name": "magearna",
        "types": [
            "steel",
            "fairy"
        ],
        "hp": 80,
        "attack": 95,
        "defense": 115,
        "attack+": 130,
        "defense+": 115,
        "speed": 65,
        "total": 600
    },
    {
        "name": "marshadow",
        "types": [
            "fighting",
            "ghost"
        ],
        "hp": 90,
        "attack": 125,
        "defense": 80,
        "attack+": 90,
        "defense+": 90,
        "speed": 125,
        "total": 600
    },
    {
        "name": "poipole",
        "types": [
            "poison"
        ],
        "hp": 67,
        "attack": 73,
        "defense": 67,
        "attack+": 73,
        "defense+": 67,
        "speed": 73,
        "total": 420
    },
    {
        "name": "naganadel",
        "types": [
            "poison",
            "dragon"
        ],
        "hp": 73,
        "attack": 73,
        "defense": 73,
        "attack+": 127,
        "defense+": 73,
        "speed": 121,
        "total": 540
    },
    {
        "name": "stakataka",
        "types": [
            "rock",
            "steel"
        ],
        "hp": 61,
        "attack": 131,
        "defense": 211,
        "attack+": 53,
        "defense+": 101,
        "speed": 13,
        "total": 570
    },
    {
        "name": "blacephalon",
        "types": [
            "fire",
            "ghost"
        ],
        "hp": 53,
        "attack": 127,
        "defense": 53,
        "attack+": 151,
        "defense+": 79,
        "speed": 107,
        "total": 570
    },
    {
        "name": "zeraora",
        "types": [
            "electric"
        ],
        "hp": 88,
        "attack": 112,
        "defense": 75,
        "attack+": 102,
        "defense+": 80,
        "speed": 143,
        "total": 600
    },
    {
        "name": "meltan",
        "types": [
            "steel"
        ],
        "hp": 46,
        "attack": 65,
        "defense": 65,
        "attack+": 55,
        "defense+": 35,
        "speed": 34,
        "total": 300
    },
    {
        "name": "melmetal",
        "types": [
            "steel"
        ],
        "hp": 135,
        "attack": 143,
        "defense": 143,
        "attack+": 80,
        "defense+": 65,
        "speed": 34,
        "total": 600
    },
    {
        "name": "grookey",
        "types": [
            "grass"
        ],
        "hp": 50,
        "attack": 65,
        "defense": 50,
        "attack+": 40,
        "defense+": 40,
        "speed": 65,
        "total": 310
    },
    {
        "name": "thwackey",
        "types": [
            "grass"
        ],
        "hp": 70,
        "attack": 85,
        "defense": 70,
        "attack+": 55,
        "defense+": 60,
        "speed": 80,
        "total": 420
    },
    {
        "name": "rillaboom",
        "types": [
            "grass"
        ],
        "hp": 100,
        "attack": 125,
        "defense": 90,
        "attack+": 60,
        "defense+": 70,
        "speed": 85,
        "total": 530
    },
    {
        "name": "scorbunny",
        "types": [
            "fire"
        ],
        "hp": 50,
        "attack": 71,
        "defense": 40,
        "attack+": 40,
        "defense+": 40,
        "speed": 69,
        "total": 310
    },
    {
        "name": "raboot",
        "types": [
            "fire"
        ],
        "hp": 65,
        "attack": 86,
        "defense": 60,
        "attack+": 55,
        "defense+": 60,
        "speed": 94,
        "total": 420
    },
    {
        "name": "cinderace",
        "types": [
            "fire"
        ],
        "hp": 80,
        "attack": 116,
        "defense": 75,
        "attack+": 65,
        "defense+": 75,
        "speed": 119,
        "total": 530
    },
    {
        "name": "sobble",
        "types": [
            "water"
        ],
        "hp": 50,
        "attack": 40,
        "defense": 40,
        "attack+": 70,
        "defense+": 40,
        "speed": 70,
        "total": 310
    },
    {
        "name": "drizzile",
        "types": [
            "water"
        ],
        "hp": 65,
        "attack": 60,
        "defense": 55,
        "attack+": 95,
        "defense+": 55,
        "speed": 90,
        "total": 420
    },
    {
        "name": "inteleon",
        "types": [
            "water"
        ],
        "hp": 70,
        "attack": 85,
        "defense": 65,
        "attack+": 125,
        "defense+": 65,
        "speed": 120,
        "total": 530
    },
    {
        "name": "skwovet",
        "types": [
            "normal"
        ],
        "hp": 70,
        "attack": 55,
        "defense": 55,
        "attack+": 35,
        "defense+": 35,
        "speed": 25,
        "total": 275
    },
    {
        "name": "greedent",
        "types": [
            "normal"
        ],
        "hp": 120,
        "attack": 95,
        "defense": 95,
        "attack+": 55,
        "defense+": 75,
        "speed": 20,
        "total": 460
    },
    {
        "name": "rookidee",
        "types": [
            "flying"
        ],
        "hp": 38,
        "attack": 47,
        "defense": 35,
        "attack+": 33,
        "defense+": 35,
        "speed": 57,
        "total": 245
    },
    {
        "name": "corvisquire",
        "types": [
            "flying"
        ],
        "hp": 68,
        "attack": 67,
        "defense": 55,
        "attack+": 43,
        "defense+": 55,
        "speed": 77,
        "total": 365
    },
    {
        "name": "corviknight",
        "types": [
            "flying",
            "steel"
        ],
        "hp": 98,
        "attack": 87,
        "defense": 105,
        "attack+": 53,
        "defense+": 85,
        "speed": 67,
        "total": 495
    },
    {
        "name": "blipbug",
        "types": [
            "bug"
        ],
        "hp": 25,
        "attack": 20,
        "defense": 20,
        "attack+": 25,
        "defense+": 45,
        "speed": 45,
        "total": 180
    },
    {
        "name": "dottler",
        "types": [
            "bug",
            "psychic"
        ],
        "hp": 50,
        "attack": 35,
        "defense": 80,
        "attack+": 50,
        "defense+": 90,
        "speed": 30,
        "total": 335
    },
    {
        "name": "orbeetle",
        "types": [
            "bug",
            "psychic"
        ],
        "hp": 60,
        "attack": 45,
        "defense": 110,
        "attack+": 80,
        "defense+": 120,
        "speed": 90,
        "total": 505
    },
    {
        "name": "nickit",
        "types": [
            "dark"
        ],
        "hp": 40,
        "attack": 28,
        "defense": 28,
        "attack+": 47,
        "defense+": 52,
        "speed": 50,
        "total": 245
    },
    {
        "name": "thievul",
        "types": [
            "dark"
        ],
        "hp": 70,
        "attack": 58,
        "defense": 58,
        "attack+": 87,
        "defense+": 92,
        "speed": 90,
        "total": 455
    },
    {
        "name": "gossifleur",
        "types": [
            "grass"
        ],
        "hp": 40,
        "attack": 40,
        "defense": 60,
        "attack+": 40,
        "defense+": 60,
        "speed": 10,
        "total": 250
    },
    {
        "name": "eldegoss",
        "types": [
            "grass"
        ],
        "hp": 60,
        "attack": 50,
        "defense": 90,
        "attack+": 80,
        "defense+": 120,
        "speed": 60,
        "total": 460
    },
    {
        "name": "wooloo",
        "types": [
            "normal"
        ],
        "hp": 42,
        "attack": 40,
        "defense": 55,
        "attack+": 40,
        "defense+": 45,
        "speed": 48,
        "total": 270
    },
    {
        "name": "dubwool",
        "types": [
            "normal"
        ],
        "hp": 72,
        "attack": 80,
        "defense": 100,
        "attack+": 60,
        "defense+": 90,
        "speed": 88,
        "total": 490
    },
    {
        "name": "chewtle",
        "types": [
            "water"
        ],
        "hp": 50,
        "attack": 64,
        "defense": 50,
        "attack+": 38,
        "defense+": 38,
        "speed": 44,
        "total": 284
    },
    {
        "name": "drednaw",
        "types": [
            "water",
            "rock"
        ],
        "hp": 90,
        "attack": 115,
        "defense": 90,
        "attack+": 48,
        "defense+": 68,
        "speed": 74,
        "total": 485
    },
    {
        "name": "yamper",
        "types": [
            "electric"
        ],
        "hp": 59,
        "attack": 45,
        "defense": 50,
        "attack+": 40,
        "defense+": 50,
        "speed": 26,
        "total": 270
    },
    {
        "name": "boltund",
        "types": [
            "electric"
        ],
        "hp": 69,
        "attack": 90,
        "defense": 60,
        "attack+": 90,
        "defense+": 60,
        "speed": 121,
        "total": 490
    },
    {
        "name": "rolycoly",
        "types": [
            "rock"
        ],
        "hp": 30,
        "attack": 40,
        "defense": 50,
        "attack+": 40,
        "defense+": 50,
        "speed": 30,
        "total": 240
    },
    {
        "name": "carkol",
        "types": [
            "rock",
            "fire"
        ],
        "hp": 80,
        "attack": 60,
        "defense": 90,
        "attack+": 60,
        "defense+": 70,
        "speed": 50,
        "total": 410
    },
    {
        "name": "coalossal",
        "types": [
            "rock",
            "fire"
        ],
        "hp": 110,
        "attack": 80,
        "defense": 120,
        "attack+": 80,
        "defense+": 90,
        "speed": 30,
        "total": 510
    },
    {
        "name": "applin",
        "types": [
            "grass",
            "dragon"
        ],
        "hp": 40,
        "attack": 40,
        "defense": 80,
        "attack+": 40,
        "defense+": 40,
        "speed": 20,
        "total": 260
    },
    {
        "name": "flapple",
        "types": [
            "grass",
            "dragon"
        ],
        "hp": 70,
        "attack": 110,
        "defense": 80,
        "attack+": 95,
        "defense+": 60,
        "speed": 70,
        "total": 485
    },
    {
        "name": "appletun",
        "types": [
            "grass",
            "dragon"
        ],
        "hp": 110,
        "attack": 85,
        "defense": 80,
        "attack+": 100,
        "defense+": 80,
        "speed": 30,
        "total": 485
    },
    {
        "name": "silicobra",
        "types": [
            "ground"
        ],
        "hp": 52,
        "attack": 57,
        "defense": 75,
        "attack+": 35,
        "defense+": 50,
        "speed": 46,
        "total": 315
    },
    {
        "name": "sandaconda",
        "types": [
            "ground"
        ],
        "hp": 72,
        "attack": 107,
        "defense": 125,
        "attack+": 65,
        "defense+": 70,
        "speed": 71,
        "total": 510
    },
    {
        "name": "cramorant",
        "types": [
            "flying",
            "water"
        ],
        "hp": 70,
        "attack": 85,
        "defense": 55,
        "attack+": 85,
        "defense+": 95,
        "speed": 85,
        "total": 475
    },
    {
        "name": "arrokuda",
        "types": [
            "water"
        ],
        "hp": 41,
        "attack": 63,
        "defense": 40,
        "attack+": 40,
        "defense+": 30,
        "speed": 66,
        "total": 280
    },
    {
        "name": "barraskewda",
        "types": [
            "water"
        ],
        "hp": 61,
        "attack": 123,
        "defense": 60,
        "attack+": 60,
        "defense+": 50,
        "speed": 136,
        "total": 490
    },
    {
        "name": "toxel",
        "types": [
            "electric",
            "poison"
        ],
        "hp": 40,
        "attack": 38,
        "defense": 35,
        "attack+": 54,
        "defense+": 35,
        "speed": 40,
        "total": 242
    },
    {
        "name": "toxtricity",
        "types": [
            "electric",
            "poison"
        ],
        "hp": 75,
        "attack": 98,
        "defense": 70,
        "attack+": 114,
        "defense+": 70,
        "speed": 75,
        "total": 502
    },
    {
        "name": "sizzlipede",
        "types": [
            "fire",
            "bug"
        ],
        "hp": 50,
        "attack": 65,
        "defense": 45,
        "attack+": 50,
        "defense+": 50,
        "speed": 45,
        "total": 305
    },
    {
        "name": "centiskorch",
        "types": [
            "fire",
            "bug"
        ],
        "hp": 100,
        "attack": 115,
        "defense": 65,
        "attack+": 90,
        "defense+": 90,
        "speed": 65,
        "total": 525
    },
    {
        "name": "clobbopus",
        "types": [
            "fighting"
        ],
        "hp": 50,
        "attack": 68,
        "defense": 60,
        "attack+": 50,
        "defense+": 50,
        "speed": 32,
        "total": 310
    },
    {
        "name": "grapploct",
        "types": [
            "fighting"
        ],
        "hp": 80,
        "attack": 118,
        "defense": 90,
        "attack+": 70,
        "defense+": 80,
        "speed": 42,
        "total": 480
    },
    {
        "name": "sinistea",
        "types": [
            "ghost"
        ],
        "hp": 40,
        "attack": 45,
        "defense": 45,
        "attack+": 74,
        "defense+": 54,
        "speed": 50,
        "total": 308
    },
    {
        "name": "polteageist",
        "types": [
            "ghost"
        ],
        "hp": 60,
        "attack": 65,
        "defense": 65,
        "attack+": 134,
        "defense+": 114,
        "speed": 70,
        "total": 508
    },
    {
        "name": "hatenna",
        "types": [
            "psychic"
        ],
        "hp": 42,
        "attack": 30,
        "defense": 45,
        "attack+": 56,
        "defense+": 53,
        "speed": 39,
        "total": 265
    },
    {
        "name": "hattrem",
        "types": [
            "psychic"
        ],
        "hp": 57,
        "attack": 40,
        "defense": 65,
        "attack+": 86,
        "defense+": 73,
        "speed": 49,
        "total": 370
    },
    {
        "name": "hatterene",
        "types": [
            "psychic",
            "fairy"
        ],
        "hp": 57,
        "attack": 90,
        "defense": 95,
        "attack+": 136,
        "defense+": 103,
        "speed": 29,
        "total": 510
    },
    {
        "name": "impidimp",
        "types": [
            "dark",
            "fairy"
        ],
        "hp": 45,
        "attack": 45,
        "defense": 30,
        "attack+": 55,
        "defense+": 40,
        "speed": 50,
        "total": 265
    },
    {
        "name": "morgrem",
        "types": [
            "dark",
            "fairy"
        ],
        "hp": 65,
        "attack": 60,
        "defense": 45,
        "attack+": 75,
        "defense+": 55,
        "speed": 70,
        "total": 370
    },
    {
        "name": "grimmsnarl",
        "types": [
            "dark",
            "fairy"
        ],
        "hp": 95,
        "attack": 120,
        "defense": 65,
        "attack+": 95,
        "defense+": 75,
        "speed": 60,
        "total": 510
    },
    {
        "name": "obstagoon",
        "types": [
            "dark",
            "normal"
        ],
        "hp": 93,
        "attack": 90,
        "defense": 101,
        "attack+": 60,
        "defense+": 81,
        "speed": 95,
        "total": 520
    },
    {
        "name": "perrserker",
        "types": [
            "steel"
        ],
        "hp": 70,
        "attack": 110,
        "defense": 100,
        "attack+": 50,
        "defense+": 60,
        "speed": 50,
        "total": 440
    },
    {
        "name": "cursola",
        "types": [
            "ghost"
        ],
        "hp": 60,
        "attack": 95,
        "defense": 50,
        "attack+": 145,
        "defense+": 130,
        "speed": 30,
        "total": 510
    },
    {
        "name": "sirfetch'd",
        "types": [
            "fighting"
        ],
        "hp": 62,
        "attack": 135,
        "defense": 95,
        "attack+": 68,
        "defense+": 82,
        "speed": 65,
        "total": 507
    },
    {
        "name": "runerigus",
        "types": [
            "ground",
            "ghost"
        ],
        "hp": 58,
        "attack": 95,
        "defense": 145,
        "attack+": 50,
        "defense+": 105,
        "speed": 30,
        "total": 483
    },
    {
        "name": "milcery",
        "types": [
            "fairy"
        ],
        "hp": 45,
        "attack": 40,
        "defense": 40,
        "attack+": 50,
        "defense+": 61,
        "speed": 34,
        "total": 270
    },
    {
        "name": "alcremie",
        "types": [
            "fairy"
        ],
        "hp": 65,
        "attack": 60,
        "defense": 75,
        "attack+": 110,
        "defense+": 121,
        "speed": 64,
        "total": 495
    },
    {
        "name": "falinks",
        "types": [
            "fighting"
        ],
        "hp": 65,
        "attack": 100,
        "defense": 100,
        "attack+": 70,
        "defense+": 60,
        "speed": 75,
        "total": 470
    },
    {
        "name": "pincurchin",
        "types": [
            "electric"
        ],
        "hp": 48,
        "attack": 101,
        "defense": 95,
        "attack+": 91,
        "defense+": 85,
        "speed": 15,
        "total": 435
    },
    {
        "name": "snom",
        "types": [
            "ice",
            "bug"
        ],
        "hp": 30,
        "attack": 25,
        "defense": 35,
        "attack+": 45,
        "defense+": 30,
        "speed": 20,
        "total": 185
    },
    {
        "name": "frosmoth",
        "types": [
            "ice",
            "bug"
        ],
        "hp": 70,
        "attack": 65,
        "defense": 60,
        "attack+": 125,
        "defense+": 90,
        "speed": 65,
        "total": 475
    },
    {
        "name": "stonjourner",
        "types": [
            "rock"
        ],
        "hp": 100,
        "attack": 125,
        "defense": 135,
        "attack+": 20,
        "defense+": 20,
        "speed": 70,
        "total": 470
    },
    {
        "name": "eiscue",
        "types": [
            "ice"
        ],
        "hp": 75,
        "attack": 80,
        "defense": 110,
        "attack+": 65,
        "defense+": 90,
        "speed": 50,
        "total": 470
    },
    {
        "name": "indeedee",
        "types": [
            "psychic",
            "normal"
        ],
        "hp": 60,
        "attack": 65,
        "defense": 55,
        "attack+": 105,
        "defense+": 95,
        "speed": 95,
        "total": 475
    },
    {
        "name": "morpeko",
        "types": [
            "electric",
            "dark"
        ],
        "hp": 58,
        "attack": 95,
        "defense": 58,
        "attack+": 70,
        "defense+": 58,
        "speed": 97,
        "total": 436
    },
    {
        "name": "cufant",
        "types": [
            "steel"
        ],
        "hp": 72,
        "attack": 80,
        "defense": 49,
        "attack+": 40,
        "defense+": 49,
        "speed": 40,
        "total": 330
    },
    {
        "name": "copperajah",
        "types": [
            "steel"
        ],
        "hp": 122,
        "attack": 130,
        "defense": 69,
        "attack+": 80,
        "defense+": 69,
        "speed": 30,
        "total": 500
    },
    {
        "name": "dracozolt",
        "types": [
            "electric",
            "dragon"
        ],
        "hp": 90,
        "attack": 100,
        "defense": 90,
        "attack+": 80,
        "defense+": 70,
        "speed": 75,
        "total": 505
    },
    {
        "name": "arctozolt",
        "types": [
            "electric",
            "ice"
        ],
        "hp": 90,
        "attack": 100,
        "defense": 90,
        "attack+": 90,
        "defense+": 80,
        "speed": 55,
        "total": 505
    },
    {
        "name": "dracovish",
        "types": [
            "water",
            "dragon"
        ],
        "hp": 90,
        "attack": 90,
        "defense": 100,
        "attack+": 70,
        "defense+": 80,
        "speed": 75,
        "total": 505
    },
    {
        "name": "arctovish",
        "types": [
            "water",
            "ice"
        ],
        "hp": 90,
        "attack": 90,
        "defense": 100,
        "attack+": 80,
        "defense+": 90,
        "speed": 55,
        "total": 505
    },
    {
        "name": "duraludon",
        "types": [
            "steel",
            "dragon"
        ],
        "hp": 70,
        "attack": 95,
        "defense": 115,
        "attack+": 120,
        "defense+": 50,
        "speed": 85,
        "total": 535
    },
    {
        "name": "dreepy",
        "types": [
            "dragon",
            "ghost"
        ],
        "hp": 28,
        "attack": 60,
        "defense": 30,
        "attack+": 40,
        "defense+": 30,
        "speed": 82,
        "total": 270
    },
    {
        "name": "drakloak",
        "types": [
            "dragon",
            "ghost"
        ],
        "hp": 68,
        "attack": 80,
        "defense": 50,
        "attack+": 60,
        "defense+": 50,
        "speed": 102,
        "total": 410
    },
    {
        "name": "dragapult",
        "types": [
            "dragon",
            "ghost"
        ],
        "hp": 88,
        "attack": 120,
        "defense": 75,
        "attack+": 100,
        "defense+": 75,
        "speed": 142,
        "total": 600
    },
    {
        "name": "zacian",
        "types": [
            "fairy",
            "steel"
        ],
        "hp": 92,
        "attack": 170,
        "defense": 115,
        "attack+": 80,
        "defense+": 115,
        "speed": 148,
        "total": 720
    },
    {
        "name": "zamazenta",
        "types": [
            "fighting",
            "steel"
        ],
        "hp": 92,
        "attack": 130,
        "defense": 145,
        "attack+": 80,
        "defense+": 145,
        "speed": 128,
        "total": 720
    },
    {
        "name": "eternatus",
        "types": [
            "poison",
            "dragon"
        ],
        "hp": 140,
        "attack": 85,
        "defense": 95,
        "attack+": 145,
        "defense+": 95,
        "speed": 130,
        "total": 690
    },
    {
        "name": "kubfu",
        "types": [
            "fighting"
        ],
        "hp": 60,
        "attack": 90,
        "defense": 60,
        "attack+": 53,
        "defense+": 50,
        "speed": 72,
        "total": 385
    },
    {
        "name": "urshifu",
        "types": [
            "fighting",
            "dark"
        ],
        "hp": 100,
        "attack": 130,
        "defense": 100,
        "attack+": 63,
        "defense+": 60,
        "speed": 97,
        "total": 550
    },
    {
        "name": "zarude",
        "types": [
            "dark",
            "grass"
        ],
        "hp": 105,
        "attack": 120,
        "defense": 105,
        "attack+": 70,
        "defense+": 95,
        "speed": 105,
        "total": 600
    },
    {
        "name": "regieleki",
        "types": [
            "electric"
        ],
        "hp": 80,
        "attack": 100,
        "defense": 50,
        "attack+": 100,
        "defense+": 50,
        "speed": 200,
        "total": 580
    },
    {
        "name": "regidrago",
        "types": [
            "dragon"
        ],
        "hp": 200,
        "attack": 100,
        "defense": 50,
        "attack+": 100,
        "defense+": 50,
        "speed": 80,
        "total": 580
    },
    {
        "name": "glastrier",
        "types": [
            "ice"
        ],
        "hp": 100,
        "attack": 145,
        "defense": 130,
        "attack+": 65,
        "defense+": 110,
        "speed": 30,
        "total": 580
    },
    {
        "name": "spectrier",
        "types": [
            "ghost"
        ],
        "hp": 100,
        "attack": 65,
        "defense": 60,
        "attack+": 145,
        "defense+": 80,
        "speed": 130,
        "total": 580
    },
    {
        "name": "calyrex",
        "types": [
            "psychic",
            "grass"
        ],
        "hp": 100,
        "attack": 80,
        "defense": 80,
        "attack+": 80,
        "defense+": 80,
        "speed": 80,
        "total": 500
    }
]

def clear_screen():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def show_plays_card(plays_card):
    plays_card = [
        f" ╭─────────────────────╮",
        f" │ {plays_card['name'].upper().center(19)} │",
        f" ├──────────────┬──────┤",
        f" │ [1] HP       │ {plays_card['hp']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [2] ATTACK   │ {plays_card['attack']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [3] DEFENSE  │ {plays_card['defense']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [4] ATTACK+  │ {plays_card['attack+']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [5] DEFENSE+ │ {plays_card['defense+']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [6] SPEED    │ {plays_card['speed']:4.0f} │",
        f" ╰──────────────┴──────╯"
    ]
    oppos_card = [
        f"╭─────────────────────╮",
        f"│ ░░░░░░░░░░░░░░░░░░░ │",
        f"├──────────────┬──────┤",
        f"│ [1] HP       │ ░░░░ │",
        f"├──────────────┼──────┤",
        f"│ [2] ATTACK   │ ░░░░ │",
        f"├──────────────┼──────┤",
        f"│ [3] DEFENSE  │ ░░░░ │",
        f"├──────────────┼──────┤",
        f"│ [4] ATTACK+  │ ░░░░ │",
        f"├──────────────┼──────┤",
        f"│ [5] DEFENSE+ │ ░░░░ │",
        f"├──────────────┼──────┤",
        f"│ [6] SPEED    │ ░░░░ │",
        f"╰──────────────┴──────╯"
    ]
    print("\n".join([
        plays_card[i] + "    "  + oppos_card[i] for i in range(len(plays_card))
    ]))

def show_oppos_card(plays_card, oppos_card, option):
    plays_card = [
        f" ╭─────────────────────╮",
        f" │ {plays_card['name'].upper().center(19)} │",
        f" ├──────────────┬──────┤",
        f" │ [1] HP       │ {plays_card['hp']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [2] ATTACK   │ {plays_card['attack']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [3] DEFENSE  │ {plays_card['defense']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [4] ATTACK+  │ {plays_card['attack+']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [5] DEFENSE+ │ {plays_card['defense+']:4.0f} │",
        f" ├──────────────┼──────┤",
        f" │ [6] SPEED    │ {plays_card['speed']:4.0f} │",
        f" ╰──────────────┴──────╯"
    ]
    oppos_card = [
        f"╭─────────────────────╮",
        f"│ {oppos_card['name'].upper().center(19)} │",
        f"├──────────────┬──────┤",
        f"│ [1] HP       │ {oppos_card['hp']:4.0f} │",
        f"├──────────────┼──────┤",
        f"│ [2] ATTACK   │ {oppos_card['attack']:4.0f} │",
        f"├──────────────┼──────┤",
        f"│ [3] DEFENSE  │ {oppos_card['defense']:4.0f} │",
        f"├──────────────┼──────┤",
        f"│ [4] ATTACK+  │ {oppos_card['attack+']:4.0f} │",
        f"├──────────────┼──────┤",
        f"│ [5] DEFENSE+ │ {oppos_card['defense+']:4.0f} │",
        f"├──────────────┼──────┤",
        f"│ [6] SPEED    │ {oppos_card['speed']:4.0f} │",
        f"╰──────────────┴──────╯"
    ]
    print("\n".join([
        plays_card[i] + (" ←→ " if i == (option * 2) + 1 else "    ")  + oppos_card[i] for i in range(len(plays_card))
    ]))

def differ(plays_card, oppos_card, option):
    if option == 1:
        return (plays_card["hp"] - oppos_card["hp"])
    elif option == 2:
        return (plays_card["attack"] - oppos_card["attack"])
    elif option == 3:
        return (plays_card["defense"] - oppos_card["defense"])
    elif option == 4:
        return (plays_card["attack+"] - oppos_card["attack+"])
    elif option == 5:
        return (plays_card["defense+"] - oppos_card["defense+"])
    else:
        return (plays_card["speed"] - oppos_card["speed"])

def oppos_choice(oppos_card):
    options = { 
        1 : oppos_card["hp"], 
        2 : oppos_card["attack"], 
        3 : oppos_card["defense"], 
        4 : oppos_card["attack+"], 
        5 : oppos_card["defense+"], 
        6 : oppos_card["speed"]
    }

    return choice([option for option in options if options[option] == max(options.values())])

def scorecard(rounds, points):
    return "\n".join([
        f" ╭──────────────────╮",
        f" │ {(str(rounds) + ' ROUNDS').center(16)} │",
        f" ├──────────┬───────┤",
        f" │ PLAYER   │ {points['player']:5.0f} │",
        f" ├──────────┼───────┤",
        f" │ OPPONENT │ {points['opponent']:5.0f} │",
        f" ╰──────────┴───────╯"
    ])

if __name__ == "__main__":
    cards = [pokemon for pokemon in pokemons]

    pickedcards = sample(cards, k=30)
    plays_cards = pickedcards[:15]
    oppos_cards = pickedcards[15:]

    points = {
        "player"   : 0,
        "opponent" : 0
    }

    round_number = 1

    while plays_cards and oppos_cards:
        plays_card = choice(plays_cards)
        oppos_card = choice(oppos_cards)

        oppos_cards.remove(oppos_card)
        plays_cards.remove(plays_card)

        clear_screen()
        show_plays_card(plays_card)

        option = None
        if round_number % 2:
            option = input("player   > ").strip()
            if option.isdecimal():
                option = int(option)
            else:
                break
        else:
            option = oppos_choice(oppos_card)
            input(f"opponent > {option}")

        differs = differ(plays_card, oppos_card, option)

        if differs > 0:
            points["player"] += differs
            clear_screen()
            show_oppos_card(plays_card, oppos_card, option)
            input(f"> You won by {differs} points.")
        elif differs < 0:
            differs = abs(differs)
            points["opponent"] += differs
            clear_screen()
            show_oppos_card(plays_card, oppos_card, option)
            input(f"> You lost by {differs} points.")
        else:
            clear_screen()
            show_oppos_card(plays_card, oppos_card, option)
            input(f"> It's a tie.")

        round_number += 1

    clear_screen()
    print(scorecard(round_number - 1, points))

""" sample ----------------------------------------
 ╭─────────────────────╮    ╭─────────────────────╮
 │       SWELLOW       │    │ ░░░░░░░░░░░░░░░░░░░ │
 ├──────────────┬──────┤    ├──────────────┬──────┤
 │ [1] HP       │   60 │    │ [1] HP       │ ░░░░ │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [2] ATTACK   │   85 │    │ [2] ATTACK   │ ░░░░ │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [3] DEFENSE  │   60 │    │ [3] DEFENSE  │ ░░░░ │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [4] ATTACK+  │   75 │    │ [4] ATTACK+  │ ░░░░ │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [5] DEFENSE+ │   50 │    │ [5] DEFENSE+ │ ░░░░ │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [6] SPEED    │  125 │    │ [6] SPEED    │ ░░░░ │
 ╰──────────────┴──────╯    ╰──────────────┴──────╯
player   > 6

 ╭─────────────────────╮    ╭─────────────────────╮
 │       SWELLOW       │    │       DONPHAN       │
 ├──────────────┬──────┤    ├──────────────┬──────┤
 │ [1] HP       │   60 │    │ [1] HP       │   90 │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [2] ATTACK   │   85 │    │ [2] ATTACK   │  120 │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [3] DEFENSE  │   60 │    │ [3] DEFENSE  │  120 │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [4] ATTACK+  │   75 │    │ [4] ATTACK+  │   60 │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [5] DEFENSE+ │   50 │    │ [5] DEFENSE+ │   60 │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [6] SPEED    │  125 │ ←→ │ [6] SPEED    │   50 │
 ╰──────────────┴──────╯    ╰──────────────┴──────╯
> You won by 75 points.

 ╭─────────────────────╮    ╭─────────────────────╮
 │      BOUNSWEET      │    │ ░░░░░░░░░░░░░░░░░░░ │
 ├──────────────┬──────┤    ├──────────────┬──────┤
 │ [1] HP       │   42 │    │ [1] HP       │ ░░░░ │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [2] ATTACK   │   30 │    │ [2] ATTACK   │ ░░░░ │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [3] DEFENSE  │   38 │    │ [3] DEFENSE  │ ░░░░ │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [4] ATTACK+  │   30 │    │ [4] ATTACK+  │ ░░░░ │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [5] DEFENSE+ │   38 │    │ [5] DEFENSE+ │ ░░░░ │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [6] SPEED    │   32 │    │ [6] SPEED    │ ░░░░ │
 ╰──────────────┴──────╯    ╰──────────────┴──────╯
opponent > 4

 ╭─────────────────────╮    ╭─────────────────────╮
 │      BOUNSWEET      │    │       VIKAVOLT      │
 ├──────────────┬──────┤    ├──────────────┬──────┤
 │ [1] HP       │   42 │    │ [1] HP       │   77 │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [2] ATTACK   │   30 │    │ [2] ATTACK   │   70 │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [3] DEFENSE  │   38 │    │ [3] DEFENSE  │   90 │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [4] ATTACK+  │   30 │ ←→ │ [4] ATTACK+  │  145 │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [5] DEFENSE+ │   38 │    │ [5] DEFENSE+ │   75 │
 ├──────────────┼──────┤    ├──────────────┼──────┤
 │ [6] SPEED    │   32 │    │ [6] SPEED    │   43 │
 ╰──────────────┴──────╯    ╰──────────────┴──────╯
> You lost by 115 points.

 ╭──────────────────╮
 │     2 ROUNDS     │
 ├──────────┬───────┤
 │ PLAYER   │    75 │
 ├──────────┼───────┤
 │ OPPONENT │   115 │
 ╰──────────┴───────╯
"""