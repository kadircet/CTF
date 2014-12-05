#!/bin/bash
for i in $(seq 25); do
    echo $i $1 | tr $(printf %${i}s | tr ' ' '.')\A-Z A-ZA-Z
done
