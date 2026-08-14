import pandas as pd


def recommend_funds(risk_appetite):
    """
    Recommend the top 3 mutual funds by Sharpe ratio
    matching the selected risk appetite.
    """

    # Load required datasets
    scorecard = pd.read_csv("fund_scorecard.csv")
    scheme = pd.read_csv(
        "data/processed/cleaned_scheme_performance.csv"
    )

    # Merge risk grade with scorecard
    data = scorecard.merge(
        scheme[
            [
                "amfi_code",
                "risk_grade"
            ]
        ],
        on="amfi_code",
        how="left"
    )

    # Validate risk appetite
    valid_risks = [
        "Low",
        "Moderate",
        "High"
    ]

    if risk_appetite not in valid_risks:
        raise ValueError(
            "Risk appetite must be Low, Moderate, or High."
        )

    # Filter matching risk grade
    matching_funds = data[
        data["risk_grade"] == risk_appetite
    ].copy()

    # Rank by Sharpe ratio
    recommendations = (
        matching_funds
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    return recommendations[
        [
            "amfi_code",
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "fund_score"
        ]
    ]


if __name__ == "__main__":

    print("=" * 70)
    print("BLUESTOCK MUTUAL FUND RECOMMENDER")
    print("=" * 70)

    risk = input(
        "Enter risk appetite (Low / Moderate / High): "
    ).strip().title()

    try:
        result = recommend_funds(risk)

        if result.empty:
            print(
                "\nNo matching funds found for:",
                risk
            )
        else:
            print(
                "\nTop 3 Recommended Funds:"
            )

            print(
                result.to_string(
                    index=False
                )
            )

    except ValueError as error:
        print("\nError:", error)