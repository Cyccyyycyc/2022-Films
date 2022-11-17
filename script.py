from tools import get_films
import os

# 正则匹配表达式
p = \
[
    # 从排行榜中获得电影url
    ['<a href="https://movie.douban.com/subject/(.*?)/" class="">'],

    #  从电影主页获得电影信息
    [
        '<span property="v:itemreviewed">(.*?)</span>',  # 电影名字
        '<span property="v:genre">(.*?)</span>',  # type
        '<span class="pl">语言:</span>(.*?)<br>',  #  language
        '<span class="pl">制片国家/地区:</span>(.*?)<br>',  #  country
        '<span class="pl">上映日期:</span> <span property="v:initialReleaseDate" content="(.*?)">',  # date
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

film_id = \
[
    '26305582',
    '35360684',
    '35807455',
    '35437938',
    '35693381',
    '35707087',
    '26654184',
    '35608160',
    '35649759',
    '35675082',
    '35377026',
    '35765781',
    '30449624',
    '35319389',
    '35417834',
    '35183042',
    '35337517',
    '35505100',
    '35118954',
    '26710112',
    '26642033',
    '35234581',
    '35768795',
    '36035677',
    '6424756',
    '35230876',
    '35192672',
    '34832354',
    '35240235',
    '27203644',
    '35073886',
    '26995893',
    '34970503',
    '35914264',
    '26926448',
    '35182979',
    '35814526',
    '35294952',
    '35430833',
    '36090857',
    '26873582',
]

# 表头
header_com = ['seen', 'username', 'id', 'time', 'location', 'votes', 'star', 'comment']
header_inf = ['id', 'name', 'type', 'language', 'country' , 'date', 'scores', 'box-office', 'five', 'four', 'three', 'two', 'one']

data_foder = "data/"
comments_foder = data_foder + "details/"

os.makedirs(data_foder, exist_ok=True)
os.makedirs(comments_foder, exist_ok=True)
get_data = get_films(p=p, film=film_id, delay=5)
get_data.get_film()
get_data.get_info(save=True, foder=data_foder, header=header_inf)
get_data.get_comments(save=True, foder=comments_foder, header=header_com)