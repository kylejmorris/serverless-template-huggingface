if __name__ == '__main__':
	import os
	# testing build args can be set via banana UI 
	if os.getenv("HF_AUTH_TOKEN") is None:
		print("found auth token test failed!")
		import paoiasjdf # force an error to throw to bail out early
