teams = ["Arsenal", "Barca", "Chelsea", "Man UTD", "Liverpool", "Man City"]

for teamA in teams:
    for teamB in teams:
        if teamA != teamB:
            print(f"{teamA} Vs {teamB}")
