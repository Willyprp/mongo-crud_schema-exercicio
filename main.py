from unicodedata import name
from db.database import Database
from helper.WriteAJson import writeAJson

db = Database("db","Livros")
#db.create("Assassin's Creed. Odyssey","Gordon Doherty",2018,35.90)
db.create("Assassin's Creed: Valhalla: A Saga de Geirmund"," Matthew J. Kirby",2020,67.90)
# falta os itens 3 e 4
# deixar os itens 4 comentados no codigo

# item 1
#{
#  $jsonSchema: {
#    bsonType: 'object',
#    required: [
#      'titulo',
#      'autor',
#      'ano',
#      'preco'
#    ],
#    properties: {
#      titulo: {
#        bsonType: 'string',
#        description: 'nome do livro'
#      },
#      autor: {
#        bsonType: 'string',
#        description: 'autor do livro'
#      },
#      ano: {
#        bsonType: 'int',
#        description: 'ano de publicacao'
#      },
#      preco: {
#        bsonType: 'int',
#        description: 'preco da unidade'
#      }
#    }
#  }
#}

#item 4
# ano/1(asc)