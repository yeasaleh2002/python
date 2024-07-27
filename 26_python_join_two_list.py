# python join two list
'''
- if we have 2 list then we can merge these list and make a list.
- we can use it by 2 method
- one is busing + ( ex: newListName = list1 + list2 )
- Another method is using extends() metnod. (ex: list1.extends(list2) )

'''

list1 = [1, 3, 4, 6, 6, 2, 1, 12];
list2 = ['sd', 'sg', 'hd', 'pc'];

# plus (+) method
newList1 = list1 + list2;
print("new list 1", newList1);

list2.extend(list1);
print("List 2", list2);