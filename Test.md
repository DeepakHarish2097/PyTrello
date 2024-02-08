# Test

### Default Context
```
context = {
        "bread_crumbs": ["Breadcrumb 1", "Breadcrumb 2", "Breadcrumb 3"],
        "last_crumb": "Breadcrumb 3",
        "board_groups": [
            {
                "name": "Board Group 12345678910",
                "boards": [
                    {
                        "name": "Board 1",
                        "id": "bd-1"
                    },
                    {
                        "name": "Board 2",
                        "id": "bd-2"
                    },
                    {
                        "name": "Board 3",
                        "id": "bd-3"
                    },
                ]
            },
            {
                "name": "Board Group 2",
                "boards": [
                    {
                        "name": "Board 4",
                        "id": "bd-4"
                    },
                    {
                        "name": "Board 5",
                        "id": "bd-5"
                    },
                    {
                        "name": "Board 6",
                        "id": "bd-6"
                    },
                ]
            },
            {
                "name": "Board Group 3",
                "boards": [
                    {
                        "name": "Board 7",
                        "id": "bd-7"
                    },
                    {
                        "name": "Board 8",
                        "id": "bd-8"
                    },
                    {
                        "name": "Board 9",
                        "id": "bd-9"
                    },
                ]
            },
        ],
        "other_boards": [
            {
                "name": "Board 10",
                "id": "bd-10",
            },
            {
                "name": "Board 11",
                "id": "bd-11"
            },
            {
                "name": "Board 12",
                "id": "bd-12"
            },
            {
                "name": "Board 13",
                "id": "bd-13"
            }
        ],
        "active_menu": "bd-9"
    }
    
```

### To get url from redirect
`print(redirect('project_view', id=id).url)`
