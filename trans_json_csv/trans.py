import json

if __name__ == '__main__':
    try:
        with open('input.json','r') as f:
            data = json.load(f)
            print(data)
        output = ','.join(data[0].keys())
        for obj in data:
            output += '\n'
            for key in data[0].keys():
                output += f'{obj[key]},'
            output = output.rstrip(',')
        
        with open('output.csv','w') as f:
            f.write(output)

    except Exception as ex:
        print(f'error:{str(ex)}')