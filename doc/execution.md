# Executing the calculation

## Option #1: Using snakemake

The necessary requirements for running the calculation can be automatically installed using snakemake

Blah, blah

    snakemake --use-conda

## Option #2: Manual installation

1. Install Anaconda or Miniconda 3.
2. (Optional) Create a new conda environment for this calculation.  This is optional but recommended as it helps with package version verification.
3. The .yaml file(s) in the envs/ directory specify the conda package requirements for the calculation.
4. Run the calculation using

        cd scripts
        python calc_{name}.py calc_{name}.in
