from finance import analyze_transactions, load_transactions
from visualization import plot_summary
import pandas as pd
import os
print("Arbeitsverzeichnis:", os.getcwd())
def main():
    print("Willkommen zur Finanzanalyse-App!")
    
    transactions = load_transactions("data.csv")
    
    summary, savings_advice = analyze_transactions(transactions)
    
    print("\nFinanzübersicht:")
    print(summary)
    
    print("\nSpar-Tipp:")
    print(savings_advice)
    
    plot_summary(summary)

if __name__ == "__main__":
    main()