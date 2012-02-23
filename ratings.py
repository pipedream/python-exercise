import numpy as np

class ratings(object):
 """ratings"""

 def __init__(self, inputdict):
  self._data = inputdict
  self.get_person_ids()
  self.get_paper_ids()
  self.get_ratings_array()

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

 def get_ratings_array(self):
  self.myratings = np.zeros((len(self.persons),len(self.papers)), dtype = float)
  for person in self.persons:
   for paper in self._data[person].keys():
    self.myratings[self.persons.index(person),self.papers.index(paper)] = self._data[person][paper]

 def compare_ratings(person1, person2):
	# only check non-zero ratings
	indices = np.where(self.myratings[person1] != 0) or np.where(self.myratings[person2] != 0)
	if len(indices) == 0: return len(self.papers)*25+1 #5 is max difference;no basis to compare
	cmp1 = self.myratings[person1][indices]
	cmp2 = self.myratings[person2][indices]
	return np.linalg.norm(self.myratings[cmp1] - self.myratings[cmp2])

 def recommendations(self):
  allrecommendations = {}
  for person in self.persons:
        minimum = len(self.papers)*25+1
        for otherperson in self.persons:
		if otherperson == person: break;
        	tmp = compare_ratings(person, otherperson)
        	if tmp < minimum:
        		closest = otherperson
        		minimum = tmp
  	notread = np.where(np.array(self.myratings[self.persons.index(otherperson)] == 0))
	print self.myratings
	print self.persons.index(otherperson)
	print notread
  	maxindex = np.where(self.myratings[self.persons.index(otherperson)][notread] == self.myratings[self.persons.index(otherperson)][notread].max())
  	allrecommendations[person] = self._data[otherperson][maxindex]
  return allrecommendations

# Alternative distances:
# pearson
# tanimoto scipy.spatial.distance.rogerstanimoto

