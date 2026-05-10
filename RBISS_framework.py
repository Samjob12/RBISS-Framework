import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle



fig, ax = plt.subplots(figsize=(18, 11))
ax.set_xlim(0, 18)
ax.set_ylim(0, 11)
ax.axis("off")


blue = "#1f4e79"
light_blue = "#eaf3fb"
row_bg = "#f7fafc"
border = "#c8d8e8"
dark = "#222222"
gray = "#555555"

orange = "#d95f02"
yellow = "#f2b000"
green = "#009e73"
selected_red = "#c0392b"
table_gray = "#f2f2f2"


ax.text(
    9, 10.55,
    "Rule-Based Indicator Selection Score (RBISS)",
    ha="center", va="center",
    fontsize=27, fontweight="bold", color=blue
)

ax.text(
    9, 10.15,
    "A scale-flexible and normalization-based qualitative screening framework for transparent and reproducible indicator selection",
    ha="center", va="center",
    fontsize=15.5, color=gray
)


rows = [
    ("Relevance", 8.95, ["Weak link", "Moderate link", "Direct GHG link"]),
    ("Policy", 7.70, ["Limited use", "Indirect support", "Direct policy tool"]),
    ("Data", 6.45, ["Limited data", "Partial data", "Complete data"])
]

x_points = [6.0, 9.0, 12.0]
score_colors = [orange, yellow, green]
score_labels = ["Low", "Medium", "High"]
score_values = ["1", "2", "3"]

for criterion, y, descriptors in rows:
    ax.add_patch(
        FancyBboxPatch(
            (0.9, y - 0.48), 16.2, 0.92,
            boxstyle="round,pad=0.02,rounding_size=0.10",
            linewidth=1.1,
            edgecolor=border,
            facecolor=row_bg
        )
    )

    ax.text(
        1.45, y,
        criterion,
        ha="left", va="center",
        fontsize=20,
        fontweight="bold",
        color=blue
    )

    for i, x in enumerate(x_points):
        ax.add_patch(
            Circle(
                (x, y + 0.14),
                0.31,
                facecolor=score_colors[i],
                edgecolor="black",
                linewidth=1.6
            )
        )

        ax.text(
            x, y + 0.14,
            score_values[i],
            ha="center", va="center",
            fontsize=15,
            fontweight="bold",
            color="white"
        )

        ax.text(
            x, y - 0.12,
            score_labels[i],
            ha="center", va="center",
            fontsize=11.5,
            fontweight="bold",
            color=dark
        )

        ax.text(
            x, y - 0.34,
            descriptors[i],
            ha="center", va="center",
            fontsize=9.8,
            color=gray
        )

    ax.annotate(
        "", xy=(8.35, y + 0.14), xytext=(6.45, y + 0.14),
        arrowprops=dict(arrowstyle="-|>", lw=2.1, color="#2c3e50")
    )

    ax.annotate(
        "", xy=(11.35, y + 0.14), xytext=(9.45, y + 0.14),
        arrowprops=dict(arrowstyle="-|>", lw=2.1, color="#2c3e50")
    )



ax.add_patch(
    FancyBboxPatch(
        (0.9, 4.45), 16.2, 1.45,
        boxstyle="round,pad=0.12,rounding_size=0.10",
        linewidth=2,
        edgecolor=blue,
        facecolor="white"
    )
)

ax.text(
    9, 5.72,
    "Scale Configuration and Standardization",
    ha="center", va="center",
    fontsize=15,
    fontweight="bold",
    color=blue
)


headers = ["Raw scale", "Low", "Medium", "High", "Standardization", "Operational Status"]
x_headers = [2.0, 4.1, 5.8, 7.5, 10.3, 14.3]

for x, h in zip(x_headers, headers):
    ax.text(
        x, 5.35,
        h,
        ha="center", va="center",
        fontsize=11.5,
        fontweight="bold",
        color=blue
    )


scale_rows = [
    ("1–3",  "1", "2",   "3",  r"$(S-1)/(3-1)$",   "Operationalized"),
    ("1–5",  "1", "3",   "5",  r"$(S-1)/(5-1)$",   "Supported"),
    ("1–7",  "1", "4",   "7",  r"$(S-1)/(7-1)$",   "Supported"),
    ("1–10", "1", "5.5", "10", r"$(S-1)/(10-1)$", "Supported")
]

y_rows = [5.08, 4.84, 4.60, 4.36]

for row, y in zip(scale_rows, y_rows):
    raw, low, med, high, norm, use = row

    
    if raw == "1–3":
        ax.add_patch(
            FancyBboxPatch(
                (1.25, y - 0.12), 15.2, 0.22,
                boxstyle="round,pad=0.02,rounding_size=0.04",
                linewidth=0,
                facecolor="#fdecea"
            )
        )

    values = [raw, low, med, high, norm, use]

    for x, val in zip(x_headers, values):
        color = selected_red if raw == "1–3" and val in ["1–3", "Operationalized"] else dark
        weight = "bold" if raw == "1–3" else "normal"

        ax.text(
            x, y,
            val,
            ha="center", va="center",
            fontsize=10.8,
            fontweight=weight,
            color=color
        )


ax.text(
    9, 4.18,
    "All scales are standardized to a common 0–1 interval; the 1–3 scale is operationalized.",
    ha="center", va="center",
    fontsize=10.8,
    color=gray
)


ax.text(
    9, 3.85,
    "Computational Structure",
    ha="center", va="center",
    fontsize=16,
    fontweight="bold",
    color=blue
)


ax.add_patch(
    FancyBboxPatch(
        (1.1, 2.65), 7.55, 0.95,
        boxstyle="round,pad=0.18,rounding_size=0.10",
        linewidth=2,
        edgecolor=blue,
        facecolor=light_blue
    )
)

ax.text(
    4.875, 3.32,
    "Min–Max Normalization",
    ha="center", va="center",
    fontsize=14,
    fontweight="bold",
    color=blue
)

ax.text(
    4.875, 2.95,
    r"$S_{norm}=\dfrac{S-S_{min}}{S_{max}-S_{min}}$",
    ha="center", va="center",
    fontsize=22,
    color=dark
)


ax.add_patch(
    FancyBboxPatch(
        (9.35, 2.65), 7.55, 0.95,
        boxstyle="round,pad=0.18,rounding_size=0.10",
        linewidth=2,
        edgecolor=blue,
        facecolor=light_blue
    )
)

ax.text(
    13.125, 3.32,
    "RBISS Aggregation",
    ha="center", va="center",
    fontsize=14,
    fontweight="bold",
    color=blue
)

ax.text(
    13.125, 3.03,
    r"$RBISS_i=w_RR_{norm,i}+w_PP_{norm,i}+w_DD_{norm,i}$",
    ha="center", va="center",
    fontsize=19,
    color=dark
)

ax.text(
    13.125, 2.78,
    r"$w_R+w_P+w_D=1$",
    ha="center", va="center",
    fontsize=16.5,
    color=dark
)


ax.annotate(
    "", xy=(9.15, 3.12), xytext=(8.85, 3.12),
    arrowprops=dict(arrowstyle="-|>", lw=2.5, color=blue)
)


ax.add_patch(
    FancyBboxPatch(
        (1.1, 1.67), 15.8, 0.55,
        boxstyle="round,pad=0.16,rounding_size=0.09",
        linewidth=1.6,
        edgecolor="#8aa9c4",
        facecolor="white"
    )
)

ax.text(
    9, 1.95,
    r"Study configuration: 1–3 expert scoring scale with equal criterion weights "
    r"$w_R=w_P=w_D=\frac{1}{3}$",
    ha="center", va="center",
    fontsize=13.2,
    fontweight="bold",
    color=dark
)


ax.add_patch(
    FancyBboxPatch(
        (1.1, 0.65), 15.8, 0.65,
        boxstyle="round,pad=0.18,rounding_size=0.10",
        linewidth=2,
        edgecolor=blue,
        facecolor=row_bg
    )
)

ax.text(
    9, 0.98,
    "Decision Rule: Configure Scale → Normalize → Aggregate → Rank → Select",
    ha="center", va="center",
    fontsize=16,
    fontweight="bold",
    color=blue
)


plt.tight_layout()

plt.savefig(
    "RBISS_framework_scale_standardization_table.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "RBISS_framework_scale_standardization_table.pdf",
    bbox_inches="tight"
)

plt.show()