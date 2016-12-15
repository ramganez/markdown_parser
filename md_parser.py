import codecs
import re


class Markdown(object):
    without_space_p = re.compile(r"^[ \t]+$", re.M)

    def __init__(self, text=''):
        self.text = text

    def build_headers(self):
        pass

    def build_paragraph(self):
        pass

    def build_text_attributes(self):
        """
        method for process italic and bold
        """
        pass

    def build_list(self):
        pass

    def convert(self):
        pass


def main():
    import ipdb;ipdb.set_trace()

    fp = codecs.open('parser_test.md', 'r', encoding='utf-8')
    md_text = fp.read()
    fp.close()


if __name__ == "__main__":
    main()
