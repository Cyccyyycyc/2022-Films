from selenium.webdriver import Chrome
import csv
import re

class get_top10():
    def __init__(self, p=None):
        self.chrome = Chrome()
        self.p_id = p[0]  # 从排行榜中获得电影url
        self.p_info = p[1]  #  从电影主页获得电影信息
        self.p_item = p[2]  #  获得单部电影的短评论信息
        self.film = []

    #  获得电影id号
    def get_film(self):
        self.chrome.get("https://movie.douban.com/chart")
        html = self.chrome.page_source
        self.film = re.findall(self.p_id[0], html)
        return self.film

    #  获得电影信息
    def get_info(self, save=False, foder=None, header=None):
        films = []
        for id in self.film:
            info = [str(id)]
            self.chrome.get("https://movie.douban.com/subject/{}".format(id))
            html = self.chrome.page_source.replace('\n', '')

            for p in self.p_info:
                tmp = re.findall(p, html)
                if not tmp:
                    info.append("")
                for t in tmp:
                    info.append(t)
            films.append(info)
        if save:
            # write film.csv
            with open(foder + 'info.csv', 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                # write header
                writer.writerow(header)
                writer.writerows(films)
        return films

    #  获得电影评论
    def get_comments(self, save=False, foder=None, header=None):
        film = []
        for i, id in enumerate(self.film):
            # 一部电影所有短评论
            coms = []
            for j in range(0, 200, 20):
                url = "https://movie.douban.com/subject/{}/comments?status=P&start={}&limit=20&sort=new_score".format(id, j)
                self.chrome.get(url)
                html = self.chrome.page_source.replace('\n', '')
                items = re.findall(self.p_item[0], html)

                # a single comment
                for item in items:
                    com = ['1']
                    for p in self.p_item[1:]:
                        tmp = re.findall(p, item)
                        if not tmp:
                            com.append("")
                        for t in tmp:
                            com.append(t)
                    coms.append(com)
            #  not seen
            for j in range(0, 200, 20):
                url = "https://movie.douban.com/subject/{}/comments?status=F&start={}&limit=20&sort=new_score".format(id, j)
                self.chrome.get(url)
                html = self.chrome.page_source.replace('\n', '')
                items = re.findall(self.p_item[0], html)

                for item in items:
                    com = ['0']
                    for p in self.p_item[1:]:
                        tmp = re.findall(p, item)
                        if not tmp:
                            com.append("")
                        for t in tmp:
                            com.append(t)
                    coms.append(com)
            film.append(coms)

            if save:
                # write film.csv
                with open(foder + '{}.csv'.format(i), 'w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    # write header
                    writer.writerow(header)
                    writer.writerows(coms)
        return film
