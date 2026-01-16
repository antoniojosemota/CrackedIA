import tensorflow as tf
import numpy as np
import cv2

model = tf.keras.models.load_model("crack_detection2.keras")

# imagem original
img_orig = cv2.imread("piso.jpg")
h, w, _ = img_orig.shape

# imagem para o modelo (⚠️ deve ser o MESMO tamanho do treino)
img = cv2.resize(img_orig, (128, 128))
img_norm = img / 255.0
img_input = np.expand_dims(img_norm, axis=0)

# previsão
mask_pred = model.predict(img_input)[0]  # (64,64,1)
mask_bin = (mask_pred > 0.5).astype(np.uint8) * 255  # (64,64,1)

# remover canal antes do resize
mask_bin = mask_bin.squeeze()  # (64,64)

# voltar a máscara para o tamanho original
mask_big = cv2.resize(mask_bin, (w, h), interpolation=cv2.INTER_NEAREST)

# overlay
overlay = img_orig.copy()
overlay[mask_big == 255] = [0, 0, 255]

cv2.imshow("Imagem Original", img_orig)
cv2.imshow("Máscara Prevista", mask_big)
cv2.imshow("Rachaduras (Overlay)", overlay)
cv2.waitKey(0)
cv2.destroyAllWindows()
