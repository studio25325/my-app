from django.shortcuts import render
from django.utils import timezone
from .models import Post10
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

#dataFrameの利用に必要
from django_pandas.io import read_frame

def index(request):
    #return HttpResponse("10 サウザンド")
    posts = Post10.objects.all()

    params = { # <- 渡したい変数を辞書型オブジェクトに格納
        'taiga_01': 'a',
        'taiga_02': 'b',
        'taiga_03': 'b',
        'yuki_01': 'a',
        'yuki_02': 'b',
        'yuki_03': 'b',
    }
    #form = PostForm()
    context = {'posts': posts, 'params': params, }
    #id = 1

    #df = Post10.objects.filter(challenger=id)
    df = Post10.objects.all()
    df = read_frame(df)
    df_t = df[df.challenger == '1']
    df_st = df_t[df_t.title == 'ストローク']
    df_se = df_t[df_t.title == 'サーブ']
    df_y = df[df.challenger == '2']

    #合計件数
    #params['title'] = len(df)

    params['taiga_01'] = df_st['result'].sum(axis=0)
    params['taiga_02'] = df_se['result'].sum(axis=0)
    params['yuki_01'] = df_y['result'].sum(axis=0)
    #df_net1 = df_p[df_p.winner == '0']

    return render(request, 'tt/post_list.html', context)
