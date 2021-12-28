# Object Oriented Course - Task 3: Graphs in Python
The theme of the project is  Design and implementation of directed and weighted graphs in Python.

![‏‏לכידה](https://user-images.githubusercontent.com/73783656/147393321-648d1d74-4257-4500-bd18-f31b6b95fd5e.JPG)


## Authors

- [@dvir borochov](https://github.com/dvirbo)
- [@yuval shabat](https://github.com/yuvili)

## Features
- Build a directed weighted graph.
- Create, add and remove vertices.
- Create, add and remove edges.
- Load a graph from a json file.
- Saves the graph to a json file.
- Run algorithms on a directed weighted graph.
- Graph display using matplotlib

## Main algorithm's
GraphAlgo represents a Graph Theory algorithms, and is an implementation of the GraphAlgoInterface interface.
This class is based on 3 main variables:
- `graph` DiGraph (empty if the input in None)
- `distances` - dictionary containing the distances(float) and paths(List) of the graph's nodes
- `connected` - variable to determine if the graph is connected. (-1) - if wasn't checked yet, (0) - if not, (1) if the graph is connected.

 methods of the interface:
- _**get_graph:**_ returns `graph`
- _**shortest_path**_: Using the Dijkstra's algorithm, this function returns the shortest path of 2 given nodes (List), and it's distance(float).
Before the function will "dive in" the algorithm, it checks first if the requested value is located in `distances`. If not, the function will go over
the graph's node till it reaches the destination node. In case there isn't a path between the input nodes, the function will return to the user `inf []`.
The other main usage of this function is updating `distances`.
- _**centerPoint**_: Finds the node which minimizes the max distance to all the other nodes, by looping through the graph's nodes, extracting 
the max distance of the node and returning the node with the lowest max distance. This function will check first if the 
graph is connected using `connected` and the *is_connected* function. If the graph 
is not connected, this function will return `-1, inf`.
- _**TSP**_: Computes a list of consecutive nodes which go over all the nodes in a given List, and returns the path (List)
and the path's distance (float). In case a path wasn't found, it will return `inf []`.
- _**save_to_json**_: save your graph in JSON format.
- _**load_from_json**_: load a graph from a JSON format.
- _**plot_graph**_: Plots the graph.

 Algorithms and functions the program uses in the above methods:
 - _**lowest_dist**_: returns the node that wasn't used yet with the lowest distance to the source node. Used by *shortest_path*.
 - _**Dijkstra_algorithm_path**_: Calculates the shortest route.
 - _**is_connected**_: checks if `graph` is strongly connected and there is a valid path from each node to each other node.
 - _**DFS**_: Depth-first search, used by *is_connected*
  
   





## Tests:
 using unittest we check the two classes that implement TestCase:
* TestDiGraph: check all the methods that given in GraphInterface to see the accuracy of the code.
 * TestGraphAlgo: check all the methods that given in GraphAlgoInterface to see the accuracy of the code




  








## Download and run The Project:
 to run the project, install the above packages:

    pandas Version 1.3.4 (or higher), matplotlib Version 3.4.3 (or higher).
Download the project and export it by the above actions:

    Click Code (Green Button) ->  Download ZIP -> Choose Extract to Folder in Zip -> Run: Main.py





## Docs:
* information and auxiliary departments for this task can be found at this link: https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex3
* intro to matplotlib: https://colab.research.google.com/github/makeabilitylab/signals/blob/master/Tutorials/IntroToMatplotlib.ipynb#scrollTo=MzNLMwO6dhl7 

 