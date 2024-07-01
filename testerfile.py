from deepface import DeepFace
import cv2
# Example usage
img_path = ("0.jpeg")
db_path = "D:\\New folder\\Face Detection\\DB"
img = ""
# Perform face recognition using DeepFace
try:
    dfs = DeepFace.find(img_path=img_path, db_path=db_path)
    for i in dfs:
        for j in i:
            img = dfs[0][j].to_string(index=False)
            imge = cv2.imread(img)
            cv2.imshow("My image", imge)
            cv2.waitKey(0)
            break
        break
    print(img)
except ValueError:
    print("Image not found")
#print(dfs)
#print(dfs[[identity]])



