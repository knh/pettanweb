#!/usr/bin/env python
import os
import Cookie

HAS_GIVEN_HEADER = False

def give_header(headers = {"Content-Type":"text/html"}, append = []):
    global HAS_GIVEN_HEADER
    if HAS_GIVEN_HEADER:
        print "<h2>[Error] Headers already sent!</h2>"
        return
    for header in headers:
        print "%s: %s" % (header, headers[header])
    for line in append:
        print line
    print ""
    HAS_GIVEN_HEADER = True

def redirect(url):
    give_header({"Location": url})

def get_querystring():
    return os.environ.get("QUERY_STRING", "")

def get_cookies():
    try:
        return Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE", ""))
    except (Cookie.CookieError, KeyError):
        return None 

def router(query):
    paths = query.split("/");
    # sanitize the paths
    sanitized = []
    for p in paths:
        if p == "" or p == ".":
            continue;
        if p == "..":
            if len(sanitized) > 0:
                sanitized.pop()
                continue;
            else:
                continue;
        sanitized.append(p)
    return tuple(sanitized)

def route_match(route, current):
    if len(route) < 2:
        return False
    for r in xrange(0, len(route) - 2):
        if current[r] != route[r]:
            return False
    return True
        
        
def route(routes, routing = get_querystring()):
    current = router(routing)
    for route in routes:
        if current == route:
            routes[route](current)
            return
        if route != () and route[-1] == "*":
            if route_match(route, current):
                routes[route](current)
                return
    if () in routes:
        routes[()](current)
        return
    print "<h1>404 - Route Not Found</h1>"
    print "<p>Could not access the resource you are requesting.</p>"
    print ""
    return
