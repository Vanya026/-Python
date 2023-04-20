#todo: Заданы два списка. Необходимо их сериализовать в один файл.
import pickle
list_one = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
list_two = [False, 'Sparse is better than dense.', {'age': 90}]

filename = "data.pkl"
pkl_obj = [list_one, list_two]
fq = open(filename, 'wb')
pickle.dump(pkl_obj, fq, pickle.HIGHEST_PROTOCOL)
fq.close()

with open(filename, 'rb') as f:
    obj = pickle.load(f)
print(obj)    