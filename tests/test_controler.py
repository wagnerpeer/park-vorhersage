import os.path
import sys
sys.path.append(os.path.join(os.path.abspath(os.getcwd()), 'src'))

from park_vorhersage import controler


if __name__ == "__main__":
    controler.create()
    controler.scrape_and_store()
