#!/usr/bin/env bash

Backup='.'$1'.bak'

cp $Backup $1
rm $Backup
