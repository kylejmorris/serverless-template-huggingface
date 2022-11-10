if __name__ == '__main__':
	import os
	# testing build args can be set via banana UI 
	if os.getenv("HF_AUTH_TOKEN") is None:
		print("no auth token found test failed")
		exit(0)
