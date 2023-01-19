__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from zipfile import ZipFile
from os import path
import os


def clean_cache():
	cache = path.join(path.dirname(__file__), "cache")
	if not (path.exists(cache)):
		os.mkdir(cache)
	else:
		for file in os.listdir(cache):
			os.remove(path.join(cache, file))


def cache_zip(zip_file, cache_dir):
	with ZipFile(zip_file, "r") as open_zip:
		open_zip.extractall(cache_dir)


def cached_files():
	r_list = []
	cache = path.join(path.dirname(__file__), "cache")
	for file in os.listdir(cache):
		file = path.join(cache, file)
		if path.isfile(file):
			r_list.append(file)
	return (r_list)


def find_password(list_files):
	for file in list_files:
		with open(file, 'r') as open_file:
			content = open_file.read()
			if (content.find('password') != -1):
				content = content.split('\n')
				for line in content:
					if (line.startswith('password: ')):
						return (line.replace('password: ', ''))
	
