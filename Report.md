# Aura healthcare analysis

## Findings and recommendations

**Data quality.** All 4,406 records were retained. The file has no missing values or duplicates. There are 3 negative-income records; these need source clarification before any decision to recode them. In-memory optimization reduced storage from 2,263,919 to 159,767 bytes.

**Age and income.** After conversion, mean age is 74.02 years, the median is 73.0, and the range is 66–109. This older sample cannot represent all age groups. Mean income is 25,271.32 currency units versus a median of 16,981.50; the upper tail pulls the mean upward. Income ranges from -10,125.00 to 548,351.00.

**Visits.** Mean visits is 5.77, median visits is 4, and the maximum is 89. There are 683 zero-visit records (15.5%). The mean exceeding the median and the upper box-plot tail indicate right skew.

**Health.** Average visits are 8.90 for poor health (n=554), 5.51 for average health (n=3509), and 3.43 for excellent health (n=343). Poor-health respondents have the highest descriptive utilization. Aura could investigate their service needs when planning care capacity; this association does not prove that health status causes the difference.

**Region.** Mean visits are highest in west (6.37) and lowest in midwest (5.41), a gap of 0.96 visits per person. The source category `other` is retained as given. Differences are unadjusted for age, health, and other case-mix factors and have not been tested for statistical significance. Investigate these factors before allocating resources by region.

**Correlation and outliers.** Visits and chronic-condition count have a Pearson correlation of 0.262. Correlations describe linear associations and may be affected by skew and extreme observations. The 1.5 × IQR rule flags 53 age, 270 income, and 173 visit observations. A statistical flag is not evidence of a data error. Review source records and consider sensitivity analyses before removing values.

**Limits.** This analysis uses unweighted sample summaries. The supplied CSV does not establish survey weights, a sampling design, precise visit definitions or reporting periods, or income currency/price basis. Avoid interpreting `visits` as all types of healthcare use combined: the file has other distinct utilization columns. Historical data should not be treated as a current forecast. The analysis supports further investigation rather than clinical decisions or causal conclusions.


See Aura_Capstone.html or Aura_Capstone.ipynb for methods, statistics, tables, code, and plots.
