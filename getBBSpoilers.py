#Birchbox spoilers util by ThePolymath
#2016
import requests
import urllib
import sys
from bs4 import BeautifulSoup
import argparse


def main(args):
    box_date = args.month + "-" + args.year;
    host = "https://www.birchbox.com/shop/birchbox-1/{d}/{d}-bb"
    host = host.replace("{d}", box_date);
    for x in range(1,71):
        box_url = host + str(x)
        response = requests.head(box_url)
        if response.status_code != 404:
            print box_url
            if args.show_items:
              	html = urllib.urlopen(box_url).read()
              	soup = BeautifulSoup(html, "html.parser")
              	for product in soup.findAll("a", { "class" : "product_name track-event" }):
          	        print product.contents[0].encode('utf-8').strip()
              	print "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Print boxes for a given month and year.')
    parser.add_argument('--month', required=True, help='Month of box.')
    parser.add_argument('--year', required=True, help='Year of box.')
    parser.add_argument('--show_items', required=False, 
                      default=False, help='If True, print the products contained in each box.')
    parser.add_argument('--output_file', required=False, 
                      default=False, help='If specified, write output to specified text file.  If flag is not used, data will be printed to console')
    args = parser.parse_args()

    if args.output_file:
        print "Writing boxes to file " + args.output_file
        orig_stdout = sys.stdout
        f = file(args.output_file, 'w')
        sys.stdout = f
        main(args)
        sys.stdout = orig_stdout
        f.close()
    else:
        print "Writing boxes to cmdline"
        main(args)

    print "Box searching has completed"
