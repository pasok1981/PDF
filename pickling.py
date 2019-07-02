import pickle
import json

def write_pickle(filename_, data_):
	try:
		with open(filename_, 'wb') as out:
			pickle.dump(data_, out)
			out.close()
	except IOError as er:
		print(er)


def read_pickle(filename_):
	try:
		with open(filename_, 'rb') as infile:
			retrieved = pickle.load(infile)
			infile.close()
	except IOError as e:
		raise e 

	return retrieved

def write_json(filename_, data_):
	try:
		with open(filename_, 'w', encoding='utf-8') as out:
			json.dump(data_, out, indent=2)
			out.close()	
			print("Written to file {}".format(filename_))
	except IOError as er:
		raise er

def read_json(_filename):
	try:
		with open(_filename, 'r', encoding='utf-8') as infile:
			data = json.load(infile)
			if(data):
				return dict(data)	
			else:
				raise RuntimeError
	except IOError as er:
		raise er