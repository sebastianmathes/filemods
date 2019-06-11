# filemods
Automatically insert and remove data between a self-defined start and end pattern


## ins\_in\_file
Takes 3 arguments:
1. Filename - the name of the file, duh.
2. Startmark - User defined pattern which marks the beginning of the block
3. Data - The Data you want to insert. 

If the pattern was not found you will get an error.

## del\_from\_file
Takes 3 arguments:
1. Filename - the name of the file, duh.
2. Startmark - User defined pattern which marks the beginning of the block
3. Endmark - Same as above, but the end this time

You can set the pattern to pretty much anything you want, but it has to stand in a single line containing nothing else.
