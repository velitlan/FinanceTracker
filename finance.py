import pandas as pd

def load_transactions(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)

def analyze_transactions(df: pd.DataFrame) -> tuple[pd.DataFrame, str]:
    df['Betrag'] = pd.to_numeric(df['Betrag'], errors='coerce').fillna(0)
    
    monthly_summary = df.pivot_table(
        index='Monat',
        columns='Kategorie',
        values='Betrag',
        aggfunc='sum',
        fill_value=0
    )

    totals = df.groupby('Kategorie')['Betrag'].sum()
    income = totals.get('Einnahme', 0)
    expenses = totals.get('Ausgabe', 0)

    net = income - expenses
    advice = (
        f"Du hast einen Überschuss von {net:.2f}€. Gut gemacht!"
        if net > 0
        else f"Du gibst {abs(net):.2f}€ mehr aus, als du einnimmst. Zeit zum Sparen!"
    )

    return monthly_summary, advice