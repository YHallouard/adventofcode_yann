init-repo: ## initialize the repo
	python setup.py install

update-package: ## install the functions
	pip uninstall calandarevent -y
	python setup.py install
