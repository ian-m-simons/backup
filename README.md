These three scripts serve as an automated backup system for any file which you might be editing. By running the backup script followed by a file name a hidden backup will automatically be created in the following format: .<fileName>.<fileExtension>.bak
running the restore script will replace the existing file with the created backup file and delete the backup
running the commit changes script will simply delete the backup 

how to use:

>create aliases to each script, ensure you use the full path so that you can run them anywhere in your system. 
>before editing file run the backup script followed by the file name. 
>if you need to revert changes run restore script followed by file name
>if changes are correct and you are done run commit changes and backup will be deleted

examples (without alias):

python3 Backup.py test.txt
python3 Restore.py test.txt
python3 commitChanges.py test.txt
