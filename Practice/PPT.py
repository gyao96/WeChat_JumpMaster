def onMouse(event, x, y, flag, param):
	global select_point_num
	global img
	if event == 4 and select_point_num <4:
		print(x, y, select_point_num) 
	
	# 已选择的点加 1
	select_point_num = select_point_num + 1

	# 将选择好的点添加到相应的数组当中
	point = (x,y)
	cv2.circle(img, point, 2, (0, 255, 0), 2)#修改最后一个参数

	# 划线
	if len(star_points) >= 1:
		# 取出最后一个点
		last_point = star_points[len(star_points)-1]
		# 划线
		cv2.line(img, point, last_point, (155, 155, 155), 2)
	
	if len(star_points) == 3: 
		# 取出开始的一个点
		last_point = star_points[0] 
		# 划线
		cv2.line(img, point, last_point, (155, 155, 155), 2)

	# 更新图片
	cv2.imshow(window, img)
	star_points.append(point)
	if len(star_points) == 4:
		rectify_that_part_of_photo() 


def rectify_that_part_of_photo():
	global star_points
	global opened_pic_file
	
	# 打开一份备份img
	img_copy = cv2.imread(opened_pic_file)
	cv2.namedWindow("result_img",0)

	origin_selected_corners = []
	region_selected_lu = (star_points[0][0],star_points[0][1])
	region_selected_ru = (star_points[1][0],star_points[1][1])
	region_selected_ld = (star_points[3][0],star_points[3][1])
	region_selected_rd = (star_points[2][0],star_points[2][1])

	# 添加到 origin_selected_corners
	origin_selected_corners.append(region_selected_lu)
	origin_selected_corners.append(region_selected_ru)
	origin_selected_corners.append(region_selected_rd)
	origin_selected_corners.append(region_selected_ld)

	# 变换过后的图像展示在一个宽为show_width,长为show_height的长方形窗口
	show_window_corners = []
	show_window_lu = (0,0)
	show_window_ru = (show_width-1,0)
	show_window_ld = (0,show_height-1)
	show_window_rd = (show_width-1,show_height-1)
	
	# 获得transform函数
	transform = cv2.getPerspectiveTransform(np.array(show_window_corners,dtype=np.float32),np.array(origin_selected_corners,dtype=np.float32))

	#
	transfered_pos = np.zeros([show_width,show_height,2])
	for x in range(show_width):
		for y in range(show_height):
			temp_pos = np.dot(transform,np.array([x,y,1]).T)
			transfered_x = temp_pos[0]/temp_pos[2]
			transfered_y = temp_pos[1]/temp_pos[2]
			transfered_pos[x][y] = (int(transfered_x),int(transfered_y))

	result_img = np.zeros((show_height,show_width,3),np.uint8)
	print(result_img.shape)

	for x in range(show_width):
		for y in range(show_height):
			result_img[y][x] = img_copy[transfered_pos[x][y][1]][transfered_pos[x][y][0]]

	cv2.imshow("result_img",result_img)