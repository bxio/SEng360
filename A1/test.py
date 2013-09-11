import optparse

parser = optparse.OptionParser()

parser.add_option('-b', help='boolean option', dest='bool', \
    default=False, action='store_true')

(opts, args) = parser.parse_args()
