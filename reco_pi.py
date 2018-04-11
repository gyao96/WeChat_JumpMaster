#  -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
import shutil
import time
import math

# 参数表
under_game_score_y = 110  # 截图中刚好低于分数显示区域的 Y 坐标
piece_base_height_1_2 = 25  # 二分之一的棋子底座高度，可能要调节
Gau, standard = (5,5), 3

up_B, down_B, left_B, right_B = 14,754,260,665 #裁剪原始图像的边界
w = right_B - left_B
h = down_B - up_B

special_board = ['music_player.png','cesspool.png','red.png'] # 有加分的目标
special_board_contour = ['red_c.png','sqr_c.png']
piece_template = cv2.imread('chess.png',0) # 棋子模板
white_point_template = cv2.imread('white_point.png',0) # 白点模板

piece_w, piece_h = piece_template.shape[::-1]
method = 'cv2.TM_CCORR_NORMED'
meth = eval('cv2.TM_CCORR_NORMED')

# 模板匹配 获取棋子坐标
def find_piece(img):
	res = cv2.matchTemplate(img, piece_template, meth)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	piece_x, piece_y = max_loc
	piece_x = int(piece_x + piece_w / 2)
	piece_y = piece_y + piece_h - piece_base_height_1_2
	return piece_x, piece_y

def find_board(img,piece_x,piece_y):

    board_x = 0
    board_y = 0
    result = 0
	

	
    img2 = img.copy()
    method = 'cv2.TM_CCOEFF_NORMED'
    img[:110,] = 0

    img2 = cv2.GaussianBlur(img2, Gau, standard)
    img_canny = cv2.Canny(img2, 3, 10)		

#############Digging out the chess ###########################		
    for i in range(piece_y - 120, piece_y + 10):
        for j in range(piece_x - 16, piece_x + 16):
            img_canny[i][j] = 0
##############################################################

#############################################################
######### This sector is for special_board detection ########
    for i in special_board:
        template = cv2.imread(i, 0)
        #cv2.imshow("image",template)
        #cv2.waitKey(0)
        template_w, template_h = template.shape[::-1]
		
        res = cv2.matchTemplate(img2, template, meth)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val > 0.99 and (max_loc[1] + template_h / 2) < piece_y:
            board_x = max_loc[0] + template_w / 2
            board_y = max_loc[1] + template_h / 2
            result = 2
            print('found special_board  max_val:  %f' % max_val)
            return board_x, board_y, result
##############################################################

######### This sector is for special_board detection with contour########
    for i in special_board_contour:
        template = cv2.imread(i, 0)
        #cv2.imshow("image",template)
        #cv2.waitKey(0)
        template_w, template_h = template.shape[::-1]
		
        res = cv2.matchTemplate(img_canny, template, meth)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val > 0.98 and (max_loc[1] + template_h / 2) < piece_y:
            board_x = max_loc[0] + template_w / 2
            board_y = max_loc[1] + template_h / 2
            result = 2
            print('found special_board_contour  max_val:  %f' % max_val)
            return board_x, board_y, result
##############################################################


		
##############################################################
######### This sector is for white point detection ###########		
    res = cv2.matchTemplate(img_canny, white_point_template, eval(method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val > 0.9:
        board_x = max_loc[0] + 22
        board_y = max_loc[1] + 22
        result = 1
        print('white_point_val:  %f' % max_val)
        return board_x, board_y, result
##############################################################
		


############This sector is the normal board locating algorithm
    img_canny[:,:2] = 0
    board_y_top = under_game_score_y

    cv2.imwrite('c2.png',img_canny)
    for i in img_canny[under_game_score_y:]:
        # i是一整行像素的list，max返回最大值，一旦最大值存在，则找到了board_y_top
        if max(i):
            break
        board_y_top += 1

    board_x = int(np.mean(np.nonzero(img_canny[board_y_top])))
    board_y_bottom = board_y_top + 10


    board_y = board_y_top

    x1 = board_x
    fail_count = 0
    if board_x > piece_x:
        for i in img_canny[board_y_top:board_y_top+80]:
            try:
                x = max(np.nonzero(i)[0])
            except:
                pass
            if x > x1:
                x1 = x
                board_y += 1
                if fail_count < 5 and fail_count != 0:
                    fail_count -= 1
            elif fail_count > 6 and board_y - board_y_bottom >10:
                result = 1
                board_y -= 1
                break
            elif fail_count > 6 and board_y - board_y_bottom <= 10:
                result = 0
                break

            else:
                fail_count += 1

    else:
        for i in img_canny[board_y_top:board_y_top+80]:
            try:
                x = min(np.nonzero(i)[0])
            except:
                pass
            if  x < x1:
                x1 = x
                board_y += 1
                if fail_count < 5 and fail_count != 0:
                    fail_count -= 1
            elif fail_count > 6 and board_y - board_y_bottom > 10:
                board_y -= 1
                result = 1
                break
            elif fail_count > 6 and board_y - board_y_bottom <= 10:
                result = 0
                break
            else:
                fail_count += 1

    if result == 0:
        board_y = piece_y - abs(board_x - piece_x) * math.sqrt(3) / 3
        result = 1
        print("return by old")


    # print('result:  %d' % result)
    return board_x, board_y, result

def main():
    filename = 'image.jpg'
    img = cv2.imread(filename,0)

    piece_x , piece_y = find_piece(img)
    board_x , board_y, result = find_board(img,piece_x,piece_y)
    grad = 1.0*(board_y-piece_y)/(board_x-piece_x)
    print('Piece_x = %d; Piece_y = %d' % (piece_x,piece_y))
    print('Board_x = %d; Board_y = %d' % (board_x,board_y))
    print('Grad = %f; Result = %d' % (grad, result))
    cv2.circle(img, (piece_x,piece_y), 4, (255,255,0), -1)
    cv2.circle(img, (int(board_x),int(board_y)), 4, (255,0,255), -1)
    cv2.imwrite("debug.jpg",img)

    if abs(grad)>0.2 and abs(grad)<0.9 :
        print("On track")
    else:
        print("Fault")

if __name__ == '__main__':
    main()
