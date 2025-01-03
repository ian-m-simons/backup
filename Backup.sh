#!/usr/bin/env bash
#creating backup name and making it hidden
Backup=.$1'.bak'

#creating abckup 
cp $1 $Backup
