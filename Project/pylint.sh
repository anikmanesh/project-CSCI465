#!/bin/bash

pylint --load-plugins pylint_django --disable=missing-docstring ./helloSite/helloSite
pylint --load-plugins pylint_django --disable=missing-docstring ./helloSite/myapp
