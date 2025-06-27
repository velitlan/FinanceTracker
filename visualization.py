import matplotlib.pyplot as plt
import pandas as pd

def plot_summary(summary_df: pd.DataFrame) -> None:
    summary_df.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title("Monatliche Einnahmen und Ausgaben")
    plt.xlabel("Monat")
    plt.ylabel("Betrag (€)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend(title="Kategorie")
    plt.show()
