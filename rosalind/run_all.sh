#!/bin/sh -e

SCRIPT_DIR=$(dirname $(readlink -f "$0"))

DIRS_TO_EXCLUDE="bioinf_common template"

for PROBLEM_DIR in "$SCRIPT_DIR/"* ; do
  PROBLEM=$(basename "$PROBLEM_DIR")
  if [[ ! -d "$PROBLEM_DIR" || -L "$PROBLEM_DIR" || "$DIRS_TO_EXCLUDE" = *"$PROBLEM"* ]]; then
    continue
  fi;

  MAIN="$PROBLEM_DIR/main.py"
  DATASET="$PROBLEM_DIR/sample_ds.txt"
  echo "$PROBLEM"
  "$MAIN" "$DATASET" > /dev/null
done
