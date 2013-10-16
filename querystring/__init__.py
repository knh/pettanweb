#!/usr/bin/env python
def parse_simple (query_string):
    # this is not standards compliant
    # but its good enough most of the time
    qs = {}
    queryitems = query_string.split("&");
    for item in queryitems:
        p = item.split("=")
        qs[p[0]] = p[1]
    return qs
    
def form_simple (qsobject):
    # also not standards compliant, but hey
    qs = []
    for key in qsobject:
        qs.append("=".join([key, qsobject[key]]))
    return "&".join(qs)
