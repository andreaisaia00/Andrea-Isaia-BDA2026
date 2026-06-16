

def clean_spines(ax):
    """Hide the top and right border lines of the plot, for a cleaner look."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)