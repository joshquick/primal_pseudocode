
class MultiplexScheme(object):
    def run(self):
        while True:
            if region number is > 2:
                Calculate fwd primer left limit
            if region number is > 1:
                Calculate fwd primer left limit for region 2
            if region number == 1:
                Fwd primer left limit is 0 for region 1

            if region number > 1:
                Calculate fwd primer right limit to maintain minimum overlap
            if region number == 1:
                There is no fwd primer right limit for region 0 so set to max gap

            if region number >= 1:
                if remaining reference length is < amplicon length:
                    Set last region flag to True

            try:
                Run the findPrimers function and append region object to a list
            except no suitable primers:
                break

        Assign list of region objects to self


    def findPrimers(arguments):
        if region number == 1:
            Calculate where to slice the reference starting at 0
        elif last region flag:
            Calculate where to slice the reference working backwards
        else:
            Calculate where to slice the reference taking into account amplicon length and length variation

        Assign initial slice coordinates values

        Assign the default primer3 global arguments from settings
        Assign the default primer3 sequence arguments from settings
        Assign product size range for primer3 based on amplicon length and length variation
        Override number of primers for primer3 to return based on max candidates

        Set left limit flag to False
        while True:
            Slice primary reference according to coordinates calculated
            Assign primary reference slice to primer3 sequence arguments
            Assign length of primary reference slice to primer3 sequence arguments
            Run designPrimers function and assign output to variable
            Make an empty list
            for candidate primer in max candidates:
                Extract name, sequence and position from primer3 output dictionary
                Instantiate candidatePrimer object for fwd candidate
                Instantiate candidatePrimer object for rev candidate
                Instantiate candidatePrimerPair object with candidatePrimer objects
            if number of unique fwd and rev primers > 2:
                return Region(arguments)
            if region number == 1 or left limit flag is True:
                Increase slice coordinates by step size
                if slice end > length of primary reference:
                    raise no suitable primer exception
            else:
                Decrease slice coordinates by step size
                if slice start <= fwd primer left limit:
                    Set slice coordinates to initial values so as to begin opening a gap
                    Set left limit flag to True
