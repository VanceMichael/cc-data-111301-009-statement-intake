# 来源资料约定

statement.ofx 与 correction.ofx 为 XML 包络，legacy.ofx 为 OFX 1.x SGML 包络。legacy 中的简单元素允许省略结束标签。示例账户和交易均为虚构；账户 A 和 B 中出现的 trade-1 不是同一账户流水。更正文件使用新的 FITID，并通过 CORRECTFITID 与 CORRECTACTION 引用被更正流水。金额原文使用十进制字符串。
