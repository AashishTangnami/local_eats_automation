FOOD_CATGEGORIES = [
    {
    'Category Name' : 'Buy 1 Get 1 Free',
    'Category Desc' : ''
    },
    {
        'Category Name' : 'Chef Favorites',
     'Category Desc' : ''
     },
    {
        'Category Name' : 'Picked For You',
     'Category Desc' : ''
     },
    {
    'Category Name' : 'Create Your Own Masterpiece',
     'Category Desc' : ''}
]

ADDON_CATEGORIES = [
    {
        'Category Name': 'Pick Your Studio Crust',
        'Category Desc': ''
    },
    {
        'Category Name': 'Spread Your Sauce',
        'Category Desc': ''
    },
    {
        'Category Name': 'Choose Your Cheese',
        'Category Desc': ''
    },
    {
        'Category Name': 'Load Your Toppings',
        'Category Desc': ''
    },
    {
        'Category Name': 'Add Your Protein',
        'Category Desc': ''
    },
    {
        'Category Name': 'Specialty Toppings',
        'Category Desc': ''
    }
]

ADDON_ITEMS = [
    {
        'Addon Category Name': 'Pick Your Studio Crust',
        'Addon Items': [
            {
                'Add on Name': 'Traditional',
                'Add on Desc': '',
                'Price': '0.00'
            },
            {
                'Add on Name': 'Firecracker',
                'Add on Desc': '',
                'Price': '0.00'
            },
            {
                'Add on Name': 'Gluten Free Crust',
                'Add on Desc': '',
                'Price': '3.00'
            },
            {
                'Add on Name': 'Cauliflower Crust (GF)',
                'Add on Desc': 'Popular',
                'Price': '3.00'
            },
            {
                'Add on Name': 'Whole Grain & Flax Seed',
                'Add on Desc': '',
                'Price': '0.00'
            },
            {
                'Add on Name': 'Rosemary Herb Crust',
                'Add on Desc': '',
                'Price': '0.00'
            }
        ]
    }
]


FOOD_ITEM = [
    {
        'Food Item Name': 'Create Your Own 10" Pizza',
        'Food Item Desc': '10" Pizza with Unlimited Toppings!',
        'Price': '17.99',
        'Food Category': 'Create Your Own Masterpiece',
        'Addon Category': [
            {
                'Addon Category Name': 'Pick Your Studio Crust',
                'Addon Type': 'Can Select Only One',
                'Required': True,
                'Addon Items': [
                    'Cauliflower Crust (GF)',
                ]
            },
            {
                'Addon Category Name': 'Spread Your Sauce',
                'Addon Type': 'Can Select Muitiple',
                'Required': True,
                'Addon Items': [
                    'Classic Red Sauce',
                    'Spicy Red Sauce',
                    'BBQ Sauce',
                    'Olive Oil',
                    'Garlic Ranch Sauce',
                    'Buffalo Sauce'
                ]
            },
            {
                'Addon Category Name': 'Choose Your Cheese',
                'Addon Type': 'Can Select Only One',
                'Required': True,
                'Addon Items': [
                    'Mozzarella',
                    'Feta',
                    'Cheddar',
                    'Parmesan',
                    'Dairy Free Cheese',
                    'Vegan Cheese'
                ]
            },
            {
                'Addon Category Name': 'Load Your Toppings',
                'Addon Type': 'Can Select Multiple',
                'Required': False,
                'Addon Items': [
                    'Pepperoni',
                    'Sausage',
                    'Canadian Bacon',
                    'Bacon',
                    'Grilled Chicken',
                    'Meatballs',
                    'Salami',
                    'Anchovies',
                    'Artichoke Hearts',
                    'Black Olives',
                    'Green Olives',
                    'Mushrooms',
                    'Red Onions',
                    'Green Peppers',
                    'Banana Peppers',
                    'Jalapenos',
                    'Pineapple',
                    'Spinach',
                    'Roma Tomatoes',
                    'Sun-Dried Tomatoes',
                    'Fresh Basil',
                    'Fresh Garlic',
                    'Cilantro',
                    'Pesto',
                    'Roasted Red Peppers',
                    'Roasted Garlic',
                    'Roasted Mushrooms',
                    'Roasted Zucchini',
                    'Roasted Broccoli',
                    'Roasted Cauliflower',
                    'Roasted Potatoes',
                    'Roasted Carrots',
                    'Roasted Corn',
                    'Roasted Asparagus',
                    'Roasted Artichoke Hearts',
                    'Roasted Jalapenos',
                    'Roasted Green Peppers',
                ]
            },
            {
                'Addon Category Name': 'Add Your Protein',
                'Addon Type': 'Can Select Only One',
                'Required': False,
                'Addon Items': [
                    'Pepperoni',
                    'Sausage',
                    'Canadian Bacon',
                    'Bacon',
                    'Grilled Chicken',
                    'Meatballs',
                    'Salami',
                    'Anchovies',
                ]
            },
            {
                'Addon Category Name': 'Specialty Toppings',
                'Addon Type': 'Can Select Multiple',
                'Required': False,
                'Addon Items': [
                    'Pepperoni',
                    'Sausage',
                    'Canadian Bacon',
                    'Bacon',
                    'Grilled Chicken',
                    'Meatballs',
                    'Salami',
                    'Anchovies',
                ]
            },
            {
                'Addon Category Name': 'Specialty Toppings',
                'Addon Type': 'Can Select Multiple',
                'Required': False,
                'Addon Items': [
                    'Plant Based Meatballs'
                ]
            }
        ]

    }
]