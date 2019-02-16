"""
 1. Data structura : Dictionary, tuple, set

# Assignment:
 1. Create dictionary of user data
 2. Create list of user data dictionary with minimum of 10 user data
 3. Create 5 dictionaries which have list values
 """
# dictionary_variable = {'Name': 'Abhishek',
#                        'add': 'home',
#                        'cont_no1': '9856231470'
#                        }
#
# print(dictionary_variable)
# print(dictionary_variable['cont_no1'])
# print(dictionary_variable.get('name', "key does not found"))
# print(dictionary_variable.keys())
# print(dictionary_variable.values())
# print(dictionary_variable.items())
# cont_no = dictionary_variable['cont_no1']
# (dictionary_variable.pop('cont_no1'))
# print(dictionary_variable)
# dictionary_variable['cont_no'] = cont_no
# print(dictionary_variable)

dict_01 = [{'test1': 'test2', 'test3': 'test4'},
           {'test5': [{'test6': 'test7', 'test8': 'test9'},
                     {'test10': 'test11', 'test12': 'test13'}
                     ]
            }
           ]

print(dict_01[1]['test5'][1]['test12'])

dict_02 = {
           'test1': 'test2',
                            'test3':
                            [

                               {
                                   'test4': 'test5',
                                   'test6': [
                                             'test7', 'test8'
                                            ]
                               },
                                   [
                                       {
                                           'test9': 'test10'
                                       },
                                       'test11',
                                               {
                                                'test12': 'test13', 'test14': 'print_me'
                                               }
                                    ],

                                    {
                                        'test15': 'print_me_2'
                                    }
                            ]
           }

# print(dict_02['test3'][1][2]['test14'])
# print(dict_02['test3'][2]['test15'])
print(dict_02['test3'][1][0]['test9'])

# tuple_variable = (1,)
# print(tuple_variable)



