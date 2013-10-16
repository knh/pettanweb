#!/usr/bin/env python

##
# Minimalistic Templater
##

def do_template ( basefile, templater ):
    with open (basefile, "r") as w:
        for line in w:
            yield templater(line)
            
def mre_templater_wrapper ( matcher, replacer, evaluator ):
    # M-R-E templating process, match a line, replace and/or evaluate
    raise Exception("Unimplemented")
    
def templater_import ( basefile, importstring ):
    # resolves imports 
    raise Exception("Unimplemented")
