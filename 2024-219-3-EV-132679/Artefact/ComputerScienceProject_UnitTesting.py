#Please run the programme as in artefact file. Close the "graphs and charts" pop-up window and then enter "1" to exit the programme.
#Then, the unit tests will be executed and displayed in the shell.

import unittest #In-built Python module. 

#imports "mean", "minimum", "maximum" and "median" functions from the main programme file "ComputerScienceProjectArtefact".

from ComputerScienceProjectArtefact import mean
from ComputerScienceProjectArtefact import minimum
from ComputerScienceProjectArtefact import maximum 
from ComputerScienceProjectArtefact import median

#The unit testing below is arranged in accordance to the "Triple-A-Model" (Arrange, Act and Assert).


#Class is used to sepreate unit test of different functions by their use and purpose.

#class authenticationTest(unittest.TestCase):
   
class dataAnalysisTest(unittest.TestCase):

    def testMeanFunction(self):
            
        #Arrange 
        listOfValues = [4, 5, 6, 7, 8, 9, 10]
        
        #Act
        result = mean(listOfValues)
        
        #Assert
        expectedMean = sum(listOfValues) / len(listOfValues)
        self.assertEqual(result, expectedMean)

    def testMinimumFunction(self):
            
        #Arrange 
        listOfValues = [4, 5, 6, 7, 8, 9, 10]
        
        #Act
        result = minimum(listOfValues)
        
        #Assert
        listOfValues.sort()
        expectedMinimum = listOfValues[0]
        self.assertEqual(result, expectedMinimum)

    def testMaximumFunction(self):
            
        #Arrange 
        listOfValues = [4, 5, 6, 7, 8, 9, 10]
        
        #Act
        result = maximum(listOfValues)
        
        #Assert
        listOfValues.sort()
        expectedMaximum = listOfValues[-1]
        self.assertEqual(result, expectedMaximum)
     
    def testMedianFunction(self):
            
        #Arrange 
        listOfValues = [4, 5, 6, 7, 8, 9, 10]
        
        #Act
        result = median(listOfValues)
        
        #Assert
        listOfValues.sort()
        if len(listOfValues) % 2 == 0:
            expectedMedian = (listOfValues[(len(listOfValues) // 2)-1] + listOfValues[(len(listOfValues) // 2)]) / 2
        else:
            expectedMedian = listOfValues[(len(listOfValues) // 2)]
        self.assertEqual(result, expectedMedian)

#The block of code below captures all of the tests in the imported file "ComputerScienceProjectArtefact" and runs then one by one.   
    
if __name__ == "__main__":
    unittest.main()   