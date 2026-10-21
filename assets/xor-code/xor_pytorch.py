"""Train a 2-2-1 sigmoid network to classify the four XOR samples."""

import torch
import torch.nn.functional as F


torch.manual_seed(7)
torch.set_default_dtype(torch.float64)

# ① 张量：x 的四行依次是 00、01、10、11；两列分别是 x1、x2。
# target 每行一个 XOR 正确答案：00→0，01→1，10→1，11→0。
x = torch.tensor(
    [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]],
    dtype=torch.float64,
)
target = torch.tensor([[0.0], [1.0], [1.0], [0.0]], dtype=torch.float64)

# ② 模型：Parameter 表示可学习的连接权重 W、v 和偏置 b。
# W 从两个输入连向两个隐藏单元；v 从隐藏层连向一个输出。
W = torch.nn.Parameter(torch.tensor([[2.0, -2.0], [-2.0, 2.0]]))
b_hidden = torch.nn.Parameter(torch.tensor([-1.0, -1.0]))
v = torch.nn.Parameter(torch.tensor([[3.0], [3.0]]))
b_output = torch.nn.Parameter(torch.tensor([-2.5]))

parameters = [W, b_hidden, v, b_output]
optimizer = torch.optim.Adam(parameters, lr=0.03)

for epoch in range(1, 301):
    optimizer.zero_grad(set_to_none=True)
    hidden = torch.sigmoid(x @ W + b_hidden)  # 每例两个隐藏值
    logits = hidden @ v + b_output  # 每例一个原始输出分数
    loss = F.binary_cross_entropy_with_logits(logits, target)  # ③ 损失
    loss.backward()  # ④ 梯度写入各参数的 .grad
    optimizer.step()  # ⑤ Adam 读取梯度并更新参数

with torch.no_grad():
    hidden = torch.sigmoid(x @ W + b_hidden)
    final_logits = hidden @ v + b_output
    final_loss = F.binary_cross_entropy_with_logits(final_logits, target)
    probabilities = torch.sigmoid(final_logits)  # 0～1 的概率
    predictions = (probabilities >= 0.5).to(torch.int64)
    correct = torch.all(predictions == target.to(torch.int64)).item()

print(f"epoch={epoch}, loss={final_loss.item():.4f}")
print("x1 x2 | target | hidden (h1, h2) | probability | predicted")
for sample, label, hidden_row, probability, prediction in zip(
    x, target, hidden, probabilities, predictions
):
    print(
        f"{int(sample[0].item())}  {int(sample[1].item())}  |"
        f"   {int(label[0].item())}    |"
        f"    ({hidden_row[0].item():.3f}, {hidden_row[1].item():.3f})    |"
        f"    {probability[0].item():.4f}    |"
        f"     {prediction[0].item()}"
    )

if not correct:
    raise SystemExit("XOR was not fully classified; try more epochs.")
print("All four XOR samples classified correctly.")
