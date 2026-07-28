import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_incoming_value(file):
    tree = ET.parse(file)
    root = tree.getroot()
    for group in root.findall('group'):
        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
            incoming = timing_exbytes.find('incoming')
            if incoming is not None:
                logging.info(f"Group: {group.find('name').text}, incoming: {incoming.text}")
            else:
                logging.info(f"Group: {group.find('name').text}, incoming: Не знайдено")

find_incoming_value('groups.xml')