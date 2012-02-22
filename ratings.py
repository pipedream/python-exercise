import numpy as np

class ratings(object):
 """ratings"""

 def __init__(self, inputdict):
  self._data = inputdict
  self.get_person_ids()
  self.get_paper_ids()
  self.get_ratings_array()

 def get_ratings_array(self):
  self.myratings = np.zeros((len(self.persons),len(self.papers)), dtype = float)
  for person in self.persons:
   for paper in self._data[person].keys():
    self.myratings[self.persons.index(person),self.papers.index(paper)] = self._data[person][paper]

 def get_person_ids(self):
  self.persons = self._data.keys()
  self.persons.sort()

 def get_paper_ids(self):
  self.papers = []
  for person in self.persons:
   for paper in self._data[person].keys():
    if paper not in self.papers:
     self.papers.append(paper)
  self.papers.sort()

 def recommendations():
  return None
  # calculate and return recommendations


