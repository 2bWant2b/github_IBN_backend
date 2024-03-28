from datetime import datetime

from ..exts import db


class UserIntent(db.Model):
    """用户意图表"""
    __tablename__ = 'user_intents'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    raw_text = db.Column(db.String(255), nullable=False)  # 用户原始输入
    prep_text = db.Column(db.String(255), nullable=False)  # 预处理后的输入文本
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))
    slot_id = db.Column(db.Integer, db.ForeignKey('slot_results.id'))
    configure_id = db.Column(db.Integer, db.ForeignKey('configurations.id'))
    policy_id = db.Column(db.Integer, db.ForeignKey('policies.id'))
    is_integrity = db.Column(db.Integer)
    is_worked = db.Column(db.Integer)


class Service(db.Model):
    """业务表
    用于存储网络业务类型信息"""
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    coarser_intent = db.Column(db.String(255), nullable=False)  # 粗粒度意图
    finer_intent = db.Column(db.String(255), nullable=False)  # 细粒度意图
    example = db.Column(db.String(255), nullable=False)  # 例句


class SlotLabel(db.Model):
    """槽位标签表"""
    __tablename__ = 'slot_labels'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)  # 槽位标签
    # slot_label = db.Column(db.String(255), nullable=False)  # 槽位标签
    # slot_value = db.Column(db.String(255), nullable=False)  # 槽位值


class CorpusIntent(db.Model):
    """意图语料表"""
    __tablename__ = 'corpus_intents'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    raw_text = db.Column(db.String(255), nullable=False)  # 原始文本
    prep_text = db.Column(db.String(255), nullable=False)  # 预处理后的文本
    service = db.Column(db.String(255), nullable=False)  # 服务
    slot = db.Column(db.String(255), nullable=False)  # 序列标注文本


class SlotResult(db.Model):
    """槽位填充结果表"""
    __tablename__ = 'slot_results'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    server_name = db.Column(db.String(255), nullable=False)  # 服务平台名称
    label_type = db.Column(db.String(255), nullable=False)  # 服务要求标签类型
    label_value = db.Column(db.String(255), nullable=False)  # 标签值


class Configuration(db.Model):
    """路由配置报文表
    用于存储转译过程中构建的业务路由配置报文"""
    __tablename__ = 'configurations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))  # 业务类型编号
    slot_id = db.Column(db.Integer, db.ForeignKey('slot_results.id'))
    # src_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))
    # dst_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))
    qosrule_id = db.Column(db.Integer, db.ForeignKey('route_qos_rules.id'))


class Policy(db.Model):
    """路由策略表
    用于存储意图处理过程中构建的路由策略结果"""
    __tablename__ = 'policies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, default=datetime.now)  # 创建时间
    route_policy = db.Column(db.String(255))


class RouteQoSRule(db.Model):
    """路由QoS规则表
    用于存储业务到路由服务质量的映射规则"""
    __tablename__ = 'route_qos_rules'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))
    bandwidth = db.Column(db.Float)
    delay = db.Column(db.Float)
    loss = db.Column(db.Float)


class Equipment(db.Model):
    """设备信息表
    用于存储底层设备信息"""
    __tablename__ = 'equipment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))  # 设备名称
    address = db.Column(db.String(255))  # ip地址
