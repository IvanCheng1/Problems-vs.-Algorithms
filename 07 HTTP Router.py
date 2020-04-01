
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = "/"
        self.handler = handler # default is None
        self.children = {}


    def insert(self, nodes, handler):
        # if there are no more nodes to recur, assign handler
        if len(nodes) == 0:
            self.handler = handler
            return
        # node to recur into, and remove from nodes list
        node = nodes.pop(0)
        # assign new RouteTrie if not exist
        if node not in self.children:
            self.children[node] = RouteTrie()
        # recur with one node less
        self.children[node].insert(nodes, handler)


    def find(self, nodes):
        # if there are no more nodes to recur in, return the handler
        if len(nodes) == 0:
            return self.handler
        # node to recur into, and remove from nodes list
        node = nodes.pop(0)
        # if node doesn't exist, there is no such path, return None
        if node not in self.children:
            return None
        # recur with one node less
        return self.children[node].find(nodes)


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, node, handler):
        # Insert the node as before
        self.children[node] = RouteTrieNode(handler)


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, error_handler="Page not found"):
        # initialise variables, with input handler for RouteTrie()
        self.root = RouteTrie(handler)
        # error handler for non existing paths
        self.error_handler = error_handler


    def add_handler(self, path, handler):
        # split the path by '/', returned as a list of 'nodes'
        nodes = self.split_path(path)
        # recur in with a list of nodes, and the handler to add
        self.root.insert(nodes, handler)


    def lookup(self, path):
        # split path by '/', returned as a list of nodes
        nodes = self.split_path(path)
        # check if handler is empty, if empty, return error_handler
        output = self.root.find(nodes)
        if output:
            # return handler
            return output
        else:
            # return error_handler in __init__
            return self.error_handler


    def split_path(self, path):
        # check if it's root
        if path == '/':
            return []
        # it's not
        else:
            # check if trailing character exists
            if path[-1] == '/':
                # if yes, remove last character, and remove the first charater, which is also a '/'
                path = path[1:-1]
            else:
                # no trailing character, remove first '/'
                path = path[1:]
            # return a list of nodes
            return path.split('/')


# =================================================================================
#                                      Test one
# =================================================================================

print("=== Test one ===")

# create the router and add a route
router1 = Router("root handler", "not found handler")
router1.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print ("Pass" if  ("root handler" == router1.lookup("/")) else "Fail")
print ("Pass" if  ("not found handler" == router1.lookup("/home")) else "Fail")
print ("Pass" if  ("about handler" == router1.lookup("/home/about")) else "Fail")
print ("Pass" if  ("about handler" == router1.lookup("/home/about/")) else "Fail")
print ("Pass" if  ("not found handler" == router1.lookup("/home/about/me")) else "Fail")


# =================================================================================
#                                      Test two
# =================================================================================

print("=== Test two ===")

# create the router and add a route
router2 = Router("root handler")
router2.add_handler("/home/about", "about handler")  # add a route
router2.add_handler("/home/about/me/documents", "document handler")  # add a route
router2.add_handler("/user/apple", "apple handler")  # add a route

# some lookups with the expected output
print ("Pass" if  ("root handler" == router2.lookup("/")) else "Fail")
print ("Pass" if  ("Page not found" == router2.lookup("/home")) else "Fail")
print ("Pass" if  ("Page not found" == router2.lookup("/home/abou")) else "Fail")
print ("Pass" if  ("document handler" == router2.lookup("/home/about/me/documents/")) else "Fail")
print ("Pass" if  ("apple handler" == router2.lookup("/user/apple")) else "Fail")


# =================================================================================
#                                      Test three
# =================================================================================

print("=== Test Three ===")

# create the router and add a route
router3 = Router("root handler", "oops")
router3.add_handler("/objects/apple", "apple handler")  # add a route
router3.add_handler("/objects/apple/green", "green handler")  # add a route
router3.add_handler("/objects/banana", "banana handler")  # add a route

# some lookups with the expected output
print ("Pass" if  ("root handler" == router3.lookup("/")) else "Fail")
print ("Pass" if  ("oops" == router3.lookup("/home")) else "Fail")
print ("Pass" if  ("apple handler" == router3.lookup("/objects/apple/")) else "Fail")
print ("Pass" if  ("oops" == router3.lookup("/objects/aple/")) else "Fail")
print ("Pass" if  ("banana handler" == router3.lookup("/objects/banana/")) else "Fail")
