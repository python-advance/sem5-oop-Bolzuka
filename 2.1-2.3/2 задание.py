# 2.1 Разработка классов и объектов «запись», «комментарий» для приложения «Блог» (использование наследования).
# 2.2. Создание геттеров и сеттеров для классов «запись», «комментарий» приложения «Гостевая книга».
# Создание функций для вывода на печать информации, хранящийся в объектах.
# 2.3. Формирование отчета по практическому заданию и публикация его в портфолио.
# Отчет сформирован в портфолио по данным заданиям.

class Post:
    def __init__(self, author, content):
        self.author = author
        self._content = content
        self.comments = list()

    def show(self):
        return ("Автор: " + str(self.author) + "\n" + "Содержание: " + str(self._content) + "\n")

    def show_comments(self):
        comments_string = ""
        for comment in self.comments:
            comments_string += comment.show()
        return comments_string

    @property
    def content(self):
        return self._content

    def add_comment(self, comment):
        self.comments.append(comment)

    @content.setter
    def content(self, content):
        self._content = content

    @content.getter
    def content(self):
        return self._content

      
class Comments(Post):
    def __init__(self, author, content):
        super(Comments, self).__init__(author=author, content=content)


if __name__ == "__main__":
    post = Post("Эрмитаж", "Мы вынуждены вас расстроить, наших любимых гостей. Сегодня в Эрмитаже санитарный день, поэтому мы закрыты, но уже завтра мы будем работать по расписанию")

    post.add_comment(Comments("Кирилл", "Я так хотел посетить сегодня эрмитаж"))
    post.add_comment(Comments("Ксюша", "Эх, придется идти завтра, хочу к импрессионистам на выставку :)"))

    with open('Record.txt', 'a') as f:
        f.write("\nПост\n")
        f.write(str(post.show()))
        f.write("\nКомментарии\n")
        f.write(str(post.show_comments()))
