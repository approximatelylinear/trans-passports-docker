#!/usr/bin/env bash

rake db:create db:migrate db:seed
rails s -p 3000 -b '0.0.0.0'
