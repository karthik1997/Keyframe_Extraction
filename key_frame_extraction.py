import os
import os.path
import cv2
from Katna.video import Video
import multiprocessing

def main():

    # Extract specific number of key frames from video
    # if os.name == 'nt':
    #     multiprocessing.freeze_support()
    os.chdir("/content/drive/My Drive")

    vid = Video()

    # folder to save extracted images
    output_folder_path = "selectedframes"
    output_directory = os.path.join(".", output_folder_path)

    if not os.path.isdir(output_directory):
        os.mkdir(output_directory)

    # number of images to be returned
    needed_frames = 10
    # VIdeo file path
    video_path = os.path.join("/","content", "drive","My Drive","test2.mp4")
    print(f"Input video file path = {video_path}")

    images = vid.extract_frames_as_images(
        no_of_frames=needed_frames, file_path=video_path
    )

    # Save it to disk
    for counter, img in enumerate(images):
        vid.save_frame_to_disk(
            img,
            file_path=output_directory,
            file_name="test_" + str(counter),
            file_ext=".jpeg",
        )
    print(f"Exracted key frames file path = {output_directory}")

   #calling the driver function 

    if __name__ == "__main__":
    multiprocessing.set_start_method('spawn', force=True)
    main()

