// Select examples without animation so each state stays readable in class.
(() => {
  const examples = {
    cross: [
      '正在写 a new iPhone：参考“手机店”和“新款苹果手机”。',
      '正在写 softer apples：参考“菜市场”和“软一点的苹果”，这里说的是水果。',
      '正在写 did not enter：保留“没有”的否定，并结合“手机店”理解进的是哪家店。',
      '正在写 grandmother’s home：参考“奶奶家”，交代把水果送到哪里。',
    ],
    self: [
      '当前位置：“他”',
      '当前位置：“进店”',
      '当前位置：最后一处“苹果”',
    ],
    selfStatus: [
      '“他”：结合前文“小林”，形成这个人物在当前位置的表示。',
      '“进店”：结合前文“手机店”，理解这里说的是没有走进手机店。',
      '最后一处“苹果”：联系前文，表示买来送给奶奶的水果。',
    ],
  };
  document.querySelectorAll('[data-apple-attention]').forEach(figure => {
    const kind = figure.dataset.appleAttention;
    const buttons = [...figure.querySelectorAll('[data-apple-case]')];
    const render = value => {
      buttons.forEach(button => button.setAttribute('aria-pressed', String(Number(button.dataset.appleCase) === value)));
      figure.querySelectorAll('[data-apple-trace]').forEach(trace => trace.classList.toggle('is-active', Number(trace.dataset.appleTrace) === value));
      figure.querySelector('[data-apple-status]').textContent = (kind === 'self' ? examples.selfStatus : examples.cross)[value];
      if (kind === 'self') figure.querySelector('[data-apple-query]').textContent = examples.self[value];
    };
    buttons.forEach(button => button.addEventListener('click', () => render(Number(button.dataset.appleCase))));
  });
})();
