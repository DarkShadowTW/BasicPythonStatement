#from BOOK - PyTorch 深度學習攻略
#CH2 - PAGE 2-3 Example
#AUTHOR : Eli Stevens．Luca Antiga．Thomas Viehmann, 施威銘研究室(旗標)

#Phase 1 - 載入 torchvision 中的模型，並顯示有哪些模型
from torchvision import models
print(dir(models))

#OUTPUT
#['AlexNet', 'DenseNet', 'GoogLeNet', 'GoogLeNetOutputs', 'Inception3',
# 'InceptionOutputs', 'MNASNet', 'MobileNetV2', 'MobileNetV3', 'ResNet',
# 'ShuffleNetV2', 'SqueezeNet', 'VGG', ... 'wide_resnet101_2', 'wide_resnet50_2']


#Phase 2 - 使土殘差網路 resnet101, 並且使用預先 Train 好的結果
resnet = models.resnet101(pretrained=True)

#Phase 3 - 對圖片進行預處理，先轉換 256*256，再裁前為 224*224，轉換成張量 (224*224*3)，對 RGB 正規化處理，設定平均值和標準差
from torchvision import transforms
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )])

#Phase 4 - 載入圖片並顯示圖片
from PIL import Image

img = Image.open("./image/cute-dog-headshot.jpg")

img.show()

#Phase 5 - 將圖片透過預處理
img_t = preprocess(img)
print(img_t.shape)       #torch.Size([3, 224, 224])


#Phase 6 - 因 ResNet 4D 可載入多圖，目前 img_t.shape 為 3D，因此使用 torch.unsqueeze 加一個維度
import torch
#batch_t = torch.unsqueeze(img_t, 3)   #torch.Size([3, 224, 224, 1])
batch_t = torch.unsqueeze(img_t, 0)
print(batch_t.shape)                   #orch.Size([1, 3, 224, 224])

#Phase 7 Eval Mode - 設定模型為 eval 開始處理資料
resnet.eval()

#Phase 8 Output  傳入剛載入圖片，並轉成 4 維的張量
out = resnet(batch_t)
print(out.shape) #torch.Size([1, 1000])

#Phase 9 Load Label File - 資料組 = [自訂變數 for 自訂變數 in 資料組 if 關係運算式]
#strip - 移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
with open('label/imagenet_classes.txt') as f:
    labels = [line.strip() for line in f.readlines()]

#Phase 10 find tensor Max value
#Out put 1000 個分數為 resnet101 可判斷 1000 個類別標籤，下表是從 1000 中捉出分數最大的值
#https://blog.csdn.net/weixin_48249563/article/details/111387501 torch.max()这个函数返回的是两个值，第一个值是具体的value（我们用下划线_表示），第二个值是value所在的index（也就是predicted）。
#这个 下划线_ 表示的就是具体的value，也就是输出的最大值。那么为什么用 下划线_，可不可以用其他的变量名称来代替，比如x？答案自然是可以的。
_, index = torch.max(out, 1)  #1 為 dim=1 所在行取最大值
#_ 有值，從 out (torch.Size([1, 1000])) 二維張量取最大值 dim=1 表示输出所在行的最大值
print(_)     #tensor([12.1374], grad_fn=<MaxBackward0>)
print(index) #tensor([200])
#index.shape = 1, index[0] = {Tensor: ()} tensor(200)

#Phase 11 using softmax for Normalization for setting value as 0 or 1
percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100   #Softmax 正規化讓值在 [0,1] 間
#index[0] 因其為 Array 目前放最大值在 index的第一個元素
print(labels[index[0]])      #機率最高的 Label 名, Tibetan terrier, chrysanthemum dog
print(percentage[index[0]])  #percentage.shape = 1000 , tensor(60.1664, grad_fn=<SelectBackward>) 百分筆
print(labels[index[0]], percentage[index[0]].item()) #Tibetan terrier, chrysanthemum dog 60.16643142700195

#Phase 12 捉出前五名, indices 指數
_, indices = torch.sort(out, descending=True)
list_top5 = [(labels[idx], percentage[idx].item()) for idx in indices[0][:5]]

print(list_top5)
#[('Tibetan terrier, chrysanthemum dog', 60.16643142700195), ('Yorkshire terrier', 18.21837043762207), ('miniature poodle', 4.851706504821777), ('toy poodle', 4.082067966461182), ('Lhasa, Lhasa apso', 2.9239742755889893)]