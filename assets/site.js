const menu=document.querySelector('.menu');
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&menu?.open){menu.open=false;menu.querySelector('summary').focus();}});
document.addEventListener('click',event=>{if(menu?.open&&!menu.contains(event.target))menu.open=false;});
const choices=[...document.querySelectorAll('[data-opportunity]')];
const result=document.querySelector('#oracle-result');
function updateOracle(){
  const selected=choices.filter(input=>input.checked).map(input=>input.value);
  let title='Leave some room in the journey.';
  let copy='With no new invitation in view, Sire can stay a little longer, finish a chapter and explore where he already is. The next country can wait for a worthwhile reason to move.';
  if(selected.length===1&&selected[0]==='reading'){title='A reading opens a door.';copy='A woman who has read his work invites him to a small readers’ gathering in a harbour city. That gives him a reason to look more closely: time to talk, share a chapter and discover the city through the people who live there.';}
  if(selected.length===1&&selected[0]==='craft'){title='Stay long enough to learn something.';copy='A mountain workshop offers a place to learn a local craft. A longer stay could make room for useful work, patient learning and new friendships. He weighs that against the writing and commitments already in his life.';}
  if(selected.length===1&&selected[0]==='music'){title='Let music change the direction.';copy='An arts festival brings musicians, makers and shared meals together. He could contribute a story session and spend time listening. The event offers a meeting point for several interests at once.';}
  if(selected.length>1){title=selected.length===3?'Several possibilities. An open route.':'Two invitations change the picture.';copy='The oracle brings '+selected.map(v=>({reading:'the readers’ gathering',craft:'the craft workshop',music:'the arts festival'}[v])).join(', ').replace(/, ([^,]*)$/,' and $1')+' into the same conversation. It checks timing, travel, resources, energy and existing promises. A longer stay, a return visit or a different order may work better. Sire chooses which possibility to explore.';}
  result.replaceChildren(Object.assign(document.createElement('h3'),{textContent:title}),Object.assign(document.createElement('p'),{textContent:copy}));
}
choices.forEach(input=>input.addEventListener('change',updateOracle));
