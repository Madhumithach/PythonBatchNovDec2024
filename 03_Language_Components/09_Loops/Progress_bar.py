"""
Assignment: Progress bar implementation
    [          ]   3
    [*         ]  10
    [**        ]  20
    [***       ]  30
    [****      ]  40
    [*****     ]  50
    [******    ]  60
    [*******   ]  70
    [********  ]  80
    [********* ]  90
    [**********] 100
"""
total_allocation=10
space_allocation=10
star_allocation=total_allocation-space_allocation
for i in range(0,110,10):
    string=f"[{star_allocation} * '*' {space_allocation} * ' ']"
    print(string)
    space_allocation-=1
