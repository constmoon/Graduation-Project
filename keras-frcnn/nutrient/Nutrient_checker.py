import pandas as pd


def nutrient_checker(input_tag):
    treshold = 0.25

    # input_tag = ["bulgogi", "gim", "rice"]
    input_tag = [item[0] for item in input_tag]


    Category_list_male = pd.read_csv("category_male.csv")

    input_nutrient_list = Category_list_male[Category_list_male['Tag'].isin(input_tag)]

    input_nutrient_sum = input_nutrient_list.sum()

    input_nutrient_sum = input_nutrient_sum.drop('Tag', 0)

    df = pd.DataFrame(input_nutrient_sum)
    print("Sum of nutrients from input image")
    print(df, '\n')
    df = df.sort_values(by=0)
    df = df[df[0] < treshold]

    lack_nutrient = list(df.index)
    print("List of lack nutrients")
    print(lack_nutrient, "\n")


    Food_list = pd.read_csv('nutrients.csv')

    Food_list = Food_list.sort_values(by=lack_nutrient, ascending=False)

    Recommend_list = Food_list[0:3]
    Recommend_list = list(Recommend_list['Food'])
    print("Recommended food list")
    print(Recommend_list)


nutrient_checker([('bulgogi', 92.15009808540344), ('sangchu', 94.08701062202454)])