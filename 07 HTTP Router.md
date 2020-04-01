# HTTPRouter using a Trie

* Implementing a HTTPRouter using a Trie data structure.
* The Trie will contain a part of the http path at each node, building from the root node `/`
* In addition to a path, a handler is added at a node, for the sake of simplicity

`class RouteTrie`
Time complexity for `def insert`
* O(M*N)

Time complexity for `def find`
* O(n)

`class RouteTrieNode`
Time complexity for `def insert`
* O(1)

`class Router`
Time complexity for `def add_handler`
* O(n)

Time complexity for `def lookup`
* O(n)

Time complexity for `def split_path`
* O(n)
