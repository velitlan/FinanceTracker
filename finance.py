import pandas as pd

def load_transactions(filepath):
    return pd.read_csv(filepath)

def analyze_transactions(df):
    df['Betrag'] = df['Betrag'].astype(float)
    
    monthly_summary = df.groupby(['Monat', 'Kategorie'])['Betrag'].sum().unstack().fillna(0)
    
    income = df[df['Kategorie'] == 'Einnahme']['Betrag'].sum()
    expenses = df[df['Kategorie'] == 'Ausgabe']['Betrag'].sum()
    
    net = income - expenses
    advice = ""
    
    if net > 0:
        advice = f"Du hast einen Überschuss von {net:.2f}€. Gut gemacht!"
    else:
        advice = f"Du gibst {abs(net):.2f}€ mehr aus, als du einnimmst. Zeit zum Sparen!"

    return monthly_summary, advice