class ArrayQueue:
	""" FIFO queue implementation using a Python list as underlying storage """
	DEFAULTY_CAPACITY = 1

	def __init__ (self):
		""" create an empty queue """
		self._data = [None] * ArrayQueue.DEFAULTY_CAPACITY
		self._size = 0
		self._front = 0

	def len(self):
		""" Return the number of elements in the queue """
		return self._size

	def capacity(self):
		return len(self._data)

	def is_empty(self):
		""" Return True if the queue is empty """
		return self._size == 0

	def first(self):
		""" Return (not remove) the element at the fron of the queue
		"""
		if self.is_empty():
			print('Queue is empty')
		else:
			return self._data[self._front]

	def dequeue(self):
		""" Remove and return the front element of the queue		
		"""

		if self.is_empty():
			print('Queue is empty')
		else:			
			answer = self._data[self._front]
			self._data[self._front] = None
			self._front = (self._front + 1) % len(self._data)
			self._size -= 1
			if 0 < self._size < len(self._data) // 4:
				self._resize(len(self._data) // 2)
			return answer

	def enqueue(self, e):
		""" Add an element to the back of queue """

		if self._size == len(self._data):				# if queue elements == queue capacity, allow queue capacity to grow 2* present capacity
			self._resize(2 * len(self._data))
		avail = (self._front + self._size) % len(self._data)
		self._data[avail] = e
		self._size += 1

	def _resize( self, cap):
		""" Resize to a new list of capacity >= len(self) """

		old = self._data
		self._data = [None] * cap
		walk = self._front
		for k in range(self._size):
			self._data[k] = old[walk]
			walk = (1 + walk) % len(old)
		self._front = 0

	def display(self):
		print self._data