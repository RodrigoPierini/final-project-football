# Import necessary libraries
import json

# Define the arrays
nations = ['ALG', 'BFA', 'FRA', 'SEN', 'CIV', 'BRA', 'CGO', 'SUI', 'TUN',
           'ENG', 'MLI', 'ESP', 'COL', 'SRB', 'BEL', 'NGA', 'GNB', 'POR',
           'MAR', 'CRO', 'JAM', 'ARG', 'SCO', 'ITA', 'DEN', 'UKR', 'CZE',
           'GHA', 'NED', 'GER', 'BIH', 'FIN', 'USA', 'BUL', 'CPV', 'GAB',
           'POL', 'CMR', 'JPN', 'PHI', 'AUT', 'GAM', 'GRE', 'WAL', 'LBR',
           'IRN', 'COD', 'HON', 'BEN', 'PAR', 'IRL', 'ZAM', 'NOR', 'ALB',
           'KVX', 'AUS', 'URU', 'SWE', 'VEN', 'HUN', 'KOR', 'ISR', 'TUR',
           'MTN', 'SLE', 'MNE', 'COM', 'TOG', 'ARM', 'ROU', 'GLP', 'CAN',
           'GUI', 'EGY', 'ZIM', 'LUX', 'CHI', 'RUS', 'MKD', 'GEO', 'MEX',
           'NIR', 'NZL', 'MSR', 'DOM', 'UZB', 'MTQ', 'SVN', 'LVA', 'ANG',
           'SVK', 'RSA', 'SUR', 'ECU']

squads = ['Ajaccio', 'Almería', 'Angers', 'Arsenal', 'Aston Villa',
          'Atalanta', 'Athletic Club', 'Atlético Madrid', 'Augsburg',
          'Auxerre', 'Barcelona', 'Bayern Munich', 'Betis', 'Bochum',
          'Bologna', 'Bournemouth', 'Brentford', 'Brest', 'Brighton',
          'Celta Vigo', 'Chelsea', 'Clermont Foot', 'Cremonese',
          'Crystal Palace', 'Cádiz', 'Dortmund', 'Eint Frankfurt', 'Elche',
          'Empoli', 'Espanyol', 'Everton', 'Fiorentina', 'Freiburg',
          'Fulham', 'Getafe', 'Girona', 'Hellas Verona', 'Hertha BSC',
          'Hoffenheim', 'Inter', 'Juventus', 'Köln', 'Lazio', 'Lecce',
          'Leeds United', 'Leicester City', 'Lens', 'Leverkusen', 'Lille',
          'Liverpool', 'Lorient', 'Lyon', "M'Gladbach", 'Mainz 05',
          'Mallorca', 'Manchester City', 'Manchester Utd', 'Marseille',
          'Milan', 'Monaco', 'Montpellier', 'Monza', 'Nantes', 'Napoli',
          'Newcastle Utd', 'Nice', "Nott'ham Forest", 'Osasuna', 'Paris S-G',
          'RB Leipzig', 'Rayo Vallecano', 'Real Madrid', 'Real Sociedad',
          'Reims', 'Rennes', 'Roma', 'Salernitana', 'Sampdoria', 'Sassuolo',
          'Schalke 04', 'Sevilla', 'Southampton', 'Spezia', 'Strasbourg',
          'Stuttgart', 'Torino', 'Tottenham', 'Toulouse', 'Troyes',
          'Udinese', 'Union Berlin', 'Valencia', 'Valladolid', 'Villarreal',
          'Werder Bremen', 'West Ham', 'Wolfsburg', 'Wolves']

comps = ['Ligue 1', 'La Liga', 'Premier League', 'Serie A', 'Bundesliga']

# Create the mappings
nation_mapping = {nation: idx for idx, nation in enumerate(nations)}
squad_mapping = {squad: idx for idx, squad in enumerate(squads)}
comp_mapping = {comp: idx for idx, comp in enumerate(comps)}

# Combine all mappings into one dictionary
combined_mapping = {
    "Nation": nation_mapping,
    "Squad": squad_mapping,
    "Comp": comp_mapping
}

# Save the combined mapping to a JSON file
with open('categorical_mapping.json', 'w') as json_file:
    json.dump(combined_mapping, json_file, indent=4)

print("Mappings have been saved to mapping.json")