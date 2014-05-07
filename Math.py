
class Math():
	UNDEFINED = "undefined"
	INFINITE = "infinite"

	@classmethod
	def sum(cls,a,b):
		return a+b

	@classmethod
	def div(cls,a,b):
		if (a==0 and b==0):
			return Math.UNDEFINED
		if (b==0):
			return Math.INFINITE
		return a/b		