def partition_with_index(test,index):
    before=test[:index]
    at_index=test[index]
    after_index=test[index+1:]
    return before,at_index,after_index



test="Python is interesting"
result=partition_with_index(test,4)
print("Result :",result)