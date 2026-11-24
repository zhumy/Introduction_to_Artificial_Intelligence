(() => {
  const chapters = [
    ['21', '人脸识别'], ['22', '车牌识别'], ['23', 'AI美颜'],
    ['24', 'AI绘画大师'], ['25', 'AI鉴伪'], ['26', '语音识别'],
    ['27', '声纹识别'], ['28', '语音合成'], ['29', '机器作家'],
    ['30', '人工智能诗人'], ['31', '机器翻译'], ['32', '围棋国手'],
    ['33', 'AI游戏'], ['34', '扫地机器人'], ['35', '搜索引擎'],
    ['36', '商品推荐']
  ];

  const sidebar = document.querySelector('.sidebar');
  const navs = sidebar ? sidebar.querySelectorAll('nav') : [];
  if (navs.length >= 2) {
    const part = document.createElement('a');
    part.className = 'part-link';
    part.href = '#v9-part3-overview';
    part.textContent = '第三篇 人工智能应用';
    const nav = document.createElement('nav');
    nav.setAttribute('aria-label', '第三篇 人工智能应用');
    for (const [number, title] of chapters) {
      const link = document.createElement('a');
      link.href = '#chapter-' + number;
      link.textContent = number + '. ' + title;
      nav.append(link);
    }
    navs[1].after(part, nav);
  }

  const pages = document.querySelectorAll('main .v4-page');
  pages.forEach((page, index) => {
    const count = page.querySelector('footer span');
    if (count) count.textContent = (index + 1) + ' / ' + pages.length;
  });

  const lastPageLink = document.querySelector('#v7-p051 footer a:last-child');
  if (lastPageLink) {
    lastPageLink.href = '#v9-part3-overview';
    lastPageLink.textContent = '下一篇 →';
  }
})();
