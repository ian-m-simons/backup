#!/usr/bin/env bash

#finding backup's name
Backup='.'$1'.bak'

#restoring file
cp $Backup $1
#deleting backup
rm $Backup
