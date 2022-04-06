# sphinx-github-pages


Make conda env:

```
    conda env create -f environment.yaml

    conda activate sph_gh_test

```

Make documentation:

```
    cd docsrc
    make html
```

Make documentation and copy to `docs`:

```
    cd docsrc
    make github
```
(or `make html` and then `cp -a _build/html/. ../docs`)

Then open https://nchaly.github.io/sphinx-github-pages/ to check deployed documentation.

(Create by the tutorial: https://www.docslikecode.com/articles/github-pages-python-sphinx/ )