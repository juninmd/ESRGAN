import sys
import torch
from collections import OrderedDict

if len(sys.argv) < 2:
    print('Usage: python net_interp.py <alpha>')
    print('  alpha: interpolation parameter in [0, 1]')
    sys.exit(1)

alpha = float(sys.argv[1])
if not (0 <= alpha <= 1):
    print('Error: alpha must be in [0, 1]')
    sys.exit(1)

net_PSNR_path = './models/RRDB_PSNR_x4.pth'
net_ESRGAN_path = './models/RRDB_ESRGAN_x4.pth'
net_interp_path = './models/interp_{:02d}.pth'.format(int(alpha*10))

net_PSNR = torch.load(net_PSNR_path, weights_only=True)
net_ESRGAN = torch.load(net_ESRGAN_path, weights_only=True)
net_interp = OrderedDict()

print('Interpolating with alpha = ', alpha)

for k, v_PSNR in net_PSNR.items():
    v_ESRGAN = net_ESRGAN[k]
    net_interp[k] = (1 - alpha) * v_PSNR + alpha * v_ESRGAN

torch.save(net_interp, net_interp_path)
