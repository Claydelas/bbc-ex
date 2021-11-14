import json
import pandas as pd

data = pd.read_csv('./bg-sentence-pair-scores.csv')

# average rating by evaluator id
eval_avg = data.groupby('evaluator id')['q1 score'].mean()

with open('1.json', 'w') as file:
    json.dump(eval_avg.to_dict(), file, indent=2)

# average rating for each sentence
sent_avg = data.groupby('sentence pair id', sort=False)['q1 score'].mean()

# highest-scoring sentences
max_val = sent_avg.max()
max_series = sent_avg[sent_avg == max_val]

# lowest-scoring sentences
min_val = sent_avg.min()
min_series = sent_avg[sent_avg == min_val]

# combined output
result = {"avg": sent_avg.to_dict(),
          "min": {"score": min_val, "sentences": min_series.index.to_list()},
          "max": {"score": max_val, "sentences": max_series.index.to_list()}
          }

with open('2.json', 'w') as file:
    json.dump(result, file, indent=2)
