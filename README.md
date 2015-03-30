**GetIsolationSources** is a small command line utility written in Python that generates distribution of isolation sources given fasta files containing GenBank IDs in sequence descriptions.

It searches for IDs using regular expressions in accordance with [NCBI specifications](http://www.ncbi.nlm.nih.gov/Sequin/acc.html), so the format of description strings does not matter.

To obtain needed information it uses automated Entrez queries, so you need a working Internet connection to perform the analysis. Queries are made in accordance with NCBI load-balance regulations, therefore processing several thousand records may take several minutes or even longer.

It is distributed as a source code supporting python setup tools, and as a standalone executables for Windows and Linux operation systems.

**GetIsolationSources uses [BioPython](http://biopython.org/wiki/Main_Page).** So if you're using source code distribution, the latest version of [BioPython](http://biopython.org/wiki/Main_Page) should be installed.

[**Downaloads**](https://github.com/allista/GetIsolationSource/releases)

***

**GetIsolationSources** by [**Evgeny Taranov**](https://www.linkedin.com/pub/evgeny-taranov/a6/b71/62a) is licensed under the [MIT](http://opensource.org/licenses/MIT) license.