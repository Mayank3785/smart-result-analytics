from fastapi import APIRouter, Query
import pandas as pd
import os

# Create router
router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

# Build absolute path to CSV
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "results.csv")


@router.get("/branch-top10")
def branch_top_10(branch: str = Query(..., example="CSE")):
    if not os.path.exists(CSV_PATH):
        return {"error": "CSV file not found"}

    df = pd.read_csv(CSV_PATH)

    branch_df = df[df["Branch"].str.upper() == branch.upper()]

    if branch_df.empty:
        return {"error": f"No data found for branch {branch}"}

    top_10 = (
        branch_df
        .sort_values(by="CGPA", ascending=False)
        .head(10)
        .to_dict(orient="records")
    )

    return {
        "branch": branch.upper(),
        "top_10_students": top_10
    }


@router.get("/all-branches-top10")
def all_branches_top_10():
    if not os.path.exists(CSV_PATH):
        return {"error": "CSV file not found"}

    df = pd.read_csv(CSV_PATH)
    result = {}

    for branch in df["Branch"].unique():
        top_students = (
            df[df["Branch"] == branch]
            .sort_values(by="CGPA", ascending=False)
            .head(10)
            .to_dict(orient="records")
        )
        result[branch] = top_students

    return result


@router.get("/university-top10")
def university_top_10():
    if not os.path.exists(CSV_PATH):
        return {"error": "CSV file not found"}

    df = pd.read_csv(CSV_PATH)

    top_10 = (
        df.sort_values(by="CGPA", ascending=False)
        .head(10)
        .to_dict(orient="records")
    )

    return {"university_top_10": top_10}
