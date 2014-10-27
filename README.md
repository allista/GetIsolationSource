**GetIsolationSources** is a small command line utility written in Python that generates distribution of isolation sources given fasta files containing GenBank IDs in sequence descriptions (as produced by [SILVA](http://www.arb-silva.de/) tools).

To obtain needed information it uses automated Entrez queries, so you need a working Internet connection to perform the analysis. Queries are made in accordance with NCBI load-balance regulations, therefore processing several thousand records may take several minutes or even longer.

It is distributed as a source code supporting python setup tools, and as a standalone executables for Windows and Linux operation systems.

**GetIsolationSources uses [BioPython](http://biopython.org/wiki/Main_Page).** So if you're using source code distribution, the latest version of  [BioPython](http://biopython.org/wiki/Main_Page) should be installed.

[**Downaloads**](https://github.com/allista/GetIsolationSource/releases)

***
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a>
<br />
<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">GetIsolationSources</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://www.linkedin.com/pub/evgeny-taranov/a6/b71/62a" property="cc:attributionName" rel="cc:attributionURL">Evgeny Taranov</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.