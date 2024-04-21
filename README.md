# FeatureStructure

This repo combines multiple pdp files from different sources, runs the aggregation function if needed, produces a weights file and a URL for the intended segmentation project.

---

## Usage

Activate venv:

```shell
python source .venv/bin/activate
```

Run the main script:

```shell
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

To-Do

- Issue when features have the same name? modify them based on the class name in both the csv AND the weights file?

- possibility to ommit features?
