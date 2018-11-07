import pandas as pd


def nutrient_checker(Category_list_male, Food_list, input_tag):
    treshold = 0.25

    input_tag = [item[0] for item in input_tag]

    input_nutrient_list = Category_list_male[Category_list_male['Tag'].isin(input_tag)]

    input_nutrient_sum = input_nutrient_list.sum()

    input_nutrient_sum = input_nutrient_sum.drop('Tag', 0)

    df = pd.DataFrame(input_nutrient_sum)
    print("Sum of nutrients from input image")
    df = df.sort_values(by=0)
    print(df, '\n')
    df = df[df[0] < treshold]

    lack_nutrient = list(df.index)
    print("List of lack nutrients")
    print(lack_nutrient, "\n")

    Food_list = Food_list.sort_values(by=lack_nutrient, ascending=False)

    Recommend_list = Food_list[0:3]
    Recommend_list = list(Recommend_list['Food'])
    print("Recommended food list")
    print(Recommend_list)
