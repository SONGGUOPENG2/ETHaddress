from multiprocessing import Process
import os
import address_generate_encrypt
import address_generate_common
def common_generate():
    processes = []
    num_processes = os.cpu_count()  # 获取CPU核心数
    print("cpu核心数：", num_processes)
    num_processes = int(input("输入运行的核心数："))
    print("SONGGUOPENG正在加载进程！")
    for _ in range(num_processes):
        process = Process(target=address_generate_common.songguopeng)
        processes.append(process)
    print("进程正在陆续启动！")

    for process in processes:
        process.start()
    for process in processes:
        process.join()
if __name__ =='__main__':
    if True:
        common_generate()
    else:
        txt_file_path = "D:\其他\文件-不便列出\\alladdresses.txt"
        word_path = "D:\其他\文件-不便列出\助记词标准单词库.txt"
        txt_file_path = input("请输入address文件路径：")  # (注意\\转义字符)
        word_path = input("请输入mnemonic文件路径：")
        print("PENG正在加载地址文件！")
        addressall = address_generate_encrypt.read_addresses_from_file(txt_file_path)

        processes = []
        num_processes = os.cpu_count()  # 获取CPU核心数
        print("address文件加载完毕！")
        print("cpu核心数：", num_processes)
        num_processes = int(input("输入运行的核心数："))

        nums = []
        nums.append(int(input("输入第1区段起始点：")))
        nums.append(int(input("输入第1区段截止点：")))
        nums.append(int(input("输入第2区段起始点：")))
        nums.append(int(input("输入第2区段截止点：")))
        nums.append(int(input("输入第3区段起始点：")))
        nums.append(int(input("输入第3区段截止点：")))
        nums.append(int(input("输入第4区段起始点：")))
        nums.append(int(input("输入第4区段截止点：")))
        nums.append(int(input("输入第5区段起始点：")))
        nums.append(int(input("输入第5区段截止点：")))
        nums.append(int(input("输入第6区段起始点：")))
        nums.append(int(input("输入第6区段截止点：")))
        nums.append(int(input("输入第7区段起始点：")))
        nums.append(int(input("输入第7区段截止点：")))
        nums.append(int(input("输入第8区段起始点：")))
        nums.append(int(input("输入第8区段截止点：")))
        nums.append(int(input("输入第9区段起始点：")))
        nums.append(int(input("输入第9区段截止点：")))
        nums.append(int(input("输入第10区段起始点：")))
        nums.append(int(input("输入第10区段截止点：")))
        nums.append(int(input("输入第11区段起始点：")))
        nums.append(int(input("输入第11区段截止点：")))
        nums.append(int(input("输入第12区段起始点：")))
        nums.append(int(input(f"输入第12区段截止点，该区段长度必须是进程{num_processes}的整数倍：")))
        print("PENG正在加载进程！")

        kai = nums[22]
        shi = nums[23]
        everypan = (shi - kai) // num_processes
        startpan = nums[22]

        for _ in range(num_processes):
            process = Process(target=address_generate_encrypt.peng, args=(addressall, word_path, nums,))
            processes.append(process)
        print("进程正在陆续启动！")

        i = 0
        for process in processes:
            nums[22] = startpan + i * everypan
            nums[23] = nums[22] + everypan
            i = i + 1
            process.start()

        for process in processes:
            process.join()

        outall = input()

