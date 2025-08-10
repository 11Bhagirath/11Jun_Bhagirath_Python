
// Shared site script: dropdown, login flow, chatbot and redirect handling

document.addEventListener('DOMContentLoaded', function(){
  // mega dropdown toggle
  document.querySelectorAll('.mega-btn').forEach(btn=>{
    const wrap = btn.closest('.mega');
    btn.addEventListener('click', e=>{ e.stopPropagation(); wrap.classList.toggle('open'); });
  });
  document.addEventListener('click', ()=> document.querySelectorAll('.mega').forEach(m=>m.classList.remove('open')));

  // highlight active link
  const path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach(a=>{
    if(a.getAttribute('href')===path) a.classList.add('active-link');
  });

  // login redirect handling (on login page)
  const loginForm = document.getElementById('loginForm');
  if(loginForm){
    loginForm.addEventListener('submit', function(e){
      e.preventDefault();
      const role = document.getElementById('role').value;
      const user = document.getElementById('username').value;
      // demo: store in localStorage
      localStorage.setItem('e_police_loggedIn','1');
      localStorage.setItem('e_police_user', user || 'user');
      localStorage.setItem('e_police_role', role);
      // redirect back if requested
      const params = new URLSearchParams(location.search);
      const red = params.get('redirect') || 'index.html';
      window.location.href = red;
    });
  }

  // protect pages that require login (data-protect attribute)
  document.querySelectorAll('[data-protect="true"]').forEach(el=>{
    const logged = localStorage.getItem('e_police_loggedIn');
    if(!logged){
      // redirect to login with redirect param
      const current = location.pathname.split('/').pop();
      window.location.href = 'login.html?redirect='+encodeURIComponent(current);
    }
  });

  // Chat widget behavior (only present on some pages)
  const chatToggle = document.getElementById('chatToggle');
  const chatWindow = document.getElementById('chatWindow');
  if(chatToggle){
    chatToggle.addEventListener('click', ()=> chatWindow.classList.toggle('open'));
    document.getElementById('chatSend')?.addEventListener('click', sendChat);
    document.getElementById('chatInput')?.addEventListener('keydown', function(e){ if(e.key==='Enter') sendChat(); });
  }
});

// simple chat implementation
function sendChat(){
  const input = document.getElementById('chatInput');
  const body = document.getElementById('chatBody');
  if(!input || !body) return;
  const text = input.value.trim(); if(!text) return;
  addMsg('user', text);
  input.value='';
  setTimeout(()=>{
    let reply = 'I can help with registration, filing FIRs, emergency contacts and rules. Try: "How to file FIR?"';
    const t = text.toLowerCase();
    if(t.includes('register')) reply = 'To register: go to Register page -> fill details -> submit.';
    if(t.includes('fir') || t.includes('file')) reply = 'To file FIR: Login as Citizen -> Add FIR -> provide evidence if any.';
    if(t.includes('emergency')) reply = 'Emergency helpline: 112 (police). For cybercrime, call 1930.';
    addMsg('bot', reply);
  }, 600 + Math.random()*800);
}

function addMsg(who, text){
  const body = document.getElementById('chatBody');
  if(!body) return;
  const div = document.createElement('div'); div.className = 'msg '+(who==='bot'?'bot':'user');
  const bubble = document.createElement('div'); bubble.className = 'bubble '+(who==='user'?'user':'');
  bubble.textContent = text;
  div.appendChild(bubble);
  body.appendChild(div);
  body.scrollTop = body.scrollHeight;
}
