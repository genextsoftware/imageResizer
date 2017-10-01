import os
from PIL import Image

#imazeResizer by Rakes Prasad
# ver 2.0 Dated 01/oct/2017    Read This First...

# image extension *.png,*.jpg supported

# Code written in python
# please rename the filename to pp.jpg or ss.jpg for further processing.
# Serach for an directory named GenextImage for target files.
# For batch processing please keep all of your images in 'rawImage ' folder
# Choose 'b' for batch image processing ,'c' for Customization or Choose 'd' for defalt output resize samples
# please use small letters for filename or for command in software ,otherwise it will show errors
# thanks for reading and using the softwre.


target_dir = '/home/rakes/Desktop/GenextImage'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

target_dir1 = '/home/rakes/Desktop/rawImage'
if not os.path.exists(target_dir1):
    os.mkdir(target_dir1)




path1 = r'/home/rakes/Desktop/pp.jpg'
path2 = r'/home/rakes/Desktop/GenextImage/newPhoto.jpg'
path3 = r'/home/rakes/Desktop/ss.jpg'
path4 = r'/home/rakes/Desktop/GenextImage/newSign.jpg'
path5 = r'/home/rakes/Desktop/GenextImage/10012090.jpg'
path6 = r'/home/rakes/Desktop/GenextImage/100120100.jpg'
path7 = r'/home/rakes/Desktop/GenextImage/10012075.jpg'
path8 = r'/home/rakes/Desktop/GenextImage/sn1406075.jpg'
path9 = r'/home/rakes/Desktop/GenextImage/sn1406090.jpg'
path10 = r'/home/rakes/Desktop/GenextImage/sn14060100.jpg'


directory1 = 'rawImage'
directory2 = 'GenextImage'


print ("For a customized size press c")
print ("For default  sizes press d")



running = True
while running:
    choice = raw_input("Enter your choice c/d:")

    if choice == 'c':
                    # this is to customize photo section
        try:
            img = Image.open(path1)

            new_width  = int(raw_input('Enter Width of pp : '))
            new_height = int(raw_input('Enter height of pp  : '))
            new_quality = int(raw_input('Enter quality of pp in percentage :  '))


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save(path2,quality = new_quality)
        except IOError:
            pass
            print ("There is no such pp.jpg found")


        try:
                        #this is to customize signature section
            img = Image.open(path3)
            new_width  = int(raw_input('Enter Width of ss : '))
            new_height = int(raw_input('Enter height of ss  : '))
            new_quality = int(raw_input('Enter quality of ss in percentage :  '))


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save(path4,quality = new_quality)
        except IOError:
            pass
            print ("There is no such sn.jpg found")


                # this deals with batch file customization
        try:
            if not os.listdir(directory1):
                print('Folder rawImage is empty')
                break

            new_percent = int(raw_input('Enter percentage (1-100) for batch file images: '))
            new_quality = int(raw_input('Enter quality of picturs of batch file images: '))

            for image in os.listdir(directory1):
                print('Resizing image ' + image)



                img = Image.open(os.path.join(directory1,image))


                new_width  = int(img.size[0]* new_percent/100)
                new_height =int(img.size[1] * new_percent/100)
                new_quality = 70

                img = img.resize((new_width,new_height),Image.ANTIALIAS)
                img.save(os.path.join(directory2,image),quality = new_quality)

        except OSError:
            pass
            print ("There is no such folder rawImage found or it contains no images")


        print ("Done")
        running =False

    elif choice == 'd':
        try:
            img = Image.open(path1)

                        # copy this code form here for another sample
                        # this is 100 *120 *90(quality of picture)
            new_width  = 100
            new_height = 120


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save(path5,quality = 90)

                        # and paste after it with new arguments.
                        # this is 100*120*100%
            new_width  = 100
            new_height = 120


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save(path6,quality = 100)

                    # this is 100*120*75%

            new_width  = 100
            new_height = 120


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save(path7,quality = 75)



        except IOError:
            pass
            print ("There is no such pp.jpg found")

        # this is end of samples and starting of loops.
        print ('Done')
        running = False

# This section for signature part

        try:
            img = Image.open(path3)
#sample1
            new_width  = 140
            new_height = 60


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save(path8,quality = 75)

#sample2
            new_width  = 140
            new_height = 60


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save(path9,quality = 90)

#sample3
            new_width  = 140
            new_height = 60


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save(path10,quality = 100)


        except IOError:
            pass
            print ("There is no such ss.jpg found")



            # this block is for default batch file processing with 40% resized
            # this also maintains defalt aspect ratio or raw images
            # to change the percentage please keep decimals to both variables same
            # this is to done for keeping aspect ratio unaltered
        try:
            if not os.listdir(directory1):
                print('Folder rawImage is empty')
                break

            for image in os.listdir(directory1):
                print('Resizing image ' + image)

                img = Image.open(os.path.join(directory1,image))
                print(img.size)

                new_width  = int(float(img.size[0])*0.40)
                new_height =int(float(img.size[1])*0.40)
                new_quality = 70

                img = img.resize((new_width,new_height),Image.ANTIALIAS)
                img.save(os.path.join(directory2,image),quality = new_quality)

            print ("Done")


            print ('Batch processing complete')

        except OSError:
            pass
            print ("There is no such folder found named rawImage ,please recheck")



    else:
        print("or Enter either b or c or d in small letters only - Please Try Again !")

else:
    print("Everything is OK")





# This software is developed by Rakes Prasad @ Genext Software for use in Genext Cyber Cafe
# Email id : genextsoftware@gmail.com