import unittest
from MainClasses import *
import WildAnimals
import TradeSecrets
import FourthAmendment

#excluded due to data privacy concerns
#import NIHL


class Tests(unittest.TestCase):
    
    def test_wild_animals(self):
        
        adf = WildAnimals.adf()
        expOutcome = WildAnimals.expectedOutcomeCases()
        cases = WildAnimals.cases()   
        
        self.query_adf(adf,expOutcome,cases)
        
        adf = WildAnimals.adf()
        expOutcome = WildAnimals.expectedOutcomeCases()
        cases = WildAnimals.cases()
        
        self.save_import(adf,"TestWildAnimals",cases,expOutcome)
        
    def test_trade_secrets(self):
        
        adf = TradeSecrets.adf()
        expOutcome = TradeSecrets.expectedOutcomeCases()
        cases = TradeSecrets.cases()   
        
        self.query_adf(adf,expOutcome,cases)
        
        adf = TradeSecrets.adf()
        expOutcome = TradeSecrets.expectedOutcomeCases()
        cases = TradeSecrets.cases() 
        
        self.save_import(adf,"TestTradeSecrets",cases,expOutcome)
        
    def test_fourth_amendment(self):
        
        adf = FourthAmendment.adf()
        expOutcome = FourthAmendment.expectedOutcomeCases()
        cases = FourthAmendment.cases()   
        
        self.query_adf(adf,expOutcome,cases)
        
        adf = FourthAmendment.adf()
        expOutcome = FourthAmendment.expectedOutcomeCases()
        cases = FourthAmendment.cases()  
        
        self.save_import(adf,"TestFourthAmendment",cases,expOutcome)
        
    # def test_NIHL(self):
        
    #     adf = NIHL.adf()
    #     expOutcome = NIHL.expectedOutcomeCases()
    #     cases = NIHL.cases()   
        
    #     self.query_adf(adf,expOutcome,cases)
        
    #     adf = NIHL.adf()
    #     expOutcome = NIHL.expectedOutcomeCases()
    #     cases = NIHL.cases()  
        
    #     self.save_import(adf,"TestNIHL",cases,expOutcome)
        
    def save_import(self,adf,filename,cases,expOutcome):
        
        #keeps track of the old adf for comparison
        adf_old = adf
        
        adf.saveNew('{}'.format(filename))
                    
        file = "{}.xlsx".format(filename)
        adf_new = importADF(file,filename)
        
        #test nodes have the same name after import and that they are all present
        self.assertEqual(adf_old.nodes.keys(),adf_new.nodes.keys())
        
        #test the question order is the same in each
        self.assertEqual(adf_old.questionOrder, adf_new.questionOrder)
        
        #tests that the expected outcomes after the save/import are correct
        self.query_adf(adf_new,expOutcome,cases)
        
    def query_adf(self,adf,expectedOutcome,cases):
           
        for key,value in cases.items():

            #queries the case
            adf.evaluateTree(value)
            
            #removes the decide node from the outcome as not in the prolog
            try:
                adf.case.remove('Decide')
            except:
                pass
            
            #finds the expected outcome in the list of cases
            outcome = expectedOutcome[key]
            
            #removes the first item in the list which is a string of the expected outcome decision
            outcomeStatement = outcome.pop(0)
            
            #tests the outcomes are the same
            self.assertEqual(outcomeStatement,adf.statements[-1])
               
            #tests the individual fators are the same - converts each list into a set since order does not matter only equality
            self.assertEqual(set(adf.case),set(expectedOutcome[key]))
    
if __name__== '__main__':
    
    unittest.main()