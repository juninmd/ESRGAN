import sys
import torch
from collections import OrderedDict

if len(sys.argv) < 2:
    print('Usage: python net_interp.py <alpha>')
    print('  alpha: interpolation factor between 0 and 1')
    sys.exit(1)

try:
    alpha = float(sys.argv[1])
except ValueError:
    print('Error: alpha must be a valid floating-point number')
    sys.exit(1)

if not 0.0 <= alpha <= 1.0:
    print('Error: alpha must be between 0 and 1')
    sys.exit(1)

net_PSNR_path = './models/RRDB_PSNR_x4.pth'
net_ESRGAN_path = './models/RRDB_ESRGAN_x4.pth'
net_interp_path = './models/interp_{:02d}.pth'.format(int(alpha*10))

net_PSNR = torch.load(net_PSNR_path)
net_ESRGAN = torch.load(net_ESRGAN_path)
net_interp = OrderedDict()

print('Interpolating with alpha = ', alpha)

for k, v_PSNR in net_PSNR.items():
    v_ESRGAN = net_ESRGAN[k]
    net_interp[k] = (1 - alpha) * v_PSNR + alpha * v_ESRGAN

torch.save(net_interp, net_interp_path)
