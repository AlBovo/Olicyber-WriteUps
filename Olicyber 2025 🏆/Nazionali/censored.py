#!/usr/bin/env python3

import cv2
import numpy as np
from collections import OrderedDict

# gerate a censored image with this text
ALPHABET = "abcdefghijklmnopqrstuvwxyz_{}"

def find_boxes_bgr(img, min_area=2000):
    mask = ((img[:,:,0] < 15) & (img[:,:,1] < 15) & (img[:,:,2] < 15)).astype(np.uint8) * 255
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=8)
    boxes = []
    for i in range(1, num_labels):
        x, y, w, h, area = stats[i]
        if area >= min_area and w >= 5 and h >= 5:
            boxes.append((x, y, w, h))
    boxes.sort(key=lambda b: (b[1], b[0]))
    return boxes

def boxes_by_rows(boxes, y_tol=10):
    rows = []
    for b in boxes:
        x,y,w,h = b
        placed = False
        for row in rows:
            if abs(y - np.median([rb[1] for rb in row])) <= y_tol:
                row.append(b)
                placed = True
                break
        if not placed:
            rows.append([b])
    rows = [sorted(row, key=lambda b: b[0]) for row in rows]
    return rows

def build_width_map_from_first_occurrence(boxes, alphabet=ALPHABET):
    seen = OrderedDict()
    for b in boxes:
        w = b[2]
        if w not in seen:
            if len(seen) < len(alphabet):
                seen[w] = alphabet[len(seen)]
        if len(seen) == len(alphabet):
            break
    return dict(seen)

def decode_from_boxes(boxes, width_to_char, y_tol=10):
    rows = boxes_by_rows(boxes, y_tol=y_tol)
    out_rows = []
    for row in rows:
        s = ""
        for x,y,w,h in row:
            best = min(width_to_char.keys(), key=lambda k: abs(k - w))
            s += width_to_char[best] if abs(best - w) <= 3 else "?"
        out_rows.append(s)
    return out_rows

if __name__ == "__main__":
    img_alpha = cv2.imread("alfabeto.png")
    img_cens = cv2.imread("censurato.png")

    alpha_boxes = find_boxes_bgr(img_alpha, min_area=2000)
    cens_boxes = find_boxes_bgr(img_cens, min_area=2000)

    width_to_char = build_width_map_from_first_occurrence(alpha_boxes, ALPHABET)
    decoded_rows = decode_from_boxes(cens_boxes, width_to_char, y_tol=10)

    print("\\n".join(decoded_rows))
    print("joined:", "".join(decoded_rows))