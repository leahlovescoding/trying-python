class functionalGroup:

    def __init__(self, singlebond, doublebond, triplebond):
        sigmabond= self.singlebond
        pisigmabond= self.doublebond
        pipisigmabond= self.triplebond


    def classify_it():
        if sigmabond == 1:
            (
            print ("this could be an Ethane funtional group")
            )
        elif pisigmabond == 1:
            (
            print ("this could be an Ethene funtional group")
            )
        elif pipisigmabond == 1:
            (
            print ("this could be an Ethyne funtional group")
            )

if __name__ == '__main__':
    group = functionalGroup
    group.classify_it()

Ethane = functionalGroup(1, 0, 0)
Ethene = functionalGroup(0, 1, 0)
Ethyne = functionalGroup(0, 0, 1)
