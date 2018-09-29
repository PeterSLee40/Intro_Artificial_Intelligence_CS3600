# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()



def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    startStack = util.Stack()
    startStack.push([problem.getStartState()])
    return dfs_recursive(problem, startStack, set(), {})
#recursive helper function, has problem, current stack, and visited as params
def dfs_recursive(problem, stack, visited, parents):
    current = stack.pop()
    if current[0] in visited:
        return dfs_recursive(problem, stack, visited, parents)
    if problem.isGoalState(current[0]):
        trace = []
        while (current[0] is not problem.getStartState()):
            trace.append(current[1])
            current = parents.get(current)
            print current
        return trace[::-1]
    if current[0] not in visited:
        visited.add(current[0])
        for child in problem.getSuccessors(current[0]):
            stack.push(child)
            if child not in parents:
                parents[child] = current
    return dfs_recursive(problem, stack, visited, parents)

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    startstate = problem.getStartState()
    visited = []
    q = util.Queue()
    q.push((startstate, []));
    
    while not q.isEmpty():
        state, direction = q.pop()
        if problem.isGoalState(state):
            return direction
        if not state in visited:
            for child, delta, dist in problem.getSuccessors(state):
                if child in visited:
                    continue
                if not child in visited: 
                    newDir = direction + [delta]
                    q.push((child, newDir))
        visited.append(state)
def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    visited = set()
    priorityQ = util.PriorityQueue()
    weightSet = dict()
    weightSet[start] = 0
    priorityQ.push([start], 0)
    parents = {start:None}
    
    #priorityMap.append(problem.getStartState(), 0)
    while not priorityQ.isEmpty():

        current = priorityQ.pop()
        weight = weightSet[current[0]]
        if current[0] not in visited:
            visited.add(current[0])
            if (problem.isGoalState(current[0])):
                trace = []
                while (current[0] is not problem.getStartState()):
                    trace.append(current[1])
                    current = parents.get(current)
                return trace[::-1]
            for child in problem.getSuccessors(current[0]):
                if child[0] not in visited:
                    parents[child] = current
                    weightSet[child[0]] = weight + child[2]
                    priorityQ.push(child, weight + child[2])
        #visited.add(current[0])
        
            '''if ((weight + 1) < priorityMap[child[0]]):
                priorityMap.append(child[0], weight + 1)
                priorityQueue.push(child, weight + 1)
                parents[child] = current'''

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    openSet = util.PriorityQueue()
    openSet.push(start, heuristic(start, problem))
    blank = []
    openSet = util.PriorityQueue()
    startcost = heuristic(start, problem)
    openSet.push((start, blank), startcost)
    visited = blank
    
    while not openSet.isEmpty():
        current, pastmoves = openSet.pop()
        if current in visited:
            continue
        if problem.isGoalState(current):
            return pastmoves
        if current not in visited:
            for child, delta, dist in problem.getSuccessors(current):
                newmoves = pastmoves + [delta]
                cost = problem.getCostOfActions(newmoves)
                if child not in visited:
                    f = heuristic(child, problem) + cost
                    openSet.push((child, newmoves), f)
            visited.append(current)

    
# Abbreviations

bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
