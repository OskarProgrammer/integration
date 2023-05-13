class Integration(object):
    def __init__(self,start:int,stop:int,accuracy):
        #entering content
        self._start = float(start)
        self._stop = float(stop)
        self._accuracy = float(accuracy)

        #loop jump calculation
        self._jump = ((self._stop - self._start)/self._accuracy)
        #pattern -> (end - beginning)/accuracy
    
    def func(self,x:float)->float:
        """
            function that returns the function value for a given argument
        """
        self._function = x**2 # here place your function

        return self._function

    def integration(self)->float:
        
        
        # initializing variables to make function "integration" works
        self._sum = 0 
        self._list = [0] #list with first element 0
        self._x = self._start

        
        #creating while loop, beacause for loop doesnt work with not integer jump
        while self._x<=self._stop:
            #skipping the first iteration because the self._pole would be 0!
            if self._x==self._start:
                self._x+=self._jump
                continue

            #pattern for self._pole = (value_of_current_self._x) * ( (current_arg)-(last_index_of_list) ) 
            self._pole = self.func(float(self._x)) * (float(self._jump))
            print(f"FOR {self._x} --> {self.func(self._x)} * ({self._x}-{self._list[-1]})")
            #adding result of self._pole to current value of self._sum
            self._sum += self._pole

            #adding current argument to the list to use it in the next iteration of loop
            self._list.append(self._x)

            #increasing the value of self._x by adding the self._jump that we calculated in
            # __init__ function by the pattern
            self._x += self._jump
            

        return self._sum

    def __str__(self):
        return f"self._start = {self._start}\nself._stop = {self._stop}\nself._accuracy = {self._accuracy}\nself._jump = {self._jump}"

obiekt = Integration(0, 5, 10)
print(obiekt)
result = obiekt.integration()
print(f"result => {result}")











# class Calkowanie_trapez:
#     def __init__(self, start, stop, dokladnosc):
#         self._start = start
#         self._stop = stop + 1
#         self._dok = dokladnosc

#         self._jump = ((self._stop-1-self._start)/self._dok)

#     def start(self):
#         self._result = self.calk()
#         print("Wynik calkowania funkcji {} z dokladnoscia {} wynosi {}".format(
#             self._funkcja, self._dok, self._result))

#     def f(self, x):
#         self._funkcja = None  # miejsce na funkcje
#         return self._funkcja

#     def calk(self):
#         self._sum = 0
#         self._list = [0]
#         for x in range(self._start, self._stop, self._jump):
#             self._podstawa1 = f(self._list[-1])
#             self._podstawa2 = f(x)
#             self._sumapod = self._podstawa1 + self._podstawa2

#             self._h = x - self._list[-1]

#             self._pole = (self._sumapod * self._h)/2
#             self._sum += self._pole

#             self._list.append(x)

#         return self._sum


# o = Calkowanie_prostokat(0, 5, 1000)

# o.start()