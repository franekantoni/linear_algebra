import math

def rounded(num):
    return round(float(num),7)

class Vector(object):

	#Creates a vector
	#assigns coordinates and dimension
	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple(coordinates)
			self.dimension = len(coordinates)

		except ValueError:
			raise ValueError("The coordinates must be not empty")

		except TypeError:
			raise TypeError("The coordinates must be an interable")

	#how the vector gets printed
	def __str__(self):
		return "Vector: {}".format(self.coordinates)

	#how the vector equality gets checked
	def __eq__(self, v):
		return self.coordinates == v.coordinates

	#adding two vectors
	def plus(self, v):
		return Vector(tuple([x+y for x, y in zip(self.coordinates, v.coordinates)]))

	#vector minus vector
	def minus(self, v):
		return Vector(tuple([round(float(x)-float(y),7) for x,y in zip (self.coordinates, v.coordinates)]))

	#multiplies vector by a scalar
	def scal(self, a):
		return Vector(tuple([x*a for x in self.coordinates]))

	#computes the magnitude of a vector
	def mag(self):
		return math.sqrt(sum([x*x for x in self.coordinates]))

	#normalizes the vector
	def normalized(self):
		try:
			magnitude = self.mag()
			return self.scal(1./magnitude)
		except ZeroDivisionError:
			raise Exception("Cannot divide by zero vector")

	#computes the dot product of two vectors
	def dot(self,v):
		return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

	#computes the angle betwen two vectors
	def angle(self, v, degrees=False):

		radiants = math.acos(self.cos(v))

		if degrees:
			return radiants * (180/math.pi)
		else:
			return radiants

	#check if two vectors are parallel
	def is_parallel(self, v):
		ratios = [round(x/y, 7) for x,y in zip(self.coordinates, v.coordinates)]
		return len(set(ratios)) == 1

	#checks if two vectors are orthogonal
	def is_orthogonal(self, v):
		return round(self.dot(v), 7) == 0.0 

	#computes the projecton of one vector onto another 
	def orthogonalized(self,v):
		try:
			dot_prod = self.dot(v)
			denominator = v.mag()*v.mag()
			return v.scal(dot_prod/denominator)
		except ZeroDivisionError:
			raise Exception("Cannot divide by zero vector")

	#computes the perpendicualr vectoż
	def perp(self,v):
		parallel = self.orthogonalized(v)
		return self.minus(parallel)

	def cos(self, v):
		try:
			dot_prod = self.dot(v)
			denominator = self.mag()*v.mag()
			return dot_prod/denominator
		except ZeroDivisionError:
			raise Exception("Cannot divide by zero vector")

	def cross_prd(self,v):
		if self.dimension == v.dimension == 3:
			w = self.coordinates
			v = v.coordinates
			x1 = w[1]*v[2] - v[1]*w[2]
			x2 = -(w[0]*v[2] - v[0]*w[2])
			x3 = w[0]*v[1] - v[0]*w[1]
			return Vector((x1, x2, x3))
		else:
			raise Exception("Cross product can only be computed for 3d vectors")

	def parall_area(self, v):
		cp = self.cross_prd(v)
		return round(cp.mag(),7)

	def parall_triangle(self, v):
		return round(self.parall_area(v)*0.5,7)
