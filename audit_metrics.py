"""Audit metrics from figure counts, not from retrained model predictions.

Matrix layout: [[TN, FP], [FN, TP]], with default as positive class.
Python standard library only. Original analysis belongs to Dilip Singh Rajpurohit;
this script is a supplementary portfolio evidence check prepared with AI assistance.
"""
import csv
from pathlib import Path

MATRICES = {
    "Logistic regression": {"tn": 4281, "fp": 232, "fn": 679, "tp": 535},
    "Decision tree": {"tn": 4239, "fp": 274, "fn": 454, "tp": 760},
}

def calculate(counts):
    tn, fp, fn, tp = (counts[k] for k in ("tn", "fp", "fn", "tp"))
    if any(not isinstance(v, int) or v < 0 for v in (tn, fp, fn, tp)):
        raise ValueError("Counts must be non-negative integers")
    total = tn + fp + fn + tp
    if not total or not (tp + fn) or not (tn + fp) or not (tp + fp):
        raise ValueError("This audit requires non-empty actual classes and positive predictions")
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    specificity = tn / (tn + fp)
    return {
        **counts, "test_count": total,
        "accuracy": (tn + tp) / total,
        "default_precision": precision,
        "default_recall": recall,
        "default_f1": 2 * tp / (2 * tp + fp + fn),
        "specificity": specificity,
        "balanced_accuracy": (recall + specificity) / 2,
        "test_default_rate": (tp + fn) / total,
        "majority_non_default_accuracy": (tn + fp) / total,
    }

def main():
    rows = [{"model": name, **calculate(c)} for name, c in MATRICES.items()]
    assert rows[0]["test_count"] == rows[1]["test_count"] == 5727
    assert rows[0]["tn"] + rows[0]["fp"] == rows[1]["tn"] + rows[1]["fp"]
    assert rows[0]["tp"] + rows[0]["fn"] == rows[1]["tp"] + rows[1]["fn"]
    path = Path(__file__).resolve().parents[1] / "results" / "confusion-matrix-metrics.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print("Evidence audit: counts transcribed from original figures; models not retrained.")
    for row in rows:
        print(f"{row['model']}: accuracy={row['accuracy']:.2%}, "
              f"precision={row['default_precision']:.2%}, "
              f"recall={row['default_recall']:.2%}, F1={row['default_f1']:.2%}")
    print(f"Majority non-default accuracy: {rows[0]['majority_non_default_accuracy']:.2%}")
    print(f"CSV saved: {path.name}")

if __name__ == "__main__":
    main()
