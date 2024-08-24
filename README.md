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

You will have to enter general infos about the project, select the feature folders (where the individual PDP are) and select -if desired- which features to aggregate together. The results will be stored in `INTER/`, in the form of modified weights file, modified json file and aggregation plots. The last stage will integrate all plots and produce one final .csv file and one finel weights file from the information in `INTER/`:

```shell
# This bit is now integrated in the main `STRUCT.py` script
python INTEGRATE_sets.py
```

Mind you, this line in `INTEGRATE_sets.py` drops column 'source' to make the files lighter on the server:

```python
data_reduced = dropcol.main(combined_df,colname='source')
```

---

## CHECK_SALTA

You can use this complementary script to evaluate the output, and to jot down whether or not it works in the GUI.

```terminal
python CHECK_SALTA.py
```

---

## Color conventions

> RED mpipe
> 
> BLUE audio
> 
> GREEN inert

---

## Progress

Issue with merging features: (Does the module apply the right weights while aggregating features?)

> make example test to see the issue
> find where the merging happens
> add button to make the next thing optional...
> apply weights appropriately

---

Issue with the wrong X-axis representation in the App

> I dealt with this before. Where could I find that?
> We encounter again the issue with space on the right from the plots, I can't remember if it was related to a minimum number of samples???

**NOW THE X_AXIS REPRESENTS MILLISECONDS**

---

###### Issue with the App sometimes giving me an error

analyze csv files directly, if no issue could be found...

> ...

Issue when features have the same name? 

>  modify them based on the class name in both the csv AND the weights file?
> 
> ...

~~Could it be the merged feature names, which may not exist in the weights file?~~

~~Could it be combining modalities?~~

Could it be that the reason why there are two very similar files? 

> (note, I NEED the surname for the files, because there are different settings) Does the format hold also for segtree?

~~Could it be specific features?~~

~~Could it be features with NaN as weight?~~

~~Could it be that the generated names are to long?~~

> !!! The issue with the App seems to be the classes !!! The tests that didn't work (6 and 7) are the ones that have more than one different class. BUT `test3`DID work even though it has 2 different classes!
> 
> It is merging what creates the source column...
> 
> 112 chars still no problem...

I could run it locally in node.js to see the error message

> ...

###### Go systematically:

> 1 class (no merge)
> 
> > mic    `test_19`
> > 
> > mix    `test_20` NO
> > 
> > imu    `test_21` NO                                    2.1mb
> > 
> > mpipe    `test_22` NO                                9.9mb
> 
> 1 class (merged)
> 
> > mic     `test_23`
> > 
> > mix
> > 
> > imu
> > 
> > mpipe
> 
> 2 classes (no merge)
> 
> > mic + imu    `test_3`
> > 
> > ...
> 
> 2 classes (each merged as one feature)
> 
> > mic + imu    `test_5` NO, `test_12` SI    21mb
> > 
> > imu + mpipe `test_6` SI, `test_26`NO    7.9mb
> > 
> > mpipe + mic `test_7` NO, `test_14` SI    20mb
> > 
> > imu + mix `test_8` NO, `test_15` NO    20mb
> > 
> > mic + mix `test_17` NO                            37mb
> > 
> > mpipe + mix `test_16` NO                        25mb
> 
> 3 classe (each merged)
> 
> > mic + imu + mpipe `test_18` NO            24mb
> > 
> > ...
> 
> ...

---

###### In test88, `SpectralSpread`does funny things...

> could there be negative values or sth?
> 
> ...

###### Identify where the second (confusing) csv is generated

> ...

---

### To-Do

- possibility to ommit features?
- If there is only ONE feature, do not ask whether or not to merge!
- There are 2 .csv generated. I guess it is ok if one of them is 'raw' (with source, no prettyfy, etc. and the other one the one meant for the GUI) --> rename the output files to achieve this
- At "check"... could there be a 'yes to all' and 'no to all' options?
- UPLOAD to Drive:

> exp16a_mic-vs-imu-mpipe
> 
> exp16a_mic-vs-mix

---

test_2agg:

> paths_list:
> ['INPUT/testu51/testu51-Energy.csv',
> 'INPUT/testu51/testu51-EntropyEnergy.csv',
> 'INPUT/testu51/testu51-SpectralCentroid.csv',
> 'INPUT/testu51/testu51-SpectralEntropy.csv',
> 'INPUT/testu51/testu51-d.csv',
> 'INTER/testu51/aggregate_MFCC2_MFCC13_MFCC8_MFCC7_MFCC11_MFCC9_MFCC4_MFCC10_MFCC3_MFCC12_MFCC5_MFCC6.csv']



0,0.0,aggregate_TiltZ_AccelX_TiltY,lower_limit

477300,0.0,aggregate_TiltZ_AccelX_TiltY,higher_limit