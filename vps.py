import os

print("Code by DuonngwTek, DONOT COPY!")
print("Starting now...")
cmd = 'wget -O bios64.bin "https://github.com/BlankOn/ovmf-blobs/raw/master/bios64.bin"'
os.system(cmd)
cmd = 'wget -O os.iso "https://drive.massgrave.dev/en_windows_10_iot_enterprise_ltsc_2019_x64_dvd_a1aa819f.iso"'
os.system(cmd)
cmd = 'sudo apt-get update'
os.system(cmd)
cmd = 'sudo apt autoremove'
os.system(cmd)
cmd = 'sudo apt install qemu-kvm -y'
os.system(cmd)
cmd = 'qemu-img create -f raw os.img 20G'
os.system(cmd)
print("Done. Please continue your work.")
print("Code by The CatTek Team x DuonngwTek, DONOT COPY!")
