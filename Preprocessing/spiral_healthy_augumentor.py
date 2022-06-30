# Author - ikurious
# Use this as boiler plate to make augumented training and testing image dataset

from  tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import os

cur_dir = os.getcwd() 

data = ImageDataGenerator(
                rotation_range= 40,
                horizontal_flip= True,
                fill_mode = 'nearest'
)

img_path = os.path.join(cur_dir,'Original_data/spiral/healthy')
img_list = os.listdir(img_path)



augumented_folder = os.path.join(cur_dir,'spiral_Augument')

if not os.path.exists(augumented_folder):
    os.makedirs(augumented_folder)

for images in img_list:

    string = 'healthy_'+images
    name = os.path.splitext(string)[0] 


    cur_img_path = os.path.join('Original_data/spiral/healthy/',images)
    print(name)


    img = load_img(cur_img_path)
    img_array = img_to_array(img)
    img_array = img_array.reshape((1,) + img_array.shape)

    augumented_train_images = 1
    augumented_test_images = 1

    augumented_train = os.path.join(cur_dir, 'spiral_Augument/healthy/')
    print(augumented_train)
    if not os.path.exists(augumented_train):
        os.makedirs(augumented_train)

    # augumented_test = os.path.join(cur_dir, 'spiral/healthy/')
    # if not os.path.exists(augumented_test):
    #     os.makedirs(augumented_test)

    for batch in data.flow(img_array, batch_size=1, save_to_dir= augumented_train, save_prefix=name, save_format='jpg'):
        augumented_train_images += 1
        if augumented_train_images > 300 :
            break
    
    # for batch in data.flow(img_array, batch_size=1, save_to_dir= augumented_test, save_prefix=name, save_format='jpg'):
    #     augumented_test_images += 1
    #     if augumented_test_images > 15 :
    #         break