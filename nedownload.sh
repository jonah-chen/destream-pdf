#!/bin/bash
python parser.py "$1"
while IFS= read -r line; do
  ./destreamer.sh -i "$line" -o downloads --skip &
done < queue.txt
cat downloaded.txt queue.txt > downloaded.txt
rm queue.txt
