"""
AgriChat Kullanim Kilavuzu - QR Kod Uretici

Kullanim:
    python generate_qr.py <URL>
    python generate_qr.py https://aysenurhepguven0.github.io/AgriChatManual

Bu script verilen URL'i iceren bir QR kod PNG dosyasi uretir (qr.png).
QR okutuldugunda telefonun tarayicisi bu URL'i acar.
"""
import sys
import io
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_H
except ImportError:
    print("Hata: 'qrcode' kutuphanesi yuklu degil.")
    print("Yuklemek icin:  pip install qrcode[pil]")
    sys.exit(1)


def make_qr(url: str, output_path: Path) -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=12,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#14532d", back_color="white")
    img.save(output_path)
    print(f"[OK] QR kod uretildi: {output_path}")
    print(f"     Hedef URL: {url}")


def main() -> None:
    if len(sys.argv) < 2:
        url = "https://example.github.io/AgriChat/manual/"
        print("Uyari: URL verilmedi, placeholder kullaniliyor.")
        print(f"Dogru kullanim: python {Path(__file__).name} <URL>")
    else:
        url = sys.argv[1]

    output = Path(__file__).parent / "qr.png"
    make_qr(url, output)


if __name__ == "__main__":
    main()
