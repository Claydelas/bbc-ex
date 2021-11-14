import json
import pandas as pd

data = pd.read_csv('./bg-sentence-pair-scores.csv')

# average rating by evaluator id
eval_avg = data.groupby('evaluator id')['q1 score'].mean()

with open('1.json', 'w') as file:
    json.dump(eval_avg.to_dict(), file, indent=2)
