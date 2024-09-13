from PIL import Image,ImageFilter,ImageEnhance
from IPython.display import display
def open_image(path):
    try:
        img=Image.open(path)
        return img 
    except Exception as e:
        print("error opening the image")
        return None
def save_image(img,path):
    try:
        img.save(path)
        print(f"image saved to:{path}")
    except Exception as e:
        print("error saving the image")
def resize_image(img,width,height):
    resized_img=img.resize((width,height))
    print(f"image resized into:{width}X{height}")
    return resized_img
def crop_img(img,left,top,right,bottom):
    cropped_img=img.crop((left,top,right,bottom))
    return cropped_img
def rotate_img(img,angle):
    rotated_img=img.rotate(angle)
    return rotated_img
def user():
    image_path=input("enter the path of the image")
    img=open_image(image_path)
    if img is None:
        return None
    print("\n available options are")
    print("1 for Resize the image")
    print("2 for crop the image")
    print("3 for rotate the image")
    print("4 for save the new image")
    while True:
        choice=input("enter the options from 1-4: ")
        if choice=="1":
            width=int(input("enter the width:"))
            height=int(input("enter the height:"))
            img=resize_image(img,width,height)
        elif choice=="2":
            left=int(input("enter the left dimensions:"))
            right=int(input("enter the right dimensions:"))
            bottom=int(input("enter the bottom dimensions:"))
            top=int(input("enter the top dimensions:"))
            img=crop_img(img,left,top,right,bottom)
        elif choice=="3":
            angle=int(input("enter the angle to be rotated:"))
            img=rotate_img(img,angle)
        elif choice=="4":
            save_path=input('enter the path to save the image: ')
            save_image(img,save_path)
            break
        else:
            print("invalid choice")
user()