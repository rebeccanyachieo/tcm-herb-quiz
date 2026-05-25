import random

cold_release_exterior_herbs = [
    {
        "name": "Bo He",
        "pinyin": "Bò Hé",
        "english": "Menthae Herba",
        "keywords": [
            "Releases exterior wind heat",
            "Cools throat, eyes, head",
            "Cools and smooths liver",
            "Vents rashes"
        ]
    },

    {
        "name": "Niu Bang Zi",
        "pinyin": "Níu Bàng Zǐ",
        "english": "Arctii Fructus",
        "keywords": [
            "Clears wind heat especially throat",
            "Moistens intestines"
        ]
    },

    {
        "name": "Chan Tui",
        "pinyin": "Chán Tuì",
        "english": "Cicadae Periostracum",
        "keywords": [
            "Clears wind heat especially eyes and throat",
            "Stops spasm",
            "Vents rashes"
        ]
    },

    {
        "name": "Sang Ye",
        "pinyin": "Sāng Yè",
        "english": "Mori Folium",
        "keywords": [
            "Clears wind heat",
            "Benefits eyes and cough",
            "Clears heat from liver",
            "Cools blood and stops bleeding"
        ]
    },

    {
        "name": "Ju Hua",
        "pinyin": "Jú Huā",
        "english": "Chrysanthemi Flos",
        "keywords": [
            "Clears wind heat from eyes",
            "Cools and smooths liver"
        ]
    },

    {
        "name": "Man Jing Zi",
        "pinyin": "Màn Jīng Zǐ",
        "english": "Viticis Fructus",
        "keywords": [
            "Disperses wind",
            "Clears heat",
            "Benefits liver and eyes",
            "Helps headache"
        ]
    },

    {
        "name": "Dan Dou Chi",
        "pinyin": "Dàn Dòu Chǐ",
        "english": "Semen Sojae Praeparatae",
        "keywords": [
            "Weakly releases wind heat",
            "Helps restlessness and irritability",
            "Stops lactation by cooling channels"
        ]
    },

    {
        "name": "Fu Ping",
        "pinyin": "Fú Píng",
        "english": "Spirodelae Herba",
        "keywords": [
            "Strongly disperses wind heat",
            "Vents rashes",
            "Expels wind damp"
        ]
    },

    {
        "name": "Mu Zei",
        "pinyin": "Mù Zéi",
        "english": "Equiseti Hiemalis Herba",
        "keywords": [
            "Clears heat from eyes",
            "Stops bleeding"
        ]
    },

    {
        "name": "Ge Gen",
        "pinyin": "Gé Gēn",
        "english": "Puerariae Radix",
        "keywords": [
            "Releases muscles",
            "Helps stiff neck",
            "Stops diarrhea",
            "Nourishes fluids",
            "Vents measles"
        ]
    },

    {
        "name": "Chai Hu",
        "pinyin": "Chái Hú",
        "english": "Bupleuri Radix",
        "keywords": [
            "Spreads liver qi",
            "Clears Shao Yang heat",
            "Raises qi"
        ]
    },

    {
        "name": "Sheng Ma",
        "pinyin": "Shēng Má",
        "english": "Cimicifugae Rhizoma",
        "keywords": [
            "Raises qi",
            "Vents rashes"
        ]
    }
]

score = 0

print("Cold Release the Exterior Herb Quiz")

for question_number in range(5):

    herb = random.choice(cold_release_exterior_herbs)

    print(f"\nQuestion {question_number + 1}")
    print(f"What are the keywords for {herb['name']}?")

    answer = input("> ").lower()

    correct = " ".join(herb["keywords"]).lower()

    if answer in correct:
        print("Correct!")
        score += 1
    else:
        print("\nPossible answers:")
        for keyword in herb["keywords"]:
            print("-", keyword)

print(f"\nFinal score: {score}/5")
