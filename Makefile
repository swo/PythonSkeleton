.PHONY: rst_readme

rst_readme: 
	pandoc -t rst README.md > README.rst

register:
	python setup.py register

sdist:
	python setup.py sdist

cheesecake:
	cheesecake_index --path=dist/foo.tar.gz

upload:
	python setup.py upload
