import requests
from tk import *
from pprint import pprint


def main():
    URL = "https://cabinet.miem.hse.ru/api/student_profile"
    URL2 = 'https://api.github.com/users/' + GITHUB_USERNAME + '/repos'
    URL3 = 'https://gitlab.com/api/v4' + '/projects/' + str(GITLAB_REPOID) + '/repository/commits'

    headers = {"X-Auth-Token": MIEM_TOKEN}
    headers2 = {
        'Authorization': GITHUB_TOKEN
    }
    params = {
        'private_token': GITLAB_TOKEN
    }

    response = requests.get(URL, headers=headers)
    response2 = requests.get(URL2, headers=headers2)
    response3 = requests.get(URL3, params=params)

    if response.status_code == 200 and response2.status_code == 200 and response3.status_code == 200:
        data = response.json()
        name = data['data'][0]['main']['name']
        email = data['data'][0]['main']['email']
        description = data['data'][0]['main']['description'][0]

        data2 = response2.json()
        repos = []

        for i in range(len(data2)):
            temp = f'{i + 1}. {data2[i]["name"]} - {data2[i]["html_url"]}'
            repos.append(temp)
        repos = "\n".join(repos)

        commits = response.json()
        comm_info = """"""
        n = 1
        for commit in commits:
            commit_id = commit['id']
            author_name = commit['author_name']
            message = commit['message']
            temp = f"{n}. Commit ID: {commit_id}\nAuthor: {author_name}\Message: {message}\n--------------------\n"
            comm_info += temp
            n+=1

        with open('resume.txt', 'w', encoding="utf-8") as f:
            f.write(f'Имя: {name}\n')
            f.write(f'Адрес электронной почты: {email}\n')
            f.write(f'Текущая должность: {description}\n')
            f.write(f'Репозитории в GitHub:\n{repos}\n')
            f.write(f'Информация о коммитах в GitLab:\n{comm_info}\n')

        print("Информация успешно была записана в resume.txt")
    else:
        print("Ошибка при получении информации")


if __name__ == "__main__":
    main()
