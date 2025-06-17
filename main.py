import os
import pandas as pd
from finance import analyze_transactions, load_transactions
from visualization import plot_summary

DATA_FILE = "data.csv"

def main():
    print(f"Arbeitsverzeichnis: {os.getcwd()}")
    print("Willkommen zur Finanzanalyse-App!")

    transactions = load_transactions(DATA_FILE)
    summary, savings_advice = analyze_transactions(transactions)

    print("\n--- Finanzübersicht ---")
    print(summary)

    print("\n--- Spar-Tipp ---")
    print(savings_advice)

    plot_summary(summary)

if __name__ == "__main__":
    main()