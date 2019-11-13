rule atommantest:
    input:
        "input.json"
    output:
        "system.json"
    conda:
        "envs/test.yaml"
    script:
        "testing.py"
