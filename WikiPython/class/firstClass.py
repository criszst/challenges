class user(object):
    users = []

    def __init__(self, nome, Id):
        self.nome = nome
        self.Id = Id

    def save(self):    
      self.__class__.users.append(self)
      
    def find(self):
      msg = ''
      if self in self.__class__.users:
        msg = print(f'\nUsuário encontrado:\n[Nome: {self.nome}, Id: {self.Id}]')
      else:
        msg = print('Usuário não encontrado.')
        
      return msg

    def __repr__(self):
        return 'User: %s, Id: %s' % (self.nome, self.Id)

    @classmethod
    def all(cls):
      return cls.users
    
xpto = user('XXXX', '99')

a = user('aaaa', '222')

xpto.save()
a.save()

print(user.find(a))