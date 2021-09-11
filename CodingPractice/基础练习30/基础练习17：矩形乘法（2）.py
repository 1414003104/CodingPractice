# 矩阵乘法
def matrixMulti(matrix, factor):
    '''

    :param matrix: 原始矩阵
    :param factor: 指数
    :return: 结果矩阵
    '''
    # matrix1 保存原始矩阵的值， matrix2保存每次乘积后的结果
    matrix1 = matrix
    matrix2 = matrix

    # row 矩阵的行数， line 矩阵的列数， 求幂只能是方阵，可以只留一个
    row = len(matrix)
    line = len(matrix[0])

    # 当指数为0时候输出原始矩阵对应的单位矩阵
    if factor == 0:
        # resList 存储矩阵的结果
        resList = []
        for i in range(row):
            # resRow 存储矩阵中每一行的结果
            resRow = []
            for j in range(line):
                # 单位矩阵对角线上的数据为1，其他数据为0，
                '''
                第一行的resRow： 1 0 0 0 0 0 ...
                第二行的resRow： 0 1 0 0 0 0 ...
                第三行的resRow： 0 0 1 0 0 0 ...
                                ...
                '''
                if i==j:
                    resRow.append(1)
                else:
                    resRow.append(0)
            resList.append(resRow)
        return resList
    else:
        # factor次幂需要进行 factor-1 次矩阵乘法计算
        for i in range(factor-1):
            # resList 存储矩阵的结果
            resList = []
            for i in range(row):
                # rowList表示取出原始矩阵的第i行，随后需要乘以前次计算的结果矩阵matrix2的每一列，
                # 并将结果存入resRow中
                rowList = matrix1[i]
                resRow = []

                # j表示从matrix2中需要取出的列号
                for j in range(line):
                    res = 0
                    # rowList中取数，每个数需要乘以matrix2中对应行中的数
                    '''
                    rowList中第1个数，乘以matrix2中第1行的第j列的数
                    rowList中第2个数，乘以matrix2中第2行的第j列的数
                    rowList中第3个数，乘以matrix2中第3行的第j列的数
                                ...
                    最后求和存储到res中，res即是某次矩阵乘法计算出来的结果
                    '''
                    for index, num in enumerate(rowList):
                        res += num * matrix2[index][j]
                    # 然后将结果加入resRow中，此时resRow长度为line
                    resRow.append(res)
                # 再将某次计算的结果加入到总的结果中，resList长度为row
                resList.append(resRow)
            # 最后把结果赋值给matrix2，看是否需要继续计算，不需要则matrix2为最终结果
            matrix2 = resList
        return matrix2