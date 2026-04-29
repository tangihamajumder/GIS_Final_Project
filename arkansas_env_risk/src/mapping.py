"""
mapping.py
----------
Helper functions for generating choropleth maps of Arkansas
census tract indicator variables and risk scores.

Usage:
    from src.mapping import make_map, save_map
"""

import os
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


RISK_CMAP = ListedColormap(["#2c7bb6", "#abd9e9", "#ffffbf", "#fdae61", "#d7191c"])


def make_map(gdf, column: str, title: str,
             cmap="viridis", categorical: bool = False,
             legend: bool = True, figsize: tuple = (10, 8)):
    """
    Generate a choropleth map for a GeoDataFrame column.

    Parameters
    ----------
    gdf : GeoDataFrame
        Spatial data to plot.
    column : str
        Column to visualize.
    title : str
        Map title.
    cmap : str or Colormap
        Matplotlib colormap.
    categorical : bool
        If True, treat column as categorical.
    legend : bool
        If True, include a legend.
    figsize : tuple
        Figure size in inches (width, height).

    Returns
    -------
    fig, ax : matplotlib Figure and Axes
    """
    fig, ax = plt.subplots(figsize=figsize)
    gdf.plot(
        column=column,
        ax=ax,
        legend=legend,
        cmap=cmap,
        categorical=categorical,
        linewidth=0.05,
        edgecolor="white",
        missing_kwds={"color": "lightgrey", "label": "Missing"}
    )
    ax.set_title(title, fontsize=14)
    ax.set_axis_off()
    plt.tight_layout()
    return fig, ax


def save_map(fig, filename: str, output_folder: str = "assets/"):
    """
    Save a matplotlib figure to the assets folder.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to save.
    filename : str
        Output filename (e.g., 'risk_score_map.png').
    output_folder : str
        Destination directory (default: 'assets/').
    """
    os.makedirs(output_folder, exist_ok=True)
    path = os.path.join(output_folder, filename)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"Saved: {path}")
