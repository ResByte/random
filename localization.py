#This is basic localization algorithm. form Udacity course 


colors1 = [['green', 'green',  'green' ],
          ['green', 'red',  'red'],
          ['green', 'green', 'green']]
colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements1 = ['red','red']
measurements = ['green', 'green', 'green' ,'green', 'green']

motions1 = [[0,0],[0,1]]
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
sensor_right = 1.0


p_move = 0.9


def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT


p = [[1.0 for i in range(len(colors[j-1]))] for j in range(len(colors))] 
#p[1][1]=1.0
#print p 
 
def sense(arr,Z):
	for i in range(len(colors)):
		for j in range(len(colors[i])):
			hit = (Z==colors[i][j])
			arr[i][j]=arr[i][j]*(hit*sensor_right+(1-hit)*(1-sensor_right))
def normalize(array):
	s=0
	for i in range(len(array)):
    		s= s+ sum(array[i])
	for i in range(len(array)):
    		for x in range(len(array[i])):
        		array[i][x]=array[i][x]/s
        return array

     
def motion(p,U,Z):
	q=[]
	for i in range(len(colors)):
		m=[]
		for j in range(len(colors[i])):
			hit = (Z==colors[i][j])
			if True :
				if U==[0,0]: 
#					print "no move"
					#pass
	#				print "no_move"
					s=p[i][j] 
#					print p[i][j]
					m.append(s)
				if U ==[0,1]:
					#right
#					print "right"
					#1=1%len(colors[])
					s=p[i][(j-U[1])%len(p[i])]*p_move
					s=s+p[i][(j-U[1]+1)%len(p[i])]*(1-p_move)	
					m.append(s)
#					print m
				if U ==[0,-1]:
#					print "left"
					s=p[i][(j-U[1])%len(p[i])]*p_move
					s=s+p[i][(j-U[1]-1)%len(p[i])]*(1-p_move)
					m.append(s)
#					
				if U ==[1,0]:
#					print "down"
					s=p[(i-U[0])%len(p)][j]*p_move
					s=s+p[(i-U[0]+1)%len(p)][j]*(1-p_move)
					m.append(s)				

				if U ==[-1,0]:
#					print "up"
					s=p[(i-U[0])%len(p)][j]*p_move
					s=s+p[(i-U[0]-1)%len(p)][j]*(1-p_move)
					m.append(s)
		q.append(m)	
	return q			
					

for i in range(len(measurements)):
#	print i
	normalize(p)
	#sense(p,measurements[i])
#	print p
	#p=normalize(p)
	#print p
#	print motions[i]
#	print measurements[i]
	p=motion(p,motions[i],measurements[i])
	
#	print "motion"
	
#	print p
	sense(p,measurements[i])
#	print p
	normalize(p)

#Your probability array must be printed 
#with the following code.

show(p)
