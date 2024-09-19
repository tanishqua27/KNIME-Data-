import subprocess
import os

# Define the paths to AutoDock Vina executable and input files
vina_executable = r"C:\Program Files (x86)\The Scripps Research Institute\Vina\vina.exe"
receptor_pdbqt = r"C:\Users\Tanishaqua\OneDrive\Desktop\knime\Script\Receptor.pdbqt"  # Update with the correct path
ligand_pdbqt = r"C:\Users\Tanishaqua\OneDrive\Desktop\knime\Script\4_hydroxytamoxifen.pdbqt"  # Update with the correct path
output_pdbqt = r"C:\Users\Tanishaqua\OneDrive\Desktop\knime\Output\output.pdbqt"  # Update with the desired output path
config_file = r"C:\Users\Tanishaqua\OneDrive\Desktop\knime\Script\config.txt"  # Update with the correct path

# Define the command to execute AutoDock Vina
command = [
    vina_executable,
    '--receptor', receptor_pdbqt,
    '--ligand', ligand_pdbqt,
    '--out', output_pdbqt,
    '--config', config_file  # Add config file to the command
]

# Ensure the output directory exists
output_dir = os.path.dirname(output_pdbqt)
os.makedirs(output_dir, exist_ok=True)

# Execute AutoDock Vina using subprocess
try:
    subprocess.run(command, check=True)
    print("AutoDock Vina execution successful.")
except subprocess.CalledProcessError as e:
    print("Error executing AutoDock Vina:", e)
