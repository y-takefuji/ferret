# ferret
Calculating feature importances for ferret lethal

Dataset is downloaded from https://data.cdc.gov/National-Center-for-Immunization-and-Respiratory-D/An-aggregated-dataset-of-serially-collected-influe/cr56-k9wj/about_data

Rename it to ferret.csv.

Run ferret.py by the following command.
<pre>
$ python ferret.py
Unique values in 'lethal' column: [0 1]
Sorted Feature Importances using Random Forest:
         feature  importance
4    lethal_day    0.371207
12      wt_loss    0.124300
26      d9_inoc    0.119237
7          HPAI    0.094705
8     HPAI_MBAA    0.083981
...
Random Forest Accuracy: 0.99087
Sorted Feature Importances using Extra Trees:
         feature  importance
4    lethal_day    0.323805
26      d9_inoc    0.132350
8     HPAI_MBAA    0.128762
7          HPAI    0.115642
12      wt_loss    0.095213
...
Extra Trees Accuracy: 0.99087
</pre>
