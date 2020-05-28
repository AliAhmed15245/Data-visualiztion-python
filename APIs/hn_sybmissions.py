import requests, pygal
from operator import itemgetter
from pygal.style import LightColorizedStyle as LCS, LightenStyle as  LS

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(r.status_code)

submissions_ids = r.json()
submissions_dicts = []
for submmission_id in submissions_ids[:30]:
    url = ("https://hacker-news.firebaseio.com/v0/item/" + str(submmission_id) +  ".json")
    submmission_r = requests.get(url)
    #print(submmission_r.status_code)
    response_dict = submmission_r.json()
    submissions_dict = {
        'title' : response_dict['title'],
        'link' : "https://news.ycombinator.com/item?id=" + str(submmission_id),
        'comments' : response_dict.get('descendants', 0)
    }

    submissions_dicts.append(submissions_dict)


submissions_dicts = sorted(submissions_dicts, key=itemgetter('comments'), reverse=True)
titles, plot_dicts = [], []
for sub_dict in submissions_dicts:
    titles.append(sub_dict['title'])
    plot_dict = {
        'title' : sub_dict['title'],
        'value' : sub_dict['comments'],
        'xlink' : sub_dict['link']
      }
    plot_dicts.append(plot_dict)



my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size= 24
my_config.label_font_size = 13
my_config.major_label_font_size =18
my_config.truncate_label =15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most commented submissions in Hacker News"
chart.x_labels = titles
chart.add("", plot_dicts)
chart.render_to_file('submissions.svg')

