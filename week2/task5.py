"""
Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в
текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с
паролями, но он не смог понять какой из паролей ему нужен. Помогите ему решить
эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл
результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода
simplecrypt.decrypt узнать, какой из паролей служит ключом для расшифровки
файла с интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы.
"""

#!/usr/bin/env python3
# coding=utf-8

import simplecrypt
import multiprocessing

def decrypt(data, password):
    try:
        res = simplecrypt.decrypt(password, data)
        print(res)
    except simplecrypt.DecryptionException:
        print("Password: {} is wrong".format(password))

def main():
    with open("encrypted.bin", "rb") as ef, open("passwords.txt", "r") as pwd:
        data = ef.read()
        processes = []
        
        for p in pwd:
            password = p.rstrip()
            t = multiprocessing.Process(target=decrypt, args=(data, password))
            processes.append(t)
            t.start()

        for t in processes:
            t.join()

if __name__ == "__main__":
    main()
