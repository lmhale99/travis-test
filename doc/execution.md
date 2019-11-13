# Executing the calculation

1. Install Anaconda or Miniconda 3 if needed.

## Option #1: Use snakemake

2. Install snakemake if needed

        conda install -c conda-forge -c bioconda snakemake

3. Fill in the the calc_{name}.in file in the scripts directory.

4. Execute the snakemake file from the calculation's root directory

        snakemake --use-conda

## Option #2: Manual installation

2. Create a new conda environment for this calculation, and activate it.  This is optional but recommended as it helps with package version verification.

        conda env create -f envs/calc_{name}.yaml
        source activate calc_{name}

3. Fill in the the calc_{name}.in file in the scripts directory.

3. Run the calculation directly from within the scripts/ directory

        cd scripts/
        python calc_{name}.py calc_{name}.in
