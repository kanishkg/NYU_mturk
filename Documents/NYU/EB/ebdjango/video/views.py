# Add test data and http responses. Check assignment id.
from django.shortcuts import render
from .models import video, record
import random
from django.http import HttpResponseRedirect
from .forms import *
from random import shuffle
from django.views.decorators.clickjacking import xframe_options_exempt
from django import template

register = template.Library()

videos_list=[]
test_video_list = [['https://s3.amazonaws.com/nyurte/Baltimore/car+on+fire2.mp4','https://s3.amazonaws.com/nyurte/Baltimore/car+on+fire1.mp4','1'],['https://s3.amazonaws.com/nyurte/Baltimore/car+on+fire2.mp4','https://s3.amazonaws.com/nyurte/Baltimore/car+on+fire3.mp4','1'],['https://s3.amazonaws.com/nyurte/Baltimore/car+traffic1.mp4','https://s3.amazonaws.com/nyurte/Baltimore/car+on+fire4.mp4','0'],['https://s3.amazonaws.com/nyurte/Baltimore/car+on+fire2.mp4','https://s3.amazonaws.com/nyurte/Baltimore/car+traffic3.mp4','0'],['https://s3.amazonaws.com/nyurte/Baltimore/car+traffic1.mp4','https://s3.amazonaws.com/nyurte/Baltimore/car+traffic2.mp4','1']]
test_video_pair = 2
test_indices = []
links=[]
@register.filter
def addone(value,args):
    return int(value) + 1 

@register.filter
def subone(value):
    return int(value) - 1

def getcol(i,index,videos):
    i=i-1
    if index == 1 :
        return videos[i].a
    if index == 2 :
        return  videos[i].b
    if index == 3 :
        return  videos[i].c
    if index == 4 :
        return  videos[i].d
    if index == 5 :
        return  videos[i].e
    if index == 6 :
        return  videos[i].f
    if index == 7 :
        return  videos[i].g
    if index == 8 :
        return  videos[i].h
    if index == 9 :
        return  videos[i].i
    if index == 10 :
        return  videos[i].j
    if index == 11 :
        return  videos[i].k
    if index == 12 :
        return  videos[i].l
    if index == 13 :
        return  videos[i].m
    if index == 14 :
        return  videos[i].n
    if index == 15 :
        return  videos[i].o
    if index == 16 :
        return  videos[i].p
    if index == 17 :
        return  videos[i].q
    if index == 18 :
        return  videos[i].r
    if index == 19 :
        return  videos[i].s
    if index == 20 :
        return  videos[i].t
    if index == 21 :
        return  videos[i].u
    if index == 22 :
        return  videos[i].v
    if index == 23 :
        return  videos[i].w
    if index == 24 :
        return  videos[i].x
    if index == 25 :
        return  videos[i].y
    if index == 26 :
        return  videos[i].z
    if index == 27 :
        return  videos[i].aa
    if index == 28 :
        return  videos[i].ab
    if index == 29 :
        return  videos[i].ac
    if index == 30 :
        return  videos[i].ad
    if index == 31 :
        return  videos[i].ae
    if index == 32 :
        return videos[i].af
    if index == 33 :
        return  videos[i].ag
    if index == 34 :
        return  videos[i].ah
    if index == 35 :
        return  videos[i].ai
    if index == 36 :
        return  videos[i].aj
    if index == 37 :
        return  videos[i].ak
    if index == 38 :
        return  videos[i].al
    if index == 39 :
        return  videos[i].am
    if index == 40 :
        return  videos[i].an

def mod_db_2(k,val, workerId, vid_fold):
   
    global videos1
    i=k[0][0]
    
    vid = video.objects.get(id = k[0][0]+(vid_fold-1)*40)
    vid2 =  video.objects.get(id = k[0][1]+(vid_fold-1)*40)
   
   

    rec = record(worker_id= str(workerId), record_link_1 = str(vid.ink), record_link_2 = str(vid2.ink), record_response = int(val))
    #rec = record(worker_id= 'dhghsfedfseh', record_link_1 = 'fyyugi', record_link_2 = 'hvgguhu', record_response = 1)
    rec.save()
    


def mod_db(k,val, workerId, vid_fold):
    global videos1
    i=k[0][0]
    index = k[0][1]
    
    vid = video.objects.get(id = k[0][0]+(vid_fold-1)*40)
    

    
    if index == 1 :
         vid.a+=val
    if index == 2 :
         vid.b+=val
    if index == 3 :
          vid.c+=val
    if index == 4 :
          vid.d+=val
    if index == 5 :
          vid.e+=val
    if index == 6 :
          vid.f+=val
    if index == 7 :
          vid.g+=val
    if index == 8 :
          vid.h+=val
    if index == 9 :
          vid.i+=val
    if index == 10 :
          vid.j+=val
    if index == 11 :
          vid.k+=val
    if index == 12 :
          vid.l+=val
    if index == 13 :
          vid.m+=val
    if index == 14 :
          vid.n+=val
    if index == 15 :
          vid.o+=val
    if index == 16 :
          vid.p+=val
    if index == 17 :
          vid.q+=val
    if index == 18 :
          vid.r+=val
    if index == 19 :
          vid.s+=val
    if index == 20 :
          vid.t+=val
    if index == 21 :
          vid.u+=val
    if index == 22 :
          vid.v+=val
    if index == 23 :
          vid.w+=val
    if index == 24 :
          vid.x+=val
    if index == 25 :
          vid.y+=val
    if index == 26 :
          vid.z+=val
    if index == 27 :
          vid.aa+=val
    if index == 28 :
          vid.ab+=val
    if index == 29 :
          vid.ac+=val
    if index == 30 :
          vid.ad+=val
    if index == 31 :
          vid.ae+=val
    if index == 32 :
         vid.af+=val
    if index == 33 :
          vid.ag+=val
    if index == 34 :
          vid.ah+=val
    if index == 35 :
          vid.ai+=val
    if index == 36 :
          vid.aj+=val
    if index == 37 :
          vid.ak+=val
    if index == 38 :
          vid.al+=val
    if index == 39 :
          vid.am+=val
    if index == 40 :
          vid.an+=val
    vid.save()

@xframe_options_exempt
def videos(request):



    global test_video_list
    global test_indices
    num_video_pair = 1
    num_vid_fold = 3
    num_vid = 40
    num_videos = num_video_pair*num_vid_fold
    global links
    global videos_list
    global render_data
    if request.method == 'GET':
        
        links = []
        
        try:

            if request.GET.get("assignmentId") == "ASSIGNMENT_ID_NOT_AVAILABLE":
            # worker hasn't accepted the HIT (task) yet
                submit_state = "true"
            else:
                # worked accepted the task
                submit_state = "false"

            worker_id = request.GET.get("workerId", "")
            

            render_data = {
                "workerId": request.GET.get("workerId"),
                "assignmentId": request.GET.get("assignmentId"),
                #"amazon_host": AMAZON_HOST,
                "hitId": request.GET.get("hitId"),
            }
        except:
            pass



        form = submit()
        global k
        global videos1
        videos1 = video.objects.order_by('id')
       
        
        i=1
       
        
        
       
        def video_add(videos, num):
            added = 0 
            thresh = 1
            videos_list_func = []
            links_func = []
            videos_list_return = []
            links_return = []
            while added < num_video_pair:
                thresh-=1
                for i in xrange(num_vid):
                    for j in xrange(i):
                        val= getcol(i,j,videos1)
                        if val == thresh or val == -thresh :
                            videos_list_func.append([i,j])
                            links_func.append([videos[i-1].ink,videos[j-1].ink,num])
                            added+=1
            test_indices = random.sample(xrange(added), num_video_pair)
            for index in test_indices:
                links_return.append(links_func[index])
                videos_list_return.append(videos_list_func[index])
            return videos_list_return, links_return
        for i in xrange(num_vid_fold):
            a,b = video_add(videos1[i*num_vid:i*num_vid+num_vid-1],i+1)
            videos_list.append(a)
            links.append(b[0])
        

        videos_list_shuf = []
        links_shuf = []
        index_shuf = range(len(links))
        shuffle(index_shuf)
        for i in index_shuf:
            videos_list_shuf.append(videos_list[i])
            links_shuf.append(links[i])
        links = links_shuf
        videos_list = videos_list_shuf
        

        test_indices = random.sample(xrange(num_videos+test_video_pair-1),test_video_pair)
        done=0
        for k in xrange(num_videos+test_video_pair):
            if k in test_indices:
                links.insert(k,[test_video_list[done][0],test_video_list[done][1],0])
                done+=1


        link1 = []
        link2 = []
        for link in links:
            link1.append(link[0])
            link2.append(link[1])
            
        
    else:
        global videos1
        test_score = 0
        done = 0
        form = submit(request.POST)
        if form.is_valid():

            for k in xrange(num_videos+test_video_pair):
                res = form.cleaned_data['pair'+str(k+1)]
                if k in test_indices:
                    done += 1
                    if res == test_video_list[done-1][2]:
                        test_score += 1

        if test_score < 2:
            return HttpResponseRedirect('https://workersandbox.mturk.com/mturk/externalSubmit?assignmentId='+str(render_data['assignmentId'])+'&workerId='+str(render_data['workerId'])+'&pass='+'0'+'&hitId='+str(render_data['hitId']))
        done = 0
        for k in xrange(num_videos+test_video_pair):
            res = form.cleaned_data['pair'+str(k+1)]
            if k in test_indices:
                done += 1

            elif res == '1':
                mod_db(videos_list[k-done],1,render_data['workerId'],links[k][2])
                mod_db_2(videos_list[k-done],1,render_data['workerId'],links[k][2])
                
            else:
                mod_db(videos_list[k-done],-1,render_data['workerId'],links[k][2])
                mod_db_2(videos_list[k-done],-1,render_data['workerId'],links[k][2])
      
                    
        return HttpResponseRedirect('https://workersandbox.mturk.com/mturk/externalSubmit?assignmentId='+str(render_data['assignmentId'])+'&workerId='+str(render_data['workerId'])+'&pass='+'1'+'&hitId='+str(render_data['hitId']))
    return render(request, 'video/videos.html', {  'num_video_pair':num_videos+test_video_pair,'link1':link1,'link2':link2,'videos_list':videos_list, 'form': form, 'submit_state': submit_state, 'links':links})