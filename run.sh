#!/bin/bash

export FLASKAPP=piggy_money_v2.app;
npm run --prefix ./vue_app/ build;
flask run;

