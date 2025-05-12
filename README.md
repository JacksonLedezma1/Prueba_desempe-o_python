<h1 align="center"> Performance testing in Python </h1>



## :hammer:Project Features

- `Add products to inventory`: This feature is designed to add products of any type, names with special characters and/or accents, to improve the user experience.
- `Check products in inventory`: This part of the project is designed to do two types of queries, explore the entire list or just search by name, you have to choose one. <3
- `Update product prices`: Modify the price of a specific product in inventory.
- `Remove products from inventory`: allow the removal of a product that is no longer in inventory
- `Calculate the total value of the inventory`: Multiply the price by the quantity of each product and display the running total.
- `Exit`: Salir del programa

## 📁 Project access

**The project can be accessed by downloading the .py file attached to this project**

## 🛠️ Open and run the project

**After downloading the project, you can use it in your favorite compiler and run it <3, the only requirement is to import the library re**

```bash
import re
```

## 🤔 How to use the program
As a first step, an interactive menu will appear.

![imagen](https://github.com/user-attachments/assets/fce72953-447f-4402-b910-463f7e85f57a)

Depending on what you select in the menu, other menus are activated, for example the section for adding products.

![imagen](https://github.com/user-attachments/assets/1cdc45d2-25e3-4a24-b8f1-f21501096bb4)

As you can see in the last image, I clearly show you how to add a product (there is an option that is displayed as "Do you want to do something else?", to add a product again you write "y" or if you want to exit that section just write "n"), obviously each part has its respective validations. Next I will show you how to consult products, there are two options just searching the name or printing the complete list of products.

![imagen](https://github.com/user-attachments/assets/e52c25c8-d174-42bd-881f-8bcd7f30d456)

As you can see, there are two ways to check products in the inventory; you can use whichever you prefer. Below, I'll show you how to update prices.

![imagen](https://github.com/user-attachments/assets/37e58097-f75f-43a1-a56c-f4d59b9010e7)

Same prices error.

In the image above, I show you the correct way to update prices in the program, where it shows the previous price and the updated price.

![imagen](https://github.com/user-attachments/assets/180aae70-2aed-46ae-abb6-a3cc1d7c466f)

Okay, in the image above I show you how to delete products from the inventory, with a brief security confirmation.

![imagen](https://github.com/user-attachments/assets/481b7ab1-e33e-4fac-b757-5bba9a687e22)

In this last image I show you what the option to calculate total value looks like.

At this point, all that's missing is the exit option. Entering 6 will close the program with a short message ("Goodbye..."). This short guide will show you how the code would work ideally. It's your job to find the errors and fix them. Good luck.
