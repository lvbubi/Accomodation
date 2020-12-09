#!/bin/bash

for entry in "./"*.xlsx
do
  libreoffice --headless --convert-to csv:"Text - txt - csv (StarCalc):44,34,76,1,1/1:" $entry --outdir '.'
  echo "$entry"
done
