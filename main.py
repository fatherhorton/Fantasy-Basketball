import pandas as pd
import csv

file_path = r'C:\Users\New\Downloads\2022-2023 NBA Player Stats - Regular (1).csv'

df = pd.read_csv(file_path, encoding='latin-1', delimiter=';')

fantasy_rules = [
    ('Point', 1),
    ('3PM', 1),
    ('FGA', -1),
    ('FGM', 2),
    ('FTA', -1),
    ('FTM', 1),
    ('REB', 1),
    ('AST', 2),
    ('STL', 4),
    ('BLK', 4),
    ('TOV', -2),
]

fantasy_rules_dict = dict(fantasy_rules)

def calculate_total_fantasy_value(player_stats):
    total_value = 0
    for action, value in player_stats.items():
        if action in fantasy_rules_dict:
            total_value += value + fantasy_rules_dict[action]
    return total_value
pd.set_option('display.max_rows', None)
df['TotalFantasyValue'] = df.apply(calculate_total_fantasy_value, axis=1)


df_sorted = df.sort_values(by='TotalFantasyValue', ascending=False)


df_sorted.reset_index(drop=True, inplace=True)

print(df_sorted[['Player', 'TotalFantasyValue', 'G']])




