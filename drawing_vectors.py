GlowScript 2.7 VPython

make_grid()

mag_degrees(3,0,color.red)
mag_degrees(3,150,color.green)

#Testing inverse line creation

#Using negative angles

mag_degrees(3,90,color.orange)
mag_degrees(3,-90,color.orange)
mag_degrees(3,270,color.red)

#Using negative magnitude

mag_degrees(-3,80,color.purple)
mag_degrees(3,80,color.purple)
mag_degrees(3,260,color.red)

#Adding 180 to angles

mag_degrees(3,20,color.blue)
mag_degrees(3,200,color.blue)
mag_degrees(3,380,color.red)


### Don't change anything below here! ###

def make_grid():
  scene.background = color.white
  thickness = 0.02
  dx = 1
  xmax = 5
  x = -xmax
  while (x <= xmax):
    y = -xmax
    gridline = curve(pos=[vector(x,y,-thickness)],color=color.black,radius=thickness)
    while (y <= xmax):
      gridline.append(vector(x,y,-thickness))
      y = y + dx
    x = x + dx
  y = -xmax
  while (y <= xmax):
    x = -xmax
    gridline = curve(pos=[vector(x,y,-thickness)],color=color.black,radius=thickness)
    while (x <= xmax):
      gridline.append(vector(x,y,-thickness))
      x = x + dx
    y = y + dx
  return

def mag_degrees(mag,degrees,color):
  # Call make_vector with instructions to specify magnitude and angle.
  sleep(1)
  vec = make_vector("mag-degrees",mag,degrees,color)
  return vec

def x_y(xcomp,ycomp,color):
  # Call make_vector with instructions to specify components.
  sleep(1)
  vec = make_vector("x-y",xcomp,ycomp,color)
  return vec

def start_end(start,end,color):
  # Call make_vector with instructions to specify starting and ending points.
  sleep(1)
  vec = make_vector("start-end",start,end,color)
  return vec

def make_vector(instruction,in1,in2,color):
  if (instruction=="mag-degrees"):
    # Read inputs as magnitude and angle.
    mag = in1
    angle = in2
    # Calculate x- and y-components.
    xcomp = mag*cos(angle*pi/180)
    ycomp = mag*sin(angle*pi/180)
    # Set start and end points.
    start = vector(0,0,0)
    end = vector(xcomp+start.x,ycomp+start.y,0)
  else if (instruction=="x-y"):
    # Read inputs as x- and y-components.
    xcomp = in1
    ycomp = in2
    # Calculate magnitude and angle. 
    mag = (xcomp**2+ycomp**2)**0.5
    angle = atan(ycomp/xcomp)*180/pi
    # Set start and end points.
    start = vector(0,0,0)
    end = vector(xcomp+start.x,ycomp+start.y,0)
  else if (instruction=="start-end"):
    # Read inputs as start and end points.
    start = vector(in1[0],in1[1],0)
    end = vector(in2[0],in2[1],0)
    # Calculate x- and y-components. 
    xcomp = end.x-start.x
    ycomp = end.y-start.y
    # Calculate magnitude and angle. 
    mag = (xcomp**2+ycomp**2)**0.5
    angle = atan(ycomp/xcomp)*180/pi
  else:
    # Someone must have called this function without proper instructions. Display error message.
    print("error in make_vector! instructions not supplied")
    return

  vec = arrow(pos=start,axis=vector(xcomp,ycomp,0),color=color,shaftwidth=0.1)
  # All done!
  vec.xcomp = xcomp
  vec.ycomp = ycomp
  vec.mag = mag
  vec.degrees = angle
  vec.radians = angle*pi/180
  vec.start = start
  vec.end = end
  
  return vec
