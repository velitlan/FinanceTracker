import matplotlib.pyplot as plt

def plot_summary(summary_df):
    plt.figure(figsize=(10, 6))
    
    summary_df.plot(kind='bar', stacked=True, alpha=0.85, edgecolor='black')
    
    plt.title("📅 Monatliche Einnahmen & Ausgaben", fontsize=14, fontweight="bold")
    plt.xlabel("Monat", fontsize=12)
    plt.ylabel("Betrag (€)", fontsize=12)
    
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Kategorien", fontsize=10)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    
    plt.tight_layout()
    plt.show()