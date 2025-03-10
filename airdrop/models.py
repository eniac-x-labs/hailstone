import pytz
from django.conf import settings
from django.db import models
from common.models import BaseModel, Asset

TypeChoice = [(x, x) for x in ['Invite', 'Social', 'BridgeTransfer', 'BridgeStaking', 'BridgeWithdraw', 'bridgeGrants', 'Layer3Staking', 'Layer3Unstaking', 'Layer3Withdraw', 'Layer3Grants', 'LayerAppChainInterAction', 'SubmitProject']]

LanguageChoice = [(x, x) for x in ['zh', 'en']]

ProjectChoice = [(x, x) for x in ['Social', 'Project']]


class AirdropUser(BaseModel):
    name = models.CharField(
        default="unknown",
        max_length=100,
        unique=False,
        verbose_name='用户名'
    )
    invite_code = models.CharField(
        default="0000-0000-0000",
        max_length=100,
        unique=True,
        verbose_name='邀请码'
    )
    invite_me_uuid = models.CharField(
        default="0000-0000-0000",
        max_length=100,
        unique=False,
        verbose_name='邀请人'
    )
    photo = models.ImageField(
        upload_to='symbol/%Y/%m/%d/',
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='用户地址'
    )
    email = models.EmailField(
        blank=True,
        null=True
    )
    points = models.PositiveIntegerField(
        default=0,
        verbose_name="积分数量"
    )
    x_twitter = models.CharField(
        max_length=100,
        default="",
        blank=True,
        null=True,
        verbose_name="x",
    )
    discord = models.CharField(
        max_length=100,
        default="",
        blank=True,
        null=True,
        verbose_name="discord",
    )
    telegram = models.CharField(
        max_length=100,
        default="",
        blank=True,
        null=True,
        verbose_name="discord",
    )
    info = models.CharField(
        max_length=100,
        default="",
        blank=True,
        null=True,
        verbose_name="个人介绍",
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_invite_member_numbers(self):
        return AirdropUser.objects.filter(invite_me_uuid=self.uuid).count()

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'photo': str(self.photo),
            'address': self.address,
            'email': self.email,
            'points': self.points,
            'x_twitter': self.x_twitter,
            'discord': self.discord,
            'telegram': self.telegram,
            'invite_total': self.get_invite_member_numbers(),
            'info': self.info
        }


class PointsRecord(BaseModel):
    user = models.ForeignKey(
        AirdropUser,
        related_name="airdrop_user",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="收藏的商家",
    )
    type = models.CharField(
        max_length=100,
        choices=TypeChoice,
        default="BridgeTransfer",
        verbose_name='积分类型'
    )
    address = models.CharField(
        max_length=100,
        unique=False,
        verbose_name='用户地址'
    )
    points = models.PositiveIntegerField(
        default=0,
        verbose_name="积分数量"
    )

    class Meta:
        verbose_name = 'PointsRecord'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address

    def as_dict(self):
        tz = pytz.timezone(settings.TIME_ZONE)
        return {
            'id': self.id,
            'name': self.address,
            'type': self.type,
            'points': self.points,
            'created_at': self.created_at.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")
        }


class ProjectInterAction(BaseModel):
    step = models.CharField(
        max_length=100,
        unique=False,
        blank=True,
        verbose_name='交互步骤'
    )
    icon = models.ImageField(
        upload_to='projects/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='交互Icon'
    )
    name = models.CharField(
        max_length=100,
        unique=False,
        blank=True,
        verbose_name='交互名称'
    )
    describe = models.CharField(
        max_length=200,
        unique=False,
        verbose_name='交互描述'
    )
    link_url = models.CharField(
        max_length=200,
        unique=False,
        blank=True,
        verbose_name='交互链接'
    )
    language = models.CharField(
        max_length=100,
        choices=LanguageChoice,
        default="en",
        verbose_name='语言'
    )
    points_type = models.CharField(
        max_length=100,
        choices=TypeChoice,
        unique=False,
        default="BridgeTransfer",
        verbose_name='积分类型'
    )
    project_type = models.CharField(
        max_length=100,
        choices=ProjectChoice,
        default="Project",
        verbose_name='项目类型'
    )
    once_points = models.PositiveIntegerField(
        default=0,
        verbose_name="每次交互获得的积分数量"
    )
    daily_max_points = models.PositiveIntegerField(
        default=0,
        verbose_name="每天交互的最大积分数"
    )
    max_points = models.PositiveIntegerField(
        default=0,
        verbose_name="最大积分数"
    )

    class Meta:
        verbose_name = 'ProjectInterAction'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            'id': self.id,
            'step': self.step,
            'name': self.name,
            'icon': str(self.icon),
            'describe': self.describe,
            'points_type': self.points_type,
            'project_type': self.project_type,
            'once_points': self.once_points,
            'daily_max_points': self.daily_max_points,
            'link_url': self.link_url,
            'language': self.language,
            'max_points': self.max_points,
        }


class Questions(BaseModel):
    question = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='问题名称'
    )
    answer = models.CharField(
        max_length=500,
        unique=True,
        verbose_name='问题答案'
    )
    language = models.CharField(
        max_length=100,
        choices=LanguageChoice,
        default="en",
        verbose_name='语言'
    )

    class Meta:
        verbose_name = 'Questions'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question

    def as_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'language': self.language
        }


class Period(BaseModel):
    title = models.CharField(
        max_length=200,
        unique=False,
        blank=False,
        default="",
        verbose_name='活动主题'
    )
    sub_title = models.CharField(
        max_length=200,
        unique=False,
        blank=False,
        default="",
        verbose_name='活动副标题'
    )
    image = models.ImageField(
        upload_to='period/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='活动图片'
    )
    link_url = models.CharField(
        default="",
        max_length=100,
        unique=False,
        verbose_name='活动链接'
    )
    period = models.CharField(
        max_length=300,
        unique=False,
        blank=True,
        verbose_name='活动周期'
    )

    class Meta:
        verbose_name = 'Period'
        verbose_name_plural = verbose_name

    def as_dict(self, address):
        is_reward = True
        reward = {}
        p_reward = PeriodReward.objects.filter(address__icontains=address).first()
        if p_reward is None:
            is_reward = False
        else:
            reward = p_reward.as_dict()
        return {
            'id': self.id,
            'title': self.title,
            'sub_title': self.sub_title,
            'image': str(self.image),
            'link_url': self.link_url,
            'period': self.period,
            'is_reward': is_reward,
            "reward": reward,
        }


class PeriodReward(BaseModel):
    address = models.CharField(
        max_length=200,
        unique=False,
        verbose_name='地址'
    )
    amount = models.CharField(
        max_length=100,
        unique=False,
        verbose_name='中奖金额'
    )

    is_send = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = 'PeriodReward'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address

    def as_dict(self):
        tz = pytz.timezone(settings.TIME_ZONE)
        return {
            'id': self.id,
            'address': self.address,
            'amount': self.amount,
            'is_send': self.is_send,
            'created_at': self.created_at.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")
        }
