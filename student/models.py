from django.db import models

# Create your models here.

SEX = (
    ('男', '男'),
    ('女', '女'),
)
DEPT = (
    ('信息学院', '信息学院'),
    ('机械与自动控制学院', '机械与自动控制学院'),
    ('外国语学院', '外国语学院'),
    ('理学院', '理学院'),
    ('服装学院', '服装学院'),
    ('法政学院', '法政学院'),
    ('马克思主义学院', '马克思主义学院')
)


class Student(models.Model):
    id = models.CharField('学号', max_length=20, primary_key=True)
    name = models.CharField('姓名', max_length=20)
    sex = models.CharField('性别', max_length=4, choices=SEX, default='男')
    dept = models.CharField('学院', max_length=20, choices=DEPT, default=None)
    major = models.CharField('专业', max_length=20, default=None)
    password = models.CharField('密码', max_length=20, default='123123')
    email = models.EmailField('邮箱', default=None)
    birth = models.DateField('出生日期')

    class Meta:
        db_table = 'student'
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class Teacher(models.Model):
    id = models.CharField("教工号", max_length=20, primary_key=True)
    name = models.CharField('姓名', max_length=20)
    sex = models.CharField('性别', max_length=4, choices=SEX, default='男')
    dept = models.CharField('学院', max_length=20, choices=DEPT, default=None)
    email = models.EmailField('邮箱', default=None)
    password = models.CharField('密码', max_length=20, default='000000')
    birth = models.DateField('出生日期')

    class Meta:
        db_table = 'teacher'
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Question(models.Model):
    ANSWER = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('AB', 'AB'),
        ('AC', 'AC'),
        ('AD', 'AD'),
        ('BC', 'BC'),
        ('BD', 'BD'),
        ('CD', 'CD'),
        ('ABC', 'ABC'),
        ('ABD', 'ABD'),
        ('BCD', 'BCD'),
        ('ABCD', 'ABCD')
    )
    LEVEL = {
        ('1', 'easy'),
        ('2', 'general'),
        ('3', 'difficult'),
    }
    id = models.AutoField(primary_key=True)
    subject = models.CharField('科目', max_length=20)
    title = models.TextField('题目')
    optionA = models.CharField('A选项', max_length=50)
    optionB = models.CharField('B选项', max_length=50)
    optionC = models.CharField('C选项', max_length=50)
    optionD = models.CharField('D选项', max_length=50)
    answer = models.CharField('答案', max_length=10, choices=ANSWER)
    level = models.CharField('等级', max_length=10, choices=LEVEL)
    chapter = models.CharField('章节', max_length=30, null=True, blank=True)
    score = models.IntegerField('分数', default=1)

    class Meta:
        db_table = 'question'
        verbose_name = '选择题库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s:%s>' % (self.subject, self.title)


class Paper(models.Model):
    pid = models.ManyToManyField(Question)  # 多对多
    tid = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # 外键
    subject = models.CharField('科目', max_length=20, default='')
    major = models.CharField('考卷适用专业', max_length=20)
    exam_time = models.DateTimeField()
    duration = models.DurationField('时长', null=True, blank=True)
    passphrase = models.CharField('口令', max_length=12, null=True, blank=True)  # 允许进入考试的口令

    class Meta:
        db_table = 'paper'
        verbose_name = '试卷'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.major


class Grade(models.Model):
    sid = models.ForeignKey(Student, on_delete=models.CASCADE, default='')  # 外键
    subject = models.CharField('科目', max_length=20, default='')
    grade = models.IntegerField()
    all_grade = models.IntegerField()

    def __str__(self):
        return '<%s:%s>' % (self.sid, self.grade)

    class Meta:
        db_table = 'grade'
        verbose_name = '成绩'
        verbose_name_plural = verbose_name
