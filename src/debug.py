import numpy as np
import matplotlib.pyplot as plt

def print_frame(single_channel=False):
    def _inner(i, frame, positions):
        W, H, C = frame.shape
        if single_channel:
            frame_p = np.zeros([W,H,3], dtype=np.uint8)
            frame_p[:,:,0] = frame[:,:,0]
            frame_p[:,:,1] = frame[:,:,0]
            frame_p[:,:,2] = frame[:,:,0]
            frame = frame_p

        if positions:
            true_pos, estimated_pos = positions
            if true_pos is not None:
                t2, t1 = true_pos[0], true_pos[1]
                frame[t1-2:t1+2, t2-2:t2+2] = np.array([0, 255, 0], dtype=np.uint8)
            if estimated_pos is not None:
                e2, e1 = estimated_pos[0], estimated_pos[1]
                frame[e1-2:e1+2, e2-2:e2+2] = np.array([255, 0, 0], dtype=np.uint8)

        plt.title(str(i))
        plt.imshow(frame, cmap='viridis')
        plt.show()
    return _inner

