rule atommantest:
    input:
        "calc_diatom_scan.in"
    output:
        "results.json"
    conda:
        "envs/calc_diatom_scan.yaml"
    shell:
        "cd script/; python calc_diatom_scan.py calc_diatom_scan.in"
