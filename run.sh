#!/bin/bash

export FLASKAPP=piggy_money_v2.app
export FLASK_DEBUG=1
npm run --prefix ./vue_app/ build &
flask run
