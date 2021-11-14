import json
import sys
import pandas as pd


class Parser:
    def __init__(self, dataset_path: str):
        self.data = pd.read_csv(dataset_path)

    # Task 1 - average rating by evaluator id
    def eval_avg(self, export: bool = False):
        avg_series = self.data.groupby('evaluator id')['q1 score'].mean()
        if export:
            export_results(avg_series.to_dict(), '1.json')
        return avg_series

    # Task 2 - average rating for each sentence
    def sent_avg(self, export: bool = False):
        avg_series = self.data.groupby('sentence pair id', sort=False)[
            'q1 score'].mean()

        # highest-scoring sentences
        max_val = avg_series.max()
        max_series = avg_series[avg_series == max_val]

        # lowest-scoring sentences
        min_val = avg_series.min()
        min_series = avg_series[avg_series == min_val]

        if export:
            # combined output
            result = {"avg": avg_series.to_dict(),
                      "min": {"score": min_val, "sentences": min_series.index.to_list()},
                      "max": {"score": max_val, "sentences": max_series.index.to_list()}
                      }
            export_results(result, '2.json')
        return avg_series, max_series, min_series


def export_results(data: dict, path: str):
    with open(path, 'w') as file:
        json.dump(data, file, indent=2)


def analyse(dataset_path: str):
    parser = Parser(dataset_path)
    parser.eval_avg(export=True)
    parser.sent_avg(export=True)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        analyse(sys.argv[1])
    else:
        analyse('./bg-sentence-pair-scores.csv')
