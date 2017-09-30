import os
from PIL import Image
#imazeResizer by Rakes Prasad
# ver 1.0 Dated 30/sep/2017

# image extension *.png,*.jpg
# Note to users. Read This First
# This software is developed by Rakes Prasad @ Genext Software for use in Genext Cyber Cafe
# Code written in python and threfore platform independent
# please rename the filename to pp.jpg or ss.jpg for further processing.ANTIALIAS
# Serach for an directory named GenextImage for target files
# Choose 'c' for Customization or Choose 'd' for defalt output resize samples.ANTIALIAS
# please use small letters for filename or for command in software ,otherwise it will show errors
# thanks for reading and using the softwre.


source = ['/home/rakes/Desktop']
target_dir = '/home/rakes/Desktop/GenextImage'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)


print ("For a customized size press c")
print ("For default  sizes press d")



running = True
while running:
    choice = raw_input("Enter your choice c/d:")
    if choice == 'c':

        try:
            img = Image.open('/home/rakes/Desktop/pp.jpg')

            new_width  = int(raw_input('Enter Width of pp : '))
            new_height = int(raw_input('Enter height of pp  : '))
            new_quality = int(raw_input('Enter quality of pp in percentage :  '))


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save('/home/rakes/Desktop/GenextImage/newPhoto.jpg',quality = new_quality)
        except IOError:
            pass
            print ("There is no such pp.jpg found")


        try:
            img = Image.open('/home/rakes/Desktop/ss.jpg')
            new_width  = int(raw_input('Enter Width of ss : '))
            new_height = int(raw_input('Enter height of ss  : '))
            new_quality = int(raw_input('Enter quality of ss in percentage :  '))


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save('/home/rakes/Desktop/GenextImage/newSign.jpg',quality = new_quality)
        except IOError:
            pass
            print ("There is no such sn.jpg found")


        print ("Done")
        running =False

    elif choice == 'd':
        try:
            img = Image.open('/home/rakes/Desktop/pp.jpg')

                        # copy this code form here for another sample
                        # this is 100 *120 *90(quality of picture)
            new_width  = 100
            new_height = 120


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save('/home/rakes/Desktop/GenextImage/100*120(90%) .jpg',quality = 90)

                        # and paste after it with new arguments.
                        # this is 100*120*100%
            new_width  = 100
            new_height = 120


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save('/home/rakes/Desktop/GenextImage/100*120(100%) .jpg',quality = 100)

                    # this is 100*120*75%

            new_width  = 100
            new_height = 120


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save('/home/rakes/Desktop/GenextImage/100*120(75%) .jpg',quality = 75)



        except IOError:
            pass
            print ("There is no such pp.jpg found")

        # this is end of samples and starting of loops.
        print ('Done')
        running = False

# This section for signature part

        try:
            img = Image.open('/home/rakes/Desktop/ss.jpg')
#sample1
            new_width  = 140
            new_height = 60


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save('/home/rakes/Desktop/GenextImage/sn140*60(75%) .jpg',quality = 75)

#sample2
            new_width  = 140
            new_height = 60


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save('/home/rakes/Desktop/GenextImage/sn140*60(90%) .jpg',quality = 90)

#sample3
            new_width  = 140
            new_height = 60


            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save('/home/rakes/Desktop/GenextImage/sn140*60(100%) .jpg',quality = 100)


        except IOError:
            pass
            print ("There is no such ss.jpg found")



    else:
        print("Try Again !Enter either c or d in small letters only - ")

else:
    print("Everything is OK")


