import cv2


def generatorMemow():
    image = cv2.imread("images/meme.jpg")

    window_name = 'Image'

    border = 100

    image = cv2.copyMakeBorder(image, 10, border, 10, 10, cv2.BORDER_CONSTANT, None, value=(0, 0, 0))

    thickness = 2
    color = (255, 0, 0)
    fontScale = 1
    font = cv2.FONT_HERSHEY_SIMPLEX

    image = cv2.putText(image, 'Zabawny mem', ((image.shape[1] // 2) - 100, (image.shape[0] // 2) + border + 110), font,
                        fontScale, color, thickness, cv2.LINE_AA)

    cv2.imshow(window_name, image)

    cv2.waitKey(0)

    cv2.destroyAllWindows()


generatorMemow()
