#!/bin/bash
if pytest --cov=helpers --cov-report= --no-cov-on-fail tests; then
  coverage report --skip-covered -m
  coverage html
fi;
