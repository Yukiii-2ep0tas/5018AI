from google.cloud import vision

client = vision.ImageAnnotatorClient.from_service_account_json('Cred/t_analysis_key.json')

def image_anot(image_path): ##图像标签化
    with open(image_path,'rb') as img_file:
        vision_api_image = vision.Image(content=img_file.read())
    response = client.label_detection(image=vision_api_image)
    return response

def obj_detect(image_path): ##目标识别
    with open(image_path,'rb') as img_file:
        vision_api_image = vision.Image(content=img_file.read())
    response =  client.object_localization(image = vision_api_image)
    return response

test_response=obj_detect('Asg4\Media\concert.jpg')

for label in test_response.localized_object_annotations:
    print('Object:', label.name)
    print('Score:', label.score)
    #for vertex in object_.bounding_poly.normalized_vertices:
    #    print(vertex.x, vertex.y)
    width = label.bounding_poly.normalized_vertices[1].x - label.bounding_poly.normalized_vertices[0].x
    height = label.bounding_poly.normalized_vertices[3].y - label.bounding_poly.normalized_vertices[0].y
    print('Width:', width)
    print('Height:', height)
    print('-'*30)

