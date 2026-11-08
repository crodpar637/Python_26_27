from functools import reduce

class RecipeBook:
    def __init__(self):
        self.__recipes = {}

    def add_recipe(self, name, ingredient_list):
        if name in self.__recipes.keys():
            return "La receta ya existe en el libro"
        else:
            self.__recipes[name] = ingredient_list
            return "La receta se ha agregado en el libro"

    def get_recipe_weight(self,name):
        if name not in self.__recipes.keys():
            return 0

        ingredients_list = self.__recipes[name]
        # [("Huevos", 200), ("Patatas", 500)]
        # ingrediente = ("Huevos", 200)  --> ingrediente[1] = 200
        
        lista_pesos = map(lambda ingrediente: ingrediente[1], ingredients_list)

        suma_pesos = reduce(lambda x,y : x+y, lista_pesos)

        return suma_pesos


    
        

    def __str__(self):
        listado =""

        # for item in self.__recipes.items(): ### item[0] item[1]
        for (name, ingredients_list) in self.__recipes.items():
            listado += "Receta:" + name + "\n"  # f"Receta: {name}"
            for ingredient in ingredients_list:
                #- Huevos: 200g
                #listado += "- " + ingredient[0] + ": " + ingredient[1] + "g\n"
                listado += f"- {ingredient[0]}: {ingredient[1]}g\n"
            # En cada cambio de receta
            listado += "-"*60 + "\n"

        return listado

    def find_recipes_by_ingredient(self,ingredient_name):
        lista = []

        for item in self.__recipes.items():
            # item[0] --> nombre receta
            # item[1] --> lista tuplas ingredientes
            for ingrediente in item[1]:
                #ingrediente --> tupla ingrediente
                #ingrediente[0] --> nombre ingrediente
                #ingrediente[1] --> peso ingrediente
                if ingrediente[0] == ingredient_name:
                    lista.append(item[0])

        return lista

# main
def main():
    #instanciar el libro de recetas
    r = RecipeBook()

    print(r.add_recipe("Tortilla",[("Huevos", 200), ("Patatas", 500)]))
    print(r.add_recipe("Tortilla",[("Huevos", 200), ("Patatas", 500)]))
    print(r.add_recipe("Tortilla francesa",[("Huevos", 200)]))
    print(r.add_recipe("Bizcocho",[("Harina", 250), ("Azúcar", 200), ("Huevos", 150)]))
    print(r.add_recipe("Ensalada", [("Lechuga", 100), ("Tomate", 150)] ) )

    # print(r.__str__())
    print(r)

    print("Peso Tortilla:", r.get_recipe_weight("Tortilla"))
    print("Peso Tortilla camarones:", r.get_recipe_weight("Tortilla camarones"))
    print("Peso Bizcocho:", r.get_recipe_weight("Bizcocho"))

    print("Recetas que usan Huevos:", r.find_recipes_by_ingredient("Huevos"))

main()
          
"""
d = 
{
"Tortilla": [("Huevos", 200), ("Patatas", 500)],
"Bizcocho": [("Harina", 250), ("Azúcar", 200), ("Huevos", 150)],
"Ensalada": [("Lechuga", 100), ("Tomate", 150)]
}
    d.items()
[ ("Tortilla",[("Huevos", 200), ("Patatas", 500)]), ...   ] 

1 item --> ("Tortilla",[("Huevos", 200), ("Patatas", 500)])
item[0] --> "Tortilla"
item[1] --> [("Huevos", 200), ("Patatas", 500)]
item[1][0] --> ("Huevos", 200)
"""
        
           
            

    