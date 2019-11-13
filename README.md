# Diatom scan calculation method

[![Build Status](https://travis-ci.org/lmhale99/travis-test.svg?branch=master)](https://travis-ci.org/lmhale99/travis-test)

**Lucas M. Hale**, [lucas.hale@nist.gov](mailto:lucas.hale@nist.gov?Subject=ipr-demo), *Materials Science and Engineering Division, NIST*.

## Introduction

The diatom_scan calculation style evaluates the interaction energy between two atoms at varying distances.  This provides a measure of the isolated pair interaction of two atoms providing insights into the strengths of the attraction/repulsion and the effective range of interatomic spacings.  This scan also gives insight into the computational smoothness of the potential's functional form.

More details on the calculation's methodology and theory can be found in the [theory documentation](doc/theory.md)

### Version notes

- None

### Disclaimers

- [NIST disclaimers](http://www.nist.gov/public_affairs/disclaimer.cfm)
- No 3+ body interactions are explored with this calculation as only two atoms are used.

## How to use

1. Fill in the input parameter file calc_*.in found in the scripts/ directory.  See the [parameters documentation](doc/parameters.md) for a description of the allowed input values.
2. Copy any additional files required to run the calculation into the scripts/ folder.
3. Run the calculation.  See the [execution documentation](doc/execution.md) for more details.


