# __author:花花
# data:2021-02-03 14:10 PM

"""
python3读取解析邮件内容
    1,不不能获取附件，还没写方法，以后需要再完善
"""

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


class GetEmail(object):
    """封装一个获取邮件内容的方法"""
    def __init__(self, *args, **kwargs):
        # 参数：POP3服务器地址
        self.email = 'po@icgoo.cn'
        self.password = 'Cxonline2018ok'
        self.pop3_server = 'imap.qiye.aliyun.com'

    @property
    def get_email(self):
        """获取邮件对象"""
        msg_list = list()
        server = poplib.POP3(self.pop3_server)            # 连接到POP3服务器:
        # server.set_debuglevel(1)                        # 可以打开或关闭调试信息:
        # print(server.getwelcome().decode('utf-8'))      # 可选:打印POP3服务器的欢迎文字:
        # 身份认证:
        print(1111111)
        server.user(self.email)
        server.pass_(self.password)

        print(u'邮件数量: %s. 占用空间Size: %s' % server.stat())   # 返回邮件数量和占用空间:
        resp, mails, octets = server.list()                     # 返回所有邮件的编号:返回的列表类似[b'1 82923', b'2 2184', ...]
        print(mails)

        for one in mails:
            print(one)
            # 获取最新一封邮件, 注意索引号从1开始:
            index = len(mails)
            # lines存储了邮件的原始文本的每一行,
            resp, lines, octets = server.retr(index)
            # 可以获得整个邮件的原始文本:
            msg_content = b'\r\n'.join(lines).decode('utf-8')
            msg = Parser().parsestr(msg_content)        # 解析出邮件:
            # server.dele(index)                        # 可以根据邮件索引号直接从服务器删除邮件:
            msg_list.append(msg)
        server.quit()  # 关闭连接
        return msg_list

    def parser_email(self, msg, indent=0):
        """解析邮件"""
        subject = ''# 主题
        _from = ''  # 发建人地址
        _to = ''    # 收件人地址
        content = '' # 内容
        if indent == 0:
            for header in ['From', 'To', 'Subject']:
                value = msg.get(header, '')
                if value:
                    if header == 'Subject':
                        subject = self.decode_str(value)
                    else:
                        hdr, _from = parseaddr(value)
                        name = self.decode_str(hdr)  # 邮箱名称

                    print(subject)
        if (msg.is_multipart()):
            parts = msg.get_payload()
            for n, part in enumerate(parts):
                print(111)
                # print('22222---%spart %s' % ('  ' * indent, n))
                # print('33333----%s--------------------' % ('  ' * indent))
                self.parser_email(part, indent + 1)
        else:
            print(222)
            content_type = msg.get_content_type()
            # if content_type == 'text/plain' or content_type == 'text/html':  # 收集邮件所有文本内容
            if content_type == 'text/plain':            # 只用于收集技术部日志
                content = msg.get_payload(decode=True)
                charset = self.check_charset(msg)
                if charset:
                    content = content.decode(charset)
                # print('%sText: %s' % ('  ' * indent, content))
            # else:
            #     print('%sAttachment: %s' % ('  ' * indent, content_type))  # 附件
        if content:
        #     content += content
            print(content)
        #     return subject, _from, _to, content
        return subject, _from, _to, content

    @staticmethod
    def decode_str(s):
        """邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode"""
        value, charset = decode_header(s)[0]
        if charset:
            value = value.decode(charset)
        return value

    @staticmethod
    def check_charset(msg):
        """检测编码"""
        charset = msg.get_charset()
        if charset is None:
            content_type = msg.get('Content-Type', '').lower()
            pos = content_type.find('charset=')
            if pos >= 0:
                charset = content_type[pos + 8:].strip()
        return charset

    @property
    def start_program(self):
        """启动程序"""
        intance = GetEmail()
        msg_list = intance.get_email
        # for msg in msg_list:
        subject, _from, _to, content = self.parser_email(msg_list[0])
        print(content)
        return True


if __name__ == '__main__':
    instance = GetEmail()
    res = instance.start_program
    print(res)