
class Primer(object):
    def __init__(self, arguments):
        Instantiate simple primer class

class CandidatePrimer(Primer):
    def __init__(self, arguments):
        super(CandidatePrimer, self).__init__(arguments)
        Instantiate super class for candidate primer with more extensive attributes

class CandidatePrimerPair(object):
    def __init__(self, arguments):
        Instantiate class for candidate primer pair

class Region(object):
    def __init__(self, arguments):
        Instantiate a region class, perform alignments with Calignment function and generate alts

class CAlignment(object):
    def __init__(self, arguments):
        Instantiate an alignment object and perform a fast glocal alignment
