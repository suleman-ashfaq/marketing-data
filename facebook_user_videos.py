

import facebook
import yt_dlp

from main import get_labels

token = "EAAOjzp6FaTcBAHbQZAT5Mz3mjJkRTuh0Wik0rWZCfPwrhCq2oERZCoZABXjjJHyS0Pz08OVLWvbher39uTcidTgKGtZCRyAAK6wOS4ea6MzTqYuawuDCZCqCJeiiLhChVIzdrwFI0OMsP6UZAiJuV7UNvZCWi9xHyVGfnoIETlL0keCdnknsSixZCAuCEjGUzE69TdSRFColrMwCmJL5kRPni"


def download_video(LINK,file_name):
    URLS = []
    URLS.append(LINK)
    ydl_opts = {
        'outtmpl':file_name,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URLS)

def get_views_likes_():
    app_id = '1024532748265783'
    app_secret = '623d1235722d1f28cdd9d7dfadf6525b'

    graph = facebook.GraphAPI()

    # exactly what you're after 😉
    # token = graph.get_app_access_token(app_id, app_secret)


    graph = facebook.GraphAPI(access_token=token)

    personal = graph.request("me?fields=id,name")

    user_id = personal['id']

    print(user_id)

    videos = graph.request(user_id+"/videos?type=uploaded")

    videos = videos['data']
    all_labels = []
    permalinks = []
    views = []
    likes = []

    for video_count, video in enumerate(videos):
        likes_views = graph.request(video['id']+"?fields=views,likes,permalink_url")
        print("Views", likes_views['views'])
        permalink = "https://www.facebook.com"+likes_views['permalink_url']
        print("permalink_url", "www.facebook.com"+likes_views['permalink_url'])
        file_name = "videos/"+user_id+"_"+str(video_count)+".mp4"
        # create response object
        download_video(permalink,file_name)
        final_labels = get_labels(file_name)
        num_likes = len(likes_views['likes']['data'])
        num_views = likes_views['views']

        # print("Like",len(likes_views['likes']['data']))

        # print("Top Labels", final_labels)
        all_labels.append(final_labels)
        views.append(num_views)
        likes.append(num_likes)
        permalinks.append(permalink)

    return all_labels, likes, views, permalinks


def get_single_views(url):

    graph = facebook.GraphAPI(access_token=token)

    personal = graph.request("me?fields=id,name")

    user_id = personal['id']


    videos = graph.request(user_id+"/videos?type=uploaded")

    videos = videos['data']

    for video_count, video in enumerate(videos):
        likes_views = graph.request(video['id']+"?fields=views,likes,permalink_url")
        print("Views", likes_views['views'])
        permalink = "https://www.facebook.com"+likes_views['permalink_url']
        print("permalink_url", "www.facebook.com"+likes_views['permalink_url'])
        file_name = "videos/"+user_id+"_"+str(video_count)+".mp4"
        # create response object
        download_video(permalink,file_name)
        final_labels = get_labels(file_name)
        num_likes = len(likes_views['likes']['data'])
        num_views = likes_views['views']

        if permalink == url:
            print(final_labels,num_views,num_likes)
            final_labels =",".join(final_labels)


            return final_labels, num_views, num_likes



def get_video_stats(permalink):
    user_id = permalink.split("/")[3]
    file_name = "videos/"+user_id+".mp4"
    download_video(permalink,file_name)
    final_labels = get_labels(file_name)
    return final_labels



def get_video_links():


    graph = facebook.GraphAPI(access_token=token)

    personal = graph.request("me?fields=id,name")

    user_id = personal['id']

    # print(user_id)

    videos = graph.request(user_id+"/videos?type=uploaded")

    videos = videos['data']
    all_labels = []
    permalinks = []
    views = []
    likes = []

    for video_count, video in enumerate(videos):
        likes_views = graph.request(video['id']+"?fields=views,likes,permalink_url")
        # print("Views", likes_views['views'])
        permalink = "https://www.facebook.com"+likes_views['permalink_url']
        # print("permalink_url", "www.facebook.com"+likes_views['permalink_url'])
        # create response object
        permalinks.append(permalink)

    return permalinks

