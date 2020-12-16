class user(object):
    users = []
        
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def save(self):    
      self.__class__.users.append(self)
    
    def __repr__(self):
        return 'User: %s, Idade: %s' % (self.nome, self.idade)
    
    @classmethod
    def all(cls):
      return cls.users