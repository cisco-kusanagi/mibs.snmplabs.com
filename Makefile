.DEFAULT_GOAL := help

fetch:  ## Download all mibs from the source
	@# Wget recursive
	wget --recursive --reject-regex 'index.html*' \
	  --no-parent --no-host-directories http://mibs.snmplabs.com/asn1/

compile:  ## Compile all MIBs into .py files
	@for f in $$(ls asn1); do \
	  echo "compiling $$f"; \
	  mibdump.py --no-python-compile --destination-directory=./pysnmp --mib-source=file://$$(pwd)/asn1 $$f; \
	done
	rm -rf asn1/index.html*

help:  ## Print list of Makefile targets
	@# Taken from https://github.com/spf13/hugo/blob/master/Makefile
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  cut -d ":" -f1- | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
