
from PIL import Image
import glob

class Gif_macker:


    def create(frame_folder,tn):
        res=glob.glob(f"{frame_folder}/*.png")
        frames = [Image.open(image) for image in res]
        frame_one = frames[0]
        frame_one.save("result"+str(tn)+".gif", format="GIF", append_images=frames,
                save_all=True, duration=500, loop=0)