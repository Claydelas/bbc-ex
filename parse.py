import json
import sys
import pandas as pd


def export_results(data: dict, path: str):
    with open(path, 'w') as file:
        json.dump(data, file, indent=2)


def analyse(path: str, export: bool = False):
    data = pd.read_csv(path)

    # Task 1 - average rating by evaluator id
    eval_avg = data.groupby('evaluator id')['q1 score'].mean()

    # Task 2 - average rating for each sentence
    sent_avg = data.groupby('sentence pair id', sort=False)['q1 score'].mean()

    # highest-scoring sentences
    max_val = sent_avg.max()
    max_series = sent_avg[sent_avg == max_val]

    # lowest-scoring sentences
    min_val = sent_avg.min()
    min_series = sent_avg[sent_avg == min_val]

    if export:
        export_results(eval_avg.to_dict(), '1.json')

        # combined output
        result = {"avg": sent_avg.to_dict(),
                  "min": {"score": min_val, "sentences": min_series.index.to_list()},
                  "max": {"score": max_val, "sentences": max_series.index.to_list()}
                  }
        export_results(result, '2.json')

    return eval_avg, sent_avg, max_series, min_series


if __name__ == '__main__':
    if len(sys.argv) > 1:
        analyse(sys.argv[1], export=True)
    else:
        analyse('./bg-sentence-pair-scores.csv', export=True)
