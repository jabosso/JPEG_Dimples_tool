# ---------------------IMPORT SECTION----------------------------------------#
import cv2
import JpegDimplesLocalization as JpgD

# ---------------------------------------------------------------------------#


if __name__ == "__main__":
    img_path = '../Data/faces.png'
    img = cv2.imread(img_path)  # --->TODO replace it with a CleanUpImage procedure
    JpgD.JpegDimplesLocalization(img)
