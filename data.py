

# Reserved for imports

class Data:
	def __init__(self, name, label_names, data):
		self.name = name                            # type = string
		self.number_of_instances = None             # type = int
		self.features = None                        # type = model_data
		self.labels = None                          # type = model_data
		self.label_names = None                     # type = list of string
		self.raw_data = data                        # type = pandas dataframe
	# Creates features and labels from raw_data
	def processRawData(self):
		pass
	class model_data:
		def __init__(self):
			self.test = None                        # type = pandas dataframe
			self.train = None                       # type = pandas dataframe
# Downloads the dataset from the given url
def download_data(url):
	pass