import matplotlib.pyplot as plt
import numpy as np

def draw():
    # 数据
    x = [1, 2, 3, 4, 5]
    y1 = [2, 3, 5, 7, 6]
    y2 = [1, 2, 4, 5, 3]
    offset = 0.6  # 偏移量

    # 绘图
    plt.plot(x, y1, color='orange', marker='s', label='Line 1')  # 黄色折线 正方形标记
    plt.plot(x, y2, color='red', marker='o', label='Line 2')     # 红色折线 圆形标记

    # 在每个点上显示纵坐标的数值，并设置颜色
    for i in range(len(x)):
        plt.text(x[i], y1[i]+ offset, str(y1[i]), ha='center', va='bottom', color='orange')
        plt.text(x[i], y2[i]+ offset, str(y2[i]), ha='center', va='bottom', color='red')

    # 添加标题和标签
    plt.title('Two Lines')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # 添加图例
    plt.legend(loc='lower right')

    # 添加网格
    plt.grid(True)

    # 显示图形
    plt.show()

def draw_2():
    # 数据
    x = [5, 10, 20, 50, 100]
    y1 = [9.8, 12.2, 14.5, 17.6, 20.5]
    y2 = [7.1, 9.9, 13.3, 16.7, 19.6]
    y3 = [13.1, 15.5, 18.3, 21.7, 25.2]
    y4 = [8.4, 12.4, 15.9, 20.1, 23.9]
    offset = 0.5  # 偏移量

    # 创建子图
    fig, axs = plt.subplots(1, 2, figsize=(10, 7), gridspec_kw={'width_ratios': [1, 1]})

    # 绘制第一个子图
    axs[0].plot(x, y1, color='orange', marker='s',markersize=10, label='IN-1M DAP')  # 橙色折线，正方形标记
    axs[0].plot(x, y2, color='red', marker='o',markersize=10, label='IN-1M CLS')  # 红色折线，圆形标记

    # 在每个点上显示纵坐标的数值，并设置颜色和加粗
    for i in range(len(x)):
        axs[0].text(x[i], y1[i] + offset, str(y1[i]), ha='center', va='bottom', color='orange')
        axs[0].text(x[i], y2[i] - offset, str(y2[i]), ha='center', va='top', color='red')

    # 添加标题和标签
    # axs[0].set_title('Line Chart 1')
    axs[0].set_xlabel('k-shot per class', fontsize=14)
    # axs[0].set_ylabel('Y-axis')
    # axs[0].set_ylabel(r'$Y_{\mathrm{axis}}$')  # 使用LaTeX语法设置纵坐标标签
    axs[0].set_ylabel(r'$AP_{\mathrm{.5:.95}}$ (%) on COCO 2017 val', fontsize=14)
    axs[0].grid(True)

    # 添加图例并放在右下角
    axs[0].legend(loc='lower right',fontsize=12)

    # 设置第一个子图的横坐标
    # axs[0].set_xticks(x)

    # 绘制第二个子图
    axs[1].plot(x, y3, color='orange', marker='s',markersize=10, label='IN-14M DAP')  # 橙色折线，正方形标记
    axs[1].plot(x, y4, color='red', marker='o',markersize=10, label='IN-14M CLS')  # 红色折线，圆形标记

    # 在每个点上显示纵坐标的数值，并设置颜色和加粗
    for i in range(len(x)):
        axs[1].text(x[i], y3[i] + offset, str(y3[i]), ha='center', va='bottom', color='orange')
        axs[1].text(x[i], y4[i] - offset, str(y4[i]), ha='center', va='top', color='red')

    # 添加标题和标签
    # axs[1].set_title('Line Chart 2')
    axs[1].set_xlabel('k-shot per class',fontsize=14)
    axs[1].set_ylabel('Y-axis')
    axs[1].grid(True)

    # 添加图例并放在右下角
    axs[1].legend(loc='lower right',fontsize=12)

    # 设置第二个子图的横坐标
    # axs[1].set_xticks(x)

    # 设置两个子图的对数横坐标轴
    axs[0].set_xscale('log')
    axs[1].set_xscale('log')
    axs[0].set_yscale('log')
    axs[1].set_yscale('log')

    # 设置对数坐标轴的刻度和标签
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(x)
    axs[1].set_xticks(x)
    axs[1].set_xticklabels(x)

    # # 设置纵坐标刻度
    # axs[0].set_yticks([7, 10, 15, 20, 25])
    # axs[0].set_yticklabels([7, 10, 15, 20, 25])
    # axs[1].set_yticks([7, 10, 15, 20, 25])
    # axs[1].set_yticklabels([7, 10, 15, 20, 25])

    # 设置纵坐标刻度
    axs[0].set_yticks([7, 10, 15, 20, 25])
    axs[0].set_yticklabels([7, 10, 15, 20, 25])
    axs[1].set_yticks([7, 10, 15, 20, 25])
    axs[1].set_yticklabels([''] * len([7, 10, 15, 20, 25]))  # 隐藏右图的纵坐标刻度标签

    # 设置纵坐标范围，略微超过最大值
    max_y = max(max(y4), max(y3)) + 1
    axs[0].set_ylim([0, max_y])
    axs[1].set_ylim([0, max_y])

    # 设置第二个子图的纵坐标范围与第一个子图一致
    axs[1].set_ylim(axs[0].get_ylim())

    # 调整子图之间的间距
    plt.tight_layout()

    # 隐藏右图的纵坐标标签和名字
    axs[1].set_yticklabels([])
    axs[1].set_ylabel('')

    # 保存
    plt.savefig('fig_coco_few100_log_new.pdf', format='pdf')

    # 显示图形
    plt.show()

def draw_3():
    # 数据
    x = [5, 10, 20, 50, 100]
    y1 = [40.1, 52.0, 60.5, 67.9, 71.8]
    y2 = [26.7, 40.8, 52.8, 63.3, 70.6]
    y3 = [50.7, 59.7, 68.3, 73.8, 77.4]
    y4 = [31.2, 43.5, 58.8, 70.0, 75.3]
    offset = 0.5  # 偏移量

    # 创建子图
    fig, axs = plt.subplots(1, 2, figsize=(10, 7), gridspec_kw={'width_ratios': [1, 1]})

    # 绘制第一个子图
    axs[0].plot(x, y1, color='orange', marker='s', markersize=10, label='IN-1M DAP')  # 橙色折线，正方形标记
    axs[0].plot(x, y2, color='red', marker='o', markersize=10, label='IN-1M CLS')  # 红色折线，圆形标记

    # 在每个点上显示纵坐标的数值，并设置颜色和加粗
    for i in range(len(x)):
        axs[0].text(x[i], y1[i] + offset, str(y1[i]), ha='center', va='bottom', color='orange')
        axs[0].text(x[i], y2[i] - offset, str(y2[i]), ha='center', va='top', color='red')

    # 添加标题和标签
    # axs[0].set_title('Line Chart 1')
    axs[0].set_xlabel('k-shot per class', fontsize=14)
    # axs[0].set_ylabel('Y-axis')
    # axs[0].set_ylabel(r'$Y_{\mathrm{axis}}$')  # 使用LaTeX语法设置纵坐标标签
    axs[0].set_ylabel(r'$AP_{\mathrm{.5}}$ (%) on VOC 2007 test', fontsize=14)
    axs[0].grid(True)

    # 添加图例并放在右下角
    axs[0].legend(loc='lower right', fontsize=12)

    # 设置第一个子图的横坐标
    # axs[0].set_xticks(x)

    # 绘制第二个子图
    axs[1].plot(x, y3, color='orange', marker='s', markersize=10, label='IN-14M DAP')  # 橙色折线，正方形标记
    axs[1].plot(x, y4, color='red', marker='o', markersize=10, label='IN-14M CLS')  # 红色折线，圆形标记

    # 在每个点上显示纵坐标的数值，并设置颜色和加粗
    for i in range(len(x)):
        axs[1].text(x[i], y3[i] + offset, str(y3[i]), ha='center', va='bottom', color='orange')
        axs[1].text(x[i], y4[i] - offset, str(y4[i]), ha='center', va='top', color='red')

    # 添加标题和标签
    # axs[1].set_title('Line Chart 2')
    axs[1].set_xlabel('k-shot per class', fontsize=14)
    axs[1].set_ylabel('Y-axis')
    axs[1].grid(True)

    # 添加图例并放在右下角
    axs[1].legend(loc='lower right', fontsize=12)

    # 设置第二个子图的横坐标
    # axs[1].set_xticks(x)

    # 设置两个子图的对数横坐标轴
    # axs[0].set_xscale('log')
    # axs[1].set_xscale('log')
    # axs[0].set_yscale('log')
    # axs[1].set_yscale('log')

    # 设置对数坐标轴的刻度和标签
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(x)
    axs[1].set_xticks(x)
    axs[1].set_xticklabels(x)

    # # 设置纵坐标刻度
    # axs[0].set_yticks([7, 10, 15, 20, 25])
    # axs[0].set_yticklabels([7, 10, 15, 20, 25])
    # axs[1].set_yticks([7, 10, 15, 20, 25])
    # axs[1].set_yticklabels([7, 10, 15, 20, 25])

    # 设置纵坐标刻度
    axs[0].set_yticks([30, 40, 50, 60, 70, 80])
    axs[0].set_yticklabels([30, 40, 50, 60, 70, 80])
    axs[1].set_yticks([30, 40, 50, 60, 70, 80])
    axs[1].set_yticklabels([''] * len([30, 40, 50, 60, 70, 80]))  # 隐藏右图的纵坐标刻度标签

    # 设置纵坐标范围，略微超过最大值
    max_y = max(max(y4), 80) + 1
    axs[0].set_ylim([0, max_y])
    axs[1].set_ylim([0, max_y])

    # 设置第二个子图的纵坐标范围与第一个子图一致
    axs[1].set_ylim(axs[0].get_ylim())

    # 调整子图之间的间距
    plt.tight_layout()

    # 隐藏右图的纵坐标标签和名字
    axs[1].set_yticklabels([])
    axs[1].set_ylabel('')

    # 保存
    plt.savefig('fig_voc_few100_log_new.pdf', format='pdf')

    # 显示图形
    plt.show()

def draw_4():
    # 数据
    x = [5000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]
    x1 = [500, 1000, 1500, 2000, 2500, 3000,3500, 4000, 4500]
    y1 = [20.5, 25.0, 27.2, 27.9, 28.3, 28.2, 35.8, 35.9, 36.2]
    y2 = [24.0, 26.0, 27.8, 28.2, 30.0, 29.9, 36.0, 36.2, 37.3]
    y3 = [26.0, 31.0, 32.5, 33.2, 34.6, 35.0, 38.5, 38.6, 38.7]
    y4 = [28.0, 32.0, 33.2, 34.0, 35.1, 35.5, 38.8, 38.9, 39.2]

    y5 = [12.0, 59, 70, 74, 76, 78, 80, 80.2, 81]
    y6 = [18, 58, 63, 71, 72, 73, 76, 76, 76.1]
    y7 = [67, 71, 74, 76, 76, 75, 80, 80, 80]
    y8 = [72, 78, 80, 82, 81, 81, 85, 85, 85.8]

    # 将横坐标的刻度修改为25k, 50k, 75k
    x_ticks = [25000, 50000, 75000]
    x_labels = ['25k', '50k', '75k']

    x_ticks_1 = [500, 1000, 2000, 3000, 4000]
    x_labels_1 = ['.5k', '1k', '2k', '3k', '4k']
    offset = 0.5  # 偏移量

    # 创建子图
    fig, axs = plt.subplots(1, 2, figsize=(10, 7), gridspec_kw={'width_ratios': [1, 1]})

    # 绘制第一个子图
    axs[0].plot(x, y4, color='blue', marker='s', label='IN-14M DAP')  # 橙色折线，正方形标记
    axs[0].plot(x, y3, color='green', marker='o', label='IN-14M CLS', linestyle='--')  # 红色折线 虚线，圆形标记
    axs[0].plot(x, y2, color='red', marker='s', label='IN-1M DAP')  # 红色折线，圆形标记
    axs[0].plot(x, y1, color='deeppink', marker='o', label='IN-1M CLS', linestyle='--')  # 红色折线，圆形标记

    # 在每个点上显示纵坐标的数值，并设置颜色和加粗
    # for i in range(len(x)):
        # axs[0].text(x[i], y1[i] + offset, str(y1[i]), ha='center', va='bottom', color='orange')
        # axs[0].text(x[i], y2[i] - offset, str(y2[i]), ha='center', va='top', color='red')

    # 添加标题和标签
    # axs[0].set_title('Line Chart 1')
    axs[0].set_xlabel('Fine-tuning Iteration', fontsize=14)
    # axs[0].set_ylabel('Y-axis')
    # axs[0].set_ylabel(r'$Y_{\mathrm{axis}}$')  # 使用LaTeX语法设置纵坐标标签
    axs[0].set_ylabel(r'$AP_{\mathrm{.5:.95}}$ (%) on COCO 2017 val', fontsize=14)
    axs[0].grid(True)

    # 添加图例并放在右下角
    axs[0].legend(loc='lower right', fontsize=12)

    # 设置第一个子图的横坐标
    axs[0].set_xticks(x_ticks)
    axs[0].set_xticklabels(x_labels)

    # 绘制第二个子图
    axs[1].plot(x1, y8, color='blue', marker='s',  label='IN-14M DAP')  # 橙色折线，正方形标记
    axs[1].plot(x1, y7, color='red', marker='o',  label='IN-14M CLS')  # 红色折线，圆形标记
    axs[1].plot(x1, y6, color='deeppink', marker='s',  label='IN-1M DAP', linestyle='--')  # 红色折线，圆形标记
    axs[1].plot(x1, y5, color='green', marker='o',  label='IN-1M CLS', linestyle='--')  # 红色折线，圆形标记

    # 在每个点上显示纵坐标的数值，并设置颜色和加粗
    # for i in range(len(x)):
    #     axs[1].text(x[i], y3[i] + offset, str(y3[i]), ha='center', va='bottom', color='orange')
    #     axs[1].text(x[i], y4[i] - offset, str(y4[i]), ha='center', va='top', color='red')

    # 添加标题和标签
    # axs[1].set_title('Line Chart 2')
    axs[1].set_xlabel('Fine-tuning Iteration', fontsize=14)
    axs[1].set_ylabel(r'$AP_{\mathrm{.5}}$ (%) on VOC 2007 test', fontsize=14)
    axs[1].grid(True)

    # 添加图例并放在右下角
    axs[1].legend(loc='lower right', fontsize=12)

    # 设置第二个子图的横坐标
    axs[1].set_xticks(x_ticks_1)
    axs[1].set_xticklabels(x_labels_1)

    # 设置纵坐标刻度
    axs[0].set_yticks(np.linspace(22.5, 40.0, 8))
    axs[0].set_yticklabels(np.linspace(22.5, 40.0, 8))
    axs[1].set_yticks([20, 30, 40, 50, 60, 70, 80])
    axs[1].set_yticklabels([20, 30, 40, 50, 60, 70, 80])

    # 设置纵坐标范围，略微超过最大值
    max_y = max(max(y4), 80) + 1
    axs[0].set_ylim([20, 40.8])
    axs[1].set_ylim([10, 88])

    # 调整子图之间的间距
    plt.tight_layout()

    # 保存
    plt.savefig('fig_converge_new.pdf', format='pdf')

    # 显示图形
    plt.show()

if __name__ == '__main__':
    draw_4()