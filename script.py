from tools import get_top10

# 正则匹配表达式
p = \
[
    # 从排行榜中获得电影url
    ['<a href="https://movie.douban.com/subject/(.*?)/" class="">'],

    #  从电影主页获得电影信息
    [
        '<span property="v:itemreviewed">(.*?)</span>',  # 电影名字
        '<strong class="ll rating_num" property="v:average">(.*?)</strong>',  # 总评分
        '<span property="v:votes">(.*?)</span>',  # 评价人数
        '<span class="rating_per">(.*?)%</span>',  # 评分为5/4/3/2/1星的百分比

    ],

    #  获得单部电影的短评论信息
    [
        '<div class="comment-item " data-cid="(.*?)<div class="comment-report"',  # get a short-comment
        '<a title="(.*?)" href="https://www.douban.com/people/',  # username
        '<a href="https://www.douban.com/people/(.*?)/" class="">',  # id
        '<span class="comment-time " title="(.*?)">',  # time
        '<span class="comment-location">(.*?)</span>',  # location
        '<span class="votes vote-count">(.*?)</span>',  # votes
        '<span class="allstar(.*?) rating"',  # star
        '<span class="short">(.*?)</span>',  # comment
    ],
]

# 表头
header_com = ['seen', 'username', 'id', 'time', 'location', 'votes', 'star', 'comment']
header_inf = ['id', 'name', 'scores', 'box-office', 'five', 'four', 'three', 'two', 'one']

get_data = get_top10(p)
get_data.get_film()
get_data.get_info(save=True, foder="data/", header=header_inf)
get_data.get_comments(save=True, foder="data/short-comments/", header=header_com)