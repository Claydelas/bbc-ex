# BBC - Coding Exercise

## Setup
There is a single dependency required to run the code - pandas.

For a conda environment, it can be installed with:

```sh
conda install pandas
```

Alternatively with pip:

```sh
pip install -r requirements.txt
```

## Running
**parse.py** can be executed as a standard python script, with an optional dataset path parameter. Omitting the path parameter defaults to **'./bg-sentence-pair-scores.csv'**, relative to the directory of the script.
```sh
python parse.py [path?]
```
One could also import **parse** as a module in another script:
```py
from parse import analyse

analyse('./bg-sentence-pair-scores.csv')
```
If access to the output series objects is required and/or exporting the outputs to files is undesirable, one could use the **Parser** class instead, which offers a more granular control of the process:
```py
from parse import Parser

parser = Parser('./bg-sentence-pair-scores.csv')
eval_avg_series = parser.eval_avg()
sent_avg_series, max_series, min_series = parser.sent_avg()
```
## Output
The script generates json files with outputs for each task with the following schemas:

1.json:
```json
{
  "BBC_Bulgarian_01": 63.12,
  ...
  evaluator id: average score
}
```
2.json:
```json
{
  "avg": {
    "BG_SE_1": 48.6,
    ...
    sentence pair id: average score
  },
  "min": {
    "score": 1.6,
    "sentences": [
      "BG_SE_45",
      ...
      sentence pair id
    ]
  },
  "max": {
    "score": 100.0,
    "sentences": [
      "BG_SE_14",
      ...
      sentence pair id
    ]
  }
}
```