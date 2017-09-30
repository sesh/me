import jinja2
import markdown2
from bs4 import BeautifulSoup


def generate_me():
    html = markdown2.markdown_path('README.md')
    sidebar, content = html.split('<hr />', 1)

    soup = BeautifulSoup(sidebar, 'html.parser')
    title = soup.find('h1').text

    template = jinja2.Template(open('template.html').read())
    rendered = template.render({
        'sidebar': sidebar,
        'content': content,
        'title': title,
    })

    with open('index.html', 'w') as f:
        f.write(rendered)


def main():
    generate_me()


if __name__ == '__main__':
    main()
