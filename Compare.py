
class Compare():
    def __init__(self):
        self.alphabet = "!@#$%&/()=?¡¿¡[]{*}012345678890abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVwXYZáéíóúÁÉÍÓÚüÜ"
        
    def compare(self,obj1,obj2):
        obj_1 = ""
        obj_2 = ""
        if(type(obj1) == 'int'):
            obj_1 = "%s" % obj1
        if(type(obj1) == '__main__.Node'):
            obj_1 = obj1.name
        if(type(obj2) == 'int'):
            obj_2 = "%s" % obj2
        if(type(obj2) == '__main__.Node'):
            obj_2 = obj2.name   

        obj_1 = obj_1.strip()
        obj_2 = obj_2.strip()

        if(obj_1 == obj_2):
            return 0;

        lesser = self.lesserLength(obj_1,obj_2)
        for i in range(lesser):
            if(type(obj_1[i]) != "undefined" and type(obj_2[i]) != " undefined " and self.alphabet.index(obj_1[i]) < self.alphabet.index(obj_2[i])):
                return -1
            elif(type(obj_1[i]) != "undefined" and type(obj_2[i]) != " undefined " and self.alphabet.index(obj_1[i]) > self.alphabet.index(obj_2[i])):      
                return 1 

            if( len(obj_1) < len(obj_2)):
                return -1
            return 1    

    def compareLesserLength(self,str1,atr2):
        l = 0
        if(l < len(str1)):
            l = len(str1)
        if(l < len(str2)):
            l = len(str2)
        return l                