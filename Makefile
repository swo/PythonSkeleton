.PHONY: rst_readme

rst_readme: 
	pandoc -t rst README.md > README.rst
