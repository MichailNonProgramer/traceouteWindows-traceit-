import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('-m', type=int, dest='max_hops', default=30,
                        help='Maximum number of hops to search for target.')

    parser.add_argument('-t', '-max_time',type=float, dest='max_time',
                        default=120000.0,
                        help='Maximum times to search for target.')

    parser.add_argument('-w', '-timeout', type=float, dest='timeout',
                        default=4000.0,
                        help='Wait timeout milliseconds for each reply.')

    parser.add_argument('target_name', nargs=1)

    return parser.parse_args()