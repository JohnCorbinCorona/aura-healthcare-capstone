# Aura Healthcare Capstone

Applied Data Science with Python: analysis of the course-provided NSMES1988 dataset (4,406 records).

## Start here

- **Aura_Capstone.ipynb** — executed notebook covering all four assignment tasks.
- **Aura_Capstone.html** — download and open in a browser to read the analysis with its charts.
- **aura_capstone.py** — runnable Python analysis.
- **Report.md** — findings and limitations.
- **Aura_Capstone_Submission.zip** — complete project, including plots and supporting tables in their original folders.

The three required exports are `NSMES1988new.csv`, `NSMES1988updated.csv`, and `NSMES1988_Dummy.csv`. The original `NSMES1988.csv` is retained unchanged.

## Run

Extract the ZIP and open a terminal in the extracted Aura_Capstone folder:

```bash
python -m pip install -r requirements.txt
python aura_capstone.py
```

Alternatively, open the notebook in Jupyter or Google Colab with the original CSV in the working directory and run the cells in order.

## Scope

The workflow covers inspection and cleaning, age and income scaling, descriptive statistics, health and region comparisons, distribution tables, categorical encoding, and visualizations. Findings describe the sample and do not establish causation.

Data source: [course dataset folder](https://drive.google.com/drive/folders/1c5FUOUhE0S1mDpqEL5tbIinVx9D507IU).
