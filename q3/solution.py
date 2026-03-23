# /// script
# requires-python = ">=3.11"
# ///

from __future__ import annotations

from itertools import compress


FRAGMENTS = {
    "I1": {"wc": 9, "scores": [0.06, 0.85, 0.23, -0.88]},
    "I2": {"wc": 15, "scores": [0.23, 0.78, 0.68, 0.34]},
    "I3": {"wc": 15, "scores": [0.66, 0.17, 0.48, 0.29]},
    "I4": {"wc": 10, "scores": [1.23, -0.36, 1.09, 0.05]},
    "I5": {"wc": 7, "scores": [-0.37, 0.62, 0.61, -0.46]},
    "I6": {"wc": 12, "scores": [0.97, 0.16, 1.25, -0.25]},
    "I7": {"wc": 17, "scores": [0.4, 0.98, -0.06, 1.37]},
    "I8": {"wc": 8, "scores": [1.13, 1.29, -0.2, -0.22]},
    "I9": {"wc": 6, "scores": [0.47, 0.67, 0.34, 0.36]},
    "I10": {"wc": 13, "scores": [-0.06, 0.68, -0.39, 0.21]},
    "I11": {"wc": 8, "scores": [0.45, -0.28, 0.95, 0.77]},
    "I12": {"wc": 8, "scores": [0.42, 1.09, 0.09, 1.2]},
    "I13": {"wc": 12, "scores": [0.88, 0.95, 0.39, 0.04]},
    "I14": {"wc": 12, "scores": [0.58, 1.31, 0.55, 0.23]},
    "I15": {"wc": 10, "scores": [0.98, 1.36, 0.18, -0.16]},
    "I16": {"wc": 13, "scores": [0.22, 1.08, 0.33, -0.4]},
    "I17": {"wc": 5, "scores": [0.76, -0.23, 0.21, -0.13]},
    "I18": {"wc": 9, "scores": [-0.39, 0.94, 0.97, 0.38]},
    "I19": {"wc": 16, "scores": [0.92, 0.8, 1.45, 0.07]},
    "I20": {"wc": 15, "scores": [0.39, 0.43, 1.33, 0.9]},
    "I21": {"wc": 6, "scores": [-0.12, -0.39, 0.17, 0.13]},
}

PAIR_BONUSES = {
    ("I7", "I10"): -0.57,
    ("I10", "I13"): -0.35,
    ("I7", "I11"): 0.67,
    ("I7", "I15"): -0.53,
    ("I3", "I11"): 0.03,
    ("I6", "I10"): -0.32,
    ("I4", "I7"): -0.18,
    ("I7", "I14"): 0.14,
    ("I18", "I21"): -0.59,
    ("I1", "I11"): 0.59,
    ("I1", "I5"): -0.14,
    ("I10", "I14"): 0.31,
    ("I6", "I11"): -0.38,
    ("I10", "I19"): -0.15,
    ("I13", "I19"): -0.41,
    ("I11", "I14"): 0.39,
    ("I1", "I19"): 0.45,
    ("I12", "I18"): 0.61,
    ("I8", "I11"): -0.35,
    ("I13", "I15"): 0.55,
    ("I1", "I7"): -0.02,
    ("I12", "I19"): -0.49,
    ("I17", "I20"): 0.4,
    ("I3", "I8"): 0.54,
    ("I1", "I21"): 0.35,
    ("I12", "I16"): -0.23,
    ("I7", "I8"): 0.04,
    ("I4", "I20"): -0.33,
    ("I2", "I21"): -0.38,
    ("I8", "I18"): -0.53,
    ("I5", "I14"): -0.38,
    ("I11", "I21"): 0.15,
    ("I8", "I21"): -0.29,
    ("I8", "I20"): 0.61,
    ("I6", "I20"): -0.62,
    ("I6", "I21"): -0.55,
    ("I2", "I14"): -0.55,
    ("I14", "I19"): 0.56,
    ("I14", "I15"): 0.68,
    ("I2", "I4"): 0.59,
    ("I9", "I18"): 0.09,
    ("I9", "I20"): 0.21,
    ("I5", "I7"): -0.13,
    ("I16", "I18"): 0.5,
    ("I1", "I8"): 0.41,
}

MODEL_OFFSETS = [-2.37, -0.68, -2.48, 0.03]
BASE_ACCURACY = 95.0
TARGET_MEAN = 97.0
TARGET_FLOOR = 92.0


def evaluate(selected_ids: list[str]) -> tuple[int, float, float]:
    pair_bonus = sum(
        bonus for pair, bonus in PAIR_BONUSES.items() if pair[0] in selected_ids and pair[1] in selected_ids
    )
    word_count = sum(FRAGMENTS[item]["wc"] for item in selected_ids)
    model_scores = []
    for model_index in range(4):
        total = BASE_ACCURACY + MODEL_OFFSETS[model_index] + pair_bonus
        total += sum(FRAGMENTS[item]["scores"][model_index] for item in selected_ids)
        model_scores.append(total)
    macro_mean = sum(model_scores) / 4
    model_floor = min(model_scores)
    return word_count, macro_mean, model_floor


def solve() -> tuple[list[str], int, float, float]:
    ids = list(FRAGMENTS)
    best: tuple[list[str], int, float, float] | None = None

    for mask in range(1 << len(ids)):
        selected = list(compress(ids, [(mask >> i) & 1 for i in range(len(ids))]))
        word_count, macro_mean, model_floor = evaluate(selected)
        if macro_mean < TARGET_MEAN or model_floor < TARGET_FLOOR:
            continue
        if best is None or word_count < best[1]:
            best = (selected, word_count, macro_mean, model_floor)

    if best is None:
        raise RuntimeError("No valid prompt combination found.")
    return best


def main() -> None:
    selected, word_count, macro_mean, model_floor = solve()
    answer = f"{','.join(selected)};{word_count};{macro_mean:.2f}%;{model_floor:.2f}%"
    print(answer)


if __name__ == "__main__":
    main()
