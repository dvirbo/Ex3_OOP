# Object Oriented Course - Task 3: Graphs in Python
The theme of the project is  Design and implementation of directed and weighted graphs in Python.

![‏‏לכידה](https://user-images.githubusercontent.com/73783656/147393321-648d1d74-4257-4500-bd18-f31b6b95fd5e.JPG)


## Authors

- [@dvir borochov](https://github.com/dvirbo)
- [@yuval shabat](https://github.com/yuvili)
## Main algorithm's
 methods of the interface:
- create a graph (it's optional to add vertexes and edges)
- init: Init the graph on which this set of algorithms operates on
- shortestPath: returns list of nodes of the shortest path between source vertex to destination vertex consider the weight of each edge.
- centerPoint: Finds the node which minimizes the max distance to all the other nodes.
- tsp: Computes a list of consecutive nodes which go over all the nodes in cities.
- save: save your graph in JSON format.
- load: load a graph from a JSON format.
- plot_graph: Plots the graph.

 algorithms that we buit to help us implements the methods of the intreface:
 - lowest_dist: calculate the lowest dist between two given nodes.
 - Dijkstra_algorithm_path: Find the shortest route for any pair node,
 - Isconected: check if the graph is strongly connected (there is a valid path from each node to each other node).
 - DFS:Depth-first search
  
   





## Tests:
 using unittest we check the two classes that implement TestCase:
* TestDiGraph: check all the methods that given in GraphInterface to see the accuracy of the code.
 * TestGraphAlgo: check all the methods that given in GraphAlgoInterface to see the accuracy of the code




  








## Download and run The Project:
 to run the project, install the above packages:

    pandas Version 1.3.4 (or higher), matplotlib Version 3.4.3 (or higher).
Download the project and export it by the above actions:

    Click Code (Green Button) ->  Download ZIP -> Choose Extract to Folder in Zip -> Run: Main.py





## Doces:
* information and auxiliary departments for this task can be found at this link: https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex3
* intro to matplotlib: https://colab.research.google.com/github/makeabilitylab/signals/blob/master/Tutorials/IntroToMatplotlib.ipynb#scrollTo=MzNLMwO6dhl7 

 
