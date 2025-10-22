# フィボナッチ数列プログラム

このリポジトリには、フィボナッチ数列を生成・表示するPythonプログラムが含まれています。

## ファイル構成

- **fibonacci.py** - フィボナッチ数列を生成する基本プログラム
- **fibonacci_display.py** - fibonacci.pyを外部から呼び出し、段階的に表示するプログラム
- **README.md** - このファイル

## fibonacci.py

フィボナッチ数列を生成する基本的な関数を提供します。

### 機能

- `fibonacci_generator(n)` - 最初のn個のフィボナッチ数を生成
- `fibonacci_up_to(max_value)` - 指定値以下のフィボナッチ数を生成
- `fibonacci_nth(n)` - n番目のフィボナッチ数を計算

### 使用方法

```bash
python3 fibonacci.py
```

実行すると、以下が表示されます：
- 最初の10個のフィボナッチ数
- 100以下のフィボナッチ数
- 15番目のフィボナッチ数
- ユーザー入力による対話的な生成

### モジュールとしての使用

```python
from fibonacci import fibonacci_generator, fibonacci_nth

# 最初の10個を生成
for fib in fibonacci_generator(10):
    print(fib)

# 20番目のフィボナッチ数を取得
print(fibonacci_nth(20))
```

## fibonacci_display.py

fibonacci.pyをモジュールとして読み込み、様々な形式でフィボナッチ数列を段階的に表示します。

### 機能

1. **時間間隔表示** - 指定した時間間隔で自動的に順次表示
2. **ステップバイステップ表示** - Enterキーを押すたびに次の数を表示
3. **アニメーション表示** - 画面を更新しながら動的に表示
4. **比較表示** - 複数の表示形式を同時に比較
5. **ツリー形式表示** - ツリー構造で視覚的に表示

### 使用方法

```bash
python3 fibonacci_display.py
```

実行後、表示モードと個数を選択します。

### 使用例

```bash
# プログラムを実行
$ python3 fibonacci_display.py

# モード選択
モードを選択 [1-5, 0]: 1

# 個数入力
表示する個数を入力してください: 10

# 間隔入力（モード1の場合）
表示間隔（秒）を入力してください [0.5]: 0.3
```

### 各モードの説明

#### 1. 時間間隔表示
```
フィボナッチ数列を10個、0.3秒間隔で表示します...

F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
...
```

#### 2. ステップバイステップ表示
Enterキーを押すたびに次の数が表示されます。学習用に最適です。

#### 3. アニメーション表示
画面を更新しながら、これまでの数列全体を表示します。

#### 4. 比較表示
- リスト形式
- 段階的表示
- 合計値の計算

#### 5. ツリー形式表示
```
=== フィボナッチ数列（ツリー形式） ===

├─ F(0) = 0
  ├─ F(1) = 1
    ├─ F(2) = 1
      ├─ F(3) = 2
        ├─ F(4) = 3
...
```

## クラスとしての使用

fibonacci_display.pyは`FibonacciDisplay`クラスを提供しており、他のプログラムから呼び出すこともできます。

```python
from fibonacci_display import FibonacciDisplay

display = FibonacciDisplay()

# 10個を0.5秒間隔で表示
display.display_with_delay(10, 0.5)

# ツリー形式で表示
display.display_tree_style(8)

# 比較表示
display.display_comparison(5)
```

## 要件

- Python 3.6以上
- 標準ライブラリのみ使用（外部依存なし）

## ライセンス

このプログラムは教育目的で作成されています。自由に使用・改変してください。

## 作者

Generated with Claude Code
