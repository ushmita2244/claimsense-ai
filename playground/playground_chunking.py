text = """WAYS TO PREVENT CANCER
DON’T USE TOBACCO
Tobacco use (including cigarettes, cigars, hookah, chewing 
tobacco and more) has been linked to many types of cancer, 
including lung, colorectal, breast, throat, cervical, bladder, 
mouth and esophageal cancers. It’s best never to start using 
tobacco, but if you do use tobacco products, it’s never too 
late to quit.
According to the American Cancer Society, cigarette smoking rates reached 
a historic low in the U.S. in 2019. However, smoking still accounts for about 
30% of all cancer deaths. About 80 to 90% of all lung cancers are related to 
smoking.
Nonsmokers who are exposed to secondhand smoke are also at risk for cancer 
of the lungs and other sites, as well as other diseases. E-cigarettes also have 
serious health risks with increasing use seen among young people, which may 
lead to addiction or may also serve as a gateway to other tobacco products. 
The Prevent Cancer Foundation stands firm in discouraging the use of all 
tobacco products, including e-cigarettes.
PROTECT YOUR SKIN FROM THE SUN
Skin cancer is the most common cancer diagnosis in the U.S. and 
is also one of the most preventable cancers. Exposure to the sun’s 
ultraviolet radiation causes most skin cancers. Be sure to use 
adequate sun protection year-round. Never use indoor tanning beds.
EAT A PLANT-BASED DIET
Eat lots of fruits, vegetables, beans and whole grains, limit 
red meat and foods high in salt and cut out processed meats. 
Avoid drinks with added sugar. A large 2021 study found that 
three servings of vegetables (not starchy ones, like potatoes) 
and two of fruit (not juice) every day resulted in a 10% lower 
risk of death from cancer.
LIMIT ALCOHOL
Drinking alcohol is linked to several cancers, including breast, 
colorectal, esophageal, oral and liver cancers. To reduce your 
risk of cancer, it’s best to avoid alcohol completely. If you drink, 
limit your drinking to no more than one drink a day if you are 
a woman, and no more than one or two a day if you are a man. 
The more you drink, the greater your risk of cancer.
MAINTAIN A HEALTHY WEIGHT AND BE 
PHYSICALLY ACTIVE
Obesity is linked to many cancers, including those of the 
endometrium, liver, kidney, pancreas, colon, breast (especially 
in post-menopausal women) and more. """

chunk_size = 40

for i in range(0, len(text), chunk_size):
    print("=" * 40)
    print(text[i:i+chunk_size])