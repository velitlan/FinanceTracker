import os
import sys
import pandas as pd
from finance import analyze_transactions, load_transactions
from visualization import plot_summary

DATA_FILE = "data.csv"

def main() -> None:
    print(f"Arbeitsverzeichnis: {os.getcwd()}")
    print("Willkommen zur Finanzanalyse-App!\n")

    try:
        transactions = load_transactions(DATA_FILE)
    except FileNotFoundError:
        print(f"Fehler: Datei '{DATA_FILE}' wurde nicht gefunden.")
        sys.exit(1)
    except pd.errors.ParserError:
        print(f"Fehler: Datei '{DATA_FILE}' konnte nicht als CSV gelesen werden.")
        sys.exit(1)

    summary, savings_advice = analyze_transactions(transactions)

    print("--- Finanzübersicht ---")
    print(summary)

    print("\n--- Spar-Tipp ---")
    print(savings_advice)

    plot_summary(summary)

if __name__ == "__main__":
    main()