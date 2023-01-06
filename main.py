from netmiko import ConnectHandler
from config import get_ip
from typing import Dict,Union,List

class NetworkAutomation :
  def __init__(self)-> None:
    self.device_ip : List[str] = self.change_list()

  def main(self)-> None:
    [self.connect_server(dev_ip=dev_ip) for dev_ip in self.device_ip]

  def write_result_to_txt(self,output: str)-> None:
    with open('./python_logs.txt' , 'a' , encoding='UTF-8') as file :
      file.write(output)

  def connect_server(self,dev_ip: str)-> None:
    ios_sw : Dict[str,Union[str,bool]] = {
      "device_type":"cisco_ios",
      "ip":dev_ip,
      "username":"admin",
      "password":"cisco",
      "secret":"cisco",
      "verbose":True # 함수 수행시 발생정보들을 표준 출력으로 내보내는 방법
    }

    # ssh 연결
    net_connect = ConnectHandler(**ios_sw) # Dict 형태로 작성되었기 때문에 **를 붙임

    # 네트워크 명령어 수행
    self.execute_network_config(net_connect=net_connect)

  def execute_network_config(self,net_connect)-> None:
    # enable 상태창 들어가기
    net_connect.enable()

    # 명령어 입력
    output : str = net_connect.send_command('show run')

    # 출력 값 파일로 만들어 저장하기
    self.write_result_to_txt(output=output)

  def change_list(self)-> List[str]:
    device_ips : List[str] = get_ip.get_ip(key='ip')
    return device_ips

app = NetworkAutomation()
app.main()