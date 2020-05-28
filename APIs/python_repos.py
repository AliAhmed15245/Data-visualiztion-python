import requests, pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as Ls

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r= requests.get(url)
response_dict = r.json()
repo_dicts = response_dict['items']
names, plot_dicts = [], []
top = 10
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
    'value':repo_dict["stargazers_count"],
     'label':repo_dict['description'] or "",
     'xlink': repo_dict['html_url'],
     }
    plot_dicts.append(plot_dict)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size= 24
my_config.label_font_size = 13
my_config.major_label_font_size =18
my_config.truncate_label =15
my_config.show_y_guides = False
my_config.width = 1000
my_style = Ls('#333366', base_Style=LCS)

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most stared repos in GitHub"
chart.x_labels = names
chart.x_title = 'names'
chart.y_title = 'Stars'
chart.add("", plot_dicts)
chart.render_to_file("Stats.svg")

