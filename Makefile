# Makefile

# https://clarkgrubb.com/makefile-style-guide#prologue
MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:

TGT = GITREPO.txt

.PHONY: all
all: $(TGT)

.PHONY: FORCE
FORCE:

$(TGT): FORCE
	> $@
	echo "gitdir: `git root`/.git" >> $@
	echo "HEAD `git desc`" >> $@
	echo "remotes {" >> $@
	git remote -v >> $@
	echo "}" >> $@
	echo "branches {" >> $@
	git branch -vv >> $@
	echo "}" >> $@

install:
	# TODO copy only select files or branch to CIRCUITPY device

.PHONY: clean clobber nuke
clean clobber nuke:
	-rm -f $(TGT)

# vim: set sw=4 ts=8 noet ic ai:
