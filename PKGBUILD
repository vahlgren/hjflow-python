
pkgname=python-hjflow
_name=${pkgname#python-}
pkgver=0.0.1
pkgrel=1
pkgdesc="Library for defining program flow in HJSON"
arch=('any')
url="https://hjflow.argv0.org"
license=('Apache 2')
depends=('python' 'python-hjson')

source=("${_name}-${pkgver}.tar.gz")

build() {
  cd "${_name}-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_name}-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
  #install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}

sha256sums=(SKIP)

