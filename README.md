# IMAGE-EDITOR-python

This is a simple image editor which performs a few basic tasks on an input image. 

# The particular tasks that it will perform includes - 
1. Averaging
2. Performing Edge Detection
3. Finding the Path of least energy


Given an image we will first read the image into an array, perform some basic operations
and generate the output image. 

* Image files will be in pgm (portable graymap format). 
* These image files have the following specifications. 
- When you open images in pgm format using any text editor, you will see the following.
- The first line contains an identifier for the image which for this assignment will be P2. 
- The next line contains dimension of the image with two numbers indicating the width and the height respectively.
-  Next number specifies the maximum allowed pixel value of the image, for this assignment it will be 255. 
-  Next we have the actual pixel values of the image given in row major ordering. That is the first
   pixel value corresponds to location (0,0), the second for location (0, 1) and so on. For all pixels in the
   image, we have their value between 0 and 255. 
- The number of pixel values equals width (W) times height (H) of the image.

# Functions will perform the following tasks. 

# 1. Averaging filter:
  Create an image of the size WxH using an array of integers. Pixel value at location (i,j) of the image equals the
  average of the pixel values at locations (i − 1, j − 1), (i − 1, j), (i − 1, j + 1),(i,j−1),(i,j),(i,j+1),(i+1,j−1),(i+1,j),(i+1,j+1) of the input image. 
  
  Formally pixel value at location (i, j) is
  (image[i-1][j-1]+image[i-1][j]+image[i-1][j+1]+image[i][j1]+image[i][j]+image[i][j+1]+image[i+1][j-1]+ image[i+1][j]+image[i+1][j+1])/9 
  
# 2. Edge detection:
  The idea here is to compute some function of pixel values among neighbouring cells in horizontal and vertical directions. 
  This function approximates how close these pixel values are relative to each other. If pixel values in a neighbourhood are 
  similar, then this function value would be very small or 0 where as if there is a significant change in neighbourhood pixel
  values, then this function would have non-zero values. We detect presence of an edge by noticing how this function value changes. 
  The above is for intuition on how this works. Follow the steps mentioned below to detect edges of an image and output image to 
  ‘edge.pgm’ file.
  - Compute values of grad(i,j) = sqrt(hdif(i, j)*hdif(i,j) + vdif(i, j)*vdif(i,j)) for all i, j in the image,
    where hdiff and vdiff are the horizontal and vertical gradients and are computed as follows:
   # hdif(i,j) = (image[i-1][j-1]-image[i-1][j+1]) + 2(image[i][j-1]-image[i][j+1]) + (image[i+1][j-1]- image[i+1][j+1])
   # vdif(i,j) = (image[i-1][j-1]-image[i+1][j-1]) + 2(image[i-1][j]-image[i+1][j]) + (image[i-1][j+1]- image[i+1][j+1]) 
  
# 3. Path of least energy:
  This part of the assignment requires you to implement an algorithm that finds a path from top of the image to the bottom, 
  which has the least energy. Consider that your edge image as computed above gives the energy image. Now you have to compute 
  the path of minimum energy and color that path with white (or 255 value). Start from the top row of the image and compute 
  the energy of the pixels for the next row as follows. Please note that for the top row the pixels of MinEnergy image will 
  have the same value as edge image.

  # MinEnergy(i,j) = edge(i,j) + min(MinEnergy(i-1,j-1), MinEnergy(i-1,j), MinEnergy(i-1,j+1))
  
  
  
  
