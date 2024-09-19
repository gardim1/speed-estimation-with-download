import cv2
import numpy as np
from ultralytics import YOLO, solutions

# Caminhos dos arquivos
model_path = 'C:/Users/labsfiap/Desktop/New folder/best.pt' 
video_input_path = 'C:/Users/labsfiap/Desktop/New folder/playbackvideo.mp4' 
video_output_path = 'C:/Users/labsfiap/Desktop/New folder/output_video(2).avi'
# Carregar o modelo YOLO
model = YOLO(model_path)

# Abrir o vídeo de entrada
cap = cv2.VideoCapture(video_input_path)
assert cap.isOpened(), "Erro ao abrir o vídeo de entrada"

# Parâmetros do vídeo
fps = cap.get(cv2.CAP_PROP_FPS)
w, h = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# Criar o VideoWriter para salvar o vídeo processado
video_writer = cv2.VideoWriter(video_output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Variáveis para o cálculo de velocidade
previous_positions = {}
scale = 0.0035  # Escala em metros por pixel

# Função para calcular a velocidade
def calculate_speed(prev_pos, curr_pos, fps, scale):
    dist_pixels = np.linalg.norm(np.array(curr_pos) - np.array(prev_pos))
    dist_meters = dist_pixels * scale
    speed_mps = dist_meters * fps
    speed_kmh = speed_mps * 3.6
    return speed_kmh

# Limiar de confiança para a detecção de objetos
confidence_threshold = 0.85

# Loop para processar o vídeo frame a frame
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Processamento de vídeo concluído ou vídeo vazio.")
        break

    # Rastrear os objetos no frame
    results = model(frame, conf=confidence_threshold)

    if results and len(results) > 0:
        for bbox in results[0].boxes:
            x1, y1, x2, y2 = bbox.xyxy[0].cpu().numpy()
            conf = bbox.conf[0].cpu().numpy()
            cls = int(bbox.cls[0].cpu().numpy())

            # Coordenadas do centro do objeto
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)
            current_position = (center_x, center_y)

            # Calcular a velocidade se a posição anterior estiver disponível
            if cls in previous_positions:
                speed = calculate_speed(previous_positions[cls], current_position, fps, scale)
                # Desenhar a caixa delimitadora com a velocidade no lugar do nome
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255,191,0), 2) 
                cv2.putText(frame, f'{speed:.2f} km/h', (int(x1), int(y1) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # Atualizar a posição anterior
            previous_positions[cls] = current_position

    # Escrever o frame processado no vídeo de saída
    video_writer.write(frame)

    # Mostrar o frame (opcional)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
video_writer.release()
cv2.destroyAllWindows()

print(f'Vídeo salvo em: {video_output_path}')
