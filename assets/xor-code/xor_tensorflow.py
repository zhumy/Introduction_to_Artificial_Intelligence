"""Train a 2-2-1 sigmoid network to classify the four XOR samples."""

import tensorflow as tf


tf.keras.utils.set_random_seed(7)
tf.keras.backend.set_floatx("float64")

# ① 张量：x 的四行依次是 00、01、10、11；两列分别是 x1、x2。
# target 每行一个 XOR 正确答案：00→0，01→1，10→1，11→0。
x = tf.constant(
    [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]],
    dtype=tf.float64,
)
target = tf.constant([[0.0], [1.0], [1.0], [0.0]], dtype=tf.float64)

# ② 模型：可学习的连接权重 W、v 和偏置 b。
# W 从两个输入连向两个隐藏单元；v 从隐藏层连向一个输出。
W = tf.Variable([[2.0, -2.0], [-2.0, 2.0]], dtype=tf.float64)
b_hidden = tf.Variable([-1.0, -1.0], dtype=tf.float64)
v = tf.Variable([[3.0], [3.0]], dtype=tf.float64)
b_output = tf.Variable([-2.5], dtype=tf.float64)

parameters = [W, b_hidden, v, b_output]
optimizer = tf.keras.optimizers.Adam(learning_rate=0.03)

for epoch in range(1, 301):
    with tf.GradientTape() as tape:
        hidden = tf.sigmoid(tf.matmul(x, W) + b_hidden)  # 每例两个隐藏值
        logits = tf.matmul(hidden, v) + b_output  # 每例一个原始输出分数
        loss = tf.reduce_mean(  # ③ 损失：比较原始分数与正确标签
            tf.nn.sigmoid_cross_entropy_with_logits(
                labels=target,
                logits=logits,
            )
        )

    gradients = tape.gradient(loss, parameters)  # ④ 每个参数对损失的影响
    optimizer.apply_gradients(zip(gradients, parameters))  # ⑤ Adam 更新参数

hidden = tf.sigmoid(tf.matmul(x, W) + b_hidden)
probabilities = tf.sigmoid(tf.matmul(hidden, v) + b_output)  # 0～1 的概率
final_logits = tf.matmul(hidden, v) + b_output
final_loss = tf.reduce_mean(
    tf.nn.sigmoid_cross_entropy_with_logits(labels=target, logits=final_logits)
)
predictions = tf.cast(probabilities >= 0.5, tf.int32)
correct = tf.reduce_all(predictions == tf.cast(target, tf.int32))

print(f"epoch={epoch}, loss={final_loss.numpy():.4f}")
print("x1 x2 | target | hidden (h1, h2) | probability | predicted")
for sample, label, hidden_row, probability, prediction in zip(
    x.numpy(), target.numpy(), hidden.numpy(), probabilities.numpy(), predictions.numpy()
):
    print(
        f"{int(sample[0])}  {int(sample[1])}  |   {int(label[0])}    |"
        f"    ({hidden_row[0]:.3f}, {hidden_row[1]:.3f})    |"
        f"    {probability[0]:.4f}    |     {prediction[0]}"
    )

if not bool(correct.numpy()):
    raise SystemExit("XOR was not fully classified; try more epochs.")
print("All four XOR samples classified correctly.")
