import matplotlib.pyplot as plt

def plot_summary(summary_df):
    summary_df.plot(kind='bar', stacked=True)
    plt.title("📅 Monatliche Einnahmen & Ausgaben")
    plt.xlabel("Monat")
    plt.ylabel("Betrag (€)")
    plt.tight_layout()
    plt.grid(True)
    plt.show()