# UPDATE

### 將資料夾更新到最後一個節點
```bash
dit pull
```

### 檢查狀態
```bash
git status
```

### 暴力覆蓋所有檔案至本地端
```bash
git reset --hard origin/main
```

### 新增/更新 檔案
```bash
git add .
```
### 寫下更新內容
```bash
git commit -m "描述下你做了什麼"
```

### 確認推送上傳
```bash
git push origin main
```

@如果想要修改內容:
1.
### 創建分支並進入
```bash
git checkout -b branch_name   ->   創建不進入: "git branch branch_name" , 切換分支: "git checkout branch_name" 
```
2.
### 修改檔案的內容
```bash
vi filename   ->   編輯: 點 i|insert鍵  ，退出: 按esc後輸入:wq儲存, 不想儲存按esc輸入:q即可
```
一樣進行git add 還有 git commit
3.
### 合併分支內容到main
```bash
git checkout main   ->   切回main分支
git merge branch_name   ->   合併分支而已，記得要確認推送上傳
```

### 如果想要刪除分支
```bash
git push oirgin :branch_name
```




