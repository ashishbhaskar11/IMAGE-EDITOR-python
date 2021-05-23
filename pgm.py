	# name: File path of the pgm image file
# Output is a 2D list of integers
def readpgm(name):
	image = []
	with open(name) as f:
		lines = list(f.readlines())
		if len(lines) < 3:
			print("Wrong Image Format\n")
			exit(0)

		count = 0
		width = 0
		height = 0
		for line in lines:
			if line[0] == '#':
				continue

			if count == 0:
				if line.strip() != 'P2':
					print("Wrong Image Type\n")
					exit(0)
				count += 1
				continue

			if count == 1:
				dimensions = line.strip().split(' ')
				print(dimensions)
				width = dimensions[0]
				height = dimensions[1]
				count += 1
				continue

			if count == 2:	
				allowable_max = int(line.strip())
				if allowable_max != 255:
					print("Wrong max allowable value in the image\n")
					exit(0)
				count += 1
				continue

			data = line.strip().split()
			data = [int(d) for d in data]
			image.append(data)
	return image	

# img is the 2D list of integers
# file is the output file path
def writepgm(img, file):
	with open(file, 'w') as fout:
		if len(img) == 0:
			pgmHeader = 'p2\n0 0\n255\n'
		else:
			pgmHeader = 'P2\n' + str(len(img[0])) + ' ' + str(len(img)) + '\n255\n'
			fout.write(pgmHeader)
			line = ''
			for i in img:
				for j in i:
					line += str(j) + ' '
				line += '\n'
			fout.write(line)

########## Function Calls ##########
x = readpgm('test.pgm')			# test.pgm is the image present in the same working directory
writepgm(x, 'test_o.pgm')		# x is the image to output and test_o.pgm is the image output in the same working directory
###################################

def Averaging_filter():
	avg=x[:] # Here we are making a clone of x so that we can make changes in that clone
	i = 0
	while i < len(avg) :
		j = 0
		while j < len(avg[i]) :   
			
			if i==0 or i==(len(avg)-1) or j==0 or j==(len(avg[i])-1):       #H is the number of rows in matrix x or avg which is [len(x)-1]
				j+=1 # do nothing or just continue
			
			else:
				avg[i][j]=((x[i-1][j-1]+x[i-1][j]+x[i-1][j+1]+x[i][j-1]+x[i][j]+x[i][j+1]+x[i+1][j-1]+ x[i+1][j]+x[i+1][j+1]))//9 # the pixel value at(i,j) will be equal to the average of the pixle value at the given 9 locations	
				j+=1
		i+=1
				
	writepgm(avg,'average.pgm')


def Edge_detection():
	# Edge detection along with zero padding and normalization
	def vdif(i,j): # as given in the assignment

		return ((x[i-1][j-1] - x[i+1][j-1]) + 2*(x[i-1][j] - x[i+1][j]) + (x[i-1][j+1] - x[i+1][j+1]))

	def hdif(i,j): # as given

		return ((x[i-1][j-1] - x[i-1][j+1]) + 2*(x[i][j-1] - x[i][j+1]) + (x[i+1][j-1] - x[i+1][j+1]))

	def grad(i,j): # as given

		return int((hdif(i,j)**2 + vdif(i,j)**2)**(0.5))
	
	edge=[[column for column in row] for row in x]  # copying the elements of x in edge here edge=x[:] does is not working and i dont know why this is happening it is giving overflowerror
	
	i = 0	
	while i < len(edge) :
		j=0
		while j < len(edge[i]) :
			if i == 0 or i == len(edge)-1 or j == 0 or  j == len(edge[i])-1:
				if i==0 and j==0:  # ZERO PADDING
					edge[i][j] = 0
					j+=1
				elif i==0 and j==(len(edge[i])-1):
					edge[i][j] = 0
					j+=1
				elif i==(len(edge)-1) and j==0:
					edge[i][j] = 0
					j+=1
				elif i==(len(edge)-1) and j==(len(edge[i])-1):
					edge[i][j] = 0
					j+=1	
				else:
					j+=1
					continue
			else:
				edge[i][j] = grad(i,j)
				j+=1
		i+=1
				
		# NORMALIZATION
	for i in range(len(edge)):
		for j in range(len(edge[i])):
			if i == 0 or i == len(edge)-1 or j == 0 or  j == len(edge[i])-1:
				continue
			else:	
				maximum=max(edge[i])
				edge[i][j]=(edge[i][j])*255//maximum
				
	writepgm(edge,'edge.pgm')
				
				
Averaging_filter()  # calling the functions
Edge_detection()