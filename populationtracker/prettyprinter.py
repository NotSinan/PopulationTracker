from tabulate import tabulate

class PrettyPrinter():

    def prettyprint(self, data):
        print(tabulate(data, headers=['World', 'Change']))
