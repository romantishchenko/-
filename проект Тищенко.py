class Polynomial:

    def __init__(self, *coefficients):
        
        if type(coefficients[0]) == dict:
            max_ = 0
            for k in coefficients[0].keys():
                if k > max_:
                    max_ = k
            coeff_list = [0] * (max_ + 1)
            for k in coefficients[0].keys():
                coeff_list[k] = coefficients[0].get(k)  
            ind, sl_ = 0, len(coeff_list)
            for i in range(len(coeff_list) - 1, -1, -1):
                if ind == 0 and coeff_list[i] == 0:
                    sl_ = i
                else:
                    ind = 1
            self.p = coeff_list[:sl_]
            
        elif type(coefficients[0]) == int: 
            coeff_list = list(coefficients)
            ind, sl_ = 0, len(coeff_list)
            for i in range(len(coeff_list) - 1, -1, -1):
                if ind == 0 and coeff_list[i] == 0:
                    sl_ = i
                else:
                    ind = 1
            self.p = coeff_list[:sl_]
        
        elif type(coefficients[0]) == list:
            coefficients = list(coefficients[0])
            ind, sl_ = 0, len(coefficients)
            for i in range(len(coefficients) - 1, -1, -1):
                if ind == 0 and coefficients[i] == 0:
                    sl_ = i
                else:
                    ind = 1
            self.p = coefficients[:sl_]
            
        elif type(coefficients[0]) == Polynomial:
            self.p = coefficients[0].p
    
    
    def __repr__(self):
        return 'Polynomial ' + str(self.p)
    
    
    def __str__(self):
        
        def sgn(n, i, end):
            if n != 0:
                if end == 0: 
                    if i == 0:
                        if str(n)[0] == '-':  
                            return ' - ' + str(n)[1:] 
                        elif str(n)[0] != '-':
                            return ' + ' + str(n)
                    elif i == 1:
                        if str(n)[0] == '-':
                            if str(n)[1:] != '1':
                                return ' - ' + str(n)[1:] + 'x'
                            else:
                                return ' - ' + 'x'
                        elif str(n)[0] != '-':
                            if str(n) != '1':
                                return ' + ' + str(n) + 'x'
                            else:
                                return ' + ' + 'x'
                    else:
                        if str(n)[0] == '-':  
                            if str(n)[1:] != '1':
                                return ' - ' + str(n)[1:] + 'x^' + str(i)
                            else:
                                return ' - ' + 'x^' + str(i)
                        elif str(n)[0] != '-':
                            if str(n) != '1':
                                return ' + ' + str(n) + 'x^' + str(i)
                            else:
                                return ' + ' + 'x^' + str(i)
                else:
                    if i == 0:
                        if str(n)[0] == '-':    
                            return '-' + str(n)[1:]
                        elif str(n)[0] != '-':
                            return str(n)
                    elif i == 1:
                        if str(n)[0] == '-':
                            if str(n)[1:] != '1':
                                return str(n) + 'x'
                            else:
                                return '-x'
                        elif str(n)[0] != '-':
                            if str(n)[1:] != '1':
                                return str(n) + 'x'
                            else:
                                return 'x'
                    else:
                        if str(n)[0] == '-':
                            if str(n)[1:] != '1':
                                return str(n) + 'x^' + str(i)
                            else:
                                return '-x^' + str(i)
                        elif str(n)[0] != '-':
                            if str(n)[1:] != '1':
                                return str(n) + 'x^' + str(i)
                            else:
                                return 'x^' + str(i)
            else:
                return ''
                
        
        s = sgn(self.p[-1], len(self.p) - 1, end=1)
        for i in range(len(self.p) - 2, -1, -1):
            s += sgn(self.p[i], i, end=0)
            
        return s
    
    
    def __eq__(self, other):
        return self.p == other.p
    

    def __add__(self, other):
        if type(self) == int and type(other) == int:
            ans = list(self + other)
            return Polynomial(ans)
        elif type(self) == int and type(other) != int:
            other.p[0] += self
            return Polynomial(other.p)
        elif type(self) != int and type(other) == int:
            self.p[0] += other
            return Polynomial(self.p)
        else:
            i, j, res = 0, 0, []
            while i < len(self.p) and j < len(other.p):
                res.append(self.p[i] + other.p[j])
                i += 1
                j += 1
            for k_1 in range(i, len(self.p)):
                res.append(self.p[k_1])
            for k_2 in range(j, len(other.p)):
                res.append(other.p[k_2])
            return Polynomial(res)
    
    
    __radd__ = __add__
    

    def __neg__(self):
        for i in range(len(self.p)):
            self.p[i] = -self.p[i]
        return Polynomial(self.p)
    
    
    def __sub__(self, other):
    
        if type(self) != int and type(other) == int:
            self.p[0] -= other
            return Polynomial(self.p)
        else:
            i, j, res = 0, 0, []
            while i < len(self.p) and j < len(other.p):
                res.append(self.p[i] - other.p[j])
                i += 1
                j += 1
            for k_1 in range(i, len(self.p)):
                res.append(self.p[k_1])
            for k_2 in range(j, len(other.p)):
                res.append(-other.p[k_2])
            return Polynomial(res)
    
    
    def __rsub__(self, other):
        
        if type(self) != int and type(other) == int:
            self = -self
            self.p[0] += other
            return Polynomial(self.p)
        else:
            i, j, res = 0, 0, []
            while i < len(self.p) and j < len(other.p):
                res.append(self.p[i] - other.p[j])
                i += 1
                j += 1
            for k_1 in range(i, len(self.p)):
                res.append(self.p[k_1])
            for k_2 in range(j, len(other.p)):
                res.append(-other.p[k_2])
            return Polynomial(res)

    
    def __call__(self, x):
        sum_ = 0
        for k in range(len(self.p)):
            sum_ += self.p[k] * (x ** k)
        return sum_
    

    def degree(self):
        if len(self.p) > 0:
            return len(self.p) - 1
        else:
            return 0