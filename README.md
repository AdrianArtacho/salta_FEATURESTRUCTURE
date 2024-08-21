# FeatureStructure

This repo combines multiple pdp files from different sources, runs the aggregation function if needed, produces a weights file and a URL for the intended segmentation project.

---

## Installation

1. Clone repository

2. Create venv

```termminal
    python3 -m venv ./.venv
```

---

## Usage

Activate venv and run main script:

```shell
python source .venv/bin/activate
python STRUCT.py
```

You will have to enter general infos about the project, select the feature folders (where the individual PDP are) and select -if desired- which features to aggregate together.

The results will be stored in `INTER/`, in the form of modified weights file, modified json file and aggregation plots.

The last stage will integrate all plots and produce one final .csv file and one finel weights file from the information in `INTER/`:

```shell
# This bit is now integrated in the main `STRUCT.py` script
python INTEGRATE.py
```

---

## To-Do

- Issue when features have the same name? modify them based on the class name in both the csv AND the weights file?

- possibility to ommit features?

- There is an issue with the SALAT gui:

> - ~~Could it be the merged feature names, which may not exist in the weights file?~~
>
> - ~~Could it be combining modalities?~~
>
> - Could it be that the reason why there are two very similar files? (note, I NEED the surname for the files, because there are different settings) Does the format hold also for segtree?
> 
> - ~~Could it be specific features?~~
> - ~~Could it be features with NaN as weight?~~
>
> - Could it be that the generated names are to long?

!!! THE MERGING DOES NOT APPLY THE WEIGHTS PROPERLY!!!

---

test_2agg:

> paths_list:
> ['INPUT/testu51/testu51-Energy.csv',
> 'INPUT/testu51/testu51-EntropyEnergy.csv',
> 'INPUT/testu51/testu51-SpectralCentroid.csv',
> 'INPUT/testu51/testu51-SpectralEntropy.csv',
> 'INPUT/testu51/testu51-d.csv',
> 'INTER/testu51/aggregate_MFCC2_MFCC13_MFCC8_MFCC7_MFCC11_MFCC9_MFCC4_MFCC10_MFCC3_MFCC12_MFCC5_MFCC6.csv']