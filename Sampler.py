import numpy as np


class Generator:
    """
    This class generates data in double data structure
    given frequency and probability function values as 
    scalar * variable
    """
    frequency = 1
    number_of_dimensions = 1
    distribution = "uniform"
    scalar_factors = [1.0]
    
    def __init__(self, frequency = 1,
                 number_of_dimensions = 1 ,
                 distribution = "uniform",
                 scalar_factors = [1.0] ):
        

        # Extend scalars to size of dims if left as default
        if (number_of_dimensions > 1 and
            len(scalar_factors) == 1 and 
            scalar_factors[0] == 1.0):
            
                        scalar_factors = scalar_factors * number_of_dimensions
                
        if len(scalar_factors) != number_of_dimensions:
            raise Exception("Scalar factors length and number of dimension mismatch; " 
                            +  str(len(scalar_factors)) + ", " + str(number_of_dimensions))
           
        
        self.frequency = frequency
        self.number_of_dimensions = number_of_dimensions
        self.distribution = distribution
        # Convert to numpy array
        self.scalar_factors = np.asarray(scalar_factors)
    
    
    def generate(self):
        results = np.random.uniform(low=0.0, high=1.0, 
                                    size=(self.number_of_dimensions,))
        return np.multiply(self.scalar_factors, results)
