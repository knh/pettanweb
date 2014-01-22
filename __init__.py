#!/usr/bin/env python
import os
import Cookie

HAS_GIVEN_HEADER = False

def guess_mime(filename):
    ext = filename.lower().split(".")
    if ext[-1] == "css":
        return "text/css";
    elif ext[-1] == "js":
        return "application/javascript";
    elif ext[-1] in ["txt","md","c","cpp"]:
        return "text/plain";
    else:
        return "text/html";

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
    route = tuple(route)
    current = tuple(current)
    
    if route == current:
        return True;
    if route == () or current == ():
        return False;
    
    if route[0] == "*":
        return route_match(route[1:], current[1:]) or route_match(route, current[1:])
    if route[0] == current[0]:
        return route_match(route[1:], current[1:])
        
def route(routes, routing = get_querystring()):
    current = router(routing)
    for route in routes:
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
