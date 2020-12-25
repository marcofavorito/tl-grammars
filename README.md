# Standard Grammar for LTL and LDL

This repository
contains a standard grammar for LTL and LDL.

## Build

We use [Pandoc](https://pandoc.org/) to build the document in PDF and HTML formats.

In particular, on Ubuntu, you will need the following packages:

```
sudo apt-get install -y pandoc pandoc-citeproc latexmk texlive-xetex
```

Then, just call `make`.

Otherwise, you can use the Docker image with all the needed dependencies:
```
docker build -t pandoc .
docker run -v$(pwd):/build -it pandoc /bin/bash -c "cd /build && make"
```

The output is in HTML format in `index.html` and 
in PDF format in `main.pdf`.

## Repository structure

In `docs/` you will find the sources of the standard
(one file per section).

In `grammars/` you can find implementations
of the standard. Currently, 
there's only the implementation in ANTLR4 (in `grammars/antlr4/`).

## Contribute

To contribute, please 
[open an issue](https://github.com/marcofavorito/tl-grammars/issues),
[submit a PR](https://github.com/marcofavorito/tl-grammars/pulls),
or [contact the maintainer](mailto:favorito@diag.uniroma1.it) for a discussion.


## License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

