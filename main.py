import aide_design, aide_draw, aide_document, os, yaml

def main(folder_path):
    with open(folder_path + '/params.yaml', 'w') as params_file:
        params = yaml.load(folder_path + '/params.yaml')
        # Process with aide_design
        yaml.dump(params, params_file, default_flow_style=False)

def test():
    print('AIDE has been run')