rule calc_diatom_scan:
    input:
        "calc_diatom_scan.in"
    output:
        "results.json"
    conda:
        "envs/calc_diatom_scan.yaml"
    shell:
        """
        cp -r scripts/ rundir/
        cp {input} rundir/
        cd rundir/
        python calc_diatom_scan.py {input}
        cp {output} ../.
        """
