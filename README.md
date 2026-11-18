# storylines · 地方专题周度阅读与跟进账

使用 Python 3.11 标准库，不需要联网、第三方包或数据库。输入示例使用本地合成记录。

```sh
python3 -m storylines edition data/sample.json
python3 -m unittest discover -s tests -v
```

输出为 UTF-8 JSON。输入文件不可读、业务引用无效或记录不符合口径时退出码为 2，同时报告原因。

## 记录口径

`topics` 是编辑已确认的专题；`links` 记报道与专题关联，`review` 是待审建议，不参与日常统计。`reads` 的 `id` 是阅读凭证，同一凭证仅指一篇报道，`week` 为报表周。文章可以挂多条专题。
`subscriptions` 以居民与专题标识状态，`stopped` 是明确停止，`preference` 可选为街区。`publications` 为已发布的分发批次，实际收件人与报表快照分别由周表和投递凭证存档。
