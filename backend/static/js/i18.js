(function(){
var D={ar:window.AR_DICT||{},en:window.EN_DICT||{}},LANG='fr',ON=false,store=new WeakMap(),astore=new WeakMap(),ATT=['placeholder','aria-label','alt','title','label'];
var MON={
ar:{Janvier:'يناير',Février:'فبراير',Mars:'مارس',Avril:'أبريل',Mai:'ماي',Juin:'يونيو',Juillet:'يوليوز',Août:'غشت',Septembre:'شتنبر',Octobre:'أكتوبر',Novembre:'نونبر',Décembre:'دجنبر'},
en:{Janvier:'January',Février:'February',Mars:'March',Avril:'April',Mai:'May',Juin:'June',Juillet:'July',Août:'August',Septembre:'September',Octobre:'October',Novembre:'November',Décembre:'December'}
};
var P={
ar:{sep:' : ',photo:'صورة : ',dl:'تحميل : ',recu:'تم استلام الملف بتاريخ ',dos:'الملف ',brand:' — أم القرى للتميّز',ref:'المرجع : ',code:'رمز الولوج : '},
en:{sep:': ',photo:'Photo: ',dl:'Download: ',recu:'File received on ',dos:'File ',brand:' — UMM ALQORA d’EXCELLENCE',ref:'Reference: ',code:'Access code: '}
};
var RX=[];
function norm(s){return s.replace(/\s+/g,' ').trim()}
function look(k){var d=D[LANG];return d&&Object.prototype.hasOwnProperty.call(d,k)?d[k]:undefined}
function trk(k){var v=look(norm(k));return v===undefined?k:v}
function build(){
 if(!P[LANG]){RX=[];return}
 var M=MON[LANG],p=P[LANG],low={};
 Object.keys(M).forEach(function(k){low[k.toLowerCase()]=M[k]});
 RX=[
 [/^([A-Za-zéûè]+) (\d{4})$/,function(m){return M[m[1]]?M[m[1]]+' '+m[2]:undefined}],
 [/^(\d+) ([a-zéûè]+) : (.+)$/,function(m){var a=low[m[2]];return a?m[1]+' '+a+p.sep+trk(m[3]):undefined}],
 [/^Photo : (.+)$/,function(m){return p.photo+trk(m[1])}],
 [/^Télécharger : (.+)$/,function(m){return p.dl+trk(m[1])}],
 [/^Dossier reçu le (.+)$/,function(m){return p.recu+m[1]}],
 [/^Dossier (UMM-.+)$/,function(m){return p.dos+m[1]}],
 [/^(.+) — UMM ALQORA d’EXCELLENCE$/,function(m){return trk(m[1])+p.brand}],
 [/^› (.+)$/,function(m){return'› '+trk(m[1])}],
 [/^Référence : (.+)$/,function(m){return p.ref+m[1]}],
 [/^Code d’accès : (.+)$/,function(m){return p.code+m[1]}]
 ];
}
function tr(s){var k=norm(s);if(!k)return s;var v=look(k);
 if(v===undefined){for(var i=0;i<RX.length;i++){var m=k.match(RX[i][0]);if(m){v=RX[i][1](m);if(v!==undefined)break}}}
 if(v===undefined)return s;return s.match(/^\s*/)[0]+v+s.match(/\s*$/)[0]}
function inSw(n){var e=n.nodeType===1?n:n.parentNode;return !!(e&&e.closest&&e.closest('#lang'))}
function node(n){var p=n.parentNode;if(!p||/^(SCRIPT|STYLE|NOSCRIPT)$/.test(p.nodeName))return;if(inSw(n))return;
 if(ON){if(!store.has(n))store.set(n,n.nodeValue);var o=store.get(n),t=tr(o);if(n.nodeValue!==t)n.nodeValue=t}
 else if(store.has(n)){n.nodeValue=store.get(n)}}
function attrs(el){if(inSw(el))return;ATT.forEach(function(a){if(!el.hasAttribute||!el.hasAttribute(a))return;var m=astore.get(el)||{};
 if(ON){if(!(a in m))m[a]=el.getAttribute(a);el.setAttribute(a,tr(m[a]))}else if(a in m){el.setAttribute(a,m[a])}astore.set(el,m)})}
function walk(root){if(!root)return;if(root.nodeType===3){node(root);return}if(root.nodeType!==1&&root.nodeType!==9)return;
 var base=root.nodeType===9?root.documentElement:root;
 var w=document.createTreeWalker(base,NodeFilter.SHOW_TEXT),n;while((n=w.nextNode()))node(n);
 attrs(base);base.querySelectorAll&&base.querySelectorAll('[placeholder],[aria-label],[alt],[title],[label]').forEach(attrs)}
function setLang(l,save){
 if(l!=='fr'&&l!=='en'&&l!=='ar')l='fr';
 LANG=l;ON=l!=='fr';build();
 document.documentElement.lang=l;document.documentElement.dir=l==='ar'?'rtl':'ltr';
 document.querySelectorAll('#lang [data-lang]').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-lang')===l?'true':'false')});
 if(save){try{localStorage.setItem('nh:lang',l)}catch(e){}}
 walk(document.documentElement)}
new MutationObserver(function(ms){if(!ON)return;ms.forEach(function(m){m.addedNodes.forEach(function(n){walk(n)})})}).observe(document.documentElement,{childList:true,subtree:true});
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('#lang [data-lang]');if(b)setLang(b.getAttribute('data-lang'),true)});
var q=(location.search.match(/[?&]lang=(fr|en|ar)\b/)||[])[1],saved=null;try{saved=localStorage.getItem('nh:lang')}catch(e){}
window.NH_I18N={set:setLang,dict:D,tr:tr};
var start=q||saved;if(start==='ar'||start==='en')setLang(start,false);
})();