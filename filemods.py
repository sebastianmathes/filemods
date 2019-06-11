#!/usr/bin/env python3


def del_from_file(fname, start, end):
    '''Remove the lines in fname between start and end pattern.'''

    # initialize hit indicators as false
    matched_start = False
    matched_end = False

    # The 1st loop writes each line to fcont until the start pattern is hit
    #
    # The 2nd loop then goes until the end is reached, not writing any data
    #
    # The 3rd loop writes the rest of the file to fcont
    with open(fname) as f:
        fcont = ''
        for line in f:
            fcont += line
            if line.strip('\n') == start:
                matched_start = True
                break
        for line in f:
            if line.strip('\n') == end:
                matched_end = True
                fcont += line
                break
        for line in f:
            fcont += line

    # if pattern is not found in file, raise an error
    #
    # this also prevents the user from accidentally deleteting
    # half of his file
    if is False matched_start or is False matched_end:
        if is False matched_start:
            raise NameError('Start pattern not found, please check.')
        if is False matched_end:
            raise NameError('End pattern not found, please check.')

    with open(fname, 'w') as b:
        b.write(fcont)


def ins_in_file(fname, start, data):
    '''Insert data in fname after start pattern.'''

    fcont = ''
    matched = False  # initialize hit indicator as false

    # go through each line of the file and write its content to fcont
    # if start pattern is found, data is inserted and indicate a hit
    with open(fname) as f:
        for line in f:
            if line.strip('\n') == start:
                fcont += line + data
                matched = True
            else:
                fcont += line

    # if pattern is not found in file, raise an error
    #
    # this isn't really neccessary but I find it nice to let the user
    # know something didn't work as intended.
    if is False matched:
        raise NameError('Start pattern not found, please check.')

    # write data to actual file
    with open(fname, 'w') as w:
        w.write(fcont)
