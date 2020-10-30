def prompt():
    information = []

    name = str(input('Enter your username: '))
    information.append(name)
    languages = str(input('Enter the languages you are learning (ex.: Python, Java, C++): ')).split(',')
    information.append(languages)
    contact = str(input('Enter the ways of contacting you (ex.: Telegram: scaldings, Discord: scaldings#8694): '))
    contact = contact.split(',')
    information.append(contact)

    return information


def write_file(information: list):
    file = open('README.md', 'w')
    file.write(f'### Hello, my name is {information[0]}.\n\n')
    file.write(f'## Currently learning\n')
    for x in information[1]:
        file.write(f'* {x}\n')
    file.write(f'\n##Contact\n')
    for x in information[2]:
        file.write(f'* {x}\n')
    file.write('\n')
    link = f"[![{information[0]}'s github stats](https://github-readme-stats.vercel.app/api?username={information[0]}&show_icons=true&theme=dark)](https://github.com/anuraghazra/github-readme-stats)"
    file.write(f'{link}')


if __name__ == '__main__':
    write_file(prompt())
