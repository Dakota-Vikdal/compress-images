In this script file I created an image converter in order to convert .jpg images to .png images. 

First the sys module was used in order to grab arguments from the command line(In this case the arguments are image folders). 

Next I created a new folder that will hold the newly converted .png images by utilizing the os method of path.exists in conjunction with the mkdir method. 

I then utilized the os module, in particular the listdir method, in order to turn the .jpg folders contents into a list(for looping purposes). 

Lastly, I looped over the .jpg image folder, used the os method of splitext in order to seperate .jpg from the base text of the file(this was done so the files can be converted to png), and finally converted the images into .png format and sent those newly converted images into the new folder.

Thanks for reading!