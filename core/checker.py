import requests
from config import pic_purify_api_key
import json




def image_checker(file_path):
    """
    file_path: path of the image that will be analyzed.
    Return : If detect NSFW retrun True otherwise Return False
    """
    picpurify_url = 'https://www.picpurify.com/analyse/1.1'
    img_data = {'file_image': open(file_path, 'rb')}
    result_data = requests.post(picpurify_url,files = img_data, data = {"API_KEY":pic_purify_api_key, "task":"porn_moderation"})
    result_dict = json.loads(result_data.text)
    if result_dict["final_decision"]=="OK":
        return False
    if result_dict["final_decision"]=="KO":
        return True 





def video_checker(file_path):
    """
    file_path: path of the video that will be analyzed.
    Return : If detect NSFW retrun True otherwise Return False
    """
    picpurify_url = 'https://www.picpurify.com/analyse_video/1.0'
    video_data = {'file_video': open(file_path, 'rb')}
    
    result_data = requests.post(picpurify_url,files = video_data, data = {"API_KEY":pic_purify_api_key, "task":"porn_moderation", "frame_interval":1 })
    result_dict = json.loads(result_data.text)
    if result_dict["final_decision"]=="OK":
        return False
    if result_dict["final_decision"]=="KO":
        return True



