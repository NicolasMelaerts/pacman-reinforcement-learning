# featureExtractors.py
# --------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"Feature extractors for Pacman game states"

from game import Directions, Actions
import util

class FeatureExtractor:  
  def getFeatures(self, state, action):    
    """
      Returns a dict from features to counts
      Usually, the count will just be 1.0 for
      indicator functions.  
    """
    util.raiseNotDefined()

class IdentityExtractor(FeatureExtractor):
  def getFeatures(self, state, action):
    feats = util.Counter()
    feats[(state,action)] = 1.0
    return feats

def closestFood(pos, food, walls):
  """
  closestFood -- this is similar to the function that we have
  worked on in the search project; here its all in one place
  """
  fringe = [(pos[0], pos[1], 0)]
  expanded = set()
  while fringe:
    pos_x, pos_y, dist = fringe.pop(0)
    if (pos_x, pos_y) in expanded:
      continue
    expanded.add((pos_x, pos_y))
    # if we find a food at this location then exit
    if food[pos_x][pos_y]:
      return dist
    # otherwise spread out from the location to its neighbours
    nbrs = Actions.getLegalNeighbors((pos_x, pos_y), walls)
    for nbr_x, nbr_y in nbrs:
      fringe.append((nbr_x, nbr_y, dist+1))
  # no food found
  return None

class SimpleExtractor(FeatureExtractor):
  """
  Returns simple features for a basic reflex Pacman:
  - whether food will be eaten
  - how far away the next food is
  - whether a ghost collision is imminent
  - whether a ghost is one step away
  """
  
  def getFeatures(self, state, action):
      # Extract the grid of food, wall locations, and get the ghost locations
      food = state.getFood()
      walls = state.getWalls()
      ghosts = state.getGhostStates()  # Get ghost states to check if they are scared (comestible)

      features = util.Counter()

      features["bias"] = 1.0

      # Compute the location of pacman after he takes the action
      x, y = state.getPacmanPosition()
      dx, dy = Actions.directionToVector(action)
      next_x, next_y = int(x + dx), int(y + dy)

      # vérifie s'il y a un ghost à 1-step
      features["#-of-ghosts-1-step-away"] = sum((next_x, next_y) in Actions.getLegalNeighbors(g.getPosition(), walls) for g in ghosts)

      # priorité à manger un ghost
      features["eat-scared-ghost"] = 0.0
      for ghost in ghosts:
          if ghost.scaredTimer > 0:   # vérification que le ghost est effrayé
              dist_to_ghost = util.manhattanDistance((next_x, next_y), ghost.getPosition())
              if dist_to_ghost == 1:   # accessible à 1 step
                  features["eat-scared-ghost"] = 1.0 # Pacman mange le ghost

      # If there is no danger of ghosts, check if PacMan eats food
      if not features["#-of-ghosts-1-step-away"] and food[next_x][next_y]:
          features["eats-food"] = 1.0

      # Get the closest food feature
      dist = closestFood((next_x, next_y), food, walls)
      if dist is not None:
          features["closest-food"] = float(dist) / (walls.width * walls.height)

      if features["eat-scared-ghost"] == 1.0:
          features["eat-scared-ghost-priority"] = 10.0   # gros poids pour manger un fantême

      # Normalize features for stability
      features.divideAll(10.0)
      return features



