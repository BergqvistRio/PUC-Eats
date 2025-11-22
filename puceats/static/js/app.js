(function(){
  const body = document.body;
  const openers = document.querySelectorAll('[data-modal-target]');
  let lastFocused = null;

  function openModal(modal){
    if(!modal) return;
    lastFocused = document.activeElement;
    modal.classList.add('isOpen');
    modal.setAttribute('aria-hidden','false');
    body.classList.add('modalOpen');
  }

  function closeModal(modal){
    if(!modal) return;
    modal.classList.remove('isOpen');
    modal.setAttribute('aria-hidden','true');
    body.classList.remove('modalOpen');
    if(lastFocused && typeof lastFocused.focus === 'function'){
      try { lastFocused.focus(); } catch {}
    }
  }

  openers.forEach(opener => {
    opener.addEventListener('click', (e)=>{
      e.preventDefault();
      const targetSel = opener.getAttribute('data-modal-target');
      const modal = document.querySelector(targetSel);
      openModal(modal);
    });
  });

  document.addEventListener('click', (e)=>{
    const closeEl = e.target.closest('[data-modal-close]');
    if(closeEl){
      const modal = closeEl.closest('.modalContainer');
      closeModal(modal);
    }
  });

  document.addEventListener('keydown', (e)=>{
    if(e.key === 'Escape'){
      const modal = document.querySelector('.modalContainer.isOpen');
      if(modal){ closeModal(modal); }
    }
  });

  const imageChoiceInputs = document.querySelectorAll('[data-image-choice]');
  const grupoUrl = document.getElementById('grupoImagemUrl');
  const grupoUpload = document.getElementById('grupoImagemUpload');
  const campoUrl = document.getElementById('campoImagemUrl');
  const campoUpload = document.getElementById('campoImagemUpload');

  function updateImageChoice(){
    const choice = document.querySelector('[data-image-choice]:checked');
    if(!choice) return;
    const isUrl = choice.value === 'url';
    if(isUrl){
      grupoUrl.classList.remove('d-none');
      grupoUpload.classList.add('d-none');
      campoUrl.toggleAttribute('required', true);
      campoUpload.toggleAttribute('required', false);
      campoUpload.value = '';
    } else {
      grupoUrl.classList.add('d-none');
      grupoUpload.classList.remove('d-none');
      campoUrl.toggleAttribute('required', false);
      campoUpload.toggleAttribute('required', true);
      campoUrl.value = '';
    }
  }

  imageChoiceInputs.forEach(inp => inp.addEventListener('change', updateImageChoice));
  updateImageChoice();
})();
