from lxml import etree

def parse_junit(xml_file):
    tree = etree.parse(xml_file)
    results = []

    for testcase in tree.xpath("//testcase"):
        name = testcase.get("name")
        time = float(testcase.get("time"))
        status = "pass"
        if testcase.find("failure") is not None:
            status = "fail"

        results.append({
            "test_name": name,
            "status": status,
            "execution_time": time
        })

    return results