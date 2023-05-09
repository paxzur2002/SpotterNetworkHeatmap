#!/bin/sh

awk -F ";;" '{ print $5 "," $6 }'
