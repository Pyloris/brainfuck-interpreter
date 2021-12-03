# a simple brainfuck interpreter written in python

class BrainFuck:
    
    """
        THIS CLASS IMPLEMENTS ALL THE FUNCTIONALITY OF A BRAINFUCK INTERPRETER
        YOU CAN WIRTE BRAINFUCK CODE AND GIVE IT TO THIS INTERPRETER
        IT WILL RUN IT FOR YOU!!
        brainfuck(code)
        # it is great
    """
    
    def __init__(self, bf):
        # contains all the cells in list
        self.vars = [0]
        # contains offset of current cell
        self.ptr = 0
        # contains code string
        self.bf = bf
        # contains current offset in code being executed
        self.code_offset = 0
        # contains all positions of '[' as we have
        # to loop back to it when ']' is found
        self.locators = []
        
    # '+' adding functions to the operators
    def add_symbol(self):
        self.vars[self.ptr] += 1
    
    # '-' subtract function
    def sub_symbol(self):
        self.vars[self.ptr] -= 1
    
    #'>'  move cell pointer forward 
    def move_forward(self):
        if self.ptr < len(self.vars)-1:
            self.ptr+=1 
        else:
            self.vars.append(0)
            self.ptr+=1
    
    # '<' move cell pointer backward
    def move_backward(self):
        if self.ptr > 0:
            self.ptr -= 1
    
    # this method outputs the value in current cell
    def output(self):
        if isinstance(self.vars[self.ptr], int):
            print(chr(self.vars[self.ptr]), end="")
        else:
            print(self.vars[self.ptr], end="")
        
    # this method take a single character
    # and puts it in current cell
    def input_char(self):
        try:
            self.vars[self.ptr] = input()[0]
        except IndexError:
            print("YO PUT SOMETHING IN THERE!!")
    
    # '[' check if current cell is 0 
    # just jump to corresponding ']'
    # otherwise keep moving
    def current_0_forward(self):
        
        # skip or move to next placeholder
        if self.vars[self.ptr] == 0:
            # put current code offset in temp
            temp = self.code_offset
            # find next occurence of ']'
            # we will use this to keep track of current
            # loop as we may have nested loops
            # match right [] we will use this to
            # to get out of the depth
            current_start = 0
            # loop to iterate over code and find the next ]
            while temp < len(self.bf):
                # if [ is found just 
                if self.bf[temp] == '[':
                    current_start+=1
                elif self.bf[temp] == ']':
                    if current_start == 0:
                        break
                    else:
                        current_start-=1
                temp+=1
            # find next ']'
            # and skip to it
            self.code_offset = temp-1
            # pop the last item as it is useless now
            self.locators.pop()
        else:
            # move to ']'
            # push current index into locators
            self.locators.append(self.code_offset)
            
    
    # ']' check if current cell is 0
    # if true move forward to next char
    # otherwise move back to '['
    def current_0_backward(self):
        if self.vars[self.ptr] != 0:
            # take the last value in locators
            # and jump back to that offset
            # jump to ']'
            self.code_offset = self.locators[-1]
        else:
            self.locators.pop()
            
    # this is the function to inc code offset
    # to point to next char
    def inc_code_offset(self):
        self.code_offset+=1
    
    # this method executes current character
    # at the offset pointer
    def evaluate(self):
        # keep executing until end
        while self.code_offset < len(self.bf):
            print(self.vars)
            # exec func based on operator
            if self.bf[self.code_offset] == '+':
                self.add_symbol()
            elif self.bf[self.code_offset] == '-':
                self.sub_symbol()
            elif self.bf[self.code_offset] == '>':
                self.move_forward()
            elif self.bf[self.code_offset] == '<':
                self.move_backward()
            elif self.bf[self.code_offset] == '[':
                self.current_0_forward()
            elif self.bf[self.code_offset] == ']':
                self.current_0_backward()
            elif self.bf[self.code_offset] == '.':
                self.output()
            elif self.bf[self.code_offset] == ',':
                self.input_char()

            self.inc_code_offset()


# trying above class out
Compiler = BrainFuck('++[>++[>++[>++<-]<-]<-]>>+++.')

Compiler.evaluate()