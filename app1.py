

from flask import Flask, render_template,request
from facebook_user_videos import get_video_links,get_single_views
app= Flask(__name__)

@app.route("/",methods=['GET'])
def index():
    
    return render_template("login.html")

@app.route("/test",methods=['GET'])
def sendVideo():
    video_url = request.full_path.split("?")[1]
    final_labels, num_views, num_likes = get_single_views(video_url)

    final_list = []
    final_list.append(video_url)
    final_list.append(num_views)
    final_list.append(num_likes)
    final_list.append(final_labels)

    return render_template("labels.html",videos=final_list)




@app.route("/videos",methods=['GET'])
def index1():
    videoslist= get_video_links()
    return render_template("videos.html", videos=videoslist)



@app.route("/labels",methods=['GET'])
def index2():
    videoslist2=[["https://www.facebook.com/100083482954115/videos/5170225936386552/",'a',2,4]]
    return render_template("labels.html",videos=videoslist2)
import os
if __name__=="__main__":
    #app.run(host=os.getenv('IP', '0.0.0.0'),
    #port=int(os.getenv('PORT', 4000)))
    app.run(debug=True)


