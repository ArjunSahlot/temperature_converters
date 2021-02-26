#!/bin/bash

download_link=https://github.com/ArjunSahlot/temperature_converters/archive/master.zip
temporary_dir=$(mktemp -d) \
&& curl -LO $download_link \
&& unzip -d $temporary_dir master.zip \
&& rm -rf master.zip \
&& mv $temporary_dir/temperature_converters-master $1/temperature_converters \
&& rm -rf $temporary_dir
echo -e "[0;32mSuccessfully downloaded to $1/temperature_converters[0m"
