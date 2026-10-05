(function(){let e=document.createElement(`link`).relList;if(e&&e.supports&&e.supports(`modulepreload`))return;for(let e of document.querySelectorAll(`link[rel="modulepreload"]`))n(e);new MutationObserver(e=>{for(let t of e)if(t.type===`childList`)for(let e of t.addedNodes)e.tagName===`LINK`&&e.rel===`modulepreload`&&n(e)}).observe(document,{childList:!0,subtree:!0});function t(e){let t={};return e.integrity&&(t.integrity=e.integrity),e.referrerPolicy&&(t.referrerPolicy=e.referrerPolicy),t.credentials=e.crossOrigin===`use-credentials`?`include`:e.crossOrigin===`anonymous`?`omit`:`same-origin`,t}function n(e){if(e.ep)return;e.ep=!0;let n=t(e);fetch(e.href,n)}})();var e=globalThis,t=e.ShadowRoot&&(e.ShadyCSS===void 0||e.ShadyCSS.nativeShadow)&&`adoptedStyleSheets`in Document.prototype&&`replace`in CSSStyleSheet.prototype,n=Symbol(),r=new WeakMap,i=class{constructor(e,t,r){if(this._$cssResult$=!0,r!==n)throw Error("CSSResult is not constructable. Use `unsafeCSS` or `css` instead.");this.cssText=e,this.t=t}get styleSheet(){let e=this.o,n=this.t;if(t&&e===void 0){let t=n!==void 0&&n.length===1;t&&(e=r.get(n)),e===void 0&&((this.o=e=new CSSStyleSheet).replaceSync(this.cssText),t&&r.set(n,e))}return e}toString(){return this.cssText}},a=e=>new i(typeof e==`string`?e:e+``,void 0,n),o=(e,...t)=>new i(e.length===1?e[0]:t.reduce((t,n,r)=>t+(e=>{if(!0===e._$cssResult$)return e.cssText;if(typeof e==`number`)return e;throw Error(`Value passed to 'css' function must be a 'css' function result: `+e+`. Use 'unsafeCSS' to pass non-literal values, but take care to ensure page security.`)})(n)+e[r+1],e[0]),e,n),s=(n,r)=>{if(t)n.adoptedStyleSheets=r.map(e=>e instanceof CSSStyleSheet?e:e.styleSheet);else for(let t of r){let r=document.createElement(`style`),i=e.litNonce;i!==void 0&&r.setAttribute(`nonce`,i),r.textContent=t.cssText,n.appendChild(r)}},c=t?e=>e:e=>e instanceof CSSStyleSheet?(e=>{let t=``;for(let n of e.cssRules)t+=n.cssText;return a(t)})(e):e,{is:l,defineProperty:u,getOwnPropertyDescriptor:d,getOwnPropertyNames:f,getOwnPropertySymbols:p,getPrototypeOf:m}=Object,h=globalThis,g=h.trustedTypes,_=g?g.emptyScript:``,v=h.reactiveElementPolyfillSupport,y=(e,t)=>e,b={toAttribute(e,t){switch(t){case Boolean:e=e?_:null;break;case Object:case Array:e=e==null?e:JSON.stringify(e)}return e},fromAttribute(e,t){let n=e;switch(t){case Boolean:n=e!==null;break;case Number:n=e===null?null:Number(e);break;case Object:case Array:try{n=JSON.parse(e)}catch{n=null}}return n}},x=(e,t)=>!l(e,t),S={attribute:!0,type:String,converter:b,reflect:!1,useDefault:!1,hasChanged:x};Symbol.metadata??=Symbol(`metadata`),h.litPropertyMetadata??=new WeakMap;var C=class extends HTMLElement{static addInitializer(e){this._$Ei(),(this.l??=[]).push(e)}static get observedAttributes(){return this.finalize(),this._$Eh&&[...this._$Eh.keys()]}static createProperty(e,t=S){if(t.state&&(t.attribute=!1),this._$Ei(),this.prototype.hasOwnProperty(e)&&((t=Object.create(t)).wrapped=!0),this.elementProperties.set(e,t),!t.noAccessor){let n=Symbol(),r=this.getPropertyDescriptor(e,n,t);r!==void 0&&u(this.prototype,e,r)}}static getPropertyDescriptor(e,t,n){let{get:r,set:i}=d(this.prototype,e)??{get(){return this[t]},set(e){this[t]=e}};return{get:r,set(t){let a=r?.call(this);i?.call(this,t),this.requestUpdate(e,a,n)},configurable:!0,enumerable:!0}}static getPropertyOptions(e){return this.elementProperties.get(e)??S}static _$Ei(){if(this.hasOwnProperty(y(`elementProperties`)))return;let e=m(this);e.finalize(),e.l!==void 0&&(this.l=[...e.l]),this.elementProperties=new Map(e.elementProperties)}static finalize(){if(this.hasOwnProperty(y(`finalized`)))return;if(this.finalized=!0,this._$Ei(),this.hasOwnProperty(y(`properties`))){let e=this.properties,t=[...f(e),...p(e)];for(let n of t)this.createProperty(n,e[n])}let e=this[Symbol.metadata];if(e!==null){let t=litPropertyMetadata.get(e);if(t!==void 0)for(let[e,n]of t)this.elementProperties.set(e,n)}this._$Eh=new Map;for(let[e,t]of this.elementProperties){let n=this._$Eu(e,t);n!==void 0&&this._$Eh.set(n,e)}this.elementStyles=this.finalizeStyles(this.styles)}static finalizeStyles(e){let t=[];if(Array.isArray(e)){let n=new Set(e.flat(1/0).reverse());for(let e of n)t.unshift(c(e))}else e!==void 0&&t.push(c(e));return t}static _$Eu(e,t){let n=t.attribute;return!1===n?void 0:typeof n==`string`?n:typeof e==`string`?e.toLowerCase():void 0}constructor(){super(),this._$Ep=void 0,this.isUpdatePending=!1,this.hasUpdated=!1,this._$Em=null,this._$Ev()}_$Ev(){this._$ES=new Promise(e=>this.enableUpdating=e),this._$AL=new Map,this._$E_(),this.requestUpdate(),this.constructor.l?.forEach(e=>e(this))}addController(e){(this._$EO??=new Set).add(e),this.renderRoot!==void 0&&this.isConnected&&e.hostConnected?.()}removeController(e){this._$EO?.delete(e)}_$E_(){let e=new Map,t=this.constructor.elementProperties;for(let n of t.keys())this.hasOwnProperty(n)&&(e.set(n,this[n]),delete this[n]);e.size>0&&(this._$Ep=e)}createRenderRoot(){let e=this.shadowRoot??this.attachShadow(this.constructor.shadowRootOptions);return s(e,this.constructor.elementStyles),e}connectedCallback(){this.renderRoot??=this.createRenderRoot(),this.enableUpdating(!0),this._$EO?.forEach(e=>e.hostConnected?.())}enableUpdating(e){}disconnectedCallback(){this._$EO?.forEach(e=>e.hostDisconnected?.())}attributeChangedCallback(e,t,n){this._$AK(e,n)}_$ET(e,t){let n=this.constructor.elementProperties.get(e),r=this.constructor._$Eu(e,n);if(r!==void 0&&!0===n.reflect){let i=(n.converter?.toAttribute===void 0?b:n.converter).toAttribute(t,n.type);this._$Em=e,i==null?this.removeAttribute(r):this.setAttribute(r,i),this._$Em=null}}_$AK(e,t){let n=this.constructor,r=n._$Eh.get(e);if(r!==void 0&&this._$Em!==r){let e=n.getPropertyOptions(r),i=typeof e.converter==`function`?{fromAttribute:e.converter}:e.converter?.fromAttribute===void 0?b:e.converter;this._$Em=r;let a=i.fromAttribute(t,e.type);this[r]=a??this._$Ej?.get(r)??a,this._$Em=null}}requestUpdate(e,t,n,r=!1,i){if(e!==void 0){let a=this.constructor;if(!1===r&&(i=this[e]),n??=a.getPropertyOptions(e),!((n.hasChanged??x)(i,t)||n.useDefault&&n.reflect&&i===this._$Ej?.get(e)&&!this.hasAttribute(a._$Eu(e,n))))return;this.C(e,t,n)}!1===this.isUpdatePending&&(this._$ES=this._$EP())}C(e,t,{useDefault:n,reflect:r,wrapped:i},a){n&&!(this._$Ej??=new Map).has(e)&&(this._$Ej.set(e,a??t??this[e]),!0!==i||a!==void 0)||(this._$AL.has(e)||(this.hasUpdated||n||(t=void 0),this._$AL.set(e,t)),!0===r&&this._$Em!==e&&(this._$Eq??=new Set).add(e))}async _$EP(){this.isUpdatePending=!0;try{await this._$ES}catch(e){Promise.reject(e)}let e=this.scheduleUpdate();return e!=null&&await e,!this.isUpdatePending}scheduleUpdate(){return this.performUpdate()}performUpdate(){if(!this.isUpdatePending)return;if(!this.hasUpdated){if(this.renderRoot??=this.createRenderRoot(),this._$Ep){for(let[e,t]of this._$Ep)this[e]=t;this._$Ep=void 0}let e=this.constructor.elementProperties;if(e.size>0)for(let[t,n]of e){let{wrapped:e}=n,r=this[t];!0!==e||this._$AL.has(t)||r===void 0||this.C(t,void 0,n,r)}}let e=!1,t=this._$AL;try{e=this.shouldUpdate(t),e?(this.willUpdate(t),this._$EO?.forEach(e=>e.hostUpdate?.()),this.update(t)):this._$EM()}catch(t){throw e=!1,this._$EM(),t}e&&this._$AE(t)}willUpdate(e){}_$AE(e){this._$EO?.forEach(e=>e.hostUpdated?.()),this.hasUpdated||(this.hasUpdated=!0,this.firstUpdated(e)),this.updated(e)}_$EM(){this._$AL=new Map,this.isUpdatePending=!1}get updateComplete(){return this.getUpdateComplete()}getUpdateComplete(){return this._$ES}shouldUpdate(e){return!0}update(e){this._$Eq&&=this._$Eq.forEach(e=>this._$ET(e,this[e])),this._$EM()}updated(e){}firstUpdated(e){}};C.elementStyles=[],C.shadowRootOptions={mode:`open`},C[y(`elementProperties`)]=new Map,C[y(`finalized`)]=new Map,v?.({ReactiveElement:C}),(h.reactiveElementVersions??=[]).push(`2.1.2`);var w=globalThis,T=e=>e,E=w.trustedTypes,D=E?E.createPolicy(`lit-html`,{createHTML:e=>e}):void 0,ee=`$lit$`,te=`lit$${Math.random().toFixed(9).slice(2)}$`,ne=`?`+te,re=`<${ne}>`,ie=document,ae=()=>ie.createComment(``),oe=e=>e===null||typeof e!=`object`&&typeof e!=`function`,se=Array.isArray,ce=e=>se(e)||typeof e?.[Symbol.iterator]==`function`,le=`[ 	
\f\r]`,ue=/<(?:(!--|\/[^a-zA-Z])|(\/?[a-zA-Z][^>\s]*)|(\/?$))/g,de=/-->/g,fe=/>/g,pe=RegExp(`>|${le}(?:([^\\s"'>=/]+)(${le}*=${le}*(?:[^ \t\n\f\r"'\`<>=]|("|')|))|$)`,`g`),me=/'/g,he=/"/g,ge=/^(?:script|style|textarea|title)$/i,_e=e=>(t,...n)=>({_$litType$:e,strings:t,values:n}),O=_e(1),k=_e(2),ve=Symbol.for(`lit-noChange`),A=Symbol.for(`lit-nothing`),ye=new WeakMap,be=ie.createTreeWalker(ie,129);function xe(e,t){if(!se(e)||!e.hasOwnProperty(`raw`))throw Error(`invalid template strings array`);return D===void 0?t:D.createHTML(t)}var Se=(e,t)=>{let n=e.length-1,r=[],i,a=t===2?`<svg>`:t===3?`<math>`:``,o=ue;for(let t=0;t<n;t++){let n=e[t],s,c,l=-1,u=0;for(;u<n.length&&(o.lastIndex=u,c=o.exec(n),c!==null);)u=o.lastIndex,o===ue?c[1]===`!--`?o=de:c[1]===void 0?c[2]===void 0?c[3]!==void 0&&(o=pe):(ge.test(c[2])&&(i=RegExp(`</`+c[2],`g`)),o=pe):o=fe:o===pe?c[0]===`>`?(o=i??ue,l=-1):c[1]===void 0?l=-2:(l=o.lastIndex-c[2].length,s=c[1],o=c[3]===void 0?pe:c[3]===`"`?he:me):o===he||o===me?o=pe:o===de||o===fe?o=ue:(o=pe,i=void 0);let d=o===pe&&e[t+1].startsWith(`/>`)?` `:``;a+=o===ue?n+re:l>=0?(r.push(s),n.slice(0,l)+ee+n.slice(l)+te+d):n+te+(l===-2?t:d)}return[xe(e,a+(e[n]||`<?>`)+(t===2?`</svg>`:t===3?`</math>`:``)),r]},Ce=class e{constructor({strings:t,_$litType$:n},r){let i;this.parts=[];let a=0,o=0,s=t.length-1,c=this.parts,[l,u]=Se(t,n);if(this.el=e.createElement(l,r),be.currentNode=this.el.content,n===2||n===3){let e=this.el.content.firstChild;e.replaceWith(...e.childNodes)}for(;(i=be.nextNode())!==null&&c.length<s;){if(i.nodeType===1){if(i.hasAttributes())for(let e of i.getAttributeNames())if(e.endsWith(ee)){let t=u[o++],n=i.getAttribute(e).split(te),r=/([.?@])?(.*)/.exec(t);c.push({type:1,index:a,name:r[2],strings:n,ctor:r[1]===`.`?Oe:r[1]===`?`?ke:r[1]===`@`?Ae:De}),i.removeAttribute(e)}else e.startsWith(te)&&(c.push({type:6,index:a}),i.removeAttribute(e));if(ge.test(i.tagName)){let e=i.textContent.split(te),t=e.length-1;if(t>0){i.textContent=E?E.emptyScript:``;for(let n=0;n<t;n++)i.append(e[n],ae()),be.nextNode(),c.push({type:2,index:++a});i.append(e[t],ae())}}}else if(i.nodeType===8){if(i.data===ne)c.push({type:2,index:a});else{let e=-1;for(;(e=i.data.indexOf(te,e+1))!==-1;)c.push({type:7,index:a}),e+=te.length-1}}a++}}static createElement(e,t){let n=ie.createElement(`template`);return n.innerHTML=e,n}};function we(e,t,n=e,r){if(t===ve)return t;let i=r===void 0?n._$Cl:n._$Co?.[r],a=oe(t)?void 0:t._$litDirective$;return i?.constructor!==a&&(i?._$AO?.(!1),a===void 0?i=void 0:(i=new a(e),i._$AT(e,n,r)),r===void 0?n._$Cl=i:(n._$Co??=[])[r]=i),i!==void 0&&(t=we(e,i._$AS(e,t.values),i,r)),t}var Te=class{constructor(e,t){this._$AV=[],this._$AN=void 0,this._$AD=e,this._$AM=t}get parentNode(){return this._$AM.parentNode}get _$AU(){return this._$AM._$AU}u(e){let{el:{content:t},parts:n}=this._$AD,r=(e?.creationScope??ie).importNode(t,!0);be.currentNode=r;let i=be.nextNode(),a=0,o=0,s=n[0];for(;s!==void 0;){if(a===s.index){let t;s.type===2?t=new Ee(i,i.nextSibling,this,e):s.type===1?t=new s.ctor(i,s.name,s.strings,this,e):s.type===6&&(t=new je(i,this,e)),this._$AV.push(t),s=n[++o]}a!==s?.index&&(i=be.nextNode(),a++)}return be.currentNode=ie,r}p(e){let t=0;for(let n of this._$AV)n!==void 0&&(n.strings===void 0?n._$AI(e[t]):(n._$AI(e,n,t),t+=n.strings.length-2)),t++}},Ee=class e{get _$AU(){return this._$AM?._$AU??this._$Cv}constructor(e,t,n,r){this.type=2,this._$AH=A,this._$AN=void 0,this._$AA=e,this._$AB=t,this._$AM=n,this.options=r,this._$Cv=r?.isConnected??!0}get parentNode(){let e=this._$AA.parentNode,t=this._$AM;return t!==void 0&&e?.nodeType===11&&(e=t.parentNode),e}get startNode(){return this._$AA}get endNode(){return this._$AB}_$AI(e,t=this){e=we(this,e,t),oe(e)?e===A||e==null||e===``?(this._$AH!==A&&this._$AR(),this._$AH=A):e!==this._$AH&&e!==ve&&this._(e):e._$litType$===void 0?e.nodeType===void 0?ce(e)?this.k(e):this._(e):this.T(e):this.$(e)}O(e){return this._$AA.parentNode.insertBefore(e,this._$AB)}T(e){this._$AH!==e&&(this._$AR(),this._$AH=this.O(e))}_(e){this._$AH!==A&&oe(this._$AH)?this._$AA.nextSibling.data=e:this.T(ie.createTextNode(e)),this._$AH=e}$(e){let{values:t,_$litType$:n}=e,r=typeof n==`number`?this._$AC(e):(n.el===void 0&&(n.el=Ce.createElement(xe(n.h,n.h[0]),this.options)),n);if(this._$AH?._$AD===r)this._$AH.p(t);else{let e=new Te(r,this),n=e.u(this.options);e.p(t),this.T(n),this._$AH=e}}_$AC(e){let t=ye.get(e.strings);return t===void 0&&ye.set(e.strings,t=new Ce(e)),t}k(t){se(this._$AH)||(this._$AH=[],this._$AR());let n=this._$AH,r,i=0;for(let a of t)i===n.length?n.push(r=new e(this.O(ae()),this.O(ae()),this,this.options)):r=n[i],r._$AI(a),i++;i<n.length&&(this._$AR(r&&r._$AB.nextSibling,i),n.length=i)}_$AR(e=this._$AA.nextSibling,t){for(this._$AP?.(!1,!0,t);e!==this._$AB;){let t=T(e).nextSibling;T(e).remove(),e=t}}setConnected(e){this._$AM===void 0&&(this._$Cv=e,this._$AP?.(e))}},De=class{get tagName(){return this.element.tagName}get _$AU(){return this._$AM._$AU}constructor(e,t,n,r,i){this.type=1,this._$AH=A,this._$AN=void 0,this.element=e,this.name=t,this._$AM=r,this.options=i,n.length>2||n[0]!==``||n[1]!==``?(this._$AH=Array(n.length-1).fill(new String),this.strings=n):this._$AH=A}_$AI(e,t=this,n,r){let i=this.strings,a=!1;if(i===void 0)e=we(this,e,t,0),a=!oe(e)||e!==this._$AH&&e!==ve,a&&(this._$AH=e);else{let r=e,o,s;for(e=i[0],o=0;o<i.length-1;o++)s=we(this,r[n+o],t,o),s===ve&&(s=this._$AH[o]),a||=!oe(s)||s!==this._$AH[o],s===A?e=A:e!==A&&(e+=(s??``)+i[o+1]),this._$AH[o]=s}a&&!r&&this.j(e)}j(e){e===A?this.element.removeAttribute(this.name):this.element.setAttribute(this.name,e??``)}},Oe=class extends De{constructor(){super(...arguments),this.type=3}j(e){this.element[this.name]=e===A?void 0:e}},ke=class extends De{constructor(){super(...arguments),this.type=4}j(e){this.element.toggleAttribute(this.name,!!e&&e!==A)}},Ae=class extends De{constructor(e,t,n,r,i){super(e,t,n,r,i),this.type=5}_$AI(e,t=this){if((e=we(this,e,t,0)??A)===ve)return;let n=this._$AH,r=e===A&&n!==A||e.capture!==n.capture||e.once!==n.once||e.passive!==n.passive,i=e!==A&&(n===A||r);r&&this.element.removeEventListener(this.name,this,n),i&&this.element.addEventListener(this.name,this,e),this._$AH=e}handleEvent(e){typeof this._$AH==`function`?this._$AH.call(this.options?.host??this.element,e):this._$AH.handleEvent(e)}},je=class{constructor(e,t,n){this.element=e,this.type=6,this._$AN=void 0,this._$AM=t,this.options=n}get _$AU(){return this._$AM._$AU}_$AI(e){we(this,e)}},Me={M:ee,P:te,A:ne,C:1,L:Se,R:Te,D:ce,V:we,I:Ee,H:De,N:ke,U:Ae,B:Oe,F:je},Ne=w.litHtmlPolyfillSupport;Ne?.(Ce,Ee),(w.litHtmlVersions??=[]).push(`3.3.3`);var Pe=(e,t,n)=>{let r=n?.renderBefore??t,i=r._$litPart$;if(i===void 0){let e=n?.renderBefore??null;r._$litPart$=i=new Ee(t.insertBefore(ae(),e),e,void 0,n??{})}return i._$AI(e),i},Fe=globalThis,j=class extends C{constructor(){super(...arguments),this.renderOptions={host:this},this._$Do=void 0}createRenderRoot(){let e=super.createRenderRoot();return this.renderOptions.renderBefore??=e.firstChild,e}update(e){let t=this.render();this.hasUpdated||(this.renderOptions.isConnected=this.isConnected),super.update(e),this._$Do=Pe(t,this.renderRoot,this.renderOptions)}connectedCallback(){super.connectedCallback(),this._$Do?.setConnected(!0)}disconnectedCallback(){super.disconnectedCallback(),this._$Do?.setConnected(!1)}render(){return ve}};j._$litElement$=!0,j.finalized=!0,Fe.litElementHydrateSupport?.({LitElement:j});var Ie=Fe.litElementPolyfillSupport;Ie?.({LitElement:j}),(Fe.litElementVersions??=[]).push(`4.2.2`);var M=e=>(t,n)=>{if(n!==void 0)n.addInitializer(()=>{customElements.get(e)||customElements.define(e,t)});else{if(customElements.get(e))return;customElements.define(e,t)}};function N(e,t,n,r){var i=arguments.length,a=i<3?t:r===null?r=Object.getOwnPropertyDescriptor(t,n):r,o;if(typeof Reflect==`object`&&typeof Reflect.decorate==`function`)a=Reflect.decorate(e,t,n,r);else for(var s=e.length-1;s>=0;s--)(o=e[s])&&(a=(i<3?o(a):i>3?o(t,n,a):o(t,n))||a);return i>3&&a&&Object.defineProperty(t,n,a),a}var Le={attribute:!0,type:String,converter:b,reflect:!1,hasChanged:x},Re=(e=Le,t,n)=>{let{kind:r,metadata:i}=n,a=globalThis.litPropertyMetadata.get(i);if(a===void 0&&globalThis.litPropertyMetadata.set(i,a=new Map),r===`setter`&&((e=Object.create(e)).wrapped=!0),a.set(n.name,e),r===`accessor`){let{name:r}=n;return{set(n){let i=t.get.call(this);t.set.call(this,n),this.requestUpdate(r,i,e,!0,n)},init(t){return t!==void 0&&this.C(r,void 0,e,t),t}}}if(r===`setter`){let{name:r}=n;return function(n){let i=this[r];t.call(this,n),this.requestUpdate(r,i,e,!0,n)}}throw Error(`Unsupported decorator location: `+r)};function P(e){return(t,n)=>typeof n==`object`?Re(e,t,n):((e,t,n)=>{let r=t.hasOwnProperty(n);return t.constructor.createProperty(n,e),r?Object.getOwnPropertyDescriptor(t,n):void 0})(e,t,n)}function ze(e){return P({...e,state:!0,attribute:!1})}var Be=(e,t,n)=>(n.configurable=!0,n.enumerable=!0,Reflect.decorate&&typeof t!=`object`&&Object.defineProperty(e,t,n),n);function Ve(e,t){return(n,r,i)=>{let a=t=>t.renderRoot?.querySelector(e)??null;if(t){let{get:e,set:t}=typeof r==`object`?n:i??(()=>{let e=Symbol();return{get(){return this[e]},set(t){this[e]=t}}})();return Be(n,r,{get(){let n=e.call(this);return n===void 0&&(n=a(this),(n!==null||this.hasUpdated)&&t.call(this,n)),n}})}return Be(n,r,{get(){return a(this)}})}}function He(e){return(t,n)=>{let{slot:r,selector:i}=e??{},a=`slot`+(r?`[name=${r}]`:`:not([name])`);return Be(t,n,{get(){let t=(this.renderRoot?.querySelector(a))?.assignedElements(e)??[];return i===void 0?t:t.filter(e=>e.matches(i))}})}}var Ue=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M4 8H8V4H4V8ZM10 20H14V16H10V20ZM4 20H8V16H4V20ZM4 14H8V10H4V14ZM10 14H14V10H10V14ZM16 4V8H20V4H16ZM10 8H14V4H10V8ZM16 14H20V10H16V14ZM16 20H20V16H16V20Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M4 8H8V4H4V8ZM10 20H14V16H10V20ZM4 20H8V16H4V20ZM4 14H8V10H4V14ZM10 14H14V10H10V14ZM16 4V8H20V4H16ZM10 8H14V4H10V8ZM16 14H20V10H16V14ZM16 20H20V16H16V20Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},We=(Ue.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Ue);N([P({type:Boolean})],We.prototype,`useCssColor`,void 0),We=N([M(`obi-applications`)],We);var Ge=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M7.83 11H20V13H7.83L13.41 18.59L12 20L4 12L12 4L13.42 5.41L7.83 11Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M7.83 11H20V13H7.83L13.41 18.59L12 20L4 12L12 4L13.42 5.41L7.83 11Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Ke=(Ge.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Ge);N([P({type:Boolean})],Ke.prototype,`useCssColor`,void 0),Ke=N([M(`obi-arrow-left-google`)],Ke);var qe=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M12 4L10.59 5.41L16.17 11H4V13H16.17L10.59 18.59L12 20L20 12L12 4Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12 4L10.59 5.41L16.17 11H4V13H16.17L10.59 18.59L12 20L20 12L12 4Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Je=(qe.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,qe);N([P({type:Boolean})],Je.prototype,`useCssColor`,void 0),Je=N([M(`obi-arrow-right-google`)],Je);var Ye=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M19 6.41L17.59 5L12 10.59L6.41 5L5 6.41L10.59 12L5 17.59L6.41 19L12 13.41L17.59 19L19 17.59L13.41 12L19 6.41Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M19 6.41L17.59 5L12 10.59L6.41 5L5 6.41L10.59 12L5 17.59L6.41 19L12 13.41L17.59 19L19 17.59L13.41 12L19 6.41Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Xe=(Ye.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Ye);N([P({type:Boolean})],Xe.prototype,`useCssColor`,void 0),Xe=N([M(`obi-close-google`)],Xe);var Ze=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M6 19H9V13H15V19H18V10L12 5.5L6 10V19ZM5.6 21C5.03995 21 4.75992 21 4.54601 20.891C4.35785 20.7951 4.20487 20.6422 4.10899 20.454C4 20.2401 4 19.9601 4 19.4V10.2C4 9.76 4 9.54 4.05767 9.33808C4.10874 9.15924 4.19264 8.99145 4.30506 8.84329C4.432 8.676 4.608 8.544 4.96 8.28L11.04 3.72C11.3843 3.46181 11.5564 3.33271 11.7454 3.28294C11.9123 3.23902 12.0877 3.23902 12.2546 3.28294C12.4436 3.33271 12.6157 3.46181 12.96 3.72L19.04 8.28C19.392 8.544 19.568 8.676 19.6949 8.84329C19.8074 8.99145 19.8913 9.15924 19.9423 9.33808C20 9.54 20 9.76 20 10.2V19.4C20 19.9601 20 20.2401 19.891 20.454C19.7951 20.6422 19.6422 20.7951 19.454 20.891C19.2401 21 18.9601 21 18.4 21H14.6C14.0399 21 13.7599 21 13.546 20.891C13.3578 20.7951 13.2049 20.6422 13.109 20.454C13 20.2401 13 19.9601 13 19.4V15H11V19.4C11 19.9601 11 20.2401 10.891 20.454C10.7951 20.6422 10.6422 20.7951 10.454 20.891C10.2401 21 9.96005 21 9.4 21H5.6Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M6 19H9V13H15V19H18V10L12 5.5L6 10V19ZM5.6 21C5.03995 21 4.75992 21 4.54601 20.891C4.35785 20.7951 4.20487 20.6422 4.10899 20.454C4 20.2401 4 19.9601 4 19.4V10.2C4 9.76 4 9.54 4.05767 9.33808C4.10874 9.15924 4.19264 8.99145 4.30506 8.84329C4.432 8.676 4.608 8.544 4.96 8.28L11.04 3.72C11.3843 3.46181 11.5564 3.33271 11.7454 3.28294C11.9123 3.23902 12.0877 3.23902 12.2546 3.28294C12.4436 3.33271 12.6157 3.46181 12.96 3.72L19.04 8.28C19.392 8.544 19.568 8.676 19.6949 8.84329C19.8074 8.99145 19.8913 9.15924 19.9423 9.33808C20 9.54 20 9.76 20 10.2V19.4C20 19.9601 20 20.2401 19.891 20.454C19.7951 20.6422 19.6422 20.7951 19.454 20.891C19.2401 21 18.9601 21 18.4 21H14.6C14.0399 21 13.7599 21 13.546 20.891C13.3578 20.7951 13.2049 20.6422 13.109 20.454C13 20.2401 13 19.9601 13 19.4V15H11V19.4C11 19.9601 11 20.2401 10.891 20.454C10.7951 20.6422 10.6422 20.7951 10.454 20.891C10.2401 21 9.96005 21 9.4 21H5.6Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Qe=(Ze.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Ze);N([P({type:Boolean})],Qe.prototype,`useCssColor`,void 0),Qe=N([M(`obi-home`)],Qe);var $e=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M3 13H21V11H3V13Z" fill="currentColor"/>
<path d="M3 18H21V16H3V18Z" fill="currentColor"/>
<path d="M3 6V8H21V6H3Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M3 13H21V11H3V13Z" style="fill: var(--element-active-color)"/>
<path d="M3 18H21V16H3V18Z" style="fill: var(--element-active-color)"/>
<path d="M3 6V8H21V6H3Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},et=($e.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,$e);N([P({type:Boolean})],et.prototype,`useCssColor`,void 0),et=N([M(`obi-menu-iec`)],et);var tt=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M14 6C14 4.9 13.1 4 12 4C10.9 4 10 4.9 10 6C10 7.1 10.9 8 12 8C13.1 8 14 7.1 14 6Z" fill="currentColor"/>
<path d="M14 12C14 10.9 13.1 10 12 10C10.9 10 10 10.9 10 12C10 13.1 10.9 14 12 14C13.1 14 14 13.1 14 12Z" fill="currentColor"/>
<path d="M14 18C14 16.9 13.1 16 12 16C10.9 16 10 16.9 10 18C10 19.1 10.9 20 12 20C13.1 20 14 19.1 14 18Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M14 6C14 4.9 13.1 4 12 4C10.9 4 10 4.9 10 6C10 7.1 10.9 8 12 8C13.1 8 14 7.1 14 6Z" style="fill: var(--element-active-color)"/>
<path d="M14 12C14 10.9 13.1 10 12 10C10.9 10 10 10.9 10 12C10 13.1 10.9 14 12 14C13.1 14 14 13.1 14 12Z" style="fill: var(--element-active-color)"/>
<path d="M14 18C14 16.9 13.1 16 12 16C10.9 16 10 16.9 10 18C10 19.1 10.9 20 12 20C13.1 20 14 19.1 14 18Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},nt=(tt.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,tt);N([P({type:Boolean})],nt.prototype,`useCssColor`,void 0),nt=N([M(`obi-more-vertical-google`)],nt);var rt=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M6.99976 11.9999C6.99976 10.6738 7.52654 9.40202 8.46422 8.46434C9.4019 7.52666 10.6737 6.99988 11.9998 6.99988C13.3258 6.99988 14.5976 7.52666 15.5353 8.46434L16.2424 9.17145L9.17133 16.2425L8.46422 15.5354C7.52654 14.5977 6.99976 13.326 6.99976 11.9999ZM9.87843 9.87856C9.31583 10.4412 8.99976 11.2042 8.99976 11.9999C8.99976 12.4516 9.10163 12.8928 9.29265 13.2928L13.2926 9.29277C12.8927 9.10175 12.4515 8.99988 11.9998 8.99988C11.2041 8.99988 10.441 9.31595 9.87843 9.87856Z" fill="currentColor"/>
<path d="M3.51447 19.0709L6.3429 16.2425L7.75711 17.6567L4.92869 20.4852L3.51447 19.0709Z" fill="currentColor"/>
<path d="M0.999756 10.9999H4.99976V12.9999H0.999756V10.9999Z" fill="currentColor"/>
<path d="M4.92874 3.51462L7.75717 6.34304L6.34295 7.75726L3.51453 4.92883L4.92874 3.51462Z" fill="currentColor"/>
<path d="M12.9998 0.999878V4.99988H10.9998V0.999878H12.9998Z" fill="currentColor"/>
<path d="M20.4851 4.92878L17.6567 7.75721L16.2425 6.343L19.0709 3.51457L20.4851 4.92878Z" fill="currentColor"/>
<path d="M20.1539 11C20.8 11 21.4154 11.088 22 11.253C19.5016 11.9515 17.6924 14.036 17.6924 16.5C17.6924 18.964 19.5016 21.0485 22 21.747C21.4154 21.912 20.8 22 20.1539 22C16.757 22 14 19.536 14 16.5C14 13.464 16.757 11 20.1539 11Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M6.99976 11.9999C6.99976 10.6738 7.52654 9.40202 8.46422 8.46434C9.4019 7.52666 10.6737 6.99988 11.9998 6.99988C13.3258 6.99988 14.5976 7.52666 15.5353 8.46434L16.2424 9.17145L9.17133 16.2425L8.46422 15.5354C7.52654 14.5977 6.99976 13.326 6.99976 11.9999ZM9.87843 9.87856C9.31583 10.4412 8.99976 11.2042 8.99976 11.9999C8.99976 12.4516 9.10163 12.8928 9.29265 13.2928L13.2926 9.29277C12.8927 9.10175 12.4515 8.99988 11.9998 8.99988C11.2041 8.99988 10.441 9.31595 9.87843 9.87856Z" style="fill: var(--element-active-color)"/>
<path d="M3.51447 19.0709L6.3429 16.2425L7.75711 17.6567L4.92869 20.4852L3.51447 19.0709Z" style="fill: var(--element-active-color)"/>
<path d="M0.999756 10.9999H4.99976V12.9999H0.999756V10.9999Z" style="fill: var(--element-active-color)"/>
<path d="M4.92874 3.51462L7.75717 6.34304L6.34295 7.75726L3.51453 4.92883L4.92874 3.51462Z" style="fill: var(--element-active-color)"/>
<path d="M12.9998 0.999878V4.99988H10.9998V0.999878H12.9998Z" style="fill: var(--element-active-color)"/>
<path d="M20.4851 4.92878L17.6567 7.75721L16.2425 6.343L19.0709 3.51457L20.4851 4.92878Z" style="fill: var(--element-active-color)"/>
<path d="M20.1539 11C20.8 11 21.4154 11.088 22 11.253C19.5016 11.9515 17.6924 14.036 17.6924 16.5C17.6924 18.964 19.5016 21.0485 22 21.747C21.4154 21.912 20.8 22 20.1539 22C16.757 22 14 19.536 14 16.5C14 13.464 16.757 11 20.1539 11Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},it=(rt.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,rt);N([P({type:Boolean})],it.prototype,`useCssColor`,void 0),it=N([M(`obi-palette-day-night-iec`)],it);var at=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M5.85 17.1C6.7 16.45 7.65 15.9375 8.7 15.5625C9.75 15.1875 10.85 15 12 15C13.15 15 14.25 15.1875 15.3 15.5625C16.35 15.9375 17.3 16.45 18.15 17.1C18.7333 16.4167 19.1875 15.6417 19.5125 14.775C19.8375 13.9083 20 12.9833 20 12C20 9.78333 19.2208 7.89583 17.6625 6.3375C16.1042 4.77917 14.2167 4 12 4C9.78333 4 7.89583 4.77917 6.3375 6.3375C4.77917 7.89583 4 9.78333 4 12C4 12.9833 4.1625 13.9083 4.4875 14.775C4.8125 15.6417 5.26667 16.4167 5.85 17.1ZM12 13C11.0167 13 10.1875 12.6625 9.5125 11.9875C8.8375 11.3125 8.5 10.4833 8.5 9.5C8.5 8.51667 8.8375 7.6875 9.5125 7.0125C10.1875 6.3375 11.0167 6 12 6C12.9833 6 13.8125 6.3375 14.4875 7.0125C15.1625 7.6875 15.5 8.51667 15.5 9.5C15.5 10.4833 15.1625 11.3125 14.4875 11.9875C13.8125 12.6625 12.9833 13 12 13ZM12 22C10.6167 22 9.31667 21.7375 8.1 21.2125C6.88333 20.6875 5.825 19.975 4.925 19.075C4.025 18.175 3.3125 17.1167 2.7875 15.9C2.2625 14.6833 2 13.3833 2 12C2 10.6167 2.2625 9.31667 2.7875 8.1C3.3125 6.88333 4.025 5.825 4.925 4.925C5.825 4.025 6.88333 3.3125 8.1 2.7875C9.31667 2.2625 10.6167 2 12 2C13.3833 2 14.6833 2.2625 15.9 2.7875C17.1167 3.3125 18.175 4.025 19.075 4.925C19.975 5.825 20.6875 6.88333 21.2125 8.1C21.7375 9.31667 22 10.6167 22 12C22 13.3833 21.7375 14.6833 21.2125 15.9C20.6875 17.1167 19.975 18.175 19.075 19.075C18.175 19.975 17.1167 20.6875 15.9 21.2125C14.6833 21.7375 13.3833 22 12 22Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M5.85 17.1C6.7 16.45 7.65 15.9375 8.7 15.5625C9.75 15.1875 10.85 15 12 15C13.15 15 14.25 15.1875 15.3 15.5625C16.35 15.9375 17.3 16.45 18.15 17.1C18.7333 16.4167 19.1875 15.6417 19.5125 14.775C19.8375 13.9083 20 12.9833 20 12C20 9.78333 19.2208 7.89583 17.6625 6.3375C16.1042 4.77917 14.2167 4 12 4C9.78333 4 7.89583 4.77917 6.3375 6.3375C4.77917 7.89583 4 9.78333 4 12C4 12.9833 4.1625 13.9083 4.4875 14.775C4.8125 15.6417 5.26667 16.4167 5.85 17.1ZM12 13C11.0167 13 10.1875 12.6625 9.5125 11.9875C8.8375 11.3125 8.5 10.4833 8.5 9.5C8.5 8.51667 8.8375 7.6875 9.5125 7.0125C10.1875 6.3375 11.0167 6 12 6C12.9833 6 13.8125 6.3375 14.4875 7.0125C15.1625 7.6875 15.5 8.51667 15.5 9.5C15.5 10.4833 15.1625 11.3125 14.4875 11.9875C13.8125 12.6625 12.9833 13 12 13ZM12 22C10.6167 22 9.31667 21.7375 8.1 21.2125C6.88333 20.6875 5.825 19.975 4.925 19.075C4.025 18.175 3.3125 17.1167 2.7875 15.9C2.2625 14.6833 2 13.3833 2 12C2 10.6167 2.2625 9.31667 2.7875 8.1C3.3125 6.88333 4.025 5.825 4.925 4.925C5.825 4.025 6.88333 3.3125 8.1 2.7875C9.31667 2.2625 10.6167 2 12 2C13.3833 2 14.6833 2.2625 15.9 2.7875C17.1167 3.3125 18.175 4.025 19.075 4.925C19.975 5.825 20.6875 6.88333 21.2125 8.1C21.7375 9.31667 22 10.6167 22 12C22 13.3833 21.7375 14.6833 21.2125 15.9C20.6875 17.1167 19.975 18.175 19.075 19.075C18.175 19.975 17.1167 20.6875 15.9 21.2125C14.6833 21.7375 13.3833 22 12 22Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},ot=(at.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,at);N([P({type:Boolean})],ot.prototype,`useCssColor`,void 0),ot=N([M(`obi-user`)],ot);function st(e,t,n){return Math.min(Math.max(e,t),n)}function ct(e){return(e%360+360)%360}function lt(e){return e*Math.PI/180}function ut(e){return e*180/Math.PI}var dt=o`* {
  -webkit-tap-highlight-color: transparent;
}

* {
  box-sizing: border-box;
}

.wrapper {
  background: transparent;
  position: relative;
  min-height: var(--ui-components-button-touch-target-size);
  min-width: var(--ui-components-button-touch-target-size);
  padding: 0;

  appearance: none;
  border: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.wrapper .visible-wrapper {
    position: relative;
    height: var(--ui-components-icon-button-visual-target-size);
    width: var(--ui-components-icon-button-visual-target-size);
    box-sizing: border-box;
    border-radius: var(--ui-components-button-border-radius-top-left)
      var(--ui-components-button-border-radius-top-right)
      var(--ui-components-button-border-radius-bottom-right)
      var(--ui-components-button-border-radius-bottom-left);
    display: flex;
    align-items: center;
    justify-content: center;
  }

.wrapper.corner-left {
    align-items: flex-end;
    padding-right: 0;
  }

.wrapper.corner-left .visible-wrapper {
      width: calc(
        var(--ui-components-icon-button-visual-target-size) +
          var(--ui-components-icon-button-padding-right)
      );
      border-top-right-radius: 0;
      border-bottom-right-radius: 0;
    }

.wrapper.corner-left.hide-divider .visible-wrapper {
      border-right: none;
    }

.wrapper.corner-right {
    align-items: flex-start;
    padding-left: 0;
  }

.wrapper.corner-right .visible-wrapper {
      width: calc(
        var(--ui-components-icon-button-visual-target-size) +
          var(--ui-components-icon-button-padding-left)
      );
      border-top-left-radius: 0;
      border-bottom-left-radius: 0;
    }

.wrapper.corner-right.hide-divider .visible-wrapper {
      border-left: none;
    }

.wrapper.corner-left.corner-right .visible-wrapper {
      width: var(--ui-components-button-touch-target-size);
    }

.wrapper.wide .visible-wrapper {
    width: var(--ui-components-button-touch-target-size);
  }

.wrapper .icon {
    width: var(--ui-components-icon-button-icon-size);
    height: var(--ui-components-icon-button-icon-size);
  }

.wrapper .progress-spinner {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }

.wrapper.has-label {
    padding: var(--ui-components-icon-button-padding-vertical) 0;
  }

.wrapper .label {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-label-font-weight);
    font-size: var(--global-typography-ui-label-font-size);
    line-height: var(--global-typography-ui-label-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  }

.wrapper.variant-normal {
  cursor: pointer;
}

.wrapper.variant-normal:focus {
  outline: none;
}

.wrapper.variant-normal .visible-wrapper {
  border-color: var(--normal-enabled-border-color);
  background-color: var(--normal-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--normal-enabled-border-color);
  --base-background-color: var(--normal-enabled-background-color);
}

.wrapper.variant-normal.activated .visible-wrapper {
  border-color: var(--normal-activated-border-color);
  background-color: var(--normal-activated-background-color);
  --base-border-color: var(--normal-activated-border-color);
  --base-background-color: var(--normal-activated-background-color);
}

@media (hover:hover) {

.wrapper.variant-normal:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--normal-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--normal-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.variant-normal:active .visible-wrapper {
  border-color: var(--normal-pressed-border-color);
  background-color: var(--normal-pressed-background-color);
}

.wrapper.variant-normal:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.variant-normal:disabled .visible-wrapper {
  border-color: var(--normal-disabled-border-color);
  background-color: var(--normal-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-normal-disabled-color) !important;
}

.wrapper.variant-normal.disabled .visible-wrapper {
  border-color: var(--normal-disabled-border-color);
  background-color: var(--normal-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-normal-disabled-color) !important;
}

.wrapper.variant-normal:disabled {
  cursor: not-allowed;
}

.wrapper.variant-normal.disabled {
  cursor: not-allowed;
}

.wrapper.variant-normal {
    color: var(--on-normal-neutral-color);
}

.wrapper.variant-normal.active-color {
      color: var(--on-normal-active-color);
    }

.wrapper.variant-normal.activated .visible-wrapper {
      border-color: var(--normal-pressed-border-color);
      background-color: var(--normal-pressed-background-color);
    }

.wrapper.variant-flat {
  cursor: pointer;
}

.wrapper.variant-flat:focus {
  outline: none;
}

.wrapper.variant-flat .visible-wrapper {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.wrapper.variant-flat.activated .visible-wrapper {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

.wrapper.variant-flat:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.variant-flat:active .visible-wrapper {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

.wrapper.variant-flat:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.variant-flat:disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.variant-flat.disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.variant-flat:disabled {
  cursor: not-allowed;
}

.wrapper.variant-flat.disabled {
  cursor: not-allowed;
}

.wrapper.variant-flat {
    color: var(--on-flat-neutral-color);
}

.wrapper.variant-flat.active-color {
      color: var(--on-flat-active-color);
    }

.wrapper.variant-raised {
  cursor: pointer;
}

.wrapper.variant-raised:focus {
  outline: none;
}

.wrapper.variant-raised .visible-wrapper {
  border-color: var(--raised-enabled-border-color);
  background-color: var(--raised-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--raised-enabled-border-color);
  --base-background-color: var(--raised-enabled-background-color);
}

.wrapper.variant-raised.activated .visible-wrapper {
  border-color: var(--raised-activated-border-color);
  background-color: var(--raised-activated-background-color);
  --base-border-color: var(--raised-activated-border-color);
  --base-background-color: var(--raised-activated-background-color);
}

@media (hover:hover) {

.wrapper.variant-raised:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--raised-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--raised-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.variant-raised:active .visible-wrapper {
  border-color: var(--raised-pressed-border-color);
  background-color: var(--raised-pressed-background-color);
}

.wrapper.variant-raised:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.variant-raised:disabled .visible-wrapper {
  border-color: var(--raised-disabled-border-color);
  background-color: var(--raised-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-raised-disabled-color) !important;
}

.wrapper.variant-raised.disabled .visible-wrapper {
  border-color: var(--raised-disabled-border-color);
  background-color: var(--raised-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-raised-disabled-color) !important;
}

.wrapper.variant-raised:disabled {
  cursor: not-allowed;
}

.wrapper.variant-raised.disabled {
  cursor: not-allowed;
}

.wrapper.variant-raised {
    color: var(--on-raised-active-color);
}

.wrapper.variant-raised.active-color {
      color: var(--on-raised-active-color);
    }

.wrapper.variant-integration {
  cursor: pointer;
}

.wrapper.variant-integration:focus {
  outline: none;
}

.wrapper.variant-integration .visible-wrapper {
  border-color: var(--integration-flat-enabled-border-color);
  background-color: var(--integration-flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--integration-flat-enabled-border-color);
  --base-background-color: var(--integration-flat-enabled-background-color);
}

.wrapper.variant-integration.activated .visible-wrapper {
  border-color: var(--integration-flat-activated-border-color);
  background-color: var(--integration-flat-activated-background-color);
  --base-border-color: var(--integration-flat-activated-border-color);
  --base-background-color: var(--integration-flat-activated-background-color);
}

@media (hover:hover) {

.wrapper.variant-integration:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--integration-flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--integration-flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.variant-integration:active .visible-wrapper {
  border-color: var(--integration-flat-pressed-border-color);
  background-color: var(--integration-flat-pressed-background-color);
}

.wrapper.variant-integration:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.variant-integration:disabled .visible-wrapper {
  border-color: var(--integration-flat-disabled-border-color);
  background-color: var(--integration-flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--integration-on-flat-disabled-color) !important;
}

.wrapper.variant-integration.disabled .visible-wrapper {
  border-color: var(--integration-flat-disabled-border-color);
  background-color: var(--integration-flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--integration-on-flat-disabled-color) !important;
}

.wrapper.variant-integration:disabled {
  cursor: not-allowed;
}

.wrapper.variant-integration.disabled {
  cursor: not-allowed;
}

.wrapper.variant-integration {
    color: var(--integration-on-normal-neutral-color);
}

.wrapper.variant-integration .visible-wrapper {
      border: 0;
    }
`,ft={ATTRIBUTE:1,CHILD:2,PROPERTY:3,BOOLEAN_ATTRIBUTE:4,EVENT:5,ELEMENT:6},pt=e=>(...t)=>({_$litDirective$:e,values:t}),mt=class{constructor(e){}get _$AU(){return this._$AM._$AU}_$AT(e,t,n){this._$Ct=e,this._$AM=t,this._$Ci=n}_$AS(e,t){return this.update(e,t)}update(e,t){return this.render(...t)}},F=pt(class extends mt{constructor(e){if(super(e),e.type!==ft.ATTRIBUTE||e.name!==`class`||e.strings?.length>2)throw Error("`classMap()` can only be used in the `class` attribute and must be the only part in the attribute.")}render(e){return` `+Object.keys(e).filter(t=>e[t]).join(` `)+` `}update(e,[t]){if(this.st===void 0){this.st=new Set,e.strings!==void 0&&(this.nt=new Set(e.strings.join(` `).split(/\s/).filter(e=>e!==``)));for(let e in t)t[e]&&!this.nt?.has(e)&&this.st.add(e);return this.render(t)}let n=e.element.classList;for(let e of this.st)e in t||(n.remove(e),this.st.delete(e));for(let e in t){let r=!!t[e];r===this.st.has(e)||this.nt?.has(e)||(r?(n.add(e),this.st.add(e)):(n.remove(e),this.st.delete(e)))}return ve}}),I=e=>e??A,ht=class extends j{constructor(...e){super(...e),this.variant=`normal`,this.activated=!1,this.cornerLeft=!1,this.cornerRight=!1,this.activeColor=!1,this.wide=!1,this.disabled=!1,this.progress=void 0,this.hasLabel=!1,this.showDivider=!0,this.focusable=!0,this.ariaLabel=null}get progressSpinner(){if(this.progress===void 0)return A;if(this.progress===100)return O`<div class="progress-spinner">
        <svg
          width="40"
          height="40"
          viewBox="0 0 40 40"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <circle
            cx="20"
            cy="20"
            r="18"
            stroke="#325B9A"
            stroke-width="4"
            fill="none"
          />
        </svg>
      </div>`;let e=lt(this.progress*.95*3.6),t=20+18*Math.sin(e),n=20-18*Math.cos(e);return O`<div class="progress-spinner">
      <svg
        width="40"
        height="40"
        viewBox="0 0 40 40"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <circle
          cx="20"
          cy="20"
          r="18"
          stroke="var(--container-backdrop-color)"
          stroke-width="4"
          fill="none"
        />
        <path
          d="M18 2 A18 18 0 ${+(e>Math.PI)} 1 ${t} ${n}"
          stroke="var(--instrument-enhanced-secondary-color)"
          stroke-width="4"
          stroke-linecap="round"
        />
      </svg>
    </div>`}render(){return O`
      <button
        class=${F({wrapper:!0,[`variant-`+this.variant]:!0,activated:this.activated,"corner-left":this.cornerLeft,"corner-right":this.cornerRight,"active-color":this.activeColor,"has-label":this.hasLabel,wide:this.wide,progress:this.progress!==void 0,"hide-divider":!this.showDivider})}
        ?disabled=${this.disabled}
        aria-label=${I(this.ariaLabel??void 0)}
        tabindex=${I(this.focusable?void 0:-1)}
        part="wrapper"
      >
        ${this.progress===void 0?A:this.progressSpinner}
        <div class="visible-wrapper" part="visible-wrapper">
          <div class="icon" part="icon">
            <slot></slot>
          </div>
        </div>
        ${this.hasLabel?O`<div class="label" part="label">
                <slot name="label"></slot>
              </div>`:A}
      </button>
    `}},gt=(ht.styles=a(dt),ht);N([P({type:String})],gt.prototype,`variant`,void 0),N([P({type:Boolean})],gt.prototype,`activated`,void 0),N([P({type:Boolean})],gt.prototype,`cornerLeft`,void 0),N([P({type:Boolean})],gt.prototype,`cornerRight`,void 0),N([P({type:Boolean})],gt.prototype,`activeColor`,void 0),N([P({type:Boolean})],gt.prototype,`wide`,void 0),N([P({type:Boolean})],gt.prototype,`disabled`,void 0),N([P({type:Number})],gt.prototype,`progress`,void 0),N([P({type:Boolean})],gt.prototype,`hasLabel`,void 0),N([P({type:Boolean,attribute:!1})],gt.prototype,`showDivider`,void 0),N([P({type:Boolean,attribute:!1})],gt.prototype,`focusable`,void 0),N([P({type:String,attribute:`aria-label`})],gt.prototype,`ariaLabel`,void 0),gt=N([M(`obc-icon-button`)],gt);var _t=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M8.59009 7.41L10.0001 6L16.0001 12L10.0001 18L8.59009 16.59L13.1701 12L8.59009 7.41Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M8.59009 7.41L10.0001 6L16.0001 12L10.0001 18L8.59009 16.59L13.1701 12L8.59009 7.41Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},vt=(_t.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,_t);N([P({type:Boolean})],vt.prototype,`useCssColor`,void 0),vt=N([M(`obi-chevron-right-google`)],vt);var yt=o`* {
  -webkit-tap-highlight-color: transparent;
}

ol {
  padding: 0 var(--app-components-breadcrumbs-padding-horizontal);
  margin: 0;
  list-style-type: none;
  display: flex;
  user-select: none;
}

li {
  display: flex;
  align-items: center;
  color: var(--on-flat-neutral-color);
}

li .label-wrapper {
    color: var(--on-flat-neutral-color);
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-body-font-weight);
    font-size: var(--global-typography-ui-body-font-size);
    line-height: var(--global-typography-ui-body-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    display: flex;
    align-items: center;
    justify-content: center;
    height: var(--app-components-breadcrumb-item-touch-target-size);
    margin: 0;
    padding: 0;
    border: none;
    background: none;
  }

:is(li .label-wrapper):not(.active) {
  cursor: pointer;
}

:is(li .label-wrapper):not(.active):focus {
  outline: none;
}

:is(li .label-wrapper):not(.active) .visible-wrapper {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.activated:is(li .label-wrapper):not(.active) .visible-wrapper {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

:is(li .label-wrapper):not(.active):hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

:is(li .label-wrapper):not(.active):active .visible-wrapper {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

:is(li .label-wrapper):not(.active):focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

:is(li .label-wrapper):not(.active):disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.disabled:is(li .label-wrapper):not(.active) .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

:is(li .label-wrapper):not(.active):disabled {
  cursor: not-allowed;
}

.disabled:is(li .label-wrapper):not(.active) {
  cursor: not-allowed;
}

li .visible-wrapper {
    display: flex;
    height: var(--app-components-breadcrumb-item-visual-target-size);
    padding: 0 var(--app-components-breadcrumb-item-padding-horizontal);
    align-items: center;
    gap: var(--app-components-breadcrumb-item-label-spacing);
    border-radius: var(--app-components-breadcrumb-item-border-radius);
  }

li .active {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-body-active-font-weight);
    font-size: var(--global-typography-ui-body-active-font-size);
    line-height: var(--global-typography-ui-body-active-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    color: var(--on-flat-active-color);
  }

.divider {
  display: flex;
  align-items: center;
  justify-content: center;
  width: var(--app-components-breadcrumb-item-chevron-container-size);
}

.divider .icon {
    display: block;
    width: var(--app-components-breadcrumb-item-icon-size);
    height: var(--app-components-breadcrumb-item-icon-size);
    flex-shrink: 0;
  }
`,bt=class extends j{constructor(...e){super(...e),this.items=[],this.iconOnly=!1}render(){return O`
      <nav aria-label="Breadcrumb" class="breadcrumb">
        <ol>
          ${this.items.map((e,t)=>{let n=t===this.items.length-1;return O`
              <li>
                ${t>0?O`<span class="divider">
                        <obi-chevron-right-google class="icon">
                        </obi-chevron-right-google>
                      </span>`:A}
                ${n?O` <div class="label-wrapper active">
                        <div class="visible-wrapper">
                          ${e.icon?e.icon():A}
                          ${this.iconOnly&&!n?A:O`<span class="label">${e.label}</span>`}
                        </div>
                      </div>`:O` <button
                        role="link"
                        @click=${()=>this.handleClick(e)}
                        class="label-wrapper"
                      >
                        <div class="visible-wrapper">
                          ${e.icon?e.icon():A}
                          ${this.iconOnly&&!n?A:O`<span class="label">${e.label}</span>`}
                        </div>
                      </button>`}
              </li>
            `})}
        </ol>
      </nav>
    `}handleClick(e){this.dispatchEvent(new CustomEvent(`breadcrumb-click`,{detail:e}))}},xt=(bt.styles=a(yt),bt);N([P({attribute:!1})],xt.prototype,`items`,void 0),N([P({attribute:!1})],xt.prototype,`iconOnly`,void 0),xt=N([M(`obc-breadcrumb`)],xt);var St=o`* {
  -webkit-tap-highlight-color: transparent;
}
:host {
  width: 1px;
  height: 24px;
  flex-shrink: 0;
  border-radius: 1px;
  background: var(--border-divider-color, rgba(0, 0, 0, 0.08));
}
`,Ct=class extends j{render(){return O``}},wt=(Ct.styles=a(St),Ct);wt=N([M(`obc-divider`)],wt);var Tt=o`* {
  -webkit-tap-highlight-color: transparent;
}

:host {
  padding: 0;
}

* {
  box-sizing: border-box;
}

.clock {
  display: flex;
  align-items: center;
  color: var(--element-active-color);
  text-align: center;
  gap: var(--app-components-clock-digit-spacing-regular);
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-button-font-weight);
  font-size: var(--global-typography-ui-button-font-size);
  line-height: var(--global-typography-ui-button-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
}

.integration-bar-mode .clock {
  color: var(--integration-on-normal-active-color);
}

.blink {
  display: none;
}

@keyframes ticks {
  from {
    opacity: 1;
  }

  50% {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

.ticks {
  width: var(--app-components-clock-colon-size-regular);
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--app-components-clock-colon-spacing);
}

.ticks.animate {
    animation: ticks 1s linear infinite;
  }

.blink .ticks {
    width: 16px;
    padding: 0;
  }

.ticks .tick {
    width: 100%;
    height: 100%;
    width: calc(var(--app-components-clock-colon-size-regular) + 1px);
    height: calc(var(--app-components-clock-colon-size-regular) + 1px);
    border-radius: 100%;
    background-color: var(--element-active-color);
  }

.integration-bar-mode .ticks .tick {
  background-color: var(--integration-on-normal-active-color);
}

.blink-wrapper {
  display: none;
  height: var(--app-components-clock-touch-target);
  width: 24px;
  align-items: center;
  justify-content: center;
}

.timezone {
  color: var(--element-neutral-color);
  text-align: center;

  font-family: var(--global-typography-font-family);

  font-weight: var(--global-typography-ui-body-font-weight);

  font-size: var(--global-typography-ui-body-font-size);

  line-height: var(--global-typography-ui-body-line-height);

  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
}

.integration-bar-mode .timezone {
  color: var(--integration-on-normal-active-color);
}

.date {
  text-align: center;
  color: var(--element-active-color);
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-body-font-weight);
  font-size: var(--global-typography-ui-body-font-size);
  line-height: var(--global-typography-ui-body-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
}

.integration-bar-mode .date {
  color: var(--integration-on-normal-active-color);
}

.wrapper {
  user-select: none;
  display: flex;
  align-items: center;
  padding: 0 var(--app-components-clock-margin-horizontal);
  appearance: none;
  border: none;
  background: none;
  height: var(--app-components-clock-touch-target);
}

.wrapper:not(.no-click) {
  cursor: pointer;
}

.wrapper:not(.no-click):focus {
  outline: none;
}

.wrapper:not(.no-click) .visible-wrapper {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.wrapper.activated:not(.no-click) .visible-wrapper {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

.wrapper:not(.no-click):hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper:not(.no-click):active .visible-wrapper {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

.wrapper:not(.no-click):focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper:not(.no-click):disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.disabled:not(.no-click) .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper:not(.no-click):disabled {
  cursor: not-allowed;
}

.wrapper.disabled:not(.no-click) {
  cursor: not-allowed;
}

.wrapper.selected {
  cursor: pointer;
}

.wrapper.selected:focus {
  outline: none;
}

.wrapper.selected .visible-wrapper {
  border-color: var(--amplified-enabled-border-color);
  background-color: var(--amplified-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--amplified-enabled-border-color);
  --base-background-color: var(--amplified-enabled-background-color);
}

.wrapper.selected.activated .visible-wrapper {
  border-color: var(--amplified-activated-border-color);
  background-color: var(--amplified-activated-background-color);
  --base-border-color: var(--amplified-activated-border-color);
  --base-background-color: var(--amplified-activated-background-color);
}

@media (hover:hover) {

.wrapper.selected:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--amplified-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--amplified-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.selected:active .visible-wrapper {
  border-color: var(--amplified-pressed-border-color);
  background-color: var(--amplified-pressed-background-color);
}

.wrapper.selected:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.selected:disabled .visible-wrapper {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

.wrapper.selected.disabled .visible-wrapper {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

.wrapper.selected:disabled {
  cursor: not-allowed;
}

.wrapper.selected.disabled {
  cursor: not-allowed;
}

.wrapper.double {
    height: var(--app-components-clock-touch-target-size-double);
  }

.visible-wrapper {
  display: flex;
  align-items: center;
  border-radius: var(--app-components-clock-border-radius);
  padding: 0 var(--app-components-clock-padding-horizontal);
  height: var(--app-components-clock-visual-target);
  gap: var(--app-components-clock-label-spacing);
  border: 1px solid transparent;
}

.double .visible-wrapper {
    flex-direction: column;
    height: 48px;
    gap: 0;
  }

.divider {
  width: 1px;
  height: 16px;
  background-color: var(--border-divider-color);
}

.integration-bar-mode .divider {
  background-color: var(--integration-border-outline);
}

.double .divider {
  display: none;
}

.row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--app-components-clock-label-spacing);
}
`,Et=Symbol.for(``),Dt=e=>{if(e?.r===Et)return e?._$litStatic$},Ot=(e,...t)=>({_$litStatic$:t.reduce((t,n,r)=>t+(e=>{if(e._$litStatic$!==void 0)return e._$litStatic$;throw Error(`Value passed to 'literal' function must be a 'literal' result: ${e}. Use 'unsafeStatic' to pass non-literal values, but\n            take care to ensure page security.`)})(n)+e[r+1],e[0]),r:Et}),kt=new Map,L=(e=>(t,...n)=>{let r=n.length,i,a,o=[],s=[],c,l=0,u=!1;for(;l<r;){for(c=t[l];l<r&&(a=n[l],(i=Dt(a))!==void 0);)c+=i+t[++l],u=!0;l!==r&&s.push(a),o.push(c),l++}if(l===r&&o.push(t[r]),u){let e=o.join(`$$lit$$`);(t=kt.get(e))===void 0&&(o.raw=o,kt.set(e,t=o)),n=s}return e(t,...n)})(O),At=class extends j{constructor(...e){super(...e),this.showSeconds=!1,this.showDate=!1,this.showTimezone=!1,this.timeZoneOffsetHours=0,this.isClickable=!0,this.showYear=!1,this.showWeekday=!1,this.locale=`en-GB`,this.hour12=!1,this.selected=!1,this.double=!1,this.activated=!1,this.integrationBarMode=!1,this.blinkOnlyBreakpointPx=0}get timezoneString(){return this.timeZoneOffsetHours===0?`UTC`:this.timeZoneOffsetHours>0?`UTC+${this.timeZoneOffsetHours}`:`UTC-${-this.timeZoneOffsetHours}`}_dateString(e){let t={month:`short`,day:`numeric`,weekday:this.showWeekday?`short`:void 0,year:this.showYear?`numeric`:void 0,timeZone:`UTC`};return e.toLocaleDateString(this.locale,t).replace(/,/g,``).replace(/\./g,``)}_ampm(e){return this.hour12?e<12?` AM`:` PM`:``}render(){let e=new Date(this.date);e.setUTCHours(e.getUTCHours()+this.timeZoneOffsetHours);let t=e.getUTCHours(),n=e.getUTCMinutes(),r=this.hour12?t%12:t,i=r<10?`0${r}`:`${r}`,a=n<10?`0${n}`:`${n}`,o=e.getUTCSeconds(),s=o<10?`0${o}`:`${o}`,c=this._ampm(t),l=this._dateString(e),u=this.isClickable?Ot`button`:Ot`div`,d=L`<div class="ticks ${this.showSeconds?``:`animate`}">
      <span class="tick"></span><span class="tick"></span>
    </div>`,f=`@media (max-width: ${this.blinkOnlyBreakpointPx}px )`,p=L`<div class="clock">
        ${i}${d}${a}${this.showSeconds?L`${d}${s}`:``}${c}
      </div>

      ${this.showTimezone?L`<div class="timezone">${this.timezoneString}</div>`:null}`;return L`
      <style>
        ${f} {
          .wrapper {
            display: none !important;
          }
          .blink-wrapper {
            display: flex !important;
          }
        }
      </style>
      <${u} 
        class=${F({wrapper:!0,"no-click":!this.isClickable,selected:this.selected,double:this.double,"integration-bar-mode":this.integrationBarMode,activated:this.activated})}>
        <div class="visible-wrapper">
          ${this.double?L`<div class="row">${p}</div>`:p}
        ${this.showDate?L` <div class="divider"></div>
                <div class="date">${l}</div>`:A}
        ${this.double?L`</div>`:A}
        </div>
      </${u}>
      <div class=${F({"blink-wrapper":!0,clock:!0,blink:!0,"integration-bar-mode":this.integrationBarMode})}>
        <div class="ticks animate"><div class="tick"></div><div class="tick"></div></div>
      </div>
    `}},jt=(At.styles=a(Tt),At);N([P({type:String})],jt.prototype,`date`,void 0),N([P({type:Boolean})],jt.prototype,`showSeconds`,void 0),N([P({type:Boolean})],jt.prototype,`showDate`,void 0),N([P({type:Boolean})],jt.prototype,`showTimezone`,void 0),N([P({type:Number})],jt.prototype,`timeZoneOffsetHours`,void 0),N([P({type:Boolean,attribute:!1})],jt.prototype,`isClickable`,void 0),N([P({type:Boolean})],jt.prototype,`showYear`,void 0),N([P({type:Boolean})],jt.prototype,`showWeekday`,void 0),N([P({type:String})],jt.prototype,`locale`,void 0),N([P({type:Boolean})],jt.prototype,`hour12`,void 0),N([P({type:Boolean})],jt.prototype,`selected`,void 0),N([P({type:Boolean})],jt.prototype,`double`,void 0),N([P({type:Boolean})],jt.prototype,`activated`,void 0),N([P({type:Boolean})],jt.prototype,`integrationBarMode`,void 0),N([P({type:Number})],jt.prototype,`blinkOnlyBreakpointPx`,void 0),jt=N([M(`obc-clock`)],jt);var Mt=o`* {
  -webkit-tap-highlight-color: transparent;
}

* {
  box-sizing: border-box;
}

.wrapper {
  height: var(--app-components-topbar-touch-target-size);
  padding: 0px var(--app-components-topbar-margin-global);
  user-select: none;

  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.wrapper:not(.inactive) {
    background: var(--container-global-color, #fcfcfc);
    box-shadow: var(--shadow-flat);
  }

.wrapper.tall {
    height: var(--app-components-topbar-touch-target-tall);
  }

.wrapper.inactive {
    padding-left: calc(
      var(--app-components-topbar-margin-global) +
        var(--app-components-topbar-padding-left-small)
    ); /* no menu button: inset the title instead */
  }

/* ---- One flex line ----
   Flattened because a squeeze must reach the texts, not a group: a shrinkable
   left group collapses under an unshrinkable alert and covers the menu button. */

.group {
  display: contents;
}

.settings .group.left > * {
    margin-right: 0;
    margin-left: 0;
  }

.group.left .title {
    padding-right: var(--app-components-topbar-label-spacing);
  }

.group.left .menu-button {
    margin-right: 0;
    margin-left: 0;
  }

.wide:is(.group.left .menu-button) {
      margin-left: 8px;
      margin-right: 8px;
    }

.group .app-icon {
    padding-right: var(--app-components-topbar-label-spacing);
    width: var(--app-components-topbar-icon-size);
    height: var(--app-components-topbar-icon-size);
    box-sizing: content-box;
    color: var(--element-neutral-color);
  }

/* Controls never shrink: a squeeze reaches the texts, then overflows the end */
.menu-button,
.app-icon,
.left-more-button,
.dimming-button,
.user-button,
.apps-button,
::slotted([slot="command-button"]),
::slotted([slot="clock"]) {
  flex-shrink: 0;
}

.alert-container {
  display: flex;
  flex: 1 1 0; /* zero basis: fills what the texts leave, holds its min-content in a squeeze */
  gap: var(--app-components-topbar-label-spacing);
  align-items: center;
  justify-content: right;
}

/* ---- Text gives way first ---- */

.title,
.page-name {
  overflow: hidden;
  color: var(--element-active-color, #1a1a1a);
}

.title {
  flex-shrink: 3; /* the app title gives way before the page name */
  min-width: 2em; /* room for "A…": narrower boxes paint a clipped glyph instead */
  white-space: nowrap;
  text-overflow: ellipsis;
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-body-font-weight);
  font-size: var(--global-typography-ui-body-font-size);
  line-height: var(--global-typography-ui-body-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
}

.page-name {
  min-width: 0; /* shrink below the longest word instead of pushing buttons out */
  display: -webkit-box; /* two lines, then an ellipsis */
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-body-active-font-weight);
  font-size: var(--global-typography-ui-body-active-font-size);
  line-height: var(--global-typography-ui-body-active-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
}

.left-more-button {
  display: none;
}

.divider {
  width: 1px;
  height: var(--ui-components-divider-height-small);
  background: var(--border-divider-color);
}
`,Nt=`lit-localize-status`,Pt=e=>typeof e!=`string`&&`strTag`in e,Ft=(e,t,n)=>{let r=e[0];for(let i=1;i<e.length;i++)r+=t[n?n[i-1]:i-1],r+=e[i];return r},R=(e=>Pt(e)?Ft(e.strings,e.values):e),It=class{constructor(e){this.__litLocalizeEventHandler=e=>{e.detail.status===`ready`&&this.host.requestUpdate()},this.host=e}hostConnected(){window.addEventListener(Nt,this.__litLocalizeEventHandler)}hostDisconnected(){window.removeEventListener(Nt,this.__litLocalizeEventHandler)}},Lt=e=>e.addController(new It(e)),Rt=()=>(e,t)=>(e.addInitializer(Lt),e),zt=class{constructor(){this.settled=!1,this.promise=new Promise((e,t)=>{this._resolve=e,this._reject=t})}resolve(e){this.settled=!0,this._resolve(e)}reject(e){this.settled=!0,this._reject(e)}},Bt=[];for(let e=0;e<256;e++)Bt[e]=(e>>4&15).toString(16)+(e&15).toString(16);new zt().resolve();var Vt=class extends j{constructor(...e){super(...e),this.appTitle=`App`,this.pageName=`Page`,this.menuButtonIcon=`menu`,this.menuButtonActivated=!1,this.dimmingButtonActivated=!1,this.appsButtonActivated=!1,this.leftMoreButtonActivated=!1,this.userButtonActivated=!1,this.userButtonDisabled=!1,this.tall=!1,this.wideMenuButton=!1,this.showAppsButton=!1,this.showDimmingButton=!1,this.showUserButton=!1,this.showClock=!1,this.showDate=!1,this.showAppIcon=!1,this.inactive=!1,this.appButtonBreakpointPx=500,this.dimmingButtonBreakpointPx=500,this.appTitleBreakpointPx=500,this.userButtonBreakpointPx=500,this.appIconBreakpointPx=500,this.settings=!1,this.breadcrumbItems=[],this.leftButtonEvent=null,this.leftButtonTimeout=null,this.isLeftButtonDown=!1,this.isEmergencyBrightness=!1}dimmingButtonClicked(){this.dispatchEvent(new CustomEvent(`dimming-button-clicked`))}appsButtonClicked(){this.dispatchEvent(new CustomEvent(`apps-button-clicked`))}leftMoreButtonClicked(){this.dispatchEvent(new CustomEvent(`left-more-button-clicked`))}userButtonClicked(){this.dispatchEvent(new CustomEvent(`user-button-clicked`))}leftButtonDown(e){this.leftButtonEvent=e,this.isLeftButtonDown=!0,this.leftButtonTimeout=setTimeout(()=>{this.leftButtonEvent=null,this.dispatchEvent(new CustomEvent(`emergency-brightness-start`)),this.isEmergencyBrightness=!0},500)}leftButtonUp(){this.leftButtonTimeout&&=(clearTimeout(this.leftButtonTimeout),null),this.isEmergencyBrightness&&=(this.dispatchEvent(new CustomEvent(`emergency-brightness-stop`)),!1),this.isLeftButtonDown=!1}leftButtonActivate(e,t){if(e.detail===0){this.dispatchEvent(new CustomEvent(t));return}this.leftButtonEvent&&=(this.dispatchEvent(this.leftButtonEvent),null)}leftButtonLeave(){this.isLeftButtonDown&&=(this.leftButtonTimeout&&=(clearInterval(this.leftButtonTimeout),null),this.isEmergencyBrightness&&=(this.dispatchEvent(new CustomEvent(`emergency-brightness-stop`)),!1),!1)}render(){let e=[];return this.settings?(e.push(O`<div class="menu-button">
          <obc-icon-button
            variant="flat"
            aria-label=${R(`Close`)}
            @pointerdown=${()=>this.leftButtonDown(new CustomEvent(`close`))}
            @pointerup=${()=>this.leftButtonUp()}
            @pointerleave=${()=>this.leftButtonLeave()}
            @click=${e=>this.leftButtonActivate(e,`close`)}
          >
            <obi-close-google></obi-close-google>
          </obc-icon-button>
        </div>`),e.push(O`<obc-icon-button
          variant="flat"
          aria-label=${R(`Back`)}
          @click=${()=>this.dispatchEvent(new CustomEvent(`back`))}
        >
          <obi-arrow-left-google></obi-arrow-left-google>
        </obc-icon-button>`),e.push(O`<div class="title">${this.appTitle}</div>`),e.push(O`<obc-breadcrumb
          .items=${this.breadcrumbItems}
          @breadcrumb-click=${e=>this.dispatchEvent(new CustomEvent(`breadcrumb-click`,{detail:e.detail}))}
        ></obc-breadcrumb>`)):(this.inactive||e.push(O`<div class="menu-button ${this.wideMenuButton?`wide`:null}">
            <obc-icon-button
              variant="flat"
              aria-label=${this.menuButtonIcon===`menu`?R(`Menu`):R(`Home`)}
              @pointerdown=${()=>this.leftButtonDown(new CustomEvent(`menu-button-clicked`))}
              @pointerup=${()=>this.leftButtonUp()}
              @pointerleave=${()=>this.leftButtonLeave()}
              @click=${e=>this.leftButtonActivate(e,`menu-button-clicked`)}
              ?activated=${this.menuButtonActivated}
            >
              ${this.menuButtonIcon===`menu`?O`<obi-menu-iec></obi-menu-iec>`:O`<obi-home></obi-home>`}
            </obc-icon-button>
          </div>`),this.showAppIcon&&e.push(O`<div class="app-icon"><slot name="app-icon"></slot></div>`),e.push(O`<div class="title">${this.appTitle}</div>`),e.push(O`<div class="page-name">${this.pageName}</div>`),e.push(O`<slot name="command-button"></slot>`)),O`
      <style>
        @media (max-width: ${Math.max(this.appButtonBreakpointPx,this.dimmingButtonBreakpointPx)}px) {
          .left-more-button {
            display: revert !important;
          }

          .group.left > * {
            margin-right: 4px;
            margin-left: 4px;
          }
        }

        @media (max-width: ${this.appButtonBreakpointPx}px) {
          .apps-button {
            display: none;
          }
        }

        @media (max-width: ${this.dimmingButtonBreakpointPx}px) {
          .dimming-button {
            display: none;
          }
        }

        @media (max-width: ${this.appTitleBreakpointPx}px) {
          .title {
            display: none !important; /* the stylesheet's display wins over this inline rule otherwise */
          }
        }

        @media (max-width: ${this.userButtonBreakpointPx}px) {
          .user-button {
            display: none;
          }
        }

        @media (max-width: ${this.appIconBreakpointPx}px) {
          .app-icon {
            display: none;
          }
        }
      </style>
      <nav
        class=${F({wrapper:!0,inactive:this.inactive,settings:this.settings,tall:this.tall})}
      >
        <div class="left group">${e}</div>
        <div class="right group">
          <div class="alert-container">
            <slot name="alerts"></slot>
          </div>
          ${this.showDimmingButton&&!this.inactive?O`<obc-icon-button
                  class="dimming-button"
                  part="dimming-button"
                  variant="flat"
                  aria-label=${R(`Dimming`)}
                  @click=${this.dimmingButtonClicked}
                  ?activated=${this.dimmingButtonActivated}
                >
                  <obi-palette-day-night-iec></obi-palette-day-night-iec>
                </obc-icon-button>`:null}
          ${this.showUserButton&&!this.inactive?O`<obc-icon-button
                  class="user-button"
                  variant="flat"
                  part="user-button"
                  aria-label=${R(`User`)}
                  @click=${this.userButtonClicked}
                  ?activated=${this.userButtonActivated}
                  ?disabled=${this.userButtonDisabled}
                >
                  <obi-user></obi-user>
                </obc-icon-button>`:null}
          ${this.showAppsButton&&!this.inactive?O`<obc-icon-button
                  class="apps-button"
                  variant="flat"
                  part="apps-button"
                  aria-label=${R(`Apps`)}
                  @click=${this.appsButtonClicked}
                  ?activated=${this.appsButtonActivated}
                >
                  <obi-applications></obi-applications>
                </obc-icon-button>`:null}
          ${this.showClock?O`<slot name="clock"></slot>`:null}
          ${this.inactive?null:O`<obc-icon-button
                  class="left-more-button"
                  part="left-more-button"
                  variant="flat"
                  aria-label=${R(`More`)}
                  @click=${this.leftMoreButtonClicked}
                  ?activated=${this.leftMoreButtonActivated}
                >
                  <obi-more-vertical-google></obi-more-vertical-google>
                </obc-icon-button>`}
        </div>
      </nav>
    `}},z=(Vt.styles=a(Mt),Vt);N([P({type:String})],z.prototype,`appTitle`,void 0),N([P({type:String})],z.prototype,`pageName`,void 0),N([P({type:String})],z.prototype,`menuButtonIcon`,void 0),N([P({type:Boolean})],z.prototype,`menuButtonActivated`,void 0),N([P({type:Boolean})],z.prototype,`dimmingButtonActivated`,void 0),N([P({type:Boolean})],z.prototype,`appsButtonActivated`,void 0),N([P({type:Boolean})],z.prototype,`leftMoreButtonActivated`,void 0),N([P({type:Boolean})],z.prototype,`userButtonActivated`,void 0),N([P({type:Boolean})],z.prototype,`userButtonDisabled`,void 0),N([P({type:Boolean})],z.prototype,`tall`,void 0),N([P({type:Boolean})],z.prototype,`wideMenuButton`,void 0),N([P({type:Boolean})],z.prototype,`showAppsButton`,void 0),N([P({type:Boolean})],z.prototype,`showDimmingButton`,void 0),N([P({type:Boolean})],z.prototype,`showUserButton`,void 0),N([P({type:Boolean})],z.prototype,`showClock`,void 0),N([P({type:Boolean})],z.prototype,`showDate`,void 0),N([P({type:Boolean})],z.prototype,`showAppIcon`,void 0),N([P({type:Boolean})],z.prototype,`inactive`,void 0),N([P({type:Number})],z.prototype,`appButtonBreakpointPx`,void 0),N([P({type:Number})],z.prototype,`dimmingButtonBreakpointPx`,void 0),N([P({type:Number})],z.prototype,`appTitleBreakpointPx`,void 0),N([P({type:Number})],z.prototype,`userButtonBreakpointPx`,void 0),N([P({type:Number})],z.prototype,`appIconBreakpointPx`,void 0),N([P({type:Boolean})],z.prototype,`settings`,void 0),N([P({type:Array})],z.prototype,`breadcrumbItems`,void 0),z=N([M(`obc-top-bar`)],z);var Ht=class{constructor(e){this.host=e,this.installed=!1,this.dismissed=!1,this.toggling=!1,this.onBeforeToggle=e=>{if(this.host.softDismiss){if(this.toggling=!0,setTimeout(()=>{this.toggling=!1},0),e.newState===`open`){this.ensureCover(),this.host.open=!0;return}this.dismissed=this.host.open,this.host.open=!1}},this.onToggle=e=>{this.host.softDismiss&&(this.toggling=!1,e.newState===`closed`&&this.dismissed&&(this.dismissed=!1,this.host.dispatchEvent(new CustomEvent(`close`))))},e.addController(this)}hostConnected(){this.host.addEventListener(`beforetoggle`,this.onBeforeToggle),this.host.addEventListener(`toggle`,this.onToggle),this.host.hasUpdated&&this.sync()}hostUpdated(){this.sync()}hostDisconnected(){this.host.removeEventListener(`beforetoggle`,this.onBeforeToggle),this.host.removeEventListener(`toggle`,this.onToggle),this.toggling=!1}sync(){let e=this.host;if(!e.softDismiss){this.installed&&(e.removeAttribute(`popover`),this.installed=!1,this.backdrop?.remove(),this.backdrop=void 0);return}if(this.installed||(e.setAttribute(`popover`,`auto`),this.installed=!0,this.ensureCover()),!e.isConnected||this.toggling)return;let t=e.matches(`:popover-open`);e.open&&!t?e.showPopover():!e.open&&t&&e.hidePopover()}ensureCover(){let e=this.host.shadowRoot;if(!e||this.backdrop)return;let t=document.createElement(`div`);t.setAttribute(`part`,`backdrop`),t.style.cssText=`position:fixed;top:var(--topbar-height,var(--app-components-topbar-touch-target-size,0px));right:0;bottom:0;left:0;z-index:-1;margin:0;padding:0;border:0;background:transparent`,t.addEventListener(`click`,()=>this.host.hidePopover()),e.append(t),this.backdrop=t}};function Ut(e,t){return e.composedPath().find(e=>t.includes(e))}var Wt=class{constructor(e,t){this.adapter=e,this.options=t}navigable(){return this.adapter.items().filter(e=>!(this.adapter.isDisabled?.(e)??!1))}refresh(){let e=this.navigable();if(e.length===0){this.activeItem=void 0,this.adapter.items().forEach(e=>this.adapter.setFocusable(e,!1));return}let t=this.adapter.preferred?.(),n=(this.activeItem&&e.includes(this.activeItem)?this.activeItem:void 0)??(t&&e.includes(t)?t:void 0)??e[0];this.setActive(n,!1)}setActive(e,t){this.activeItem=e;for(let t of this.adapter.items())this.adapter.setFocusable(t,t===e);t&&(this.adapter.focusItem??(e=>e.focus()))(e)}handleFocusin(e){let t=Ut(e,this.navigable());t&&t!==this.activeItem&&this.setActive(t,!1)}handleKeydown(e){if(e.altKey||e.ctrlKey||e.metaKey)return!1;let t=this.navigable(),n=Ut(e,t);if(!n)return!1;let r=this.options.orientation!==`vertical`,i=this.options.orientation!==`horizontal`,a;switch(e.key){case`ArrowRight`:if(!r)return!1;a=1;break;case`ArrowLeft`:if(!r)return!1;a=-1;break;case`ArrowDown`:if(!i)return!1;a=1;break;case`ArrowUp`:if(!i)return!1;a=-1;break;case`Home`:return this.setActive(t[0],!0),!0;case`End`:return this.setActive(t[t.length-1],!0),!0;default:return!1}let o=t.indexOf(n)+a,s=this.options.wrap===!1?st(o,0,t.length-1):(o+t.length)%t.length;return this.setActive(t[s],!0),!0}},Gt=class{constructor(e){this.adapter=e}isDisabled(e){return this.adapter.isDisabled?.(e)??!1}visibleRows(){let e=[],t=n=>{for(let r of n)e.push(r),this.adapter.isGroup(r)&&this.adapter.isExpanded(r)&&t(this.adapter.childRows(r))};return t(this.adapter.getRows()),e}navigableRows(){return this.visibleRows().filter(e=>!this.isDisabled(e))}parentRow(e){let t,n=(r,i)=>{for(let a of r){if(a===e){t=i;return}if(this.adapter.isGroup(a)&&(n(this.adapter.childRows(a),a),t!==void 0))return}};return n(this.adapter.getRows(),void 0),t}refresh(){let e=this.navigableRows();if(e.length===0){this.activeRow=void 0;return}let t;if(this.activeRow&&e.includes(this.activeRow))t=this.activeRow;else if(this.activeRow){let n=this.parentRow(this.activeRow);for(;n&&!e.includes(n);)n=this.parentRow(n);t=n??e[0]}else t=e[0];this.setActiveRow(t,!1)}setActiveRow(e,t){this.activeRow=e;for(let t of this.visibleRows()){let n=this.adapter.innerItem(t);n&&(n.focusable=t===e)}if(!t)return;let n=this.adapter.innerItem(e);n?n.focus():queueMicrotask(()=>this.adapter.innerItem(e)?.focus())}rowFromEvent(e){return Ut(e,this.allRows())}allRows(){let e=[],t=[...this.adapter.getRows()];for(;t.length;){let n=t.pop();e.push(n),this.adapter.isGroup(n)&&t.push(...this.adapter.childRows(n))}return e}handleKeydown(e){let t=this.rowFromEvent(e);if(!t)return!1;switch(e.key){case`ArrowDown`:return this.moveByOffset(t,1),!0;case`ArrowUp`:return this.moveByOffset(t,-1),!0;case`ArrowRight`:return this.onArrowRight(t),!0;case`ArrowLeft`:return this.onArrowLeft(t),!0;case`Home`:return this.moveToEdge(!0),!0;case`End`:return this.moveToEdge(!1),!0;default:return!1}}moveByOffset(e,t){let n=this.navigableRows(),r=n.indexOf(e);if(r===-1)return;let i=n[r+t];i&&this.setActiveRow(i,!0)}moveToEdge(e){let t=this.navigableRows();t.length!==0&&this.setActiveRow(e?t[0]:t[t.length-1],!0)}onArrowRight(e){if(!this.adapter.isGroup(e))return;if(!this.adapter.isExpanded(e)){this.adapter.setExpanded(e,!0),this.refresh();return}let t=this.adapter.childRows(e).find(e=>!this.isDisabled(e));t&&this.setActiveRow(t,!0)}onArrowLeft(e){if(this.adapter.isGroup(e)&&this.adapter.isExpanded(e)){this.adapter.setExpanded(e,!1),this.refresh();return}let t=this.parentRow(e);t&&this.setActiveRow(t,!0)}},Kt=o`* {
    -webkit-tap-highlight-color: transparent;
}

:host([popover]) {
    /* The browser pins a popover to all four edges and lets the automatic
       margins centre it. Unpinning drops it back where it would normally sit,
       for the consumer to position from. */
    inset: auto;
    margin: 0;

    padding: 0;
    border: none;
    background: none;
    color: inherit;

    /* The menus scroll their own content. */
    overflow: visible;

    /* The browser shrink-wraps a popover to its contents. */
    width: auto;
    height: auto;
  }

.wrapper {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  height: 100%;
  width: 320px;
  background: var(--container-global-color, #fcfcfc);
  box-shadow: var(--shadow-flat);
}

.wrapper nav {
    padding: var(--app-components-navigation-menu-margin-vertical)
      var(--app-components-navigation-menu-footer-margin-horizontal);
  }

.wrapper.icon-only,.wrapper.compact {
    width: fit-content;
  }

:is(.wrapper.icon-only,.wrapper.compact) nav.main {
      padding: var(--app-components-navigation-menu-margin-vertical) 0px;
    }

:is(.wrapper.icon-only,.wrapper.compact) .footer nav {
      padding: 0;
    }

.wrapper.icon-only-large {
    width: fit-content;
  }

.wrapper .main {
    flex: 1 1 auto;
    min-height: 0;
    overflow-y: auto;
  }

.wrapper .footer {
    display: flex;
    flex-direction: column;
    border-top: 1px solid var(--border-outline-color);
    flex: 0 0 auto;
  }

.wrapper.small-screen .footer nav ol {
    display: flex;
    justify-content: space-around;
    width: 100%;
  }

.full .footer.has-footer nav {
  border-bottom: 1px solid var(--border-outline-color);
}

.full .logo {
  height: 96px;
  width: 100%;
}

.icon-only-large .footer nav {
  padding-bottom: 0;
}

.icon-only-large .logo {
  padding: var(--app-components-navigation-menu-margin-vertical)
    var(--app-components-navigation-menu-footer-margin-horizontal);
  padding-top: 0;
  height: calc(
    var(--menu-navigation-components-navigation-item-touch-target-size) +
      var(--app-components-navigation-menu-margin-vertical)
  );
}

.icon-only .logo {
  height: var(--menu-navigation-components-navigation-item-touch-target-size);
}

.compact .logo {
  height: var(
    --menu-navigation-components-navigation-item-touch-target-size-large
  );
}

.logo {
  transition: height 200ms;
}

.wrapper:not(.small-screen) ::slotted([slot="logo"]) {
  width: 100%;
}

ol {
  list-style: none;
  margin: 0;
  padding: 0;
}
`,B=function(e){return e.Alarm=`alarm`,e.Warning=`warning`,e.Caution=`caution`,e.LevelCritical=`level-critical`,e.LevelHigh=`level-high`,e.LevelMedium=`level-medium`,e.LevelLow=`level-low`,e.LevelDiagnostic=`level-diagnostic`,e}({}),V=function(e){return e.Default=`default`,e.Fast=`fast`,e.Slow=`slow`,e.VerySlow=`very-slow`,e.Fixed=`fixed`,e}({}),qt=[`level-critical`,`alarm`,`level-high`,`warning`,`level-medium`,`caution`,`level-low`,`level-diagnostic`],Jt=function(e){return e.Alarm=`obi-alarm-badge`,e.Warning=`obi-warning-badge`,e.Caution=`obi-caution-badge`,e.Critical=`obi-critical-badge`,e.Diagnostic=`obi-diagnostic-badge`,e}({}),Yt=function(e){return e.Active=`active`,e.Rectified=`rectified`,e}({});function Xt(e,t,n=`active`){if(e!==V.Default)return e;if(t===B.Caution||t===B.LevelDiagnostic)return V.Fixed;if(n===`rectified`)return V.VerySlow;switch(t){case B.LevelCritical:case B.Alarm:case B.LevelHigh:return V.Fast;case B.Warning:case B.LevelMedium:return V.Slow;case B.LevelLow:return V.VerySlow;default:return V.Fixed}}function Zt(e){switch(e){case B.LevelCritical:return`obi-critical-badge`;case B.Warning:case B.LevelMedium:return`obi-warning-badge`;case B.Caution:case B.LevelLow:return`obi-caution-badge`;case B.LevelDiagnostic:return`obi-diagnostic-badge`;case B.Alarm:case B.LevelHigh:default:return`obi-alarm-badge`}}var Qt={[B.Alarm]:`countAlarm`,[B.Warning]:`countWarning`,[B.Caution]:`countCaution`,[B.LevelCritical]:`countLevelCritical`,[B.LevelHigh]:`countLevelHigh`,[B.LevelMedium]:`countLevelMedium`,[B.LevelLow]:`countLevelLow`,[B.LevelDiagnostic]:`countLevelDiagnostic`};function $t(e,t=!1){let n=qt.map(t=>({type:t,count:e[Qt[t]]??0})).filter(e=>e.count>0);if(!t||n.length===0)return n;let r=n.reduce((e,t)=>e+t.count,0);return[{type:n[0].type,count:r}]}B.Alarm,B.Warning,B.Caution,B.LevelCritical,B.LevelHigh,B.LevelMedium,B.LevelLow,B.LevelDiagnostic;var en=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M13 2H11V5H8V7H11V10H13V7H16V5H13V2Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M13 2H11V5H8V7H11V10H13V7H16V5H13V2Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},tn=(en.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,en);N([P({type:Boolean})],tn.prototype,`useCssColor`,void 0),tn=N([M(`obi-alert-header-aggregated-iec`)],tn);var nn=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M13 2H11V5H8V7H11V10H13V7H16V5H13V2Z" fill="currentColor"/>
<path d="M19 8H17V11H14V13H17V16H19V13H22V11H19V8Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M13 2H11V5H8V7H11V10H13V7H16V5H13V2Z" style="fill: var(--element-active-color)"/>
<path d="M19 8H17V11H14V13H17V16H19V13H22V11H19V8Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},rn=(nn.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,nn);N([P({type:Boolean})],rn.prototype,`useCssColor`,void 0),rn=N([M(`obi-alert-header-group-iec`)],rn);var an=o`* {
  -webkit-tap-highlight-color: transparent;
}

* {
  box-sizing: border-box;
}

:host {
  display: block;
}

.wrapper {
  display: flex;
  align-items: center;
  width: 100%;
  height: var(--menu-navigation-components-tree-navigation-item-touch-target);
  user-select: none;
}

.wrapper:focus-visible {
    outline-offset: -2px;
  }

.wrapper {
  cursor: pointer;
}

.wrapper:focus {
  outline: none;
}

.wrapper .visible-wrapper {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.wrapper.activated .visible-wrapper {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

.wrapper:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper:active .visible-wrapper {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

.wrapper:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper:disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper:disabled {
  cursor: not-allowed;
}

.wrapper.disabled {
  cursor: not-allowed;
}

.wrapper {
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-body-font-weight);
  font-size: var(--global-typography-ui-body-font-size);
  line-height: var(--global-typography-ui-body-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  color: var(--on-flat-active-color);
}

.wrapper .visible-wrapper {
    display: flex;
    align-items: center;
    width: 100%;
    height: 100%;
    border-radius: var(--global-border-radius-border-radius-base);
    padding: 0
      var(--menu-navigation-components-tree-navigation-item-padding-horizontal);
  }

/*
   * A checked row is not re-selectable, so it stays on the amplified enabled
   * style with no hover/pressed feedback.
   */

.wrapper.checked {
  cursor: pointer;
}

.wrapper.checked:focus {
  outline: none;
}

.wrapper.checked .visible-wrapper {
  border-color: var(--amplified-enabled-border-color);
  background-color: var(--amplified-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--amplified-enabled-border-color);
  --base-background-color: var(--amplified-enabled-background-color);
}

.wrapper.checked.activated .visible-wrapper {
  border-color: var(--amplified-activated-border-color);
  background-color: var(--amplified-activated-background-color);
  --base-border-color: var(--amplified-activated-border-color);
  --base-background-color: var(--amplified-activated-background-color);
}

@media (hover:hover) {

.wrapper.checked:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--amplified-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--amplified-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.checked:active .visible-wrapper {
  border-color: var(--amplified-pressed-border-color);
  background-color: var(--amplified-pressed-background-color);
}

.wrapper.checked:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.checked:disabled .visible-wrapper {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

.wrapper.checked.disabled .visible-wrapper {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

.wrapper.checked:disabled {
  cursor: not-allowed;
}

.wrapper.checked.disabled {
  cursor: not-allowed;
}

.wrapper.checked {
    cursor: default;
}

.wrapper.checked .visible-wrapper,.wrapper.checked:hover .visible-wrapper,.wrapper.checked:active .visible-wrapper {
      background-color: var(--amplified-enabled-background-color);
      border-color: var(--amplified-enabled-border-color);
    }

.wrapper.checked .label {
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-body-active-font-weight);
      font-size: var(--global-typography-ui-body-active-font-size);
      line-height: var(--global-typography-ui-body-active-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
      color: var(--on-flat-active-color);
    }

.wrapper.checked .leading-icon {
      color: var(--on-amplified-active-color);
    }

/* Guide lines are tree structure, not row state, so they do not dim here. */

.wrapper.disabled {
    color: var(--on-flat-disabled-color);
  }

.wrapper.disabled .leading-icon {
      color: var(--on-flat-disabled-color);
    }

.tree-node-row {
  display: flex;
  align-items: center;
  height: 100%;
  flex-shrink: 0;
}

.branch {
  position: relative;
  height: 100%;
  width: var(--menu-navigation-components-branch-width);
  flex-shrink: 0;
}

/*
 * Guide lines all run on a rail at 75% of each 32px column and share the faint
 * outline color. Verticals and the dropdown bleed 1px past the row edges so they
 * cross the visible-wrapper's 1px transparent flat border and meet the adjacent
 * row's line with no seam gap.
 */
.branch-vertical {
  position: absolute;
  top: -1px;
  bottom: -1px;
  left: 75%;
  width: 1px;
  transform: translateX(-0.5px);
  background: var(--border-outline-color);
}

.branch-horizontal {
  position: absolute;
  top: 50%;
  transform: translateY(-0.5px);
  left: 75%;
  right: 0;
  height: 1px;
  background: var(--border-outline-color);
}

/*
 * Corner (└, last child): a single bordered box replaces the straight rects so
 * the bend can be rounded. The box bleeds 1px past the column's right edge so its
 * bottom border overlaps the terminal connector with no break, and translateY
 * drops it 0.5px so that border lands on the connector's pixel row (else the join
 * reads as a \`---___\` step). The radius stays tight — the stub is only 8px, so a
 * larger fillet would consume the whole flat run.
 */
.branch-corner .branch-vertical,
.branch-corner .branch-horizontal {
  display: none;
}

.branch-corner .branch-elbow {
  position: absolute;
  top: -1px;
  bottom: 50%;
  left: 75%;
  right: -1px;
  transform: translate(-0.5px, 0.5px);
  border-left: 1px solid var(--border-outline-color);
  border-bottom: 1px solid var(--border-outline-color);
  border-bottom-left-radius: var(
    --menu-navigation-components-branch-corner-radius,
    2px
  );
}

.terminal {
  position: relative;
  height: 100%;
  width: var(--global-size-spacing-touch-target-min);
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Stub entering the terminal, continuing the guide line up to the chevron gap. */
.terminal-connector {
  position: absolute;
  top: 50%;
  transform: translateY(-0.5px);
  left: 0;
  width: 25%;
  height: 1px;
  background: var(--border-outline-color);
}

/* On a leaf (no chevron) the stub runs further, stopping ~13px before the icon. */
.terminal:not(:has(.chevron)) .terminal-connector {
  width: calc(100% - 13px);
}

/* Descends from below the chevron to connect an expanded node to its children. */
.terminal-dropdown {
  position: absolute;
  left: 50%;
  transform: translateX(-0.5px);
  top: 75%;
  bottom: -1px;
  width: 1px;
  background: var(--border-outline-color);
}

/* Visual expand/collapse indicator only — not a separate control. */
.chevron {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: var(--menu-navigation-components-tree-navigation-item-icon-size);
  height: var(--menu-navigation-components-tree-navigation-item-icon-size);
  color: var(--element-neutral-color);
  transition: transform 100ms ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .chevron {
    transition: none;
  }
}

.wrapper.disabled .chevron {
  color: var(--on-flat-disabled-color);
}

:host([expanded]) .chevron {
  transform: rotate(90deg);
}

/* Alert-header marker for non-regular terminal types, at the terminal's top-right. */
.terminal-header {
  position: absolute;
  inset: 0;
  display: flex;
  justify-content: flex-end;
  align-items: flex-start;
  padding: var(--menu-navigation-components-terminal-padding-aggregated-icon);
  color: var(--element-neutral-color);
  pointer-events: none;
}

.terminal-header > * {
  width: var(--menu-navigation-components-tree-navigation-item-icon-size);
  height: var(--menu-navigation-components-tree-navigation-item-icon-size);
}

.wrapper.disabled .terminal-header {
  color: var(--on-flat-disabled-color);
}

.label-container {
  display: flex;
  flex: 1;
  gap: var(
    --menu-navigation-components-tree-navigation-item-padding-horizontal
  );
  align-items: center;
  min-width: 0;
  padding-right: var(
    --menu-navigation-components-tree-navigation-item-padding-horizontal
  );
}

.leading-icon {
  position: relative;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: var(--menu-navigation-components-tree-navigation-item-icon-size);
  height: var(--menu-navigation-components-tree-navigation-item-icon-size);
  color: var(--on-flat-neutral-color);
}

::slotted([slot="icon"]) {
  display: block;
  width: var(--menu-navigation-components-tree-navigation-item-icon-size);
  height: var(--menu-navigation-components-tree-navigation-item-icon-size);
}

.label {
  flex: 1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  min-width: 0;
}

/*
 * Trailing badge area. A row can carry more than one alert badge (e.g. a
 * critical count beside a warning count); they sit in a flex row spaced by the
 * shared alert-counter spacing token.
 */
.alert-badges {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  gap: var(--app-components-alert-counter-item-badge-spacing);
}

.alert-badge {
  flex-shrink: 0;
}
`,on=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M10.5977 3.45245L2.11783 18.6539C1.68126 19.4365 1.46298 19.8278 1.5 20.1481C1.5323 20.4276 1.68084 20.6806 1.90919 20.8449C2.17092 21.0333 2.61899 21.0333 3.51513 21.0333H20.4697C21.3656 21.0333 21.8136 21.0333 22.0753 20.845C22.3036 20.6806 22.4522 20.4277 22.4845 20.1483C22.5216 19.828 22.3034 19.4367 21.8672 18.6542L13.3925 3.45281C12.9361 2.63423 12.7079 2.22495 12.4074 2.08895C12.1454 1.97039 11.8451 1.97035 11.5831 2.08884C11.2825 2.22476 11.0542 2.63399 10.5977 3.45245Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M10.5977 3.45245L2.11783 18.6539C1.68126 19.4365 1.46298 19.8278 1.5 20.1481C1.5323 20.4276 1.68084 20.6806 1.90919 20.8449C2.17092 21.0333 2.61899 21.0333 3.51513 21.0333H20.4697C21.3656 21.0333 21.8136 21.0333 22.0753 20.845C22.3036 20.6806 22.4522 20.4277 22.4845 20.1483C22.5216 19.828 22.3034 19.4367 21.8672 18.6542L13.3925 3.45281C12.9361 2.63423 12.7079 2.22495 12.4074 2.08895C12.1454 1.97039 11.8451 1.97035 11.5831 2.08884C11.2825 2.22476 11.0542 2.63399 10.5977 3.45245Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},sn=(on.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,on);N([P({type:Boolean})],sn.prototype,`useCssColor`,void 0),sn=N([M(`obi-alarm-badge`)],sn);var cn=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M3 4.6C3 4.03995 3 3.75992 3.10899 3.54601C3.20487 3.35785 3.35785 3.20487 3.54601 3.10899C3.75992 3 4.03995 3 4.6 3H19.4C19.9601 3 20.2401 3 20.454 3.10899C20.6422 3.20487 20.7951 3.35785 20.891 3.54601C21 3.75992 21 4.03995 21 4.6V19.4C21 19.9601 21 20.2401 20.891 20.454C20.7951 20.6422 20.6422 20.7951 20.454 20.891C20.2401 21 19.9601 21 19.4 21H4.6C4.03995 21 3.75992 21 3.54601 20.891C3.35785 20.7951 3.20487 20.6422 3.10899 20.454C3 20.2401 3 19.9601 3 19.4V4.6Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M3 4.6C3 4.03995 3 3.75992 3.10899 3.54601C3.20487 3.35785 3.35785 3.20487 3.54601 3.10899C3.75992 3 4.03995 3 4.6 3H19.4C19.9601 3 20.2401 3 20.454 3.10899C20.6422 3.20487 20.7951 3.35785 20.891 3.54601C21 3.75992 21 4.03995 21 4.6V19.4C21 19.9601 21 20.2401 20.891 20.454C20.7951 20.6422 20.6422 20.7951 20.454 20.891C20.2401 21 19.9601 21 19.4 21H4.6C4.03995 21 3.75992 21 3.54601 20.891C3.35785 20.7951 3.20487 20.6422 3.10899 20.454C3 20.2401 3 19.9601 3 19.4V4.6Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},ln=(cn.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,cn);N([P({type:Boolean})],ln.prototype,`useCssColor`,void 0),ln=N([M(`obi-caution-badge`)],ln);var un=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z" fill="currentColor"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M18.2071 9.20718L10.5 16.9143L5.79291 12.2072L7.20712 10.793L10.5 14.0859L16.7929 7.79297L18.2071 9.20718Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z" style="fill: var(--alert-running-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M18.2071 9.20718L10.5 16.9143L5.79291 12.2072L7.20712 10.793L10.5 14.0859L16.7929 7.79297L18.2071 9.20718Z" style="fill: var(--on-running-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},dn=(un.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,un);N([P({type:Boolean})],dn.prototype,`useCssColor`,void 0),dn=N([M(`obi-running-color-iec`)],dn);var fn=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<circle cx="12" cy="12" r="10" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="12" cy="12" r="10" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},pn=(fn.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,fn);N([P({type:Boolean})],pn.prototype,`useCssColor`,void 0),pn=N([M(`obi-warning-badge`)],pn);var mn=o`* {
  -webkit-tap-highlight-color: transparent;
}

.wrapper {
  user-select: none;
  display: flex;
  align-items: center;
  justify-content: center;
  border-style: solid;
  border-radius: var(--ui-components-badge-border-radius);
  padding: calc(var(--ui-components-badge-padding) - 1px);
  border: 1px solid var(--alert-alarm-outline-color);
  background: var(--alert-alarm-color);
  width: fit-content;
  height: 16px;
  box-sizing: border-box;
}

.wrapper .badge-icon {
    width: 100%;
    height: 100%;
  }

.wrapper .icon {
    width: var(--ui-components-badge-icon-size);
    height: var(--ui-components-badge-icon-size);
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
  }

.wrapper .number {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-label-active-font-weight);
    font-size: var(--global-typography-ui-label-active-font-size);
    line-height: var(--global-typography-ui-label-active-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0 var(--ui-components-badge-label-spacing) 1px
      var(--ui-components-badge-label-spacing);
    height: var(--ui-components-badge-icon-size);
    min-width: var(--ui-components-badge-icon-size);
  }

.wrapper.size-large {
    display: inline-flex;
    width: fit-content;
    height: 24px;
    min-width: var(--ui-components-badge-min-size-large);
    min-height: var(--ui-components-badge-min-size-large);

    padding: calc(var(--ui-components-badge-padding) - 1px);
    justify-content: center;
    align-items: center;
    background: var(--alert-alarm-color);
  }

.wrapper.size-large .number {
      padding-bottom: 0;
    }

.wrapper.size-large .number-text {
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-body-active-font-weight);
      font-size: var(--global-typography-ui-body-active-font-size);
      line-height: var(--global-typography-ui-body-active-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    }

.wrapper.size-large .icon {
      width: var(--ui-components-badge-icon-size-large);
      height: var(--ui-components-badge-icon-size-large);
      display: flex;
      align-items: center;
      justify-content: center;
    }

.wrapper.size-large.type-empty {
      min-width: 38px;
      height: 24px;
    }

.wrapper.type-regular {
    color: var(--on-normal-neutral-color);
    background-color: var(--normal-enabled-background-color);
    border-color: var(--normal-enabled-border-color);
  }

.wrapper.type-alarm {
    background-color: var(--alert-alarm-color);
    border-color: var(--alert-alarm-outline-color);
    color: var(--on-alarm-color);
  }

.wrapper.type-warning {
    background-color: var(--alert-warning-color);
    border-color: var(--alert-warning-outline-color);
    color: var(--on-warning-color);
  }

.wrapper.type-caution,.wrapper.type-level-low {
    background-color: var(--alert-caution-color);
    border-color: var(--alert-caution-outline-color);
    color: var(--on-caution-color);
  }

.wrapper.type-level-critical {
    background-color: var(--critical-enabled-background-color);
    border-color: var(--critical-enabled-border-color);
    color: var(--on-critical-color);
  }

.wrapper.type-level-high {
    background-color: var(--alert-alarm-color);
    border-color: var(--alert-alarm-outline-color);
    color: var(--on-alarm-color);
  }

.wrapper.type-level-medium {
    background-color: var(--alert-warning-color);
    border-color: var(--alert-warning-outline-color);
    color: var(--on-warning-color);
  }

.wrapper.type-level-diagnostic {
    background-color: var(--notification-enabled-background-color);
    border-color: var(--notification-enabled-border-color);
    color: var(--on-notification-active-color);
  }

.wrapper.type-running {
    background-color: var(--alert-running-color);
    border-color: var(--alert-running-color);
    color: var(--on-running-color);
  }

.wrapper.type-notification {
    background-color: var(--instrument-enhanced-primary-color);
    border-color: var(--instrument-enhanced-primary-color);
    color: var(--on-selected-active-color);
  }

.wrapper.type-enhance {
    background-color: var(--instrument-enhanced-secondary-color);
    border-color: var(--instrument-enhanced-secondary-color);
    color: var(--on-selected-active-color);
  }

.wrapper.type-empty {
    background-color: var(--flat-enabled-background-color);
    border-color: var(--normal-enabled-border-color);
    min-width: 28px;
  }

.wrapper.type-automation {
    background-color: var(--container-background-color);
    border-color: var(--container-background-color);
    color: var(--on-flat-neutral-color);
  }

.wrapper.variant-flat {
    background-color: var(--flat-enabled-background-color);
    border-color: var(--flat-enabled-background-color);
  }

.wrapper.variant-flat .icon {
      min-width: var(--ui-components-badge-icon-size);
      min-height: var(--ui-components-badge-icon-size);
    }

.wrapper.variant-flat .icon.type-alarm {
      color: unset;
      border-color: var(--alert-alarm-outline-color);
      background: none;
    }

.wrapper.variant-flat .icon.type-warning {
      color: unset;
      border-color: var(--alert-warning-outline-color);
      background: none;
    }

.wrapper.variant-flat .icon.type-caution,.wrapper.variant-flat .icon.type-level-low {
      color: unset;
      border-color: var(--alert-caution-outline-color);
      background: none;
    }

.wrapper.variant-flat .icon.type-level-critical {
      color: unset;
      border-color: var(--critical-enabled-border-color);
      background: none;
    }

.wrapper.variant-flat .icon.type-level-high {
      color: unset;
      border-color: var(--alert-alarm-outline-color);
      background: none;
    }

.wrapper.variant-flat .icon.type-level-medium {
      color: unset;
      border-color: var(--alert-warning-outline-color);
      background: none;
    }

.wrapper.variant-flat .icon.type-level-diagnostic {
      color: unset;
      border-color: var(--notification-enabled-border-color);
      background: none;
    }

.wrapper.variant-flat .icon.type-regular {
      color: unset;
      border-color: var(--normal-enabled-border-color);
      background: none;
    }

.wrapper.variant-flat .icon.type-notification {
      color: var(--instrument-enhanced-primary-color);
      border-color: var(
        --instrument-enhanced-primary-outline-color,
        transparent
      );
      background: none;
    }

.wrapper.variant-flat .icon.type-enhance {
      color: var(--instrument-enhanced-secondary-color);
      background: none;
    }

.wrapper.variant-flat .icon.type-regular {
      color: var(--on-normal-neutral-color);
    }

.wrapper.variant-flat .number {
      color: var(--element-active-color);
    }

.wrapper.variant-flat .icon.type-automation {
      color: unset;
      background: none;
    }

.wrapper.variant-flat .icon.type-outline {
      width: var(--ui-components-badge-icon-size-flat);
      height: var(--ui-components-badge-icon-size-flat);
    }

.wrapper.variant-flat .icon.type-outline + .number {
      color: var(--on-normal-neutral-color);
    }

.icon.type-alarm path {
  stroke: var(--alert-alarm-outline-color);
}
.icon.type-warning circle {
  stroke: var(--alert-warning-outline-color);
}
.icon.type-caution path {
  stroke: var(--alert-caution-outline-color);
}
.icon.type-running path {
  stroke: none;
}
`,hn,gn=function(e){return e.regular=`regular`,e.large=`large`,e}({}),_n=function(e){return e.alarm=`alarm`,e.warning=`warning`,e.caution=`caution`,e.levelCritical=`level-critical`,e.levelHigh=`level-high`,e.levelMedium=`level-medium`,e.levelLow=`level-low`,e.levelDiagnostic=`level-diagnostic`,e.running=`running`,e.notification=`notification`,e.enhance=`enhance`,e.regular=`regular`,e.empty=`empty`,e.automation=`automation`,e.outline=`outline`,e}({}),vn=(hn=class extends j{constructor(...e){super(...e),this.number=0,this.showNumber=!0,this.type=`regular`,this.size=`regular`,this.variant=`default`,this.showIcon=!1}get effectiveType(){return!this.showIcon&&!this.showNumber?`empty`:this.type}renderIcon(){let e=this.variant===`flat`;switch(this.type){case`alarm`:return O`
          <svg width="100%" height="100%" viewBox="0 0 12 12" fill="none">
            <path
              d="M5.29694 1.72622L1.05702 9.32693C0.838739 9.71823 0.729598 9.91388 0.748108 10.0741C0.764257 10.2138 0.83853 10.3403 0.952704 10.4225C1.08357 10.5167 1.3076 10.5167 1.75567 10.5167H10.233C10.6809 10.5167 10.9049 10.5167 11.0357 10.4225C11.1499 10.3403 11.2242 10.2139 11.2404 10.0741C11.2589 9.914 11.1498 9.71837 10.9317 9.3271L6.69433 1.7264C6.46616 1.31712 6.35207 1.11247 6.20181 1.04447C6.07082 0.985194 5.92064 0.985175 5.78964 1.04442C5.63936 1.11238 5.52522 1.317 5.29694 1.72622Z"
              fill=${e?`var(--alert-alarm-color)`:`currentColor`}
            />
          </svg>
        `;case`warning`:return O`
          <svg width="100%" height="100%" viewBox="0 0 12 12" fill="none">
            <circle
              cx="6"
              cy="6"
              r="4.5"
              fill=${e?`var(--alert-warning-color)`:`currentColor`}
              stroke=${e?`var(--alert-warning-outline-color)`:`currentColor`}
            />
          </svg>
        `;case`caution`:return O`
          <svg width="100%" height="100%" viewBox="0 0 12 12" fill="none">
            <path
              d="M2.2998 2H9.7002C9.848 2 9.92907 2.00015 9.9873 2.00488C9.98955 2.00507 9.99213 2.0047 9.99414 2.00488C9.99436 2.0072 9.9949 2.01006 9.99512 2.0127C9.99985 2.07093 10 2.152 10 2.2998V9.7002C10 9.848 9.99985 9.92907 9.99512 9.9873C9.99493 9.98958 9.99433 9.9921 9.99414 9.99414C9.9921 9.99433 9.98958 9.99493 9.9873 9.99512C9.92907 9.99985 9.848 10 9.7002 10H2.2998C2.152 10 2.07093 9.99985 2.0127 9.99512C2.01006 9.9949 2.0072 9.99436 2.00488 9.99414C2.0047 9.99213 2.00507 9.98955 2.00488 9.9873C2.00015 9.92907 2 9.848 2 9.7002V2.2998L2.00488 2.0127C2.0051 2.01009 2.00467 2.00718 2.00488 2.00488C2.00718 2.00467 2.01009 2.0051 2.0127 2.00488L2.2998 2Z"
              fill=${e?`var(--alert-caution-color)`:`currentColor`}
              stroke=${e?`var(--alert-caution-outline-color)`:`currentColor`}
            />
          </svg>
        `;case`level-high`:return O`
          <svg width="100%" height="100%" viewBox="0 0 12 12" fill="none">
            <path
              d="M5.29694 1.72622L1.05702 9.32693C0.838739 9.71823 0.729598 9.91388 0.748108 10.0741C0.764257 10.2138 0.83853 10.3403 0.952704 10.4225C1.08357 10.5167 1.3076 10.5167 1.75567 10.5167H10.233C10.6809 10.5167 10.9049 10.5167 11.0357 10.4225C11.1499 10.3403 11.2242 10.2139 11.2404 10.0741C11.2589 9.914 11.1498 9.71837 10.9317 9.3271L6.69433 1.7264C6.46616 1.31712 6.35207 1.11247 6.20181 1.04447C6.07082 0.985194 5.92064 0.985175 5.78964 1.04442C5.63936 1.11238 5.52522 1.317 5.29694 1.72622Z"
              fill=${e?`var(--alert-alarm-color)`:`currentColor`}
            />
          </svg>
        `;case`level-medium`:return O`
          <svg width="100%" height="100%" viewBox="0 0 12 12" fill="none">
            <circle
              cx="6"
              cy="6"
              r="4.5"
              fill=${e?`var(--alert-warning-color)`:`currentColor`}
              stroke=${e?`var(--alert-warning-outline-color)`:`currentColor`}
            />
          </svg>
        `;case`level-low`:return O`
          <svg width="100%" height="100%" viewBox="0 0 12 12" fill="none">
            <path
              d="M2.2998 2H9.7002C9.848 2 9.92907 2.00015 9.9873 2.00488C9.98955 2.00507 9.99213 2.0047 9.99414 2.00488C9.99436 2.0072 9.9949 2.01006 9.99512 2.0127C9.99985 2.07093 10 2.152 10 2.2998V9.7002C10 9.848 9.99985 9.92907 9.99512 9.9873C9.99493 9.98958 9.99433 9.9921 9.99414 9.99414C9.9921 9.99433 9.98958 9.99493 9.9873 9.99512C9.92907 9.99985 9.848 10 9.7002 10H2.2998C2.152 10 2.07093 9.99985 2.0127 9.99512C2.01006 9.9949 2.0072 9.99436 2.00488 9.99414C2.0047 9.99213 2.00507 9.98955 2.00488 9.9873C2.00015 9.92907 2 9.848 2 9.7002V2.2998L2.00488 2.0127C2.0051 2.01009 2.00467 2.00718 2.00488 2.00488C2.00718 2.00467 2.01009 2.0051 2.0127 2.00488L2.2998 2Z"
              fill=${e?`var(--alert-caution-color)`:`currentColor`}
              stroke=${e?`var(--alert-caution-outline-color)`:`currentColor`}
            />
          </svg>
        `;case`level-critical`:return O`
          <svg width="100%" height="100%" viewBox="0 0 12 12" fill="none">
            <path
              d="M11 6L8.5 10.33H3.5L1 6L3.5 1.67H8.5L11 6Z"
              fill=${e?`var(--critical-enabled-background-color)`:`currentColor`}
            />
          </svg>
        `;case`level-diagnostic`:return O`
          <svg width="100%" height="100%" viewBox="0 0 12 12" fill="none">
            <path
              d="M5.25 1H6.75V5.7L9.955 3.85L10.705 5.15L7.5 7L10.705 8.85L9.955 10.15L6.75 8.3V11H5.25V8.3L2.045 10.15L1.295 8.85L4.5 7L1.295 5.15L2.045 3.85L5.25 5.7V1Z"
              fill=${e?`var(--notification-enabled-background-color)`:`currentColor`}
            />
          </svg>
        `;case`running`:return O`
          <svg width="100%" height="100%" viewBox="0 0 12 12" fill="none">
            <path
              fill-rule="evenodd"
              clip-rule="evenodd"
              d="M11 6C11 8.76142 8.76142 11 6 11C3.23858 11 1 8.76142 1 6C1 3.23858 3.23858 1 6 1C8.76142 1 11 3.23858 11 6ZM2.89624 6.10353L3.60335 5.39642L5.24979 7.04287L8.39624 3.89642L9.10335 4.60353L5.24979 8.45708L2.89624 6.10353Z"
              fill=${e?`var(--alert-running-color)`:`currentColor`}
            />
          </svg>
        `;default:return O`<slot class="badge-icon" name="badge-icon"></slot>`}}render(){let e=this.variant===`flat`;return O`
      <div
        class=${F({wrapper:!0,[`size-`+this.size]:!0,[`type-`+this.effectiveType]:!e,"variant-flat":e,hideNumber:!this.showNumber})}
      >
        ${this.effectiveType===`empty`?``:O`
                ${this.showIcon?O`
                        <div
                          class=${F({icon:!0,[`type-`+this.type]:e})}
                        >
                          ${this.renderIcon()}
                        </div>
                      `:A}
                ${this.showNumber?O`<div class="number">
                        <span class="number-text">${this.number}</span>
                      </div>`:``}
              `}
      </div>
    `}},hn.styles=a(mn),hn);N([P({type:Number})],vn.prototype,`number`,void 0),N([P({type:Boolean,attribute:!1})],vn.prototype,`showNumber`,void 0),N([P({type:String})],vn.prototype,`type`,void 0),N([P({type:String})],vn.prototype,`size`,void 0),N([P({type:String})],vn.prototype,`variant`,void 0),N([P({type:Boolean})],vn.prototype,`showIcon`,void 0),vn=N([M(`obc-badge`)],vn);var yn,bn=function(e){return e.straight=`straight`,e.intersection=`intersection`,e.corner=`corner`,e.blank=`blank`,e}({}),xn=function(e){return e.regular=`regular`,e.aggregatedHeader=`aggregated-header`,e.groupHeader=`group-header`,e}({}),Sn=(yn=class extends j{constructor(...e){super(...e),this.label=`List item`,this.branches=[],this.expandable=!1,this.expanded=!1,this.checked=!1,this.disabled=!1,this.focusable=!0,this.hasLeadingIcon=!0,this.terminalType=`regular`}focus(e){this.wrapperElement?.focus(e)}get alertBadges(){return this.alerts?$t(this.alerts,this.alerts.combine):[]}get isRoot(){return this.branches.length===0}get isBlankAncestry(){return this.branches.length>0&&this.branches.every(e=>e===`blank`)}activate(){this.disabled||(this.expandable&&this.dispatchEvent(new CustomEvent(`expand-toggle`,{detail:!this.expanded})),!this.checked&&(this.dispatchEvent(new CustomEvent(`click`)),this.href!==void 0&&(window.location.href=this.href)))}handleKeydown(e){this.disabled||(e.key===`Enter`||e.key===` `)&&(e.preventDefault(),this.activate())}renderBranch(e){let t=e===`straight`||e===`intersection`||e===`corner`,n=e===`intersection`||e===`corner`;return O`<div
      class=${F({branch:!0,[`branch-`+e]:!0})}
    >
      ${t?O`<div class="branch-vertical"></div>`:A}
      ${n?O`<div class="branch-horizontal"></div>`:A}
      ${e===`corner`?O`<div class="branch-elbow"></div>`:A}
    </div>`}renderTerminalHeader(){return this.terminalType===`aggregated-header`?O`<div class="terminal-header" aria-hidden="true">
        <obi-alert-header-aggregated-iec></obi-alert-header-aggregated-iec>
      </div>`:this.terminalType===`group-header`?O`<div class="terminal-header" aria-hidden="true">
        <obi-alert-header-group-iec></obi-alert-header-group-iec>
      </div>`:A}render(){return O`
      <div
        class=${F({wrapper:!0,checked:this.checked,disabled:this.disabled,"has-icon":this.hasLeadingIcon})}
        role="treeitem"
        aria-expanded=${I(this.expandable?this.expanded:void 0)}
        aria-current=${I(this.checked?`page`:void 0)}
        aria-selected=${I(this.checked?`true`:void 0)}
        aria-disabled=${I(this.disabled?`true`:void 0)}
        tabindex=${this.disabled?-1:this.focusable?0:-1}
        @click=${this.activate}
        @keydown=${this.handleKeydown}
      >
        <div class="visible-wrapper">
          <div class="tree-node-row">
            ${this.branches.map(e=>this.renderBranch(e))}
            <div class="terminal">
              ${this.isRoot||this.isBlankAncestry?A:O`<div class="terminal-connector"></div>`}
              ${!this.isRoot&&!this.isBlankAncestry&&this.expandable&&this.expanded?O`<div class="terminal-dropdown"></div>`:A}
              ${this.expandable?O`<div class="chevron" aria-hidden="true">
                      <obi-chevron-right-google></obi-chevron-right-google>
                    </div>`:A}
              ${this.renderTerminalHeader()}
            </div>
          </div>
          <div class="label-container">
            ${this.hasLeadingIcon?O`<div class="leading-icon">
                    <slot name="icon"></slot>
                  </div>`:A}
            <span part="label" class="label">${this.label}</span>
          </div>
          ${this.alertBadges.length>0?O`<div class="alert-badges">
                  ${this.alertBadges.map(e=>O`<obc-badge
                        class="alert-badge"
                        .type=${e.type}
                        .number=${e.count}
                      ></obc-badge>`)}
                </div>`:A}
        </div>
      </div>
    `}},yn.styles=a(an),yn);N([P({type:String})],Sn.prototype,`label`,void 0),N([P({type:Array})],Sn.prototype,`branches`,void 0),N([P({type:Boolean})],Sn.prototype,`expandable`,void 0),N([P({type:Boolean,reflect:!0})],Sn.prototype,`expanded`,void 0),N([P({type:Boolean,reflect:!0})],Sn.prototype,`checked`,void 0),N([P({type:Boolean,reflect:!0})],Sn.prototype,`disabled`,void 0),N([P({type:Boolean,attribute:!1})],Sn.prototype,`focusable`,void 0),N([P({type:Boolean,attribute:!1})],Sn.prototype,`hasLeadingIcon`,void 0),N([P({type:String})],Sn.prototype,`terminalType`,void 0),N([P({type:Object})],Sn.prototype,`alerts`,void 0),N([P({type:String})],Sn.prototype,`href`,void 0),N([Ve(`.wrapper`)],Sn.prototype,`wrapperElement`,void 0),Sn=N([M(`obc-tree-navigation-item`)],Sn);var Cn,wn=`obc-navigation-item`,Tn=`obc-navigation-item-group`;function En(e){return e.tagName.toLowerCase()===Tn}function Dn(e){let t=e.tagName.toLowerCase();return t===wn||t===Tn}var On=function(e){return e.Full=`full`,e.IconOnly=`icon-only`,e.IconOnlyLarge=`icon-only-large`,e.Compact=`compact`,e.Tree=`tree`,e}({}),kn=(Cn=class extends j{constructor(...e){super(...e),this.softDismiss=!1,this.open=!1,this.softDismissController=new Ht(this),this.variant=`full`,this.flyoutVariant=`full`,this.smallScreen=!1,this.slotObservers=[],this.hasFooter=!1,this.treeNavigator=new Gt({getRows:()=>this.treeRootRows(),childRows:e=>this.treeChildRows(e),isGroup:e=>En(e),isExpanded:e=>En(e)&&e.expanded,setExpanded:(e,t)=>{En(e)&&(t?e.open():e.close())},innerItem:e=>this.treeInnerItem(e)}),this.onTreeKeydown=e=>{this.variant===`tree`&&this.treeNavigator.handleKeydown(e)&&e.preventDefault()}}treeRootRows(){return Array.from(this.children).filter(e=>{if(!Dn(e))return!1;let t=e.getAttribute(`slot`);return t===null||t===`main`})}treeChildRows(e){return Array.from(e.children).filter(Dn)}treeInnerItem(e){return e.shadowRoot?.querySelector(`obc-tree-navigation-item`)??null}connectedCallback(){super.connectedCallback(),this.addEventListener(`keydown`,this.onTreeKeydown)}findAllElements(e,t,{slot:n,stopTag:r}={}){let i=[];for(let a of e.children)if(a.tagName.toLowerCase()===t){if(n&&a.getAttribute(`slot`)!==n)continue;i.push(a)}else if(r&&a.tagName.toLowerCase()===r)continue;else{if(n&&a.getAttribute(`slot`)!==n)continue;i.push(...this.findAllElements(a,t,{stopTag:r}))}return i}findAllGroups(e){return this.findAllElements(e,`obc-navigation-item-group`)}findRootItems(e){return this.findAllElements(e,`obc-navigation-item`,{stopTag:`obc-navigation-item-group`})}findAllItems(e,t){return this.findAllElements(e,`obc-navigation-item`,{slot:t})}closeAllGroups(){this.findAllGroups(this).forEach(e=>{e.close()})}registerGroup(e){e.forEach(t=>{t.addEventListener(`open`,()=>{this.variant!==`tree`&&e.forEach(e=>{e!==t&&e.close()})});let n=this.findAllGroups(t);this.registerGroup(n)})}cleanupSlotObservers(){this.slotObservers.forEach(e=>e.disconnect()),this.slotObservers=[]}setupSlotObservers(){this.cleanupSlotObservers();let e=this.shadowRoot?.querySelector(`slot[name="main"]`),t=this.shadowRoot?.querySelector(`slot[name="footer"]`);this.hasFooter=t?.assignedElements().length>0,[e,t].forEach(e=>{e&&e.assignedElements().forEach(e=>{let t=new MutationObserver(()=>{this.setupItems()});t.observe(e,{childList:!0,subtree:!0}),this.slotObservers.push(t)})})}firstUpdated(e){super.firstUpdated(e);let t=this.findAllGroups(this);this.registerGroup(t)}updated(e){super.updated(e),(e.has(`variant`)||e.has(`flyoutVariant`))&&this.setupItems()}setVariantToFlyoutItems(e){this.findAllElements(e,`obc-navigation-item`).forEach(e=>{e.variant=`full`}),this.findAllGroups(e).forEach(e=>{e.variant=`full`,this.setVariantToFlyoutItems(e)})}disconnectedCallback(){super.disconnectedCallback(),this.cleanupSlotObservers(),this.removeEventListener(`keydown`,this.onTreeKeydown)}handleSlotChange(){this.setupItems(),this.setupSlotObservers()}assignTreeBranches(e,t){for(let n of e.children){let e=n.tagName.toLowerCase(),r=e===`obc-navigation-item`,i=e===`obc-navigation-item-group`;if(!r&&!i)continue;if(t===0){let e=n.getAttribute(`slot`);if(e!==null&&e!==`main`)continue}let a=Array.from({length:t},()=>bn.blank),o=n;o.treeMode=!0,o.treeBranches=a,i&&this.assignTreeBranches(n,t+1)}}clearTreeMode(e){for(let t of e.children){let e=t.tagName.toLowerCase(),n=e===`obc-navigation-item`,r=e===`obc-navigation-item-group`;if(!n&&!r)continue;let i=t;i.treeMode=!1,i.treeBranches=[],r&&this.clearTreeMode(t)}}setupItems(){if(this.variant===`tree`){this.assignTreeBranches(this,0),[`footer`,`logo`].forEach(e=>{this.findAllItems(this,e).forEach(e=>{e.treeMode=!1,e.treeBranches=[],e.variant=`full`})}),queueMicrotask(()=>this.treeNavigator.refresh());return}this.clearTreeMode(this);let e=this.variant!==`full`||this.flyoutVariant===`compact`;this.setHugToGroups(this,e),this.findAllGroups(this).forEach(e=>{e.variant=this.variant,this.setVariantToFlyoutItems(e)}),this.findRootItems(this).forEach(e=>{e.variant=this.variant});let t=this.smallScreen&&this.variant===`full`?`compact`:this.variant;this.findAllItems(this,`footer`).forEach(e=>{e.variant=t}),this.findAllItems(this,`logo`).forEach(e=>{e.variant=t}),this.findAllItems(this).forEach(e=>{e.addEventListener(`click`,()=>{this.closeAllGroups()})})}setHugToGroups(e,t){this.findAllGroups(e).forEach(e=>{e.hug=t,this.setHugToGroups(e,t)})}render(){return O`
      <div
        class="wrapper ${this.variant} ${this.smallScreen?`small-screen`:``}"
      >
        <nav class="main">
          <ol>
            <slot name="main" @slotchange=${this.handleSlotChange}></slot>
          </ol>
        </nav>
        <div class="footer ${this.hasFooter?`has-footer`:``}">
          <nav>
            <ol>
              <slot name="footer" @slotchange=${this.handleSlotChange}></slot>
              ${this.smallScreen?O` <slot name="logo"></slot> `:A}
            </ol>
          </nav>
          ${this.smallScreen?A:O`
                  <div class="logo">
                    <slot name="logo"></slot>
                  </div>
                `}
        </div>
      </div>
    `}},Cn.styles=a(Kt),Cn);N([P({type:Boolean})],kn.prototype,`softDismiss`,void 0),N([P({type:Boolean})],kn.prototype,`open`,void 0),N([P({type:String})],kn.prototype,`variant`,void 0),N([P({type:String})],kn.prototype,`flyoutVariant`,void 0),N([P({type:Boolean})],kn.prototype,`smallScreen`,void 0),N([ze()],kn.prototype,`hasFooter`,void 0),kn=N([M(`obc-navigation-menu`)],kn);var An=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M9.5 15.0687C9.5 15.6745 9.5 15.9774 9.6198 16.1177C9.72374 16.2394 9.87967 16.304 10.0392 16.2914C10.2231 16.2769 10.4373 16.0627 10.8657 15.6344L13.9343 12.5657C14.1323 12.3677 14.2313 12.2687 14.2684 12.1546C14.3011 12.0541 14.3011 11.946 14.2684 11.8455C14.2313 11.7314 14.1323 11.6324 13.9343 11.4344L10.8657 8.36573C10.4373 7.93736 10.2231 7.72317 10.0392 7.7087C9.87967 7.69614 9.72374 7.76073 9.6198 7.88243C9.5 8.0227 9.5 8.3256 9.5 8.93142L9.5 15.0687Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M9.5 15.0687C9.5 15.6745 9.5 15.9774 9.6198 16.1177C9.72374 16.2394 9.87967 16.304 10.0392 16.2914C10.2231 16.2769 10.4373 16.0627 10.8657 15.6344L13.9343 12.5657C14.1323 12.3677 14.2313 12.2687 14.2684 12.1546C14.3011 12.0541 14.3011 11.946 14.2684 11.8455C14.2313 11.7314 14.1323 11.6324 13.9343 11.4344L10.8657 8.36573C10.4373 7.93736 10.2231 7.72317 10.0392 7.7087C9.87967 7.69614 9.72374 7.76073 9.6198 7.88243C9.5 8.0227 9.5 8.3256 9.5 8.93142L9.5 15.0687Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},jn=(An.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,An);N([P({type:Boolean})],jn.prototype,`useCssColor`,void 0),jn=N([M(`obi-arrow-flyout-google`)],jn);var Mn=o`* {
  -webkit-tap-highlight-color: transparent;
}

* {
  box-sizing: border-box;
}

.wrapper {
  display: flex;
  align-items: center;
  width: 100%;
  height: var(--menu-navigation-components-navigation-item-touch-target-size);
  transition: height 200ms;
  text-decoration: none;
  user-select: none;
}

.wrapper:focus-visible {
    outline-offset: -2px;
  }

.wrapper {
  cursor: pointer;
}

.wrapper:focus {
  outline: none;
}

.wrapper .visible-wrapper {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.wrapper.activated .visible-wrapper {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

.wrapper:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper:active .visible-wrapper {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

.wrapper:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper:disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper:disabled {
  cursor: not-allowed;
}

.wrapper.disabled {
  cursor: not-allowed;
}

.wrapper {
  color: var(--on-flat-active-color);
}

.wrapper .visible-wrapper {
    display: flex;
    align-items: center;
    width: 100%;
    height: 100%;
    border-radius: var(
      --menu-navigation-components-navigation-item-border-radius
    );
    padding: 0px
      calc(
        var(
            --menu-navigation-components-navigation-item-margin-horizontal-list-item
          ) +
          var(--menu-navigation-components-navigation-item-padding-horizontal)
      );
  }

.wrapper {

  font-family: var(--global-typography-font-family);

  font-weight: var(--global-typography-ui-body-font-weight);

  font-size: var(--global-typography-ui-body-font-size);

  line-height: var(--global-typography-ui-body-line-height);

  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
}

.wrapper.full .flyout-wrapper {
    display: flex;
    width: var(
      --menu-navigation-components-navigation-item-flyout-icon-container-size
    );
    align-items: center;
  }

:is(.wrapper.full .flyout-wrapper) .icon {
      flex-shrink: 0;
    }

.wrapper.icon-only,.wrapper.icon-only-large {
    width: var(--menu-navigation-components-navigation-item-touch-target-size);
    padding: var(
        --menu-navigation-components-navigation-item-margin-vertical-icon-button
      )
      var(
        --menu-navigation-components-navigation-item-margin-horizontal-icon-button
      );
  }

:is(.wrapper.icon-only,.wrapper.icon-only-large) .visible-wrapper {
      position: relative;
      padding: 0;
      display: flex;
      align-items: center;
      justify-content: center;
    }

.wrapper.icon-only-large {
    width: var(--menu-navigation-components-navigation-item-touch-target-size);
    height: var(--menu-navigation-components-navigation-item-touch-target-size);
    padding: 0;
  }

.wrapper.icon-only-large .icon.leading {
      anchor-name: --leading-icon;
    }

.wrapper.icon-only-large .icon.trailing {
      width: var(--menu-navigation-components-navigation-item-icon-size);
      height: var(--menu-navigation-components-navigation-item-icon-size);
      flex-shrink: 0;
      position: absolute;
      right: anchor(right);
      transform: translateX(60%);
      position-anchor: --leading-icon;
      top: anchor(top);
      bottom: anchor(bottom);
      margin: auto;
    }

.wrapper.compact {
    position: relative;
    width: var(
      --menu-navigation-components-navigation-item-touch-target-size-large
    );
    height: var(
      --menu-navigation-components-navigation-item-touch-target-size-large
    );
    padding: var(
        --menu-navigation-components-navigation-item-margin-vertical-icon-button
      )
      var(
        --menu-navigation-components-navigation-item-margin-horizontal-icon-button
      );
  }

.wrapper.compact .visible-wrapper {
      padding: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }

.wrapper.compact .icon.leading {
      anchor-name: --leading-icon;
    }

.wrapper.compact .icon.trailing {
      width: var(--menu-navigation-components-navigation-item-icon-size);
      height: var(--menu-navigation-components-navigation-item-icon-size);
      flex-shrink: 0;
      position: absolute;
      right: anchor(right);
      transform: translateX(60%);
      position-anchor: --leading-icon;
      top: anchor(top);
      bottom: anchor(bottom);
      margin: auto;
    }

.wrapper.compact .label {
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-label-font-weight);
      font-size: var(--global-typography-ui-label-font-size);
      line-height: var(--global-typography-ui-label-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
      flex-grow: 0;
      flex-basis: auto;
    }

.checked :is(.wrapper.compact .label) {
        font-family: var(--global-typography-font-family);
        font-weight: var(--global-typography-ui-label-active-font-weight);
        font-size: var(--global-typography-ui-label-active-font-size);
        line-height: var(--global-typography-ui-label-active-line-height);
        font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
      }

.wrapper.checked {
  cursor: pointer;
}

.wrapper.checked:focus {
  outline: none;
}

.wrapper.checked .visible-wrapper {
  border-color: var(--amplified-enabled-border-color);
  background-color: var(--amplified-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--amplified-enabled-border-color);
  --base-background-color: var(--amplified-enabled-background-color);
}

.wrapper.checked.activated .visible-wrapper {
  border-color: var(--amplified-activated-border-color);
  background-color: var(--amplified-activated-background-color);
  --base-border-color: var(--amplified-activated-border-color);
  --base-background-color: var(--amplified-activated-background-color);
}

@media (hover:hover) {

.wrapper.checked:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--amplified-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--amplified-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.checked:active .visible-wrapper {
  border-color: var(--amplified-pressed-border-color);
  background-color: var(--amplified-pressed-background-color);
}

.wrapper.checked:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.checked:disabled .visible-wrapper {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

.wrapper.checked.disabled .visible-wrapper {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

.wrapper.checked:disabled {
  cursor: not-allowed;
}

.wrapper.checked.disabled {
  cursor: not-allowed;
}

.wrapper.checked {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-body-active-font-weight);
    font-size: var(--global-typography-ui-body-active-font-size);
    line-height: var(--global-typography-ui-body-active-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
}

.wrapper.checked .icon.leading {
      color: var(--instrument-enhanced-secondary-color);
    }

.wrapper.group-selected .visible-wrapper {
    background: var(--flat-pressed-background-color);
    border-color: var(--flat-hover-border-color);
  }

.wrapper .icon {
    display: flex;
    align-items: center;
    color: var(--on-flat-neutral-color);
  }

.wrapper.full.has-icon .icon.leading {
    margin-right: var(
      --menu-navigation-components-navigation-item-label-spacing
    );
  }

.wrapper ::slotted([slot="icon"]),.wrapper ::slotted([slot="trailing-icon"]) {
    display: block;
    width: var(--menu-navigation-components-navigation-item-icon-size);
    height: var(--menu-navigation-components-navigation-item-icon-size);
  }

.wrapper .icon.trailing {
    width: var(--menu-navigation-components-navigation-item-icon-size);
    height: var(--menu-navigation-components-navigation-item-icon-size);
  }

.wrapper .label {
    flex: 1;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    min-width: 0;
  }

obc-tree-navigation-item.tree {
  display: block;
  width: 100%;
}
`,Nn,Pn=function(e){return e.Button=`button`,e.MenuItem=`menuitem`,e.MenuItemRadio=`menuitemradio`,e}({}),Fn=(Nn=class extends j{constructor(...e){super(...e),this.label=`Label`,this.focusable=!0,this.checked=!1,this.variant=On.Full,this.group=!1,this.groupSelected=!1,this.hasIcon=!1,this.hasTrailingIcon=!1,this.treeMode=!1,this.treeBranches=[],this.terminalType=xn.regular}handleKeydown(e){let t=this.getAttribute(`role`)===`menuitem`;(this.href===void 0||t)&&(e.key===`Enter`||e.key===` `)&&(e.preventDefault(),this.anchorElement?.click())}focus(e){(this.treeItemElement??this.anchorElement)?.focus(e)}getItemRole(){if(this.itemRole!==void 0)return this.itemRole;let e=this.getAttribute(`role`);return e===`menuitem`?`menuitem`:e===`menuitemradio`?`menuitemradio`:this.href===void 0?`button`:void 0}getItemTabIndex(){if(!this.focusable)return-1;let e=this.getAttribute(`tabindex`);if(e!==null){let t=Number(e);return Number.isNaN(t)?void 0:t}return this.href===void 0?0:void 0}render(){if(this.treeMode)return O`
        <obc-tree-navigation-item
          class="tree"
          .label=${this.label}
          .branches=${this.treeBranches}
          ?checked=${this.checked}
          .hasLeadingIcon=${this.hasIcon}
          .href=${this.href}
          .terminalType=${this.terminalType}
          .alerts=${this.alerts}
        >
          ${this.hasIcon?O`<slot name="icon" slot="icon"></slot>`:A}
        </obc-tree-navigation-item>
      `;let e=this.group&&this.variant!==On.IconOnly,t=this.variant===On.Compact;return O`
      <a
        class="${F({wrapper:!0,checked:this.checked,"group-selected":this.groupSelected&&this.group,"has-icon":this.hasIcon,[this.variant]:!0})}"
        href=${I(this.href)}
        @keydown=${this.handleKeydown}
        tabindex=${I(this.getItemTabIndex())}
        role=${I(this.getItemRole())}
        aria-checked=${I(this.getItemRole()===`menuitemradio`?this.checked?`true`:`false`:void 0)}
      >
        <div class="visible-wrapper">
          ${this.hasIcon?O`<slot name="icon" class="icon leading"></slot>`:A}
          ${[On.IconOnly,On.IconOnlyLarge].includes(this.variant)?A:O`
                  <span
                    part="label"
                    class=${F({label:!0,"label-flyout":e&&!t})}
                  >
                    ${this.label}
                  </span>
                `}
          ${e?O`
                  <div class="flyout-wrapper">
                    <obi-arrow-flyout-google
                      class="icon trailing"
                    ></obi-arrow-flyout-google>
                  </div>
                `:A}
          ${this.hasTrailingIcon&&!e?O`<slot name="trailing-icon" class="icon trailing"></slot>`:A}
        </div>
      </a>
    `}},Nn.styles=a(Mn),Nn);N([P({type:String})],Fn.prototype,`label`,void 0),N([P({type:Boolean,attribute:!1})],Fn.prototype,`focusable`,void 0),N([P({type:String,attribute:!1})],Fn.prototype,`itemRole`,void 0),N([P({type:String})],Fn.prototype,`href`,void 0),N([P({type:Boolean})],Fn.prototype,`checked`,void 0),N([P({type:String})],Fn.prototype,`variant`,void 0),N([P({type:Boolean})],Fn.prototype,`group`,void 0),N([P({type:Boolean})],Fn.prototype,`groupSelected`,void 0),N([P({type:Boolean,reflect:!0})],Fn.prototype,`hasIcon`,void 0),N([P({type:Boolean})],Fn.prototype,`hasTrailingIcon`,void 0),N([P({type:Boolean})],Fn.prototype,`treeMode`,void 0),N([P({type:Array})],Fn.prototype,`treeBranches`,void 0),N([P({type:String})],Fn.prototype,`terminalType`,void 0),N([P({type:Object})],Fn.prototype,`alerts`,void 0),N([Ve(`a`)],Fn.prototype,`anchorElement`,void 0),N([Ve(`obc-tree-navigation-item`)],Fn.prototype,`treeItemElement`,void 0),Fn=N([M(`obc-navigation-item`)],Fn);var In=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M18.41 16.59L17 18L11 12L17 6L18.41 7.41L13.83 12L18.41 16.59Z" fill="currentColor"/>
<path d="M12.41 16.59L11 18L5 12L11 6L12.41 7.41L7.83 12L12.41 16.59Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M18.41 16.59L17 18L11 12L17 6L18.41 7.41L13.83 12L18.41 16.59Z" style="fill: var(--element-active-color)"/>
<path d="M12.41 16.59L11 18L5 12L11 6L12.41 7.41L7.83 12L12.41 16.59Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Ln=(In.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,In);N([P({type:Boolean})],Ln.prototype,`useCssColor`,void 0),Ln=N([M(`obi-chevron-double-left-google`)],Ln);var Rn=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M5 7.41L6.41 6L12.41 12L6.41 18L5 16.59L9.58 12L5 7.41Z" fill="currentColor"/>
<path d="M11 7.41L12.41 6L18.41 12L12.41 18L11 16.59L15.58 12L11 7.41Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M5 7.41L6.41 6L12.41 12L6.41 18L5 16.59L9.58 12L5 7.41Z" style="fill: var(--element-active-color)"/>
<path d="M11 7.41L12.41 6L18.41 12L12.41 18L11 16.59L15.58 12L11 7.41Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},zn=(Rn.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Rn);N([P({type:Boolean})],zn.prototype,`useCssColor`,void 0),zn=N([M(`obi-chevron-double-right-google`)],zn);var Bn=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M13.9999 18L15.4099 16.59L10.8299 12L15.4099 7.41L13.9999 6L7.99991 12L13.9999 18Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M13.9999 18L15.4099 16.59L10.8299 12L15.4099 7.41L13.9999 6L7.99991 12L13.9999 18Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Vn=(Bn.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Bn);N([P({type:Boolean})],Vn.prototype,`useCssColor`,void 0),Vn=N([M(`obi-chevron-left-google`)],Vn);var Hn=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12 20.5C16.6944 20.5 20.5 16.6944 20.5 12C20.5 7.30558 16.6944 3.5 12 3.5C7.30558 3.5 3.5 7.30558 3.5 12C3.5 16.6944 7.30558 20.5 12 20.5ZM12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" fill="currentColor"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M12 13.5C12.8284 13.5 13.5 12.8284 13.5 12C13.5 11.1716 12.8284 10.5 12 10.5C11.1716 10.5 10.5 11.1716 10.5 12C10.5 12.8284 11.1716 13.5 12 13.5ZM12 15C13.6569 15 15 13.6569 15 12C15 10.3431 13.6569 9 12 9C10.3431 9 9 10.3431 9 12C9 13.6569 10.3431 15 12 15Z" fill="currentColor"/>
<path d="M11.25 5H12.75V7.5H11.25V5Z" fill="currentColor"/>
<path d="M19 11.25V12.75H16.5V11.25H19Z" fill="currentColor"/>
<path d="M7.58008 17.48L6.51942 16.4193L8.28719 14.6516L9.34785 15.7122L7.58008 17.48Z" fill="currentColor"/>
<path d="M6.51953 7.58008L7.58019 6.51942L9.34796 8.28719L8.2873 9.34785L6.51953 7.58008Z" fill="currentColor"/>
<path d="M11.25 16.5H12.75V19H11.25V16.5Z" fill="currentColor"/>
<path d="M7.5 11.25V12.75H5V11.25H7.5Z" fill="currentColor"/>
<path d="M15.7129 9.34839L14.6522 8.28773L16.42 6.51996L17.4807 7.58062L15.7129 9.34839Z" fill="currentColor"/>
<path d="M14.6523 15.7122L15.713 14.6515L17.4808 16.4193L16.4201 17.4799L14.6523 15.7122Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12 20.5C16.6944 20.5 20.5 16.6944 20.5 12C20.5 7.30558 16.6944 3.5 12 3.5C7.30558 3.5 3.5 7.30558 3.5 12C3.5 16.6944 7.30558 20.5 12 20.5ZM12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" style="fill: var(--element-active-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M12 13.5C12.8284 13.5 13.5 12.8284 13.5 12C13.5 11.1716 12.8284 10.5 12 10.5C11.1716 10.5 10.5 11.1716 10.5 12C10.5 12.8284 11.1716 13.5 12 13.5ZM12 15C13.6569 15 15 13.6569 15 12C15 10.3431 13.6569 9 12 9C10.3431 9 9 10.3431 9 12C9 13.6569 10.3431 15 12 15Z" style="fill: var(--element-active-color)"/>
<path d="M11.25 5H12.75V7.5H11.25V5Z" style="fill: var(--element-active-color)"/>
<path d="M19 11.25V12.75H16.5V11.25H19Z" style="fill: var(--element-active-color)"/>
<path d="M7.58008 17.48L6.51942 16.4193L8.28719 14.6516L9.34785 15.7122L7.58008 17.48Z" style="fill: var(--element-active-color)"/>
<path d="M6.51953 7.58008L7.58019 6.51942L9.34796 8.28719L8.2873 9.34785L6.51953 7.58008Z" style="fill: var(--element-active-color)"/>
<path d="M11.25 16.5H12.75V19H11.25V16.5Z" style="fill: var(--element-active-color)"/>
<path d="M7.5 11.25V12.75H5V11.25H7.5Z" style="fill: var(--element-active-color)"/>
<path d="M15.7129 9.34839L14.6522 8.28773L16.42 6.51996L17.4807 7.58062L15.7129 9.34839Z" style="fill: var(--element-active-color)"/>
<path d="M14.6523 15.7122L15.713 14.6515L17.4808 16.4193L16.4201 17.4799L14.6523 15.7122Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Un=(Hn.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Hn);N([P({type:Boolean})],Un.prototype,`useCssColor`,void 0),Un=N([M(`obi-display-brilliance-iec`)],Un);var Wn=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M16.9498 15.5355L15.5355 16.9497L16.9498 18.364L18.364 16.9497L16.9498 15.5355Z" fill="currentColor"/>
<path d="M13 18V20H11V18H13Z" fill="currentColor"/>
<path d="M8.46447 16.9498L7.05025 15.5355L5.63604 16.9498L7.05025 18.364L8.46447 16.9498Z" fill="currentColor"/>
<path d="M4 13V11H6L6 13H4Z" fill="currentColor"/>
<path d="M7.05025 5.63604L5.63604 7.05025L7.05025 8.46446L8.46447 7.05025L7.05025 5.63604Z" fill="currentColor"/>
<path d="M11 4H13V6H11V4Z" fill="currentColor"/>
<path d="M18.364 7.05025L16.9497 5.63604L15.5355 7.05025L16.9497 8.46447L18.364 7.05025Z" fill="currentColor"/>
<path d="M18 11H20V13H18V11Z" fill="currentColor"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M12 13C12.5523 13 13 12.5523 13 12C13 11.4477 12.5523 11 12 11C11.4477 11 11 11.4477 11 12C11 12.5523 11.4477 13 12 13ZM12 15C13.6569 15 15 13.6569 15 12C15 10.3431 13.6569 9 12 9C10.3431 9 9 10.3431 9 12C9 13.6569 10.3431 15 12 15Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M16.9498 15.5355L15.5355 16.9497L16.9498 18.364L18.364 16.9497L16.9498 15.5355Z" style="fill: var(--element-active-color)"/>
<path d="M13 18V20H11V18H13Z" style="fill: var(--element-active-color)"/>
<path d="M8.46447 16.9498L7.05025 15.5355L5.63604 16.9498L7.05025 18.364L8.46447 16.9498Z" style="fill: var(--element-active-color)"/>
<path d="M4 13V11H6L6 13H4Z" style="fill: var(--element-active-color)"/>
<path d="M7.05025 5.63604L5.63604 7.05025L7.05025 8.46446L8.46447 7.05025L7.05025 5.63604Z" style="fill: var(--element-active-color)"/>
<path d="M11 4H13V6H11V4Z" style="fill: var(--element-active-color)"/>
<path d="M18.364 7.05025L16.9497 5.63604L15.5355 7.05025L16.9497 8.46447L18.364 7.05025Z" style="fill: var(--element-active-color)"/>
<path d="M18 11H20V13H18V11Z" style="fill: var(--element-active-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M12 13C12.5523 13 13 12.5523 13 12C13 11.4477 12.5523 11 12 11C11.4477 11 11 11.4477 11 12C11 12.5523 11.4477 13 12 13ZM12 15C13.6569 15 15 13.6569 15 12C15 10.3431 13.6569 9 12 9C10.3431 9 9 10.3431 9 12C9 13.6569 10.3431 15 12 15Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Gn=(Wn.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Wn);N([P({type:Boolean})],Gn.prototype,`useCssColor`,void 0),Gn=N([M(`obi-display-brilliance-low`)],Gn);var Kn=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M14.8331 9.17621C14.83 9.17312 14.8269 9.17002 14.8238 9.16694C14.1003 8.4458 13.1022 8 12 8C10.8978 8 9.89964 8.44583 9.17615 9.167C9.1731 9.17005 9.17005 9.1731 9.167 9.17615C8.44583 9.89964 8 10.8978 8 12C8 14.2091 9.79086 16 12 16C14.2091 16 16 14.2091 16 12C16 10.8978 15.5542 9.8997 14.8331 9.17621ZM12 14C13.1046 14 14 13.1046 14 12C14 10.8954 13.1046 10 12 10C10.8954 10 10 10.8954 10 12C10 13.1046 10.8954 14 12 14ZM18.364 4.22182L19.7782 5.63604L16.9497 8.46447L16.237 7.75175L15.5355 7.05025L18.364 4.22182ZM4.22183 5.63604L5.63605 4.22183L8.46447 7.05025L7.76316 7.75157L7.75175 7.76298L7.05026 8.46447L4.22183 5.63604ZM7.05025 15.5355L8.46446 16.9498L5.63603 19.7782L4.22182 18.364L7.05025 15.5355ZM16.9498 15.5355L19.7782 18.364L18.364 19.7782L15.5355 16.9497L16.9498 15.5355ZM11 2H13V6H11V2ZM2 13V11H6V13H2ZM13 22H11V18H13V22ZM22 11V13H18V11H22Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M14.8331 9.17621C14.83 9.17312 14.8269 9.17002 14.8238 9.16694C14.1003 8.4458 13.1022 8 12 8C10.8978 8 9.89964 8.44583 9.17615 9.167C9.1731 9.17005 9.17005 9.1731 9.167 9.17615C8.44583 9.89964 8 10.8978 8 12C8 14.2091 9.79086 16 12 16C14.2091 16 16 14.2091 16 12C16 10.8978 15.5542 9.8997 14.8331 9.17621ZM12 14C13.1046 14 14 13.1046 14 12C14 10.8954 13.1046 10 12 10C10.8954 10 10 10.8954 10 12C10 13.1046 10.8954 14 12 14ZM18.364 4.22182L19.7782 5.63604L16.9497 8.46447L16.237 7.75175L15.5355 7.05025L18.364 4.22182ZM4.22183 5.63604L5.63605 4.22183L8.46447 7.05025L7.76316 7.75157L7.75175 7.76298L7.05026 8.46447L4.22183 5.63604ZM7.05025 15.5355L8.46446 16.9498L5.63603 19.7782L4.22182 18.364L7.05025 15.5355ZM16.9498 15.5355L19.7782 18.364L18.364 19.7782L15.5355 16.9497L16.9498 15.5355ZM11 2H13V6H11V2ZM2 13V11H6V13H2ZM13 22H11V18H13V22ZM22 11V13H18V11H22Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},qn=(Kn.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Kn);N([P({type:Boolean})],qn.prototype,`useCssColor`,void 0),qn=N([M(`obi-display-brilliance-proposal`)],qn);var Jn=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M7 15H11V17H7C4.24 17 2 14.76 2 12C2 9.24 4.24 7 7 7H11V9H7C5.35 9 4 10.35 4 12C4 13.65 5.35 15 7 15Z" fill="currentColor"/>
<path d="M13 7H17C19.76 7 22 9.24 22 12C22 14.76 19.76 17 17 17H13V15H17C18.65 15 20 13.65 20 12C20 10.35 18.65 9 17 9H13V7Z" fill="currentColor"/>
<path d="M16 11H8V13H16V11Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M7 15H11V17H7C4.24 17 2 14.76 2 12C2 9.24 4.24 7 7 7H11V9H7C5.35 9 4 10.35 4 12C4 13.65 5.35 15 7 15Z" style="fill: var(--element-active-color)"/>
<path d="M13 7H17C19.76 7 22 9.24 22 12C22 14.76 19.76 17 17 17H13V15H17C18.65 15 20 13.65 20 12C20 10.35 18.65 9 17 9H13V7Z" style="fill: var(--element-active-color)"/>
<path d="M16 11H8V13H16V11Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Yn=(Jn.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Jn);N([P({type:Boolean})],Yn.prototype,`useCssColor`,void 0),Yn=N([M(`obi-link`)],Yn);var Xn=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.4279 2.37775C11.6445 1.87408 12.3555 1.87408 12.5721 2.37776L13.7412 5.09716C13.8901 5.44343 14.3078 5.57976 14.6309 5.38751L17.1681 3.8777C17.638 3.59806 18.2133 4.01786 18.0937 4.55318L17.4482 7.44346C17.366 7.81149 17.6241 8.1684 17.998 8.20361L20.9342 8.48009C21.478 8.5313 21.6978 9.21054 21.2878 9.57303L19.0741 11.5302C18.7923 11.7794 18.7923 12.2206 19.0741 12.4698L21.2878 14.427C21.6978 14.7895 21.478 15.4687 20.9342 15.5199L17.998 15.7964C17.6241 15.8316 17.366 16.1885 17.4482 16.5565L18.0937 19.4468C18.2133 19.9821 17.638 20.4019 17.1681 20.1223L14.6309 18.6125C14.3078 18.4202 13.8901 18.5566 13.7412 18.9028L12.5721 21.6222C12.3555 22.1259 11.6445 22.1259 11.4279 21.6222L10.2588 18.9028C10.1099 18.5566 9.69222 18.4202 9.36914 18.6125L6.83191 20.1223C6.36198 20.4019 5.78673 19.9821 5.9063 19.4468L6.55183 16.5565C6.63403 16.1885 6.37587 15.8316 6.00199 15.7964L3.06579 15.5199C2.52197 15.4687 2.30224 14.7895 2.71224 14.427L4.92587 12.4698C5.20775 12.2206 5.20774 11.7794 4.92587 11.5302L2.71224 9.57303C2.30224 9.21054 2.52197 8.5313 3.0658 8.48009L6.00199 8.20361C6.37587 8.1684 6.63403 7.81149 6.55183 7.44346L5.9063 4.55318C5.78673 4.01786 6.36198 3.59806 6.83191 3.8777L9.36914 5.38751C9.69222 5.57976 10.1099 5.44343 10.2588 5.09716L11.4279 2.37775ZM17 12C17 14.7614 14.7614 17 12 17C9.23858 17 7 14.7614 7 12C7 9.23858 9.23858 7 12 7C14.7614 7 17 9.23858 17 12Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.4279 2.37775C11.6445 1.87408 12.3555 1.87408 12.5721 2.37776L13.7412 5.09716C13.8901 5.44343 14.3078 5.57976 14.6309 5.38751L17.1681 3.8777C17.638 3.59806 18.2133 4.01786 18.0937 4.55318L17.4482 7.44346C17.366 7.81149 17.6241 8.1684 17.998 8.20361L20.9342 8.48009C21.478 8.5313 21.6978 9.21054 21.2878 9.57303L19.0741 11.5302C18.7923 11.7794 18.7923 12.2206 19.0741 12.4698L21.2878 14.427C21.6978 14.7895 21.478 15.4687 20.9342 15.5199L17.998 15.7964C17.6241 15.8316 17.366 16.1885 17.4482 16.5565L18.0937 19.4468C18.2133 19.9821 17.638 20.4019 17.1681 20.1223L14.6309 18.6125C14.3078 18.4202 13.8901 18.5566 13.7412 18.9028L12.5721 21.6222C12.3555 22.1259 11.6445 22.1259 11.4279 21.6222L10.2588 18.9028C10.1099 18.5566 9.69222 18.4202 9.36914 18.6125L6.83191 20.1223C6.36198 20.4019 5.78673 19.9821 5.9063 19.4468L6.55183 16.5565C6.63403 16.1885 6.37587 15.8316 6.00199 15.7964L3.06579 15.5199C2.52197 15.4687 2.30224 14.7895 2.71224 14.427L4.92587 12.4698C5.20775 12.2206 5.20774 11.7794 4.92587 11.5302L2.71224 9.57303C2.30224 9.21054 2.52197 8.5313 3.0658 8.48009L6.00199 8.20361C6.37587 8.1684 6.63403 7.81149 6.55183 7.44346L5.9063 4.55318C5.78673 4.01786 6.36198 3.59806 6.83191 3.8777L9.36914 5.38751C9.69222 5.57976 10.1099 5.44343 10.2588 5.09716L11.4279 2.37775ZM17 12C17 14.7614 14.7614 17 12 17C9.23858 17 7 14.7614 7 12C7 9.23858 9.23858 7 12 7C14.7614 7 17 9.23858 17 12Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Zn=(Xn.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Xn);N([P({type:Boolean})],Zn.prototype,`useCssColor`,void 0),Zn=N([M(`obi-palette-day-bright`)],Zn);var Qn=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M14.4178 2.66892C14.7789 2.25636 15.4554 2.47526 15.5064 3.02113L15.7816 5.96838C15.8166 6.34367 16.1721 6.60197 16.5386 6.51851L19.4174 5.8631C19.9506 5.74171 20.3687 6.3182 20.0902 6.79072L18.5862 9.34191C18.3947 9.66677 18.5305 10.0858 18.8753 10.2344L21.5838 11.4014C22.0855 11.6175 22.0854 12.3314 21.5838 12.5501L19.2437 13.5701C19.9738 14.2507 20.5123 15.1503 20.7626 16.1622C21.9582 16.6967 22.7499 17.9449 22.7499 19.3243C22.7499 21.1817 21.3013 22.75 19.4588 22.75H9.62935C8.73882 22.75 7.89257 22.3876 7.27532 21.7385C6.61858 21.085 6.27173 20.2054 6.25014 19.2667L6.24994 19.2581V19.212C6.24994 18.6736 6.37017 18.152 6.59526 17.6786L4.5824 18.1369C4.04921 18.2582 3.63113 17.6818 3.90968 17.2092L5.41363 14.658C5.60514 14.3332 5.46938 13.9141 5.12449 13.7655L2.41601 12.5986C1.91436 12.3825 1.9144 11.6686 2.41608 11.4499L5.12472 10.2692C5.46962 10.1189 5.60543 9.69915 5.41397 9.37526L3.91034 6.83168C3.63185 6.36057 4.05 5.78196 4.58318 5.90066L7.4619 6.54149C7.82846 6.62309 8.18396 6.36299 8.21905 5.98753L8.49462 3.03888C8.54566 2.49275 9.2222 2.27043 9.58323 2.68116L11.5324 4.89872C11.7807 5.18109 12.2201 5.17998 12.4683 4.89635L14.4178 2.66892ZM8.77567 15.8232C9.0014 15.7627 9.23504 15.7262 9.47374 15.7151C9.91656 15.02 10.6813 14.5702 11.5529 14.5702C11.6374 14.5702 11.7229 14.5744 11.8091 14.5835C12.7056 13.1529 14.2426 12.25 15.947 12.25C16.3039 12.25 16.652 12.29 16.9877 12.3658C17.1542 10.1198 15.7772 7.96694 13.5391 7.2428C10.9118 6.39271 8.09283 7.83343 7.24274 10.4608C6.59862 12.4515 7.26972 14.5523 8.77567 15.8232ZM12.8665 15.771C13.4558 14.5213 14.6481 13.75 15.947 13.75C17.6096 13.75 19.0881 15.057 19.371 16.8409L19.4468 17.3191L19.9138 17.4469C20.6575 17.6504 21.2499 18.4014 21.2499 19.3243C21.2499 20.4233 20.4045 21.25 19.4588 21.25H9.62935C9.14786 21.25 8.69223 21.0546 8.35732 20.6995L8.34813 20.6898L8.3386 20.6804C7.9796 20.326 7.7653 19.8279 7.74994 19.2403V19.212C7.74994 18.6904 7.94322 18.1961 8.2958 17.8083C8.65036 17.419 9.1208 17.2115 9.62936 17.2115C9.73976 17.2115 9.76618 17.213 9.79884 17.2188L10.4228 17.329L10.6357 16.7323C10.7806 16.3265 11.1414 16.0702 11.5529 16.0702C11.6726 16.0702 11.7795 16.0905 11.8851 16.1372L12.5544 16.4329L12.8665 15.771Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M14.4178 2.66892C14.7789 2.25636 15.4554 2.47526 15.5064 3.02113L15.7816 5.96838C15.8166 6.34367 16.1721 6.60197 16.5386 6.51851L19.4174 5.8631C19.9506 5.74171 20.3687 6.3182 20.0902 6.79072L18.5862 9.34191C18.3947 9.66677 18.5305 10.0858 18.8753 10.2344L21.5838 11.4014C22.0855 11.6175 22.0854 12.3314 21.5838 12.5501L19.2437 13.5701C19.9738 14.2507 20.5123 15.1503 20.7626 16.1622C21.9582 16.6967 22.7499 17.9449 22.7499 19.3243C22.7499 21.1817 21.3013 22.75 19.4588 22.75H9.62935C8.73882 22.75 7.89257 22.3876 7.27532 21.7385C6.61858 21.085 6.27173 20.2054 6.25014 19.2667L6.24994 19.2581V19.212C6.24994 18.6736 6.37017 18.152 6.59526 17.6786L4.5824 18.1369C4.04921 18.2582 3.63113 17.6818 3.90968 17.2092L5.41363 14.658C5.60514 14.3332 5.46938 13.9141 5.12449 13.7655L2.41601 12.5986C1.91436 12.3825 1.9144 11.6686 2.41608 11.4499L5.12472 10.2692C5.46962 10.1189 5.60543 9.69915 5.41397 9.37526L3.91034 6.83168C3.63185 6.36057 4.05 5.78196 4.58318 5.90066L7.4619 6.54149C7.82846 6.62309 8.18396 6.36299 8.21905 5.98753L8.49462 3.03888C8.54566 2.49275 9.2222 2.27043 9.58323 2.68116L11.5324 4.89872C11.7807 5.18109 12.2201 5.17998 12.4683 4.89635L14.4178 2.66892ZM8.77567 15.8232C9.0014 15.7627 9.23504 15.7262 9.47374 15.7151C9.91656 15.02 10.6813 14.5702 11.5529 14.5702C11.6374 14.5702 11.7229 14.5744 11.8091 14.5835C12.7056 13.1529 14.2426 12.25 15.947 12.25C16.3039 12.25 16.652 12.29 16.9877 12.3658C17.1542 10.1198 15.7772 7.96694 13.5391 7.2428C10.9118 6.39271 8.09283 7.83343 7.24274 10.4608C6.59862 12.4515 7.26972 14.5523 8.77567 15.8232ZM12.8665 15.771C13.4558 14.5213 14.6481 13.75 15.947 13.75C17.6096 13.75 19.0881 15.057 19.371 16.8409L19.4468 17.3191L19.9138 17.4469C20.6575 17.6504 21.2499 18.4014 21.2499 19.3243C21.2499 20.4233 20.4045 21.25 19.4588 21.25H9.62935C9.14786 21.25 8.69223 21.0546 8.35732 20.6995L8.34813 20.6898L8.3386 20.6804C7.9796 20.326 7.7653 19.8279 7.74994 19.2403V19.212C7.74994 18.6904 7.94322 18.1961 8.2958 17.8083C8.65036 17.419 9.1208 17.2115 9.62936 17.2115C9.73976 17.2115 9.76618 17.213 9.79884 17.2188L10.4228 17.329L10.6357 16.7323C10.7806 16.3265 11.1414 16.0702 11.5529 16.0702C11.6726 16.0702 11.7795 16.0905 11.8851 16.1372L12.5544 16.4329L12.8665 15.771Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},$n=(Qn.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Qn);N([P({type:Boolean})],$n.prototype,`useCssColor`,void 0),$n=N([M(`obi-palette-day`)],$n);var er=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.5529 3.75275C11.7695 3.24908 12.4805 3.24908 12.6971 3.75276L13.8662 6.47216C14.0151 6.81843 14.4328 6.95476 14.7559 6.76251L17.2931 5.2527C17.763 4.97306 18.3383 5.39286 18.2187 5.92818L17.5732 8.81846C17.491 9.18649 17.7491 9.5434 18.123 9.57861L21.0592 9.85509C21.603 9.9063 21.8228 10.5855 21.4128 10.948L19.1991 12.9052C19.1278 12.9683 19.0745 13.0436 19.0393 13.125H21C21.4142 13.125 21.75 13.4608 21.75 13.875C21.75 14.2892 21.4142 14.625 21 14.625H3C2.58579 14.625 2.25 14.2892 2.25 13.875C2.25 13.4608 2.58579 13.125 3 13.125H5.21069C5.17546 13.0436 5.12219 12.9683 5.05087 12.9052L2.83724 10.948C2.42724 10.5855 2.64697 9.9063 3.1908 9.85509L6.12699 9.57861C6.50087 9.5434 6.75903 9.18649 6.67683 8.81846L6.0313 5.92818C5.91173 5.39286 6.48698 4.97306 6.95691 5.2527L9.49414 6.76251C9.81722 6.95476 10.2349 6.81843 10.3838 6.47216L11.5529 3.75275ZM7.13114 13.125H17.1189C16.9886 10.4797 14.8026 8.375 12.125 8.375C9.44741 8.375 7.2614 10.4797 7.13114 13.125Z" fill="currentColor"/>
<path d="M7.5 15.75C7.08579 15.75 6.75 16.0858 6.75 16.5C6.75 16.9142 7.08579 17.25 7.5 17.25H16.5C16.9142 17.25 17.25 16.9142 17.25 16.5C17.25 16.0858 16.9142 15.75 16.5 15.75H7.5Z" fill="currentColor"/>
<path d="M13.875 19.25C13.875 19.6642 13.5392 20 13.125 20H12H10.875C10.4608 20 10.125 19.6642 10.125 19.25C10.125 18.8358 10.4608 18.5 10.875 18.5H12H13.125C13.5392 18.5 13.875 18.8358 13.875 19.25Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M11.5529 3.75275C11.7695 3.24908 12.4805 3.24908 12.6971 3.75276L13.8662 6.47216C14.0151 6.81843 14.4328 6.95476 14.7559 6.76251L17.2931 5.2527C17.763 4.97306 18.3383 5.39286 18.2187 5.92818L17.5732 8.81846C17.491 9.18649 17.7491 9.5434 18.123 9.57861L21.0592 9.85509C21.603 9.9063 21.8228 10.5855 21.4128 10.948L19.1991 12.9052C19.1278 12.9683 19.0745 13.0436 19.0393 13.125H21C21.4142 13.125 21.75 13.4608 21.75 13.875C21.75 14.2892 21.4142 14.625 21 14.625H3C2.58579 14.625 2.25 14.2892 2.25 13.875C2.25 13.4608 2.58579 13.125 3 13.125H5.21069C5.17546 13.0436 5.12219 12.9683 5.05087 12.9052L2.83724 10.948C2.42724 10.5855 2.64697 9.9063 3.1908 9.85509L6.12699 9.57861C6.50087 9.5434 6.75903 9.18649 6.67683 8.81846L6.0313 5.92818C5.91173 5.39286 6.48698 4.97306 6.95691 5.2527L9.49414 6.76251C9.81722 6.95476 10.2349 6.81843 10.3838 6.47216L11.5529 3.75275ZM7.13114 13.125H17.1189C16.9886 10.4797 14.8026 8.375 12.125 8.375C9.44741 8.375 7.2614 10.4797 7.13114 13.125Z" style="fill: var(--element-active-color)"/>
<path d="M7.5 15.75C7.08579 15.75 6.75 16.0858 6.75 16.5C6.75 16.9142 7.08579 17.25 7.5 17.25H16.5C16.9142 17.25 17.25 16.9142 17.25 16.5C17.25 16.0858 16.9142 15.75 16.5 15.75H7.5Z" style="fill: var(--element-active-color)"/>
<path d="M13.875 19.25C13.875 19.6642 13.5392 20 13.125 20H12H10.875C10.4608 20 10.125 19.6642 10.125 19.25C10.125 18.8358 10.4608 18.5 10.875 18.5H12H13.125C13.5392 18.5 13.875 18.8358 13.875 19.25Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},tr=(er.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,er);N([P({type:Boolean})],tr.prototype,`useCssColor`,void 0),tr=N([M(`obi-palette-dusk`)],tr);var nr=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M12 21C9.5 21 7.375 20.125 5.625 18.375C3.875 16.625 3 14.5 3 12C3 9.5 3.875 7.375 5.625 5.625C7.375 3.875 9.5 3 12 3C12.2333 3 12.4625 3.00833 12.6875 3.025C12.9125 3.04167 13.1333 3.06667 13.35 3.1C12.6667 3.58333 12.1208 4.2125 11.7125 4.9875C11.3042 5.7625 11.1 6.6 11.1 7.5C11.1 9 11.625 10.275 12.675 11.325C13.725 12.375 15 12.9 16.5 12.9C17.4167 12.9 18.2583 12.6958 19.025 12.2875C19.7917 11.8792 20.4167 11.3333 20.9 10.65C20.9333 10.8667 20.9583 11.0875 20.975 11.3125C20.9917 11.5375 21 11.7667 21 12C21 14.5 20.125 16.625 18.375 18.375C16.625 20.125 14.5 21 12 21ZM12 19C13.4667 19 14.7833 18.5958 15.95 17.7875C17.1167 16.9792 17.9667 15.925 18.5 14.625C18.1667 14.7083 17.8333 14.775 17.5 14.825C17.1667 14.875 16.8333 14.9 16.5 14.9C14.45 14.9 12.7042 14.1792 11.2625 12.7375C9.82083 11.2958 9.1 9.55 9.1 7.5C9.1 7.16667 9.125 6.83333 9.175 6.5C9.225 6.16667 9.29167 5.83333 9.375 5.5C8.075 6.03333 7.02083 6.88333 6.2125 8.05C5.40417 9.21667 5 10.5333 5 12C5 13.9333 5.68333 15.5833 7.05 16.95C8.41667 18.3167 10.0667 19 12 19Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12 21C9.5 21 7.375 20.125 5.625 18.375C3.875 16.625 3 14.5 3 12C3 9.5 3.875 7.375 5.625 5.625C7.375 3.875 9.5 3 12 3C12.2333 3 12.4625 3.00833 12.6875 3.025C12.9125 3.04167 13.1333 3.06667 13.35 3.1C12.6667 3.58333 12.1208 4.2125 11.7125 4.9875C11.3042 5.7625 11.1 6.6 11.1 7.5C11.1 9 11.625 10.275 12.675 11.325C13.725 12.375 15 12.9 16.5 12.9C17.4167 12.9 18.2583 12.6958 19.025 12.2875C19.7917 11.8792 20.4167 11.3333 20.9 10.65C20.9333 10.8667 20.9583 11.0875 20.975 11.3125C20.9917 11.5375 21 11.7667 21 12C21 14.5 20.125 16.625 18.375 18.375C16.625 20.125 14.5 21 12 21ZM12 19C13.4667 19 14.7833 18.5958 15.95 17.7875C17.1167 16.9792 17.9667 15.925 18.5 14.625C18.1667 14.7083 17.8333 14.775 17.5 14.825C17.1667 14.875 16.8333 14.9 16.5 14.9C14.45 14.9 12.7042 14.1792 11.2625 12.7375C9.82083 11.2958 9.1 9.55 9.1 7.5C9.1 7.16667 9.125 6.83333 9.175 6.5C9.225 6.16667 9.29167 5.83333 9.375 5.5C8.075 6.03333 7.02083 6.88333 6.2125 8.05C5.40417 9.21667 5 10.5333 5 12C5 13.9333 5.68333 15.5833 7.05 16.95C8.41667 18.3167 10.0667 19 12 19Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},rr=(nr.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,nr);N([P({type:Boolean})],rr.prototype,`useCssColor`,void 0),rr=N([M(`obi-palette-night`)],rr);var ir=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M20 3H4C2.9 3 2 3.9 2 5V15C2 16.1 2.9 17 4 17H10V19H8V21H16V19H14V17H20C21.1 17 22 16.1 22 15V5C22 3.9 21.1 3 20 3ZM4 15H20V5H4V15Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M20 3H4C2.9 3 2 3.9 2 5V15C2 16.1 2.9 17 4 17H10V19H8V21H16V19H14V17H20C21.1 17 22 16.1 22 15V5C22 3.9 21.1 3 20 3ZM4 15H20V5H4V15Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},ar=(ir.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,ir);N([P({type:Boolean})],ar.prototype,`useCssColor`,void 0),ar=N([M(`obi-screen-desk`)],ar);function or(e){e.stopPropagation()}var sr=o`* {
  -webkit-tap-highlight-color: transparent;
}

.wrapper {
  padding: 0;
  user-select: none;
  background: transparent;
  height: var(--ui-components-button-touch-target-size);
  min-width: var(--ui-components-button-touch-target-size);
  appearance: none;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  font-feature-settings:
    "liga" off,
    "clig" off;
  font-family: var(--font-family-main);
  font-size: var(--global-typography-ui-button-font-size);
  font-style: normal;
  font-weight: var(--global-typography-ui-button-font-weight);
  line-height: var(--global-typography-ui-button-line-height) /* 150% */;
  text-decoration: none;
}

.wrapper.full-width {
    width: 100%;
  }

.wrapper.full-width .visible-wrapper {
      width: 100%;
    }

.wrapper .visible-wrapper {
    border-radius: var(--ui-components-button-border-radius-top-left)
      var(--ui-components-button-border-radius-top-right)
      var(--ui-components-button-border-radius-bottom-right)
      var(--ui-components-button-border-radius-bottom-left);
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
    padding-left: calc(2 * var(--ui-components-button-padding-horizontal));
    padding-right: calc(2 * var(--ui-components-button-padding-horizontal));
    height: var(--ui-components-button-visual-size);
  }

.wrapper .icon {
    height: var(--ui-components-button-icon-size);
    width: var(--ui-components-button-icon-size);
  }

.wrapper:not(.hasIconLeading) .icon.leading {
    display: none;
    width: 0;
  }

.wrapper:not(.hasIconTrailing) .icon.trailing {
    display: none;
    width: 0;
  }

.wrapper .label {
    padding-left: var(--ui-components-button-label-spacing);
    padding-right: var(--ui-components-button-label-spacing);
  }

.wrapper.variant-normal {
  cursor: pointer;
}

.wrapper.variant-normal:focus {
  outline: none;
}

.wrapper.variant-normal .visible-wrapper {
  border-color: var(--normal-enabled-border-color);
  background-color: var(--normal-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--normal-enabled-border-color);
  --base-background-color: var(--normal-enabled-background-color);
}

.wrapper.variant-normal.activated .visible-wrapper {
  border-color: var(--normal-activated-border-color);
  background-color: var(--normal-activated-background-color);
  --base-border-color: var(--normal-activated-border-color);
  --base-background-color: var(--normal-activated-background-color);
}

@media (hover:hover) {

.wrapper.variant-normal:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--normal-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--normal-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.variant-normal:active .visible-wrapper {
  border-color: var(--normal-pressed-border-color);
  background-color: var(--normal-pressed-background-color);
}

.wrapper.variant-normal:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.variant-normal:disabled .visible-wrapper {
  border-color: var(--normal-disabled-border-color);
  background-color: var(--normal-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-normal-disabled-color) !important;
}

.wrapper.variant-normal.disabled .visible-wrapper {
  border-color: var(--normal-disabled-border-color);
  background-color: var(--normal-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-normal-disabled-color) !important;
}

.wrapper.variant-normal:disabled {
  cursor: not-allowed;
}

.wrapper.variant-normal.disabled {
  cursor: not-allowed;
}

.wrapper.variant-normal {
    color: var(--on-normal-active-color);
}

.wrapper.variant-normal .icon {
      color: var(--on-normal-neutral-color);
    }

.wrapper.variant-normal:disabled .icon {
      color: var(--on-normal-disabled-color);
    }

.wrapper.variant-flat {
  cursor: pointer;
}

.wrapper.variant-flat:focus {
  outline: none;
}

.wrapper.variant-flat .visible-wrapper {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.wrapper.variant-flat.activated .visible-wrapper {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

.wrapper.variant-flat:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.variant-flat:active .visible-wrapper {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

.wrapper.variant-flat:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.variant-flat:disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.variant-flat.disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.variant-flat:disabled {
  cursor: not-allowed;
}

.wrapper.variant-flat.disabled {
  cursor: not-allowed;
}

.wrapper.variant-flat {
    color: var(--on-flat-active-color);
}

.wrapper.variant-flat .icon {
      color: var(--on-flat-neutral-color);
    }

.wrapper.variant-flat:disabled .icon {
      color: var(--on-flat-disabled-color);
    }

.wrapper.variant-raised {
  cursor: pointer;
}

.wrapper.variant-raised:focus {
  outline: none;
}

.wrapper.variant-raised .visible-wrapper {
  border-color: var(--raised-enabled-border-color);
  background-color: var(--raised-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--raised-enabled-border-color);
  --base-background-color: var(--raised-enabled-background-color);
}

.wrapper.variant-raised.activated .visible-wrapper {
  border-color: var(--raised-activated-border-color);
  background-color: var(--raised-activated-background-color);
  --base-border-color: var(--raised-activated-border-color);
  --base-background-color: var(--raised-activated-background-color);
}

@media (hover:hover) {

.wrapper.variant-raised:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--raised-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--raised-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.variant-raised:active .visible-wrapper {
  border-color: var(--raised-pressed-border-color);
  background-color: var(--raised-pressed-background-color);
}

.wrapper.variant-raised:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.variant-raised:disabled .visible-wrapper {
  border-color: var(--raised-disabled-border-color);
  background-color: var(--raised-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-raised-disabled-color) !important;
}

.wrapper.variant-raised.disabled .visible-wrapper {
  border-color: var(--raised-disabled-border-color);
  background-color: var(--raised-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-raised-disabled-color) !important;
}

.wrapper.variant-raised:disabled {
  cursor: not-allowed;
}

.wrapper.variant-raised.disabled {
  cursor: not-allowed;
}

.wrapper.variant-raised {
    color: var(--on-raised-active-color);
}

.wrapper.variant-raised .icon {
      color: var(--on-raised-neutral-color);
    }

.wrapper.variant-raised:disabled .icon {
      color: var(--on-raised-disabled-color);
    }

.wrapper.segment-position-start {
    margin-right: -1px;
  }

.wrapper.segment-position-start .visible-wrapper {
      border-top-right-radius: 0;
      border-bottom-right-radius: 0;
    }

.wrapper.segment-position-middle .visible-wrapper {
    border-radius: 0;
  }

.wrapper.segment-position-end .visible-wrapper {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
  }

:host:has(.segment-position-start),
:host:has(.segment-position-middle) {
  margin-right: -0.5px;
}

:host:has(.segment-position-middle),
:host:has(.segment-position-end) {
  margin-left: -0.5px;
}
`,cr=class extends j{constructor(...e){super(...e),this.variant=`normal`,this.fullWidth=!1,this.disabled=!1,this.showLeadingIcon=!1,this.showTrailingIcon=!1,this.href=void 0,this.target=void 0,this.segmentPosition=`single`}renderLeadingIcon(){return this.showLeadingIcon?L`
        <span class="icon leading" part="icon leading">
          <slot name="leading-icon"></slot>
        </span>
      `:L``}renderTrailingIcon(){return this.showTrailingIcon?L`
        <span class="icon trailing" part="icon trailing">
          <slot name="trailing-icon"></slot>
        </span>
      `:L``}render(){let e=this.href?Ot`a`:Ot`button`;return L`
      <${e}
        class=${F({wrapper:!0,[`variant-`+this.variant]:!0,hasIconLeading:this.showLeadingIcon,hasIconTrailing:this.showTrailingIcon,"full-width":this.fullWidth,[`segment-position-`+this.segmentPosition]:!0})}
        ?disabled=${this.disabled}
        href=${I(this.href)}
        target=${I(this.target)}
        part="wrapper"
      >
        <div class="visible-wrapper" part="visible-wrapper">
          ${this.renderLeadingIcon()}
          <span class="label" part="label">
            <slot></slot>
          </span>
          ${this.renderTrailingIcon()}
        </div>
      </${e}>
    `}},lr=(cr.styles=a(sr),cr);N([P({type:String})],lr.prototype,`variant`,void 0),N([P({type:Boolean,reflect:!0})],lr.prototype,`fullWidth`,void 0),N([P({type:Boolean})],lr.prototype,`disabled`,void 0),N([P({type:Boolean})],lr.prototype,`showLeadingIcon`,void 0),N([P({type:Boolean})],lr.prototype,`showTrailingIcon`,void 0),N([P({type:String})],lr.prototype,`href`,void 0),N([P({type:String})],lr.prototype,`target`,void 0),N([P({type:String})],lr.prototype,`segmentPosition`,void 0),lr=N([M(`obc-button`)],lr);var ur=o`* {
  -webkit-tap-highlight-color: transparent;
}

* {
  box-sizing: border-box;
}

.wrapper {
  display: flex;
  user-select: none;
  min-width: var(--ui-components-user-button-touch-target-size);
  min-height: var(--ui-components-app-button-touch-target-size);
  width: fit-content;
  padding: var(--ui-components-user-button-padding-vertical) 0px;
  margin: 0;
  appearance: none;
  justify-content: center;
  align-items: center;
  border-radius: var(--ui-components-user-button-border-radius-container);
  border: none;
  background: transparent;
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-body-font-weight);
  font-size: var(--global-typography-ui-body-font-size);
  line-height: var(--global-typography-ui-body-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
}

.wrapper.size-large {
    min-width: var(--ui-components-user-button-touch-target-size-enhanced);
    min-height: var(--ui-components-user-button-touch-target-size-enhanced);
    padding: var(--ui-components-user-button-padding-vertical-enhanced) 0px;
  }

.wrapper.size-large .user-button-circle {
      width: var(--ui-components-user-button-visual-size-enhanced);
      height: var(--ui-components-user-button-visual-size-enhanced);
    }

.wrapper.size-large .icon-container {
      width: var(--ui-components-user-button-icon-size-enhanced);
      height: var(--ui-components-user-button-icon-size-enhanced);
    }

.wrapper.size-large .user-initials {
      font-family: var(--global-typography-font-family);
      font-weight: var(--font-weight-regular);
      font-size: var(--font-size-150);
      line-height: var(--line-height-150);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    }

.wrapper.size-large .user-label {
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-body-font-weight);
      font-size: var(--global-typography-ui-body-font-size);
      line-height: var(--global-typography-ui-body-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    }

.wrapper.size-large .user-sublabel {
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-body-font-weight);
      font-size: var(--global-typography-ui-body-font-size);
      line-height: var(--global-typography-ui-body-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    }

.wrapper.size-large.has-sublabel .user-label {
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-body-active-font-weight);
      font-size: var(--global-typography-ui-body-active-font-size);
      line-height: var(--global-typography-ui-body-active-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    }

.wrapper.size-large.style-selected .user-initials {
      font-family: var(--global-typography-font-family);
      font-weight: var(--font-weight-bold);
      font-size: var(--global-typography-ui-title-font-size);
      line-height: var(--global-typography-ui-title-line-height);
      letter-spacing: var(--global-typography-ui-title-letter-spacing);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    }

.wrapper.size-large.style-selected .user-label {
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-body-active-font-weight);
      font-size: var(--global-typography-ui-body-active-font-size);
      line-height: var(--global-typography-ui-body-active-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    }

.wrapper.size-large.state-static {
      width: var(--ui-components-user-button-visual-size-enhanced);
      height: var(--ui-components-user-button-visual-size-enhanced);
      min-width: unset;
      min-height: unset;
      padding: 0;
      margin: 0;
    }

.wrapper .user-label {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-label-font-weight);
    font-size: var(--global-typography-ui-label-font-size);
    line-height: var(--global-typography-ui-label-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    color: var(--element-active-color);
  }

.wrapper .user-sublabel {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-label-font-weight);
    font-size: var(--global-typography-ui-label-font-size);
    line-height: var(--global-typography-ui-label-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    color: var(--element-active-color);
  }

.wrapper.has-sublabel .user-label {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-label-active-font-weight);
    font-size: var(--global-typography-ui-label-active-font-size);
    line-height: var(--global-typography-ui-label-active-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  }

.wrapper:disabled .user-label,.wrapper:disabled .user-sublabel {
    color: var(--element-disabled-color);
  }

.wrapper .user-button-circle {
    display: flex;
    width: var(--ui-components-user-button-visual-size);
    height: var(--ui-components-user-button-visual-size);
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-radius: 100px;
  }

.wrapper.state-static {
    width: var(--ui-components-user-button-visual-size);
    height: var(--ui-components-user-button-visual-size);
    min-width: unset;
    min-height: unset;
    padding: 0;
    margin: 0;
  }

.wrapper.style-flat {
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-body-active-font-weight);
  font-size: var(--global-typography-ui-body-active-font-size);
  line-height: var(--global-typography-ui-body-active-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
}

.wrapper.style-flat:not(.state-static) {
  cursor: pointer;
}

.wrapper.style-flat:not(.state-static):focus {
  outline: none;
}

.wrapper.style-flat:not(.state-static) .user-button-circle {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.wrapper.style-flat.activated:not(.state-static) .user-button-circle {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

.wrapper.style-flat:not(.state-static):hover .user-button-circle {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.style-flat:not(.state-static):active .user-button-circle {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

.wrapper.style-flat:not(.state-static):focus-visible .user-button-circle {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.style-flat:not(.state-static):disabled .user-button-circle {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.style-flat.disabled:not(.state-static) .user-button-circle {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.style-flat:not(.state-static):disabled {
  cursor: not-allowed;
}

.wrapper.style-flat.disabled:not(.state-static) {
  cursor: not-allowed;
}

.wrapper.style-flat .user-icon {
    color: var(--on-flat-neutral-color);
  }

.wrapper.style-flat .user-button-circle {
    border-radius: var(--ui-components-button-border-radius-top-left)
      var(--ui-components-button-border-radius-top-right)
      var(--ui-components-button-border-radius-bottom-right)
      var(--ui-components-button-border-radius-bottom-left);
    color: var(--on-flat-neutral-color);
  }

.wrapper.style-normal:not(.state-static) {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.wrapper.style-normal:not(.state-static):focus {
  outline: none;
}

.wrapper.style-normal.activated:not(.state-static) {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

.wrapper.style-normal:not(.state-static):hover {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.style-normal:not(.state-static):active {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

.wrapper.style-normal:not(.state-static):focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.style-normal:not(.state-static):disabled {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.style-normal.disabled:not(.state-static) {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.style-normal .user-button-circle {
    border: 1px solid var(--normal-enabled-border-color);
    background: var(--normal-enabled-background-color);
    color: var(--on-normal-neutral-color);
  }

.wrapper.style-normal.mode-initials .user-button-circle {
    color: var(--element-neutral-color);
  }

.wrapper.style-normal.mode-initials:disabled .user-button-circle {
    color: var(--element-disabled-color);
    background-color: var(--normal-disabled-background-color);
    border-color: var(--normal-disabled-border-color);
  }

.wrapper.style-normal.mode-icon:disabled .user-button-circle {
    color: var(--on-normal-disabled-color);
    background-color: var(--normal-disabled-background-color);
    border-color: var(--normal-disabled-border-color);
  }

.wrapper.style-selected {
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-body-active-font-weight);
  font-size: var(--global-typography-ui-body-active-font-size);
  line-height: var(--global-typography-ui-body-active-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
}

.wrapper.style-selected:not(.state-static) {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.wrapper.style-selected:not(.state-static):focus {
  outline: none;
}

.wrapper.style-selected.activated:not(.state-static) {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

.wrapper.style-selected:not(.state-static):hover {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.style-selected:not(.state-static):active {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

.wrapper.style-selected:not(.state-static):focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.style-selected:not(.state-static):disabled {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.style-selected.disabled:not(.state-static) {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.style-selected .user-button-circle {
    color: var(--on-selected-active-color);
    border: 1px solid var(--selected-enabled-border-color);
    background: var(--selected-enabled-background-color);
  }

.wrapper.style-selected .user-label {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-label-active-font-weight);
    font-size: var(--global-typography-ui-label-active-font-size);
    line-height: var(--global-typography-ui-label-active-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  }

.wrapper.style-selected:disabled .user-button-circle {
    color: var(--on-selected-disabled-color);
    background-color: var(--selected-disabled-background-color);
    border-color: var(--selected-disabled-border-color);
  }

.content-container {
  display: flex;
  justify-content: center;
  align-items: center;
  align-self: stretch;
  flex-direction: column;
}

.icon-container {
  width: var(--ui-components-user-button-icon-size);
  height: var(--ui-components-user-button-icon-size);
  flex-shrink: 0;
}

.chip-icon-wrapper ::slotted(*) {
  width: 100%;
  height: 100%;
  flex-shrink: 0;
}
`,dr=class extends j{constructor(...e){super(...e),this.variant=`icon`,this.size=`regular`,this.styleType=`flat`,this.static=!1,this.disabled=!1,this.initials=``}get formattedInitials(){if(!this.initials)return``;let e=this.initials.replace(/\s+/g,``).toUpperCase(),t=this.size===`large`?3:2;return e.length>t?(console.warn(`Initials "${this.initials}" are longer than ${t} characters.`),e.slice(0,t)):e}get shouldShowIcon(){return this.variant===`icon`}render(){let e=this.size===`large`&&this.styleType===`flat`?`normal`:this.styleType,t={wrapper:!0,"wrapper-static":this.static,[`style-${e}`]:!0,"mode-icon":this.shouldShowIcon,"mode-initials":!this.shouldShowIcon,"state-static":this.static,[`size-${this.size}`]:!0,"has-sublabel":!!this.sublabel&&!this.static},n=this.static?Ot`div`:Ot`button`,r=[this.label,this.sublabel].filter(Boolean).join(`, `),i=!this.static&&r||this.initials||`User button`,a=this.label&&!this.static?L`<span class="user-label" part="label">${this.label}</span>`:A,o=this.sublabel&&!this.static?L`<span class="user-sublabel" part="sublabel">
            ${this.sublabel}
          </span>`:A;return L`
        <${n}
          class=${F(t)}
          ?disabled=${this.disabled}
          aria-label=${i}
        >
        <div class="content-container" part="content-container">
          <div class="user-button-circle">
            ${this.shouldShowIcon?L`
                    <div class="icon-container">
                      <slot name="icon">
                        <!-- Fallback to default icon if no slot content -->
                        <obi-user></obi-user>
                      </slot>
                    </div>
                  `:L`
                    <span class="user-initials">
                      ${this.formattedInitials}
                    </span>
                  `}
          </div>
          ${a} ${o}
        </div>
        </${n}>
      `}},fr=(dr.styles=a(ur),dr);N([P({type:String})],fr.prototype,`variant`,void 0),N([P({type:String})],fr.prototype,`size`,void 0),N([P({type:String})],fr.prototype,`styleType`,void 0),N([P({type:Boolean})],fr.prototype,`static`,void 0),N([P({type:Boolean})],fr.prototype,`disabled`,void 0),N([P({type:String})],fr.prototype,`initials`,void 0),N([P({type:String})],fr.prototype,`label`,void 0),N([P({type:String})],fr.prototype,`sublabel`,void 0),fr=N([M(`obc-user-button`)],fr);var pr=o`* {
  -webkit-tap-highlight-color: transparent;
}

* {
  box-sizing: border-box;
}

:host {
  display: inline-block;
}

.wrapper {
  width: 100%;
  display: inline-flex;
  min-width: var(--ui-components-app-button-touch-target-size-enhanced);
  min-height: var(--ui-components-app-button-touch-target-size-enhanced);
  padding: var(--ui-components-app-button-padding-vertical-enhanced) 0px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: var(--ui-components-app-button-border-radius-container);
  border-width: 0 !important;
}

.wrapper {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.wrapper:focus {
  outline: none;
}

.wrapper.activated {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

.wrapper:hover {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper:active {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

.wrapper:focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper:disabled {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.disabled {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

:is(.wrapper .icon-wrapper) {
  border-color: var(--normal-enabled-border-color);
  background-color: var(--normal-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  --base-border-color: var(--normal-enabled-border-color);
  --base-background-color: var(--normal-enabled-background-color);
}

.wrapper .icon-wrapper {
    color: var(--on-normal-neutral-color);

    width: var(--ui-components-app-button-visual-size-enhanced);
    height: var(--ui-components-app-button-visual-size-enhanced);
    border-radius: var(--ui-components-app-button-border-radius-large);

    display: flex;

    align-items: center;
    justify-content: center;
  }

:is(.wrapper .icon-wrapper) .icon {
      width: var(--ui-components-app-button-icon-size-enhanced);
      height: var(--ui-components-app-button-icon-size-enhanced);
    }

.wrapper .label {
    color: var(--element-active-color);
    text-align: center;
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-label-font-weight);
    font-size: var(--global-typography-ui-label-font-size);
    line-height: var(--global-typography-ui-label-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;

    /* Checking a button switches this label to bold, which is wider. Reserving
     * that width in every state keeps a row of app buttons sized from its
     * labels from resizing as the selection moves (#1212). */
  }

:is(.wrapper .label) .label-width-reserve {
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-label-active-font-weight);
      font-size: var(--global-typography-ui-label-active-font-size);
      line-height: var(--global-typography-ui-label-active-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
      display: block;
      /* Contributes width to the parent without occupying a visible box. */
      height: 0;
      overflow: hidden;
      visibility: hidden;
    }

.wrapper.small {
    min-width: var(--ui-components-app-button-touch-target-size);
    min-height: var(--ui-components-app-button-touch-target-size);
    padding: var(--ui-components-app-button-padding-vertical) 0px;
  }

.wrapper.small .icon-wrapper {
      width: var(--ui-components-app-button-visual-size);
      height: var(--ui-components-app-button-visual-size);
      border-radius: var(--ui-components-app-button-border-radius-small);
    }

.wrapper.small .icon {
      width: var(--ui-components-app-button-icon-size);
      height: var(--ui-components-app-button-icon-size);
    }

:is(.wrapper.checked .icon-wrapper) {
  border-color: var(--selected-enabled-border-color);
  background-color: var(--selected-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--selected-enabled-border-color);
  --base-background-color: var(--selected-enabled-background-color);
}

:is(.wrapper.checked .icon-wrapper):focus {
  outline: none;
}

.activated:is(.wrapper.checked .icon-wrapper) {
  border-color: var(--selected-activated-border-color);
  background-color: var(--selected-activated-background-color);
  --base-border-color: var(--selected-activated-border-color);
  --base-background-color: var(--selected-activated-background-color);
}

@media (hover:hover) {

:is(.wrapper.checked .icon-wrapper):hover {
    border-color: color-mix(in srgb, var(--selected-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--selected-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

:is(.wrapper.checked .icon-wrapper):active {
  border-color: var(--selected-pressed-border-color);
  background-color: var(--selected-pressed-background-color);
}

:is(.wrapper.checked .icon-wrapper):focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

:is(.wrapper.checked .icon-wrapper):disabled {
  border-color: var(--selected-disabled-border-color);
  background-color: var(--selected-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-selected-disabled-color) !important;
}

.disabled:is(.wrapper.checked .icon-wrapper) {
  border-color: var(--selected-disabled-border-color);
  background-color: var(--selected-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-selected-disabled-color) !important;
}

.wrapper.checked .icon-wrapper {
      color: var(--on-selected-active-color);
    }

.wrapper.checked .label {
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-label-active-font-weight);
      font-size: var(--global-typography-ui-label-active-font-size);
      line-height: var(--global-typography-ui-label-active-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    }

.wrapper.integration {
  border-color: var(--integration-flat-enabled-border-color);
  background-color: var(--integration-flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--integration-flat-enabled-border-color);
  --base-background-color: var(--integration-flat-enabled-background-color);
}

.wrapper.integration:focus {
  outline: none;
}

.wrapper.integration.activated {
  border-color: var(--integration-flat-activated-border-color);
  background-color: var(--integration-flat-activated-background-color);
  --base-border-color: var(--integration-flat-activated-border-color);
  --base-background-color: var(--integration-flat-activated-background-color);
}

@media (hover:hover) {

.wrapper.integration:hover {
    border-color: color-mix(in srgb, var(--integration-flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--integration-flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.integration:active {
  border-color: var(--integration-flat-pressed-border-color);
  background-color: var(--integration-flat-pressed-background-color);
}

.wrapper.integration:focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.integration:disabled {
  border-color: var(--integration-flat-disabled-border-color);
  background-color: var(--integration-flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--integration-on-flat-disabled-color) !important;
}

.wrapper.integration.disabled {
  border-color: var(--integration-flat-disabled-border-color);
  background-color: var(--integration-flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--integration-on-flat-disabled-color) !important;
}

:is(.wrapper.integration .icon-wrapper) {
  border-color: var(--integration-normal-enabled-border-color);
  background-color: var(--integration-normal-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  --base-border-color: var(--integration-normal-enabled-border-color);
  --base-background-color: var(--integration-normal-enabled-background-color);
}

.wrapper.integration .icon-wrapper {
      color: var(--integration-on-normal-neutral-color);
    }

.wrapper.integration .label {
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-label-font-weight);
      font-size: var(--global-typography-ui-label-font-size);
      line-height: var(--global-typography-ui-label-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
      color: var(--integration-on-normal-neutral-color);
    }

:is(.wrapper.integration.checked .icon-wrapper) {
  border-color: var(--integration-selected-enabled-border-color);
  background-color: var(--integration-selected-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--integration-selected-enabled-border-color);
  --base-background-color: var(--integration-selected-enabled-background-color);
}

:is(.wrapper.integration.checked .icon-wrapper):focus {
  outline: none;
}

.activated:is(.wrapper.integration.checked .icon-wrapper) {
  border-color: var(--integration-selected-activated-border-color);
  background-color: var(--integration-selected-activated-background-color);
  --base-border-color: var(--integration-selected-activated-border-color);
  --base-background-color: var(--integration-selected-activated-background-color);
}

@media (hover:hover) {

:is(.wrapper.integration.checked .icon-wrapper):hover {
    border-color: color-mix(in srgb, var(--integration-selected-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--integration-selected-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

:is(.wrapper.integration.checked .icon-wrapper):active {
  border-color: var(--integration-selected-pressed-border-color);
  background-color: var(--integration-selected-pressed-background-color);
}

:is(.wrapper.integration.checked .icon-wrapper):focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

:is(.wrapper.integration.checked .icon-wrapper):disabled {
  border-color: var(--integration-selected-disabled-border-color);
  background-color: var(--integration-selected-disabled-background-color);
  cursor: not-allowed;
  color: var(--integration-on-selected-disabled-color) !important;
}

.disabled:is(.wrapper.integration.checked .icon-wrapper) {
  border-color: var(--integration-selected-disabled-border-color);
  background-color: var(--integration-selected-disabled-background-color);
  cursor: not-allowed;
  color: var(--integration-on-selected-disabled-color) !important;
}

.wrapper.integration.checked .icon-wrapper {
      color: var(--integration-on-selected-active-color);
    }

.wrapper.integration.checked .label {
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-label-active-font-weight);
      font-size: var(--global-typography-ui-label-active-font-size);
      line-height: var(--global-typography-ui-label-active-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
      color: var(--integration-element-active-color);
    }

.wrapper.disabled {
    cursor: not-allowed;
  }

.wrapper.disabled .icon-wrapper {
      color: var(--element-disabled-color);
    }

.wrapper.disabled .label {
      color: var(--element-disabled-color);
    }

.wrapper.checked.disabled .icon-wrapper {
    background-color: var(--selected-disabled-background-color);
    border-color: var(--selected-disabled-border-color);
    color: var(--on-selected-disabled-color);
  }

.wrapper.integration.disabled .icon-wrapper {
      color: var(--element-disabled-color);
    }

.wrapper.integration.disabled .label {
      color: var(--element-disabled-color);
    }
`,mr=class extends j{constructor(...e){super(...e),this.label=`Button`,this.checked=!1,this.showLabel=!0,this.integration=!1,this.size=`normal`,this.disabled=!1}render(){return O` <button
      class="${F({wrapper:!0,checked:this.checked,small:this.size===`small`,integration:this.integration,disabled:this.disabled})}"
      ?disabled=${this.disabled}
    >
      <div class="icon-wrapper">
        <span class="icon">
          <slot name="icon"></slot>
        </span>
      </div>
      ${this.showLabel?O`<div class="label">
              ${this.label}<span class="label-width-reserve" aria-hidden="true"
                >${this.label}</span
              >
            </div>`:A}
    </button>`}},hr=(mr.styles=a(pr),mr);N([P({type:String})],hr.prototype,`label`,void 0),N([P({type:Boolean})],hr.prototype,`checked`,void 0),N([P({type:Boolean,attribute:!1})],hr.prototype,`showLabel`,void 0),N([P({type:Boolean})],hr.prototype,`integration`,void 0),N([P({type:String})],hr.prototype,`size`,void 0),N([P({type:Boolean})],hr.prototype,`disabled`,void 0),hr=N([M(`obc-app-button`)],hr);var gr=o`* {
  -webkit-tap-highlight-color: transparent;
}

* {
  box-sizing: border-box;
}

:host {
  --_thumb-size: 48px;
  --_thumb-half: 24px;

  display: flex;
  align-items: center;
  justify-content: center;
  height: var(--_thumb-size);

  color: var(--element-neutral-color, #1a1a1a);
}

:host([hugcontainer]) {
  margin-left: -12px;
  margin-right: -12px;
}

.wrapper {
  flex: 1;
  height: var(--_thumb-size);
  position: relative;
}

.wrapper.disabled {
    cursor: not-allowed;
    pointer-events: none;
  }

.wrapper.disabled .track::after {
    background: var(--flat-disabled-background-color);
  }

.wrapper.disabled.enhanced .track {
    background: var(--indent-disabled-background-color);
  }

.wrapper.disabled.enhanced .track::after {
    background: var(--indent-disabled-background-color);
  }

.wrapper.disabled .interactive-track {
    background: var(--selected-disabled-background-color);
    border-color: var(--selected-disabled-background-color);
  }

.wrapper.disabled .thumb {
    background: var(--selected-disabled-background-color);
    border-color: var(--normal-disabled-border-color);
  }

.wrapper.disabled.enhanced .thumb {
    border-color: var(--selected-disabled-border-color);
    background: var(--container-background-color);
  }

.slider {
  position: absolute;
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: var(--_thumb-size);
  margin: 0;
  padding: 0;
  background: none;
}

.slider::-webkit-slider-container {
  position: absolute;
  margin: auto 0;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  height: 40px;
  border-radius: 6px;
  cursor: pointer;
}

.no-input :is(.slider::-webkit-slider-container) {
    cursor: default;
  }

.slider::-moz-range-track {
  position: absolute;
  margin: auto 0;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  height: 40px;
  border-radius: 6px;
  cursor: pointer;
  background: transparent;
  border: none;
}

.no-input :is(.slider::-moz-range-track) {
    cursor: default;
  }

.container-hover {
  position: absolute;
  left: calc(
    var(--_ratio, 0) * (100% - var(--_thumb-size)) + var(--_thumb-size)
  );
  top: 0;
  bottom: 0;
  right: 0;
  cursor: pointer;
}

.no-input .container-hover {
    cursor: default;
  }

.track {
  position: absolute;
  -webkit-appearance: none;
  appearance: none;
  margin: auto 0;
  padding: 0;
  top: 0;
  bottom: 0;
  left: 18px;
  right: 18px;
  height: 4px;
  border-radius: 6px;
  background: var(--border-outline-color);
}

.track::after {
    content: "";
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background: var(--flat-enabled-background-color);
    border-radius: 6px;
  }

.enhanced .track {
  height: 32px;
  background: var(--indent-enabled-background-color);
  border: 1px solid var(--indent-enabled-border-color);
}

.normal .track:has(~ .container-hover:hover)::after,
.normal .track:has(~ input:hover)::after {
  background: var(--flat-hover-background-color);
}

.enhanced .track:has(~ .container-hover:hover)::after,
.enhanced .track:has(~ input:hover)::after {
  background-color: var(--indent-hover-background-color);
  border-color: var(--indent-hover-border-color);
}

.normal .track:has(~ .container-hover:active)::after,
.normal .track:has(~ input:active)::after {
  background: var(--flat-pressed-background-color);
}

.enhanced .track:has(~ .container-hover:active)::after,
.enhanced .track:has(~ input:active)::after {
  background-color: var(--indent-pressed-background-color);
  border-color: var(--indent-pressed-border-color);
}

.interactive-track-hover {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  right: calc(
    (1 - var(--_ratio, 0)) * (100% - var(--_thumb-size)) + var(--_thumb-size)
  );
  cursor: pointer;
}

.no-input .interactive-track-hover {
    cursor: default;
  }

.interactive-track {
  position: absolute;
  left: 18px;
  top: 0;
  bottom: 0;
  height: 4px;
  border-radius: 6px;
  right: calc(
    100% - var(--_ratio, 0) * (100% - var(--_thumb-size)) - var(--_thumb-half)
  );
  margin-top: auto;
  margin-bottom: auto;
  background: var(--selected-enabled-background-color);
  border-color: var(--selected-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  pointer-events: none;
}

.enhanced .interactive-track {
  height: 32px;
  right: calc(100% - var(--_ratio, 0) * (100% - var(--_thumb-size)) - 30px);
}

.interactive-track-hover:hover ~ .interactive-track,
input:hover ~ .interactive-track {
  background: var(--selected-hover-background-color);
  border-color: var(--selected-hover-background-color);
}

.interactive-track-hover:active ~ .interactive-track,
input:active ~ .interactive-track {
  background: var(--selected-pressed-background-color);
  border-color: var(--selected-pressed-background-color);
}

/** slider thumb */
input::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  margin: 0;
  padding: 0;
  width: var(--_thumb-size);
  height: var(--_thumb-size);
  background: transparent;
  cursor: grab;
}

input::-moz-range-thumb {
  appearance: none;
  margin: 0;
  padding: 0;
  width: var(--_thumb-size);
  height: var(--_thumb-size);
  background: transparent;
  border: none;
  cursor: grab;
}

.no-input input::-webkit-slider-thumb {
  cursor: default;
}

.no-input input::-moz-range-thumb {
  cursor: default;
}

input:active::-webkit-slider-thumb {
  cursor: grabbing;
}

input:active::-moz-range-thumb {
  cursor: grabbing;
}

.no-input input:active::-webkit-slider-thumb {
  cursor: default;
}

.no-input input:active::-moz-range-thumb {
  cursor: default;
}

.thumb {
  position: absolute;
  top: 0;
  left: calc(var(--_ratio, 0) * (100% - var(--_thumb-size)));
  right: calc((1 - var(--_ratio, 0)) * (100% - var(--_thumb-size)));
  bottom: 0;
  border-radius: 6px;
  border-width: 2px;
  height: 28px;
  width: 12px;
  margin: auto;
  border-style: solid;
  border-color: var(--container-background-color);
  background: var(--selected-enabled-background-color);
  pointer-events: none;
}

:host:has(.no-input) {
  height: 24px;
  margin-left: -8px;
  margin-right: -8px;
}

.no-input .thumb {
    height: 12px;
    width: 12px;
  }

.enhanced .thumb {
  border-width: 4px;
  height: 32px;
  border-color: var(--selected-enabled-background-color);
  background: var(--container-background-color);
}

input:hover ~ .thumb {
  background: var(--selected-hover-background-color);
}

.enhanced input:hover ~ .thumb {
  border-color: var(--selected-hover-background-color);
  background: var(--container-background-color);
}

input:active ~ .thumb {
  background: var(--selected-pressed-background-color);
}

.enhanced input:active ~ .thumb {
  border-color: var(--selected-pressed-background-color);
  background: var(--container-background-color);
}
`,_r=`important`,vr=` !`+_r,yr=pt(class extends mt{constructor(e){if(super(e),e.type!==ft.ATTRIBUTE||e.name!==`style`||e.strings?.length>2)throw Error("The `styleMap` directive must be used in the `style` attribute and must be the only part in the attribute.")}render(e){return Object.keys(e).reduce((t,n)=>{let r=e[n];return r==null?t:t+`${n=n.includes(`-`)?n:n.replace(/(?:^(webkit|moz|ms|o)|)(?=[A-Z])/g,`-$&`).toLowerCase()}:${r};`},``)}update(e,[t]){let{style:n}=e.element;if(this.ft===void 0)return this.ft=new Set(Object.keys(t)),this.render(t);for(let e of this.ft)t[e]??(this.ft.delete(e),e.includes(`-`)?n.removeProperty(e):n[e]=null);for(let e in t){let r=t[e];if(r!=null){this.ft.add(e);let t=typeof r==`string`&&r.endsWith(vr);e.includes(`-`)||t?n.setProperty(e,t?r.slice(0,-11):r,t?_r:``):n[e]=r}}return ve}}),br,xr=function(e){return e.Normal=`normal`,e.Enhanced=`enhanced`,e.NoInput=`no-input`,e}({}),Sr=(br=class extends j{constructor(...e){super(...e),this.value=50,this.min=0,this.max=100,this.stepClick=10,this.variant=`normal`,this.hasLeftIcon=!1,this.hasRightIcon=!1,this.decrementLabel=`Decrease`,this.incrementLabel=`Increase`,this.allowSeeking=!1,this.seekingSpeed=1/3,this.disabled=!1,this.animationFrame=null,this.isMouseDown=!1,this.isTouchActive=!1,this.targetValue=0,this.isDragging=!1,this.animationStartTime=null,this.animationStartValue=0,this.onWindowMouseMove=e=>{this.onMouseMove(e)},this.onWindowMouseUp=()=>{this.onMouseUp()},this.onWindowTouchMove=e=>{this.onTouchMove(e)},this.onWindowTouchEnd=()=>{this.onTouchEnd()}}get ratio(){let e=this.max-this.min;if(!Number.isFinite(e)||e<=0)return 0;let t=(this.value-this.min)/e;return Number.isFinite(t)?st(t,0,1):0}onInput(e){this.value=e,this.dispatchEvent(new CustomEvent(`value`,{detail:this.value}))}fireChangeEvent(){this.dispatchEvent(new CustomEvent(`change`,{detail:this.value}))}onReduceClick(){this.disabled||(this.onInput(Math.max(this.value-this.stepClick,this.min)),this.fireChangeEvent())}onIncreaseClick(){this.disabled||(this.onInput(Math.min(this.value+this.stepClick,this.max)),this.fireChangeEvent())}get slider(){return this.renderRoot.querySelector(`input[type="range"]`)}isClickingThumb(e){let t=this.slider.getBoundingClientRect(),n=t.left+24+(t.width-48)*this.ratio,r;return r=`touches`in e?e.touches[0].clientX:e.clientX,Math.abs(r-n)<=24}onMouseDown(e){this.variant===`no-input`||this.disabled||this.isClickingThumb(e)||(this.isMouseDown=!0,this.updateTargetValue(e),e.preventDefault(),window.addEventListener(`mousemove`,this.onWindowMouseMove),window.addEventListener(`mouseup`,this.onWindowMouseUp),this.startAnimation())}onTouchStart(e){this.variant===`no-input`||this.disabled||this.isClickingThumb(e)||(this.isTouchActive=!0,this.updateTargetValue(e),e.preventDefault(),window.addEventListener(`touchmove`,this.onWindowTouchMove,{passive:!1}),window.addEventListener(`touchend`,this.onWindowTouchEnd),this.startAnimation())}onMouseMove(e){this.isMouseDown&&this.updateTargetValue(e)}onTouchMove(e){this.isTouchActive&&this.updateTargetValue(e)}onMouseUp(){this.isMouseDown=!1,window.removeEventListener(`mousemove`,this.onWindowMouseMove),window.removeEventListener(`mouseup`,this.onWindowMouseUp),this.stopAnimation(),this.fireChangeEvent()}onTouchEnd(){this.isTouchActive=!1,window.removeEventListener(`touchmove`,this.onWindowTouchMove),window.removeEventListener(`touchend`,this.onWindowTouchEnd),this.stopAnimation(),this.fireChangeEvent()}updateTargetValue(e){let t=this.slider.getBoundingClientRect(),n=t.left+24,r=t.width-48,i=((e instanceof MouseEvent?e.clientX:e.touches[0].clientX)-n)/r,a=parseFloat(this.slider.min),o=a+(parseFloat(this.slider.max)-a)*i;this.targetValue=this.step?Math.round(o/this.step)*this.step:o}startAnimation(){this.isDragging=this.allowSeeking,this.animationStartTime=performance.now(),this.animationStartValue=parseFloat(this.slider.value);let e=parseFloat(this.slider.min),t=parseFloat(this.slider.max),n=this.step,r=1/this.seekingSpeed*1e3,i=this.targetValue>this.animationStartValue?1:-1,a=()=>{let o=this.targetValue;if(!this.isDragging){let a=performance.now(),s=a-(this.animationStartTime??a),c=Math.abs(t-e),l=Math.min(s/r,1),u=this.animationStartValue+i*c*l;i>0?(o=n===void 0?u:Math.ceil((u-e)/n)*n+e,o=Math.min(this.targetValue,o)):(o=n===void 0?u:Math.floor((u-e)/n)*n+e,o=Math.max(this.targetValue,o))}parseFloat(this.slider.value)!==o&&(this.slider.value=String(o),this.slider.dispatchEvent(new Event(`input`))),i>0&&o<this.targetValue||i<0&&o>this.targetValue?this.animationFrame=requestAnimationFrame(a):(this.isMouseDown||this.isTouchActive)&&(this.animationStartTime=performance.now(),this.animationStartValue=parseFloat(this.slider.value),this.animationFrame=requestAnimationFrame(a),this.isDragging=!0)};this.animationFrame=requestAnimationFrame(a)}stopAnimation(){this.animationFrame!==null&&(cancelAnimationFrame(this.animationFrame),this.animationFrame=null)}render(){return O`
      ${this.hasLeftIcon?O` <obc-icon-button
              ?disabled=${this.disabled}
              aria-label=${this.decrementLabel}
              @click=${this.onReduceClick}
              variant="normal"
            >
              <slot name="icon-left"></slot>
            </obc-icon-button>`:null}
      <div
        class=${F({wrapper:!0,[this.variant]:!0,disabled:this.disabled})}
        style=${yr({"--_ratio":String(this.ratio)})}
      >
        <div class="track"></div>
        <input
          type="range"
          min=${this.min}
          max=${this.max}
          step=${I(this.step)}
          .value=${this.value.toString()}
          ?disabled=${this.variant===`no-input`||this.disabled}
          class="slider"
          @input=${e=>{this.value=Number(e.target.value),this.dispatchEvent(new CustomEvent(`value`,{detail:this.value}))}}
          @change=${()=>{this.fireChangeEvent()}}
          @mousedown=${this.onMouseDown}
          @touchstart=${this.onTouchStart}
          @mousemove=${this.onMouseMove}
          @touchmove=${this.onTouchMove}
          @mouseup=${this.onMouseUp}
          @touchend=${this.onTouchEnd}
        />
        <div
          class="interactive-track-hover"
          @mousedown=${this.onMouseDown}
          @touchstart=${this.onTouchStart}
          @mousemove=${this.onMouseMove}
          @touchmove=${this.onTouchMove}
          @mouseup=${this.onMouseUp}
          @touchend=${this.onTouchEnd}
        ></div>
        <div
          class="container-hover"
          @mousedown=${this.onMouseDown}
          @touchstart=${this.onTouchStart}
          @mousemove=${this.onMouseMove}
          @touchmove=${this.onTouchMove}
          @mouseup=${this.onMouseUp}
          @touchend=${this.onTouchEnd}
        ></div>
        <div class="interactive-track"></div>
        <div class="thumb"></div>
      </div>
      ${this.hasRightIcon?O`<obc-icon-button
              ?disabled=${this.disabled}
              aria-label=${this.incrementLabel}
              @click=${this.onIncreaseClick}
              variant="normal"
            >
              <slot name="icon-right"></slot>
            </obc-icon-button>`:null}
    `}},br.styles=a(gr),br);N([P({type:Number})],Sr.prototype,`value`,void 0),N([P({type:Number})],Sr.prototype,`min`,void 0),N([P({type:Number})],Sr.prototype,`max`,void 0),N([P({type:Number})],Sr.prototype,`step`,void 0),N([P({type:Number})],Sr.prototype,`stepClick`,void 0),N([P({type:String})],Sr.prototype,`variant`,void 0),N([P({type:Boolean})],Sr.prototype,`hasLeftIcon`,void 0),N([P({type:Boolean})],Sr.prototype,`hasRightIcon`,void 0),N([P({type:String})],Sr.prototype,`decrementLabel`,void 0),N([P({type:String})],Sr.prototype,`incrementLabel`,void 0),N([P({type:Boolean})],Sr.prototype,`allowSeeking`,void 0),N([P({type:Number})],Sr.prototype,`seekingSpeed`,void 0),N([P({type:Boolean})],Sr.prototype,`disabled`,void 0),Sr=N([M(`obc-slider`)],Sr);var Cr=o`* {
    -webkit-tap-highlight-color: transparent;
}

:host([popover]) {
    /* The browser pins a popover to all four edges and lets the automatic
       margins centre it. Unpinning drops it back where it would normally sit,
       for the consumer to position from. */
    inset: auto;
    margin: 0;

    padding: 0;
    border: none;
    background: none;
    color: inherit;

    /* The menus scroll their own content. */
    overflow: visible;

    /* The browser shrink-wraps a popover to its contents. */
    width: auto;
    height: auto;
  }

* {
  box-sizing: border-box;
}

.card {
  border-radius: 8px;
  background: var(--container-global-color, #fcfcfc);
  /* Shadow/Floating */
  box-shadow: var(--shadow-floating);
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  width: 320px;
  user-select: none;
}

.card.tabbed {
  overflow: hidden;
}

.title-container {
  padding: var(--app-components-system-menu-margin-vertical)
    calc(
      var(--app-components-system-menu-margin-horizontal) +
        var(--app-components-system-menu-padding-horizontal)
    );
}

.title-container h3 {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-overline-font-weight);
    font-size: var(--global-typography-ui-overline-font-size);
    line-height: var(--global-typography-ui-overline-line-height);
    letter-spacing: var(--global-typography-ui-overline-letter-spacing);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    color: var(--element-neutral-color, rgba(0, 0, 0, 0.59));
    margin: 0;
  }

.card.normal .palette .value-label-container {
  padding-top: 0 !important;
}

.content-container {
  padding: var(--app-components-system-menu-padding-vertical)
    var(--app-components-system-menu-margin-vertical);
}

.content-container.palette {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

.content-container.palette.without-link {
      padding-bottom: 24px;
    }

.content-container.palette .value-label-container {
      padding-bottom: 0 !important;
    }

.content-container .value-container {
    display: flex;
    padding: var(--app-components-system-menu-padding-vertical) 0;
    flex-direction: column;
    align-items: center;
    align-self: stretch;
  }

:is(.content-container .value-container) .value-label-container {
      display: flex;
      padding: var(--app-components-system-menu-padding-vertical) 0;
      justify-content: center;
      align-items: center;
      gap: var(--app-components-dimming-menu-label-spacing);
      align-self: stretch;
    }

:is(:is(.content-container .value-container) .value-label-container) .icon {
        width: var(--app-components-dimming-menu-icon-size);
        height: var(--app-components-dimming-menu-icon-size);
        color: var(--instrument-enhanced-secondary-color);
      }

:is(:is(.content-container .value-container) .value-label-container) .label-container {
        display: flex;
        align-items: baseline;
        font-family: var(--global-typography-font-family);
        font-weight: var(
    --global-typography-instrument-value-large-font-weight-active
  );
        font-size: var(--global-typography-instrument-value-large-font-size);
        line-height: var(--global-typography-instrument-value-large-line-height);
        letter-spacing: var(
    --global-typography-instrument-value-large-letter-spacing
  );
        font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
        transition: width 0.1s ease-in-out;
      }

:is(:is(:is(.content-container .value-container) .value-label-container) .label-container) .value {
          color: var(--element-active-color);
        }

:is(:is(:is(.content-container .value-container) .value-label-container) .label-container) .unit {
          font-family: var(--global-typography-font-family);
          font-size: var(--global-typography-instrument-label-font-size);
          line-height: var(--global-typography-instrument-label-line-height);
          font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
          color: var(--element-neutral-color);
        }

:is(.content-container .value-container) .value-slider-container {
      width: 100%;
    }

.content-container .icon-button-container {
    display: flex;
    flex-direction: row;
    padding: 0 var(--app-components-system-menu-padding-horizontal);
  }

:is(.content-container .icon-button-container) > obc-button {
      width: 100%;
      display: block;
      z-index: 1;
    }

.disabled:is(:is(.content-container .icon-button-container) > obc-button) {
        z-index: 0;
      }

:is(.content-container .icon-button-container) .btn-icon {
      color: var(--on-normal-neutral-color);
    }

:is(.content-container .icon-button-container) .disabled .btn-icon {
      color: var(--on-normal-disabled-color);
    }

.palette obc-button::part(visible-wrapper) {
  height: 100%;
}

.divider {
  height: 1px;
  align-self: stretch;
  background: var(--border-divider-color);
}

.footer {
  padding: var(--app-components-dimming-menu-padding-vertical)
    var(--app-components-dimming-menu-margin-horizontal);

  padding-top: calc(var(--app-components-dimming-menu-padding-vertical) - 1px);

  border-top: 1px solid var(--border-divider-color);
}

.footer obc-user-button {
    height: auto;
    width: auto;
  }
`,wr=o`* {
  -webkit-tap-highlight-color: transparent;
}

label {
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  height: var(--ui-components-toggle-switch-item-touch-target-size-two-story);
  padding: 0px var(--ui-components-toggle-switch-item-padding-horizontal);
  flex: 1 0 0;

  color: var(--element-active-color);
  cursor: pointer;
  user-select: none;
}

label.has-description .icon-label-container {
    display: flex;
    align-items: center;
    flex: 1 0 0;
  }

label .label {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-body-font-weight);
    font-size: var(--global-typography-ui-body-font-size);
    line-height: var(--global-typography-ui-body-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  }

label .description {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-label-font-weight);
    font-size: var(--global-typography-ui-label-font-size);
    line-height: var(--global-typography-ui-label-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 1;
    color: var(--element-neutral-color);
    overflow: hidden;
  }

label .icon-label-container {
    display: flex;
    align-items: center;
    flex: 1 0 0;
  }

label .label-container {
    display: flex;
    padding: 0px var(--ui-components-toggle-switch-item-label-spacing);
    align-items: center;
    flex: 1 0 0;
  }

label.has-description .label-container {
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
  }

label .presenter {
    box-sizing: border-box;
    width: var(--ui-components-toggle-switch-selection-width);
    height: var(--ui-components-toggle-switch-selection-height);
    padding: 0px var(--ui-components-toggle-switch-selection-padding);
    flex-shrink: 0;
    border-radius: var(--ui-components-toggle-switch-item-border-radius);

    background: var(--indent-enabled-background-color, rgba(0, 0, 0, 0.05));
    border: solid 1px var(--element-inactive-color, rgba(0, 0, 0, 0.42));
    user-select: none;

    display: flex;
    position: relative;
    align-items: center;

    /* Add transition for smooth background and border color changes */
    transition:
      background-color 0.3s ease,
      border-color 0.3s ease,
      box-shadow 0.15s ease;
  }

:is(label .presenter):hover {
      background: var(--indent-hover-background-color, rgba(0, 0, 0, 0.1));
    }

:is(label .presenter):active {
      background: var(--indent-pressed-background-color, rgba(0, 0, 0, 0.16));
    }

:is(label .presenter):has(:focus-visible) {
      /* Remove the original border when focused */
      border: 1px solid transparent;

      /* Ensure the focus styling works with the proper border radius */
      border-radius: var(
        --global-border-radius-border-radius-round,
        var(--ui-components-toggle-switch-item-border-radius)
      );

      /* Create the double border effect with proper spacing */
      box-shadow: 
        /* Inner border (1px) */
        0 0 0 1px var(--container-global-color, #fff),
        /* Outer border (variable width) */ 0 0 0
          calc(1px + var(--global-size-spacing-border-weight-focusframe, 2px))
          var(--border-focus-color, #007bff);

      /* Remove default outline */
      outline: none;

      /* Ensure the element is positioned to accommodate the box-shadow */
      position: relative;
      z-index: 1;
    }

label.disabled * {
    color: var(--element-disabled-color);
    cursor: not-allowed;
  }

label.disabled {
    cursor: not-allowed;
  }

:is(label.disabled .presenter) {
  border-color: var(--disabled-enabled-border-color);
  background-color: var(--disabled-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--disabled-enabled-border-color);
  --base-background-color: var(--disabled-enabled-background-color);
}

:is(label.disabled .presenter):focus {
  outline: none;
}

.activated:is(label.disabled .presenter) {
  border-color: var(--disabled-activated-border-color);
  background-color: var(--disabled-activated-background-color);
  --base-border-color: var(--disabled-activated-border-color);
  --base-background-color: var(--disabled-activated-background-color);
}

@media (hover:hover) {

:is(label.disabled .presenter):hover {
    border-color: color-mix(in srgb, var(--disabled-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--disabled-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

:is(label.disabled .presenter):active {
  border-color: var(--disabled-pressed-border-color);
  background-color: var(--disabled-pressed-background-color);
}

:is(label.disabled .presenter):focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

:is(label.disabled .presenter):disabled {
  border-color: var(--disabled-disabled-border-color);
  background-color: var(--disabled-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-disabled-disabled-color) !important;
}

.disabled:is(label.disabled .presenter) {
  border-color: var(--disabled-disabled-border-color);
  background-color: var(--disabled-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-disabled-disabled-color) !important;
}

label.disabled .knob {
      background-color: var(--element-disabled-color);
    }

label.checked .label {
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-body-active-font-weight);
      font-size: var(--global-typography-ui-body-active-font-size);
      line-height: var(--global-typography-ui-body-active-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    }

:is(label.checked .presenter) {
  border-color: var(--selected-enabled-border-color);
  background-color: var(--selected-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--selected-enabled-border-color);
  --base-background-color: var(--selected-enabled-background-color);
}

:is(label.checked .presenter):focus {
  outline: none;
}

.activated:is(label.checked .presenter) {
  border-color: var(--selected-activated-border-color);
  background-color: var(--selected-activated-background-color);
  --base-border-color: var(--selected-activated-border-color);
  --base-background-color: var(--selected-activated-background-color);
}

@media (hover:hover) {

:is(label.checked .presenter):hover {
    border-color: color-mix(in srgb, var(--selected-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--selected-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

:is(label.checked .presenter):active {
  border-color: var(--selected-pressed-border-color);
  background-color: var(--selected-pressed-background-color);
}

:is(label.checked .presenter):focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

:is(label.checked .presenter):disabled {
  border-color: var(--selected-disabled-border-color);
  background-color: var(--selected-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-selected-disabled-color) !important;
}

.disabled:is(label.checked .presenter) {
  border-color: var(--selected-disabled-border-color);
  background-color: var(--selected-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-selected-disabled-color) !important;
}

label.checked.disabled .presenter {
        border-color: var(--selected-disabled-border-color);
        background-color: var(--selected-disabled-background-color);
        cursor: not-allowed;
      }

label.checked.disabled .knob {
        background-color: var(--on-selected-disabled-color);
      }

.icon-container {
  width: var(--ui-components-toggle-switch-item-icon-size);
  height: var(--ui-components-toggle-switch-item-icon-size);
  color: var(--element-neutral-color);
}

.switch {
  padding: var(--global-size-spacing-border-weight-focusframe, 2px);
  overflow: visible;
}

input {
  position: absolute;
  height: var(--ui-components-toggle-switch-touch-target);
  width: var(--ui-components-toggle-switch-selection-width);
  top: 0;
  bottom: 0;
  right: -1px;
  left: -1px;
  opacity: 0;
  margin: auto;
  cursor: pointer;
}

.knob {
  width: var(--ui-components-toggle-switch-thumb-size);
  height: var(--ui-components-toggle-switch-thumb-size);
  flex-shrink: 0;
  fill: var(--on-selected-active-color);
  border-radius: 50%;

  background: var(--element-neutral-color, rgba(0, 0, 0, 0.59));

  /* Add transition for smooth knob movement and color change */
  transition:
    transform 0.3s ease,
    background-color 0.3s ease;
}

.checked .knob {
    background: var(--on-selected-active-color, #fff);
    /* Move knob to the right edge, matching the original flex-end position */
    transform: translateX(
      calc(
        var(--ui-components-toggle-switch-selection-width) -
          var(--ui-components-toggle-switch-thumb-size) -
          (2 * var(--ui-components-toggle-switch-selection-padding))
      )
    );
  }

.bottom-divider {
  width: 100%;
  height: 1px;
  position: absolute;
  bottom: -1px;
  border-radius: 1px;
  background: var(--border-divider-color);
}
`,Tr=class extends j{constructor(...e){super(...e),this.label=`Label`,this.checked=!1,this.disabled=!1,this.hasDescription=!1,this.description=``,this.hasBottomDivider=!1,this.hasIcon=!1,this.externalControl=!1}_tryChange(e){if(this.disabled){e.preventDefault();return}let t=!this.checked;this._userSelectedChecked=t,this.externalControl||(this.checked=t),e.stopPropagation(),this.dispatchEvent(new CustomEvent(`input`,{detail:{checked:t}})),this.externalControl&&(e.target.checked=this.checked)}_fireChangeEvent(e){if(this.disabled){e.preventDefault();return}this.dispatchEvent(new CustomEvent(`change`,{detail:{checked:this._userSelectedChecked??this.checked}}))}render(){return O`
      <label
        class=${F({checked:this.checked,disabled:this.disabled,"has-description":this.hasDescription})}
      >
        <div class="icon-label-container">
          ${this.hasIcon?O`<div class="icon-container">
                  <slot name="icon"></slot>
                </div>`:A}
          <div class="label-container">
            <span class="label">${this.label}</span>
            ${this.hasDescription?O`<span class="description">${this.description}</span>`:A}
          </div>
        </div>
        <div class="switch">
          <div class="presenter ${F({checked:this.checked})}">
            <div class="knob"></div>
            <input
              type="checkbox"
              .checked=${this.checked}
              ?disabled=${this.disabled}
              @input=${this._tryChange}
              @change=${this._fireChangeEvent}
            />
          </div>
        </div>
        ${this.hasBottomDivider?O`<div class="bottom-divider"></div>`:A}
      </label>
    `}},Er=(Tr.styles=a(wr),Tr);N([P({type:String})],Er.prototype,`label`,void 0),N([P({type:Boolean})],Er.prototype,`checked`,void 0),N([P({type:Boolean})],Er.prototype,`disabled`,void 0),N([P({type:Boolean})],Er.prototype,`hasDescription`,void 0),N([P({type:String})],Er.prototype,`description`,void 0),N([P({type:Boolean})],Er.prototype,`hasBottomDivider`,void 0),N([P({type:Boolean})],Er.prototype,`hasIcon`,void 0),N([P({type:Boolean})],Er.prototype,`externalControl`,void 0),Er=N([M(`obc-toggle-switch`)],Er);var Dr=o`* {
  -webkit-tap-highlight-color: transparent;
}

:host {
  flex: 1;
}

.wrapper {
  height: var(--ui-components-button-touch-target-size);
  width: 100%;
  min-width: var(--ui-components-toggle-button-touch-target-size);
  min-height: var(
    --ui-components-toggle-button-toggle-button-item-touch-target-size
  );
  user-select: none;
  padding: 0;
  background: transparent;
  display: flex;
  appearance: none;
  border: none;
  align-items: center;
  justify-content: center;
  position: relative;
}

.wrapper {
  cursor: pointer;
}

.wrapper:focus {
  outline: none;
}

.wrapper .visible-wrapper {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.wrapper.activated .visible-wrapper {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

.wrapper:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper:active .visible-wrapper {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

.wrapper:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper:disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper:disabled {
  cursor: not-allowed;
}

.wrapper.disabled {
  cursor: not-allowed;
}

.wrapper.activated .visible-wrapper {
      background-color: var(--flat-pressed-background-color);
      border-color: var(--flat-pressed-border-color);
    }

.wrapper.type-flat {
    border: none;
  }

.wrapper.hug-text:not(.icon-text-under) .visible-wrapper {
    width: fit-content;
  }

.wrapper.large:not(.icon-text-under) .visible-wrapper {
    height: 100%;
  }

.visible-wrapper {
  box-sizing: border-box;
  display: flex;
  height: var(--ui-components-toggle-button-toggle-button-item-visual-size);
  min-width: var(
    --ui-components-toggle-button-icon-toggle-button-horizontal-item-touch-target-size
  );
  padding: 0px calc(var(--ui-components-check-button-padding-horizontal) * 2);
  border-radius: var(
    --ui-components-toggle-button-toggle-button-item-border-radius
  );
  width: 100%;
  position: relative;
  align-items: center;
  justify-content: center;
}

.icon {
  color: var(--on-flat-neutral-color);
  width: var(--ui-components-toggle-button-toggle-button-item-icon-size);
  height: var(--ui-components-toggle-button-toggle-button-item-icon-size);
}

.label {
  text-wrap: nowrap;
}

.label-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.wrapper.inline-label .label {
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-body-font-weight);
  font-size: var(--global-typography-ui-body-font-size);
  line-height: var(--global-typography-ui-body-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  color: var(--on-flat-active-color);
  padding: 0px
    var(--ui-components-toggle-button-toggle-button-item-label-spacing, 8px);
}

:is(.wrapper.selected.type-regular .visible-wrapper) {
  border-color: var(--selected-enabled-border-color);
  background-color: var(--selected-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--selected-enabled-border-color);
  --base-background-color: var(--selected-enabled-background-color);
}

:is(.wrapper.selected.type-regular .visible-wrapper):focus {
  outline: none;
}

.activated:is(.wrapper.selected.type-regular .visible-wrapper) {
  border-color: var(--selected-activated-border-color);
  background-color: var(--selected-activated-background-color);
  --base-border-color: var(--selected-activated-border-color);
  --base-background-color: var(--selected-activated-background-color);
}

@media (hover:hover) {

:is(.wrapper.selected.type-regular .visible-wrapper):hover {
    border-color: color-mix(in srgb, var(--selected-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--selected-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

:is(.wrapper.selected.type-regular .visible-wrapper):active {
  border-color: var(--selected-pressed-border-color);
  background-color: var(--selected-pressed-background-color);
}

:is(.wrapper.selected.type-regular .visible-wrapper):focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

:is(.wrapper.selected.type-regular .visible-wrapper):disabled {
  border-color: var(--selected-disabled-border-color);
  background-color: var(--selected-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-selected-disabled-color) !important;
}

.disabled:is(.wrapper.selected.type-regular .visible-wrapper) {
  border-color: var(--selected-disabled-border-color);
  background-color: var(--selected-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-selected-disabled-color) !important;
}

.wrapper.selected.type-regular .icon {
    color: var(--on-selected-active-color);
  }

.wrapper.selected.type-regular .label {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-label-active-font-weight);
    font-size: var(--global-typography-ui-label-active-font-size);
    line-height: var(--global-typography-ui-label-active-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  }

.wrapper.selected.type-regular.inline-label .label {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-body-active-font-weight);
    font-size: var(--global-typography-ui-body-active-font-size);
    line-height: var(--global-typography-ui-body-active-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    color: var(--on-selected-active-color);
  }

.wrapper.selected.type-regular.disabled .visible-wrapper {
      border-color: var(--selected-disabled-border-color);
      background-color: var(--selected-disabled-background-color);
      cursor: not-allowed;
    }

.wrapper.selected.type-regular.disabled .icon,.wrapper.selected.type-regular.disabled.inline-label .label {
      color: var(--on-selected-disabled-color);
    }

.wrapper.selected.type-regular.disabled .label {
      color: var(--on-flat-disabled-color);
    }

:is(.wrapper.selected.type-flat .visible-wrapper) {
  border-color: var(--amplified-enabled-border-color);
  background-color: var(--amplified-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--amplified-enabled-border-color);
  --base-background-color: var(--amplified-enabled-background-color);
}

:is(.wrapper.selected.type-flat .visible-wrapper):focus {
  outline: none;
}

.activated:is(.wrapper.selected.type-flat .visible-wrapper) {
  border-color: var(--amplified-activated-border-color);
  background-color: var(--amplified-activated-background-color);
  --base-border-color: var(--amplified-activated-border-color);
  --base-background-color: var(--amplified-activated-background-color);
}

@media (hover:hover) {

:is(.wrapper.selected.type-flat .visible-wrapper):hover {
    border-color: color-mix(in srgb, var(--amplified-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--amplified-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

:is(.wrapper.selected.type-flat .visible-wrapper):active {
  border-color: var(--amplified-pressed-border-color);
  background-color: var(--amplified-pressed-background-color);
}

:is(.wrapper.selected.type-flat .visible-wrapper):focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

:is(.wrapper.selected.type-flat .visible-wrapper):disabled {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

.disabled:is(.wrapper.selected.type-flat .visible-wrapper) {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

.wrapper.selected.type-flat .icon {
    color: var(--on-amplified-active-color);
  }

.wrapper.selected.type-flat .label {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-label-active-font-weight);
    font-size: var(--global-typography-ui-label-active-font-size);
    line-height: var(--global-typography-ui-label-active-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    color: var(--on-amplified-active-color);
  }

.wrapper.selected.type-flat.inline-label .label {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-body-active-font-weight);
    font-size: var(--global-typography-ui-body-active-font-size);
    line-height: var(--global-typography-ui-body-active-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    color: var(--on-amplified-active-color);
  }

.wrapper.selected.type-flat.disabled .visible-wrapper {
      border-color: var(--amplified-disabled-border-color);
      background-color: var(--amplified-disabled-background-color);
      cursor: not-allowed;
    }

.wrapper.selected.type-flat.disabled .icon,.wrapper.selected.type-flat.disabled .label,.wrapper.selected.type-flat.disabled.inline-label .label {
      color: var(--on-amplified-disabled-color);
    }

:is(.wrapper.selected.type-normal .visible-wrapper) {
  border-color: var(--normal-enabled-border-color);
  background-color: var(--normal-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--normal-enabled-border-color);
  --base-background-color: var(--normal-enabled-background-color);
}

:is(.wrapper.selected.type-normal .visible-wrapper):focus {
  outline: none;
}

.activated:is(.wrapper.selected.type-normal .visible-wrapper) {
  border-color: var(--normal-activated-border-color);
  background-color: var(--normal-activated-background-color);
  --base-border-color: var(--normal-activated-border-color);
  --base-background-color: var(--normal-activated-background-color);
}

@media (hover:hover) {

:is(.wrapper.selected.type-normal .visible-wrapper):hover {
    border-color: color-mix(in srgb, var(--normal-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--normal-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

:is(.wrapper.selected.type-normal .visible-wrapper):active {
  border-color: var(--normal-pressed-border-color);
  background-color: var(--normal-pressed-background-color);
}

:is(.wrapper.selected.type-normal .visible-wrapper):focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

:is(.wrapper.selected.type-normal .visible-wrapper):disabled {
  border-color: var(--normal-disabled-border-color);
  background-color: var(--normal-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-normal-disabled-color) !important;
}

.disabled:is(.wrapper.selected.type-normal .visible-wrapper) {
  border-color: var(--normal-disabled-border-color);
  background-color: var(--normal-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-normal-disabled-color) !important;
}

.wrapper.selected.type-normal .icon {
    color: var(--on-normal-neutral-color);
  }

.wrapper.selected.type-normal .label {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-label-active-font-weight);
    font-size: var(--global-typography-ui-label-active-font-size);
    line-height: var(--global-typography-ui-label-active-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    color: var(--on-normal-active-color);
  }

.wrapper.selected.type-normal.inline-label .label {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-body-active-font-weight);
    font-size: var(--global-typography-ui-body-active-font-size);
    line-height: var(--global-typography-ui-body-active-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    color: var(--on-normal-active-color);
  }

.wrapper.selected.type-normal.disabled .visible-wrapper {
      border-color: var(--normal-disabled-border-color);
      background-color: var(--normal-disabled-background-color);
      cursor: not-allowed;
    }

.wrapper.selected.type-normal.disabled .icon,.wrapper.selected.type-normal.disabled .label,.wrapper.selected.type-normal.disabled.inline-label .label {
      color: var(--on-normal-disabled-color);
    }

.wrapper.selected.icon-text-under .label {
  color: var(--element-active-color);
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-label-active-font-weight);
  font-size: var(--global-typography-ui-label-active-font-size);
  line-height: var(--global-typography-ui-label-active-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
}

.wrapper.icon-text-under {
  align-items: flex-start;
  justify-content: flex-start;
  flex-direction: column;
  padding-top: 0;
  height: auto;
  min-height: var(--ui-components-button-touch-target-size);
}

.wrapper.icon-text-under .visible-wrapper {
  margin-top: 0;
  height: var(--ui-components-toggle-button-toggle-button-item-visual-size);
}

.wrapper.icon-text-under .label-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.wrapper.icon-text-under .label {
  color: var(--element-active-color, #1a1a1a);
  text-align: center;
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-label-font-weight);
  font-size: var(--global-typography-ui-label-font-size);
  line-height: var(--global-typography-ui-label-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
}

.wrapper.disabled {
  cursor: not-allowed;
}

.wrapper.disabled .visible-wrapper {
    cursor: not-allowed;
  }

.wrapper.disabled .icon,.wrapper.disabled .label,.wrapper.disabled.inline-label .label,.wrapper.disabled.icon-text-under .label {
    color: var(--on-flat-disabled-color);
  }
`,Or,kr=function(e){return e.icon=`icon`,e.text=`text`,e.iconTextUnder=`icon-text-under`,e.iconText=`text-icon`,e}({}),Ar=function(e){return e.flat=`flat`,e.regular=`regular`,e.normal=`normal`,e}({}),jr=(Or=class extends j{constructor(...e){super(...e),this.value=`value`,this.selected=!1,this.activated=!1,this.type=`text`,this.variant=`regular`,this.hugText=!1,this.showDivider=!0,this.disabled=!1,this.large=!1,this.focusable=!0}focus(e){this.shadowRoot?.querySelector(`button`)?.focus(e)}onClick(e){if(this.disabled){e.preventDefault();return}this.selected||this.dispatchEvent(new CustomEvent(`selected`,{detail:{value:this.value}}))}render(){let e=this.type===`text`||this.type===`text-icon`,t=this.type!==`text`,n=this.type!==`icon`,r=this.type===`icon-text-under`;return O`
      <button
        class=${F({wrapper:!0,selected:this.selected,"inline-label":e,"type-flat":this.variant===`flat`,"type-regular":this.variant===`regular`,"type-normal":this.variant===`normal`,"icon-text-under":r,"hug-text":this.hugText,disabled:this.disabled,activated:this.activated,large:this.large})}
        ?disabled=${this.disabled}
        role="radio"
        aria-checked=${this.selected}
        tabindex=${this.focusable?0:-1}
        @click=${this.onClick}
      >
        <div class="visible-wrapper" part="visible-wrapper">
          ${t?O`<div class="icon" part="icon">
                  <slot name="icon"></slot>
                </div>`:``}
          ${n&&!r?O`<div class="label"><slot></slot></div>`:``}
        </div>
        ${n&&r?O`<div class="label-container">
                <div class="label"><slot></slot></div>
              </div>`:``}
      </button>
    `}},Or.styles=a(Dr),Or);N([P({type:String})],jr.prototype,`value`,void 0),N([P({type:Boolean,reflect:!0})],jr.prototype,`selected`,void 0),N([P({type:Boolean,reflect:!0})],jr.prototype,`activated`,void 0),N([P({type:String})],jr.prototype,`type`,void 0),N([P({type:String})],jr.prototype,`variant`,void 0),N([P({type:Boolean})],jr.prototype,`hugText`,void 0),N([P({type:Boolean,reflect:!0})],jr.prototype,`showDivider`,void 0),N([P({type:Boolean,reflect:!0})],jr.prototype,`disabled`,void 0),N([P({type:Boolean,reflect:!0})],jr.prototype,`large`,void 0),N([P({type:Boolean,attribute:!1})],jr.prototype,`focusable`,void 0),jr=N([M(`obc-toggle-button-option`)],jr);var Mr=o`* {
  -webkit-tap-highlight-color: transparent;
}

:host {
  isolation: isolate;
}

.outer-wrapper {
  box-sizing: border-box;
  width: 100%;
  display: flex;
  align-items: center;
  min-height: var(--ui-components-toggle-button-touch-target-size);
}

.outer-wrapper.hug-text {
    width: fit-content;
  }

.outer-wrapper.icon-text-under .wrapper {
    height: var(--ui-components-toggle-button-toggle-button-item-visual-size);
    align-items: flex-start;
  }

.outer-wrapper.disabled .wrapper {
    background-color: var(--indent-disabled-background-color);
    border-color: var(--indent-disabled-border-color);
  }

.outer-wrapper.large:not(.icon-text-under) .wrapper {
    height: 100%;
  }

.wrapper {
  box-sizing: border-box;
  display: flex;
  position: relative;
  align-items: center;
  height: var(--ui-components-toggle-button-toggle-button-item-visual-size);
  outline: 1px solid var(--indent-enabled-border-color);
  outline-offset: -1px;
  width: 100%;
  background: var(--indent-enabled-background-color);
  flex-shrink: 0;
  border-radius: var(--ui-components-toggle-button-border-radius);
}

.outer-wrapper.flat .wrapper {
  background: none;
  outline: none;
  border: none;
}

.outer-wrapper ::slotted(*:not(:first-child):not([selected]))::before {
    box-sizing: border-box;
    content: "";
    position: absolute;
    top: 0;
    bottom: 0;
    margin-left: -0.5px;
    margin-top: auto;
    margin-bottom: auto;
    z-index: -1;
    display: block;
    width: 1px;
    border-radius: 1px;
    background: var(--border-divider-color);
    height: var(--ui-components-divider-height-small);
    fill: var(--border-divider-color);
  }

.outer-wrapper.icon-text-under {
  padding: 0;
  align-items: flex-start;
}

::slotted(:not([showdivider]))::before {
  content: none !important;
}

.wrapper ::slotted(*) {
  flex: 1;
}
`,Nr=class extends j{constructor(...e){super(...e),this.value=``,this.type=kr.text,this.variant=Ar.regular,this.hugText=!1,this.externalControl=!1,this.allowEmptySelection=!1,this.disabled=!1,this.large=!1,this.ariaLabel=null,this.navigator=new Wt({items:()=>Array.from(this.options),isDisabled:e=>e.disabled,preferred:()=>this.getOptionByValue(this.value)??void 0,setFocusable:(e,t)=>{e.focusable=t},focusItem:e=>{this.externalControl||e.focus()}},{orientation:`both`}),this._originalDisabledStates=new Map}handleKeydown(e){let t=this.navigator.activeItem;if(!this.navigator.handleKeydown(e))return;e.preventDefault();let n=this.navigator.activeItem;n&&(this.externalControl?(this.requestOption(n.value),t&&this.navigator.setActive(t,!1)):this.updateSelection(n.value,!0,!0))}hasAnyEnabledOption(){return!this.disabled&&Array.from(this.options).some(e=>!e.disabled)}canSelectOption(e){if(this.disabled)return!1;let t=this.getOptionByValue(e);return t!==null&&!t.disabled}getOptionByValue(e){return Array.from(this.options).find(t=>t.value===e)||null}getFirstSelectableOption(){return this.disabled?null:Array.from(this.options).find(e=>!e.disabled)||null}updateSelection(e,t=!0,n=!1){let r=this.value;if(!this.hasAnyEnabledOption()){this.options.forEach(e=>{e.selected=e.value===this.value}),this.setNoDivider();return}if(!this.canSelectOption(e)){if(this.value&&this.getOptionByValue(this.value)){this.options.forEach(e=>{e.selected=e.value===this.value}),this.setNoDivider();return}e=this.allowEmptySelection?``:this.getFirstSelectableOption()?.value||``}this.value=e,this.options.forEach(t=>{t.selected=t.value===e}),this.setNoDivider(),t&&r!==e&&this.dispatchEvent(new CustomEvent(`value`,{detail:{value:e,previousValue:r}})),n&&r!==e&&this.dispatchEvent(new CustomEvent(`change`,{detail:{value:e}}))}updateActivated(e){e?this.options.forEach(t=>{t.activated=t.value===e}):this.options.forEach(e=>{e.activated=!1})}setNoDivider(){let e=Array.from(this.options).findIndex(e=>e.selected);if(this.options.forEach(e=>{e.showDivider=!0}),e===-1)return;let t=this.options[e+1];t&&(t.showDivider=!1)}firstUpdated(e){super.firstUpdated(e);let t=Array.from(this.options).map(e=>e.value),n=new Set(t);if(t.length!==n.size&&console.warn(`Toggle button group has duplicate values. This may cause unexpected behavior.`),this.options.forEach(e=>{this._originalDisabledStates.set(e,e.hasAttribute(`disabled`)),e.addEventListener(`selected`,e=>this.handleOptionClick(e)),new MutationObserver(t=>{t.forEach(t=>{t.attributeName===`disabled`&&!e.hasAttribute(`data-group-disabled`)&&(this._originalDisabledStates.set(e,e.hasAttribute(`disabled`)),this.handleOptionDisabledChange())})}).observe(e,{attributes:!0,attributeFilter:[`disabled`]}),e.type=this.type,e.variant=this.variant,e.hugText=this.hugText,e.large=this.large,this.disabled&&(e.setAttribute(`data-group-disabled`,`true`),e.disabled=!0)}),!this.value||!this.getOptionByValue(this.value)){if(this.allowEmptySelection)this.updateSelection(``,!1);else{let e=this.getFirstSelectableOption();e&&this.updateSelection(e.value,!1)}}else this.updateSelection(this.value,!1);this.activated&&this.updateActivated(this.activated)}handleOptionDisabledChange(){if(this.getOptionByValue(this.value)?.disabled&&this.hasAnyEnabledOption()){if(this.allowEmptySelection){this.updateSelection(``);return}let e=this.getFirstSelectableOption();e&&this.updateSelection(e.value)}}handleOptionClick(e){let{value:t}=e.detail;this.externalControl?this.requestOption(t):this.updateSelection(t,!0,!0)}requestOption(e){this.dispatchEvent(new CustomEvent(`value`,{detail:{value:e,previousValue:this.value}})),this.dispatchEvent(new CustomEvent(`change`,{detail:{value:e}}))}willUpdate(e){e.has(`value`)&&this.updateSelection(this.value),e.has(`activated`)&&this.updateActivated(this.activated),(e.has(`type`)||e.has(`variant`)||e.has(`hugText`)||e.has(`large`))&&this.options.forEach(e=>{e.type=this.type,e.variant=this.variant,e.hugText=this.hugText,e.large=this.large}),e.has(`disabled`)&&this.options.forEach(e=>{this.disabled?(e.setAttribute(`data-group-disabled`,`true`),e.disabled=!0):(e.removeAttribute(`data-group-disabled`),e.disabled=this._originalDisabledStates.get(e)||!1)})}updated(e){if(super.updated(e),this.navigator.refresh(),e.has(`value`)){let e=this.getOptionByValue(this.value);e&&!e.disabled&&(this.navigator.setActive(e,!1),this.matches(`:focus-within`)&&e.focus())}if(this.getOptionByValue(this.value)?.disabled&&this.hasAnyEnabledOption()){if(this.allowEmptySelection){this.updateSelection(``);return}let e=this.getFirstSelectableOption();e&&this.updateSelection(e.value)}}render(){return O`
      <div
        class=${F({"outer-wrapper":!0,flat:this.variant===Ar.flat,regular:this.variant===Ar.regular,"hug-text":this.hugText,"icon-text-under":this.type===kr.iconTextUnder,disabled:this.disabled,large:this.large})}
        role="radiogroup"
        aria-label=${I(this.ariaLabel??void 0)}
        @keydown=${this.handleKeydown}
        @focusin=${e=>this.navigator.handleFocusin(e)}
      >
        <div class="wrapper">
          <slot @slotchange=${()=>this.navigator.refresh()}></slot>
        </div>
      </div>
    `}},Pr=(Nr.styles=a(Mr),Nr);N([P({type:String})],Pr.prototype,`value`,void 0),N([P({type:String})],Pr.prototype,`activated`,void 0),N([P({type:String})],Pr.prototype,`type`,void 0),N([P({type:String})],Pr.prototype,`variant`,void 0),N([P({type:Boolean})],Pr.prototype,`hugText`,void 0),N([P({type:Boolean})],Pr.prototype,`externalControl`,void 0),N([P({type:Boolean})],Pr.prototype,`allowEmptySelection`,void 0),N([P({type:Boolean,reflect:!0})],Pr.prototype,`disabled`,void 0),N([P({type:Boolean,reflect:!0})],Pr.prototype,`large`,void 0),N([P({type:String,attribute:`aria-label`})],Pr.prototype,`ariaLabel`,void 0),N([He({selector:`obc-toggle-button-option`})],Pr.prototype,`options`,void 0),Pr=N([M(`obc-toggle-button-group`)],Pr);var Fr=o`* {
  -webkit-tap-highlight-color: transparent;
}
.wrapper {
  display: flex;
  user-select: none;
  padding: 8px;
  flex-direction: column;
  align-items: flex-start;
  gap: 8px;
  flex: 1 0 0;
}
.wrapper.style-fullwidth {
    width: 100%;
  }
.wrapper.style-compact {
    width: fit-content;
  }
.wrapper .content-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    align-self: stretch;
    align-items: center;
    gap: var(--menu-navigation-components-page-indicator-indicator-spacing);
  }
.wrapper .dot {
    width: var(--menu-navigation-components-page-indicator-indicator-size);
    height: var(--menu-navigation-components-page-indicator-indicator-size);
    border-radius: 50%;
  }
.wrapper .dot.state-inactive {
    fill: var(--indent-enabled-background-color);
    background-color: var(--indent-enabled-background-color);
  }
.wrapper .dot.state-active {
    background-color: var(--instrument-enhanced-secondary-color);
    fill: var(--instrument-enhanced-secondary-color);
  }
`,Ir=class extends j{constructor(...e){super(...e),this.totalSteps=5,this.currentStep=1,this.fullwidth=!1}get validCurrentStep(){return st(this.currentStep,1,Math.max(1,this.totalSteps))}get validTotalSteps(){return Math.max(1,this.totalSteps)}renderDots(){let e=[];for(let t=0;t<this.validTotalSteps;t++)e.push(O`
        <div
          class=${F({dot:!0,"state-active":t===this.validCurrentStep-1,"state-inactive":t!==this.validCurrentStep-1})}
        ></div>
      `);return e}render(){return O`
      <div
        class=${F({wrapper:!0,"style-fullwidth":this.fullwidth,"style-compact":!this.fullwidth})}
      >
        <div class="content-container">${this.renderDots()}</div>
      </div>
    `}},Lr=(Ir.styles=a(Fr),Ir);N([P({type:Number})],Lr.prototype,`totalSteps`,void 0),N([P({type:Number})],Lr.prototype,`currentStep`,void 0),N([P({type:Boolean})],Lr.prototype,`fullwidth`,void 0),Lr=N([M(`obc-progress-indicator-dots`)],Lr);var Rr=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M11 7H13V11H17V13H13V17H11V13H7V11H11V7Z" fill="currentColor"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M1.61214 10.516L10.516 1.61214C11.3322 0.795953 12.6678 0.795953 13.484 1.61214L22.3879 10.516C23.204 11.3322 23.204 12.6678 22.3879 13.484L13.484 22.3879C12.6678 23.204 11.3322 23.204 10.516 22.3879L1.61214 13.484C0.795953 12.6678 0.795953 11.3322 1.61214 10.516ZM12 3L3 12L12 21L21 12L12 3Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M11 7H13V11H17V13H13V17H11V13H7V11H11V7Z" style="fill: var(--element-active-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M1.61214 10.516L10.516 1.61214C11.3322 0.795953 12.6678 0.795953 13.484 1.61214L22.3879 10.516C23.204 11.3322 23.204 12.6678 22.3879 13.484L13.484 22.3879C12.6678 23.204 11.3322 23.204 10.516 22.3879L1.61214 13.484C0.795953 12.6678 0.795953 11.3322 1.61214 10.516ZM12 3L3 12L12 21L21 12L12 3Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},zr=(Rr.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Rr);N([P({type:Boolean})],zr.prototype,`useCssColor`,void 0),zr=N([M(`obi-placeholder`)],zr);var Br=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M13 13H19V11H13V5H11V11H5V13H11V19H13V13Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M13 13H19V11H13V5H11V11H5V13H11V19H13V13Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Vr=(Br.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Br);N([P({type:Boolean})],Vr.prototype,`useCssColor`,void 0),Vr=N([M(`obi-up-iec`)],Vr);var Hr=o`* {
  -webkit-tap-highlight-color: transparent;
}

:host {
  display: block;
  flex: 1;
  width: 100%;
}

.wrapper {
  display: flex;
  align-items: center;
  flex-direction: row;
  width: 100%;
}

.tabs {
  display: flex;
  flex: 1 1 auto;
  align-items: center;
  min-width: 0; /* the tabs shrink below their 240px basis, as they did as direct children of .wrapper */
}

.tabs.hug {
  flex: 0 1 auto; /* hugging tabs keep the add button right after the last tab */
}

.add-new-tab {
  flex-shrink: 0;
  box-shadow:
    -1px 0 0 0 var(--border-outline-color),
    0 1px 0 0 var(--border-outline-color);
}

.wrapper obc-tab-item:not([checked]) {
  box-shadow: 0 1px 0 0 var(--border-divider-color);
  background-color: var(--container-section-color);
}

.wrapper obc-icon-button {
  background-color: var(--container-section-color);
}
`,Ur=o`* {
  -webkit-tap-highlight-color: transparent;
}

:host {
  display: flex;
  flex: 1 1 240px;
  min-width: 0;
  box-sizing: border-box;
}

:host([hug]) {
  flex: none;
  width: fit-content;
}

.wrapper {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.wrapper:focus {
  outline: none;
}

.wrapper.activated {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

.wrapper:hover {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper:active {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

.wrapper:focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper:disabled {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.disabled {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper {
  user-select: none;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  height: var(--menu-navigation-components-tab-item-touch-target-size);
  user-select: none;
  box-sizing: border-box;
  width: 100%;
  border: none;
  padding-left: var(--menu-navigation-components-tab-item-padding-horizontal);
  padding-right: var(--menu-navigation-components-tab-item-padding-horizontal);
}

.wrapper.hug:not(.has-close) {
    padding-left: var(--menu-navigation-components-tab-item-padding-horizontal);
    padding-right: var(
      --menu-navigation-components-tab-item-padding-horizontal
    );
  }

.wrapper.has-close {
    padding-right: 0;
    padding-left: var(--menu-navigation-components-tab-item-padding-horizontal);
  }

.wrapper.center-content .content {
    justify-content: center;
  }

.wrapper.center-content .text-content {
    flex: 0 1 auto;
  }

.wrapper.center-content .title,.wrapper.center-content .subtitle {
    text-align: center;
  }

.wrapper.hug {
    width: fit-content;
    min-width: 140px;
  }

.wrapper.disabled .title,.wrapper.disabled .subtitle,.wrapper.disabled .leading-icon {
    color: var(--on-flat-disabled-color);
  }

.wrapper .badges {
    display: flex;
    align-items: center;
    gap: 4px;
    position: relative;
  }

.wrapper .badge {
    position: relative;
  }

.wrapper:not(.hug) .badges {
    right: 0;
  }

.wrapper .content {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    position: relative;
    min-width: 0;
    width: 100%;
  }

.wrapper .text-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    flex: 1 1 auto;
    min-width: 0;
    overflow: hidden;
  }

.wrapper .leading-icon {
    width: var(--menu-navigation-components-tab-item-icon-size);
    height: var(--menu-navigation-components-tab-item-icon-size);
    color: var(--on-flat-neutral-color);
    flex-shrink: 0;
  }

.wrapper .title,.wrapper .subtitle {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-body-font-weight);
    font-size: var(--global-typography-ui-body-font-size);
    line-height: var(--global-typography-ui-body-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    min-width: 0;
    padding: 0 var(--menu-navigation-components-tab-item-label-spacing);
    color: var(--on-flat-neutral-color);
  }

.wrapper .subtitle {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-label-font-weight);
    font-size: var(--global-typography-ui-label-font-size);
    line-height: var(--global-typography-ui-label-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  }

.wrapper .divider {
    width: 1px;
    height: var(--menu-navigation-components-tab-action-button-divider-height);
    flex-shrink: 0;
    color: var(--border-divider-color);
    fill: var(--border-divider-color);
    background-color: var(--border-divider-color);
    position: absolute;
  }

.wrapper.has-divider::before {
    content: "";
    position: absolute;
    left: 0;
    width: 1px;
    height: var(--menu-navigation-components-tab-action-button-divider-height);
    background: var(--border-divider-color);
  }

.wrapper.hug.has-close .content {
    flex: 1;
    justify-content: flex-start;
  }

:host([checked]) .wrapper {
  background: var(--container-global-color);
  border-right: 1px solid var(--border-divider-color);
  border-left: 1px solid var(--border-divider-color);
  border-color: var(--border-divider-color);
}

:is(:host([checked]) .wrapper) .leading-icon {
    color: var(--instrument-enhanced-secondary-color);
  }

.disabled:is(:host([checked]) .wrapper) .leading-icon {
    color: var(--on-flat-disabled-color);
  }

:is(:host([checked]) .wrapper) .title {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-body-active-font-weight);
    font-size: var(--global-typography-ui-body-active-font-size);
    line-height: var(--global-typography-ui-body-active-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  }
`,Wr=class extends j{constructor(...e){super(...e),this.hug=!1,this.centerContent=!1,this.checked=!1,this.hasClose=!1,this.hasLeadingIcon=!1,this.hasTitle=!1,this.hasDivider=!1,this.badges=[],this.hasBadge=!1,this.icon=`placeholder`,this.title=`Tab title`,this.showSubtitle=!1,this.subtitle=``,this.disabled=!1,this.focusable=!0,this.panel=null,this.badgeType=_n.regular,this.badgeSize=gn.regular,this.badgeShowNumber=!0,this.badgeCount=0,this.showLeadingBadgeIcon=!1}handleClick(e){if(this.disabled){e.preventDefault();return}let t=new CustomEvent(`tab-click`,{detail:{title:this.title},bubbles:!0,composed:!0});this.dispatchEvent(t)}handleClose(e){e.stopPropagation();let t=new CustomEvent(`tab-close`,{detail:{title:this.title},bubbles:!0,composed:!0});this.dispatchEvent(t)}focus(e){(this.shadowRoot?.querySelector(`.wrapper`))?.focus(e)}handleKeyDown(e){let t=this.shadowRoot?.querySelector(`.close-button`);if(!(t&&e.composedPath().includes(t))){if(e.key===`Delete`){this.hasClose&&!this.disabled&&(e.preventDefault(),this.handleClose(e));return}(e.key===`Enter`||e.key===` `)&&(e.preventDefault(),this.handleClick(e))}}updated(e){if(e.has(`panel`)){let e=this.shadowRoot?.querySelector(`[role="tab"]`);e&&(e.ariaControlsElements=this.panel?[this.panel]:null)}}get effectiveBadges(){return this.badges.length>0?this.badges:this.hasBadge?[{type:this.badgeType||_n.regular,size:this.badgeSize||gn.regular,count:this.badgeShowNumber?this.badgeCount:void 0,showIcon:this.showLeadingBadgeIcon,iconSlotName:this.showLeadingBadgeIcon?`badge-icon`:void 0}]:[]}renderBadge(e){return O`
      <obc-badge
        class="badge"
        .number=${e.count??0}
        .type=${e.type||_n.regular}
        .size=${e.size||gn.regular}
        .showNumber=${e.count!==void 0}
        .showIcon=${e.showIcon??!1}
      >
        ${e.iconSlotName?O`<slot name=${e.iconSlotName} slot="badge-icon"></slot>`:A}
      </obc-badge>
    `}render(){let e=this.effectiveBadges,t=e.length>0;return O`
      <div
        class=${F({wrapper:!0,hug:this.hug,"has-close":this.hasClose,"has-leading-icon":this.hasLeadingIcon,"has-title":this.hasTitle,"has-divider":this.hasDivider&&!this.checked,"has-badge":t,"has-subtitle":this.showSubtitle,disabled:this.disabled,"center-content":this.centerContent})}
        role="tab"
        aria-selected=${this.checked}
        aria-disabled=${I(this.disabled?`true`:void 0)}
        aria-keyshortcuts=${I(this.hasClose&&!this.disabled?`Delete`:void 0)}
        tabindex=${this.disabled?-1:this.focusable?0:-1}
        @click=${this.handleClick}
        @keydown=${this.handleKeyDown}
      >
        <div class="content">
          ${this.hasLeadingIcon?O`
                  <div class="leading-icon">
                    <slot name="leading-icon"></slot>
                  </div>
                `:A}
          ${this.hasTitle?O`
                  <div class="text-content">
                    <div class="title">
                      <slot name="title">${this.title}</slot>
                    </div>
                    ${this.showSubtitle&&this.subtitle?O`<div class="subtitle">${this.subtitle}</div>`:A}
                  </div>
                `:A}
          ${this.centerContent&&t?O`<div class="badges">
                  ${e.map(e=>this.renderBadge(e))}
                </div>`:A}
        </div>
        ${!this.centerContent&&t?O`<div class="badges">
                ${e.map(e=>this.renderBadge(e))}
              </div>`:A}
        ${this.hasClose?O`
                <obc-icon-button
                  class="close-button"
                  variant="flat"
                  @click=${this.handleClose}
                  aria-label="Close tab"
                  .focusable=${!1}
                  .disabled=${this.disabled}
                  ><obi-close-google></obi-close-google
                ></obc-icon-button>
              `:A}
      </div>
    `}},H=(Wr.styles=a(Ur),Wr);N([P({type:Boolean,reflect:!0})],H.prototype,`hug`,void 0),N([P({type:Boolean})],H.prototype,`centerContent`,void 0),N([P({type:Boolean,reflect:!0})],H.prototype,`checked`,void 0),N([P({type:Boolean,attribute:`has-close`})],H.prototype,`hasClose`,void 0),N([P({type:Boolean,attribute:`has-leading-icon`})],H.prototype,`hasLeadingIcon`,void 0),N([P({type:Boolean,attribute:`has-title`})],H.prototype,`hasTitle`,void 0),N([P({type:Boolean,attribute:`has-divider`})],H.prototype,`hasDivider`,void 0),N([P({type:Array,attribute:!1})],H.prototype,`badges`,void 0),N([P({type:Boolean,attribute:`has-badge`})],H.prototype,`hasBadge`,void 0),N([P({type:String})],H.prototype,`icon`,void 0),N([P({type:String})],H.prototype,`title`,void 0),N([P({type:Boolean,attribute:`show-subtitle`})],H.prototype,`showSubtitle`,void 0),N([P({type:String})],H.prototype,`subtitle`,void 0),N([P({type:Boolean})],H.prototype,`disabled`,void 0),N([P({type:Boolean,attribute:!1})],H.prototype,`focusable`,void 0),N([P({attribute:!1})],H.prototype,`panel`,void 0),N([P({type:String})],H.prototype,`badgeType`,void 0),N([P({type:String})],H.prototype,`badgeSize`,void 0),N([P({type:Boolean,attribute:!1})],H.prototype,`badgeShowNumber`,void 0),N([P({type:Number})],H.prototype,`badgeCount`,void 0),N([P({type:Boolean})],H.prototype,`showLeadingBadgeIcon`,void 0),H=N([M(`obc-tab-item`)],H);var{I:Gr}=Me,Kr=e=>e,qr=e=>e.strings===void 0,Jr=()=>document.createComment(``),Yr=(e,t,n)=>{let r=e._$AA.parentNode,i=t===void 0?e._$AB:t._$AA;if(n===void 0)n=new Gr(r.insertBefore(Jr(),i),r.insertBefore(Jr(),i),e,e.options);else{let t=n._$AB.nextSibling,a=n._$AM,o=a!==e;if(o){let t;n._$AQ?.(e),n._$AM=e,n._$AP!==void 0&&(t=e._$AU)!==a._$AU&&n._$AP(t)}if(t!==i||o){let e=n._$AA;for(;e!==t;){let t=Kr(e).nextSibling;Kr(r).insertBefore(e,i),e=t}}}return n},Xr=(e,t,n=e)=>(e._$AI(t,n),e),Zr={},Qr=(e,t=Zr)=>e._$AH=t,$r=e=>e._$AH,ei=e=>{e._$AR(),e._$AA.remove()},ti=(e,t,n)=>{let r=new Map;for(let i=t;i<=n;i++)r.set(e[i],i);return r},ni=pt(class extends mt{constructor(e){if(super(e),e.type!==ft.CHILD)throw Error(`repeat() can only be used in text expressions`)}dt(e,t,n){let r;n===void 0?n=t:t!==void 0&&(r=t);let i=[],a=[],o=0;for(let t of e)i[o]=r?r(t,o):o,a[o]=n(t,o),o++;return{values:a,keys:i}}render(e,t,n){return this.dt(e,t,n).values}update(e,[t,n,r]){let i=$r(e),{values:a,keys:o}=this.dt(t,n,r);if(!Array.isArray(i))return this.ut=o,a;let s=this.ut??=[],c=[],l,u,d=0,f=i.length-1,p=0,m=a.length-1;for(;d<=f&&p<=m;)if(i[d]===null)d++;else if(i[f]===null)f--;else if(s[d]===o[p])c[p]=Xr(i[d],a[p]),d++,p++;else if(s[f]===o[m])c[m]=Xr(i[f],a[m]),f--,m--;else if(s[d]===o[m])c[m]=Xr(i[d],a[m]),Yr(e,c[m+1],i[d]),d++,m--;else if(s[f]===o[p])c[p]=Xr(i[f],a[p]),Yr(e,i[d],i[f]),f--,p++;else if(l===void 0&&(l=ti(o,p,m),u=ti(s,d,f)),l.has(s[d])){if(l.has(s[f])){let t=u.get(o[p]),n=t===void 0?null:i[t];if(n===null){let t=Yr(e,i[d]);Xr(t,a[p]),c[p]=t}else c[p]=Xr(n,a[p]),Yr(e,i[d],n),i[t]=null;p++}else ei(i[f]),f--}else ei(i[d]),d++;for(;p<=m;){let t=Yr(e,c[m+1]);Xr(t,a[p]),c[p++]=t}for(;d<=f;){let e=i[d++];e!==null&&ei(e)}return this.ut=o,Qr(e,c),ve}}),ri=class extends j{constructor(...e){super(...e),this.tabs=[],this.selectedTabId=``,this.hasClose=!1,this.centerContent=!1,this.hug=!1,this.showSubtitle=!1,this.hasAddNewTab=!1,this.hasPanels=!1,this.label=`Tabs`,this.navigator=new Wt({items:()=>this.tabItems(),isDisabled:e=>e.disabled,preferred:()=>this.tabItems().find(e=>e.checked),setFocusable:(e,t)=>{e.focusable=t}},{orientation:`horizontal`})}tabItems(){return Array.from(this.shadowRoot?.querySelectorAll(`obc-tab-item`)??[])}handleKeydown(e){this.navigator.handleKeydown(e)&&e.preventDefault()}updated(){this.navigator.refresh();let e=Array.from(this.shadowRoot?.querySelectorAll(`.panel`)??[]);this.tabItems().forEach((t,n)=>{t.panel=e[n]??null})}handleTabClick(e,t){e.stopPropagation();let n=this.tabs.findIndex(e=>e.id===t);n!==-1&&(this.selectedTabId=this.tabs[n].id,this.dispatchEvent(new CustomEvent(`tab-selected`,{detail:{tab:this.tabs[n],id:t,index:n},bubbles:!0,composed:!0})))}handleTabClose(e,t){e.stopPropagation();let n=this.tabs.findIndex(e=>e.id===t);if(n===-1)return;let r=this.tabs[n],i=this.tabItems()[n]?.matches(`:focus-within`);if(this.tabs=[...this.tabs.slice(0,n),...this.tabs.slice(n+1)],r.id===this.selectedTabId&&this.tabs.length){let e=Math.min(n,this.tabs.length-1);this.selectedTabId=this.tabs[e].id}this.dispatchEvent(new CustomEvent(`tab-closed`,{detail:{tab:r,id:r.id,index:n},bubbles:!0,composed:!0})),i&&this.focusAfterClose(n)}async focusAfterClose(e){await this.updateComplete;let t=this.tabItems(),n=t.slice(e).find(e=>!e.disabled)??t.slice(0,e).reverse().find(e=>!e.disabled);n&&this.navigator.setActive(n,!0)}handleAddNewTab(){this.dispatchEvent(new CustomEvent(`add-new-tab`,{bubbles:!0,composed:!0}))}renderTab(e,t){let n=t===0,r=this.selectedTabId===this.tabs[t-1]?.id,i=e.id===this.selectedTabId,a=e.showSubtitle??this.showSubtitle,o=[...new Set((e.badges??[]).map(e=>e.iconSlotName).filter(e=>e!==void 0))];return(e.showLeadingBadgeIcon??!1)&&!o.includes(`badge-icon`)&&o.push(`badge-icon`),O`
      <obc-tab-item
        .title=${e.title}
        .subtitle=${e.subtitle??``}
        .showSubtitle=${a}
        .checked=${i}
        .hasClose=${this.hasClose}
        .hasLeadingIcon=${e.hasLeadingIcon??!0}
        .hasTitle=${!0}
        .hasDivider=${!n&&!r}
        .hug=${this.hug}
        .centerContent=${this.centerContent}
        .disabled=${e.disabled||!1}
        .badges=${e.badges??[]}
        .hasBadge=${e.hasBadge||!1}
        .badgeCount=${e.badgeCount||0}
        .badgeType=${e.badgeType??_n.regular}
        .badgeSize=${e.badgeSize??gn.regular}
        .badgeShowNumber=${e.badgeShowNumber??!0}
        .showLeadingBadgeIcon=${e.showLeadingBadgeIcon||!1}
        @tab-click=${t=>this.handleTabClick(t,e.id)}
        @tab-close=${t=>this.handleTabClose(t,e.id)}
      >
        ${e.hasLeadingIcon===!1?``:O`
                <slot name="tab-${e.id}-icon" slot="leading-icon">
                  <obi-placeholder></obi-placeholder>
                </slot>
              `}
        <span slot="title">${e.title}</span>
        ${o.map(t=>O`
            <slot name="tab-${e.id}-${t}" slot=${t}>
              <obi-placeholder></obi-placeholder>
            </slot>
          `)}
      </obc-tab-item>
    `}render(){return O`
      <div class="wrapper">
        <div
          class=${F({tabs:!0,hug:this.hug})}
          role="tablist"
          aria-label=${this.label}
          @keydown=${this.handleKeydown}
          @focusin=${e=>this.navigator.handleFocusin(e)}
        >
          ${ni(this.tabs,e=>e.id,(e,t)=>this.renderTab(e,t))}
        </div>
        ${this.hasAddNewTab?O`
                <obc-icon-button
                  class="add-new-tab"
                  variant="flat"
                  @click=${this.handleAddNewTab}
                  aria-label="Add new tab"
                >
                  <obi-up-iec></obi-up-iec>
                </obc-icon-button>
              `:``}
      </div>
      ${this.hasPanels?this.renderPanels():A}
    `}renderPanels(){return ni(this.tabs,e=>e.id,e=>O`
        <div
          class="panel"
          role="tabpanel"
          aria-label=${e.title}
          tabindex="0"
          ?hidden=${e.id!==this.selectedTabId}
        >
          <slot name="tab-${e.id}-panel"></slot>
        </div>
      `)}},ii=(ri.styles=a(Hr),ri);N([P({type:Array})],ii.prototype,`tabs`,void 0),N([P({type:String,attribute:`selected-tab-id`})],ii.prototype,`selectedTabId`,void 0),N([P({type:Boolean,attribute:`has-close`})],ii.prototype,`hasClose`,void 0),N([P({type:Boolean})],ii.prototype,`centerContent`,void 0),N([P({type:Boolean})],ii.prototype,`hug`,void 0),N([P({type:Boolean,attribute:`show-subtitle`})],ii.prototype,`showSubtitle`,void 0),N([P({type:Boolean,attribute:`has-add-new-tab`})],ii.prototype,`hasAddNewTab`,void 0),N([P({type:Boolean,attribute:`has-panels`})],ii.prototype,`hasPanels`,void 0),N([P({type:String})],ii.prototype,`label`,void 0),ii=N([M(`obc-tab-row`)],ii);var ai,oi=`brilliance`,si=`palette`,U=(ai=class extends j{constructor(...e){super(...e),this.softDismiss=!1,this.open=!1,this.softDismissController=new Ht(this),this.palette=`day`,this.brightness=50,this.showLinkBrightness=!1,this.showLinkPalette=!1,this.showBrightness=!0,this.showPalette=!0,this.showNightPalette=!0,this.showDuskPalette=!0,this.showDayPalette=!0,this.showBrightPalette=!0,this.variant=`normal`,this.brightnessUnit=`%`,this.brightnessMax=100,this.brightnessMinorStep=5,this.brightnessMajorStep=25,this.brightnessInputVariant=`buttons`,this.showScreenControlLink=!1,this.showAdditionalScreenControls=!1,this.selectedTabId=oi}willUpdate(e){if(this.showPalette){let e=this.availablePalettes;e.length>0&&!e.includes(this.palette)&&(this.palette=e[0],this.dispatchEvent(new CustomEvent(`palette-changed`,{detail:{value:this.palette}})))}}onPaletteChanged(e){this.palette=e.detail.value,this.dispatchEvent(new CustomEvent(`palette-changed`,{detail:{value:e.detail.value}}))}handleBrightnessChanged(e){this.brightness=e.detail,this.dispatchEvent(new CustomEvent(`brightness-changed`,{detail:{value:e.detail}}))}increaseBrightness(e){this.brightness=st(this.brightness+e,0,Math.max(0,this.brightnessMax)),this.dispatchEvent(new CustomEvent(`brightness-changed`,{detail:{value:this.brightness}}))}get canIncreaseBrightness(){return this.brightness<this.brightnessMax}get canDecreaseBrightness(){return this.brightness>0}onLinkPaletteChanged(e){this.dispatchEvent(new CustomEvent(`link-palette-changed`,{detail:{value:e.target.checked}}))}onLinkBrightnessChanged(e){this.dispatchEvent(new CustomEvent(`link-brightness-changed`,{detail:{value:e.target.checked}}))}get availablePalettes(){let e=[];return this.showNightPalette&&e.push(`night`),this.showDuskPalette&&e.push(`dusk`),this.showDayPalette&&e.push(`day`),this.showBrightPalette&&e.push(`bright`),e}get canIncreasePalette(){let e=this.availablePalettes,t=e.indexOf(this.palette);return t>=0&&t<e.length-1}get canDecreasePalette(){return this.availablePalettes.indexOf(this.palette)>0}onTabSelected(e){e.stopPropagation(),this.selectedTabId=e.detail.id}get tabs(){return[{id:oi,title:R(`Brilliance`),hasLeadingIcon:!0},{id:si,title:`${R(`Day`)}/${R(`Night`)}`,hasLeadingIcon:!0}]}nextPalette(){if(this.canIncreasePalette){let e=this.availablePalettes,t=e.indexOf(this.palette);this.palette=e[t+1],this.dispatchEvent(new CustomEvent(`palette-changed`,{detail:{value:this.palette}}))}}previousPalette(){if(this.canDecreasePalette){let e=this.availablePalettes,t=e.indexOf(this.palette);this.palette=e[t-1],this.dispatchEvent(new CustomEvent(`palette-changed`,{detail:{value:this.palette}}))}}renderBrightness(){let e=this.variant===`tabbed`?A:O`<div class="title-container">
            <h3>${R(`Brilliance`)}</h3>
          </div>`,t=this.brightness.toString().length+.5*this.brightnessUnit.length;return O`${e}
      <div class="content-container brilliance">
        ${this.variant===`compact`?O` <obc-slider
                value=${this.brightness}
                @value=${this.handleBrightnessChanged}
                min="0"
                max=${this.brightnessMax}
                variant=${xr.Normal}
                haslefticon
                hasrighticon
              >
                <obi-display-brilliance-low
                  slot="icon-left"
                ></obi-display-brilliance-low>
                <obi-display-brilliance-proposal
                  slot="icon-right"
                ></obi-display-brilliance-proposal>
              </obc-slider>`:O`
                <div class="value-container">
                  <div class="value-label-container">
                    <obi-display-brilliance-proposal
                      class="icon"
                    ></obi-display-brilliance-proposal>
                    <div
                      class="label-container"
                      style="width: ${t}ch"
                    >
                      <div class="value">${this.brightness.toFixed(0)}</div>
                      <div class="unit">${this.brightnessUnit}</div>
                    </div>
                  </div>
                  <div class="value-slider-container">
                    ${this.brightnessInputVariant===`buttons`?O`
                            <obc-slider
                              value=${this.brightness}
                              variant=${xr.NoInput}
                              min="0"
                              max=${this.brightnessMax}
                            ></obc-slider>
                          `:O`
                            <obc-slider
                              value=${this.brightness}
                              variant=${xr.Enhanced}
                              @value=${this.handleBrightnessChanged}
                              min="0"
                              max=${this.brightnessMax}
                            ></obc-slider>
                          `}
                  </div>
                </div>
                ${this.brightnessInputVariant===`buttons`?O`
                        <div class="icon-button-container">
                          <obc-button
                            segmentPosition="start"
                            fullWidth
                            ?disabled=${!this.canDecreaseBrightness}
                            class=${this.canDecreaseBrightness?``:`disabled`}
                            @click=${()=>this.increaseBrightness(-this.brightnessMajorStep)}
                          >
                            <obi-chevron-double-left-google
                              class="btn-icon"
                            ></obi-chevron-double-left-google>
                          </obc-button>
                          <obc-button
                            segmentPosition="middle"
                            fullWidth
                            ?disabled=${!this.canDecreaseBrightness}
                            class=${this.canDecreaseBrightness?``:`disabled`}
                            @click=${()=>this.increaseBrightness(-this.brightnessMinorStep)}
                          >
                            <obi-chevron-left-google
                              class="btn-icon"
                            ></obi-chevron-left-google>
                          </obc-button>
                          <obc-button
                            segmentPosition="middle"
                            fullWidth
                            ?disabled=${!this.canIncreaseBrightness}
                            class=${this.canIncreaseBrightness?``:`disabled`}
                            @click=${()=>this.increaseBrightness(this.brightnessMinorStep)}
                          >
                            <obi-chevron-right-google
                              class="btn-icon"
                            ></obi-chevron-right-google>
                          </obc-button>
                          <obc-button
                            segmentPosition="end"
                            fullWidth
                            ?disabled=${!this.canIncreaseBrightness}
                            class=${this.canIncreaseBrightness?``:`disabled`}
                            @click=${()=>this.increaseBrightness(this.brightnessMajorStep)}
                          >
                            <obi-chevron-double-right-google
                              class="btn-icon"
                            ></obi-chevron-double-right-google>
                          </obc-button>
                        </div>
                      `:A}
              `}
        ${this.showLinkBrightness?O`<obc-toggle-switch
                .label="${R(`Link`)}"
                hasicon
                @input=${this.onLinkBrightnessChanged}
              >
                <obi-link slot="icon"></obi-link>
              </obc-toggle-switch>`:A}
      </div>`}get effectivePalette(){let e=this.availablePalettes;return e.includes(this.palette)?this.palette:e[0]}get paletteIcon(){return this.effectivePalette===`night`?O`<obi-palette-night class="icon"></obi-palette-night>`:this.effectivePalette===`dusk`?O`<obi-palette-dusk class="icon"></obi-palette-dusk>`:this.effectivePalette===`day`?O`<obi-palette-day class="icon"></obi-palette-day>`:this.effectivePalette===`bright`?O`<obi-palette-day-bright
        class="icon"
      ></obi-palette-day-bright>`:A}paletteOptions(){let e=[];return this.showNightPalette&&e.push(O`<obc-toggle-button-option value="night" type="icon">
          <obi-palette-night slot="icon"></obi-palette-night>
        </obc-toggle-button-option>`),this.showDuskPalette&&e.push(O`<obc-toggle-button-option value="dusk" type="icon">
          <obi-palette-dusk slot="icon"></obi-palette-dusk>
        </obc-toggle-button-option>`),this.showDayPalette&&e.push(O`<obc-toggle-button-option value="day" type="icon">
          <obi-palette-day slot="icon"></obi-palette-day>
        </obc-toggle-button-option>`),this.showBrightPalette&&e.push(O`<obc-toggle-button-option value="bright" type="icon">
          <obi-palette-day-bright slot="icon"></obi-palette-day-bright>
        </obc-toggle-button-option>`),e}renderPalette(){let e=this.availablePalettes;if(e.length===0)return A;let t={night:R(`Night`),dusk:R(`Dusk`),day:R(`Day`),bright:R(`Bright`)},n=t[this.effectivePalette],r=n.length,i=e.indexOf(this.effectivePalette),a=Math.min(i+1,e.length-1),o=Math.max(i-1,0),s=t[e[a]],c=t[e[o]];return O`
      ${this.variant===`tabbed`?A:O`
              <div class="title-container">
                <h3>${R(`Day`)}/${R(`Night`)}</h3>
              </div>
            `}
      <div
        class="content-container palette ${this.showLinkPalette?`with-link`:`without-link`}"
      >
        ${this.variant===`compact`?O` <obc-toggle-button-group
                aria-label=${`${R(`Day`)}/${R(`Night`)}`}
                value=${this.effectivePalette}
                @value=${this.onPaletteChanged}
                variant=${Ar.regular}
                type=${kr.icon}
              >
                ${this.paletteOptions()}
              </obc-toggle-button-group>`:O`
                <div class="value-container">
                  <div class="value-label-container">
                    ${this.paletteIcon}
                    <div
                      class="label-container"
                      style="width: ${r}ch"
                    >
                      <div class="value">${n}</div>
                    </div>
                  </div>
                  <obc-progress-indicator-dots
                    .totalSteps=${e.length}
                    .currentStep=${i+1}
                  ></obc-progress-indicator-dots>
                </div>
                <div class="icon-button-container">
                  <obc-button
                    segmentPosition="start"
                    fullWidth
                    showLeadingIcon
                    ?disabled=${!this.canDecreasePalette}
                    class=${this.canDecreasePalette?``:`disabled`}
                    @click=${()=>this.previousPalette()}
                  >
                    ${c}
                    <obi-chevron-left-google
                      slot="leading-icon"
                    ></obi-chevron-left-google>
                  </obc-button>

                  <obc-button
                    segmentPosition="end"
                    fullWidth
                    showTrailingIcon
                    ?disabled=${!this.canIncreasePalette}
                    class=${this.canIncreasePalette?``:`disabled`}
                    @click=${()=>this.nextPalette()}
                  >
                    ${s}
                    <obi-chevron-right-google
                      slot="trailing-icon"
                    ></obi-chevron-right-google>
                  </obc-button>
                </div>
              `}
        ${this.showLinkPalette?O`<obc-toggle-switch
                .label="${R(`Link`)}"
                hasicon
                @input=${this.onLinkPaletteChanged}
              >
                <obi-link slot="icon"></obi-link>
              </obc-toggle-switch>`:A}
      </div>
    `}renderScreenControlLink(){return this.showScreenControlLink||this.showAdditionalScreenControls?O`
        <div class="footer">
          ${this.showScreenControlLink?O`
                  <obc-navigation-item
                    .label="${R(`Screen Control`)}"
                    @click=${()=>this.handleScreenControlLinkClicked()}
                    hasicon
                  >
                    <obc-user-button
                      slot="icon"
                      static
                      variant="icon"
                      styleType="normal"
                    >
                      <obi-screen-desk slot="icon"></obi-screen-desk>
                    </obc-user-button>
                  </obc-navigation-item>
                `:A}
          ${this.showAdditionalScreenControls?O`<slot name="additional-screen-controls"></slot>`:A}
        </div>
      `:A}render(){return this.variant===`tabbed`?O`
        <div class="card tabbed">
          <obc-tab-row
            .tabs=${this.tabs}
            .selectedTabId=${this.selectedTabId}
            .centerContent=${!0}
            .hasPanels=${!0}
            .label=${R(`Display`)}
            @tab-selected=${this.onTabSelected}
            @tab-closed=${or}
            @add-new-tab=${or}
          >
            <obi-display-brilliance-iec
              slot="tab-${oi}-icon"
            ></obi-display-brilliance-iec>
            <obi-palette-day-night-iec
              slot="tab-${si}-icon"
            ></obi-palette-day-night-iec>
            <div slot="tab-${oi}-panel">
              ${this.renderBrightness()}
            </div>
            <div slot="tab-${si}-panel">
              ${this.renderPalette()}
            </div>
          </obc-tab-row>
          ${this.renderScreenControlLink()}
        </div>
      `:O`
        <div class="card ${this.variant}">
          ${this.showBrightness?this.renderBrightness():A}
          ${this.showBrightness&&this.showPalette?O`<div class="divider"></div>`:A}
          ${this.showPalette?this.renderPalette():A}
          ${this.renderScreenControlLink()}
        </div>
      `}handleScreenControlLinkClicked(){this.dispatchEvent(new CustomEvent(`screen-control-link-clicked`))}},ai.styles=a(Cr),ai);N([P({type:Boolean})],U.prototype,`softDismiss`,void 0),N([P({type:Boolean})],U.prototype,`open`,void 0),N([P({type:String})],U.prototype,`palette`,void 0),N([P({type:Number})],U.prototype,`brightness`,void 0),N([P({type:Boolean})],U.prototype,`showLinkBrightness`,void 0),N([P({type:Boolean})],U.prototype,`showLinkPalette`,void 0),N([P({type:Boolean,attribute:!1})],U.prototype,`showBrightness`,void 0),N([P({type:Boolean,attribute:!1})],U.prototype,`showPalette`,void 0),N([P({type:Boolean,attribute:!1})],U.prototype,`showNightPalette`,void 0),N([P({type:Boolean,attribute:!1})],U.prototype,`showDuskPalette`,void 0),N([P({type:Boolean,attribute:!1})],U.prototype,`showDayPalette`,void 0),N([P({type:Boolean,attribute:!1})],U.prototype,`showBrightPalette`,void 0),N([P({type:String})],U.prototype,`variant`,void 0),N([P({type:String})],U.prototype,`brightnessUnit`,void 0),N([P({type:Number})],U.prototype,`brightnessMax`,void 0),N([P({type:Number})],U.prototype,`brightnessMinorStep`,void 0),N([P({type:Number})],U.prototype,`brightnessMajorStep`,void 0),N([P({type:String})],U.prototype,`brightnessInputVariant`,void 0),N([P({type:Boolean})],U.prototype,`showScreenControlLink`,void 0),N([P({type:Boolean})],U.prototype,`showAdditionalScreenControls`,void 0),N([ze()],U.prototype,`selectedTabId`,void 0),U=N([Rt(),M(`obc-brilliance-menu`)],U);var ci=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M8.9313 10C8.32548 10 8.02257 10 7.88231 10.1198C7.76061 10.2237 7.69602 10.3797 7.70858 10.5392C7.72305 10.7231 7.93724 10.9373 8.36561 11.3657L11.4342 14.4343C11.6323 14.6323 11.7313 14.7313 11.8454 14.7684C11.9458 14.8011 12.054 14.8011 12.1544 14.7684C12.2686 14.7313 12.3676 14.6323 12.5656 14.4343L15.6342 11.3657C16.0626 10.9373 16.2768 10.7231 16.2913 10.5392C16.3038 10.3797 16.2392 10.2237 16.1175 10.1198C15.9773 10 15.6744 10 15.0686 10H8.9313Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M8.9313 10C8.32548 10 8.02257 10 7.88231 10.1198C7.76061 10.2237 7.69602 10.3797 7.70858 10.5392C7.72305 10.7231 7.93724 10.9373 8.36561 11.3657L11.4342 14.4343C11.6323 14.6323 11.7313 14.7313 11.8454 14.7684C11.9458 14.8011 12.054 14.8011 12.1544 14.7684C12.2686 14.7313 12.3676 14.6323 12.5656 14.4343L15.6342 11.3657C16.0626 10.9373 16.2768 10.7231 16.2913 10.5392C16.3038 10.3797 16.2392 10.2237 16.1175 10.1198C15.9773 10 15.6744 10 15.0686 10H8.9313Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},li=(ci.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,ci);N([P({type:Boolean})],li.prototype,`useCssColor`,void 0),li=N([M(`obi-drop-down-google`)],li);var ui=o`* {
  -webkit-tap-highlight-color: transparent;
}

.wrapper {
  position: relative;
  user-select: none;
  padding: 0;
  background: transparent;
  width: fit-content;
  height: var(--ui-components-button-touch-target-size);
  appearance: none;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-button-font-weight);
  font-size: var(--global-typography-ui-button-font-size);
  line-height: var(--global-typography-ui-button-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
}

.wrapper.full-width {
    width: 100%;
  }

.wrapper.full-width .visible-wrapper {
      width: 100%;
      justify-content: space-between;
    }

.wrapper .visible-wrapper {
    height: var(--ui-components-button-visual-size);
    border-radius: var(--ui-components-button-border-radius-top-left)
      var(--ui-components-button-border-radius-top-right)
      var(--ui-components-button-border-radius-bottom-right)
      var(--ui-components-button-border-radius-bottom-left);
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
    padding-left: calc(var(--ui-components-button-padding-horizontal) * 2);
    padding-right: var(--ui-components-button-padding-horizontal);
  }

.wrapper .icon-container {
    display: flex;
    align-items: center;
    justify-content: center;
    height: var(--global-size-spacing-icon-icon-size-regular);
    width: var(--global-size-spacing-icon-icon-size-regular);
  }

.wrapper .icon {
    height: var(--global-size-spacing-icon-icon-size-regular);
    width: var(--global-size-spacing-icon-icon-size-regular);
  }

.wrapper.disabled .icon-container {
    color: var(--on-normal-disabled-color);
  }

.wrapper.disabled .icon {
    color: var(--on-normal-disabled-color);
  }

.wrapper .label {
    padding-left: var(--ui-components-button-label-spacing);
    padding-right: var(--ui-components-button-label-spacing);
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
  }

.wrapper {
  cursor: pointer;
}

.wrapper:focus {
  outline: none;
}

.wrapper .visible-wrapper {
  border-color: var(--normal-enabled-border-color);
  background-color: var(--normal-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--normal-enabled-border-color);
  --base-background-color: var(--normal-enabled-background-color);
}

.wrapper.activated .visible-wrapper {
  border-color: var(--normal-activated-border-color);
  background-color: var(--normal-activated-background-color);
  --base-border-color: var(--normal-activated-border-color);
  --base-background-color: var(--normal-activated-background-color);
}

@media (hover:hover) {

.wrapper:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--normal-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--normal-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper:active .visible-wrapper {
  border-color: var(--normal-pressed-border-color);
  background-color: var(--normal-pressed-background-color);
}

.wrapper:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper:disabled .visible-wrapper {
  border-color: var(--normal-disabled-border-color);
  background-color: var(--normal-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-normal-disabled-color) !important;
}

.wrapper.disabled .visible-wrapper {
  border-color: var(--normal-disabled-border-color);
  background-color: var(--normal-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-normal-disabled-color) !important;
}

.wrapper:disabled {
  cursor: not-allowed;
}

.wrapper.disabled {
  cursor: not-allowed;
}

.wrapper {
  color: var(--on-normal-active-color);
}

.wrapper .icon {
    color: var(--on-normal-neutral-color);
  }

.wrapper:disabled .icon {
    color: var(--on-normal-disabled-color);
  }

.wrapper select {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    appearance: none;
    appearance: base-select;
    opacity: 0;
  }

.wrapper:has(select:focus-visible) .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

::picker(select) {
  appearance: base-select;
  border: none;
  min-width: var(--ui-components-context-menu-menu-width);
  border-radius: 12px;
  background: var(--container-global-color);
  box-shadow: var(--shadow-floating);
  padding: var(--ui-components-context-menu-margin-vertical)
    var(--ui-components-context-menu-margin-horizontal);

  overflow-y: auto;
}

.wrapper.open-top select::picker(select) {
  position-area: block-start span-inline-end;
}

option {
  height: var(--menu-navigation-components-navigation-item-touch-target-size);
  min-height: var(
    --menu-navigation-components-navigation-item-touch-target-size
  );
  padding: 0px
    var(--menu-navigation-components-navigation-item-padding-horizontal);
  border-radius: var(
    --menu-navigation-components-navigation-item-border-radius
  );
}

option {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

option:focus {
  outline: none;
}

option.activated {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

option:hover {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

option:active {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

option:focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

option:disabled {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

option.disabled {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

option {
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-body-font-weight);
  font-size: var(--global-typography-ui-body-font-size);
  line-height: var(--global-typography-ui-body-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  color: var(--on-flat-neutral-color);
}

option:checked {
  border-color: var(--amplified-enabled-border-color);
  background-color: var(--amplified-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--amplified-enabled-border-color);
  --base-background-color: var(--amplified-enabled-background-color);
}

option:checked:focus {
  outline: none;
}

option.activated:checked {
  border-color: var(--amplified-activated-border-color);
  background-color: var(--amplified-activated-background-color);
  --base-border-color: var(--amplified-activated-border-color);
  --base-background-color: var(--amplified-activated-background-color);
}

@media (hover:hover) {

option:checked:hover {
    border-color: color-mix(in srgb, var(--amplified-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--amplified-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

option:checked:active {
  border-color: var(--amplified-pressed-border-color);
  background-color: var(--amplified-pressed-background-color);
}

option:checked:focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

option:checked:disabled {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

option.disabled:checked {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

option:checked {
  color: var(--on-flat-active-color);
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-body-active-font-weight);
  font-size: var(--global-typography-ui-body-active-font-size);
  line-height: var(--global-typography-ui-body-active-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
}

option::checkmark {
  display: none;
}

.wrapper.flat {
  cursor: pointer;
}

.wrapper.flat:focus {
  outline: none;
}

.wrapper.flat .visible-wrapper {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.wrapper.flat.activated .visible-wrapper {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

.wrapper.flat:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.flat:active .visible-wrapper {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

.wrapper.flat:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.flat:disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.flat.disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.flat:disabled {
  cursor: not-allowed;
}

.wrapper.flat.disabled {
  cursor: not-allowed;
}

.wrapper.integration {
  cursor: pointer;
}

.wrapper.integration:focus {
  outline: none;
}

.wrapper.integration .visible-wrapper {
  border-color: var(--integration-selected-enabled-border-color);
  background-color: var(--integration-selected-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--integration-selected-enabled-border-color);
  --base-background-color: var(--integration-selected-enabled-background-color);
}

.wrapper.integration.activated .visible-wrapper {
  border-color: var(--integration-selected-activated-border-color);
  background-color: var(--integration-selected-activated-background-color);
  --base-border-color: var(--integration-selected-activated-border-color);
  --base-background-color: var(--integration-selected-activated-background-color);
}

@media (hover:hover) {

.wrapper.integration:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--integration-selected-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--integration-selected-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.integration:active .visible-wrapper {
  border-color: var(--integration-selected-pressed-border-color);
  background-color: var(--integration-selected-pressed-background-color);
}

.wrapper.integration:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.integration:disabled .visible-wrapper {
  border-color: var(--integration-selected-disabled-border-color);
  background-color: var(--integration-selected-disabled-background-color);
  cursor: not-allowed;
  color: var(--integration-on-selected-disabled-color) !important;
}

.wrapper.integration.disabled .visible-wrapper {
  border-color: var(--integration-selected-disabled-border-color);
  background-color: var(--integration-selected-disabled-background-color);
  cursor: not-allowed;
  color: var(--integration-on-selected-disabled-color) !important;
}

.wrapper.integration:disabled {
  cursor: not-allowed;
}

.wrapper.integration.disabled {
  cursor: not-allowed;
}

.wrapper.integration .visible-wrapper {
    box-sizing: border-box;
    height: 40px;
  }
`,di=class extends j{constructor(...e){super(...e),this.options=[],this.disabled=!1,this.fullWidth=!1,this.allowEmptySelection=!1,this.placeholder=``,this.type=`label`,this.openTop=!1,this.integration=!1,this.flat=!1,this.selectedValue=``,this.selectedLabel=``}connectedCallback(){super.connectedCallback(),this.updateSelectedValues()}willUpdate(e){(e.has(`value`)||e.has(`options`))&&this.updateSelectedValues()}updateSelectedValues(){if(this.options.length===0){this.selectedValue=``,this.selectedLabel=``;return}let e=this.value?this.options.find(e=>e.value===this.value):void 0;if(e){this.selectedValue=e.value,this.selectedLabel=e.label;return}if(this.allowEmptySelection){this.selectedValue=``,this.selectedLabel=this.placeholder;return}this.selectedValue=this.options[0].value,this.selectedLabel=this.options[0].label}render(){return O`
      <div
        class=${F({wrapper:!0,"full-width":this.fullWidth,"open-top":this.openTop,integration:this.integration,flat:this.flat&&!this.integration,disabled:this.disabled})}
      >
        <div class="visible-wrapper">
          ${this.type===`label`?A:O`<div class="icon-container">
                  <slot name="icon"></slot>
                </div>`}
          ${this.type===`icon`?A:O`<div class="label">${this.selectedLabel}</div>`}
          <div class="icon">
            <obi-drop-down-google></obi-drop-down-google>
          </div>
        </div>
        <select @change=${this.changeHandler} ?disabled=${this.disabled}>
          ${this.allowEmptySelection&&this.selectedValue===``?O`<option value="" disabled selected hidden>
                  ${this.placeholder}
                </option>`:A}
          ${this.options.map(e=>{let t=e.level?(e.level-1)*2:0,n=[];for(let e=0;e<t;e++)n.push(O`&nbsp;`);return O`<option
              value=${e.value}
              ?selected=${e.value===this.selectedValue}
            >
              ${n}${e.label}
            </option>`})}
        </select>
      </div>
    `}changeHandler(e){let t=e.target;this.selectedValue=t.value,this.selectedLabel=this.options.find(e=>e.value===this.selectedValue).label.trim(),this.dispatchEvent(new CustomEvent(`dropdown-change`,{detail:{value:this.selectedValue,label:this.selectedLabel}})),this.dispatchEvent(new CustomEvent(`change`,{detail:{value:this.selectedValue,label:this.selectedLabel}}))}},fi=(di.styles=a(ui),di);N([P({type:Array})],fi.prototype,`options`,void 0),N([P({type:String})],fi.prototype,`value`,void 0),N([P({type:Boolean})],fi.prototype,`disabled`,void 0),N([P({type:Boolean})],fi.prototype,`fullWidth`,void 0),N([P({type:Boolean})],fi.prototype,`allowEmptySelection`,void 0),N([P({type:String})],fi.prototype,`placeholder`,void 0),N([P({type:String})],fi.prototype,`type`,void 0),N([P({type:Boolean})],fi.prototype,`openTop`,void 0),N([P({type:Boolean})],fi.prototype,`integration`,void 0),N([P({type:Boolean})],fi.prototype,`flat`,void 0),N([ze()],fi.prototype,`selectedValue`,void 0),N([ze()],fi.prototype,`selectedLabel`,void 0),fi=N([M(`obc-dropdown-button`)],fi);var pi=o`* {
  -webkit-tap-highlight-color: transparent;
}

* {
  box-sizing: border-box;
}

.wrapper {
  display: flex;
  align-items: center;
  width: fit-content;
  gap: 4px;
  flex: 1 0 0;
  height: 48px;
  padding: 8px;
}

.indicator-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
}

.indicator {
  width: 16px;
  height: 8px;
  flex-shrink: 0;
  border-radius: 2px;
  border-width: 1px;
  border-style: solid;
}

.state-active .indicator {
    border-color: var(--base-blue-600);
    background-color: var(--base-blue-500);
  }

.state-inactive .indicator {
    border-color: var(--element-inactive-color);
    background-color: var(--element-disabled-color);
  }

.state-caution .indicator {
    border-color: var(--alert-caution-outline-color);
    background-color: var(--alert-caution-color);
  }

.state-warning .indicator {
    border-color: var(--alert-warning-outline-color);
    background-color: var(--alert-warning-color);
  }

.state-alarm .indicator {
    border-color: var(--alert-alarm-outline-color);
    background-color: var(--alert-alarm-color);
  }

.state-running .indicator {
    border-color: var(--alert-running-outline-color);
    background-color: var(--alert-running-color);
  }

.label {
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-button-font-weight);
  font-size: var(--global-typography-ui-button-font-size);
  line-height: var(--global-typography-ui-button-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  color: var(--element-active-color);
}

.state-inactive .label {
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-body-font-weight);
  font-size: var(--global-typography-ui-body-font-size);
  line-height: var(--global-typography-ui-body-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  color: var(--element-neutral-color);
}
`,mi=class extends j{constructor(...e){super(...e),this.status=`active`}render(){return O`
      <div
        class=${F({wrapper:!0,[`state-`+this.status]:!0})}
      >
        <div class="indicator-container">
          <div class="indicator"></div>
        </div>
        <div class="label">
          <slot></slot>
        </div>
      </div>
    `}},hi=(mi.styles=a(pi),mi);N([P({type:String})],hi.prototype,`status`,void 0),hi=N([M(`obc-status-indicator`)],hi);var gi=function(e){return e.active=`active`,e.loading=`loading`,e.off=`off`,e}({}),W=function(e){return e.regular=`regular`,e.enhanced=`enhanced`,e}({}),_i=function(e){return e.regular=`regular`,e.flat=`flat`,e.framed=`framed`,e.instrument=`instrument`,e}({}),vi=function(e){return e.innerFirstChild=`innerFirstChild`,e.middleChild=`middleChild`,e.middleRoundedChild=`middleRoundedChild`,e.outerLastChild=`outerLastChild`,e}({}),yi=function(e){return e.notEqual=`notEqual`,e.equal=`equal`,e.equalZero=`equalZero`,e.focus=`focus`,e}({}),bi=function(e){return e.enhanced=`enhanced`,e.regular=`regular`,e}({}),xi=`M22.5918 0.5C25.014 0.50013 26.3186 3.34437 24.917 5.29199L15.0244 19.0371C14.0268 20.423 11.9635 20.423 10.9658 19.0371L1.07326 5.29199C-0.328328 3.34437 0.97623 0.500124 3.39845 0.5L22.5918 0.5Z`,Si=.8,Ci=`--setpoint-animation-duration`,wi=`300ms`;function Ti(e){let t=getComputedStyle(e).getPropertyValue(Ci).trim();if(!t)return 300;let n=parseFloat(t);return Number.isNaN(n)?300:t.endsWith(`s`)&&!t.endsWith(`ms`)?n*1e3:n}function Ei(e,t){let n=ct(t)-ct(e);return n>180&&(n-=360),n<-180&&(n+=360),e+n}function Di(e,t,n=!1){return n?`var(--instrument-frame-tertiary-color)`:e===`focus`?t===`enhanced`?`var(--base-blue-100)`:`var(--instrument-regular-tertiary-color)`:t===`enhanced`?`var(--instrument-enhanced-primary-color)`:`var(--instrument-regular-primary-color)`}function Oi(e,t){return e===`focus`?t===`enhanced`?`var(--element-neutral-enhanced-color)`:`var(--instrument-regular-secondary-color)`:`var(--border-silhouette-color)`}function ki(e){return xi}function Ai(e){switch(e){case`equal`:case`equalZero`:return Si;default:return 1}}function ji(e){switch(e){case`equalZero`:return 8;case`notEqual`:case`focus`:return 4;default:return 0}}function Mi(e=`setpoint`){return`${e}-${Math.random().toString(36).slice(2,9)}`}function Ni(e){let{visualState:t,colorMode:n,disabled:r=!1,id:i}=e,a=Di(t,n,r),o=Oi(t,n),s=ki(t),c=Ai(t),l=`${i}-marker`,u=`${i}-mask`;return k`
    <defs>
      <g id="${l}">
        <path
          fill-rule="evenodd"
          clip-rule="evenodd"
          transform="translate(${-13}, ${-21})"
          d="${s}"
          vector-effect="non-scaling-stroke"
        />
      </g>
      <mask id="${u}">
        <rect x="-20" y="-30" width="50" height="50" fill="white" />
        <use href="#${l}" fill="black" />
      </mask>
    </defs>
    <g transform="${`scale(${c})`}" style="transition: transform 200ms ease-in-out;">
      <use href="#${l}" fill="${a}" stroke="none" />
      ${t===`focus`?k`
          <!-- Focus state: 1px silhouette (outer) + 2px colored border (inner) -->
          <!-- First: masked silhouette stroke for outer 1px edge -->
          <use
            href="#${l}"
            mask="url(#${u})"
            fill="none"
            stroke="var(--border-silhouette-color)"
            stroke-width="4"
            stroke-linejoin="round"
            vector-effect="non-scaling-stroke"
          />
          <!-- Second: 2px colored border on top -->
          <use
            href="#${l}"
            fill="none"
            stroke="${o}"
            stroke-width="2"
            stroke-linejoin="round"
            vector-effect="non-scaling-stroke"
          />
        `:k`
          <use
            href="#${l}"
            mask="url(#${u})"
            fill="none"
            stroke="${o}"
            stroke-width="2"
            stroke-linejoin="round"
            vector-effect="non-scaling-stroke"
          />
        `}
    </g>
  `}function Pi(e){let{state:t,priority:n,atSetpoint:r,angleSetpoint:i,setpointAtZeroDeadband:a=.5,newAngleSetpoint:o,touching:s=!1,setpointOverride:c=!1}=e,l=o!==void 0,u=n===W.enhanced?`enhanced`:`regular`;return t===gi.loading||t===gi.off?{visualState:`notEqual`,colorMode:u,disabled:!c,hasNewSetpoint:l}:s&&!l?{visualState:`focus`,colorMode:u,disabled:!1,hasNewSetpoint:l}:r&&i!==void 0&&Math.abs(i)<a?{visualState:`equalZero`,colorMode:u,disabled:!1,hasNewSetpoint:l}:r?{visualState:`equal`,colorMode:u,disabled:!1,hasNewSetpoint:l}:{visualState:`notEqual`,colorMode:u,disabled:!1,hasNewSetpoint:l}}function Fi(e){let{value:t,setpoint:n,touching:r,auto:i,deadband:a,atSetpointManual:o,angularWraparound:s=!1}=e;if(t===void 0||n===void 0||r)return!1;if(i){let e=Math.abs(t-n);return s&&e>180&&(e=360-e),e<=(Number.isFinite(a)?a:0)}return o}var Ii=class{constructor(e){this.atSetpoint=!1,this.touching=!1,this.autoAtSetpoint=!0,this.setpointOverride=!1,this.animateSetpoint=!1,this.autoAtSetpointDeadband=e?.defaultDeadband??2,this.setpointAtZeroDeadband=e?.defaultZeroDeadband??.5,this._angularWraparound=e?.angularWraparound??!1,this._onAnimationEnd=e?.onAnimationEnd}sync(e){let t=this.newSetpoint;(e.setpoint!==void 0||`setpoint`in e)&&(this.setpoint=e.setpoint),(e.newSetpoint!==void 0||`newSetpoint`in e)&&(this.newSetpoint=e.newSetpoint),e.atSetpoint!==void 0&&(this.atSetpoint=e.atSetpoint),e.touching!==void 0&&(this.touching=e.touching),e.autoAtSetpoint!==void 0&&(this.autoAtSetpoint=e.autoAtSetpoint),e.autoAtSetpointDeadband!==void 0&&(this.autoAtSetpointDeadband=e.autoAtSetpointDeadband),e.setpointAtZeroDeadband!==void 0&&(this.setpointAtZeroDeadband=e.setpointAtZeroDeadband),e.setpointOverride!==void 0&&(this.setpointOverride=e.setpointOverride),e.animateSetpoint!==void 0&&(this.animateSetpoint=e.animateSetpoint),t!==void 0&&this.newSetpoint===void 0&&this.animateSetpoint&&(this.departingNewSetpoint=t,clearTimeout(this._animationTimer),this._animationTimer=setTimeout(()=>{this.departingNewSetpoint=void 0,this._onAnimationEnd?.()},300))}dispose(){clearTimeout(this._animationTimer)}computeAtSetpoint(e){return Fi({value:e,setpoint:this.setpoint,touching:this.touching,auto:this.autoAtSetpoint,deadband:this.autoAtSetpointDeadband,atSetpointManual:this.atSetpoint,angularWraparound:this._angularWraparound})}},Li=function(e){return e.square=`square`,e.bbox=`bbox`,e}({});function Ri(e){let{areas:t,outerRadius:n,innerRadius:r,extension:i,targetSize:a,margin:o=.06,includeBox:s,fit:c=`square`}=e;if(t.length===0){let e=a;return{radiusOffset:0,x:-e/2,y:-e/2,width:e,height:e,viewBox:`${-e/2} ${-e/2} ${e} ${e}`}}let l=a*(1-2*o),u=e=>{let a=zi(t,n+e,r+e,i);return Math.max(a.xMax-a.xMin,a.yMax-a.yMin)},d=0,f=a;for(let e=0;e<16&&u(f)<l;e++)f*=2;for(let e=0;e<50;e++){let e=(d+f)/2;u(e)<l?d=e:f=e}let p=Math.max(0,d),m=Bi(zi(t,n+p,r+p,i),s),h=m.xMax-m.xMin,g=m.yMax-m.yMin,_=Math.max(h,g),v=_*o,y=(m.xMin+m.xMax)/2,b=(m.yMin+m.yMax)/2,x=c===`bbox`?h+v*2:_+v*2,S=c===`bbox`?g+v*2:_+v*2,C=Hi(y-x/2),w=Hi(b-S/2),T=Hi(x),E=Hi(S);return{radiusOffset:p,x:C,y:w,width:T,height:E,viewBox:`${C} ${w} ${T} ${E}`}}function zi(e,t,n,r){let i=t+r,a=n,o=1/0,s=-1/0,c=1/0,l=-1/0,u=(e,t)=>{e<o&&(o=e),e>s&&(s=e),t<c&&(c=t),t>l&&(l=t)};for(let t of e){let e=lt(t.startAngle),n=lt(t.endAngle);for(let t of[i,a])u(t*Math.sin(e),-t*Math.cos(e)),u(t*Math.sin(n),-t*Math.cos(n));let r=ct(t.startAngle),o=ct(t.endAngle);for(let e of[0,90,180,270])if(Vi(r,o,e)){let t=lt(e);for(let e of[i,a])u(e*Math.sin(t),-e*Math.cos(t))}}return o===1/0?{xMin:0,xMax:0,yMin:0,yMax:0}:{xMin:o,xMax:s,yMin:c,yMax:l}}function Bi(e,t){return t?{xMin:Math.min(e.xMin,t.xMin),xMax:Math.max(e.xMax,t.xMax),yMin:Math.min(e.yMin,t.yMin),yMax:Math.max(e.yMax,t.yMax)}:e}function Vi(e,t,n){let r=ct(e),i=ct(t),a=ct(n);return r<=i?a>=r&&a<=i:a>=r||a<=i}function Hi(e){return Math.round(e*1e4)/1e4}var Ui=184,Wi=176,Gi=9,Ki=4,qi=.45;function Ji(e){let t=e.clientWidth,n=e.clientHeight;if(t===0||n===0){let r=e.parentElement?.getBoundingClientRect();r&&(t=r.width,n=r.height)}return{width:t,height:n}}function Yi(e,t,n){return t?.hostWidthPx!==void 0&&t.hostHeightPx!==void 0?(e.style.width=`${t.hostWidthPx}px`,e.style.height=`${t.hostHeightPx}px`,e.style.display=`block`,!0):(n&&(e.style.removeProperty(`width`),e.style.removeProperty(`height`),e.style.removeProperty(`display`)),!1)}function Xi(e,t){let n=t.querySelector(`svg, .container`);n&&e.observe(n)}function Zi(e){let t=0;for(let n of e)n!==void 0&&n.length>t&&(t=n.length);return t*7}function Qi(e){if(!e)return{fx:1,fy:1};let t=1-(e.left+e.right)/100,n=1-(e.top+e.bottom)/100;return{fx:t>0?t:1,fy:n>0?n:1}}function $i(e,t){let{fx:n,fy:r}=Qi(t),i=e*n,a=e*r,o=-e/2+e*(t?.left??0)/100,s=-e/2+e*(t?.top??0)/100;return{x:o,y:s,width:i,height:a,viewBox:`${o} ${s} ${i} ${a}`,radiusOffset:0}}function ea(e){if(e.faceDiameter===void 0)return;let t=e.faceDiameter/368;return Number.isFinite(t)&&t>0?t:void 0}function ta(e,t,n){let r=e.containerPx?.width??0,i=e.containerPx?.height??0;if(!(!Number.isFinite(r)||!Number.isFinite(i)||r<=0||i<=0))return Math.min(r/t,i/n)}function na(e,t){let n=e.containerPx?.width??0,r=e.containerPx?.height??0;if(!Number.isFinite(n)||!Number.isFinite(r)||n<=0||r<=0)return;let i=Math.min(n/t.width,r/t.height);return Number.isFinite(i)&&i>0?i:void 0}function ra(e,t,n,r,i,a=!1){let o={...e,scale:n,labelReserve:r,labelsHidden:i,clipsAdjusted:a};return t&&(o.hostWidthPx=e.width*n,o.hostHeightPx=e.height*n),o}function ia(e,t,n){let r=(Wi+e.basePadding)*2,{fx:i,fy:a}=Qi(n),o=e=>2*(187+t/e),s=r,c=!1;if(t>0){let n=ea(e);if(n!==void 0){let e=Math.max(r,o(n));c=t/n*2/e>qi,s=c?r:e}else{let n=ta(e,i,a);n===void 0?s=Math.max(r,o(1)):2*t/n>.45?c=!0:s=Math.max(r,374/(1-2*t/n))}}return{side:s,labelsHidden:c}}function aa(e,t,n,r){let i=r/n,a=Math.max(0,(.5-i/t)*100),o=e.bottom>a?a:e.bottom,s=e.top>a?a:e.top;return o===e.bottom&&s===e.top?e:{...e,top:s,bottom:o}}function oa(e){let t=e.labelWidthPx??0,n=t>0?Gi+t+Ki:0;if(e.zoomToFitArc&&e.areas&&e.areas.length>0)return sa(e,n);let r=(Wi+e.basePadding)*2,i=e.clips,{side:a,labelsHidden:o}=ia(e,n,i),s=e.labelDropPx??0;if(s>0&&n>0&&!o&&i){for(let t=0;t<2;t++){let t=ea(e)??na(e,$i(a,i))??1,r=aa(i,a,t,s);if(r===i)break;i=r;let c=ia(e,n,i);a=c.side,o=c.labelsHidden}if(o){i=e.clips;let t=ia(e,n,i);a=t.side,o=t.labelsHidden}}let c=$i(a,i),l=ea(e),u=l??na(e,c)??1;return ra(c,l!==void 0,u,(a-r)/2,o,i!==e.clips)}function sa(e,t){let n=0,r=!1,i=ca(e,e.basePadding);if(t>0)for(let a=0;a<2;a++){let a=t/ua(e,i);if(2*a/Math.max(i.width,i.height)>.45){r=!0,n=0,i=ca(e,e.basePadding);break}n=a,i=ca(e,e.basePadding+n)}let a=la(e,i),o=a??na(e,i)??1;return ra(i,a!==void 0,o,r?0:n,r)}function ca(e,t){return Ri({areas:e.areas,outerRadius:Ui,innerRadius:e.innerRadius??Ui,extension:t,targetSize:(Wi+t)*2,fit:e.zoomFit,includeBox:e.zoomIncludeBox})}function la(e,t){if(e.faceDiameter===void 0)return;let n=e.faceDiameter/(2*(Ui+t.radiusOffset));return Number.isFinite(n)&&n>0?n:void 0}function ua(e,t){return la(e,t)??na(e,t)??1}var da=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="70" y="72" width="16" height="8" fill="var(--instrument-frame-primary-color)"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M92 66.6364H83.7941L83.1324 65.4385L84.2794 62.1943H85.2941L82.4265 60.9964H82.0735L81.8057 59.7842C81.7044 59.3261 81.2984 59 80.8292 59H79.1708C78.7016 59 78.2956 59.3261 78.1943 59.7842L77.9265 60.9964H77.5735L74.7059 62.1943H75.7206L76.8676 65.4385L76.2059 66.6364H68V67.0856H69.3235V70.2299H68V79.3137V80.0624L68.5089 82.024C68.9278 83.639 70.1096 84.8535 71.5707 85.1706L80 87L88.4293 85.1706C89.8904 84.8535 91.0722 83.639 91.4911 82.024L92 80.0624V79.3137V70.2299V66.6364ZM86.3529 71.9657V79.3137H70.081V71.9657H86.3529Z" fill="var(--instrument-frame-primary-color)"/>
    <path d="M92 80.0624L91.4911 82.024C91.0722 83.639 89.8904 84.8535 88.4293 85.1706L80 87L71.5707 85.1706C70.1096 84.8535 68.9278 83.639 68.5089 82.024L68 80.0624M92 80.0624H68M92 80.0624V79.3137M83.7941 66.6364H92V70.2299M83.7941 66.6364L83.1324 65.4385M83.7941 66.6364H76.2059M83.1324 65.4385L84.2794 62.1943M83.1324 65.4385H76.8676M84.2794 62.1943H85.2941L82.4265 60.9964H82.0735M84.2794 62.1943H75.7206M68 80.0624V79.3137M76.2059 66.6364H68V67.0856H69.3235V70.2299M76.2059 66.6364L76.8676 65.4385M76.8676 65.4385L75.7206 62.1943M75.7206 62.1943H74.7059L77.5735 60.9964H77.9265M68 79.3137H70.081M68 79.3137V70.2299H69.3235M92 79.3137H86.3529M92 79.3137V70.2299M86.3529 79.3137V71.9657H70.081V79.3137M86.3529 79.3137H70.081M69.3235 70.2299H92M82.0735 60.9964H81.7206H78.2794H77.9265M82.0735 60.9964L81.8057 59.7842C81.7044 59.3261 81.2984 59 80.8292 59H79.1708C78.7016 59 78.2956 59.3261 78.1943 59.7842L77.9265 60.9964" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,fa=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect 
    x="74" 
    y="72" 
    width="16" 
    height="8" 
    fill="var(--instrument-frame-primary-color)"/>
<path
     fill-rule="evenodd"
     clip-rule="evenodd"
     d="M68 66.6364H76.2059L76.8676 65.4385L75.7206 62.1943H74.7059L77.5735 60.9964H77.9265L78.1943 59.7842C78.2956 59.3261 78.7016 59 79.1708 59H80.8292C81.2984 59 81.7044 59.3261 81.8057 59.7842L82.0735 60.9964H82.4265L85.2941 62.1943H84.2794L83.1324 65.4385L83.7941 66.6364H92V67.0856H90.6765V70.2299H92V79.3137V80.0624L91.4911 82.024C91.0722 83.639 89.8904 84.8535 88.4293 85.1706L80 87L71.5707 85.1706C70.1096 84.8535 68.9278 83.639 68.5089 82.024L68 80.0624V79.3137V70.2299V66.6364ZM74 72V79.3137H90V72H74Z"
     fill="var(--instrument-frame-primary-color)" />
  <path
     d="M68 80.0624L68.5089 82.024C68.9278 83.639 70.1096 84.8535 71.5707 85.1706L80 87L88.4293 85.1706C89.8904 84.8535 91.0722 83.639 91.4911 82.024L92 80.0624M68 80.0624H92M68 80.0624V79.3137M76.2059 66.6364H68V70.2299M76.2059 66.6364L76.8676 65.4385M76.2059 66.6364H83.7941M76.8676 65.4385L75.7206 62.1943M76.8676 65.4385H83.1324M75.7206 62.1943H74.7059L77.5735 60.9964H77.9265M75.7206 62.1943H84.2794M92 80.0624V79.3137M83.7941 66.6364H92V67.0856H90.6765V70.2299M83.7941 66.6364L83.1324 65.4385M83.1324 65.4385L84.2794 62.1943M84.2794 62.1943H85.2941L82.4265 60.9964H82.0735M92 79.3137H90M92 79.3137V70.2299H90.6765M68 79.3137H74M68 79.3137V70.2299M74 79.3137V72H90V79.3137M74 79.3137H90M90.6765 70.2299H68M77.9265 60.9964H78.2794H81.7206H82.0735M77.9265 60.9964L78.1943 59.7842C78.2956 59.3261 78.7016 59 79.1708 59H80.8292C81.2984 59 81.7044 59.3261 81.8057 59.7842L82.0735 60.9964"
     vector-effect="non-scaling-stroke"
     stroke="var(--instrument-tick-mark-secondary-color)" />
</svg>
`,pa=e=>k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M10 74.9115L13.0001 73.5L48.0001 73L52.8784 68.1352H75.4774L76.1648 65.6631L75.0908 62.3099H74.3605L76.6374 60H83.3628L85.6396 62.3099H84.9093L83.8353 65.6631L84.5227 68.1352H107.122L112 73L147 73.5L150 74.9115L150 80.16L147 81.8885L146.846 83.4086C146.791 83.95 146.452 84.3687 146.031 84.4377C145.96 84.4493 145.89 84.4476 145.818 84.4479C144.806 84.451 136.713 84.4895 128.544 84.9172C124.018 85.1541 118.577 85.6275 113.488 86.1336C102.356 87.2408 91.1872 88 80.0001 88C68.813 88 57.6441 87.2408 46.5119 86.1336C41.4228 85.6275 35.9817 85.1541 31.456 84.9172C23.2869 84.4895 15.194 84.451 14.182 84.4479C14.1104 84.4476 14.0397 84.4493 13.969 84.4377C13.5479 84.3687 13.2092 83.95 13.1543 83.4086L13.0001 81.8885L10.0001 80.16L10 74.9115Z" fill="${e}"/>
    <path d="M48.0001 73L13.0001 73.5L10 74.9115L10.0001 80.16M48.0001 73L52.8784 68.1352H75.4774M48.0001 73H112M75.4774 68.1352L76.1648 65.6631M75.4774 68.1352H84.5227M76.1648 65.6631L75.0908 62.3099M76.1648 65.6631H83.8353M75.0908 62.3099H74.3605L76.6374 60H83.3628L85.6396 62.3099H84.9093M75.0908 62.3099H84.9093M10.0001 80.16L13.0001 81.8885L13.1543 83.4086C13.2092 83.95 13.5479 84.3687 13.969 84.4377C14.0397 84.4493 14.1104 84.4476 14.182 84.4479C15.194 84.451 23.2869 84.4895 31.456 84.9172C35.9817 85.1541 41.4228 85.6275 46.5119 86.1336C57.6441 87.2408 68.813 88 80.0001 88C91.1872 88 102.356 87.2408 113.488 86.1336C118.577 85.6275 124.018 85.1541 128.544 84.9172C136.713 84.4895 144.806 84.451 145.818 84.4479C145.89 84.4476 145.96 84.4493 146.031 84.4377C146.452 84.3687 146.791 83.95 146.846 83.4086L147 81.8885L150 80.16M10.0001 80.16H150M112 73L147 73.5L150 74.9115L150 80.16M112 73L107.122 68.1352H84.5227M84.5227 68.1352L83.8353 65.6631M83.8353 65.6631L84.9093 62.3099" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
  </svg>
`,ma=pa(`var(--instrument-frame-primary-color)`),ha=pa(`var(--container-background-color)`),ga=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M80.0007 151.999C73.373 152 68 146.627 68 139.999L68 128.776L68 104.642L68 56.7557L68 19.9992C68 13.3717 73.3726 7.99916 80 7.99916C86.6274 7.99916 92 13.3717 92 19.9992L92 23.108L92 56.7557L92 108.092L92 137.357L92 139.999C92 146.626 86.6278 151.999 80.0007 151.999Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M85.8387 85.9422L73.9677 85.9422L73.9677 74.336L85.8387 74.336L85.8387 85.9422Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M92 108.092L86.2419 108.092M92 108.092L92 56.7557M92 108.092L92 137.357M86.2419 108.092L84.4516 104.642L72.9355 104.642L68 104.642M86.2419 108.092L86.2419 137.357L92 137.357M68 104.642L68 128.776L68 139.999C68 146.627 73.373 152 80.0007 151.999V151.999C86.6278 151.999 92 146.626 92 139.999L92 137.357M68 104.642L68 56.7557M68 56.7557L68 19.9992C68 13.3717 73.3726 7.99916 80 7.99916V7.99916V7.99916C86.6274 7.99916 92 13.3717 92 19.9992L92 23.108M68 56.7557L86.2419 56.7557M92 56.7557L86.2419 56.7557M92 56.7557L92 23.108M86.2419 56.7557L86.2419 23.108L92 23.108M73.9677 85.9422L85.8387 85.9422M73.9677 85.9422L73.9677 74.336M73.9677 85.9422L76.5806 83.424M85.8387 85.9422L85.8387 74.336M85.8387 85.9422L83.2258 83.424M85.8387 74.336L73.9677 74.336M85.8387 74.336L83.2258 76.8541M73.9677 74.336L76.5806 76.8541M76.5806 83.424L83.2258 83.424M76.5806 83.424L76.5806 76.8541M83.2258 83.424L83.2258 76.8541M83.2258 76.8541L76.5806 76.8541" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,_a=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect x="60" y="52" width="40" height="3" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M80.0036 77.9545V87C80.0036 87 83.7476 81.9921 82.7622 80C82.1928 78.8489 80.0036 77.9545 80.0036 77.9545Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80.0036 87V77.9545C80.0036 77.9545 77.8718 78.8255 77.2684 79.9545C77.2603 79.9697 77.2525 79.9848 77.245 80C76.2596 81.9921 80.0036 87 80.0036 87Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80.0036 87H90.7728C92.982 87 94.7728 85.2091 94.7728 83V80H82.7622C83.7476 81.9921 80.0036 87 80.0036 87Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M65.2344 79.9545V83C65.2344 85.2091 67.0252 87 69.2344 87H80.0036C80.0036 87 76.2596 81.9921 77.245 80C77.2525 79.9848 77.2603 79.9697 77.2684 79.9545H65.2344Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M69 64H65.2344V74V79.9545H77.2684C77.8718 78.8255 80.0036 77.9545 80.0036 77.9545L80.0036 64H69Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M94.7728 64H91H80.0036L80.0036 77.9545C80.0036 77.9545 82.1928 78.8489 82.7622 80H94.7728V79.9545V74V64Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M91 64V52H69V64H80.0036H91Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M91 52L94 49H66L69 52H91Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M66 49H94H94.7728L93 47.2273H83.0301H81.184H78.8232H76.9771H67.133L65.2344 49H66Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M83.0301 39H77.0036L76.9771 47.2273H78.8232L78.7728 40.4205H81.2344L81.184 47.2273H83.0301V39Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M91 64H94.7728V74V79.9545V80M91 64V52M91 64H80.0036M91 52L94 49M91 52H69M94 49H66M94 49H94.7728L93 47.2273H83.0301M66 49L69 52M66 49H65.2344L67.133 47.2273H76.9771M69 52V64M69 64H65.2344V74V79.9545M69 64H80.0036M76.9771 47.2273H83.0301M76.9771 47.2273L77.0036 39H83.0301V47.2273M76.9771 47.2273H78.8232M83.0301 47.2273H81.184M65.2344 79.9545V83C65.2344 85.2091 67.0252 87 69.2344 87H80.0036M65.2344 79.9545H77.2684M78.8232 47.2273L78.7728 40.4205H81.2344L81.184 47.2273M78.8232 47.2273H81.184M80.0036 64L80.0036 77.9545M80.0036 87H90.7728C92.982 87 94.7728 85.2091 94.7728 83V80M80.0036 87V77.9545M80.0036 87C80.0036 87 83.7476 81.9921 82.7622 80M80.0036 87C80.0036 87 76.2596 81.9921 77.245 80C77.2525 79.9848 77.2603 79.9697 77.2684 79.9545M80.0036 77.9545C80.0036 77.9545 82.1928 78.8489 82.7622 80M80.0036 77.9545C80.0036 77.9545 77.8718 78.8255 77.2684 79.9545M82.7622 80H94.7728" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M80.0036 77.9545V87C80.0036 87 83.7476 81.9921 82.7622 80C82.1928 78.8489 80.0036 77.9545 80.0036 77.9545Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80.0036 87V77.9545C80.0036 77.9545 77.8718 78.8255 77.2684 79.9545C77.2603 79.9697 77.2525 79.9848 77.245 80C76.2596 81.9921 80.0036 87 80.0036 87Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80.0036 87H90.7728C92.982 87 94.7728 85.2091 94.7728 83V80H82.7622C83.7476 81.9921 80.0036 87 80.0036 87Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M65.2344 79.9545V83C65.2344 85.2091 67.0252 87 69.2344 87H80.0036C80.0036 87 76.2596 81.9921 77.245 80C77.2525 79.9848 77.2603 79.9697 77.2684 79.9545H65.2344Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M94.7728 64H92.3113H80.0036L80.0036 77.9545C80.0036 77.9545 82.1928 78.8489 82.7622 80H94.7728V79.9545V74V64Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M65.2344 79.9545V83C65.2344 85.2091 67.0252 87 69.2344 87H80.0036M65.2344 79.9545V74V64H67.6959H80.0036M65.2344 79.9545H77.2684M80.0036 64H92.3113H94.7728V74V79.9545V80M80.0036 64L80.0036 77.9545M80.0036 87H90.7728C92.982 87 94.7728 85.2091 94.7728 83V80M80.0036 87V77.9545M80.0036 87C80.0036 87 83.7476 81.9921 82.7622 80M80.0036 87C80.0036 87 76.2596 81.9921 77.245 80C77.2525 79.9848 77.2603 79.9697 77.2684 79.9545M80.0036 77.9545C80.0036 77.9545 82.1928 78.8489 82.7622 80M80.0036 77.9545C80.0036 77.9545 77.8718 78.8255 77.2684 79.9545M82.7622 80H94.7728" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="87.498" cy="70.0003" rx="1.5" ry="2" transform="rotate(45 87.498 70.0003)" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="72.4983" cy="70" rx="1.5" ry="2" transform="rotate(-45 72.4983 70)" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M96 55L91 60" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M64 55L69 60" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,va=e=>k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M140.366 87.1181H21.3855V83.0385L12.4844 80V71H18.4844V63L22 44H26V63H32.4844V53.5604V50.1099L31 48.9973L32 48.1429H37.4294L37.2747 38.5H39.5L41.88 48.1429H45.8152C48.7962 48.1429 51.7388 48.8152 54.4239 50.1099H52.5695L50.3443 53.5604V71H117.416L124.833 64.1236H148C148 64.1236 146.5 67 144.5 71C143.302 73.3966 143.5 75.6209 143.5 75.6209C145.701 75.6209 147.484 77.4047 147.484 79.6053V80C147.484 83.9312 144.297 87.1181 140.366 87.1181Z" fill="${e}"/>
    <path d="M12.4844 80H147.484M12.4844 80L21.3855 83.0385V87.1181H140.366C144.297 87.1181 147.484 83.9312 147.484 80V80M12.4844 80V71H18.4844M147.484 80V79.6053C147.484 77.4047 145.701 75.6209 143.5 75.6209V75.6209C143.5 75.6209 143.302 73.3966 144.5 71C146.5 67 148 64.1236 148 64.1236H124.833L117.416 71H50.3443M18.4844 71H50.3443M18.4844 71V63L22 44H26V63H32.4844V53.5604M32.4844 53.5604H50.3443M32.4844 53.5604V50.1099M50.3443 53.5604L52.5695 50.1099H32.4844M50.3443 53.5604V71M32.4844 50.1099H54.4239V50.1099C51.7388 48.8152 48.7962 48.1429 45.8152 48.1429H41.88M32.4844 50.1099L31 48.9973L32 48.1429H37.4294M41.88 48.1429L39.5 38.5H37.2747L37.4294 48.1429M41.88 48.1429H37.4294" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
    <circle cx="136" cy="70" r="2" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
  </svg>
`,ya=va(`var(--instrument-frame-primary-color)`),ba=va(`var(--container-background-color)`),xa=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M66.5 146.75L66.5 32.1402C66.5 11.5 80 9.25 80 9.25C80 9.25 93.5 11.5 93.5 32.1402L93.5 146.75C93.5 147.855 92.6046 148.75 91.5 148.75L90.125 148.75L69.875 148.75L68.5 148.75C67.3954 148.75 66.5 147.855 66.5 146.75Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M74 122L64 122L64 118L72 118L75 114L85 114L88 118L96 118L96 122L86 122L86 138.75L74 138.75L74 122Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,Sa=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M80 77.9545V87C80 87 83.744 81.9921 82.7586 80C82.1892 78.8489 80 77.9545 80 77.9545Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80 87V77.9545C80 77.9545 77.8682 78.8255 77.2648 79.9545C77.2567 79.9697 77.2489 79.9848 77.2414 80C76.256 81.9921 80 87 80 87Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80 87H90.7692C92.9784 87 94.7692 85.2091 94.7692 83V80H82.7586C83.744 81.9921 80 87 80 87Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M65.2308 79.9545V83C65.2308 85.2091 67.0216 87 69.2308 87H80C80 87 76.256 81.9921 77.2414 80C77.2489 79.9848 77.2567 79.9697 77.2648 79.9545H65.2308Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M67.6923 64H65.2308V74V79.9545H77.2648C77.8682 78.8255 80 77.9545 80 77.9545L80 64H67.6923Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M94.7692 64H92.3077H80L80 77.9545C80 77.9545 82.1892 78.8489 82.7586 80H94.7692V79.9545V74V64Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M92.3077 64V57.75H67.6923V64H80H92.3077Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M92.3077 57.75L94.7692 52.6364H65.2308L67.6923 57.75H92.3077Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M65.2308 52.6364H94.7692H96L92.3077 49.2273H83.0265H81.1804H78.8196H76.9735H67.6923L64 52.6364H65.2308Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M83.0265 41H77L76.9735 49.2273H78.8196L78.7692 42.4205H81.2308L81.1804 49.2273H83.0265V41Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M92.3077 64H94.7692V74V79.9545V80M92.3077 64V57.75M92.3077 64H80M92.3077 57.75L94.7692 52.6364M92.3077 57.75H67.6923M94.7692 52.6364H65.2308M94.7692 52.6364H96L92.3077 49.2273H83.0265M65.2308 52.6364L67.6923 57.75M65.2308 52.6364H64L67.6923 49.2273H76.9735M67.6923 57.75V64M67.6923 64H65.2308V74V79.9545M67.6923 64H80M76.9735 49.2273H83.0265M76.9735 49.2273L77 41H83.0265V49.2273M76.9735 49.2273H78.8196M83.0265 49.2273H81.1804M65.2308 79.9545V83C65.2308 85.2091 67.0216 87 69.2308 87H80M65.2308 79.9545H77.2648M78.8196 49.2273L78.7692 42.4205H81.2308L81.1804 49.2273M78.8196 49.2273H81.1804M80 64L80 77.9545M80 87H90.7692C92.9784 87 94.7692 85.2091 94.7692 83V80M80 87V77.9545M80 87C80 87 83.744 81.9921 82.7586 80M80 87C80 87 76.256 81.9921 77.2414 80C77.2489 79.9848 77.2567 79.9697 77.2648 79.9545M80 77.9545C80 77.9545 82.1892 78.8489 82.7586 80M80 77.9545C80 77.9545 77.8682 78.8255 77.2648 79.9545M82.7586 80H94.7692M75.5862 72L75.0345 71H71.7241L72.2759 72H75.5862ZM83.8621 72L84.4138 71H87.7241L87.1724 72H83.8621Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M79.4545 70V65.7333H74V64.1818H74.5455V55.6485V38.1939V19.1879V7.16364H74V6H86V7.16364V64.1818V65.7333H84.0909V70H79.4545Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M74.5455 64.1818H74V65.7333H79.4545V70H84.0909V65.7333H86V64.1818M74.5455 64.1818H86M74.5455 64.1818V55.6485M74.5455 7.16364H74V6H86V7.16364M74.5455 7.16364H86M74.5455 7.16364V19.1879M86 64.1818V7.16364M74.5455 19.1879H81.9091M74.5455 19.1879V38.1939M74.5455 38.1939H81.9091M74.5455 38.1939V55.6485M74.5455 55.6485H81.9091" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M80.0036 77.9545V87C80.0036 87 83.7476 81.9921 82.7622 80C82.1928 78.8489 80.0036 77.9545 80.0036 77.9545Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80.0036 87V77.9545C80.0036 77.9545 77.8718 78.8255 77.2684 79.9545C77.2603 79.9697 77.2525 79.9848 77.245 80C76.2596 81.9921 80.0036 87 80.0036 87Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80.0036 87H90.7728C92.982 87 94.7728 85.2091 94.7728 83V80H82.7622C83.7476 81.9921 80.0036 87 80.0036 87Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M65.2344 79.9545V83C65.2344 85.2091 67.0252 87 69.2344 87H80.0036C80.0036 87 76.2596 81.9921 77.245 80C77.2525 79.9848 77.2603 79.9697 77.2684 79.9545H65.2344Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M67.6959 64H65.2344V74V79.9545H77.2684C77.8718 78.8255 80.0036 77.9545 80.0036 77.9545L80.0036 64H67.6959Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M94.7728 64H92.3113H80.0036L80.0036 77.9545C80.0036 77.9545 82.1928 78.8489 82.7622 80H94.7728V79.9545V74V64Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M65.2344 79.9545V83C65.2344 85.2091 67.0252 87 69.2344 87H80.0036M65.2344 79.9545V74V64H67.6959H80.0036M65.2344 79.9545H77.2684M80.0036 64H92.3113H94.7728V74V79.9545V80M80.0036 64L80.0036 77.9545M80.0036 87H90.7728C92.982 87 94.7728 85.2091 94.7728 83V80M80.0036 87V77.9545M80.0036 87C80.0036 87 83.7476 81.9921 82.7622 80M80.0036 87C80.0036 87 76.2596 81.9921 77.245 80C77.2525 79.9848 77.2603 79.9697 77.2684 79.9545M80.0036 77.9545C80.0036 77.9545 82.1928 78.8489 82.7622 80M80.0036 77.9545C80.0036 77.9545 77.8718 78.8255 77.2684 79.9545M82.7622 80H94.7728M75.5898 72L75.0381 71H71.7277L72.2795 72H75.5898ZM83.8657 72L84.4174 71H87.7277L87.176 72H83.8657Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,Ca=e=>k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M119.273 71V66.7333H112V65.1818H112.727V56.6485V39.1939V20.1879V8.16364H112V7H128V8.16364V65.1818V66.7333H125.455V71H119.273Z" fill="${e}"/>
    <path d="M112.727 65.1818H112V66.7333H119.273V71H125.455V66.7333H128V65.1818M112.727 65.1818H128M112.727 65.1818V56.6485M112.727 8.16364H112V7H128V8.16364M112.727 8.16364H128M112.727 8.16364V20.1879M128 65.1818V8.16364M112.727 20.1879H122.545M112.727 20.1879V39.1939M112.727 39.1939H122.545M112.727 39.1939V56.6485M112.727 56.6485H122.545" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
    <path d="M140.366 87.1181H21.3855V83.0385L12.4844 80V71V58.5604V54.1099L11 52.9973L12 51.1429H17.4294L17.2747 41.5H19.5L21.88 51.1429H25.2998C28.5783 51.1429 31.7725 52.1816 34.4239 54.1099H32.5695L30.3443 58.5604V71H117.416L124.833 64.1236H146.743C146.743 64.1236 143.808 67.7438 142.292 70.614C141.041 72.9834 139.325 77.1044 139.325 77.1044L143.176 76.4042C145.419 75.9963 147.484 77.7198 147.484 80C147.484 83.9312 144.297 87.1181 140.366 87.1181Z" fill="${e}"/>
    <path d="M12.4844 80H147.484M12.4844 80L21.3855 83.0385V87.1181H140.366C144.297 87.1181 147.484 83.9312 147.484 80V80M12.4844 80V71M147.484 80V80C147.484 77.7198 145.419 75.9963 143.176 76.4042L139.325 77.1044C139.325 77.1044 141.041 72.9834 142.292 70.614C143.808 67.7438 146.743 64.1236 146.743 64.1236H124.833L117.416 71H30.3443M12.4844 71V58.5604M12.4844 71H30.3443M12.4844 58.5604H30.3443M12.4844 58.5604V54.1099M30.3443 58.5604L32.5695 54.1099H12.4844M30.3443 58.5604V71M12.4844 54.1099H34.4239V54.1099C31.7725 52.1816 28.5783 51.1429 25.2998 51.1429H21.88M12.4844 54.1099L11 52.9973L12 51.1429H17.4294M21.88 51.1429L19.5 41.5H17.2747L17.4294 51.1429M21.88 51.1429H17.4294" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
    <path d="M95.2727 71V66.7333H88V65.1818H88.7273V56.6485V39.1939V20.1879V8.16364H88V7H104V8.16364V65.1818V66.7333H101.455V71H95.2727Z" fill="${e}"/>
    <path d="M88.7273 65.1818H88V66.7333H95.2727V71H101.455V66.7333H104V65.1818M88.7273 65.1818H104M88.7273 65.1818V56.6485M88.7273 8.16364H88V7H104V8.16364M88.7273 8.16364H104M88.7273 8.16364V20.1879M104 65.1818V8.16364M88.7273 20.1879H98.5455M88.7273 20.1879V39.1939M88.7273 39.1939H98.5455M88.7273 39.1939V56.6485M88.7273 56.6485H98.5455" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
    <path d="M71.2727 71V66.7333H64V65.1818H64.7273V56.6485V39.1939V20.1879V8.16364H64V7H80V8.16364V65.1818V66.7333H77.4545V71H71.2727Z" fill="${e}"/>
    <path d="M64.7273 65.1818H64V66.7333H71.2727V71H77.4545V66.7333H80V65.1818M64.7273 65.1818H80M64.7273 65.1818V56.6485M64.7273 8.16364H64V7H80V8.16364M64.7273 8.16364H80M64.7273 8.16364V20.1879M80 65.1818V8.16364M64.7273 20.1879H74.5455M64.7273 20.1879V39.1939M64.7273 39.1939H74.5455M64.7273 39.1939V56.6485M64.7273 56.6485H74.5455" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
    <path d="M47.2727 71V66.7333H40V65.1818H40.7273V56.6485V39.1939V20.1879V8.16364H40V7H56V8.16364V65.1818V66.7333H53.4545V71H47.2727Z" fill="${e}"/>
    <path d="M40.7273 65.1818H40V66.7333H47.2727V71H53.4545V66.7333H56V65.1818M40.7273 65.1818H56M40.7273 65.1818V56.6485M40.7273 8.16364H40V7H56V8.16364M40.7273 8.16364H56M40.7273 8.16364V20.1879M56 65.1818V8.16364M40.7273 20.1879H50.5455M40.7273 20.1879V39.1939M40.7273 39.1939H50.5455M40.7273 39.1939V56.6485M40.7273 56.6485H50.5455" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
  </svg>
`,wa=Ca(`var(--instrument-frame-primary-color)`),Ta=Ca(`var(--container-background-color)`),Ea=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M66.5 146.75L66.5 32.1402C66.5 11.5 80 9.25 80 9.25C80 9.25 93.5 11.5 93.5 32.1402L93.5 146.75C93.5 147.855 92.6046 148.75 91.5 148.75L90.125 148.75L69.875 148.75L68.5 148.75C67.3954 148.75 66.5 147.855 66.5 146.75Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M74 140L64 140L64 128L72 128L75 124L85 124L88 128L96 128L96 140L86 140L86 148.75L74 148.75L74 140Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M76.3472 21.6677C78.2643 22.1593 79.8323 23.5259 80.5811 25.3486L80.7239 25.7307L83.565 34.1692L77.6776 27.4895C76.2735 25.8965 75.7779 23.7047 76.3472 21.6677Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M76.3472 45.6667C78.2643 46.1584 79.8323 47.5249 80.5811 49.3476L80.7239 49.7297L83.565 58.1682L77.6776 51.4885C76.2735 49.8955 75.7779 47.7037 76.3472 45.6667Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M76.3472 69.6667C78.2643 70.1584 79.8323 71.5249 80.5811 73.3476L80.7239 73.7297L83.565 82.1682L77.6776 75.4885C76.2735 73.8955 75.7779 71.7037 76.3472 69.6667Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M76.3472 93.6667C78.2643 94.1584 79.8323 95.5249 80.5811 97.3476L80.7239 97.7297L83.565 106.168L77.6776 99.4885C76.2735 97.8955 75.7779 95.7037 76.3472 93.6667Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,Da=e=>k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M132.366 87.1181H29.3855V83.0385L20.4844 80V71.5412H24V68.7912H20.4844V66.0412H24V51.1429H31.5L36 66.0412H48L51.5 71.5412H54.4157L55.575 61.5604L54.0915 57.1099H52.608L54.4157 54.1429H57.4294L54.4624 44.5H56.6877L61.88 54.1429C65.3312 54.1429 68.772 54.5206 72.1409 55.2692L80.4239 57.1099H78.5695L76.3443 61.5604L88.5 71.0827C102.374 69.3897 109.424 63.1236 109.424 63.1236H118L115.5 51.1429H118L122 63.1236H140.743C132 69.5 130.325 77.1044 130.325 77.1044L135.162 76.321C137.428 75.9539 139.484 77.7039 139.484 80C139.484 83.9312 136.297 87.1181 132.366 87.1181Z" fill="${e}"/>
<path d="M20.4844 80H139.484M20.4844 80L29.3855 83.0385V87.1181H132.366C136.297 87.1181 139.484 83.9312 139.484 80V80M20.4844 80V71.5412H24V68.7912H20.4844V66.0412H24M139.484 80V80C139.484 77.7039 137.428 75.9539 135.162 76.321L130.325 77.1044C130.325 77.1044 132 69.5 140.743 63.1236H122M54.4157 71.5412C54.4157 71.5412 75.9997 71.5 81.5 71.5C100 71.5 109.424 63.1236 109.424 63.1236H118M54.4157 71.5412L55.575 61.5604M54.4157 71.5412H51.5L48 66.0412H36M55.575 61.5604H76.3443M55.575 61.5604L54.0915 57.1099H78.5695L76.3443 61.5604M76.3443 61.5604L88.5 71.0827M61.88 54.1429V54.1429C65.3312 54.1429 68.772 54.5206 72.1409 55.2692L80.4239 57.1099H52.608L54.4157 54.1429H57.4294M61.88 54.1429L56.6877 44.5H54.4624L57.4294 54.1429M61.88 54.1429H57.4294M24 66.0412V51.1429H31.5L36 66.0412M24 66.0412H36M122 63.1236L118 51.1429H115.5L118 63.1236M122 63.1236H118" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,Oa=Da(`var(--instrument-frame-primary-color)`),ka=Da(`var(--container-background-color)`),Aa=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M80 18.25C80 18.25 93.5 18.25 93.5 51.1402L93.5 94.2378L93.5 122L93.5 128L93.5 135L93.5 139.75C93.5 140.855 92.6046 141.75 91.5 141.75L90.125 141.75L69.875 141.75L68.5 141.75C67.3954 141.75 66.5 140.855 66.5 139.75L66.5 135L66.5 128L66.5 122L66.5 51.1402C66.5 18.25 80 18.25 80 18.25Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M66.5 135L66.5 139.75C66.5 140.855 67.3954 141.75 68.5 141.75L69.875 141.75L90.125 141.75L91.5 141.75C92.6046 141.75 93.5 140.855 93.5 139.75L93.5 135M66.5 135L93.5 135M66.5 135L66.5 128M93.5 135L93.5 128M93.5 122L93.5 94.2378L93.5 51.1402C93.5 18.25 80 18.25 80 18.25C80 18.25 66.5 18.25 66.5 51.1402L66.5 122M93.5 122L93.5 128M93.5 122L88 122L88 128M93.5 128L88 128M66.5 128L66.5 122M66.5 128L72 128M88 128L72 128M66.5 122L72 122L72 128M82 34L81.5 42.5L78.5 42.5L78 34L82 34Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M71 103.375L64.25 103.375L64.25 94.375C64.25 94.375 67.4029 89.009 69.5 86C71.7705 82.7422 75.5 78.625 75.5 78.625L84.5 78.625C84.5 78.625 87.8347 82.9839 90 86C92.2512 89.1357 95.75 94.375 95.75 94.375L95.75 103.375L89 103.375L85.625 103.5L74.375 103.5L71 103.375Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M74.375 103.5L71 103.375L64.25 103.375L64.25 94.375C64.25 94.375 67.4029 89.009 69.5 86C71.7705 82.7422 75.5 78.625 75.5 78.625M74.375 103.5L85.625 103.5M74.375 103.5L74.375 91C74.6384 86.5926 75.5 78.625 75.5 78.625M85.625 103.5L89 103.375L95.75 103.375L95.75 94.375C95.75 94.375 92.2512 89.1357 90 86C87.8347 82.9839 84.5 78.625 84.5 78.625M85.625 103.5L85.625 91C85.3616 86.5925 84.5 78.625 84.5 78.625M84.5 78.625L75.5 78.625" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M85.625 97.625L85.625 103.25L83.375 104.375L76.625 104.375L74.375 103.25L74.375 97.625L76.625 101L83.375 101L85.625 97.625Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M83.375 101L85.625 97.625L85.625 103.25L83.375 104.375M83.375 101L76.625 101M83.375 101L83.375 104.375M76.625 101L74.375 97.625L74.375 103.25L76.625 104.375M76.625 101L76.625 104.375M76.625 104.375L83.375 104.375" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,ja=e=>k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<mask id="path-1-inside-1_208_29995" fill="white">
<path d="M125.032 93.6077C139.926 93.6077 152 81.5337 152 66.6396L11.7453 66.6396L11.7453 93.6076L125.032 93.6077Z"/>
</mask>
<path d="M125.032 93.6077C139.926 93.6077 152 81.5337 152 66.6396L11.7453 66.6396L11.7453 93.6076L125.032 93.6077Z" fill="${e}"/>
<path d="M152 66.6396L154 66.6396L154 64.6396L152 64.6396L152 66.6396ZM11.7453 66.6396L11.7453 64.6396L9.74529 64.6396L9.74529 66.6396L11.7453 66.6396ZM11.7453 93.6076L9.74528 93.6076L9.74528 95.6076L11.7453 95.6076L11.7453 93.6076ZM125.032 95.6077C141.031 95.6077 154 82.6382 154 66.6396L150 66.6396C150 80.4291 138.821 91.6077 125.032 91.6077L125.032 95.6077ZM152 64.6396L11.7453 64.6396L11.7453 68.6396L152 68.6396L152 64.6396ZM9.74529 66.6396L9.74528 93.6076L13.7453 93.6076L13.7453 66.6396L9.74529 66.6396ZM11.7453 95.6076L125.032 95.6077L125.032 91.6077L11.7453 91.6076L11.7453 95.6076Z" fill="var(--instrument-tick-mark-secondary-color)" mask="url(#path-1-inside-1_208_29995)"/>
</svg>
`,Ma=ja(`var(--instrument-frame-primary-color)`),Na=ja(`var(--container-background-color)`),Pa=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M80 9.18359C71.6308 14.0249 66 23.0737 66 33.4377L66 151.06L94 151.06L94 33.4377C94 23.0737 88.3692 14.0249 80 9.18359Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80 9.18359C71.6308 14.0249 66 23.0737 66 33.4377L66 151.06L94 151.06L94 33.4377C94 23.0737 88.3692 14.0249 80 9.18359Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,Fa=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M67.1154 52.6364H93.8846H95L91.6538 49.2273H85.9615H75.0385H69.3462L66 52.6364H67.1154Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M67.1154 79.9545H93.8846V74H91.6538H69.3462H67.1154V79.9545Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M67.1154 83C67.1154 85.2091 68.9062 87 71.1154 87H89.8846C92.0938 87 93.8846 85.2091 93.8846 83V79.9545H67.1154V83Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M69.3462 64H67.1154V74H69.3462V64Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M91.6538 64V57.75H69.3462V64V74H91.6538V64Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M93.8846 64H91.6538V74H93.8846V64Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M91.6538 57.75L93.8846 52.6364H67.1154L69.3462 57.75H91.6538Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M82.7308 41H78.2692L75.0385 49.2273H76.7115L79.3846 42.4205H81.6154L84.2885 49.2273H85.9615L82.7308 41Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M91.6538 64H93.8846V74M91.6538 64V57.75M91.6538 64V74M91.6538 57.75L93.8846 52.6364M91.6538 57.75H69.3462M93.8846 52.6364H67.1154M93.8846 52.6364H95L91.6538 49.2273H85.9615M67.1154 52.6364L69.3462 57.75M67.1154 52.6364H66L69.3462 49.2273H75.0385M69.3462 57.75V64M69.3462 64H67.1154V74M69.3462 64V74M75.0385 49.2273H85.9615M75.0385 49.2273L78.2692 41H82.7308L85.9615 49.2273M75.0385 49.2273H76.7115L79.3846 42.4205H81.6154L84.2885 49.2273H85.9615M93.8846 79.9545V83C93.8846 85.2091 92.0938 87 89.8846 87H71.1154C68.9062 87 67.1154 85.2091 67.1154 83V79.9545M93.8846 79.9545H67.1154M93.8846 79.9545V74M67.1154 79.9545V74M67.1154 74H69.3462M93.8846 74H91.6538M91.6538 74H69.3462" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,Ia=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M80 77.9545V87C80 87 83.744 81.9921 82.7586 80C82.1892 78.8489 80 77.9545 80 77.9545Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80 87V77.9545C80 77.9545 77.8682 78.8255 77.2648 79.9545C77.2567 79.9697 77.2489 79.9848 77.2414 80C76.256 81.9921 80 87 80 87Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80 87H90.7692C92.9784 87 94.7692 85.2091 94.7692 83V80H82.7586C83.744 81.9921 80 87 80 87Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M65.2308 79.9545V83C65.2308 85.2091 67.0216 87 69.2308 87H80C80 87 76.256 81.9921 77.2414 80C77.2489 79.9848 77.2567 79.9697 77.2648 79.9545H65.2308Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M67.6923 64H65.2308V74V79.9545H77.2648C77.8682 78.8255 80 77.9545 80 77.9545L80 64H67.6923Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M94.7692 64H92.3077H80L80 77.9545C80 77.9545 82.1892 78.8489 82.7586 80H94.7692V79.9545V74V64Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M92.3077 64V57.75H67.6923V64H80H92.3077Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M92.3077 57.75L94.7692 52.6364H65.2308L67.6923 57.75H92.3077Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M65.2308 52.6364H94.7692H96L92.3077 49.2273H86.0265H84.1804H75.8196H73.9735H67.6923L64 52.6364H65.2308Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M82.4615 41H77.5385L73.9735 49.2273H75.8196L78.7692 42.4205H81.2308L84.1804 49.2273H86.0265L82.4615 41Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M92.3077 64H94.7692V74V79.9545V80M92.3077 64V57.75M92.3077 64H80M92.3077 57.75L94.7692 52.6364M92.3077 57.75H67.6923M94.7692 52.6364H65.2308M94.7692 52.6364H96L92.3077 49.2273H86.0265M65.2308 52.6364L67.6923 57.75M65.2308 52.6364H64L67.6923 49.2273H73.9735M67.6923 57.75V64M67.6923 64H65.2308V74V79.9545M67.6923 64H80M73.9735 49.2273H86.0265M73.9735 49.2273L77.5385 41H82.4615L86.0265 49.2273M73.9735 49.2273H75.8196M86.0265 49.2273H84.1804M65.2308 79.9545V83C65.2308 85.2091 67.0216 87 69.2308 87H80M65.2308 79.9545H77.2648M75.8196 49.2273L78.7692 42.4205H81.2308L84.1804 49.2273M75.8196 49.2273H84.1804M80 64L80 77.9545M80 87H90.7692C92.9784 87 94.7692 85.2091 94.7692 83V80M80 87V77.9545M80 87C80 87 83.744 81.9921 82.7586 80M80 87C80 87 76.256 81.9921 77.2414 80C77.2489 79.9848 77.2567 79.9697 77.2648 79.9545M80 77.9545C80 77.9545 82.1892 78.8489 82.7586 80M80 77.9545C80 77.9545 77.8682 78.8255 77.2648 79.9545M82.7586 80H94.7692M75.5862 72L75.0345 71H71.7241L72.2759 72H75.5862ZM83.8621 72L84.4138 71H87.7241L87.1724 72H83.8621Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,La=e=>k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M140.366 87.1181H21.3855V83.0385L12.4844 80V71.5412H92.5943L105.575 58.5604L104.092 54.1099H102.608L104.092 52.9973H106.688V51.1429H107.429L104.462 41.5H106.688L111.88 51.1429C115.331 51.1429 118.772 51.5206 122.141 52.2692L130.424 54.1099H128.57L126.344 58.5604L131.907 64.1236H146.743C146.743 64.1236 143.808 67.7438 142.292 70.614C141.041 72.9834 139.325 77.1044 139.325 77.1044L143.176 76.4042C145.419 75.9963 147.484 77.7198 147.484 80C147.484 83.9312 144.297 87.1181 140.366 87.1181Z" fill="${e}"/>
<path d="M12.4844 80H147.484M12.4844 80L21.3855 83.0385V87.1181H140.366C144.297 87.1181 147.484 83.9312 147.484 80V80M12.4844 80V71.5412H92.5943M147.484 80V80C147.484 77.7198 145.419 75.9963 143.176 76.4042L139.325 77.1044C139.325 77.1044 141.041 72.9834 142.292 70.614C143.808 67.7438 146.743 64.1236 146.743 64.1236H131.907M92.5943 71.5412H97.4157L104.833 64.1236H131.907M92.5943 71.5412L105.575 58.5604M105.575 58.5604H126.344M105.575 58.5604L104.092 54.1099H128.57L126.344 58.5604M126.344 58.5604L131.907 64.1236M111.88 51.1429V51.1429C115.331 51.1429 118.772 51.5206 122.141 52.2692L130.424 54.1099H102.608L104.092 52.9973H106.688V51.1429H107.429M111.88 51.1429L106.688 41.5H104.462L107.429 51.1429M111.88 51.1429H107.429" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,Ra=La(`var(--instrument-frame-primary-color)`),za=La(`var(--container-background-color)`),Ba=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M66.5 74.4634L66.5 42.1402C66.5 9.25 80 9.25 80 9.25C80 9.25 93.5 9.25 93.5 42.1402L93.5 85.2378L93.5 146.75C93.5 147.855 92.6046 148.75 91.5 148.75L90.125 148.75L69.875 148.75L68.5 148.75C67.3954 148.75 66.5 147.855 66.5 146.75L66.5 74.4634Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M66.5 74.4634L71 67.6585L71 61.9878L89.5625 61.9878L89.5625 81.2683L93.5 85.2378M93.5 85.2378L93.5 146.75C93.5 147.855 92.6046 148.75 91.5 148.75L90.125 148.75L69.875 148.75L68.5 148.75C67.3954 148.75 66.5 147.855 66.5 146.75L66.5 42.1402C66.5 9.25 80 9.25 80 9.25C80 9.25 93.5 9.25 93.5 42.1402L93.5 85.2378Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M71 55.375L64.25 55.375L64.25 46.375L71 41.875L75.5 30.625L84.5 30.625L89 41.875L95.75 46.375L95.75 55.375L89 55.375L85.625 58.75L74.375 58.75L71 55.375Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M74.375 58.75L71 55.375L64.25 55.375L64.25 46.375L71 41.875L75.5 30.625M74.375 58.75L85.625 58.75M74.375 58.75L74.375 43C74.6384 38.5926 75.5 30.625 75.5 30.625M85.625 58.75L89 55.375L95.75 55.375L95.75 46.375L89 41.875L84.5 30.625M85.625 58.75L85.625 43C85.3616 38.5926 84.5 30.625 84.5 30.625M84.5 30.625L75.5 30.625" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M85.625 49.625L85.625 55.25L83.375 56.375L76.625 56.375L74.375 55.25L74.375 49.625L76.625 53L83.375 53L85.625 49.625Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M83.375 53L85.625 49.625L85.625 55.25L83.375 56.375M83.375 53L76.625 53M83.375 53L83.375 56.375M76.625 53L74.375 49.625L74.375 55.25L76.625 56.375M76.625 53L76.625 56.375M76.625 56.375L83.375 56.375" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,Va=e=>k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M21.3861 87.1181H140.367C144.298 87.1181 147.485 83.9312 147.485 80C147.485 77.3161 145.721 75.4558 143.354 74.1896C142.097 73.5171 141.313 72.47 142.293 70.614C143.809 67.7438 147.485 61 147.485 61C139.641 59.2601 125.9 58.5457 110.345 58.2682V55.5604L112.57 51.1099H114.425L106.142 49.2692C102.773 48.5206 99.3318 48.1429 95.8807 48.1429L94.7268 46H102.001L104.834 43H93.0345L90.6883 38.5H88.4631L90.2323 43H74.5007V26H64.0007V71.5412H8.48505C8.48505 71.5412 7.50138 78 12.485 80L21.3861 83.0385V87.1181ZM75.8339 58.1236L74.5007 60.5354V48.1429V46H90.7708L91.4301 48.1429H89.6883L86.6883 49.9973H77.0922L75.6087 51.1099H77.0922L78.5757 55.5604V58.1199C77.6695 58.1223 76.7557 58.1236 75.8339 58.1236Z" fill="${e}"/>
<path d="M12.485 80C65.2058 80 147.485 80 147.485 80M12.485 80C15.9611 81.1866 21.3861 83.0385 21.3861 83.0385M12.485 80C7.50138 78 8.48505 71.5412 8.48505 71.5412H64.0007M12.485 80L21.3861 83.0385M147.485 80V80C147.485 83.9312 144.298 87.1181 140.367 87.1181V87.1181M147.485 80V80C147.485 77.3161 145.721 75.4557 143.354 74.1896V74.1896M147.485 80C147.485 77.3161 145.721 75.4558 143.354 74.1896M147.485 80C147.485 83.9312 144.298 87.1181 140.367 87.1181M21.3861 83.0385V87.1181H140.367M147.485 61C147.485 61 143.809 67.7438 142.293 70.614C141.313 72.47 142.097 73.5171 143.354 74.1896M147.485 61C134.501 58.1199 105.36 58.0499 78.5757 58.1199M147.485 61C139.641 59.2601 125.9 58.5457 110.345 58.2682V55.5604M78.5757 55.5604H110.345M78.5757 55.5604L77.0922 51.1099M78.5757 55.5604V58.1199M110.345 55.5604L112.57 51.1099M112.57 51.1099H77.0922M112.57 51.1099H114.425M77.0922 51.1099H75.6087M75.6087 51.1099H114.425M75.6087 51.1099L77.0922 49.9973H86.6883L89.6883 48.1429H91.4301M114.425 51.1099L106.142 49.2692M95.8807 48.1429V48.1429C99.3318 48.1429 102.773 48.5206 106.142 49.2692V49.2692M95.8807 48.1429H91.4301M95.8807 48.1429L94.7268 46M95.8807 48.1429C99.3318 48.1429 102.773 48.5206 106.142 49.2692M91.4301 48.1429L90.7708 46M64.0007 71.5412V26H74.5007V43M64.0007 71.5412H68.4164L74.5007 60.5354M74.5007 46V48.1429V60.5354M74.5007 46V43M74.5007 46H90.7708M74.5007 43H90.2323M93.0345 43H104.834L102.001 46H94.7268M93.0345 43L90.6883 38.5H88.4631L90.2323 43M93.0345 43H90.2323M90.7708 46H94.7268M74.5007 60.842V60.5354M78.5757 58.1199C77.6695 58.1223 76.7557 58.1236 75.8339 58.1236L74.5007 60.5354" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,Ha=Va(`var(--instrument-frame-primary-color)`),Ua=Va(`var(--container-background-color)`),Wa=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M66.5 81L66.5 42.1402C66.5 9.25 80 9.25 80 9.25C80 9.25 93.5 9.25 93.5 42.1402L93.5 81L93.5 135.25C93.5 142.706 87.4558 148.75 80 148.75C72.5442 148.75 66.5 142.706 66.5 135.25L66.5 81Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M66.5 81L73 81L73 77.9878L87 77.9878L87 81L93.5 81M93.5 81L93.5 135.25C93.5 142.706 87.4558 148.75 80 148.75V148.75C72.5442 148.75 66.5 142.706 66.5 135.25L66.5 42.1402C66.5 9.25 80 9.25 80 9.25C80 9.25 93.5 9.25 93.5 42.1402L93.5 81Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M74.375 80.125L71.5 84L67 84L64 80L64 65L71 59.25L75.5 46L84.5 46L89 59.25L96 65L96 80.125L93 84L88.5 84L85.625 80.125L85.625 76L74.375 76L74.375 80.125Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M84.5 46L89 59.25L96 65L96 80.125L93 84L88.5 84L85.625 80.125L85.625 76M84.5 46L75.5 46M84.5 46C84.5 46 85.3616 55.5926 85.625 60L85.625 76M75.5 46L71 59.25L64 65L64 80L67 84L71.5 84L74.375 80.125L74.375 76M75.5 46C75.5 46 74.6384 55.5926 74.375 60L74.375 76M74.375 76L85.625 76" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M85.625 65L85.625 70.625L83.375 71.75L76.625 71.75L74.375 70.625L74.375 65L76.625 68.375L83.375 68.375L85.625 65Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M83.375 68.375L85.625 65L85.625 70.625L83.375 71.75M83.375 68.375L76.625 68.375M83.375 68.375L83.375 71.75M76.625 68.375L74.375 65L74.375 70.625L76.625 71.75M76.625 68.375L76.625 71.75M76.625 71.75L83.375 71.75" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="82.4185" y="91.8209" width="5" height="31" transform="rotate(-150 82.4185 91.8209)" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="79.9992" cy="91.0031" r="5.5" transform="rotate(-150 79.9992 91.0031)" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,Ga=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect x="60" y="52" width="40" height="3" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M80.0036 77.9545V87C80.0036 87 83.7476 81.9921 82.7622 80C82.1928 78.8489 80.0036 77.9545 80.0036 77.9545Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80.0036 87V77.9545C80.0036 77.9545 77.8718 78.8255 77.2684 79.9545C77.2603 79.9697 77.2525 79.9848 77.245 80C76.2596 81.9921 80.0036 87 80.0036 87Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80.0036 87H90.7728C92.982 87 94.7728 85.2091 94.7728 83V80H82.7622C83.7476 81.9921 80.0036 87 80.0036 87Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M65.2344 79.9545V83C65.2344 85.2091 67.0252 87 69.2344 87H80.0036C80.0036 87 76.2596 81.9921 77.245 80C77.2525 79.9848 77.2603 79.9697 77.2684 79.9545H65.2344Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M69 64H65.2344V74V79.9545H77.2684C77.8718 78.8255 80.0036 77.9545 80.0036 77.9545L80.0036 64H69Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M94.7728 64H91H80.0036L80.0036 77.9545C80.0036 77.9545 82.1928 78.8489 82.7622 80H94.7728V79.9545V74V64Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M91 64V52H69V64H80.0036H91Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M91 52L94 49H66L69 52H91Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M66 49H94H94.7728L93 47.2273H83.0301H81.184H78.8232H76.9771H67.133L65.2344 49H66Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M83.0301 39H77.0036L76.9771 47.2273H78.8232L78.7728 40.4205H81.2344L81.184 47.2273H83.0301V39Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M91 64H94.7728V74V79.9545V80M91 64V52M91 64H80.0036M91 52L94 49M91 52H69M94 49H66M94 49H94.7728L93 47.2273H83.0301M66 49L69 52M66 49H65.2344L67.133 47.2273H76.9771M69 52V64M69 64H65.2344V74V79.9545M69 64H80.0036M76.9771 47.2273H83.0301M76.9771 47.2273L77.0036 39H83.0301V47.2273M76.9771 47.2273H78.8232M83.0301 47.2273H81.184M65.2344 79.9545V83C65.2344 85.2091 67.0252 87 69.2344 87H80.0036M65.2344 79.9545H77.2684M78.8232 47.2273L78.7728 40.4205H81.2344L81.184 47.2273M78.8232 47.2273H81.184M80.0036 64L80.0036 77.9545M80.0036 87H90.7728C92.982 87 94.7728 85.2091 94.7728 83V80M80.0036 87V77.9545M80.0036 87C80.0036 87 83.7476 81.9921 82.7622 80M80.0036 87C80.0036 87 76.2596 81.9921 77.245 80C77.2525 79.9848 77.2603 79.9697 77.2684 79.9545M80.0036 77.9545C80.0036 77.9545 82.1928 78.8489 82.7622 80M80.0036 77.9545C80.0036 77.9545 77.8718 78.8255 77.2684 79.9545M82.7622 80H94.7728" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M80.0036 77.9545V87C80.0036 87 83.7476 81.9921 82.7622 80C82.1928 78.8489 80.0036 77.9545 80.0036 77.9545Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80.0036 87V77.9545C80.0036 77.9545 77.8718 78.8255 77.2684 79.9545C77.2603 79.9697 77.2525 79.9848 77.245 80C76.2596 81.9921 80.0036 87 80.0036 87Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80.0036 87H90.7728C92.982 87 94.7728 85.2091 94.7728 83V80H82.7622C83.7476 81.9921 80.0036 87 80.0036 87Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M65.2344 79.9545V83C65.2344 85.2091 67.0252 87 69.2344 87H80.0036C80.0036 87 76.2596 81.9921 77.245 80C77.2525 79.9848 77.2603 79.9697 77.2684 79.9545H65.2344Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M94.7728 64H92.3113H80.0036L80.0036 77.9545C80.0036 77.9545 82.1928 78.8489 82.7622 80H94.7728V79.9545V74V64Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M65.2344 79.9545V83C65.2344 85.2091 67.0252 87 69.2344 87H80.0036M65.2344 79.9545V74V64H67.6959H80.0036M65.2344 79.9545H77.2684M80.0036 64H92.3113H94.7728V74V79.9545V80M80.0036 64L80.0036 77.9545M80.0036 87H90.7728C92.982 87 94.7728 85.2091 94.7728 83V80M80.0036 87V77.9545M80.0036 87C80.0036 87 83.7476 81.9921 82.7622 80M80.0036 87C80.0036 87 76.2596 81.9921 77.245 80C77.2525 79.9848 77.2603 79.9697 77.2684 79.9545M80.0036 77.9545C80.0036 77.9545 82.1928 78.8489 82.7622 80M80.0036 77.9545C80.0036 77.9545 77.8718 78.8255 77.2684 79.9545M82.7622 80H94.7728" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M92.09 64H67.8359C70.2566 59.8154 74.781 57 79.963 57C85.145 57 89.6694 59.8154 92.09 64Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M67.8359 64L67.4031 63.7496L66.9691 64.5H67.8359V64ZM92.09 64V64.5H92.9569L92.5228 63.7496L92.09 64ZM67.8359 64.5H92.09V63.5H67.8359V64.5ZM68.2687 64.2504C70.6037 60.2139 74.9667 57.5 79.963 57.5V56.5C74.5953 56.5 69.9095 59.4169 67.4031 63.7496L68.2687 64.2504ZM79.963 57.5C84.9593 57.5 89.3223 60.2139 91.6572 64.2504L92.5228 63.7496C90.0165 59.4169 85.3307 56.5 79.963 56.5V57.5Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="87.498" cy="70.0003" rx="1.5" ry="2" transform="rotate(45 87.498 70.0003)" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="72.4983" cy="70" rx="1.5" ry="2" transform="rotate(-45 72.4983 70)" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M96 55L91 60" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M64 55L69 60" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,Ka=e=>k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M53.0312 72H80.9609C80.4482 64.7347 74.3918 59 66.9961 59C59.6003 59 53.544 64.7347 53.0312 72ZM139.961 72C139.448 64.7347 133.392 59 125.996 59C118.6 59 112.544 64.7347 112.031 72H139.961ZM110.961 72C110.448 64.7347 104.392 59 96.9961 59C89.6003 59 83.544 64.7347 83.0312 72H110.961Z" fill="${e}"/>
<path d="M53.0312 72L52.5325 71.9648L52.4947 72.5H53.0312V72ZM80.9609 72V72.5H81.4975L81.4597 71.9648L80.9609 72ZM139.961 72V72.5H140.497L140.46 71.9648L139.961 72ZM112.031 72L111.532 71.9648L111.495 72.5H112.031V72ZM110.961 72V72.5H111.497L111.46 71.9648L110.961 72ZM83.0312 72L82.5325 71.9648L82.4947 72.5H83.0312V72ZM53.0312 72.5H80.9609V71.5H53.0312V72.5ZM81.4597 71.9648C80.9286 64.4396 74.6562 58.5 66.9961 58.5V59.5C74.1275 59.5 79.9678 65.0299 80.4622 72.0352L81.4597 71.9648ZM66.9961 58.5C59.336 58.5 53.0636 64.4396 52.5325 71.9648L53.53 72.0352C54.0244 65.0299 59.8647 59.5 66.9961 59.5V58.5ZM140.46 71.9648C139.929 64.4396 133.656 58.5 125.996 58.5V59.5C133.127 59.5 138.968 65.0299 139.462 72.0352L140.46 71.9648ZM125.996 58.5C118.336 58.5 112.064 64.4396 111.532 71.9648L112.53 72.0352C113.024 65.0299 118.865 59.5 125.996 59.5V58.5ZM112.031 72.5H139.961V71.5H112.031V72.5ZM111.46 71.9648C110.929 64.4396 104.656 58.5 96.9961 58.5V59.5C104.127 59.5 109.968 65.0299 110.462 72.0352L111.46 71.9648ZM96.9961 58.5C89.336 58.5 83.0636 64.4396 82.5325 71.9648L83.53 72.0352C84.0244 65.0299 89.8647 59.5 96.9961 59.5V58.5ZM83.0312 72.5H110.961V71.5H83.0312V72.5Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M140.366 87.1181H21.3855V83.0385L12.4844 80V71H18.4844V63L22 44H26V63H32.4844V53.5604V50.1099L31 48.9973L32 48.1429H37.4294L37.2747 38.5H39.5L41.88 48.1429H45.8152C48.7962 48.1429 51.7388 48.8152 54.4239 50.1099H52.5695L50.3443 53.5604V71H117.416L124.833 64.1236H148C148 64.1236 148 68.5 145.5 71C143.605 72.8947 143.5 75.6209 143.5 75.6209C145.701 75.6209 147.484 77.4047 147.484 79.6053V80C147.484 83.9312 144.297 87.1181 140.366 87.1181Z" fill="${e}"/>
<path d="M12.4844 80H147.484M12.4844 80L21.3855 83.0385V87.1181H140.366C144.297 87.1181 147.484 83.9312 147.484 80V80M12.4844 80V71H18.4844M147.484 80V79.6053C147.484 77.4047 145.701 75.6209 143.5 75.6209V75.6209C143.5 75.6209 143.605 72.8947 145.5 71C148 68.5 148 64.1236 148 64.1236H124.833L117.416 71H50.3443M18.4844 71H50.3443M18.4844 71V63L22 44H26V63H32.4844V53.5604M32.4844 53.5604H50.3443M32.4844 53.5604V50.1099M50.3443 53.5604L52.5695 50.1099H32.4844M50.3443 53.5604V71M32.4844 50.1099H54.4239V50.1099C51.7388 48.8152 48.7962 48.1429 45.8152 48.1429H41.88M32.4844 50.1099L31 48.9973L32 48.1429H37.4294M41.88 48.1429L39.5 38.5H37.2747L37.4294 48.1429M41.88 48.1429H37.4294" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="136" cy="70" r="2" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,qa=Ka(`var(--instrument-frame-primary-color)`),Ja=Ka(`var(--container-background-color)`),Ya=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M66.5 146.75L66.5 32.1402C66.5 11.5 80 9.25 80 9.25C80 9.25 93.5 11.5 93.5 32.1402L93.5 146.75C93.5 147.855 92.6046 148.75 91.5 148.75L90.125 148.75L69.875 148.75L68.5 148.75C67.3954 148.75 66.5 147.855 66.5 146.75Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M74 122L64 122L64 118L72 118L75 114L85 114L88 118L96 118L96 122L86 122L86 138.75L74 138.75L74 122Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="80" cy="44" r="11.5" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="80" cy="70" r="11.5" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="80" cy="96" r="11.5" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,Xa=e=>k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M140.366 87.1182H21.3855V83.0386L12.4844 80.0001C12.4844 77.5441 14.487 75.5592 16.943 75.5812L21.3855 75.621L84.5943 75.5413L96.8333 64.1237H100.012V49.5H101H103H105.575L106.76 54.5605H115.281C122.13 54.5605 128.463 58.203 131.907 64.1237H138C141.233 66.387 144.251 70.5308 145.98 73.1767C147.01 74.7539 147.484 76.6105 147.484 78.4946V80.0001C147.484 83.9313 144.297 87.1182 140.366 87.1182Z" fill="${e}"/>
<path d="M12.4844 80.0001H147.484M12.4844 80.0001L21.3855 83.0386V87.1182H140.366C144.297 87.1182 147.484 83.9313 147.484 80.0001V80.0001M12.4844 80.0001V80.0001C12.4844 77.5441 14.487 75.5592 16.943 75.5812L21.3855 75.621L84.5943 75.5413L96.8333 64.1237H100.012M147.484 80.0001V78.4946C147.484 76.6105 147.01 74.7539 145.98 73.1767C144.251 70.5308 141.233 66.387 138 64.1237H131.907M106.76 54.5605H115.281C122.13 54.5605 128.463 58.203 131.907 64.1237V64.1237M131.907 64.1237H109M100.012 64.1237V49.5H101M100.012 64.1237H109M109 64.1237L105.575 49.5H103M101 49.5V45M101 49.5H103M103 49.5V47" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,Za=Xa(`var(--instrument-frame-primary-color)`),Qa=Xa(`var(--container-background-color)`),$a=e=>k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M147.484 80.0001L146.814 81.5981C145.412 84.9422 142.14 87.1182 138.514 87.1182H21.3855V83.0386L12.4844 80.0001C12.4844 77.5376 14.4806 75.5413 16.9432 75.5413H21L30.5 56.5H32H34.5H36.5L33.5 75.5413H36.5943L48.8333 64.1237H100.012H127.5L145.461 66.8188C147.93 67.1894 149.587 69.5517 149.094 72L147.484 80.0001Z" fill="${e}"/>
<path d="M12.4844 80.0001L21.3855 83.0386V87.1182H138.514C142.14 87.1182 145.412 84.9422 146.814 81.5981L147.484 80.0001L149.094 72M12.4844 80.0001V80.0001C12.4844 77.5376 14.4806 75.5413 16.9432 75.5413H21M12.4844 80.0001H107.04C116.302 80.0001 125.519 78.7134 134.427 76.1768L149.094 72M21 75.5413L30.5 56.5H32M21 75.5413H33.5M33.5 75.5413H36.5943L48.8333 64.1237H100.012H127.5L145.461 66.8188C147.93 67.1894 149.587 69.5517 149.094 72V72M33.5 75.5413L36.5 56.5H34.5M34.5 56.5V48.5M34.5 56.5H32M32 56.5V53" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,eo=$a(`var(--instrument-frame-primary-color)`),to=$a(`var(--container-background-color)`),no=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M121.033 100.2L101 80H96L118.289 99.8667C118.741 100.27 119 100.846 119 101.452V102.835C119 103.478 119.522 104 120.165 104C120.809 104 121.33 103.478 121.33 102.835V100.922C121.33 100.652 121.223 100.392 121.033 100.2Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M39.2975 100.2L59.3301 80H64.3301L42.0407 99.8667C41.5887 100.27 41.3301 100.846 41.3301 101.452V102.835C41.3301 103.478 40.8085 104 40.1651 104C39.5216 104 39 103.478 39 102.835V100.922C39 100.652 39.1069 100.392 39.2975 100.2Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M121.033 100.2L101 80H96L118.289 99.8667C118.741 100.27 119 100.846 119 101.452V102.835C119 103.478 119.522 104 120.165 104C120.809 104 121.33 103.478 121.33 102.835V100.922C121.33 100.652 121.223 100.392 121.033 100.2Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M39.2975 100.2L59.3301 80H64.3301L42.0407 99.8667C41.5887 100.27 41.3301 100.846 41.3301 101.452V102.835C41.3301 103.478 40.8085 104 40.1651 104C39.5216 104 39 103.478 39 102.835V100.922C39 100.652 39.1069 100.392 39.2975 100.2Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M118 64H126V77.8755C126 79.2677 125.637 80.6358 124.946 81.8446L123.736 83.9611C122.969 85.3048 121.031 85.3048 120.264 83.9611L119.054 81.8446C118.363 80.6358 118 79.2677 118 77.8755V64Z" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M34 64H42V77.8755C42 79.2677 41.6367 80.6358 40.9459 81.8446L39.7365 83.9611C38.9687 85.3048 37.0313 85.3048 36.2635 83.9611L35.0541 81.8446C34.3633 80.6358 34 79.2677 34 77.8755V64Z" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M134 75.1317V73H120L98 70V73L90 79.9999L132.136 77.127C133.185 77.0555 134 76.1834 134 75.1317Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M98 73L90 79.9999L132.136 77.127C133.185 77.0555 134 76.1834 134 75.1317V73H120M98 73H120M98 73V70L120 73" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M26 75.1346V73H40L62 70V73L69 79.9999L27.8608 77.1298C26.8128 77.0567 26 76.1852 26 75.1346Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M62 73L69 79.9999L27.8608 77.1298C26.8128 77.0567 26 76.1852 26 75.1346V73H40M62 73H40M62 73V70L40 73" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M93.039 84.5757L97.8383 73.3773C97.945 73.1284 98 72.8603 98 72.5895V68.9075C98 68.3308 97.751 67.7822 97.317 67.4024L90.5655 61.4948C90.201 61.1758 89.733 61 89.2485 61H70.7585C70.2698 61 69.798 61.1789 69.4322 61.503L62.6737 67.491C62.2453 67.8706 62 68.4156 62 68.988V73L66.961 84.5757C67.5913 86.0464 69.0375 87 70.6376 87H89.3624C90.9625 87 92.4087 86.0464 93.039 84.5757Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="12.5" y="57.5" width="51" height="7" rx="1.5" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="96.5" y="57.5" width="51" height="7" rx="1.5" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M70 61L72.7396 65.1094C73.1105 65.6658 73.735 66 74.4037 66H85.5963C86.265 66 86.8895 65.6658 87.2604 65.1094L90 61" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M62 68H98" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="80" cy="79" rx="6" ry="6" transform="rotate(90 80 79)" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="80" cy="79" rx="4" ry="4" transform="rotate(90 80 79)" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="81" cy="78" rx="2" ry="2" transform="rotate(90 81 78)" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,ro=e=>k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M131 75C133.209 75 135 76.7909 135 79C135 81.2091 133.209 83 131 83V75Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M132 84V74C132 73.4477 131.552 73 131 73H89L98.7002 84.6402C98.8901 84.8682 99.1716 85 99.4684 85H131C131.552 85 132 84.5523 132 84Z" fill="${e}" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M129.736 73.4611L122.576 85.9923C122.22 86.6154 121.557 87 120.839 87H69.8301C69.2805 87 68.7346 86.9094 68.2144 86.7317L28 73V68.0879L29.1795 65.9233C30.0014 64.415 31.5399 63.4342 33.2542 63.3257L70 61H90L124.906 65.3632C125.627 65.4533 126.319 65.6995 126.935 66.0846L129.925 67.9534C129.972 67.9824 130 68.0332 130 68.0879V72.4689C130 72.8169 129.909 73.159 129.736 73.4611Z" fill="${e}"/>
<path d="M28 68.0879V73L68.2144 86.7317C68.7346 86.9094 69.2805 87 69.8301 87H120.839C121.557 87 122.22 86.6154 122.576 85.9923L129.736 73.4611C129.909 73.159 130 72.8169 130 72.4689V68.0879M28 68.0879L29.1795 65.9233C30.0014 64.415 31.5399 63.4342 33.2542 63.3257L70 61H90L124.906 65.3632C125.627 65.4533 126.319 65.6995 126.935 66.0846L129.925 67.9534C129.972 67.9824 130 68.0332 130 68.0879M28 68.0879H130" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M128.918 100.202L101 80H96L126.097 99.9027C126.661 100.276 127 100.907 127 101.583V102.835C127 103.478 127.522 104 128.165 104C128.809 104 129.33 103.478 129.33 102.835V101.009C129.33 100.689 129.177 100.389 128.918 100.202Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M31.4125 100.202L59.3301 80H64.3301L34.2334 99.9027C33.6694 100.276 33.3301 100.907 33.3301 101.583V102.835C33.3301 103.478 32.8085 104 32.1651 104C31.5216 104 31 103.478 31 102.835V101.009C31 100.689 31.1534 100.389 31.4125 100.202Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M128.918 100.202L101 80H96L126.097 99.9027C126.661 100.276 127 100.907 127 101.583V102.835C127 103.478 127.522 104 128.165 104C128.809 104 129.33 103.478 129.33 102.835V101.009C129.33 100.689 129.177 100.389 128.918 100.202Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M31.4125 100.202L59.3301 80H64.3301L34.2334 99.9027C33.6694 100.276 33.3301 100.907 33.3301 101.583V102.835C33.3301 103.478 32.8085 104 32.1651 104C31.5216 104 31 103.478 31 102.835V101.009C31 100.689 31.1534 100.389 31.4125 100.202Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M118 64H126V73.8755C126 75.2677 125.637 76.6358 124.946 77.8446L123.736 79.9611C122.969 81.3048 121.031 81.3048 120.264 79.9611L119.054 77.8446C118.363 76.6358 118 75.2677 118 73.8755V64Z" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M34 64H42V73.8755C42 75.2677 41.6367 76.6358 40.9459 77.8446L39.7365 79.9611C38.9687 81.3048 37.0313 81.3048 36.2635 79.9611L35.0541 77.8446C34.3633 76.6358 34 75.2677 34 73.8755V64Z" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M127 75.1731V73.9996C127 73.4473 126.552 72.9996 126 72.9996H120L98 70V72.9996L94 79.9996L125.181 77.1649C126.211 77.0713 127 76.2076 127 75.1731Z" fill="${e}"/>
<path d="M98 72.9996L94 79.9996L125.181 77.1649C126.211 77.0713 127 76.2076 127 75.1731V73.9996C127 73.4473 126.552 72.9996 126 72.9996H120M98 72.9996H120M98 72.9996V70L120 72.9996" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M32 75.1735V74C32 73.4477 32.4477 73 33 73H40L62 70V73L65 79.9999L33.8189 77.1653C32.7888 77.0717 32 76.2079 32 75.1735Z" fill="${e}"/>
<path d="M62 73L65 79.9999M62 73H40M62 73V70M62 73H98M65 79.9999L33.8189 77.1653C32.7888 77.0717 32 76.2079 32 75.1735V74C32 73.4477 32.4477 73 33 73H40M65 79.9999H94M40 73L62 70M62 70H98" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="12.5" y="57.5" width="51" height="7" rx="1.5" fill="${e}" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="96.5" y="57.5" width="51" height="7" rx="1.5" fill="${e}" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,io=ro(`var(--instrument-frame-primary-color)`),ao=ro(`var(--container-background-color)`),oo=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="80" cy="25" rx="4" ry="4" transform="rotate(90 80 25)" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M87.5 26L87.5 50C87.5 50.8284 86.8284 51.5 86 51.5L74 51.5C73.1716 51.5 72.5 50.8284 72.5 50L72.5 26C72.5 25.1716 73.1716 24.5 74 24.5L86 24.5C86.8284 24.5 87.5 25.1716 87.5 26Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<g clip-path="url(#clip0_25406_62468)">
<path d="M74.124 68.9067L34.8998 38.5288C34.1757 37.968 33.974 36.9602 34.4265 36.164C34.8921 35.3447 35.9013 35.0093 36.7647 35.387L81.9764 55.1651C82.5202 55.403 82.7383 56.0593 82.4451 56.5754L75.6058 68.6102C75.305 69.1394 74.6053 69.2794 74.124 68.9067Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M74.124 91.0923L34.8998 121.47C34.1757 122.031 33.974 123.039 34.4265 123.835C34.8921 124.654 35.9013 124.99 36.7647 124.612L81.9764 104.834C82.5202 104.596 82.7383 103.94 82.4451 103.424L75.6058 91.3888C75.305 90.8597 74.6053 90.7196 74.124 91.0923Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M85.8757 68.9067L125.1 38.5288C125.824 37.968 126.026 36.9602 125.573 36.164C125.108 35.3447 124.098 35.0093 123.235 35.387L78.0233 55.1651C77.4795 55.403 77.2614 56.0593 77.5546 56.5754L84.394 68.6102C84.6947 69.1394 85.3945 69.2794 85.8757 68.9067Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M85.8757 91.0923L125.1 121.47C125.824 122.031 126.026 123.039 125.573 123.835C125.108 124.654 124.098 124.99 123.235 124.612L78.0233 104.834C77.4795 104.596 77.2614 103.94 77.5546 103.424L84.394 91.3889C84.6947 90.8597 85.3945 90.7196 85.8757 91.0923Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M74.124 68.9067L34.8998 38.5288C34.1757 37.968 33.974 36.9602 34.4265 36.164C34.8921 35.3447 35.9013 35.0093 36.7647 35.387L81.9764 55.1651C82.5202 55.403 82.7383 56.0593 82.4451 56.5754L75.6058 68.6102C75.305 69.1394 74.6053 69.2794 74.124 68.9067Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M74.124 91.0923L34.8998 121.47C34.1757 122.031 33.974 123.039 34.4265 123.835C34.8921 124.654 35.9013 124.99 36.7647 124.612L81.9764 104.834C82.5202 104.596 82.7383 103.94 82.4451 103.424L75.6058 91.3888C75.305 90.8597 74.6053 90.7196 74.124 91.0923Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M85.8757 68.9067L125.1 38.5288C125.824 37.968 126.026 36.9602 125.573 36.164C125.108 35.3447 124.098 35.0093 123.235 35.387L78.0233 55.1651C77.4795 55.403 77.2614 56.0593 77.5546 56.5754L84.394 68.6102C84.6947 69.1394 85.3945 69.2794 85.8757 68.9067Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M85.8757 91.0923L125.1 121.47C125.824 122.031 126.026 123.039 125.573 123.835C125.108 124.654 124.098 124.99 123.235 124.612L78.0233 104.834C77.4795 104.596 77.2614 103.94 77.5546 103.424L84.394 91.3889C84.6947 90.8597 85.3945 90.7196 85.8757 91.0923Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M71.3558 28C69.4149 28 67.7537 29.3933 67.4163 31.3047L62.3011 60.292C62.1088 61.3815 62.3765 62.5026 63.0404 63.3877L67.1995 68.9336C67.7188 69.6259 68.0003 70.4676 68.0003 71.333V88.667C68.0003 89.5324 67.7188 90.3741 67.1995 91.0664L63.0404 96.6123C62.3765 97.4974 62.1088 98.6185 62.3011 99.708L67.4163 128.695C67.7537 130.607 69.4149 132 71.3558 132H88.6439C90.5848 132 92.246 130.607 92.5833 128.695L97.6986 99.708C97.8908 98.6185 97.6231 97.4974 96.9593 96.6123L92.8001 91.0664C92.2809 90.3741 92.0004 89.5323 92.0003 88.667V71.333C92.0004 70.4677 92.2809 69.6259 92.8001 68.9336L96.9593 63.3877C97.6231 62.5026 97.8908 61.3815 97.6986 60.292L92.5833 31.3047C92.246 29.3933 90.5848 28 88.6439 28H71.3558Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M90 69.72L85.6046 34.7506C85.4789 33.7503 84.6284 33 83.6203 33H75.4038C74.3746 33 73.5134 33.7811 73.4132 34.8054L70 69.72V127C70 128.105 70.8954 129 72 129H88C89.1046 129 90 128.105 90 127V69.72Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M19.9688 103.969C10.0104 113.927 10.0104 130.073 19.9688 140.031C29.9271 149.99 46.0729 149.99 56.0312 140.031C65.9896 130.073 65.9896 113.927 56.0312 103.969C46.0729 94.0104 29.9271 94.0104 19.9688 103.969ZM20.6759 104.676C30.2437 95.108 45.7563 95.108 55.3241 104.676C64.892 114.244 64.892 129.756 55.3241 139.324C45.7563 148.892 30.2437 148.892 20.6759 139.324C11.108 129.756 11.108 114.244 20.6759 104.676ZM21.5501 105.112C20.9439 105.42 20.8152 106.231 21.296 106.712L33.8271 119.243C33.4283 119.845 33.1745 120.516 33.0641 121.204L32.5379 121.24C31.9638 121.279 31.4336 121.563 31.0836 122.019L20.8333 135.403C20.3658 136.014 20.2899 136.839 20.6379 137.525L21.1109 138.457C21.419 139.062 22.2289 139.191 22.7095 138.71L35.2455 126.174C35.8448 126.571 36.511 126.823 37.1955 126.934L37.2307 127.461C37.2693 128.035 37.5541 128.565 38.011 128.915L51.3936 139.165C52.0042 139.633 52.8299 139.709 53.5156 139.361L54.4471 138.888C55.0531 138.58 55.1821 137.77 54.7019 137.289L42.1701 124.757C42.5663 124.159 42.8208 123.494 42.9325 122.81L43.4587 122.775C44.033 122.737 44.5636 122.453 44.9136 121.996L55.1632 108.613C55.6308 108.002 55.7071 107.177 55.3593 106.491L54.8863 105.56C54.5784 104.954 53.7685 104.824 53.2877 105.305L40.7614 117.831C40.1593 117.431 39.4894 117.175 38.801 117.064L38.7658 116.54C38.7274 115.966 38.4435 115.436 37.9869 115.086L24.603 104.835C23.9924 104.368 23.1681 104.292 22.4823 104.64L21.5501 105.112Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="38" cy="122" r="2.5" transform="rotate(-135 38 122)" vector-effect="non-scaling-stroke" stroke="var(--instrument-frame-primary-color)"/>
<path d="M38 12.5C23.9167 12.5 12.5 23.9167 12.5 38C12.5 52.0833 23.9167 63.5 38 63.5C52.0833 63.5 63.5 52.0833 63.5 38C63.5 23.9167 52.0833 12.5 38 12.5ZM38 13.5C51.531 13.5 62.5 24.469 62.5 38C62.5 51.531 51.531 62.5 38 62.5C24.469 62.5 13.5 51.531 13.5 38C13.5 24.469 24.469 13.5 38 13.5ZM38.3096 14.4258C37.6634 14.2154 37 14.6973 37 15.377V33.1006C36.2943 33.244 35.6428 33.5359 35.0791 33.9424L34.6826 33.5967C34.2495 33.2177 33.6731 33.0437 33.1025 33.1191L16.3916 35.335C15.6291 35.436 14.9918 35.9652 14.7529 36.6963L14.4287 37.6895C14.2177 38.3358 14.6991 38.9998 15.3789 39H33.1006C33.2438 39.7055 33.5362 40.3564 33.9424 40.9199L33.5957 41.3164C33.2169 41.7497 33.0425 42.3259 33.1182 42.8965L35.334 59.6074C35.4351 60.3698 35.9653 61.0072 36.6963 61.2461L37.6895 61.5703C38.3356 61.7807 39 61.2988 39 60.6191V42.8984C39.7062 42.7546 40.3589 42.4628 40.9229 42.0557L41.3193 42.4033C41.7525 42.7821 42.328 42.9564 42.8984 42.8809L59.6104 40.665C60.3724 40.5636 61.0093 40.0345 61.248 39.3037L61.5732 38.3105C61.7841 37.6644 61.3016 37.0004 60.6221 37H42.8994C42.756 36.2934 42.4638 35.6403 42.0566 35.0762L42.4033 34.6797C42.7822 34.2464 42.9565 33.6702 42.8809 33.0996L40.665 16.3887C40.5639 15.6263 40.0337 14.9889 39.3027 14.75L38.3096 14.4258Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="38" cy="38" r="2.5" transform="rotate(-90 38 38)" vector-effect="non-scaling-stroke" stroke="var(--instrument-frame-primary-color)"/>
<path d="M144.084 109.248C137.042 97.0519 121.447 92.8731 109.25 99.9147C97.0539 106.956 92.8751 122.552 99.9167 134.748C106.958 146.945 122.554 151.124 134.75 144.082C146.947 137.04 151.126 121.445 144.084 109.248ZM143.218 109.748C149.983 121.467 145.969 136.451 134.25 143.216C122.532 149.981 107.548 145.967 100.783 134.248C94.0172 122.53 98.0322 107.546 109.75 100.781C121.469 94.0153 136.452 98.0302 143.218 109.748ZM142.571 110.481C142.43 109.815 141.681 109.481 141.092 109.821L125.745 118.682C125.268 118.142 124.687 117.725 124.053 117.44L124.155 116.923C124.266 116.358 124.129 115.772 123.778 115.316L113.503 101.951C113.034 101.341 112.258 101.055 111.505 101.213L110.483 101.429C109.818 101.57 109.484 102.318 109.823 102.907L118.684 118.255C118.145 118.731 117.727 119.31 117.442 119.943L116.926 119.842C116.361 119.73 115.776 119.867 115.319 120.217L101.954 130.492C101.345 130.961 101.058 131.738 101.217 132.49L101.432 133.513C101.572 134.178 102.322 134.512 102.911 134.172L118.256 125.312C118.734 125.853 119.314 126.272 119.949 126.557L119.846 127.073C119.734 127.638 119.871 128.224 120.222 128.68L130.497 142.045C130.966 142.655 131.743 142.941 132.496 142.782L133.518 142.567C134.183 142.426 134.517 141.677 134.177 141.089L125.316 125.741C125.855 125.263 126.275 124.684 126.56 124.05L127.077 124.152C127.641 124.264 128.228 124.126 128.684 123.776L142.049 113.501C142.658 113.032 142.945 112.255 142.786 111.503L142.571 110.481Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="122" cy="121.998" r="2.5" transform="rotate(-30 122 121.998)" vector-effect="non-scaling-stroke" stroke="var(--instrument-frame-primary-color)"/>
<path d="M128.6 13.3669C114.996 9.72189 101.014 17.7947 97.3689 31.3981C93.7241 45.0014 101.797 58.9842 115.4 62.6291C129.003 66.274 142.986 58.201 146.631 44.5979C150.276 30.9946 142.203 17.012 128.6 13.3669ZM128.341 14.3328C141.411 17.835 149.167 31.2692 145.665 44.3391C142.163 57.4087 128.729 65.1651 115.659 61.6632C102.589 58.1612 94.833 44.7267 98.3348 31.657C101.837 18.587 115.271 10.8308 128.341 14.3328ZM128.4 15.3081C127.831 14.9376 127.065 15.2315 126.889 15.888L122.302 33.0058C121.584 32.9617 120.879 33.075 120.229 33.3217L119.935 32.884C119.614 32.406 119.103 32.0885 118.532 32.0138L101.817 29.829C101.055 29.7294 100.302 30.0765 99.8817 30.7208L99.3115 31.5962C98.9407 32.1657 99.234 32.9308 99.8904 33.107L117.008 37.6937C116.964 38.4135 117.078 39.119 117.326 39.7695L116.888 40.0627C116.41 40.3831 116.093 40.8945 116.018 41.4653L113.832 58.1801C113.732 58.9428 114.079 59.6956 114.724 60.1155L115.599 60.6858C116.169 61.0566 116.935 60.7628 117.111 60.1062L121.698 42.9874C122.417 43.0311 123.123 42.9179 123.773 42.6708L124.066 43.1092C124.386 43.5871 124.897 43.9045 125.468 43.9792L142.184 46.1642C142.946 46.2637 143.698 45.9172 144.118 45.2732L144.689 44.398C145.06 43.8284 144.766 43.062 144.109 42.8859L126.992 38.2992C127.036 37.58 126.923 36.874 126.676 36.224L127.112 35.9315C127.59 35.611 127.908 35.0995 127.983 34.5288L130.167 17.8138C130.267 17.0512 129.92 16.2983 129.276 15.8784L128.4 15.3081Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="122" cy="37.9978" r="2.5" transform="rotate(-75 122 37.9978)" vector-effect="non-scaling-stroke" stroke="var(--instrument-frame-primary-color)"/>
</g>
<defs>
<clipPath id="clip0_25406_62468">
<rect width="160" height="160" fill="var(--instrument-frame-primary-color)" transform="matrix(-1 0 0 1 160 0)"/>
</clipPath>
</defs>
</svg>
`,so=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M44 66.5C44 65.6716 44.6716 65 45.5 65C46.3284 65 47 65.6716 47 66.5V73H44V66.5Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M53.4165 67.8786L68.1048 66.6196C68.2285 66.609 68.226 66.4272 68.102 66.4201L52.9506 65.5543C52.3191 65.5182 51.6855 65.5572 51.0632 65.6703L46.5 66.5L50.6284 67.6259C51.5357 67.8734 52.4795 67.9589 53.4165 67.8786Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M37.0835 67.8786L22.3952 66.6196C22.2715 66.609 22.2741 66.4272 22.398 66.4201L37.5494 65.5543C38.1809 65.5182 38.8145 65.5572 39.4368 65.6703L44 66.5L39.8716 67.6259C38.9643 67.8734 38.0205 67.9589 37.0835 67.8786Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M44 66.5V73H47V66.5C47 65.6716 46.3284 65 45.5 65C44.6716 65 44 65.6716 44 66.5ZM44 66.5L39.8716 67.6259C38.9643 67.8734 38.0205 67.9589 37.0835 67.8786L22.3952 66.6196C22.2715 66.609 22.2741 66.4272 22.398 66.4201L37.5494 65.5543C38.1809 65.5182 38.8145 65.5572 39.4368 65.6703L44 66.5ZM68.1048 66.6196L53.4165 67.8786C52.4795 67.9589 51.5357 67.8734 50.6284 67.6259L46.5 66.5L51.0632 65.6703C51.6855 65.5572 52.3191 65.5182 52.9506 65.5543L68.102 66.4201C68.226 66.4272 68.2285 66.609 68.1048 66.6196Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M112 66.5C112 65.6716 112.672 65 113.5 65C114.328 65 115 65.6716 115 66.5V73H112V66.5Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M121.417 67.8786L136.105 66.6196C136.229 66.609 136.226 66.4272 136.102 66.4201L120.951 65.5543C120.319 65.5182 119.686 65.5572 119.063 65.6703L114.5 66.5L118.628 67.6259C119.536 67.8734 120.48 67.9589 121.417 67.8786Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M105.083 67.8786L90.3952 66.6196C90.2715 66.609 90.2741 66.4272 90.398 66.4201L105.549 65.5543C106.181 65.5182 106.814 65.5572 107.437 65.6703L112 66.5L107.872 67.6259C106.964 67.8734 106.02 67.9589 105.083 67.8786Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M112 66.5V73H115V66.5C115 65.6716 114.328 65 113.5 65C112.672 65 112 65.6716 112 66.5ZM112 66.5L107.872 67.6259C106.964 67.8734 106.02 67.9589 105.083 67.8786L90.3952 66.6196C90.2715 66.609 90.2741 66.4272 90.398 66.4201L105.549 65.5543C106.181 65.5182 106.814 65.5572 107.437 65.6703L112 66.5ZM136.105 66.6196L121.417 67.8786C120.48 67.9589 119.536 67.8734 118.628 67.6259L114.5 66.5L119.063 65.6703C119.686 65.5572 120.319 65.5182 120.951 65.5543L136.102 66.4201C136.226 66.4272 136.229 66.609 136.105 66.6196Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M65.1001 86.5311L68.0001 80H71.0001L67.2126 86.3124C66.7464 87.0895 66.5001 87.9787 66.5001 88.8849V95.0849C66.5001 95.5903 66.0904 96 65.585 96C65.0796 96 64.6699 95.5903 64.6699 95.0849V88.5601C64.6699 87.8612 64.8165 87.1699 65.1001 86.5311Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M94.9 86.5311L92.0001 80H89.0001L92.7875 86.3124C93.2538 87.0895 93.5001 87.9787 93.5001 88.8849V95.0849C93.5001 95.5903 93.9098 96 94.4151 96C94.9205 96 95.3302 95.5903 95.3302 95.0849V88.5601C95.3302 87.8612 95.1836 87.1699 94.9 86.5311Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M65.1001 86.5311L68.0001 80H71.0001L67.2126 86.3124C66.7464 87.0895 66.5001 87.9787 66.5001 88.8849V95.0849C66.5001 95.5903 66.0904 96 65.585 96C65.0796 96 64.6699 95.5903 64.6699 95.0849V88.5601C64.6699 87.8612 64.8165 87.1699 65.1001 86.5311Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M94.9 86.5311L92.0001 80H89.0001L92.7875 86.3124C93.2538 87.0895 93.5001 87.9787 93.5001 88.8849V95.0849C93.5001 95.5903 93.9098 96 94.4151 96C94.9205 96 95.3302 95.5903 95.3302 95.0849V88.5601C95.3302 87.8612 95.1836 87.1699 94.9 86.5311Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M92.5649 79.8671L119.363 73.562C119.736 73.4742 120 73.1411 120 72.7575C120 72.3291 119.673 71.9716 119.246 71.9342L90.4698 69.4121H70.604L40.6231 71.9476C40.2708 71.9774 40 72.2721 40 72.6257C40 72.9393 40.2143 73.2123 40.519 73.2867L67.4153 79.8572C67.8037 79.952 68.2021 80 68.6019 80H91.4197C91.8053 80 92.1895 79.9554 92.5649 79.8671Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="80" cy="82" rx="6" ry="6" transform="rotate(90 80 82)" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="80" cy="82" rx="4" ry="4" transform="rotate(90 80 82)" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="81" cy="81" rx="2" ry="2" transform="rotate(90 81 81)" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,co=e=>k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M99 78C101.209 78 103 79.7909 103 82C103 84.2091 101.209 86 99 86V78Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M99 87V78L56 77L65.7024 87.6727C65.892 87.8811 66.1606 88 66.4424 88H98C98.5523 88 99 87.5523 99 87Z" fill="${e}" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M44 66.5C44 65.6716 44.6716 65 45.5 65C46.3284 65 47 65.6716 47 66.5V73H44V66.5Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M53.4165 67.8786L68.1048 66.6196C68.2285 66.609 68.226 66.4272 68.102 66.4201L52.9506 65.5543C52.3191 65.5182 51.6855 65.5572 51.0632 65.6703L46.5 66.5L50.6284 67.6259C51.5357 67.8734 52.4795 67.9589 53.4165 67.8786Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M37.0835 67.8786L22.3952 66.6196C22.2715 66.609 22.2741 66.4272 22.398 66.4201L37.5494 65.5543C38.1809 65.5182 38.8145 65.5572 39.4368 65.6703L44 66.5L39.8716 67.6259C38.9643 67.8734 38.0205 67.9589 37.0835 67.8786Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M44 66.5V73H47V66.5C47 65.6716 46.3284 65 45.5 65C44.6716 65 44 65.6716 44 66.5ZM44 66.5L39.8716 67.6259C38.9643 67.8734 38.0205 67.9589 37.0835 67.8786L22.3952 66.6196C22.2715 66.609 22.2741 66.4272 22.398 66.4201L37.5494 65.5543C38.1809 65.5182 38.8145 65.5572 39.4368 65.6703L44 66.5ZM68.1048 66.6196L53.4165 67.8786C52.4795 67.9589 51.5357 67.8734 50.6284 67.6259L46.5 66.5L51.0632 65.6703C51.6855 65.5572 52.3191 65.5182 52.9506 65.5543L68.102 66.4201C68.226 66.4272 68.2285 66.609 68.1048 66.6196Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M112 66.5C112 65.6716 112.672 65 113.5 65C114.328 65 115 65.6716 115 66.5V73H112V66.5Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M121.417 67.8786L136.105 66.6196C136.229 66.609 136.226 66.4272 136.102 66.4201L120.951 65.5543C120.319 65.5182 119.686 65.5572 119.063 65.6703L114.5 66.5L118.628 67.6259C119.536 67.8734 120.48 67.9589 121.417 67.8786Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M105.083 67.8786L90.3952 66.6196C90.2715 66.609 90.2741 66.4272 90.398 66.4201L105.549 65.5543C106.181 65.5182 106.814 65.5572 107.437 65.6703L112 66.5L107.872 67.6259C106.964 67.8734 106.02 67.9589 105.083 67.8786Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M112 66.5V73H115V66.5C115 65.6716 114.328 65 113.5 65C112.672 65 112 65.6716 112 66.5ZM112 66.5L107.872 67.6259C106.964 67.8734 106.02 67.9589 105.083 67.8786L90.3952 66.6196C90.2715 66.609 90.2741 66.4272 90.398 66.4201L105.549 65.5543C106.181 65.5182 106.814 65.5572 107.437 65.6703L112 66.5ZM136.105 66.6196L121.417 67.8786C120.48 67.9589 119.536 67.8734 118.628 67.6259L114.5 66.5L119.063 65.6703C119.686 65.5572 120.319 65.5182 120.951 65.5543L136.102 66.4201C136.226 66.4272 136.229 66.609 136.105 66.6196Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M92.5649 79.8671L119.363 73.562C119.736 73.4742 120 73.1411 120 72.7575C120 72.3291 119.673 71.9716 119.246 71.9342L90.4698 69.4121H70.604L40.6231 71.9476C40.2708 71.9774 40 72.2721 40 72.6257C40 72.9393 40.2143 73.2123 40.519 73.2867L67.4153 79.8572C67.8037 79.952 68.2021 80 68.6019 80H91.4197C91.8053 80 92.1895 79.9554 92.5649 79.8671Z" fill="${e}" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M100.817 86.0114L92 80H88L99.3611 86.0863C100.986 86.9567 102 88.6505 102 90.4937V95.5C102 95.7761 102.224 96 102.5 96C102.776 96 103 95.7761 103 95.5V90.1425C103 88.4892 102.183 86.9428 100.817 86.0114Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M58 90.0902V95.5C58 95.7761 57.7761 96 57.5 96C57.2239 96 57 95.7761 57 95.5V89.7447C57 88.0352 57.8734 86.4442 59.3156 85.5264L66.7716 80.7817C67.5739 80.2712 68.5051 80 69.456 80H72L60.7639 85.618C59.07 86.465 58 88.1963 58 90.0902Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M100.817 86.0114L92 80H88L99.3611 86.0863C100.986 86.9567 102 88.6505 102 90.4937V95.5C102 95.7761 102.224 96 102.5 96C102.776 96 103 95.7761 103 95.5V90.1425C103 88.4892 102.183 86.9428 100.817 86.0114Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M58 90.0902V95.5C58 95.7761 57.7761 96 57.5 96C57.2239 96 57 95.7761 57 95.5V89.7447C57 88.0352 57.8734 86.4442 59.3156 85.5264L66.7716 80.7817C67.5739 80.2712 68.5051 80 69.456 80H72L60.7639 85.618C59.07 86.465 58 88.1963 58 90.0902Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,lo=co(`var(--instrument-frame-primary-color)`),uo=co(`var(--container-background-color)`),fo=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="80" cy="61" rx="4" ry="4" transform="rotate(90 80 61)" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M86 60C87.1046 60 88 60.8954 88 62L88 86C88 87.1046 87.1046 88 86 88L74 88C72.8954 88 72 87.1046 72 86L72 62C72 60.8954 72.8954 60 74 60L86 60Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M113.61 46.5204C113.678 46.429 113.565 46.3127 113.472 46.3788L92.0296 61.7523C89.9911 63.2139 87.5458 63.9999 85.0374 63.9999H73.9992C71.4028 63.9999 68.8764 63.1578 66.7993 61.6L46.5198 46.3906C46.4283 46.3221 46.3126 46.4353 46.3791 46.5283L61.7526 67.9705C63.2142 70.0091 64.0002 72.4544 64.0002 74.9627V85.0371C64.0002 87.5455 63.2142 89.9908 61.7526 92.0293L46.3791 113.472C46.3125 113.565 46.4283 113.679 46.5198 113.61L66.8002 98.3999C68.8774 96.8421 71.4038 95.9999 74.0002 95.9999H85.0373C87.5457 95.9999 89.9911 96.786 92.0297 98.2477L113.472 113.622C113.565 113.688 113.678 113.572 113.61 113.48L98.4002 93.2009C96.8423 91.1237 96.0002 88.5974 96.0002 86.001V73.999C96.0002 71.4025 96.8424 68.8761 98.4003 66.7989L113.61 46.5204Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M45.6232 41C44.5326 41 43.5232 41.3497 42.7013 41.9424L42.3039 41.5957C41.8708 41.2171 41.2951 41.0437 40.7248 41.1191L24.0129 43.334C23.2505 43.4352 22.613 43.9652 22.3742 44.6963L22.05 45.6895C21.8392 46.3356 22.3215 46.9997 23.0011 47H40.7238C41.1872 49.2821 43.2043 51 45.6232 51C46.7144 50.9999 47.7231 50.649 48.5451 50.0557L48.9406 50.4033C49.3738 50.7823 49.9501 50.9564 50.5207 50.8809L67.2316 48.665C67.9941 48.5639 68.6315 48.0339 68.8703 47.3027L69.1945 46.3096C69.4051 45.6635 68.9238 45.0004 68.2443 45H50.5226C50.0594 42.718 48.0419 41.0003 45.6232 41ZM43.8927 47C44.2387 47.5972 44.8834 48 45.6232 48C45.795 47.9999 45.9612 47.9754 46.1203 47.9346L47.7677 49.375C47.1479 49.7698 46.4126 49.9999 45.6232 50C43.7593 50 42.1922 48.7253 41.7482 47H43.8927ZM45.6232 42C47.4868 42.0003 49.0533 43.2749 49.4972 45H47.3527C47.0068 44.403 46.3628 44.0002 45.6232 44C45.4516 44 45.2851 44.0238 45.1261 44.0645L43.4797 42.623C44.0992 42.2291 44.8346 42 45.6232 42Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M40.1992 91.1499C39.5205 91.1136 39.0039 91.7511 39.1797 92.4077L43.7666 109.526C41.6821 110.564 40.545 112.957 41.1709 115.293C41.4534 116.348 42.0529 117.232 42.8389 117.873L42.6055 118.344C42.3516 118.861 42.3331 119.462 42.5537 119.994L49.0185 135.562C49.3136 136.272 49.9907 136.751 50.7588 136.792L51.8017 136.848C52.4803 136.884 52.9969 136.248 52.8213 135.591L48.2344 118.473C50.3187 117.435 51.4559 115.042 50.8301 112.706C50.5478 111.652 49.9491 110.768 49.1641 110.127L49.3955 109.654C49.6491 109.137 49.6678 108.537 49.4473 108.005L42.9824 92.4361C42.6873 91.7258 42.0101 91.247 41.2422 91.2056L40.1992 91.1499ZM48.708 111.056C49.2486 111.553 49.6602 112.203 49.8642 112.964C50.3464 114.765 49.5201 116.608 47.9687 117.483L47.4141 115.412C47.9013 114.923 48.123 114.196 47.9316 113.482C47.8872 113.316 47.8217 113.161 47.7412 113.018L48.708 111.056ZM44.5859 112.586C44.0986 113.075 43.877 113.802 44.0683 114.517C44.1129 114.683 44.18 114.838 44.2607 114.981L43.2949 116.944C42.7534 116.447 42.341 115.797 42.1367 115.035C41.6545 113.235 42.4799 111.392 44.0312 110.516L44.5859 112.586Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M96.6179 32.8858C95.9071 32.5923 95.0906 32.7324 94.5183 33.2461L93.7409 33.9444C93.2354 34.3986 93.3203 35.2148 93.9089 35.5547L109.257 44.4151C108.517 46.6231 109.405 49.1196 111.5 50.3291C112.445 50.8748 113.494 51.0755 114.503 50.9727L114.672 51.4717C114.857 52.0166 115.269 52.455 115.801 52.6748L131.382 59.1114C132.092 59.405 132.909 59.2648 133.481 58.751L134.26 58.0528C134.764 57.5984 134.679 56.7843 134.091 56.4444L118.743 47.583C119.483 45.375 118.594 42.8785 116.5 41.669C115.555 41.1238 114.507 40.9221 113.499 41.0244L113.328 40.5254C113.142 39.981 112.731 39.5431 112.199 39.3233L96.6179 32.8858ZM112.001 46C112.002 46.6902 112.359 47.3615 113 47.7315C113.149 47.8175 113.305 47.8796 113.464 47.9239L114.17 49.9942C113.435 50.026 112.683 49.8576 112 49.4629C110.386 48.531 109.666 46.6438 110.144 44.9278L112.001 46ZM113.833 42.003C114.566 41.9716 115.317 42.141 116 42.5352C117.614 43.4671 118.332 45.3543 117.854 47.0703L115.998 45.9981C115.997 45.3079 115.64 44.6366 115 44.2666C114.851 44.1808 114.695 44.1185 114.537 44.0743L113.833 42.003Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M134.569 102.481C134.429 101.816 133.68 101.482 133.091 101.822L117.743 110.683C116.201 108.938 113.595 108.459 111.5 109.668C110.555 110.214 109.856 111.022 109.441 111.947L108.925 111.844C108.36 111.732 107.774 111.87 107.318 112.221L93.9533 122.495C93.3435 122.964 93.0562 123.741 93.215 124.494L93.4308 125.516C93.5715 126.181 94.3207 126.515 94.9093 126.176L110.257 117.314C111.799 119.059 114.405 119.537 116.5 118.328C117.444 117.783 118.143 116.976 118.559 116.052L119.076 116.153C119.641 116.265 120.226 116.127 120.682 115.776L134.047 105.503C134.657 105.034 134.944 104.255 134.785 103.503L134.569 102.481ZM117.544 115.851C117.205 116.502 116.683 117.069 116 117.463C114.386 118.395 112.392 118.074 111.145 116.802L113.001 115.729C113.599 116.074 114.359 116.1 115 115.73C115.149 115.644 115.281 115.54 115.399 115.426L117.544 115.851ZM112 110.534C113.614 109.602 115.608 109.923 116.856 111.195L114.999 112.267C114.401 111.923 113.641 111.897 113 112.266C112.851 112.353 112.719 112.457 112.602 112.572L110.455 112.147C110.795 111.496 111.317 110.929 112 110.534Z" fill="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,po=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M121.033 100.2L101 80H96L118.289 99.8667C118.741 100.27 119 100.846 119 101.452V102.835C119 103.478 119.522 104 120.165 104C120.809 104 121.33 103.478 121.33 102.835V100.922C121.33 100.652 121.223 100.392 121.033 100.2Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M39.2975 100.2L59.3301 80H64.3301L42.0407 99.8667C41.5887 100.27 41.3301 100.846 41.3301 101.452V102.835C41.3301 103.478 40.8085 104 40.1651 104C39.5216 104 39 103.478 39 102.835V100.922C39 100.652 39.1069 100.392 39.2975 100.2Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M121.033 100.2L101 80H96L118.289 99.8667C118.741 100.27 119 100.846 119 101.452V102.835C119 103.478 119.522 104 120.165 104C120.809 104 121.33 103.478 121.33 102.835V100.922C121.33 100.652 121.223 100.392 121.033 100.2Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M39.2975 100.2L59.3301 80H64.3301L42.0407 99.8667C41.5887 100.27 41.3301 100.846 41.3301 101.452V102.835C41.3301 103.478 40.8085 104 40.1651 104C39.5216 104 39 103.478 39 102.835V100.922C39 100.652 39.1069 100.392 39.2975 100.2Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M118 64H126V77.8755C126 79.2677 125.637 80.6358 124.946 81.8446L123.736 83.9611C122.969 85.3048 121.031 85.3048 120.264 83.9611L119.054 81.8446C118.363 80.6358 118 79.2677 118 77.8755V64Z" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M34 64H42V77.8755C42 79.2677 41.6367 80.6358 40.9459 81.8446L39.7365 83.9611C38.9687 85.3048 37.0313 85.3048 36.2635 83.9611L35.0541 81.8446C34.3633 80.6358 34 79.2677 34 77.8755V64Z" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M134 75.1317V73H120H98L90 79.9999L132.136 77.127C133.185 77.0555 134 76.1834 134 75.1317Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M26 75.1346V73H40H62L69 79.9999L27.8608 77.1298C26.8128 77.0567 26 76.1852 26 75.1346Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M93.039 84.5757L97.8895 73.2577C97.9624 73.0877 98 72.9046 98 72.7196V70.8904C98 69.6891 97.4814 68.5462 96.5773 67.7552C92.3372 64.045 86.8945 62 81.2603 62H78.8149C73.1357 62 67.653 64.0794 63.4022 67.8456C62.5105 68.6356 62 69.7699 62 70.9613V73L66.961 84.5757C67.5913 86.0464 69.0375 87 70.6376 87H89.3624C90.9625 87 92.4087 86.0464 93.039 84.5757Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="12.5" y="57.5" width="51" height="7" rx="1.5" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="96.5" y="57.5" width="51" height="7" rx="1.5" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="80" cy="79" rx="6" ry="6" transform="rotate(90 80 79)" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="80" cy="79" rx="4" ry="4" transform="rotate(90 80 79)" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="81" cy="78" rx="2" ry="2" transform="rotate(90 81 78)" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,mo=e=>k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M131 75C133.209 75 135 76.7909 135 79C135 81.2091 133.209 83 131 83V75Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M132 84V74C132 73.4477 131.552 73 131 73H89L98.7002 84.6402C98.8901 84.8682 99.1716 85 99.4684 85H131C131.552 85 132 84.5523 132 84Z" fill="${e}" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M129.736 73.4611L122.576 85.9923C122.22 86.6154 121.557 87 120.839 87H69.8301C69.2805 87 68.7346 86.9094 68.2144 86.7317L28 73V68.0879L29.1795 65.9233C30.0014 64.415 31.5399 63.4342 33.2542 63.3257L70 61H90L124.906 65.3632C125.627 65.4533 126.319 65.6995 126.935 66.0846L129.925 67.9534C129.972 67.9824 130 68.0332 130 68.0879V72.4689C130 72.8169 129.909 73.159 129.736 73.4611Z" fill="${e}"/>
<path d="M28 68.0879V73L68.2144 86.7317C68.7346 86.9094 69.2805 87 69.8301 87H120.839C121.557 87 122.22 86.6154 122.576 85.9923L129.736 73.4611C129.909 73.159 130 72.8169 130 72.4689V68.0879M28 68.0879L29.1795 65.9233C30.0014 64.415 31.5399 63.4342 33.2542 63.3257L70 61H90L124.906 65.3632C125.627 65.4533 126.319 65.6995 126.935 66.0846L129.925 67.9534C129.972 67.9824 130 68.0332 130 68.0879M28 68.0879H130" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M128.918 100.202L101 80H96L126.097 99.9027C126.661 100.276 127 100.907 127 101.583V102.835C127 103.478 127.522 104 128.165 104C128.809 104 129.33 103.478 129.33 102.835V101.009C129.33 100.689 129.177 100.389 128.918 100.202Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M31.4125 100.202L58.3301 80H63.3301L34.2334 99.9027C33.6694 100.276 33.3301 100.907 33.3301 101.583V102.835C33.3301 103.478 32.8085 104 32.1651 104C31.5216 104 31 103.478 31 102.835V101.009C31 100.689 31.1534 100.389 31.4125 100.202Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M128.918 100.202L101 80H96L126.097 99.9027C126.661 100.276 127 100.907 127 101.583V102.835C127 103.478 127.522 104 128.165 104C128.809 104 129.33 103.478 129.33 102.835V101.009C129.33 100.689 129.177 100.389 128.918 100.202Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M31.4125 100.202L58.3301 80H63.3301L34.2334 99.9027C33.6694 100.276 33.3301 100.907 33.3301 101.583V102.835C33.3301 103.478 32.8085 104 32.1651 104C31.5216 104 31 103.478 31 102.835V101.009C31 100.689 31.1534 100.389 31.4125 100.202Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M118 64H126V73.8755C126 75.2677 125.637 76.6358 124.946 77.8446L123.736 79.9611C122.969 81.3048 121.031 81.3048 120.264 79.9611L119.054 77.8446C118.363 76.6358 118 75.2677 118 73.8755V64Z" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M34 64H42V73.8755C42 75.2677 41.6367 76.6358 40.9459 77.8446L39.7365 79.9611C38.9687 81.3048 37.0313 81.3048 36.2635 79.9611L35.0541 77.8446C34.3633 76.6358 34 75.2677 34 73.8755V64Z" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M127 75.1735V74C127 73.4477 126.552 73 126 73H120H98.5803C98.2215 73 97.8901 73.1923 97.7121 73.5039L94.9519 78.3342C94.5507 79.0363 95.1053 79.8995 95.9106 79.8263L125.181 77.1653C126.211 77.0717 127 76.2079 127 75.1735Z" fill="${e}" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M32 75.1735V74C32 73.4477 32.4477 73 33 73H40H61.3406C61.7406 73 62.1022 73.2384 62.2598 73.6061L64.3393 78.4583C64.6376 79.1544 64.0839 79.9167 63.3296 79.8481L33.8189 77.1653C32.7888 77.0717 32 76.2079 32 75.1735Z" fill="${e}" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="12.5" y="57.5" width="51" height="7" rx="1.5" fill="${e}" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="96.5" y="57.5" width="51" height="7" rx="1.5" fill="${e}" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,ho=mo(`var(--instrument-frame-primary-color)`),go=mo(`var(--container-background-color)`),_o=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="80" cy="25" rx="4" ry="4" transform="rotate(90 80 25)" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M87.5 26L87.5 50C87.5 50.8284 86.8284 51.5 86 51.5L74 51.5C73.1716 51.5 72.5 50.8284 72.5 50L72.5 26C72.5 25.1716 73.1716 24.5 74 24.5L86 24.5C86.8284 24.5 87.5 25.1716 87.5 26Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<g clip-path="url(#clip0_30829_50593)">
<path d="M74.124 68.9067L34.8998 38.5288C34.1757 37.968 33.974 36.9602 34.4265 36.164C34.8921 35.3447 35.9013 35.0093 36.7647 35.387L81.9764 55.1651C82.5202 55.403 82.7383 56.0593 82.4451 56.5754L75.6058 68.6102C75.305 69.1394 74.6053 69.2794 74.124 68.9067Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M74.124 91.0923L34.8998 121.47C34.1757 122.031 33.974 123.039 34.4265 123.835C34.8921 124.654 35.9013 124.99 36.7647 124.612L81.9764 104.834C82.5202 104.596 82.7383 103.94 82.4451 103.424L75.6058 91.3888C75.305 90.8597 74.6053 90.7196 74.124 91.0923Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M85.8757 68.9067L125.1 38.5288C125.824 37.968 126.026 36.9602 125.573 36.164C125.108 35.3447 124.098 35.0093 123.235 35.387L78.0233 55.1651C77.4795 55.403 77.2614 56.0593 77.5546 56.5754L84.394 68.6102C84.6947 69.1394 85.3945 69.2794 85.8757 68.9067Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M85.8757 91.0923L125.1 121.47C125.824 122.031 126.026 123.039 125.573 123.835C125.108 124.654 124.098 124.99 123.235 124.612L78.0233 104.834C77.4795 104.596 77.2614 103.94 77.5546 103.424L84.394 91.3889C84.6947 90.8597 85.3945 90.7196 85.8757 91.0923Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M74.124 68.9067L34.8998 38.5288C34.1757 37.968 33.974 36.9602 34.4265 36.164C34.8921 35.3447 35.9013 35.0093 36.7647 35.387L81.9764 55.1651C82.5202 55.403 82.7383 56.0593 82.4451 56.5754L75.6058 68.6102C75.305 69.1394 74.6053 69.2794 74.124 68.9067Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M74.124 91.0923L34.8998 121.47C34.1757 122.031 33.974 123.039 34.4265 123.835C34.8921 124.654 35.9013 124.99 36.7647 124.612L81.9764 104.834C82.5202 104.596 82.7383 103.94 82.4451 103.424L75.6058 91.3888C75.305 90.8597 74.6053 90.7196 74.124 91.0923Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M85.8757 68.9067L125.1 38.5288C125.824 37.968 126.026 36.9602 125.573 36.164C125.108 35.3447 124.098 35.0093 123.235 35.387L78.0233 55.1651C77.4795 55.403 77.2614 56.0593 77.5546 56.5754L84.394 68.6102C84.6947 69.1394 85.3945 69.2794 85.8757 68.9067Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M85.8757 91.0923L125.1 121.47C125.824 122.031 126.026 123.039 125.573 123.835C125.108 124.654 124.098 124.99 123.235 124.612L78.0233 104.834C77.4795 104.596 77.2614 103.94 77.5546 103.424L84.394 91.3889C84.6947 90.8597 85.3945 90.7196 85.8757 91.0923Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M68.6243 31.3047C68.9292 29.3933 70.431 28 72.1856 28H87.8144C89.569 28 91.0707 29.3933 91.3757 31.3047L92.8953 40.8301C94.9619 53.7844 96 66.8819 96 80C96 93.1181 94.9619 106.216 92.8953 119.17L91.3757 128.695C91.0707 130.607 89.569 132 87.8144 132H72.1856C70.431 132 68.9292 130.607 68.6243 128.695L67.1047 119.17C65.0381 106.216 64 93.1181 64 80C64 66.8819 65.0381 53.7844 67.1047 40.8301L68.6243 31.3047Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.4682 106.879C22.8625 107.187 22.7343 107.997 23.2148 108.477L34.2813 119.544C33.9279 120.078 33.6995 120.671 33.6004 121.281L33.2282 121.307C32.6539 121.345 32.1234 121.629 31.7733 122.086L22.7805 133.829C22.313 134.439 22.2372 135.264 22.585 135.949L22.8771 136.525C23.185 137.131 23.9943 137.259 24.475 136.779L35.5381 125.716C36.0735 126.071 36.669 126.297 37.281 126.397L37.3058 126.767C37.3442 127.341 37.6284 127.872 38.0855 128.222L49.8273 137.215C50.4379 137.683 51.2628 137.758 51.9486 137.41L52.5231 137.119C53.1293 136.811 53.2587 136.001 52.7779 135.52L41.7128 124.455C42.0676 123.919 42.2974 123.325 42.3965 122.713L42.7666 122.69C43.341 122.651 43.8715 122.367 44.2215 121.91L53.2144 110.168C53.6818 109.557 53.7585 108.732 53.4105 108.046L53.1184 107.471C52.8104 106.865 51.9998 106.737 51.5191 107.217L40.4561 118.28C39.9199 117.925 39.3238 117.697 38.7111 117.599L38.6869 117.23C38.6485 116.656 38.3643 116.126 37.9073 115.776L26.1648 106.783C25.5541 106.315 24.7293 106.238 24.0434 106.587L23.4682 106.879Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="37.9998" cy="122" r="2" transform="rotate(-45 37.9998 122)" fill="var(--container-background-color)"/>
<path d="M19.2617 103.262C8.91278 113.611 8.91278 130.39 19.2617 140.738C29.6106 151.087 46.3894 151.087 56.7383 140.738C67.0872 130.39 67.0872 113.611 56.7383 103.262C46.3894 92.9129 29.6106 92.9129 19.2617 103.262ZM22.0901 106.09C30.8769 97.3034 45.1231 97.3034 53.9099 106.09C62.6967 114.877 62.6967 129.123 53.9099 137.91C45.1231 146.697 30.8769 146.697 22.0901 137.91C13.3033 129.123 13.3033 114.877 22.0901 106.09Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M19.2617 103.262L19.6152 103.615C9.46159 113.769 9.46159 130.231 19.6152 140.385L19.2617 140.738L18.9081 141.092C8.36396 130.548 8.36396 113.452 18.9081 102.908L19.2617 103.262ZM19.2617 140.738L19.6152 140.385C29.7689 150.539 46.2311 150.539 56.3848 140.385L56.7383 140.738L57.0919 141.092C46.5477 151.636 29.4523 151.636 18.9081 141.092L19.2617 140.738ZM56.7383 140.738L56.3848 140.385C66.5384 130.231 66.5384 113.769 56.3848 103.615L56.7383 103.262L57.0919 102.908C67.636 113.452 67.636 130.548 57.0919 141.092L56.7383 140.738ZM56.7383 103.262L56.3848 103.615C46.2311 93.4617 29.7689 93.4617 19.6152 103.615L19.2617 103.262L18.9081 102.908C29.4523 92.3641 46.5477 92.3641 57.0919 102.908L56.7383 103.262ZM22.0901 106.09L21.7365 105.737C30.7186 96.7546 45.2814 96.7546 54.2635 105.737L53.9099 106.09L53.5563 106.444C44.9648 97.8522 31.0352 97.8522 22.4437 106.444L22.0901 106.09ZM53.9099 106.09L54.2635 105.737C63.2455 114.719 63.2455 129.281 54.2635 138.264L53.9099 137.91L53.5563 137.556C62.1479 128.965 62.1479 115.035 53.5563 106.444L53.9099 106.09ZM53.9099 137.91L54.2635 138.264C45.2814 147.246 30.7186 147.246 21.7365 138.264L22.0901 137.91L22.4437 137.556C31.0352 146.148 44.9648 146.148 53.5563 137.556L53.9099 137.91ZM22.0901 137.91L21.7365 138.264C12.7545 129.281 12.7545 114.719 21.7365 105.737L22.0901 106.09L22.4437 106.444C13.8521 115.035 13.8521 128.965 22.4437 137.556L22.0901 137.91Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M38.4178 17.0324C37.7716 16.8217 37.1075 17.303 37.1072 17.9826V33.634C36.4794 33.7621 35.8989 34.0194 35.3973 34.3811L35.116 34.136C34.6827 33.757 34.1066 33.5828 33.5359 33.6584L18.8748 35.6028C18.1124 35.7038 17.475 36.233 17.2361 36.9641L17.0359 37.5774C16.825 38.2236 17.3064 38.8877 17.9861 38.8879H33.6336C33.7611 39.5168 34.0227 40.0964 34.3846 40.5988L34.1385 40.8801C33.7596 41.3134 33.5853 41.8896 33.6609 42.4602L35.6053 57.1213C35.7064 57.8837 36.2357 58.5211 36.9666 58.76L37.5799 58.9602C38.2261 59.171 38.8902 58.6896 38.8904 58.01V42.3615C39.5198 42.2336 40.1016 41.9762 40.6043 41.6135L40.8836 41.8586C41.3168 42.2376 41.8921 42.4117 42.4627 42.3362L57.1248 40.3918C57.8873 40.2907 58.5247 39.7617 58.7635 39.0305L58.9637 38.4172C59.1743 37.7711 58.6931 37.1079 58.0135 37.1076H42.367C42.2391 36.4769 41.9785 35.8942 41.615 35.3908L41.8582 35.1125C42.2372 34.6793 42.4113 34.104 42.3357 33.5334L40.3924 18.8713C40.2913 18.1088 39.7613 17.4714 39.0301 17.2326L38.4178 17.0324Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="38" cy="38" r="2" fill="var(--container-background-color)"/>
<path d="M38 11.5C23.3645 11.5 11.5 23.3645 11.5 38C11.5 52.6355 23.3645 64.5 38 64.5C52.6355 64.5 64.5 52.6355 64.5 38C64.5 23.3645 52.6355 11.5 38 11.5ZM38 15.5C50.4264 15.5 60.5 25.5736 60.5 38C60.5 50.4264 50.4264 60.5 38 60.5C25.5736 60.5 15.5 50.4264 15.5 38C15.5 25.5736 25.5736 15.5 38 15.5Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M38 11.5V12C23.6406 12 12 23.6406 12 38H11.5H11C11 23.0883 23.0883 11 38 11V11.5ZM11.5 38H12C12 52.3594 23.6406 64 38 64V64.5V65C23.0883 65 11 52.9117 11 38H11.5ZM38 64.5V64C52.3594 64 64 52.3594 64 38H64.5H65C65 52.9117 52.9117 65 38 65V64.5ZM64.5 38H64C64 23.6406 52.3594 12 38 12V11.5V11C52.9117 11 65 23.0883 65 38H64.5ZM38 15.5V15C50.7025 15 61 25.2975 61 38H60.5H60C60 25.8497 50.1503 16 38 16V15.5ZM60.5 38H61C61 50.7025 50.7025 61 38 61V60.5V60C50.1503 60 60 50.1503 60 38H60.5ZM38 60.5V61C25.2975 61 15 50.7025 15 38H15.5H16C16 50.1503 25.8497 60 38 60V60.5ZM15.5 38H15C15 25.2975 25.2975 15 38 15V15.5V16C25.8497 16 16 25.8497 16 38H15.5Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M111.878 103.633C111.213 103.773 110.879 104.522 111.219 105.111L119.044 118.665C118.565 119.09 118.191 119.603 117.937 120.167L117.571 120.095C117.006 119.983 116.42 120.121 115.964 120.472L104.238 129.486C103.629 129.955 103.342 130.732 103.5 131.484L103.634 132.115C103.774 132.781 104.523 133.114 105.111 132.774L118.661 124.952C119.086 125.433 119.603 125.806 120.168 126.06L120.096 126.424C119.985 126.989 120.122 127.575 120.473 128.032L129.487 139.758C129.956 140.367 130.733 140.653 131.485 140.495L132.116 140.362C132.781 140.222 133.116 139.473 132.776 138.884L124.951 125.332C125.433 124.906 125.808 124.392 126.063 123.827L126.426 123.9C126.991 124.011 127.577 123.874 128.033 123.523L139.759 114.508C140.368 114.04 140.656 113.263 140.497 112.51L140.364 111.879C140.223 111.214 139.474 110.88 138.885 111.22L125.336 119.042C124.91 118.56 124.393 118.186 123.827 117.932L123.898 117.571C124.01 117.006 123.873 116.42 123.522 115.963L114.507 104.238C114.038 103.628 113.261 103.341 112.509 103.499L111.878 103.633Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="122" cy="122.002" r="2" transform="rotate(-30 122 122.002)" fill="var(--container-background-color)"/>
<path d="M108.751 99.0508C96.0758 106.369 91.7331 122.576 99.0508 135.25C106.369 147.925 122.576 152.268 135.251 144.95C147.925 137.632 152.268 121.425 144.95 108.75C137.632 96.0757 121.425 91.733 108.751 99.0508ZM110.751 102.515C121.512 96.3017 135.273 99.9889 141.486 110.75C147.699 121.512 144.012 135.273 133.251 141.486C122.489 147.699 108.728 144.012 102.515 133.25C96.3017 122.489 99.9889 108.728 110.751 102.515Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M108.751 99.0508L109.001 99.4838C96.5649 106.663 92.3042 122.565 99.4839 135L99.0508 135.25L98.6178 135.5C91.162 122.587 95.5866 106.074 108.501 98.6178L108.751 99.0508ZM99.0508 135.25L99.4839 135C106.664 147.436 122.565 151.697 135.001 144.517L135.251 144.95L135.501 145.383C122.587 152.839 106.074 148.414 98.6178 135.5L99.0508 135.25ZM135.251 144.95L135.001 144.517C147.436 137.337 151.697 121.436 144.517 109L144.95 108.75L145.383 108.5C152.839 121.414 148.414 137.927 135.501 145.383L135.251 144.95ZM144.95 108.75L144.517 109C137.337 96.5648 121.436 92.3041 109.001 99.4838L108.751 99.0508L108.501 98.6178C121.414 91.1619 137.927 95.5866 145.383 108.5L144.95 108.75ZM110.751 102.515L110.501 102.082C121.501 95.7306 135.568 99.4997 141.919 110.5L141.486 110.75L141.053 111C134.978 100.478 121.523 96.8728 111.001 102.948L110.751 102.515ZM141.486 110.75L141.919 110.5C148.27 121.501 144.501 135.568 133.501 141.919L133.251 141.486L133.001 141.053C143.523 134.978 147.128 121.523 141.053 111L141.486 110.75ZM133.251 141.486L133.501 141.919C122.5 148.27 108.433 144.501 102.082 133.5L102.515 133.25L102.948 133C109.023 143.523 122.478 147.128 133.001 141.053L133.251 141.486ZM102.515 133.25L102.082 133.5C95.7307 122.5 99.4998 108.433 110.501 102.082L110.751 102.515L111.001 102.948C100.478 109.023 96.8728 122.478 102.948 133L102.515 133.25Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M132.845 20.0475C132.391 19.5422 131.575 19.6279 131.236 20.2165L123.41 33.7701C122.803 33.5671 122.171 33.4998 121.556 33.5621L121.435 33.2092C121.249 32.6644 120.837 32.2255 120.305 32.0056L106.635 26.3584C105.925 26.0649 105.109 26.205 104.536 26.7185L104.056 27.1495C103.551 27.6038 103.636 28.4188 104.225 28.7588L117.774 36.5815C117.569 37.1906 117.505 37.8244 117.567 38.4413L117.216 38.5611C116.671 38.7468 116.233 39.1586 116.013 39.6907L110.365 53.3601C110.071 54.0709 110.212 54.8872 110.726 55.4596L111.156 55.9391C111.61 56.4449 112.426 56.3603 112.766 55.7715L120.59 42.2195C121.199 42.4235 121.832 42.4919 122.449 42.4291L122.568 42.7806C122.753 43.3254 123.165 43.7643 123.697 43.9842L137.367 49.6314C138.078 49.9248 138.895 49.7854 139.467 49.2718L139.947 48.8407C140.452 48.3865 140.367 47.5702 139.779 47.2302L126.229 39.4074C126.433 38.7976 126.499 38.1629 126.436 37.5455L126.785 37.4269C127.33 37.2412 127.769 36.8293 127.989 36.2973L133.636 22.6274C133.93 21.9165 133.79 21.0999 133.276 20.5276L132.845 20.0475Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="122" cy="37.9996" r="2" transform="rotate(30 122 37.9996)" fill="var(--container-background-color)"/>
<path d="M135.251 15.0488C122.576 7.73106 106.369 12.0737 99.0508 24.7485C91.7331 37.4233 96.0758 53.6304 108.751 60.9482C121.425 68.2659 137.632 63.9233 144.95 51.2485C152.268 38.5737 147.925 22.3666 135.251 15.0488ZM133.251 18.5129C144.012 24.7261 147.699 38.4869 141.486 49.2485C135.273 60.0101 121.512 63.6973 110.751 57.4841C99.9889 51.2709 96.3017 37.5101 102.515 26.7485C108.728 15.9869 122.489 12.2997 133.251 18.5129Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M135.251 15.0488L135.001 15.4818C122.565 8.30214 106.664 12.5629 99.4839 24.9985L99.0508 24.7485L98.6178 24.4985C106.074 11.5846 122.587 7.15997 135.501 14.6158L135.251 15.0488ZM99.0508 24.7485L99.4839 24.9985C92.3042 37.4341 96.5649 53.3355 109.001 60.5152L108.751 60.9482L108.501 61.3812C95.5866 53.9253 91.162 37.4124 98.6178 24.4985L99.0508 24.7485ZM108.751 60.9482L109.001 60.5152C121.436 67.6949 137.337 63.4341 144.517 50.9985L144.95 51.2485L145.383 51.4985C137.927 64.4124 121.414 68.837 108.501 61.3812L108.751 60.9482ZM144.95 51.2485L144.517 50.9985C151.697 38.5629 147.436 22.6615 135.001 15.4818L135.251 15.0488L135.501 14.6158C148.414 22.0717 152.839 38.5846 145.383 51.4985L144.95 51.2485ZM133.251 18.5129L133.501 18.0799C144.501 24.4312 148.27 38.4978 141.919 49.4985L141.486 49.2485L141.053 48.9985C147.128 38.4761 143.523 25.0211 133.001 18.9459L133.251 18.5129ZM141.486 49.2485L141.919 49.4985C135.568 60.4992 121.501 64.2684 110.501 57.9171L110.751 57.4841L111.001 57.0511C121.523 63.1262 134.978 59.5209 141.053 48.9985L141.486 49.2485ZM110.751 57.4841L110.501 57.9171C99.4998 51.5658 95.7307 37.4992 102.082 26.4985L102.515 26.7485L102.948 26.9985C96.8728 37.5209 100.478 50.9759 111.001 57.0511L110.751 57.4841ZM102.515 26.7485L102.082 26.4985C108.433 15.4978 122.5 11.7286 133.501 18.0799L133.251 18.5129L133.001 18.9459C122.478 12.8708 109.023 16.4761 102.948 26.9985L102.515 26.7485Z" fill="var(--instrument-tick-mark-secondary-color)"/>
</g>
<defs>
<clipPath id="clip0_30829_50593">
<rect width="160" height="160" fill="var(--instrument-frame-primary-color)" transform="matrix(-1 0 0 1 160 0)"/>
</clipPath>
</defs>
</svg>
`,vo=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M114.2 36.8008C118.177 36.8008 121.4 40.0243 121.4 44.0008V119.601C121.4 119.747 121.39 119.89 121.373 120.031C121.348 120.242 121.305 120.446 121.245 120.644C121.239 120.665 121.233 120.685 121.226 120.706C121.179 120.852 121.123 120.994 121.058 121.132C121.05 121.149 121.042 121.166 121.034 121.183C121.016 121.218 120.998 121.253 120.98 121.288C120.971 121.305 120.962 121.322 120.953 121.338C120.934 121.373 120.913 121.407 120.893 121.441C120.886 121.453 120.88 121.465 120.873 121.476C120.82 121.562 120.764 121.644 120.705 121.725C120.695 121.739 120.685 121.753 120.674 121.767C120.472 122.035 120.234 122.273 119.967 122.475C119.953 122.485 119.938 122.495 119.924 122.506C119.844 122.565 119.761 122.621 119.676 122.673C119.664 122.68 119.652 122.687 119.641 122.694C119.606 122.714 119.572 122.734 119.538 122.753C119.521 122.763 119.504 122.772 119.488 122.781C119.453 122.799 119.418 122.817 119.382 122.834C119.365 122.843 119.348 122.851 119.331 122.859C119.294 122.876 119.256 122.893 119.219 122.909C119.209 122.913 119.2 122.917 119.191 122.921C119.097 122.96 119.002 122.995 118.905 123.027C118.884 123.033 118.864 123.04 118.843 123.046C118.807 123.057 118.77 123.068 118.733 123.078C118.719 123.081 118.705 123.086 118.691 123.089C118.639 123.102 118.586 123.114 118.533 123.125C118.53 123.126 118.526 123.127 118.523 123.128C118.472 123.138 118.42 123.147 118.369 123.155C118.36 123.156 118.352 123.158 118.343 123.159C118.306 123.165 118.268 123.169 118.231 123.174C118.21 123.176 118.189 123.18 118.168 123.182L117.986 123.196L117.8 123.201H42.2001L42.0146 123.196C41.9318 123.192 41.8499 123.183 41.7686 123.174C41.7309 123.169 41.6933 123.165 41.6561 123.159C41.6475 123.158 41.6391 123.156 41.6306 123.155C41.5789 123.147 41.5276 123.138 41.4768 123.128C41.4732 123.127 41.4698 123.126 41.4662 123.125C41.4131 123.114 41.3603 123.102 41.308 123.089C41.2942 123.086 41.2805 123.081 41.2667 123.078C41.2295 123.068 41.1926 123.057 41.156 123.046C41.1354 123.04 41.1149 123.033 41.0944 123.027C40.9974 122.995 40.9021 122.96 40.8088 122.921C40.7993 122.917 40.7901 122.913 40.7807 122.909C40.7429 122.893 40.7053 122.876 40.6682 122.859C40.6511 122.851 40.6341 122.843 40.6172 122.834C40.5817 122.817 40.5465 122.799 40.5117 122.781C40.4949 122.772 40.4783 122.763 40.4616 122.753C40.4269 122.734 40.3928 122.714 40.3588 122.694C40.3472 122.687 40.3352 122.68 40.3236 122.673C40.2381 122.621 40.1555 122.565 40.0749 122.506C40.0609 122.495 40.0466 122.485 40.0327 122.475C39.7654 122.273 39.5271 122.035 39.3252 121.767C39.3147 121.753 39.3047 121.739 39.2944 121.725C39.2354 121.644 39.1789 121.562 39.1266 121.476C39.1195 121.465 39.1133 121.453 39.1063 121.441C39.0861 121.407 39.0658 121.373 39.0466 121.338C39.0374 121.322 39.0283 121.305 39.0193 121.288C39.0008 121.253 38.9831 121.218 38.9657 121.183C38.9574 121.166 38.9492 121.149 38.9411 121.132C38.8764 120.994 38.8204 120.852 38.7732 120.706C38.7667 120.685 38.7601 120.665 38.7539 120.644C38.6942 120.446 38.6515 120.242 38.6265 120.031C38.6096 119.89 38.6001 119.747 38.6001 119.601V44.0008C38.6001 40.0243 41.8236 36.8008 45.8001 36.8008H114.2ZM45.8001 40.4008C43.8741 40.4008 42.301 41.9133 42.2045 43.8153L42.2001 44.0008V116.001H117.8V44.0008C117.8 42.0126 116.188 40.4008 114.2 40.4008H45.8001Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<rect x="46.2998" y="81.4004" width="11.6" height="38.6" rx="1.5" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="102.1" y="81.4004" width="11.6" height="38.6" rx="1.5" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M50.5 81.4004H53.7002C54.5285 81.4005 55.2002 82.072 55.2002 82.9004V98.4004H49V82.9004C49 82.072 49.6716 81.4004 50.5 81.4004Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M106.3 81.4004H109.5C110.328 81.4005 111 82.072 111 82.9004V98.4004H104.8V82.9004C104.8 82.072 105.471 81.4004 106.3 81.4004Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M36.7998 44.8008C36.7998 40.3825 40.3815 36.8008 44.7998 36.8008H115.2C119.618 36.8008 123.2 40.3825 123.2 44.8008V76.0008C123.2 78.2099 121.409 80.0008 119.2 80.0008H40.7998C38.5907 80.0008 36.7998 78.2099 36.7998 76.0008V44.8008Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M44 51.5996C44 49.3905 45.7909 47.5996 48 47.5996H112C114.209 47.5996 116 49.3905 116 51.5996V79.9996H44V51.5996Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M116 97.8994C116 98.4517 115.553 98.8994 115 98.8994H111.448C110.959 98.8994 110.542 98.5461 110.461 98.0639L110.194 96.4634C110.093 95.8538 110.563 95.2988 111.181 95.2988H113.038C113.591 95.2988 114.038 94.8511 114.038 94.2988V92.6992C114.038 92.1469 113.591 91.6992 113.038 91.6992H110.248C109.759 91.6992 109.342 91.3459 109.261 90.8638L108.994 89.2642C108.893 88.6546 109.363 88.0996 109.981 88.0996H115C115.553 88.0996 116 88.5473 116 89.0996V97.8994Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M60.1999 97.8994C60.1999 98.4517 59.7522 98.8994 59.1999 98.8994H55.6475C55.1588 98.8994 54.7416 98.5461 54.6612 98.0639L54.3942 96.4634C54.2925 95.8538 54.7626 95.2988 55.3806 95.2988H57.239C57.7913 95.2988 58.239 94.8511 58.239 94.2988V92.6992C58.239 92.1469 57.7913 91.6992 57.239 91.6992H54.4473C53.9585 91.6992 53.5414 91.3459 53.4609 90.8638L53.1941 89.2642C53.0924 88.6546 53.5624 88.0996 54.1804 88.0996H59.1999C59.7522 88.0996 60.1999 88.5473 60.1999 89.0996V97.8994Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M99.8005 97.8994C99.8005 98.4517 100.248 98.8994 100.801 98.8994H104.353C104.842 98.8994 105.259 98.5461 105.339 98.0639L105.606 96.4634C105.708 95.8538 105.238 95.2988 104.62 95.2988H102.599C102.047 95.2988 101.599 94.8511 101.599 94.2988V92.6992C101.599 92.1469 102.047 91.6992 102.599 91.6992H105.553C106.042 91.6992 106.459 91.3459 106.54 90.8638L106.806 89.2642C106.908 88.6546 106.438 88.0996 105.82 88.0996H100.801C100.248 88.0996 99.8005 88.5473 99.8005 89.0996V97.8994Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M44.0004 97.8994C44.0004 98.4517 44.4481 98.8994 45.0004 98.8994H48.5536C49.0425 98.8994 49.4597 98.5459 49.54 98.0637L49.8065 96.4631C49.908 95.8536 49.438 95.2988 48.8201 95.2988H46.8002C46.2479 95.2988 45.8002 94.8511 45.8002 94.2988V92.6992C45.8002 92.1469 46.2479 91.6992 46.8002 91.6992H49.7538C50.2427 91.6992 50.6599 91.3458 50.7402 90.8635L51.0067 89.2639C51.1082 88.6544 50.6382 88.0996 50.0203 88.0996H45.0004C44.4481 88.0996 44.0004 88.5473 44.0004 89.0996V97.8994Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="80" cy="63.8008" r="9" transform="rotate(90 80 63.8008)" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="79.9999" cy="63.8004" r="5.4" transform="rotate(90 79.9999 63.8004)" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="80.0002" cy="114.2" rx="7.2" ry="7.2" transform="rotate(90 80.0002 114.2)" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="80" cy="114.199" r="4.5" transform="rotate(90 80 114.199)" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="49.4" cy="53.0004" rx="3.6" ry="3.6" transform="rotate(90 49.4 53.0004)" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="110.6" cy="53.0004" rx="3.6" ry="3.6" transform="rotate(90 110.6 53.0004)" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="102.5" cy="52.9992" rx="1.8" ry="1.8" transform="rotate(90 102.5 52.9992)" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="80.9002" cy="61.9992" rx="1.8" ry="1.8" transform="rotate(90 80.9002 61.9992)" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<ellipse cx="97.0999" cy="52.9992" rx="1.8" ry="1.8" transform="rotate(90 97.0999 52.9992)" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M74.6001 20.5992C74.6001 17.6169 77.0178 15.1992 80.0001 15.1992C82.9824 15.1992 85.4001 17.6169 85.4001 20.5992V36.7992H74.6001V20.5992Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="76.3999" y="17" width="7.2" height="14.4" rx="3.6" fill="var(--instrument-frame-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,yo=e=>k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M120 115.55C120 108.343 114.157 102.5 106.95 102.5C99.7427 102.5 93.9 108.343 93.9 115.55V121.4H120V115.55Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="5.4" cy="5.4" r="5.4" transform="matrix(-1 0 0 1 135.3 58.4004)" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M129.7 55.3008H108.5C107.672 55.3009 107 55.9724 107 56.8008V70.8008C107 71.6291 107.672 72.3007 108.5 72.3008H129.7C130.529 72.3008 131.2 71.6292 131.2 70.8008V56.8008C131.2 55.9724 130.529 55.3008 129.7 55.3008Z" fill="${e}" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M134.562 97.8994C134.562 98.4517 135.01 98.8994 135.562 98.8994H142.715C143.204 98.8994 143.621 98.5461 143.702 98.0639L143.969 96.4634C144.07 95.8538 143.6 95.2988 142.982 95.2988H140.962C140.409 95.2988 139.962 94.8511 139.962 94.2988V92.6992C139.962 92.1469 140.409 91.6992 140.962 91.6992H143.915C144.404 91.6992 144.821 91.3459 144.902 90.8638L145.169 89.2642C145.27 88.6546 144.8 88.0996 144.182 88.0996H135.562C135.01 88.0996 134.562 88.5473 134.562 89.0996V97.8994Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M113.321 112.227L124.015 91.3626C125.394 88.6706 124.421 85.3695 121.801 83.857C119.182 82.3445 115.836 83.152 114.195 85.6929L101.473 105.386C99.3473 108.676 100.409 113.075 103.801 115.034C107.193 116.992 111.534 115.712 113.321 112.227Z" fill="${e}" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M135.709 91.7969L120.522 85.7094C118.301 84.8189 115.8 86.0699 115.181 88.3818C114.561 90.6937 116.101 93.0274 118.47 93.367L134.666 95.6885C135.683 95.8342 136.648 95.1973 136.914 94.2053C137.18 93.2132 136.662 92.179 135.709 91.7969Z" fill="${e}" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M22.803 119.6V79.9996M105.15 121.4L111 79.0996M70.95 79.0996L65.1 121.4" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)" stroke-width="4"/>
<path d="M110.057 85.9216L105.866 116.222C105.456 119.189 102.919 121.4 99.9227 121.4H71.9869C68.3464 121.4 65.5447 118.184 66.0435 114.578L70.2339 84.2776C70.6443 81.3098 73.1812 79.0996 76.1773 79.0996H104.113C107.754 79.0996 110.555 82.3154 110.057 85.9216Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)" stroke-width="4"/>
<path d="M65.5709 117.996L70.164 84.7846C70.5796 81.7794 68.2449 79.0996 65.2111 79.0996H35.7921C32.4899 79.0996 30.61 82.8747 32.5999 85.51L58.5167 119.832C59.2621 120.819 60.4273 121.4 61.6641 121.4C63.6336 121.4 65.3011 119.947 65.5709 117.996Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)" stroke-width="4"/>
<path d="M22.8032 115.4V82.4082C22.8032 80.5809 24.2845 79.0996 26.1118 79.0996C27.1494 79.0996 28.1269 79.5864 28.7522 80.4144L54.8597 114.989C56.8496 117.624 54.9697 121.4 51.6675 121.4H28.8032C25.4895 121.4 22.8032 118.713 22.8032 115.4Z" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)" stroke-width="4"/>
<path d="M128.655 48.8033L116.284 63.8634C115.351 64.9996 114.749 66.3712 114.544 67.8273L112.832 80.0008H21.2001C20.0955 80.0008 19.2001 79.1054 19.2001 78.0008V40.8008C19.2001 38.5916 20.991 36.8008 23.2001 36.8008H104.552C105.248 36.8008 105.941 36.8916 106.613 37.0709L126.595 42.3994C129.407 43.1492 130.502 46.5547 128.655 48.8033Z" fill="${e}" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M101.999 79.9992C101.999 79.9992 102.265 51.1992 91.2 51.1992C80.1352 51.1992 80.4006 79.9992 80.4006 79.9992" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M130.8 121.4C130.8 120.405 129.994 119.6 129 119.6H20.9998V123.2H129C129.994 123.2 130.8 122.394 130.8 121.4Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M130.8 118C130.8 116.895 129.904 116 128.8 116H20.9998V121.2C20.9998 122.305 21.8952 123.2 22.9998 123.2H128.8C129.904 123.2 130.8 122.305 130.8 121.2V118Z" fill="var(--instrument-tick-mark-secondary-color)"/>
<mask id="path-15-inside-1_25406_62344" fill="${e}">
<path fill-rule="evenodd" clip-rule="evenodd" d="M91.2002 51.1992C87.8899 51.1992 85.5945 53.7775 84.002 57.3906V57.5H98.4023V57.3994C96.8096 53.7817 94.5132 51.1993 91.2002 51.1992Z"/>
</mask>
<path fill-rule="evenodd" clip-rule="evenodd" d="M91.2002 51.1992C87.8899 51.1992 85.5945 53.7775 84.002 57.3906V57.5H98.4023V57.3994C96.8096 53.7817 94.5132 51.1993 91.2002 51.1992Z" fill="${e}"/>
<path d="M91.2002 51.1992V50.1992H91.2002L91.2002 51.1992ZM84.002 57.3906H83.002V57.18L83.0869 56.9873L84.002 57.3906ZM84.002 57.5V58.5H83.002V57.5H84.002ZM98.4023 57.5H99.4023V58.5H98.4023V57.5ZM98.4023 57.3994L99.3176 56.9965L99.4023 57.189V57.3994H98.4023ZM91.2002 51.1992V52.1992C88.5179 52.1992 86.4709 54.2685 84.917 57.794L84.002 57.3906L83.0869 56.9873C84.7181 53.2864 87.2618 50.1992 91.2002 50.1992V51.1992ZM84.002 57.3906H85.002V57.5H84.002H83.002V57.3906H84.002ZM84.002 57.5V56.5H98.4023V57.5V58.5H84.002V57.5ZM98.4023 57.5H97.4023V57.3994H98.4023H99.4023V57.5H98.4023ZM98.4023 57.3994L97.4871 57.8023C95.9329 54.272 93.8846 52.1993 91.2002 52.1992L91.2002 51.1992L91.2002 50.1992C95.1417 50.1993 97.6864 53.2913 99.3176 56.9965L98.4023 57.3994Z" fill="var(--instrument-tick-mark-secondary-color)" mask="url(#path-15-inside-1_25406_62344)"/>
<path d="M91.1997 56.1992C89.2401 56.1992 87.4828 56.3987 86.23 56.7119C85.5997 56.8695 85.1248 57.0492 84.8198 57.2295C84.5739 57.3749 84.5174 57.4716 84.5044 57.499C84.5171 57.526 84.5728 57.6235 84.8198 57.7695C85.1248 57.9498 85.5997 58.1295 86.23 58.2871C87.4828 58.6003 89.2401 58.7988 91.1997 58.7988C93.1592 58.7988 94.9166 58.6003 96.1694 58.2871C96.7997 58.1296 97.2746 57.9498 97.5796 57.7695C97.8287 57.6223 97.8848 57.5251 97.897 57.499C97.8845 57.4724 97.8276 57.3761 97.5796 57.2295C97.2746 57.0492 96.7997 56.8695 96.1694 56.7119C94.9166 56.3987 93.1592 56.1992 91.1997 56.1992Z" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,bo=yo(`var(--instrument-frame-primary-color)`),xo=yo(`var(--container-background-color)`),So=k`<svg width="160" height="160" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="79.9999" cy="26.4996" r="5.4" transform="rotate(90 79.9999 26.4996)" fill="var(--instrument-tick-mark-secondary-color)"/>
<path d="M88.5 26.6992L88.5 47.8994C88.4999 48.7278 87.8284 49.3994 87 49.3994L73 49.3994C72.1716 49.3994 71.5001 48.7277 71.5 47.8994L71.5 26.6992C71.5 25.8708 72.1716 25.1992 73 25.1992L87 25.1992C87.8284 25.1992 88.5 25.8708 88.5 26.6992Z" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="36.7998" y="29.1992" width="86.4" height="111.6" rx="8" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="40.3999" y="54.4004" width="79.2" height="82.8" rx="6" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<circle cx="80.0002" cy="122.8" r="10.8" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M85.8419 122.491C88.6358 122.559 90.3391 125.593 88.9418 128.014C87.5331 130.453 84.0176 130.472 82.5829 128.047L81.4315 126.102C82.7073 125.548 83.5998 124.279 83.5998 122.799C83.5998 122.676 83.5934 122.555 83.5813 122.435L85.8419 122.491Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M76.4235 122.384C76.4079 122.52 76.3998 122.659 76.3998 122.799C76.3998 124.261 77.2714 125.517 78.5224 126.081L77.3464 128.009C75.8906 130.395 72.4116 130.353 71.0139 127.933C69.6052 125.493 71.346 122.439 74.163 122.409L76.4235 122.384Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M80.0464 112.449C82.8632 112.45 84.6366 115.484 83.2544 117.939L82.1443 119.908C81.5453 119.463 80.8033 119.199 79.9998 119.199C79.2137 119.199 78.4868 119.452 77.8948 119.879L76.8129 117.895C75.4747 115.441 77.2512 112.449 80.0464 112.449Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M82.7 122.799C82.7 124.29 81.4912 125.499 80 125.499C78.5089 125.499 77.3 124.29 77.3 122.799C77.3 121.308 78.5089 120.099 80 120.099C81.4912 120.099 82.7 121.308 82.7 122.799Z" fill="var(--instrument-frame-primary-color)"/>
<circle cx="105.2" cy="68.8" r="10.8" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M111.042 68.4907C113.836 68.559 115.539 71.5933 114.141 74.0138C112.733 76.4535 109.217 76.4716 107.783 74.0472L106.631 72.1021C107.907 71.5485 108.8 70.2786 108.8 68.7992C108.8 68.6764 108.793 68.555 108.781 68.4354L111.042 68.4907Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M101.623 68.3844C101.608 68.5205 101.6 68.6589 101.6 68.7992C101.6 70.2605 102.471 71.5169 103.722 72.0811L102.546 74.0094C101.09 76.3954 97.6114 76.3532 96.2136 73.9329C94.805 71.4931 96.5457 68.4393 99.3627 68.409L101.623 68.3844Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M105.246 58.4492C108.063 58.4498 109.836 61.4843 108.454 63.9389L107.344 65.9076C106.745 65.4627 106.003 65.1992 105.2 65.1992C104.413 65.1993 103.687 65.4519 103.095 65.8795L102.013 63.8949C100.674 61.4411 102.451 58.4492 105.246 58.4492Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M107.9 68.7992C107.9 70.2904 106.691 71.4992 105.2 71.4992C103.709 71.4992 102.5 70.2904 102.5 68.7992C102.5 67.308 103.709 66.0992 105.2 66.0992C106.691 66.0992 107.9 67.308 107.9 68.7992Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M101.825 13L99.8 16.6L103.85 23.8L111.95 23.8L116 16.6L113.975 13" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)" stroke-width="4" stroke-linecap="round"/>
<path d="M46.0252 13L44.0002 16.6L48.0502 23.8L56.1502 23.8L60.2002 16.6L58.1752 13" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)" stroke-width="4" stroke-linecap="round"/>
<circle cx="54.8" cy="68.8" r="10.8" fill="var(--instrument-tick-mark-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<path d="M60.6417 68.4907C63.4356 68.559 65.1389 71.5933 63.7416 74.0138C62.3329 76.4535 58.8174 76.4716 57.3827 74.0472L56.2313 72.1021C57.5071 71.5485 58.3996 70.2786 58.3996 68.7992C58.3996 68.6764 58.3932 68.555 58.3811 68.4354L60.6417 68.4907Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M51.2233 68.3844C51.2077 68.5205 51.1996 68.6589 51.1996 68.7992C51.1996 70.2605 52.0712 71.5169 53.3222 72.0811L52.1462 74.0094C50.6904 76.3954 47.2115 76.3532 45.8137 73.9329C44.4051 71.4931 46.1458 68.4393 48.9628 68.409L51.2233 68.3844Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M54.8462 58.4492C57.663 58.4498 59.4364 61.4843 58.0542 63.9389L56.9441 65.9076C56.3451 65.4627 55.6031 65.1992 54.7996 65.1992C54.0135 65.1993 53.2867 65.4519 52.6946 65.8795L51.6127 63.8949C50.2745 61.4411 52.0511 58.4492 54.8462 58.4492Z" fill="var(--instrument-frame-primary-color)"/>
<path d="M57.4998 68.7992C57.4998 70.2904 56.291 71.4992 54.7998 71.4992C53.3087 71.4992 52.0998 70.2904 52.0998 68.7992C52.0998 67.308 53.3087 66.0992 54.7998 66.0992C56.291 66.0992 57.4998 67.308 57.4998 68.7992Z" fill="var(--instrument-frame-primary-color)"/>
<rect x="100.7" y="23.8008" width="14.4" height="5.4" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="44.8999" y="23.8008" width="14.4" height="5.4" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="74.6001" y="76" width="10.8" height="28.8" rx="5.4" fill="var(--instrument-frame-primary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
<rect x="76.3999" y="77.8008" width="7.2" height="14.4" rx="3.6" fill="var(--instrument-frame-secondary-color)" vector-effect="non-scaling-stroke" stroke="var(--instrument-tick-mark-secondary-color)"/>
</svg>
`,Co=function(e){return e.none=`none`,e.small=`small`,e.medium=`medium`,e.large=`large`,e}({}),wo=function(e){return e.carFerryAft=`car-ferry-aft`,e.carFerryFore=`car-ferry-fore`,e.carFerrySide=`car-ferry-side`,e.carFerrySideFaded=`car-ferry-side-faded`,e.carFerryTop=`car-ferry-top`,e.cargoFore=`cargo-fore`,e.cargoSide=`cargo-side`,e.cargoSideFaded=`cargo-side-faded`,e.cargoTop=`cargo-top`,e.cargoWindFore=`cargo-wind-fore`,e.cargoWindSide=`cargo-wind-side`,e.cargoWindSideFaded=`cargo-wind-side-faded`,e.cargoWindTop=`cargo-wind-top`,e.fishingVesselSide=`fishing-vessel-side`,e.fishingVesselSideFaded=`fishing-vessel-side-faded`,e.fishingVesselTop=`fishing-vessel-top`,e.genericSide=`generic-side`,e.genericSideFaded=`generic-side-faded`,e.genericTop=`generic-top`,e.psvAft=`psv-aft`,e.psvFore=`psv-fore`,e.psvSide=`psv-side`,e.psvSideFaded=`psv-side-faded`,e.psvTop=`psv-top`,e.sovSide=`sov-side`,e.sovSideFaded=`sov-side-faded`,e.sovTop=`sov-top`,e.tankerFore=`tanker-fore`,e.tankerSide=`tanker-side`,e.tankerSideFaded=`tanker-side-faded`,e.tankerTop=`tanker-top`,e.usvLargeSide=`usv-large-side`,e.usvLargeSideFaded=`usv-large-side-faded`,e.usvSmallSide=`usv-small-side`,e.usvSmallSideFaded=`usv-small-side-faded`,e.droneMediumFront=`drone-medium-front`,e.droneMediumStbdSide=`drone-medium-stbd-side`,e.droneMediumStbdSideFaded=`drone-medium-stbd-side-faded`,e.droneMediumTop=`drone-medium-top`,e.droneSmallFront=`drone-small-front`,e.droneSmallStbdSide=`drone-small-stbd-side`,e.droneSmallStbdSideFaded=`drone-small-stbd-side-faded`,e.droneSmallTop=`drone-small-top`,e.droneGenericFront=`drone-generic-front`,e.droneGenericSide=`drone-generic-side`,e.droneGenericSideFaded=`drone-generic-side-faded`,e.droneGenericTop=`drone-generic-top`,e.rovFront=`rov-front`,e.rovSide=`rov-side`,e.rovSideFaded=`rov-side-faded`,e.rovTop=`rov-top`,e}({}),To={"car-ferry-aft":da,"car-ferry-fore":fa,"car-ferry-side":ma,"car-ferry-side-faded":ha,"car-ferry-top":ga,"cargo-fore":_a,"cargo-side":ya,"cargo-side-faded":ba,"cargo-top":xa,"cargo-wind-fore":Sa,"cargo-wind-side":wa,"cargo-wind-side-faded":Ta,"cargo-wind-top":Ea,"fishing-vessel-side":Oa,"fishing-vessel-side-faded":ka,"fishing-vessel-top":Aa,"generic-side":Ma,"generic-side-faded":Na,"generic-top":Pa,"psv-aft":Fa,"psv-fore":Ia,"psv-side":Ra,"psv-side-faded":za,"psv-top":Ba,"sov-side":Ha,"sov-side-faded":Ua,"sov-top":Wa,"tanker-fore":Ga,"tanker-side":qa,"tanker-side-faded":Ja,"tanker-top":Ya,"usv-large-side":Za,"usv-large-side-faded":Qa,"usv-small-side":eo,"usv-small-side-faded":to,"drone-medium-front":no,"drone-medium-stbd-side":io,"drone-medium-stbd-side-faded":ao,"drone-medium-top":oo,"drone-small-front":so,"drone-small-stbd-side":lo,"drone-small-stbd-side-faded":uo,"drone-small-top":fo,"drone-generic-front":po,"drone-generic-side":ho,"drone-generic-side-faded":go,"drone-generic-top":_o,"rov-front":vo,"rov-side":bo,"rov-side-faded":xo,"rov-top":So},G=function(e){return e.zeroLineThick=`zeroLineThick`,e.zeroLine=`zeroLine`,e.main=`main`,e.primary=`primary`,e.secondary=`secondary`,e.tertiary=`tertiary`,e.textOnly=`textOnly`,e}({}),Eo=function(e){return e.regular=`regular`,e.enhanced=`enhanced`,e}({});function Do(e,t){return e===`regular`?`var(--instrument-tick-mark-tertiary-color)`:t===`tertiary`?`var(--instrument-tick-mark-secondary-color)`:`var(--instrument-tick-mark-primary-color)`}function Oo(e,{size:t,style:n,scale:r,text:i,inside:a,textRadius:o,rotation:s,maxDigits:c,color:l,radiusOffset:u=0,endLabelsMaxMin:d=!1}){let f=Number.isFinite(r)&&r>0?r:1,p=u,m,h;o+=(3/f+3)*(a?-1:1);let g=lt(e);if(t===`primary`)m=164+p,h=184+p;else if(t===`secondary`)m=164+p,h=172+p;else if(t===`main`||t===`zeroLine`)m=160+p,h=184+p;else if(t===`zeroLineThick`)m=112+p,h=184+p;else if(t===`tertiary`)m=164+p,h=168+p;else return[ko(i??``,{angle:e,inside:a,scale:f,textRadius:o,endLabelsMaxMin:d})];if(a){let e=184+p,t=160+p,n=h-m;h=e-Math.max(0,m-t),m=h-n}let _=l??Do(n,t),v=k`<line x1=${Math.sin(g)*m} y1=${-Math.cos(g)*m} x2=${Math.sin(g)*h} y2=${-Math.cos(g)*h} stroke=${_} stroke-width=${t===`zeroLine`||t===`zeroLineThick`?4:1} vector-effect="non-scaling-stroke"/>`;if(i){if(s===void 0)return[v,ko(i,{angle:e,inside:a,scale:f,textRadius:o,endLabelsMaxMin:d})];{let e=o+(4/f+5)*(a?-1:1)*c/2,t=Math.sin(g)*e,n=-Math.cos(g)*e;return[v,k`<text x=${t} y=${n} class="label rotate ${a?`inside`:``}" transform="rotate(${-s})" transform-origin="${t} ${n}">${i}</text>`]}}return v}function ko(e,{angle:t,inside:n,scale:r,textRadius:i,endLabelsMaxMin:a=!1}){let o=lt(t);if(a&&Math.abs(Math.cos(o))<1e-6)return k`<text x=${Math.sin(o)*(i-(n?(6+(e.length-1)*2.5)/r:14/r))} y=${n?-(6/r):12/r} class="label bottom ${n?`inside`:``}">${e}</text>`;let s;s=t===0?`top`:t<180&&t>0?`right`:t===180?`bottom`:`left`;let c=lt(t),l=n?-1:1,u=7/r*l,d=6/r*l,f=Math.sin(c)*(i+d);t>180?f+=4/r*l:t<180&&t>0&&(f-=4/r*l);let p=-Math.cos(c)*(i+u);return k`<text x=${f} y=${p} class="label ${s} ${n?`inside`:``}">${e}</text>`}var Ao=function(e){return e.advice=`advice`,e.caution=`caution`,e}({}),jo=function(e){return e.regular=`regular`,e.hinted=`hinted`,e.triggered=`triggered`,e}({}),Mo=Math.atan2(16,336);function No(e,t,n,r,i=0){let a=lt(ct(t-e));if(a<=Mo*2)return A;let o=+(a-Mo*2>Math.PI),s=lt(e)+Mo,c=lt(t)-Mo,l=164+i,u=172+i,d=(u-l)/2,f=Math.sin(s)*l,p=-Math.cos(s)*l,m=Math.sin(s)*u,h=-Math.cos(s)*u;return k`<path d=${`M ${f} ${p} 
                    A ${l} ${l} 0 ${o} 1 ${Math.sin(c)*l} ${-Math.cos(c)*l}
                    A ${d} ${d} 0 0 0 ${Math.sin(c)*u} ${-Math.cos(c)*u}
                    A ${u} ${u} 0 ${o} 0 ${m} ${h}
                    A ${d} ${d} 0 0 0 ${f} ${p}
                    Z`} fill=${n} stroke=${r} stroke-width="1" vector-effect="non-scaling-stroke" />`}function Po(e,t=0){if(e.type===`caution`){let n,r=null;e.state===`hinted`?n=`var(--instrument-frame-tertiary-color)`:e.state===`regular`?n=`var(--instrument-tick-mark-tertiary-color)`:(n=`var(--on-caution-active-color)`,r=`var(--alert-caution-color)`);let i=[];if(t>0){let e=164+t,r=172+t,a=(e+r)/2,o=2*Math.PI*168/90,s=Math.round(2*Math.PI*a/o),c=e-12,l=r+12,u=Math.tan(.705)*(l-c)/(2*a);for(let e=0;e<s;e++){let t=e*2*Math.PI/s,r=c*Math.sin(t-u),a=-c*Math.cos(t-u),o=l*Math.sin(t+u),d=-l*Math.cos(t+u);i.push(k`<line x1=${r} y1=${a} x2=${o} y2=${d} stroke=${n} stroke-width="4"/>`)}}else for(let e=0;e<180;e+=4)i.push(k`<g transform="rotate(${e}) translate(-256 -256) ">
            <path d="M369.167 64.7317L144 194.732L142 191.268L367.167 61.2676L369.167 64.7317ZM369.167 320.732L144 450.732L142 447.267L367.167 317.267L369.167 320.732Z" fill=${n}/>
            </g>
            `);let a=`adviceMask-${e.minAngle}-${e.maxAngle}`,o=Eo.regular;e.state===`regular`?o=Eo.regular:e.state===`triggered`&&(o=Eo.enhanced);let s=t>0?`none`:`black`,c=No(e.minAngle,e.maxAngle,`white`,s,t),l=No(e.minAngle,e.maxAngle,`none`,n,t),u,d;if(t>0){let e=172+t+32;u=k`<mask id=${a} maskUnits="userSpaceOnUse" x="${-e}" y="${-e}" width="${e*2}" height="${e*2}">${c}</mask>`,d=r?k`<rect x="${-e}" y="${-e}" width="${e*2}" height="${e*2}" fill="${r}"/>`:A}else u=k`<mask id=${a}>${c}</mask>`,d=r?k`<rect x="-256" y="-256" width="512" height="512" fill="${r}"/>`:A;return k`
            ${u}
            <g mask="url(#${a})">
                ${d}
                ${i}
            </g>
            ${l}
            ${e.hideMinTickmark?A:Oo(e.minAngle,{size:G.primary,style:o,scale:1,inside:!1,textRadius:0,maxDigits:0,radiusOffset:t})}
            ${e.hideMaxTickmark?A:Oo(e.maxAngle,{size:G.primary,style:o,scale:1,inside:!1,textRadius:0,maxDigits:0,radiusOffset:t})}
        `}{let n,r;return e.state===`hinted`?(n=`var(--instrument-frame-tertiary-color)`,r=Eo.regular):e.state===`regular`?(n=`var(--instrument-regular-secondary-color)`,r=Eo.regular):(n=`var(--instrument-enhanced-secondary-color)`,r=Eo.regular),k`
            ${No(e.minAngle,e.maxAngle,e.state===`triggered`?n:`none`,n,t)}
            ${Oo(e.minAngle,{size:G.primary,style:r,scale:1,inside:!1,textRadius:0,maxDigits:0,radiusOffset:t})}
            ${Oo(e.maxAngle,{size:G.primary,style:r,scale:1,inside:!1,textRadius:0,maxDigits:0,radiusOffset:t})}
        `}}var Fo=function(e){return e.dots=`dots`,e.bar=`bar`,e}({}),Io=function(e){return e.scale=`scale`,e.innerCircle=`innerCircle`,e}({}),Lo=5,Ro=Array.from({length:Lo},(e,t)=>360/Lo*t),zo=172,Bo=100,Vo=8,Ho=4,Uo=.05;function Wo(e,t=0){return(e===`scale`?zo:Bo)+t}function Go(e,t){let n=lt(e);return{cx:Math.sin(n)*t,cy:-Math.cos(n)*t}}function Ko(e,t,n=0){let r=Wo(t,n);return k`${Ro.map(t=>{let{cx:n,cy:i}=Go(t,r);return k`<circle cx="${n}" cy="${i}" r="${Vo}" fill="${e}" />`})}`}function qo(e,t,n){let r=n+8,i=n-8,a=lt(e),o=lt(t),s=Math.sin(a)*r,c=-Math.cos(a)*r,l=Math.sin(a)*i,u=-Math.cos(a)*i,d=Math.sin(o)*r,f=-Math.cos(o)*r,p=Math.sin(o)*i,m=-Math.cos(o)*i,h=((o-a)%(2*Math.PI)+2*Math.PI)%(2*Math.PI),g,_;return h<=Math.PI?(g=1,_=0):(g=0,_=1),[`M ${s} ${c}`,`A ${r} ${r} 0 0 ${g} ${d} ${f}`,`A 8 8 0 0 ${g} ${p} ${m}`,`A ${i} ${i} 0 0 ${_} ${l} ${u}`,`Z`].join(` `)}function Jo(e,t){let n=ct(t-e);return n<=180?n:360-n}function Yo(e,t=0){return ut(8/Wo(e,t))}function Xo(e,t,n,r=0){return k`
    <g transform="rotate(${t})">
      <rect
        x="${-4}"
        y="${-Wo(n,r)-8}"
        width="${8}"
        height="${16}"
        rx="${4}"
        fill="${e}"
      />
    </g>
  `}function Zo(e){let{startAngle:t,endAngle:n,barColor:r,position:i,maskId:a=`rot-bar-mask`,radiusOffset:o=0}=e;if(Jo(t,n)<Yo(i,o))return k``;let s=qo(t,n,Wo(i,o));return k`
    <defs>
      <clipPath id="${a}">
        <path d="${s}" />
      </clipPath>
    </defs>
    <path d="${s}" fill="${r}" />
  `}function Qo(e,t,n=0){let r=Wo(t,n);return k`
    ${Ro.map(t=>{let{cx:n,cy:i}=Go(t,r);return k`<circle cx="${n}" cy="${i}" r="${Ho}" fill="${e}" />`})}
  `}360/Lo;function $o(e,t){return t.strokePosition===`center`?k`<circle id=${e} cx="0" cy="0" 
      r=${t.radius} vector-effect="non-scaling-stroke" 
      stroke=${t.strokeColor}  stroke-width=${t.strokeWidth} 
      fill=${t.fillColor}>`:t.strokePosition===`inside`?k`
		<defs>
			<clipPath id="clip${e}">
				<circle id=${e} cx="0" cy="0" r=${t.radius} vector-effect="non-scaling-stroke" />
			</clipPath>
		</defs>
		<g>
			<circle id=${e} cx="0" cy="0" r=${t.radius} vector-effect="non-scaling-stroke" stroke=${t.strokeColor}  stroke-width=${t.strokeWidth*2} fill=${t.fillColor} clip-path="url(#clip${e})"/>
		</g>
  `:k`
		<circle id=${e} cx="0" cy="0" r=${t.radius} vector-effect="non-scaling-stroke" stroke=${t.strokeColor} stroke-width=${t.strokeWidth*2} fill=${t.fillColor}/>
		  `}function es(e,t=1){return e-t}function ts(e,t,n,r,i=1){let a=es(r,i),o=n-t;return(-e+t)*a/o+a/2+i/2}function ns(e,t,n,r,i=1){let a=es(r,i),o=n-t;return(e-t)*a/o+i/2}function rs(e,t,n,r,i=1){let a=i/2,o=e,s=t;return e===n&&(o=e+a,s=t-a),e+t===r&&(s-=a),{x:o,width:s}}function is(e,t,n,r,i=1){let a=i/2,o=e,s=t;return e===n&&(o=e+a,s=t-a),e+t===r&&(s-=a),{y:o,height:s}}function as(e,t){let{defaultDeadband:n=2,defaultZeroDeadband:r=.5,angularWraparound:i=!1}=t??{};class a extends e{constructor(...e){super(...e),this.atSetpoint=!1,this.touching=!1,this.autoAtSetpoint=!0,this.autoAtSetpointDeadband=n,this.setpointAtZeroDeadband=r,this.setpointOverride=!1,this.animateSetpoint=!1}get departingNewSetpoint(){return this._departingNewSetpoint}setpointPresenceChanged(e){return e.has(`setpoint`)||e.has(`newSetpoint`)||e.has(`_departingNewSetpoint`)}computeAtSetpoint(e){return Fi({value:e,setpoint:this.setpoint,touching:this.touching,auto:this.autoAtSetpoint,deadband:this.autoAtSetpointDeadband,atSetpointManual:this.atSetpoint,angularWraparound:i})}willUpdate(e){if(super.willUpdate(e),e.has(`newSetpoint`)&&this.animateSetpoint){let t=e.get(`newSetpoint`);if(t!==void 0&&this.newSetpoint===void 0){this._departingNewSetpoint=t,clearTimeout(this._animationTimer);let e=Ti(this);this._animationTimer=setTimeout(()=>{this._departingNewSetpoint=void 0},e)}}}disconnectedCallback(){super.disconnectedCallback(),clearTimeout(this._animationTimer)}}return N([P({type:Number})],a.prototype,`setpoint`,void 0),N([P({type:Number})],a.prototype,`newSetpoint`,void 0),N([P({type:Boolean,attribute:!1})],a.prototype,`atSetpoint`,void 0),N([P({type:Boolean})],a.prototype,`touching`,void 0),N([P({type:Boolean,attribute:!1})],a.prototype,`autoAtSetpoint`,void 0),N([P({type:Number})],a.prototype,`autoAtSetpointDeadband`,void 0),N([P({type:Number})],a.prototype,`setpointAtZeroDeadband`,void 0),N([P({type:Boolean})],a.prototype,`setpointOverride`,void 0),N([P({type:Boolean})],a.prototype,`animateSetpoint`,void 0),N([ze()],a.prototype,`_departingNewSetpoint`,void 0),a}function os({x:e,y:t,width:n,height:r,radii:i}){let a=Math.min(n,r)/2,[o,s,c,l]=i.map(e=>st(e,0,Math.max(0,a))),u=e+n,d=t+r,f=(e,t,n)=>e>0?`A${e} ${e} 0 0 1 ${t} ${n}`:``;return[`M${e+o} ${t}`,`H${u-s}`,f(s,u,t+s),`V${d-c}`,f(c,u-c,d),`H${e+l}`,f(l,e,d-l),`V${t+o}`,f(o,e+o,t),`Z`].filter(Boolean).join(` `)}function ss({startAngle:e,endAngle:t,r:n,R:r,roundOutsideCut:i,roundInsideCut:a,roundRadius:o=8}){let s=lt(e),c=lt(t),l=Math.sin(s)*r,u=-Math.cos(s)*r,d=Math.sin(s)*n,f=-Math.cos(s)*n,p=Math.sin(c)*r,m=-Math.cos(c)*r,h=Math.sin(c)*n,g=-Math.cos(c)*n,_=i&&r>=o,v=a&&n>=o,y=``;if(_){let e=Math.asin(o/r),t=c-e-(s+e)<=Math.PI?0:1,n=Math.sin(s)*(r-o),i=-Math.cos(s)*(r-o),a=Math.sin(s+e)*r,l=-Math.cos(s+e)*r,u=Math.sin(c)*(r-o),d=-Math.cos(c)*(r-o),f=Math.sin(c-e)*r,p=-Math.cos(c-e)*r;y+=`M ${n} ${i} A ${o} ${o} 1 0 1 ${a} ${l}`,y+=`A ${r} ${r} 1 ${t} 1 ${f} ${p}`,y+=`A ${o} ${o} 1 0 1 ${u} ${d}`}else{let e=Math.abs(c-s)<=Math.PI?0:1;y+=`M ${l} ${u} A ${r} ${r} 1 ${e} 1 ${p} ${m}`}if(v){let e=Math.asin(o/n),t=c-e-(s+e)<=Math.PI?0:1,r=Math.sin(s)*(n+o),i=-Math.cos(s)*(n+o),a=Math.sin(s+e)*n,l=-Math.cos(s+e)*n,u=Math.sin(c)*(n+o),d=-Math.cos(c)*(n+o),f=Math.sin(c-e)*n,p=-Math.cos(c-e)*n;y+=`L ${u} ${d} A ${o} ${o} 1 0 1 ${f} ${p}`,y+=`A ${n} ${n} 1 ${t} 0 ${a} ${l}`,y+=`A ${o} ${o} 1 0 1 ${r} ${i}`}else{let e=c-s<=Math.PI?0:1;y+=`L ${h} ${g} A ${n} ${n} 1 ${e} 0 ${d} ${f}`}return y+=`Z`,y}var cs=o`* {
  -webkit-tap-highlight-color: transparent;
}

* {
  box-sizing: border-box;
}

:host {
  overflow: hidden;
}

svg {
  display: block;
}

svg.cropped {
  /* A cropped frame paints its arc outside the viewBox before \`rotation\`
     swings it into view; the host's overflow rule is what clips. */
  overflow: visible;
}

.label {
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-body-font-weight);
  font-size: var(--global-typography-ui-body-font-size);
  line-height: var(--global-typography-ui-body-line-height);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  font-size: calc(12px / var(--scale, 1));
  fill: var(--element-neutral-color);
  dominant-baseline: central;
  text-anchor: middle;
}

.label.left {
    text-anchor: end;
  }

.label.right {
    text-anchor: start;
  }

.label.north-marker {
  fill: var(--element-active-inverted-color);
}

.label.inside.left {
    text-anchor: start;
  }

.label.inside.right {
    text-anchor: end;
  }
`,ls=class{constructor(e,t,n=1,r=0){this._rotationsPerMinute=1,this._cyclePx=0,this.host=e,this.el=t,this._rotationsPerMinute=n,this._cyclePx=r,this.host.addController(this)}set rotationsPerMinute(e){this._rotationsPerMinute!==e&&(this._rotationsPerMinute=e,this.updateAnimation())}get rotationsPerMinute(){return this._rotationsPerMinute}set cyclePx(e){this._cyclePx!==e&&(this._cyclePx=e,this.updateAnimation())}get cyclePx(){return this._cyclePx}get isTranslateMode(){return this._cyclePx>0}getKeyframes(){return this.isTranslateMode?[{transform:`translateX(0px)`},{transform:`translateX(${this._cyclePx}px)`}]:[{transform:`rotate(0deg)`},{transform:`rotate(360deg)`}]}hostConnected(){this.startAnimation()}startAnimation(){let e=Math.abs(this._rotationsPerMinute),t=e===0?1:6e4/e;this.animation=this.el.animate(this.getKeyframes(),{duration:t,iterations:1/0,direction:this._rotationsPerMinute>=0?`normal`:`reverse`}),this._rotationsPerMinute===0&&this.animation.pause()}updateAnimation(){if(!this.animation)return;let e=this.animation.effect.getComputedTiming(),t=e.duration,n=this.animation.currentTime??0,r=e.direction,i=n%t/t;this.animation.cancel();let a=Math.abs(this._rotationsPerMinute),o=a===0?1:6e4/a,s=this._rotationsPerMinute>=0?`normal`:`reverse`,c=r===s?i:1-i;this.animation=this.el.animate(this.getKeyframes(),{duration:o,iterations:1/0,direction:s}),this.animation.currentTime=c*o,this._rotationsPerMinute===0&&this.animation.pause()}destroy(){this.animation?.cancel(),this.animation=void 0}hostDisconnected(){this.destroy()}};function us(e,t){t&&(t.destroy(),e.removeController(t))}function ds(e){let{scale:t,inside:n,innerRadius:r,includeNorth:i,insideFlush:a}=e,o=a?r-8/t:r-8/t-8,s=e=>e*(n?o:184+8/t+8),c=[{label:`E`,x:s(1),y:0},{label:`S`,x:0,y:s(1)},{label:`W`,x:s(-1),y:0}];return(i||t<.58||n)&&c.push({label:`N`,x:0,y:s(-1)}),c}function fs(e,t){let n,r,i,a,o,s;return typeof e==`number`?(n=e,r=t,i=!1,a=184):(n=e.scale,r=e.rotation,i=e.inside??!1,a=e.innerRadius??184,o=e.includeNorth,s=e.insideFlush),k`
    ${ds({scale:n,inside:i,innerRadius:a,includeNorth:o,insideFlush:s}).map(e=>k`
        <text
          x="${e.x}"
          y="${e.y}"
          class="label"
          transform="rotate(${-(r??0)})"
          transform-origin="${e.x} ${e.y}"
        >
          ${e.label}
        </text>
      `)}
  `}var ps=`M212.597 22.5019C213.808 23.8852 212.665 26.0529 210.836 25.8748C204.639 25.2715 198.356 24.9628 192 24.9628C185.645 24.9628 179.362 25.2715 173.165 25.8748C171.336 26.0529 170.193 23.8852 171.404 22.502L190.495 0.68299C191.292 -0.227664 192.709 -0.227663 193.506 0.682991L212.597 22.5019Z`;function ms(e){let{scale:t,rotation:n}=e,r=-(184+8/t+8);return k`
    <g transform="translate(0, ${r}) scale(${.75/t}) translate(-192, -16.963)">
      <path d=${ps} fill="var(--instrument-tick-mark-secondary-color)"/>
    </g>
    <text
      x="0"
      y="${r}"
      class="label north-marker"
      transform="rotate(${-(n??0)})"
      transform-origin="0 ${r}"
    >
      N
    </text>
  `}function hs(e){let{scale:t,rotation:n,inside:r=!1}=e;return t<.58?r?k`
        <g transform="translate(0, ${-184})">
          <path fill-rule="evenodd" clip-rule="evenodd"
            d="M-17.8457 24.984 0 0 17.8458 24.984C11.9868 24.3338 6.0324 24 0 24-6.0323 24-11.9867 24.3338-17.8457 24.984Z"
            fill="var(--instrument-frame-tertiary-color)"/>
        </g>`:k`
        <defs>
          <mask id="circleMask">
            <rect x="-${184}" y="-${184}" width="${368}" height="${368}" fill="black"/>
            <circle cx="0" cy="0" r="${184}" fill="white"/>
          </mask>
        </defs>
        <g mask="url(#circleMask)" transform="translate(0, ${-184})">
          <path fill-rule="evenodd" clip-rule="evenodd"
            d="M-17.8457 24.984 0 0 17.8458 24.984C11.9868 24.3338 6.0324 24 0 24-6.0323 24-11.9867 24.3338-17.8457 24.984Z"
            fill="var(--instrument-frame-tertiary-color)"/>
        </g>`:r?k`
      <path transform="translate(-256, -256)" fill-rule="evenodd" clip-rule="evenodd"
        d="M238.152 96.9842L255.998 72L273.844 96.9839C267.985 96.3338 262.031 96 256 96C249.967 96 244.012 96.3339 238.152 96.9842Z"
        fill="var(--instrument-frame-tertiary-color)"/>
    `:k`
    <g transform="translate(0, ${(1/t-1)*188}) scale(${1/t})">
      <path transform="translate(-192, -224)"
        d="M 221.521 35.425 C 222.388 36.4644 222.821 36.9841 222.809 37.3627 C 222.8 37.6941 222.632 37.9916 222.354 38.1721 C 222.037 38.3783 221.361 38.2774 220.011 38.0756 A ${188*t} ${188*t} 0 0 0 163.989 38.0756 C 162.639 38.2774 161.964 38.3783 161.646 38.1721 C 161.368 37.9916 161.201 37.6941 161.191 37.3627 C 161.18 36.9841 161.613 36.4644 162.479 35.425 L 190.771 1.475 C 191.193 0.9685 191.404 0.7153 191.657 0.6229 C 191.879 0.5419 192.122 0.5419 192.343 0.6229 C 192.596 0.7153 192.807 0.9685 193.229 1.475 L 221.521 35.425 Z"
        fill="var(--instrument-tick-mark-secondary-color)"/>
    </g>

    <defs>
      <mask id="circleMask">
        <rect x="-${184}" y="-${184}" width="${368}" height="${368}" fill="black"/>
        <circle cx="0" cy="0" r="${184}" fill="white"/>
      </mask>
    </defs>
    <g mask="url(#circleMask)" transform="translate(0, ${-(184+10/t+30)}) scale(${.75/t}, ${.75/t}) rotate(${-(n??0)})" transform-origin="0 25">
      <path d="M5.003 29H2.091L-3.013 20.264H-3.077C-3.066 20.52-3.056 20.7813-3.045 21.048-3.034 21.3147-3.024 21.5867-3.013 21.864-2.992 22.1307-2.976 22.4027-2.965 22.68-2.954 22.9573-2.944 23.2347-2.933 23.512V29H-4.997V17.576H-2.101L2.987 26.232H3.035C3.024 25.9867 3.014 25.736 3.003 25.48 2.992 25.2133 2.982 24.952 2.971 24.696 2.971 24.4293 2.966 24.1627 2.955 23.896 2.944 23.6293 2.934 23.3627 2.923 23.096V17.576H5.003V29Z" fill="var(--element-active-inverted-color)"/>
    </g>
  `}var gs=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M18.5 12C18.5 8.41015 15.5899 5.5 12 5.5C8.41015 5.5 5.5 8.41015 5.5 12C5.5 15.5899 8.41015 18.5 12 18.5V20C7.58172 20 4 16.4183 4 12C4 7.58172 7.58172 4 12 4C16.4183 4 20 7.58172 20 12C20 16.4183 16.4183 20 12 20V18.5C15.5899 18.5 18.5 15.5899 18.5 12Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M18.5 12C18.5 8.41015 15.5899 5.5 12 5.5C8.41015 5.5 5.5 8.41015 5.5 12C5.5 15.5899 8.41015 18.5 12 18.5V20C7.58172 20 4 16.4183 4 12C4 7.58172 7.58172 4 12 4C16.4183 4 20 7.58172 20 12C20 16.4183 16.4183 20 12 20V18.5C15.5899 18.5 18.5 15.5899 18.5 12Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},_s=(gs.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,gs);N([P({type:Boolean})],_s.prototype,`useCssColor`,void 0),_s=N([M(`obi-wind-shaft-0`)],_s);var vs=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M12 1C12.5523 1 13 1.44772 13 2V24H11V2C11 1.44772 11.4477 1 12 1Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12 1C12.5523 1 13 1.44772 13 2V24H11V2C11 1.44772 11.4477 1 12 1Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},ys=(vs.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,vs);N([P({type:Boolean})],ys.prototype,`useCssColor`,void 0),ys=N([M(`obi-wind-shaft-1`)],ys);var bs=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},xs=(bs.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,bs);N([P({type:Boolean})],xs.prototype,`useCssColor`,void 0),xs=N([M(`obi-wind-shaft-10`)],xs);var Ss=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13V13.5615L19.8545 11.8486C20.9654 11.5709 20.9654 9.99158 19.8545 9.71385L13 8V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13V13.5615L19.8545 11.8486C20.9654 11.5709 20.9654 9.99158 19.8545 9.71385L13 8V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Cs=(Ss.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Ss);N([P({type:Boolean})],Cs.prototype,`useCssColor`,void 0),Cs=N([M(`obi-wind-shaft-100`)],Cs);var ws=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V5H16C16.5523 5 17 5.44772 17 6C17 6.55228 16.5523 7 16 7H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V5H16C16.5523 5 17 5.44772 17 6C17 6.55228 16.5523 7 16 7H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Ts=(ws.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,ws);N([P({type:Boolean})],Ts.prototype,`useCssColor`,void 0),Ts=N([M(`obi-wind-shaft-15`)],Ts);var Es=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V5H19C19.5523 5 20 5.44772 20 6C20 6.55228 19.5523 7 19 7H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V5H19C19.5523 5 20 5.44772 20 6C20 6.55228 19.5523 7 19 7H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Ds=(Es.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Es);N([P({type:Boolean})],Ds.prototype,`useCssColor`,void 0),Ds=N([M(`obi-wind-shaft-20`)],Ds);var Os=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V5H19C19.5523 5 20 5.44772 20 6C20 6.55228 19.5523 7 19 7H13V9H16C16.5523 9 17 9.44772 17 10C17 10.5523 16.5523 11 16 11H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V5H19C19.5523 5 20 5.44772 20 6C20 6.55228 19.5523 7 19 7H13V9H16C16.5523 9 17 9.44772 17 10C17 10.5523 16.5523 11 16 11H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},ks=(Os.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Os);N([P({type:Boolean})],ks.prototype,`useCssColor`,void 0),ks=N([M(`obi-wind-shaft-25`)],ks);var As=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V5H19C19.5523 5 20 5.44772 20 6C20 6.55228 19.5523 7 19 7H13V9H19C19.5523 9 20 9.44772 20 10C20 10.5523 19.5523 11 19 11H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V5H19C19.5523 5 20 5.44772 20 6C20 6.55228 19.5523 7 19 7H13V9H19C19.5523 9 20 9.44772 20 10C20 10.5523 19.5523 11 19 11H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},js=(As.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,As);N([P({type:Boolean})],js.prototype,`useCssColor`,void 0),js=N([M(`obi-wind-shaft-30`)],js);var Ms=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V5H19C19.5523 5 20 5.44772 20 6C20 6.55228 19.5523 7 19 7H13V9H19C19.5523 9 20 9.44772 20 10C20 10.5523 19.5523 11 19 11H13V13H16C16.5523 13 17 13.4477 17 14C17 14.5523 16.5523 15 16 15H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V5H19C19.5523 5 20 5.44772 20 6C20 6.55228 19.5523 7 19 7H13V9H19C19.5523 9 20 9.44772 20 10C20 10.5523 19.5523 11 19 11H13V13H16C16.5523 13 17 13.4477 17 14C17 14.5523 16.5523 15 16 15H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Ns=(Ms.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Ms);N([P({type:Boolean})],Ns.prototype,`useCssColor`,void 0),Ns=N([M(`obi-wind-shaft-35`)],Ns);var Ps=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V5H19C19.5523 5 20 5.44772 20 6C20 6.55228 19.5523 7 19 7H13V9H19C19.5523 9 20 9.44772 20 10C20 10.5523 19.5523 11 19 11H13V13H19C19.5523 13 20 13.4477 20 14C20 14.5523 19.5523 15 19 15H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V5H19C19.5523 5 20 5.44772 20 6C20 6.55228 19.5523 7 19 7H13V9H19C19.5523 9 20 9.44772 20 10C20 10.5523 19.5523 11 19 11H13V13H19C19.5523 13 20 13.4477 20 14C20 14.5523 19.5523 15 19 15H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Fs=(Ps.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Ps);N([P({type:Boolean})],Fs.prototype,`useCssColor`,void 0),Fs=N([M(`obi-wind-shaft-40`)],Fs);var Is=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V5H19C19.5523 5 20 5.44772 20 6C20 6.55228 19.5523 7 19 7H13V9H19C19.5523 9 20 9.44772 20 10C20 10.5523 19.5523 11 19 11H13V13H19C19.5523 13 20 13.4477 20 14C20 14.5523 19.5523 15 19 15H13V17H16C16.5523 17 17 17.4477 17 18C17 18.5523 16.5523 19 16 19H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M19 1C19.5523 1 20 1.44772 20 2C20 2.55228 19.5523 3 19 3H13V5H19C19.5523 5 20 5.44772 20 6C20 6.55228 19.5523 7 19 7H13V9H19C19.5523 9 20 9.44772 20 10C20 10.5523 19.5523 11 19 11H13V13H19C19.5523 13 20 13.4477 20 14C20 14.5523 19.5523 15 19 15H13V17H16C16.5523 17 17 17.4477 17 18C17 18.5523 16.5523 19 16 19H13V24H11V2.09961C11.0002 1.4924 11.4924 1.00021 12.0996 1H19Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Ls=(Is.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Is);N([P({type:Boolean})],Ls.prototype,`useCssColor`,void 0),Ls=N([M(`obi-wind-shaft-45`)],Ls);var Rs=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M12 1C12.5523 1 13 1.44772 13 2V5H16C16.5523 5 17 5.44772 17 6C17 6.55228 16.5523 7 16 7H13V24H11V2C11 1.44772 11.4477 1 12 1Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12 1C12.5523 1 13 1.44772 13 2V5H16C16.5523 5 17 5.44772 17 6C17 6.55228 16.5523 7 16 7H13V24H11V2C11 1.44772 11.4477 1 12 1Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},zs=(Rs.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Rs);N([P({type:Boolean})],zs.prototype,`useCssColor`,void 0),zs=N([M(`obi-wind-shaft-5`)],zs);var Bs=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M12.2373 1.03603L12.3672 1.06044L19.8545 2.93251C20.9654 3.21025 20.9654 4.78954 19.8545 5.06728L13 6.78017V23.9999H11V2.12783C11.0001 1.45694 11.5913 0.953184 12.2373 1.03603Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.2373 1.03603L12.3672 1.06044L19.8545 2.93251C20.9654 3.21025 20.9654 4.78954 19.8545 5.06728L13 6.78017V23.9999H11V2.12783C11.0001 1.45694 11.5913 0.953184 12.2373 1.03603Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Vs=(Bs.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Bs);N([P({type:Boolean})],Vs.prototype,`useCssColor`,void 0),Vs=N([M(`obi-wind-shaft-50`)],Vs);var Hs=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.06044L12.2373 1.03603C11.5913 0.953184 11.0001 1.45694 11 2.12783V23.9999H13V10H16C16.5523 10 17 9.55228 17 9C17 8.44771 16.5523 8 16 8H13V6.78017L19.8545 5.06728C20.9654 4.78954 20.9654 3.21025 19.8545 2.93251L12.3672 1.06044Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.06044L12.2373 1.03603C11.5913 0.953184 11.0001 1.45694 11 2.12783V23.9999H13V10H16C16.5523 10 17 9.55228 17 9C17 8.44771 16.5523 8 16 8H13V6.78017L19.8545 5.06728C20.9654 4.78954 20.9654 3.21025 19.8545 2.93251L12.3672 1.06044Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Us=(Hs.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Hs);N([P({type:Boolean})],Us.prototype,`useCssColor`,void 0),Us=N([M(`obi-wind-shaft-55`)],Us);var Ws=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M12.2373 1.03603L12.3672 1.06044L19.8545 2.93251C20.9654 3.21025 20.9654 4.78954 19.8545 5.06728L13 6.78017V8H19C19.5523 8 20 8.44773 20 9C20 9.55228 19.5523 10 19 10H13V23.9999H11V2.12783C11.0001 1.45694 11.5913 0.953184 12.2373 1.03603Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.2373 1.03603L12.3672 1.06044L19.8545 2.93251C20.9654 3.21025 20.9654 4.78954 19.8545 5.06728L13 6.78017V8H19C19.5523 8 20 8.44773 20 9C20 9.55228 19.5523 10 19 10H13V23.9999H11V2.12783C11.0001 1.45694 11.5913 0.953184 12.2373 1.03603Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Gs=(Ws.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Ws);N([P({type:Boolean})],Gs.prototype,`useCssColor`,void 0),Gs=N([M(`obi-wind-shaft-60`)],Gs);var Ks=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13V13.5H16C16.5523 13.5 17 13.0523 17 12.5C17 11.9477 16.5523 11.5 16 11.5H13V10H19C19.5523 10 20 9.55228 20 9C20 8.44773 19.5523 8 19 8H13V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13V13.5H16C16.5523 13.5 17 13.0523 17 12.5C17 11.9477 16.5523 11.5 16 11.5H13V10H19C19.5523 10 20 9.55228 20 9C20 8.44773 19.5523 8 19 8H13V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},qs=(Ks.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Ks);N([P({type:Boolean})],qs.prototype,`useCssColor`,void 0),qs=N([M(`obi-wind-shaft-65`)],qs);var Js=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13V13.5H19C19.5523 13.5 20 13.0523 20 12.5C20 11.9477 19.5523 11.5 19 11.5H13V10H19C19.5523 10 20 9.55229 20 9C20 8.44773 19.5523 8 19 8H13V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13V13.5H19C19.5523 13.5 20 13.0523 20 12.5C20 11.9477 19.5523 11.5 19 11.5H13V10H19C19.5523 10 20 9.55229 20 9C20 8.44773 19.5523 8 19 8H13V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Ys=(Js.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Js);N([P({type:Boolean})],Ys.prototype,`useCssColor`,void 0),Ys=N([M(`obi-wind-shaft-70`)],Ys);var Xs=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13V17H16C16.5523 17 17 16.5523 17 16C17 15.4477 16.5523 15 16 15H13V13.5H19C19.5523 13.5 20 13.0523 20 12.5C20 11.9477 19.5523 11.5 19 11.5H13V10H19C19.5523 10 20 9.55229 20 9C20 8.44773 19.5523 8 19 8H13V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13V17H16C16.5523 17 17 16.5523 17 16C17 15.4477 16.5523 15 16 15H13V13.5H19C19.5523 13.5 20 13.0523 20 12.5C20 11.9477 19.5523 11.5 19 11.5H13V10H19C19.5523 10 20 9.55229 20 9C20 8.44773 19.5523 8 19 8H13V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Zs=(Xs.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Xs);N([P({type:Boolean})],Zs.prototype,`useCssColor`,void 0),Zs=N([M(`obi-wind-shaft-75`)],Zs);var Qs=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13V17H19C19.5523 17 20 16.5523 20 16C20 15.4477 19.5523 15 19 15H13V13.5H19C19.5523 13.5 20 13.0523 20 12.5C20 11.9477 19.5523 11.5 19 11.5H13V10H19C19.5523 10 20 9.55229 20 9C20 8.44773 19.5523 8 19 8H13V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13V17H19C19.5523 17 20 16.5523 20 16C20 15.4477 19.5523 15 19 15H13V13.5H19C19.5523 13.5 20 13.0523 20 12.5C20 11.9477 19.5523 11.5 19 11.5H13V10H19C19.5523 10 20 9.55229 20 9C20 8.44773 19.5523 8 19 8H13V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},$s=(Qs.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Qs);N([P({type:Boolean})],$s.prototype,`useCssColor`,void 0),$s=N([M(`obi-wind-shaft-80`)],$s);var ec=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13V20.5H16C16.5523 20.5 17 20.0523 17 19.5C17 18.9477 16.5523 18.5 16 18.5H13V17H19C19.5523 17 20 16.5523 20 16C20 15.4477 19.5523 15 19 15H13V13.5H19C19.5523 13.5 20 13.0523 20 12.5C20 11.9477 19.5523 11.5 19 11.5H13V10H19C19.5523 10 20 9.55229 20 9C20 8.44773 19.5523 8 19 8H13V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13V20.5H16C16.5523 20.5 17 20.0523 17 19.5C17 18.9477 16.5523 18.5 16 18.5H13V17H19C19.5523 17 20 16.5523 20 16C20 15.4477 19.5523 15 19 15H13V13.5H19C19.5523 13.5 20 13.0523 20 12.5C20 11.9477 19.5523 11.5 19 11.5H13V10H19C19.5523 10 20 9.55229 20 9C20 8.44773 19.5523 8 19 8H13V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},tc=(ec.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,ec);N([P({type:Boolean})],tc.prototype,`useCssColor`,void 0),tc=N([M(`obi-wind-shaft-85`)],tc);var nc=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13V20.5H19C19.5523 20.5 20 20.0523 20 19.5C20 18.9477 19.5523 18.5 19 18.5H13V17H19C19.5523 17 20 16.5523 20 16C20 15.4477 19.5523 15 19 15H13V13.5H19C19.5523 13.5 20 13.0523 20 12.5C20 11.9477 19.5523 11.5 19 11.5H13V10H19C19.5523 10 20 9.55229 20 9C20 8.44773 19.5523 8 19 8H13V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13V20.5H19C19.5523 20.5 20 20.0523 20 19.5C20 18.9477 19.5523 18.5 19 18.5H13V17H19C19.5523 17 20 16.5523 20 16C20 15.4477 19.5523 15 19 15H13V13.5H19C19.5523 13.5 20 13.0523 20 12.5C20 11.9477 19.5523 11.5 19 11.5H13V10H19C19.5523 10 20 9.55229 20 9C20 8.44773 19.5523 8 19 8H13V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},rc=(nc.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,nc);N([P({type:Boolean})],rc.prototype,`useCssColor`,void 0),rc=N([M(`obi-wind-shaft-90`)],rc);var ic=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13H16C16.5523 23.9997 17 23.5519 17 22.9997C17 22.4474 16.5523 21.9997 16 21.9997H13V20.5H19C19.5523 20.5 20 20.0523 20 19.5C20 18.9477 19.5523 18.5 19 18.5H13V17H19C19.5523 17 20 16.5523 20 16C20 15.4477 19.5523 15 19 15H13V13.5H19C19.5523 13.5 20 13.0523 20 12.5C20 11.9477 19.5523 11.5 19 11.5H13V10H19C19.5523 10 20 9.55229 20 9C20 8.44773 19.5523 8 19 8H13V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.3672 1.0602L12.2373 1.03578C11.5913 0.95294 11.0001 1.45669 11 2.12758V23.9997H13H16C16.5523 23.9997 17 23.5519 17 22.9997C17 22.4474 16.5523 21.9997 16 21.9997H13V20.5H19C19.5523 20.5 20 20.0523 20 19.5C20 18.9477 19.5523 18.5 19 18.5H13V17H19C19.5523 17 20 16.5523 20 16C20 15.4477 19.5523 15 19 15H13V13.5H19C19.5523 13.5 20 13.0523 20 12.5C20 11.9477 19.5523 11.5 19 11.5H13V10H19C19.5523 10 20 9.55229 20 9C20 8.44773 19.5523 8 19 8H13V6.77992L19.8545 5.06703C20.9654 4.78929 20.9654 3.21 19.8545 2.93227L12.3672 1.0602Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},ac=(ic.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,ic);N([P({type:Boolean})],ac.prototype,`useCssColor`,void 0),ac=N([M(`obi-wind-shaft-95`)],ac);var oc=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C16.4183 4 20 7.58172 20 12C20 16.4183 16.4183 20 12 20C7.58172 20 4 16.4183 4 12C4 7.58172 7.58172 4 12 4ZM12 6C8.68629 6 6 8.68629 6 12C6 15.3137 8.68629 18 12 18C15.3137 18 18 15.3137 18 12C18 8.68629 15.3137 6 12 6Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C16.4183 4 20 7.58172 20 12C20 16.4183 16.4183 20 12 20C7.58172 20 4 16.4183 4 12C4 7.58172 7.58172 4 12 4ZM12 6C8.68629 6 6 8.68629 6 12C6 15.3137 8.68629 18 12 18C15.3137 18 18 15.3137 18 12C18 8.68629 15.3137 6 12 6Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},sc=(oc.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,oc);N([P({type:Boolean})],sc.prototype,`useCssColor`,void 0),sc=N([M(`obi-wind-true-0`)],sc);var cc=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M11.9997 0C12.552 0 12.9997 0.447715 12.9997 1V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M11.9997 0C12.552 0 12.9997 0.447715 12.9997 1V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},lc=(cc.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,cc);N([P({type:Boolean})],lc.prototype,`useCssColor`,void 0),lc=N([M(`obi-wind-true-1`)],lc);var uc=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M18.9997 0C19.552 0 19.9997 0.447715 19.9997 1C19.9997 1.55228 19.552 2 18.9997 2H12.9997V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0H18.9997Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M18.9997 0C19.552 0 19.9997 0.447715 19.9997 1C19.9997 1.55228 19.552 2 18.9997 2H12.9997V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0H18.9997Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},dc=(uc.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,uc);N([P({type:Boolean})],dc.prototype,`useCssColor`,void 0),dc=N([M(`obi-wind-true-10`)],dc);var fc=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.1969 0.0200342L12.0816 0.00343268C11.508 -0.0441781 10.9997 0.4093 10.9996 1.00148V15.0005H9.00156C8.25783 15.0008 7.77356 15.7833 8.10605 16.4487L11.1041 22.4458C11.473 23.1833 12.526 23.1831 12.8951 22.4458L15.8932 16.4487C16.2259 15.7828 15.7412 15.0005 14.9977 15.0005H12.9996L13 10.6392L19.6914 9.30135C20.764 9.08662 20.764 7.55318 19.6914 7.33846L12.9996 6.0005V4.81984L19.691 3.48195C20.7637 3.26722 20.7637 1.73378 19.691 1.51906L12.1969 0.0200342Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.1969 0.0200342L12.0816 0.00343268C11.508 -0.0441781 10.9997 0.4093 10.9996 1.00148V15.0005H9.00156C8.25783 15.0008 7.77356 15.7833 8.10605 16.4487L11.1041 22.4458C11.473 23.1833 12.526 23.1831 12.8951 22.4458L15.8932 16.4487C16.2259 15.7828 15.7412 15.0005 14.9977 15.0005H12.9996L13 10.6392L19.6914 9.30135C20.764 9.08662 20.764 7.55318 19.6914 7.33846L12.9996 6.0005V4.81984L19.691 3.48195C20.7637 3.26722 20.7637 1.73378 19.691 1.51906L12.1969 0.0200342Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},pc=(fc.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,fc);N([P({type:Boolean})],pc.prototype,`useCssColor`,void 0),pc=N([M(`obi-wind-true-100`)],pc);var mc=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M18.9997 0C19.552 0 19.9997 0.447715 19.9997 1C19.9997 1.55228 19.552 2 18.9997 2H12.9997V3.5H15.9997C16.552 3.5 16.9997 3.94772 16.9997 4.5C16.9997 5.05228 16.552 5.5 15.9997 5.5H12.9997V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0H18.9997Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M18.9997 0C19.552 0 19.9997 0.447715 19.9997 1C19.9997 1.55228 19.552 2 18.9997 2H12.9997V3.5H15.9997C16.552 3.5 16.9997 3.94772 16.9997 4.5C16.9997 5.05228 16.552 5.5 15.9997 5.5H12.9997V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0H18.9997Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},hc=(mc.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,mc);N([P({type:Boolean})],hc.prototype,`useCssColor`,void 0),hc=N([M(`obi-wind-true-15`)],hc);var gc=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M18.9997 0C19.552 0 19.9997 0.447715 19.9997 1C19.9997 1.55228 19.552 2 18.9997 2H12.9997V3.5H18.9997C19.552 3.5 19.9997 3.94772 19.9997 4.5C19.9997 5.05228 19.552 5.5 18.9997 5.5H12.9997V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0H18.9997Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M18.9997 0C19.552 0 19.9997 0.447715 19.9997 1C19.9997 1.55228 19.552 2 18.9997 2H12.9997V3.5H18.9997C19.552 3.5 19.9997 3.94772 19.9997 4.5C19.9997 5.05228 19.552 5.5 18.9997 5.5H12.9997V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0H18.9997Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},_c=(gc.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,gc);N([P({type:Boolean})],_c.prototype,`useCssColor`,void 0),_c=N([M(`obi-wind-true-20`)],_c);var vc=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="25" viewBox="0 0 24 25" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M19.0301 0C19.5824 0 20.0301 0.447715 20.0301 1C20.0301 1.55228 19.5824 2 19.0301 2H13.0301V3.5H19.0301C19.5824 3.5 20.0301 3.94772 20.0301 4.5C20.0301 5.05228 19.5824 5.5 19.0301 5.5H13.0301V7H16.0301C16.5824 7 17.0301 7.44772 17.0301 8C17.0301 8.55228 16.5824 9 16.0301 9H13.0301V15H15.0281C15.7716 15 16.2564 15.7823 15.9236 16.4482L12.9256 22.4453L12.9246 22.4443C12.5789 23.1367 11.6327 23.1802 11.2117 22.5752L11.1346 22.4453L8.13652 16.4482C7.80454 15.7833 8.28773 15.0002 9.03203 15H11.0301V1C11.0301 0.447811 11.4779 0.000155104 12.0301 0H19.0301Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="25" viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M19.0301 0C19.5824 0 20.0301 0.447715 20.0301 1C20.0301 1.55228 19.5824 2 19.0301 2H13.0301V3.5H19.0301C19.5824 3.5 20.0301 3.94772 20.0301 4.5C20.0301 5.05228 19.5824 5.5 19.0301 5.5H13.0301V7H16.0301C16.5824 7 17.0301 7.44772 17.0301 8C17.0301 8.55228 16.5824 9 16.0301 9H13.0301V15H15.0281C15.7716 15 16.2564 15.7823 15.9236 16.4482L12.9256 22.4453L12.9246 22.4443C12.5789 23.1367 11.6327 23.1802 11.2117 22.5752L11.1346 22.4453L8.13652 16.4482C7.80454 15.7833 8.28773 15.0002 9.03203 15H11.0301V1C11.0301 0.447811 11.4779 0.000155104 12.0301 0H19.0301Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},yc=(vc.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,vc);N([P({type:Boolean})],yc.prototype,`useCssColor`,void 0),yc=N([M(`obi-wind-true-25`)],yc);var bc=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M18.9997 0C19.552 0 19.9997 0.447715 19.9997 1C19.9997 1.55228 19.552 2 18.9997 2H12.9997V3.5H18.9997C19.552 3.5 19.9997 3.94772 19.9997 4.5C19.9997 5.05228 19.552 5.5 18.9997 5.5H12.9997V7H18.9997C19.552 7 19.9997 7.44772 19.9997 8C19.9997 8.55228 19.552 9 18.9997 9H12.9997V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0H18.9997Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M18.9997 0C19.552 0 19.9997 0.447715 19.9997 1C19.9997 1.55228 19.552 2 18.9997 2H12.9997V3.5H18.9997C19.552 3.5 19.9997 3.94772 19.9997 4.5C19.9997 5.05228 19.552 5.5 18.9997 5.5H12.9997V7H18.9997C19.552 7 19.9997 7.44772 19.9997 8C19.9997 8.55228 19.552 9 18.9997 9H12.9997V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0H18.9997Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},xc=(bc.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,bc);N([P({type:Boolean})],xc.prototype,`useCssColor`,void 0),xc=N([M(`obi-wind-true-30`)],xc);var Sc=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M18.9997 0C19.552 0 19.9997 0.447715 19.9997 1C19.9997 1.55228 19.552 2 18.9997 2H12.9997V3.5H18.9997C19.552 3.5 19.9997 3.94772 19.9997 4.5C19.9997 5.05228 19.552 5.5 18.9997 5.5H12.9997V7H18.9997C19.552 7 19.9997 7.44772 19.9997 8C19.9997 8.55228 19.552 9 18.9997 9H12.9997V10.5H15.9997C16.552 10.5 16.9997 10.9477 16.9997 11.5C16.9997 12.0523 16.552 12.5 15.9997 12.5H12.9997V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0H18.9997Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M18.9997 0C19.552 0 19.9997 0.447715 19.9997 1C19.9997 1.55228 19.552 2 18.9997 2H12.9997V3.5H18.9997C19.552 3.5 19.9997 3.94772 19.9997 4.5C19.9997 5.05228 19.552 5.5 18.9997 5.5H12.9997V7H18.9997C19.552 7 19.9997 7.44772 19.9997 8C19.9997 8.55228 19.552 9 18.9997 9H12.9997V10.5H15.9997C16.552 10.5 16.9997 10.9477 16.9997 11.5C16.9997 12.0523 16.552 12.5 15.9997 12.5H12.9997V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0H18.9997Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Cc=(Sc.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Sc);N([P({type:Boolean})],Cc.prototype,`useCssColor`,void 0),Cc=N([M(`obi-wind-true-35`)],Cc);var wc=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M18.9997 0C19.4139 0 19.7497 0.335786 19.7497 0.75C19.7497 1.16421 19.4139 1.5 18.9997 1.5H12.9997V3H18.9997C19.4139 3 19.7497 3.33579 19.7497 3.75C19.7497 4.16421 19.4139 4.5 18.9997 4.5H12.9997V6H18.9997C19.4139 6 19.7497 6.33579 19.7497 6.75C19.7497 7.16421 19.4139 7.5 18.9997 7.5H12.9997V9H18.9997C19.4139 9 19.7497 9.33579 19.7497 9.75C19.7497 10.1642 19.4139 10.5 18.9997 10.5H12.9997V12H15.9997C16.4139 12 16.7497 12.3358 16.7497 12.75C16.7497 13.1642 16.4139 13.5 15.9997 13.5H12.9997V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0H18.9997Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M18.9997 0C19.4139 0 19.7497 0.335786 19.7497 0.75C19.7497 1.16421 19.4139 1.5 18.9997 1.5H12.9997V3H18.9997C19.4139 3 19.7497 3.33579 19.7497 3.75C19.7497 4.16421 19.4139 4.5 18.9997 4.5H12.9997V6H18.9997C19.4139 6 19.7497 6.33579 19.7497 6.75C19.7497 7.16421 19.4139 7.5 18.9997 7.5H12.9997V9H18.9997C19.4139 9 19.7497 9.33579 19.7497 9.75C19.7497 10.1642 19.4139 10.5 18.9997 10.5H12.9997V12H15.9997C16.4139 12 16.7497 12.3358 16.7497 12.75C16.7497 13.1642 16.4139 13.5 15.9997 13.5H12.9997V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0H18.9997Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Tc=(wc.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,wc);N([P({type:Boolean})],Tc.prototype,`useCssColor`,void 0),Tc=N([M(`obi-wind-true-45`)],Tc);var Ec=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M11.9997 0C12.552 0 12.9997 0.447715 12.9997 1V3.5H15.9997C16.552 3.5 16.9997 3.94772 16.9997 4.5C16.9997 5.05228 16.552 5.5 15.9997 5.5H12.9997V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M11.9997 0C12.552 0 12.9997 0.447715 12.9997 1V3.5H15.9997C16.552 3.5 16.9997 3.94772 16.9997 4.5C16.9997 5.05228 16.552 5.5 15.9997 5.5H12.9997V15H14.9978C15.7413 15 16.226 15.7823 15.8933 16.4482L12.8952 22.4453L12.8942 22.4443C12.5485 23.1367 11.6023 23.1802 11.1813 22.5752L11.1042 22.4453L8.10615 16.4482C7.77418 15.7833 8.25736 15.0002 9.00166 15H10.9997V1C10.9997 0.447811 11.4476 0.000155104 11.9997 0Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Dc=(Ec.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Ec);N([P({type:Boolean})],Dc.prototype,`useCssColor`,void 0),Dc=N([M(`obi-wind-true-5`)],Dc);var Oc=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.0816 0.00343268L12.1969 0.0200342L19.691 1.51906C20.7637 1.73378 20.7637 3.26722 19.691 3.48195L12.9996 4.81984V15.0005H14.9977C15.7412 15.0005 16.2259 15.7828 15.8932 16.4487L12.8951 22.4458C12.526 23.1831 11.473 23.1833 11.1041 22.4458L8.10605 16.4487C7.77356 15.7833 8.25783 15.0008 9.00156 15.0005H10.9996V1.00148C10.9997 0.4093 11.508 -0.0441781 12.0816 0.00343268Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.0816 0.00343268L12.1969 0.0200342L19.691 1.51906C20.7637 1.73378 20.7637 3.26722 19.691 3.48195L12.9996 4.81984V15.0005H14.9977C15.7412 15.0005 16.2259 15.7828 15.8932 16.4487L12.8951 22.4458C12.526 23.1831 11.473 23.1833 11.1041 22.4458L8.10605 16.4487C7.77356 15.7833 8.25783 15.0008 9.00156 15.0005H10.9996V1.00148C10.9997 0.4093 11.508 -0.0441781 12.0816 0.00343268Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},kc=(Oc.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Oc);N([P({type:Boolean})],kc.prototype,`useCssColor`,void 0),kc=N([M(`obi-wind-true-50`)],kc);var Ac=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.1969 0.0200342L12.0816 0.00343268C11.508 -0.0441781 10.9997 0.4093 10.9996 1.00148V15.0005H9.00156C8.25783 15.0008 7.77356 15.7833 8.10605 16.4487L11.1041 22.4458C11.473 23.1833 12.526 23.1831 12.8951 22.4458L15.8932 16.4487C16.2259 15.7828 15.7412 15.0005 14.9977 15.0005H12.9996V8H15.9996C16.5519 8 16.9996 7.55228 16.9996 7C16.9996 6.44772 16.5519 6 15.9996 6H12.9996V4.81984L19.691 3.48195C20.7637 3.26722 20.7637 1.73378 19.691 1.51906L12.1969 0.0200342Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.1969 0.0200342L12.0816 0.00343268C11.508 -0.0441781 10.9997 0.4093 10.9996 1.00148V15.0005H9.00156C8.25783 15.0008 7.77356 15.7833 8.10605 16.4487L11.1041 22.4458C11.473 23.1833 12.526 23.1831 12.8951 22.4458L15.8932 16.4487C16.2259 15.7828 15.7412 15.0005 14.9977 15.0005H12.9996V8H15.9996C16.5519 8 16.9996 7.55228 16.9996 7C16.9996 6.44772 16.5519 6 15.9996 6H12.9996V4.81984L19.691 3.48195C20.7637 3.26722 20.7637 1.73378 19.691 1.51906L12.1969 0.0200342Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},jc=(Ac.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Ac);N([P({type:Boolean})],jc.prototype,`useCssColor`,void 0),jc=N([M(`obi-wind-true-55`)],jc);var Mc=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.0816 0.00343268L12.1969 0.0200342L19.691 1.51906C20.7637 1.73378 20.7637 3.26722 19.691 3.48195L12.9996 4.81984V6.0005H18.9996C19.5519 6.0005 19.9996 6.44822 19.9996 7.0005C19.9994 7.5526 19.5518 8.0005 18.9996 8.0005H12.9996V15.0005H14.9977C15.7412 15.0005 16.2259 15.7828 15.8932 16.4487L12.8951 22.4458C12.526 23.1831 11.473 23.1833 11.1041 22.4458L8.10605 16.4487C7.77356 15.7833 8.25783 15.0008 9.00156 15.0005H10.9996V1.00148C10.9997 0.4093 11.508 -0.0441781 12.0816 0.00343268Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.0816 0.00343268L12.1969 0.0200342L19.691 1.51906C20.7637 1.73378 20.7637 3.26722 19.691 3.48195L12.9996 4.81984V6.0005H18.9996C19.5519 6.0005 19.9996 6.44822 19.9996 7.0005C19.9994 7.5526 19.5518 8.0005 18.9996 8.0005H12.9996V15.0005H14.9977C15.7412 15.0005 16.2259 15.7828 15.8932 16.4487L12.8951 22.4458C12.526 23.1831 11.473 23.1833 11.1041 22.4458L8.10605 16.4487C7.77356 15.7833 8.25783 15.0008 9.00156 15.0005H10.9996V1.00148C10.9997 0.4093 11.508 -0.0441781 12.0816 0.00343268Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Nc=(Mc.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Mc);N([P({type:Boolean})],Nc.prototype,`useCssColor`,void 0),Nc=N([M(`obi-wind-true-60`)],Nc);var Pc=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.1969 0.0200342L12.0816 0.00343268C11.508 -0.0441781 10.9997 0.4093 10.9996 1.00148V15.0005H9.00156C8.25783 15.0008 7.77356 15.7833 8.10605 16.4487L11.1041 22.4458C11.473 23.1833 12.526 23.1831 12.8951 22.4458L15.8932 16.4487C16.2259 15.7828 15.7412 15.0005 14.9977 15.0005H12.9996V11.5005H15.9996C16.5519 11.5005 16.9996 11.0528 16.9996 10.5005C16.9996 9.94822 16.5519 9.5005 15.9996 9.5005H12.9996V8.0005H18.9996C19.5518 8.0005 19.9994 7.5526 19.9996 7.0005C19.9996 6.44822 19.5519 6.0005 18.9996 6.0005H12.9996V4.81984L19.691 3.48195C20.7637 3.26722 20.7637 1.73378 19.691 1.51906L12.1969 0.0200342Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.1969 0.0200342L12.0816 0.00343268C11.508 -0.0441781 10.9997 0.4093 10.9996 1.00148V15.0005H9.00156C8.25783 15.0008 7.77356 15.7833 8.10605 16.4487L11.1041 22.4458C11.473 23.1833 12.526 23.1831 12.8951 22.4458L15.8932 16.4487C16.2259 15.7828 15.7412 15.0005 14.9977 15.0005H12.9996V11.5005H15.9996C16.5519 11.5005 16.9996 11.0528 16.9996 10.5005C16.9996 9.94822 16.5519 9.5005 15.9996 9.5005H12.9996V8.0005H18.9996C19.5518 8.0005 19.9994 7.5526 19.9996 7.0005C19.9996 6.44822 19.5519 6.0005 18.9996 6.0005H12.9996V4.81984L19.691 3.48195C20.7637 3.26722 20.7637 1.73378 19.691 1.51906L12.1969 0.0200342Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Fc=(Pc.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Pc);N([P({type:Boolean})],Fc.prototype,`useCssColor`,void 0),Fc=N([M(`obi-wind-true-65`)],Fc);var Ic=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.0816 0.00343268L12.1969 0.0200342L19.691 1.51906C20.7637 1.73378 20.7637 3.26722 19.691 3.48195L12.9996 4.81984V6.0005H18.9996C19.5519 6.0005 19.9996 6.44822 19.9996 7.0005C19.9994 7.5526 19.5518 8.0005 18.9996 8.0005H12.9996V9.5005H18.9996C19.5519 9.5005 19.9996 9.94822 19.9996 10.5005C19.9994 11.0526 19.5518 11.5005 18.9996 11.5005H12.9996V15.0005H14.9977C15.7412 15.0005 16.2259 15.7828 15.8932 16.4487L12.8951 22.4458C12.526 23.1831 11.473 23.1833 11.1041 22.4458L8.10605 16.4487C7.77356 15.7833 8.25783 15.0008 9.00156 15.0005H10.9996V1.00148C10.9997 0.4093 11.508 -0.0441781 12.0816 0.00343268Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.0816 0.00343268L12.1969 0.0200342L19.691 1.51906C20.7637 1.73378 20.7637 3.26722 19.691 3.48195L12.9996 4.81984V6.0005H18.9996C19.5519 6.0005 19.9996 6.44822 19.9996 7.0005C19.9994 7.5526 19.5518 8.0005 18.9996 8.0005H12.9996V9.5005H18.9996C19.5519 9.5005 19.9996 9.94822 19.9996 10.5005C19.9994 11.0526 19.5518 11.5005 18.9996 11.5005H12.9996V15.0005H14.9977C15.7412 15.0005 16.2259 15.7828 15.8932 16.4487L12.8951 22.4458C12.526 23.1831 11.473 23.1833 11.1041 22.4458L8.10605 16.4487C7.77356 15.7833 8.25783 15.0008 9.00156 15.0005H10.9996V1.00148C10.9997 0.4093 11.508 -0.0441781 12.0816 0.00343268Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Lc=(Ic.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Ic);N([P({type:Boolean})],Lc.prototype,`useCssColor`,void 0),Lc=N([M(`obi-wind-true-70`)],Lc);var Rc=[0,1,5,10,15,20,25,30,35,45,50,55,60,65,70,100],zc=2,Bc=1.5547000000000004*zc,Vc=new Map;function Hc(e){let t=`obi-wind-true-${e}`,n=Vc.get(t);if(n)return n;let r=customElements.get(t);if(!r)return null;let i=new r,a=i.icon??i.iconCss;return a?(Vc.set(t,a),a):null}function Uc(e,t){if(e==null||!Number.isFinite(e)||e<=0)return t[0];let n=t[0],r=Math.abs(e-n);for(let i=1;i<t.length;i++){let a=Math.abs(e-t[i]);a<r&&(n=t[i],r=a)}return n}function Wc(e){return Uc(e,Rc)}function Gc(e){let{windKnots:t,fromDirectionDeg:n,radius:r,color:i}=e,a=Hc(Wc(t));if(!a)return k``;let o=lt(n),s=Math.sin(o)*r,c=-Math.cos(o)*r;return k`<g style=${yr({color:i??`var(--instrument-regular-secondary-color)`})} transform="translate(${s} ${c}) rotate(${n}) translate(${-24} ${-44.8906}) scale(${zc})">
    ${a}
  </g>`}function Kc(e){return Jc({filename:`current-${e.current}.svg`,fromDirectionDeg:e.fromDirectionDeg,radius:e.radius,color:e.color})}function qc(e){let{current:t,fromDirectionDeg:n,scale:r,color:i}=e,a=Yc[`current-${t}.svg`];return a?k`<g style=${yr(i?{"--instrument-regular-secondary-color":i}:{})} transform="rotate(${180+n}) scale(${r}) translate(-12 -12)">
    ${a}
  </g>`:k``}function Jc(e){let{filename:t,fromDirectionDeg:n,radius:r,color:i}=e,a=lt(n-180),o=Yc[t];return k`<g style=${yr(i?{"--instrument-regular-secondary-color":i}:{})} transform="translate(${-Math.sin(a)*r} ${Math.cos(a)*r}) rotate(${180+n}) translate(-24, 0) scale(2)">
    ${o}
  </g>`}var Yc={"current-0.svg":k`<path d="M11 2V22H13V2Z" stroke="var(--border-silhouette-color)" stroke-width="2"/>
<path d="M11 2V22H13V2Z" fill="var(--instrument-regular-secondary-color)"/>`,"current-1.svg":k`<path d="M11 7.00002L11 24L13 24L13 7.00005L11 7.00002Z" stroke="var(--border-silhouette-color)" stroke-width="2"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M6.79309 5.20723L12.0002 0.00012207L17.2073 5.20723L15.7931 6.62144L12.0002 2.82855L8.2073 6.62144L6.79309 5.20723Z" stroke="var(--border-silhouette-color)" stroke-width="2"/>
<path d="M11 7.00002L11 24L13 24L13 7.00005L11 7.00002Z" fill="var(--instrument-regular-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M6.79309 5.20723L12.0002 0.00012207L17.2073 5.20723L15.7931 6.62144L12.0002 2.82855L8.2073 6.62144L6.79309 5.20723Z" fill="var(--instrument-regular-secondary-color)"/>`,"current-2.svg":k`<path d="M10.9742 12.0003L10.9742 24.0049L12.9999 24.005L12.9999 12.0004L10.9742 12.0003Z" stroke="var(--border-silhouette-color)" stroke-width="2"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M6.79285 5.20747L12 0.000366211L17.2071 5.20747L15.7928 6.62169L12 2.82879L8.20706 6.62169L6.79285 5.20747Z" stroke="var(--border-silhouette-color)" stroke-width="2"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M6.99988 10.5861L12.207 5.37903L17.4141 10.5861L15.9999 12.0003L12.207 8.20745L8.41409 12.0003L6.99988 10.5861Z" stroke="var(--border-silhouette-color)" stroke-width="2"/>
<path d="M10.9742 12.0003L10.9742 24.0049L12.9999 24.005L12.9999 12.0004L10.9742 12.0003Z" fill="var(--instrument-regular-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M6.79285 5.20747L12 0.000366211L17.2071 5.20747L15.7928 6.62169L12 2.82879L8.20706 6.62169L6.79285 5.20747Z" fill="var(--instrument-regular-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M6.99988 10.5861L12.207 5.37903L17.4141 10.5861L15.9999 12.0003L12.207 8.20745L8.41409 12.0003L6.99988 10.5861Z" fill="var(--instrument-regular-secondary-color)"/>`,"current-3.svg":k`<path d="M11 18L11 24L13 24L13 18L11 18Z" stroke="var(--border-silhouette-color)" stroke-width="2"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M6.79297 5.20711L12.0001 0L17.2072 5.20711L15.793 6.62132L12.0001 2.82843L8.20718 6.62132L6.79297 5.20711Z" stroke="var(--border-silhouette-color)" stroke-width="2"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M7 10.5858L12.2071 5.37866L17.4142 10.5858L16 12L12.2071 8.20709L8.41421 12L7 10.5858Z" stroke="var(--border-silhouette-color)" stroke-width="2"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M7 16.5858L12.2071 11.3787L17.4142 16.5858L16 18L12.2071 14.2071L8.41421 18L7 16.5858Z" stroke="var(--border-silhouette-color)" stroke-width="2"/>
<path d="M11 18L11 24L13 24L13 18L11 18Z" fill="var(--instrument-regular-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M6.79297 5.20711L12.0001 0L17.2072 5.20711L15.793 6.62132L12.0001 2.82843L8.20718 6.62132L6.79297 5.20711Z" fill="var(--instrument-regular-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M7 10.5858L12.2071 5.37866L17.4142 10.5858L16 12L12.2071 8.20709L8.41421 12L7 10.5858Z" fill="var(--instrument-regular-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M7 16.5858L12.2071 11.3787L17.4142 16.5858L16 18L12.2071 14.2071L8.41421 18L7 16.5858Z" fill="var(--instrument-regular-secondary-color)"/>`,"current-4.svg":k`<path fill-rule="evenodd" clip-rule="evenodd" d="M6.79297 5.20711L12.0001 0L17.2072 5.20711L15.793 6.62132L12.0001 2.82843L8.20718 6.62132L6.79297 5.20711Z" stroke="var(--border-silhouette-color)" stroke-width="2"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M7 10.5858L12.2071 5.37866L17.4142 10.5858L16 12L12.2071 8.20709L8.41421 12L7 10.5858Z" stroke="var(--border-silhouette-color)" stroke-width="2"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M7 16.5858L12.2071 11.3787L17.4142 16.5858L16 18L12.2071 14.2071L8.41421 18L7 16.5858Z" stroke="var(--border-silhouette-color)" stroke-width="2"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M7 22.5858L12.2071 17.3787L17.4142 22.5858L16 24L12.2071 20.2071L8.41421 24L7 22.5858Z" stroke="var(--border-silhouette-color)" stroke-width="2"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M6.79297 5.20711L12.0001 0L17.2072 5.20711L15.793 6.62132L12.0001 2.82843L8.20718 6.62132L6.79297 5.20711Z" fill="var(--instrument-regular-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M7 10.5858L12.2071 5.37866L17.4142 10.5858L16 12L12.2071 8.20709L8.41421 12L7 10.5858Z" fill="var(--instrument-regular-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M7 16.5858L12.2071 11.3787L17.4142 16.5858L16 18L12.2071 14.2071L8.41421 18L7 16.5858Z" fill="var(--instrument-regular-secondary-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M7 22.5858L12.2071 17.3787L17.4142 22.5858L16 24L12.2071 20.2071L8.41421 24L7 22.5858Z" fill="var(--instrument-regular-secondary-color)"/>`},Xc=(e,t)=>{let n=e._$AN;if(n===void 0)return!1;for(let e of n)e._$AO?.(t,!1),Xc(e,t);return!0},Zc=e=>{let t,n;do{if((t=e._$AM)===void 0)break;n=t._$AN,n.delete(e),e=t}while(n?.size===0)},Qc=e=>{for(let t;t=e._$AM;e=t){let n=t._$AN;if(n===void 0)t._$AN=n=new Set;else if(n.has(e))break;n.add(e),tl(t)}};function $c(e){this._$AN===void 0?this._$AM=e:(Zc(this),this._$AM=e,Qc(this))}function el(e,t=!1,n=0){let r=this._$AH,i=this._$AN;if(i!==void 0&&i.size!==0){if(t){if(Array.isArray(r))for(let e=n;e<r.length;e++)Xc(r[e],!1),Zc(r[e]);else r!=null&&(Xc(r,!1),Zc(r))}else Xc(this,e)}}var tl=e=>{e.type==ft.CHILD&&(e._$AP??=el,e._$AQ??=$c)},nl=class extends mt{constructor(){super(...arguments),this._$AN=void 0}_$AT(e,t,n){super._$AT(e,t,n),Qc(this),this.isConnected=e._$AU}_$AO(e,t=!0){e!==this.isConnected&&(this.isConnected=e,e?this.reconnected?.():this.disconnected?.()),t&&(Xc(this,e),Zc(this))}setValue(e){if(qr(this._$Ct))this._$Ct._$AI(e,this);else{let t=[...this._$Ct._$AH];t[this._$Ci]=e,this._$Ct._$AI(t,this,0)}}disconnected(){}reconnected(){}},rl=class{constructor(e,{target:t,config:n,callback:r,skipInitial:i}){this.t=new Set,this.o=!1,this.i=!1,this.h=e,t!==null&&this.t.add(t??e),this.l=n,this.o=i??this.o,this.callback=r,window.ResizeObserver?(this.u=new ResizeObserver(e=>{this.handleChanges(e),this.h.requestUpdate()}),e.addController(this)):console.warn(`ResizeController error: browser does not support ResizeObserver.`)}handleChanges(e){this.value=this.callback?.(e,this.u)}hostConnected(){for(let e of this.t)this.observe(e)}hostDisconnected(){this.disconnect()}async hostUpdated(){!this.o&&this.i&&this.handleChanges([]),this.i=!1}observe(e){this.t.add(e),this.u.observe(e,this.l),this.i=!0,this.h.requestUpdate()}unobserve(e){this.t.delete(e),this.u.unobserve(e)}disconnect(){this.u.disconnect()}target(e){return il(this,e)}},il=pt(class extends nl{constructor(){super(...arguments),this.observing=!1}render(e,t){}update(e,[t,n]){this.controller=t,this.part=e,this.observe=n,!1===n?(t.unobserve(e.element),this.observing=!1):!1===this.observing&&(t.observe(e.element),this.observing=!0)}disconnected(){this.controller?.unobserve(this.part.element),this.observing=!1}reconnected(){!1!==this.observe&&!1===this.observing&&(this.controller?.observe(this.part.element),this.observing=!0)}}),al,ol=function(e){return e.single=`single`,e.double=`double`,e.doubleThin=`doubleThin`,e.triple=`triple`,e}({}),sl=160,cl=112,ll=136,ul=88;function dl(e){switch(e){case`single`:return sl;case`double`:return cl;case`doubleThin`:return ll;case`triple`:return ul;default:throw Error(`Unknown WatchCircleType: ${e}`)}}var fl=4,pl=4,ml=188,hl=ml+Bc,K=(al=class extends j{constructor(...e){super(...e),this._setpointId=`watch-setpoint-${Math.random().toString(36).slice(2,9)}`,this._newSetpointId=`watch-new-setpoint-${Math.random().toString(36).slice(2,9)}`,this.state=gi.active,this.priority=W.regular,this.watchCircleType=`single`,this.hasBackgroundCircle=!1,this.northArrow=!1,this.northMarker=!1,this.atAngleSetpoint=!1,this.angleSetpointAtZeroDeadband=.5,this.setpointOverride=!1,this.touching=!1,this.animateSetpoint=!1,this._setpointCssAngle=0,this._setpointCssAngleInit=!1,this.areas=[],this.barAreas=[],this.roundBandCuts=!1,this.splitBand=!1,this.needles=[],this.tickmarks=[],this.tickmarksInside=!1,this.tickmarkStyle=Eo.regular,this.advices=[],this.crosshairEnabled=!1,this.crosshairCenterCutout=!1,this.showLabels=!1,this.insideLabelsFlush=!1,this.vessels=[],this.windKnots=null,this.windFromDirectionDeg=null,this.windSymbolRadius=null,this.current=null,this.currentFromDirectionDeg=null,this.currentSymbolRadius=null,this.currentIconCentered=!1,this.scaleCurrentIcon=1,this.starboardPortIndicator=!1,this.clipTop=0,this.clipBottom=0,this.clipLeft=0,this.clipRight=0,this.endLabelsMaxMin=!1,this.scaleWindIcon=1,this.zoomToFitArc=!1,this.tickFadeAngle=0,this.rotPosition=Io.innerCircle,this.rotStartAngle=0,this.rotEndAngle=0,this.rotPortStarboard=!1,this.rotAtZeroDeadband=Uo,this.rotDotAnimationFactor=18,this._legacyRotationsPerMinute=0,this._resizeController=new rl(this,{}),this._rOff=0,this._labelsHidden=!1,this._hostSizePinned=!1}set rotationsPerMinute(e){this._legacyRotationsPerMinute=e}get rotationsPerMinute(){return this._legacyRotationsPerMinute}get _effectiveRpm(){return this.rateOfTurnDegreesPerMinute==null?this._legacyRotationsPerMinute:this.rateOfTurnDegreesPerMinute/360*this.rotDotAnimationFactor}firstUpdated(e){super.firstUpdated(e),Xi(this._resizeController,this.renderRoot)}willUpdate(e){if(super.willUpdate(e),this._rotController&&(e.has(`rateOfTurnDegreesPerMinute`)||e.has(`rotDotAnimationFactor`)||e.has(`rotationsPerMinute`))&&(this._rotController.rotationsPerMinute=this._effectiveRpm),e.has(`newAngleSetpoint`)&&this.animateSetpoint){let t=e.get(`newAngleSetpoint`);if(t!==void 0&&this.newAngleSetpoint===void 0){this._departingNewAngleSetpoint=t,clearTimeout(this._animationTimer);let e=Ti(this);this._animationTimer=setTimeout(()=>{this._departingNewAngleSetpoint=void 0},e)}}}disconnectedCallback(){super.disconnectedCallback(),clearTimeout(this._animationTimer),this._rotController=us(this,this._rotController)}updated(e){super.updated(e),this._hostSizePinned=Yi(this,this.arcFrame?void 0:this._ownFrame,this._hostSizePinned);let t=this.rotType?this.renderRoot.querySelector(`#rot-spinner`):null;if(!t){this._rotController=us(this,this._rotController);return}(!this._rotController||this._rotController.el!==t)&&(this._rotController=us(this,this._rotController),this._rotController=new ls(this,t,this._effectiveRpm))}get innerRingRadius(){return dl(this.watchCircleType)}_bandRadius(e){return e+this._rOff}watchCircle(){let e=[],t=this.hasBackgroundCircle&&this.state!==gi.off?k`
        <circle
          cx="0"
          cy="0"
          r="${this._bandRadius(184)}"
          fill="var(--instrument-frame-primary-color)"
          stroke="none"
        />`:void 0,n=this.hasBackgroundCircle&&this.areas.length>0?k`
        <circle
          cx="0"
          cy="0"
          r="${this._bandRadius(184)}"
          fill="none"
          stroke="var(--instrument-frame-tertiary-color)"
          stroke-width="1"
          vector-effect="non-scaling-stroke"
        />`:void 0;if(this.state!==gi.off){if(e.push(k`
        <circle
          cx="0"
          cy="0"
          r="${this._bandRadius(172)}"
          stroke="var(--instrument-frame-primary-color)"
          fill="none"
          stroke-width="24"
        />`),this.watchCircleType!==`single`){let t=this._bandRadius(sl),n=this._bandRadius(this.watchCircleType===`doubleThin`?ll:cl),r=(t+n)/2,i=t-n;this.splitBand&&this.watchCircleType===`double`?e.push(...this.splitBandTracks()):this.roundBandCuts&&this.areas.length>0?e.push(...this.areas.map(e=>k`<path d=${ss({startAngle:e.startAngle,endAngle:e.endAngle,R:t,r:n,roundOutsideCut:e.roundOutsideCut,roundInsideCut:e.roundInsideCut,roundRadius:e.roundRadius})} fill="var(--instrument-frame-secondary-color)" stroke=${e.outlined?`var(--instrument-frame-tertiary-color)`:`var(--instrument-frame-secondary-color)`} stroke-width="1" vector-effect="non-scaling-stroke" />`)):e.push(k`
            <circle cx="0" cy="0" r=${r} stroke="var(--instrument-frame-secondary-color)" stroke-width=${i} fill="none" />
            <circle cx="0" cy="0" r=${t} stroke="var(--instrument-frame-secondary-color)" stroke-width="1" fill="none" vector-effect="non-scaling-stroke" />
            <circle cx="0" cy="0" r=${n} stroke="var(--instrument-frame-secondary-color)" stroke-width="1" fill="none" vector-effect="non-scaling-stroke" />
        `)}if(this.watchCircleType===`triple`){let t=this._bandRadius(cl),n=this._bandRadius(ul),r=(t+n)/2,i=t-n;e.push(k`<circle cx="0" cy="0" r=${r} stroke="var(--instrument-frame-primary-color)" stroke-width=${i} fill="none" />`)}}let r=Math.max(200,184+this._rOff+50),i=e;if(this.areas.length>0){let a=this.areas.map(e=>ss({startAngle:e.startAngle,endAngle:e.endAngle,R:this._bandRadius(184),r:this._bandRadius(this.innerRingRadius),roundOutsideCut:e.roundOutsideCut,roundInsideCut:e.roundInsideCut,roundRadius:e.roundRadius}));i=[k`<mask id="cutMask">
        <rect x="${-r}" y="${-r}" width="${r*2}" height="${r*2}" fill="black" />
        ${a.map(e=>k`<path d=${e} fill="white" vector-effect="non-scaling-stroke" stroke="white" stroke-width="1"/>`)}
      </mask>`,k`<clipPath id="rot-arc-clip">${this.areas.map(e=>k`<path d=${ss({startAngle:e.startAngle,endAngle:e.endAngle,R:184+this._rOff+20,r:0,roundOutsideCut:e.roundOutsideCut,roundInsideCut:e.roundInsideCut})} />`)}</clipPath>`,...t?[t]:[],k`<g mask="url(#cutMask)">${e}</g>`,...n?[n]:[]],this.hasBackgroundCircle||a.forEach(e=>{i.push(k`<path d=${e} fill="none" stroke="var(--instrument-frame-tertiary-color)" vector-effect="non-scaling-stroke"/>`)})}else t&&(i=[t,...e]),this.state===gi.off?i.push(k`
          ${$o(`innerRing`,{radius:this._bandRadius(184),strokeWidth:1,strokeColor:`var(--instrument-frame-tertiary-color)`,strokePosition:`center`,fillColor:`none`})}
        `):(i.push($o(`outerRing`,{radius:this._bandRadius(184),strokeWidth:1,strokeColor:`var(--instrument-frame-tertiary-color)`,strokePosition:`center`,fillColor:`none`})),i.push(k`
          ${$o(`innerRing`,{radius:this._bandRadius(this.innerRingRadius),strokeWidth:1,strokeColor:`var(--instrument-frame-tertiary-color)`,strokePosition:`center`,fillColor:`none`})}
        `));return i}_renderTickFadeDefs(){if(this.tickFadeAngle<=0||this.areas.length===0)return A;let e=this.areas[0],t=e.endAngle-e.startAngle,n=Math.min(this.tickFadeAngle,t/4);if(n<.5)return A;let{startAngle:r,endAngle:i}=e,a=184+this._rOff+200,o=e=>a*Math.sin(lt(e)),s=e=>-a*Math.cos(lt(e)),c=(e,t)=>{let n=o(e),r=s(e),i=o(t),c=s(t),l=+(t-e>180);return`M 0 0 L ${n} ${r} A ${a} ${a} 0 ${l} 1 ${i} ${c} Z`},l=(this._bandRadius(184)+this._bandRadius(this.innerRingRadius))/2,u=e=>l*Math.sin(lt(e)),d=e=>-l*Math.cos(lt(e));return k`
      <defs>
        <linearGradient id="tickFadeL" gradientUnits="userSpaceOnUse"
          x1="${u(r)}" y1="${d(r)}"
          x2="${u(r+n)}" y2="${d(r+n)}">
          <stop offset="0" stop-color="black" />
          <stop offset="1" stop-color="white" />
        </linearGradient>
        <linearGradient id="tickFadeR" gradientUnits="userSpaceOnUse"
          x1="${u(i-n)}" y1="${d(i-n)}"
          x2="${u(i)}" y2="${d(i)}">
          <stop offset="0" stop-color="white" />
          <stop offset="1" stop-color="black" />
        </linearGradient>
        <mask id="tickFadeMask" maskUnits="userSpaceOnUse"
          x="${-a}" y="${-a}" width="${a*2}" height="${a*2}">
          <path d="${c(r+n,i-n)}" fill="white" />
          <path d="${c(r,r+n)}" fill="url(#tickFadeL)" />
          <path d="${c(i-n,i)}" fill="url(#tickFadeR)" />
        </mask>
      </defs>
    `}renderCrosshair(e,t,n){let r=!!t&&t.positions.length>0,i=r||n!==void 0,a=r?Math.max(...t.positions.map(e=>Math.abs(e.x===0?e.y:e.x))):0,o=r?3/t.scale:0;return k`
      ${i?k`
        <defs>
          <mask
            id="crosshair-label-mask"
            maskUnits="userSpaceOnUse"
            x="-${e}" y="-${e}"
            width="${e*2}" height="${e*2}"
          >
            <rect x="-${e}" y="-${e}" width="${e*2}" height="${e*2}" fill="white"/>
            ${r?k`
            <!-- Annular ring knockout: hide crosshair between labels and inner ring -->
            <circle cx="0" cy="0" r="${t.innerRingRadius}" fill="black"/>
            <circle cx="0" cy="0" r="${a-o}" fill="white"/>
            <!-- Per-label rectangular knockouts -->
            ${t.positions.map(e=>{let n=12/t.scale+3/t.scale*2;return k`
                <rect
                  x="${e.x-n/2}" y="${e.y-n/2}"
                  width="${n}" height="${n}"
                  fill="black"
                  transform="rotate(${-(t.rotation??0)})"
                  transform-origin="${e.x} ${e.y}"
                />
              `})}`:A}
            ${n===void 0?A:k`<circle cx="0" cy="0" r="${n}" fill="black"/>`}
          </mask>
        </defs>`:A}
      <g mask=${i?`url(#crosshair-label-mask)`:A}>
        <line
          x1="-${e}"
          y1="0"
          x2="${e}"
          y2="0"
          stroke="var(--instrument-frame-tertiary-color)"
          stroke-width="1"
          vector-effect="non-scaling-stroke"
        />
        <line
          x1="0"
          y1="-${e}"
          x2="0"
          y2="${e}"
          stroke="var(--instrument-frame-tertiary-color)"
          stroke-width="1"
          vector-effect="non-scaling-stroke"
        />
      </g>
    `}splitBandTracks(){let e=`var(--instrument-frame-secondary-color)`;if(this.areas.length===0){let t=(this._bandRadius(128)+this._bandRadius(160))/2;return[k`<circle cx="0" cy="0" r=${this._bandRadius(116)} stroke=${e} stroke-width=${8} fill="none" />`,k`<circle cx="0" cy="0" r=${t} stroke=${e} stroke-width=${32} fill="none" />`]}return this.areas.flatMap(t=>[k`<path d=${ss({startAngle:t.startAngle,endAngle:t.endAngle,R:this._bandRadius(120),r:this._bandRadius(112),roundOutsideCut:!0,roundInsideCut:!0,roundRadius:4})} fill=${e} stroke=${e} stroke-width="1" vector-effect="non-scaling-stroke" />`,k`<path d=${ss({startAngle:t.startAngle,endAngle:t.endAngle,R:this._bandRadius(160),r:this._bandRadius(128),roundOutsideCut:!0,roundInsideCut:!0})} fill=${e} stroke=${e} stroke-width="1" vector-effect="non-scaling-stroke" />`])}renderBars(){return this.barAreas.length===0?A:this.barAreas.map((e,t)=>{let n=Math.min(e.startAngle,e.endAngle),r=Math.max(e.startAngle,e.endAngle);if(this.splitBand&&this.areas.length>0)for(let e of this.areas)Math.abs(n-e.startAngle)<=.01&&(n-=pl),Math.abs(r-e.endAngle)<=.01&&(r+=pl);let i=ss({r:this._bandRadius(e.innerRadius??cl),R:this._bandRadius(e.outerRadius??sl),startAngle:n,endAngle:r,roundInsideCut:!1,roundOutsideCut:!1}),a=(e.outerRadius??sl)+this._rOff+40,o=k`<mask id="barMask-${t}">
        <rect x="${-a}" y="${-a}" width="${a*2}" height="${a*2}" fill="black" />
        <path d=${ss({r:1,R:a,startAngle:n,endAngle:r,roundInsideCut:!1,roundOutsideCut:!1})} fill="white" />
      </mask>`,s=(this.roundBandCuts||this.splitBand)&&this.areas.length>0?k`<mask id="barTrackMask-${t}">
              <rect x="${-a}" y="${-a}" width="${a*2}" height="${a*2}" fill="black" />
              ${this.areas.map(t=>k`<path d=${ss({startAngle:t.startAngle,endAngle:t.endAngle,R:this._bandRadius(this.splitBand?160:e.outerRadius??sl),r:this._bandRadius(this.splitBand?128:e.innerRadius??cl),roundOutsideCut:this.splitBand||t.roundOutsideCut,roundInsideCut:this.splitBand||t.roundInsideCut,roundRadius:this.splitBand?void 0:t.roundRadius})} fill="white" stroke="white" stroke-width="1" vector-effect="non-scaling-stroke" />`)}
            </mask>`:A;return k`
        ${o}
        ${s}
        <g mask=${this.areas.length>0&&!this.splitBand?`url(#cutMask)`:A}>
        <g mask=${s===A?A:`url(#barTrackMask-${t})`}>
        <path
          d=${i}
          fill=${e.fillColor}
          stroke=${e.fillColor}
          stroke-width="1"
          vector-effect="non-scaling-stroke"
          mask="url(#barMask-${t})"
          />
          </g>
          </g>
          `})}renderNeedles(){return this.needles.length===0?A:this.needles.map(e=>k`
        <rect
          transform="rotate(${e.angle})"
          x="-4" y="${-this._bandRadius(sl)}" width="8" height="${e.length??48}" rx="4"
          fill=${e.fillColor}
          stroke=${e.strokeColor}
          stroke-width="1"
          vector-effect="non-scaling-stroke"
          paint-order="stroke fill"
        />
      `)}getScale({width:e,height:t}){let n=Ji(this),r=Math.min(n.width/e,n.height/t);return!Number.isFinite(r)||r<=0?1:r}getLabelWidthPx(){return this.padding!==void 0||this.tickmarksInside?0:this.showLabels?16:Zi(this.tickmarks.map(e=>e.text))}render(){let e,t,n,r,i;if(this.arcFrame)this._rOff=this.arcFrame.radiusOffset,this._labelsHidden=!1,this._ownFrame=void 0,e=this.arcFrame.width,t=this.arcFrame.height,n=this.arcFrame.x,r=this.arcFrame.y,i=this.arcFrame.viewBox;else{let a=oa({basePadding:this.padding??24,labelWidthPx:this.getLabelWidthPx(),clips:{top:this.clipTop,bottom:this.clipBottom,left:this.clipLeft,right:this.clipRight},containerPx:Ji(this),faceDiameter:this.faceDiameter,zoomToFitArc:this.zoomToFitArc,areas:this.areas,innerRadius:this.innerRingRadius});this._rOff=a.radiusOffset,this._labelsHidden=a.labelsHidden,this._ownFrame=a,e=a.width,t=a.height,n=a.x,r=a.y,i=a.viewBox}let a=this._rOff,o=this.getScale({width:e,height:t}),s=e>0?-n/e*100:50,c=t>0?-r/t*100:50,l=s!==50||c!==50,u=this.renderSetpoint(),d=this.tickmarksInside?this._bandRadius(this.innerRingRadius):this._bandRadius(184),f=Math.max(...this.tickmarks.map(e=>e.text?.length??0)),p=this.tickmarks.map(e=>Oo(e.angle,{size:e.type,style:this.tickmarkStyle,scale:o,text:this.showLabels||this._labelsHidden?void 0:e.text,inside:this.tickmarksInside,textRadius:d,rotation:this.rotation,maxDigits:f,color:e.color,radiusOffset:a,endLabelsMaxMin:this.endLabelsMaxMin})),m=this.advices?this.advices.map(e=>Po(e,a)):A,h=this.showLabels&&!this._labelsHidden,g=this.northArrow,_=this.tickmarksInside&&h,v=!this.northArrow,y=h?ds({scale:o,inside:this.tickmarksInside,innerRadius:this.innerRingRadius+a,includeNorth:v,insideFlush:this.insideLabelsFlush}):void 0,b=y?fs({scale:o,rotation:this.rotation,inside:this.tickmarksInside,innerRadius:this.innerRingRadius+a,includeNorth:v,insideFlush:this.insideLabelsFlush}):A,x=g?this.northMarker?ms({scale:o,rotation:this.rotation}):hs({scale:o,rotation:this.rotation,inside:this.northArrowInside??this.tickmarksInside}):A,S=this.windKnots!=null&&this.windFromDirectionDeg!=null?k`<g transform="scale(${this.scaleWindIcon})">${Gc({windKnots:this.windKnots,fromDirectionDeg:this.windFromDirectionDeg,radius:this.windSymbolRadius??hl,color:this.windColor})}</g>`:A,C=this.current!=null&&this.currentFromDirectionDeg!=null?this.currentIconCentered?qc({current:this.current,fromDirectionDeg:this.currentFromDirectionDeg,scale:this.scaleCurrentIcon,color:this.currentColor}):Kc({current:this.current,fromDirectionDeg:this.currentFromDirectionDeg,radius:this.currentSymbolRadius??ml,color:this.currentColor}):A;return O`
      <svg
        class=${l?`cropped`:A}
        width="100%"
        height="100%"
        viewBox=${i}
        style="--scale: ${o}; transform-origin: ${s}% ${c}%"
        transform="rotate(${this.rotation??0})"
      >
        ${this.watchCircle()} ${this.renderBars()}
        ${this.crosshairEnabled?this.renderCrosshair(184+a,_&&y?{positions:y,rotation:this.rotation,scale:o,innerRingRadius:this.innerRingRadius+a}:void 0,this.crosshairCenterCutout?this.innerRingRadius+a:void 0):A}
        ${x} ${this.renderStarboardPortIndicator()} ${C}
        ${this._renderTickFadeDefs()} ${S}
        ${this.tickFadeAngle>0&&this.areas.length>0?k`<g mask="url(#tickFadeMask)">${p}</g>`:p}
        ${this.areas.length>0?k`<g clip-path="url(#rot-arc-clip)">${this.renderRot()}</g>`:this.renderRot()}
        ${m} ${u}
        ${this.tickFadeAngle>0&&this.areas.length>0?k`<g mask="url(#tickFadeMask)">${b}</g>`:b}
        ${this.renderVesselImage()} ${this.renderNeedles()}
      </svg>
    `}getRotColors(){let e=(this.rotPriority??this.priority)===W.enhanced;if(this.rotPortStarboard){let e;if(this.rotType===Fo.bar){let t=ct(this.rotEndAngle-this.rotStartAngle);e=t<=180?t:t-360}else e=this._effectiveRpm;if(e>0)return{dotColor:`var(--instrument-starboard-secondary-color)`,barBgColor:`var(--instrument-starboard-primary-color)`};if(e<0)return{dotColor:`var(--instrument-port-secondary-color)`,barBgColor:`var(--instrument-port-primary-color)`}}return{dotColor:e?`var(--instrument-enhanced-tertiary-color)`:`var(--instrument-regular-tertiary-color)`,barBgColor:e?`var(--instrument-enhanced-secondary-color)`:`var(--instrument-regular-secondary-color)`}}renderRot(){if(!this.rotType)return A;let{dotColor:e,barBgColor:t}=this.getRotColors(),n=this._rOff;if(this.rotType===Fo.bar){let r=Jo(this.rotStartAngle,this.rotEndAngle),i=Yo(this.rotPosition,n),a=Number.isFinite(this.rotAtZeroDeadband)?this.rotAtZeroDeadband:Uo;return r<Math.max(a,i)?Xo(t,this.rotStartAngle,this.rotPosition,n):k`
        ${Zo({startAngle:this.rotStartAngle,endAngle:this.rotEndAngle,barColor:t,position:this.rotPosition,maskId:`rot-bar-mask`,radiusOffset:n})}
        ${k`<g clip-path="url(#rot-bar-mask)">
            <g id="rot-spinner">
              ${Qo(e,this.rotPosition,n)}
            </g>
          </g>`}
      `}let r=(this.rotPriority??this.priority)===W.enhanced?`var(--instrument-enhanced-secondary-color)`:`var(--instrument-regular-secondary-color)`;return this.rotPortStarboard&&(this._effectiveRpm>0?r=`var(--instrument-starboard-secondary-color)`:this._effectiveRpm<0&&(r=`var(--instrument-port-secondary-color)`)),k`
      <g id="rot-spinner">
        ${Ko(r,this.rotPosition,n)}
      </g>
    `}renderSetpoint(){if(this.angleSetpoint===void 0)return A;let{visualState:e,colorMode:t,disabled:n,hasNewSetpoint:r}=Pi({state:this.state,priority:this.priority,atSetpoint:this.atAngleSetpoint,angleSetpoint:this.angleSetpoint,setpointAtZeroDeadband:this.angleSetpointAtZeroDeadband,newAngleSetpoint:this.newAngleSetpoint,touching:this.touching,setpointOverride:this.setpointOverride}),i=ji(e),a=168+this._rOff+i-fl,o=r?.75:1,s=Ni({visualState:e,colorMode:t,disabled:n,id:this._setpointId}),c=this.animateSetpoint,l=this._departingNewAngleSetpoint!==void 0,u=this.angleSetpoint+90;this._setpointCssAngleInit?this._setpointCssAngle=Ei(this._setpointCssAngle,u):(this._setpointCssAngle=u,this._setpointCssAngleInit=!0);let d=c?k`
        <g style="transform: rotate(${this._setpointCssAngle}deg) translateX(${-a}px) rotate(270deg); opacity: ${o}; transition: transform var(${Ci}, ${wi}) ease-out, opacity var(${Ci}, ${wi}) ease-out;">
          ${s}
        </g>
      `:k`
        <g transform="rotate(${this.angleSetpoint+90}) translate(${-a}, 0) rotate(270)" opacity="${o}">
          ${s}
        </g>
      `;if(r||l){let e=r,n=e?this.newAngleSetpoint:this._departingNewAngleSetpoint,i=+!!e,a=ji(yi.focus),o=168+this._rOff+a-fl,s=Ni({visualState:yi.focus,colorMode:t,disabled:!1,id:this._newSetpointId});if(c){let e=`var(${Ci}, ${wi})`;return k`
          ${d}
          <g style="transform: rotate(${n+90}deg) translateX(${-o}px) rotate(270deg); opacity: ${i}; transition: opacity ${e} ease-out;">
            ${s}
          </g>
        `}return k`
        ${d}
        <g transform="rotate(${n+90}) translate(${-o}, 0) rotate(270)" opacity="${i}">
          ${s}
        </g>
      `}return d}renderVesselImage(){return this.vessels.length===0?A:this.vessels.map(e=>{let t;switch(e.size){case Co.large:t=224;break;case Co.medium:t=160;break;default:t=100}let n=t/160;return k`<g style="transform: ${e.transform} scale(${n}) translate(-80px, -80px) ">${To[e.vesselImage]}</g>`})}renderStarboardPortIndicator(){return this.starboardPortIndicator?[No(0,180,`var(--instrument-starboard-secondary-color)`,`var(--instrument-starboard-secondary-color)`),No(180,360,`var(--instrument-port-secondary-color)`,`var(--instrument-port-secondary-color)`)]:A}},al.styles=a(cs),al);N([P({type:String})],K.prototype,`state`,void 0),N([P({type:String})],K.prototype,`priority`,void 0),N([P({type:String})],K.prototype,`watchCircleType`,void 0),N([P({type:Boolean})],K.prototype,`hasBackgroundCircle`,void 0),N([P({type:Boolean})],K.prototype,`northArrow`,void 0),N([P({type:Boolean})],K.prototype,`northArrowInside`,void 0),N([P({type:Boolean})],K.prototype,`northMarker`,void 0),N([P({type:Number})],K.prototype,`angleSetpoint`,void 0),N([P({type:Number})],K.prototype,`newAngleSetpoint`,void 0),N([P({type:Boolean})],K.prototype,`atAngleSetpoint`,void 0),N([P({type:Number})],K.prototype,`angleSetpointAtZeroDeadband`,void 0),N([P({type:Boolean})],K.prototype,`setpointOverride`,void 0),N([P({type:Boolean})],K.prototype,`touching`,void 0),N([P({type:Boolean})],K.prototype,`animateSetpoint`,void 0),N([ze()],K.prototype,`_departingNewAngleSetpoint`,void 0),N([P({type:Number})],K.prototype,`padding`,void 0),N([P({type:Number,attribute:`face-diameter`})],K.prototype,`faceDiameter`,void 0),N([P({type:Array,attribute:!1})],K.prototype,`areas`,void 0),N([P({type:Array,attribute:!1})],K.prototype,`barAreas`,void 0),N([P({type:Boolean})],K.prototype,`roundBandCuts`,void 0),N([P({type:Boolean})],K.prototype,`splitBand`,void 0),N([P({type:Array,attribute:!1})],K.prototype,`needles`,void 0),N([P({type:Array,attribute:!1})],K.prototype,`tickmarks`,void 0),N([P({type:Boolean})],K.prototype,`tickmarksInside`,void 0),N([P({type:String})],K.prototype,`tickmarkStyle`,void 0),N([P({type:Array,attribute:!1})],K.prototype,`advices`,void 0),N([P({type:Boolean})],K.prototype,`crosshairEnabled`,void 0),N([P({type:Boolean})],K.prototype,`crosshairCenterCutout`,void 0),N([P({type:Boolean})],K.prototype,`showLabels`,void 0),N([P({type:Boolean})],K.prototype,`insideLabelsFlush`,void 0),N([P({type:Array,attribute:!1})],K.prototype,`vessels`,void 0),N([P({type:Number})],K.prototype,`windKnots`,void 0),N([P({type:Number})],K.prototype,`windFromDirectionDeg`,void 0),N([P({type:Number})],K.prototype,`windSymbolRadius`,void 0),N([P({type:String})],K.prototype,`windColor`,void 0),N([P({type:Number})],K.prototype,`current`,void 0),N([P({type:Number})],K.prototype,`currentFromDirectionDeg`,void 0),N([P({type:Number})],K.prototype,`currentSymbolRadius`,void 0),N([P({type:String})],K.prototype,`currentColor`,void 0),N([P({type:Boolean})],K.prototype,`currentIconCentered`,void 0),N([P({type:Number})],K.prototype,`scaleCurrentIcon`,void 0),N([P({type:Boolean})],K.prototype,`starboardPortIndicator`,void 0),N([P({type:Number})],K.prototype,`clipTop`,void 0),N([P({type:Number})],K.prototype,`clipBottom`,void 0),N([P({type:Number})],K.prototype,`clipLeft`,void 0),N([P({type:Number})],K.prototype,`clipRight`,void 0),N([P({type:Boolean})],K.prototype,`endLabelsMaxMin`,void 0),N([P({type:Number})],K.prototype,`scaleWindIcon`,void 0),N([P({type:Number})],K.prototype,`rotation`,void 0),N([P({type:Boolean})],K.prototype,`zoomToFitArc`,void 0),N([P({attribute:!1})],K.prototype,`arcFrame`,void 0),N([P({type:Number})],K.prototype,`tickFadeAngle`,void 0),N([P({type:String})],K.prototype,`rotType`,void 0),N([P({type:String})],K.prototype,`rotPosition`,void 0),N([P({type:Number})],K.prototype,`rotStartAngle`,void 0),N([P({type:Number})],K.prototype,`rotEndAngle`,void 0),N([P({type:String})],K.prototype,`rotPriority`,void 0),N([P({type:Boolean})],K.prototype,`rotPortStarboard`,void 0),N([P({type:Number})],K.prototype,`rotAtZeroDeadband`,void 0),N([P({type:Number})],K.prototype,`rateOfTurnDegreesPerMinute`,void 0),N([P({type:Number})],K.prototype,`rotDotAnimationFactor`,void 0),N([P({type:Number})],K.prototype,`rotationsPerMinute`,null),K=N([M(`obc-watch`)],K);var gl=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M20.2768 19.5526C20.6093 20.2175 20.1258 20.9998 19.3824 20.9998H4.61848C3.8751 20.9998 3.3916 20.2175 3.72405 19.5526L11.106 4.78863C11.1521 4.69649 11.2088 4.61588 11.2736 4.54678C11.7268 4.06309 12.5724 4.14371 12.8949 4.78863L20.2768 19.5526ZM11.4421 8.58867L6.23651 18.9998H16.6476L11.4421 8.58867Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M20.2768 19.5526C20.6093 20.2175 20.1258 20.9998 19.3824 20.9998H4.61848C3.8751 20.9998 3.3916 20.2175 3.72405 19.5526L11.106 4.78863C11.1521 4.69649 11.2088 4.61588 11.2736 4.54678C11.7268 4.06309 12.5724 4.14371 12.8949 4.78863L20.2768 19.5526ZM11.4421 8.58867L6.23651 18.9998H16.6476L11.4421 8.58867Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},_l=(gl.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,gl);N([P({type:Boolean})],_l.prototype,`useCssColor`,void 0),_l=N([M(`obi-delta`)],_l);var vl=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M2.47717 12.8113C2.30349 12.516 2.21665 12.3684 2.18269 12.2111C2.15265 12.072 2.15265 11.9281 2.18269 11.7889C2.21665 11.6317 2.30349 11.484 2.47717 11.1888L6.536 4.28877C6.7051 4.00128 6.78966 3.85754 6.90703 3.75306C7.01089 3.66061 7.13288 3.59084 7.26522 3.54819C7.41479 3.5 7.58155 3.5 7.91509 3.5L16.0849 3.5C16.4184 3.5 16.5852 3.5 16.7347 3.54819C16.8671 3.59084 16.9891 3.66061 17.0929 3.75306C17.2103 3.85754 17.2948 4.00128 17.464 4.28877L21.5228 11.1888C21.6965 11.484 21.7833 11.6317 21.8173 11.7889C21.8473 11.9281 21.8473 12.072 21.8173 12.2111C21.7833 12.3684 21.6965 12.516 21.5228 12.8113L17.464 19.7112C17.2948 19.9987 17.2103 20.1425 17.0929 20.2469C16.9891 20.3394 16.8671 20.4092 16.7347 20.4518C16.5852 20.5 16.4184 20.5 16.0849 20.5H7.91509C7.58155 20.5 7.41479 20.5 7.26522 20.4518C7.13288 20.4092 7.01089 20.3394 6.90703 20.2469C6.78966 20.1425 6.7051 19.9987 6.53599 19.7112L2.47717 12.8113Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M2.47717 12.8113C2.30349 12.516 2.21665 12.3684 2.18269 12.2111C2.15265 12.072 2.15265 11.9281 2.18269 11.7889C2.21665 11.6317 2.30349 11.484 2.47717 11.1888L6.536 4.28877C6.7051 4.00128 6.78966 3.85754 6.90703 3.75306C7.01089 3.66061 7.13288 3.59084 7.26522 3.54819C7.41479 3.5 7.58155 3.5 7.91509 3.5L16.0849 3.5C16.4184 3.5 16.5852 3.5 16.7347 3.54819C16.8671 3.59084 16.9891 3.66061 17.0929 3.75306C17.2103 3.85754 17.2948 4.00128 17.464 4.28877L21.5228 11.1888C21.6965 11.484 21.7833 11.6317 21.8173 11.7889C21.8473 11.9281 21.8473 12.072 21.8173 12.2111C21.7833 12.3684 21.6965 12.516 21.5228 12.8113L17.464 19.7112C17.2948 19.9987 17.2103 20.1425 17.0929 20.2469C16.9891 20.3394 16.8671 20.4092 16.7347 20.4518C16.5852 20.5 16.4184 20.5 16.0849 20.5H7.91509C7.58155 20.5 7.41479 20.5 7.26522 20.4518C7.13288 20.4092 7.01089 20.3394 6.90703 20.2469C6.78966 20.1425 6.7051 19.9987 6.53599 19.7112L2.47717 12.8113Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},yl=(vl.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,vl);N([P({type:Boolean})],yl.prototype,`useCssColor`,void 0),yl=N([M(`obi-critical-badge`)],yl);var bl={[V.Fast]:400,[V.Slow]:400,[V.VerySlow]:400},xl={[V.Fast]:400,[V.Slow]:1200,[V.VerySlow]:2800};V.Fast,V.Slow,V.VerySlow;function Sl(e){return bl[e]+xl[e]}function Cl(e,t){return`--flash-${e}-${t}`}function wl(e,t){let n=Cl(t,`on`),r=Cl(t,`off`),i=Sl(t),a=[{[n]:1,[r]:0,easing:`step-end`},{[n]:0,[r]:1,offset:bl[t]/i,easing:`step-end`},{[n]:0,[r]:1}],o=e.animate(a,{duration:i,iterations:1/0});return o.startTime=0,()=>o.cancel()}var Tl=class{constructor(e,t){this.host=e,this.resolve=t,e.addController(this)}get tempo(){return this.installed}hostConnected(){this.host.hasUpdated&&this.sync()}hostUpdated(){this.sync()}hostDisconnected(){this.stop()}sync(){let e=this.host.isConnected?this.resolve():V.Fixed;if(e===V.Fixed){this.stop();return}e!==this.installed&&(this.stop(),this.cancel=wl(this.host,e),this.installed=e)}stop(){this.cancel?.(),this.cancel=void 0,this.installed=void 0}},El=o`* {
  -webkit-tap-highlight-color: transparent;
}

:host {
  position: absolute;
  inset: 0;
}

:host([wrapcontent]) {
  position: unset;
  width: fit-content;
  height: fit-content;
}

:host([fullwidth]) {
  display: block;
  width: 100%;
}

.wrapper {
  --bg-color: var(--alert-alarm-color);
  --thickness: var(--global-size-spacing-border-weight-alertframe);
  /* 0/1 from the flash-<tempo> classes below; steady when no class applies. */
  --blink-on: 0;
  --blink-off: 1;
  color: var(--on-alarm-active-color);
  position: relative;
  width: 100%;
  height: 100%;
  /* The stroke's centreline follows this radius, like a Figma centre stroke. */
  border-radius: var(--ui-components-button-border-radius);
  outline: var(--thickness) solid var(--bg-color);
  /* Centre stroke: frames on touching components share one edge. */
  outline-offset: calc(-1 * var(--thickness) / 2);
  /* +2 px while on, 1 px each side, both thicknesses (Figma Flash=yes: 2 → 4 px). */
  --blink-width: 2px;
}

.wrapper.thickness-small {
    --thickness: 2px;
  }

.wrapper.wrap-content {
    width: fit-content;
    height: fit-content;
  }

.wrapper.full-width {
    width: 100%;
  }

.wrapper.flash-fast {
    --blink-on: var(--flash-fast-on);
    --blink-off: var(--flash-fast-off);
  }

.wrapper.flash-slow {
    --blink-on: var(--flash-slow-on);
    --blink-off: var(--flash-slow-off);
  }

.wrapper.flash-very-slow {
    --blink-on: var(--flash-very-slow-on);
    --blink-off: var(--flash-very-slow-off);
  }

.wrapper {

  --flash-transition: 50ms linear;
}

.wrapper.flash-effect-outline-eased {
    transition:
      outline-width var(--flash-transition),
      outline-offset var(--flash-transition);
  }

.wrapper.flash-effect-outline-eased .flap {
      transition: box-shadow var(--flash-transition);
    }

.wrapper.flash-effect-outline-eased .mask {
      transition:
        top var(--flash-transition),
        bottom var(--flash-transition),
        left var(--flash-transition),
        right var(--flash-transition);
    }

.wrapper.flash-effect-outline-eased .dash path {
      transition: stroke-width var(--flash-transition);
    }

.wrapper {

  --blink-width-dynamic: calc(var(--blink-width) * var(--blink-on));
  /* One knob for flap and masks, so they cannot drift apart from the outline. */
  --flap-grow: 0px;
}

.wrapper.unacked-active,.wrapper.unacked-rectified {
    outline-width: calc(var(--thickness) + var(--blink-width-dynamic));
    outline-offset: calc(
      -1 * (var(--thickness) + var(--blink-width-dynamic)) / 2
    );
    /* The stroke grows on both sides, so its outer edge moves by half. */
    --flap-grow: calc(var(--blink-width-dynamic) / 2);
  }

.wrapper.unacked-rectified {
    /* The dash pattern (12/6) needs an SVG stroke; outlines have no dash array. */
    outline-style: none;
  }

.wrapper.alarm,.wrapper.level-high {
    --bg-color: var(--alert-alarm-color);
    color: var(--on-alarm-active-color);
  }

.wrapper.warning,.wrapper.level-medium {
    --bg-color: var(--alert-warning-color);
    color: var(--on-warning-active-color);
  }

.wrapper.caution,.wrapper.level-low {
    --bg-color: var(--alert-caution-color);
    color: var(--on-caution-active-color);
  }

.wrapper.level-critical {
    --bg-color: var(--critical-enabled-background-color);
    color: var(--on-critical-active-color);
  }

.wrapper.level-diagnostic {
    --bg-color: var(--notification-enabled-background-color);
    color: var(--on-notification-active-color);
  }

.wrapper.sharp-edge-top-left {
    border-top-left-radius: 0;
  }

.wrapper.sharp-edge-top-right {
    border-top-right-radius: 0;
  }

.wrapper.sharp-edge-bottom-left {
    border-bottom-left-radius: 0;
  }

.wrapper.sharp-edge-bottom-right {
    border-bottom-right-radius: 0;
  }

.flap {
  position: absolute;
  background-color: var(--bg-color);
  border-radius: 0px var(--app-components-alert-frame-small-flip-border-radius)
    var(--app-components-alert-frame-small-flip-border-radius) 0px;
  padding: var(--ui-components-badge-padding);

  display: flex;
  gap: 2px;
}

.flap.small {
    top: calc(-1 * var(--thickness) / 2);
    right: calc(
      -1 * var(--app-components-alert-frame-icon-size) -
        var(--ui-components-badge-padding) * 2
    );
  }

.flap .mask {
    position: absolute;
    width: var(--ui-components-button-border-radius);
    height: var(--ui-components-button-border-radius);
    background-color: var(--bg-color);
  }

.up:is(.flap .mask) {
      width: calc(
        var(--ui-components-button-border-radius) + var(--thickness) + 0.5px
      );
      top: calc(-1 * var(--flap-grow));
      left: calc(
        -1 * var(--ui-components-button-border-radius) - var(--thickness)
      );
      clip-path: polygon(
        0 0,
        100% 0,
        100% 100%,
        calc(100% - var(--thickness)) 50%,
        50% var(--thickness)
      );
    }

.down:is(.flap .mask) {
      width: calc(
        var(--ui-components-button-border-radius) + var(--thickness) + 0.5px
      );
      bottom: calc(-1 * var(--flap-grow));
      left: calc(
        -1 * var(--ui-components-button-border-radius) - var(--thickness)
      );
      clip-path: polygon(
        0 100%,
        100% 100%,
        100% 0,
        50% calc(100% - var(--thickness)),
        calc(100% - var(--thickness)) 50%
      );
    }

.left:is(.flap .mask) {
      height: calc(
        var(--ui-components-button-border-radius) + var(--thickness) + 0.5px
      );
      top: calc(
        -1 * var(--ui-components-button-border-radius) - var(--thickness)
      );
      left: calc(-1 * var(--flap-grow));
      clip-path: polygon(
        0 0,
        0 100%,
        100% 100%,
        50% calc(100% - var(--thickness)),
        var(--thickness) 50%
      );
    }

.top .left:is(.flap .mask) {
        top: unset;
        bottom: calc(
          -1 * var(--ui-components-button-border-radius) - var(--thickness)
        );
        clip-path: polygon(
          0 100%,
          0 0,
          100% 0,
          50% var(--thickness),
          var(--thickness) 50%
        );
      }

.right:is(.flap .mask) {
      height: calc(
        var(--ui-components-button-border-radius) + var(--thickness) + 0.5px
      );
      top: calc(
        -1 * var(--ui-components-button-border-radius) - var(--thickness)
      );
      right: calc(-1 * var(--flap-grow));
      clip-path: polygon(
        100% 0,
        100% 100%,
        0 100%,
        50% calc(100% - var(--thickness)),
        calc(100% - var(--thickness)) 50%
      );
    }

.top .right:is(.flap .mask) {
        top: unset;
        bottom: calc(
          -1 * var(--ui-components-button-border-radius) - var(--thickness)
        );
        clip-path: polygon(
          100% 100%,
          100% 0,
          0 0,
          50% var(--thickness),
          calc(100% - var(--thickness)) 50%
        );
      }

.flap.large {
    flex-direction: column;
    top: calc(-1 * var(--thickness) / 2);
    bottom: calc(-1 * var(--thickness) / 2);
    right: calc(
      -1 * var(--app-components-alert-frame-icon-size) + var(--thickness) -
        var(--ui-components-badge-padding) * 2
    );
    border-radius: 0px
      var(--app-components-alert-frame-large-flip-border-radius)
      var(--app-components-alert-frame-large-flip-border-radius) 0px;
  }

.flap.bottom,.flap.top {
    left: calc(-1 * var(--thickness) / 2);
    right: calc(-1 * var(--thickness) / 2);
    padding: var(--app-components-alert-frame-large-flip-padding-vertical)
      var(--app-components-alert-frame-large-flip-4px-padding-horizontal);
    bottom: calc(
      -1 * var(--global-typography-ui-label-line-height) -
        var(--app-components-alert-frame-large-flip-padding-vertical) * 2
    );
    border-radius: 0px 0px var(--button-border-radius-bottom-right)
      var(--button-border-radius-bottom-right);
    align-items: center;

    font-family: var(--global-typography-font-family);

    font-weight: var(--global-typography-ui-label-font-weight);

    font-size: var(--global-typography-ui-label-font-size);

    line-height: var(--global-typography-ui-label-line-height);

    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    font-weight: var(--font-weight-regular);
  }

:is(.flap.bottom,.flap.top) .spacer {
      flex: 1;
    }

.text-size-large :is(.flap.bottom,.flap.top) {
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-body-font-weight);
      font-size: var(--global-typography-ui-body-font-size);
      line-height: var(--global-typography-ui-body-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
      bottom: calc(
        var(--thickness) - var(--global-typography-ui-body-line-height) -
          var(--app-components-alert-frame-large-flip-padding-vertical) * 2
      );
    }

:is(.text-size-large :is(.flap.bottom,.flap.top)) .label {
        font-family: var(--global-typography-font-family);
        font-weight: var(--global-typography-ui-body-active-font-weight);
        font-size: var(--global-typography-ui-body-active-font-size);
        line-height: var(--global-typography-ui-body-active-line-height);
        font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
      }

.flap.top {
    bottom: unset !important;
    top: calc(
      -1 * var(--global-typography-ui-label-line-height) -
        var(--app-components-alert-frame-large-flip-padding-vertical) * 2
    );
    border-radius: var(--button-border-radius-bottom-right)
      var(--button-border-radius-bottom-right) 0px 0px;
  }

.text-size-large .flap.top {
      top: calc(
        var(--thickness) - var(--global-typography-ui-body-line-height) -
          var(--app-components-alert-frame-large-flip-padding-vertical) * 2
      );
    }

.flap .label {
    flex-shrink: 1000;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
  }

/* Grows the flap outward with the outline, never toward the content: shifted
   copies leave the inner edge where it is (an outline would cross it). */
.flap.small,
.flap.large {
  box-shadow:
    var(--flap-grow) 0 0 0 var(--bg-color),
    0 calc(-1 * var(--flap-grow)) 0 0 var(--bg-color),
    0 var(--flap-grow) 0 0 var(--bg-color),
    var(--flap-grow) calc(-1 * var(--flap-grow)) 0 0 var(--bg-color),
    var(--flap-grow) var(--flap-grow) 0 0 var(--bg-color);
}

.flap.bottom {
  box-shadow:
    0 var(--flap-grow) 0 0 var(--bg-color),
    calc(-1 * var(--flap-grow)) 0 0 0 var(--bg-color),
    var(--flap-grow) 0 0 0 var(--bg-color),
    calc(-1 * var(--flap-grow)) var(--flap-grow) 0 0 var(--bg-color),
    var(--flap-grow) var(--flap-grow) 0 0 var(--bg-color);
}

.flap.top {
  box-shadow:
    0 calc(-1 * var(--flap-grow)) 0 0 var(--bg-color),
    calc(-1 * var(--flap-grow)) 0 0 0 var(--bg-color),
    var(--flap-grow) 0 0 0 var(--bg-color),
    calc(-1 * var(--flap-grow)) calc(-1 * var(--flap-grow)) 0 0 var(--bg-color),
    var(--flap-grow) calc(-1 * var(--flap-grow)) 0 0 var(--bg-color);
}

::slotted([slot="label"]) {
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}

.icon {
  width: var(--app-components-alert-frame-icon-size);
  height: var(--app-components-alert-frame-icon-size);
  display: block;
  flex-shrink: 0;
}

.dash {
  /* Overridden inline per render from the measured thickness. */
  --dash-pad: 0px;
  position: absolute;
  top: calc(-1 * var(--dash-pad));
  left: calc(-1 * var(--dash-pad));
  overflow: visible;
  pointer-events: none;
  fill: none;
  stroke: var(--bg-color);
  stroke-dasharray: 12 6;
}

.dash path {
  /* Animated on the one path: a wider second path would drift its dashes. */
  stroke-width: calc(var(--thickness) + var(--blink-width-dynamic));
}
`,Dl=class extends j{constructor(...e){super(...e),this.icon=k`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="100" height="100">
  <path d="M 10.5,2 
           L 13.5,2 
           L 13.5,9.4 
           L 19.91,5.7 
           L 21.41,8.3 
           L 15,12 
           L 21.41,15.7 
           L 19.91,18.3 
           L 13.5,14.6 
           L 13.5,22 
           L 10.5,22 
           L 10.5,14.6 
           L 4.09,18.3 
           L 2.59,15.7 
           L 9,12 
           L 2.59,8.3 
           L 4.09,5.7 
           L 10.5,9.4 
           Z" 
        fill="currentColor" />
</svg>

`}render(){return O` <div class="wrapper">${this.icon}</div> `}},Ol=(Dl.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Dl);Ol=N([M(`obi-diagnostic-badge`)],Ol);var kl,Al=function(e){return e.Regular=`regular`,e.SmallSideFlip=`small-side-flip`,e.LargeSideFlip=`large-side-flip`,e.BottomFlip=`bottom-flip`,e.TopFlip=`top-flip`,e}({}),jl=function(e){return e.Small=`small`,e.Large=`large`,e}({}),Ml=function(e){return e.ackedActive=`acked-active`,e.unackedActive=`unacked-active`,e.unackedRectified=`unacked-rectified`,e}({}),Nl=2;function Pl(e,t){return t!==void 0&&e.width===t.width&&e.height===t.height&&e.thickness===t.thickness&&e.radii.every((e,n)=>e===t.radii[n])}var Fl=(kl=class extends j{constructor(...e){super(...e),this.type=`small-side-flip`,this.thickness=`small`,this.status=B.Alarm,this.mode=`acked-active`,this.flashingSpeed=V.Default,this.flashEffect=`outline`,this.flashing=new Tl(this,()=>this.resolvedFlashingSpeed),this.measureDash=()=>{let e=this.wrapper;if(!e)return;let t=getComputedStyle(e),n=e=>parseFloat(e)||0,r={width:e.offsetWidth,height:e.offsetHeight,thickness:n(t.getPropertyValue(`--thickness`)),radii:[n(t.borderTopLeftRadius),n(t.borderTopRightRadius),n(t.borderBottomRightRadius),n(t.borderBottomLeftRadius)]};Pl(r,this.dashBox)||(this.dashBox=r)},this.wrapContent=!1,this.fullWidth=!1,this.sharpEdgeTopLeft=!1,this.sharpEdgeTopRight=!1,this.sharpEdgeBottomLeft=!1,this.sharpEdgeBottomRight=!1,this.textSize=`regular`,this.showIcon=!1,this.showAlertCategoryIcon=!0}connectedCallback(){super.connectedCallback(),this.hasUpdated&&this.requestUpdate()}updated(){let e=this.mode===`unacked-rectified`&&this.isConnected;e&&!this.dashObserver&&this.wrapper&&(this.dashObserver=new ResizeObserver(this.measureDash),this.dashObserver.observe(this.wrapper)),e&&this.measureDash(),!e&&this.dashObserver&&(this.dashObserver.disconnect(),this.dashObserver=void 0,this.dashBox=void 0)}disconnectedCallback(){super.disconnectedCallback(),this.dashObserver?.disconnect(),this.dashObserver=void 0}renderDash(){let e=this.dashBox;if(this.mode!==`unacked-rectified`||!e)return A;let t=(e.thickness+Nl)/2,n={x:t,y:t,width:e.width,height:e.height,radii:e.radii},r=e.width+2*t,i=e.height+2*t;return O`<svg
      class="dash"
      aria-hidden="true"
      width=${r}
      height=${i}
      viewBox="0 0 ${r} ${i}"
      style="--dash-pad: ${t}px"
    >
      <path d=${os(n)}></path>
    </svg>`}get resolvedFlashingSpeed(){switch(this.mode){case`unacked-active`:return Xt(this.flashingSpeed,this.status,Yt.Active);case`unacked-rectified`:return Xt(this.flashingSpeed,this.status,Yt.Rectified);default:return V.Fixed}}render(){return O`
      <div
        class=${F({wrapper:!0,"wrap-content":this.wrapContent,"full-width":this.fullWidth,[`thickness-`+this.thickness]:!0,[this.type]:!0,[this.status]:!0,[`text-size-`+this.textSize]:!0,"sharp-edge-top-left":this.sharpEdgeTopLeft,"sharp-edge-top-right":this.sharpEdgeTopRight,"sharp-edge-bottom-left":this.sharpEdgeBottomLeft,"sharp-edge-bottom-right":this.sharpEdgeBottomRight,[this.mode]:!0,[`flash-`+this.resolvedFlashingSpeed]:!0,[`flash-effect-`+this.flashEffect]:!0})}
      >
        <slot></slot>
        ${this.renderDash()} ${this.flap()}
      </div>
    `}flap(){if(this.type===`regular`||this.type===`small-side-flip`&&!this.showAlertCategoryIcon||this.type===`large-side-flip`&&!this.showIcon&&!this.showAlertCategoryIcon)return A;let e;return e=this.showAlertCategoryIcon?this.renderBadgeIcon():A,this.type===`small-side-flip`?O`<div class="flap small">
        ${e}
        <div class="mask up"></div>
      </div>`:this.type===`large-side-flip`?O`<div class="flap large">
        ${e}
        ${this.showIcon?O`<div class="icon"><slot name="icon"></slot></div>`:A}
        <div class="mask up"></div>
        <div class="mask down"></div>
      </div>`:this.type===`bottom-flip`||this.type===`top-flip`?O`<div
        class="flap ${this.type===`bottom-flip`?`bottom`:`top`}"
      >
        ${e}
        ${this.showIcon?O`<div class="icon"><slot name="icon"></slot></div>`:A}
        <div class="label"><slot name="label"></slot></div>
        <div class="spacer"></div>
        <div class="timer"><slot name="timer"></slot></div>
        <div class="mask right"></div>
        <div class="mask left"></div>
      </div>`:(console.error(`Unknown type of alert frame:`,this.type),A)}renderBadgeIcon(){switch(Zt(this.status)){case Jt.Critical:return O`<obi-critical-badge
          class="icon badge"
        ></obi-critical-badge>`;case Jt.Warning:return O`<obi-warning-badge class="icon badge"></obi-warning-badge>`;case Jt.Caution:return O`<obi-caution-badge class="icon badge"></obi-caution-badge>`;case Jt.Diagnostic:return O`<obi-diagnostic-badge
          class="icon badge"
        ></obi-diagnostic-badge>`;default:return O`<obi-alarm-badge class="icon badge"></obi-alarm-badge>`}}},kl.styles=a(El),kl);N([P({type:String})],Fl.prototype,`type`,void 0),N([P({type:String})],Fl.prototype,`thickness`,void 0),N([P({type:String})],Fl.prototype,`status`,void 0),N([P({type:String})],Fl.prototype,`mode`,void 0),N([P({type:String})],Fl.prototype,`flashingSpeed`,void 0),N([P({type:String})],Fl.prototype,`flashEffect`,void 0),N([ze()],Fl.prototype,`dashBox`,void 0),N([Ve(`.wrapper`)],Fl.prototype,`wrapper`,void 0),N([P({type:Boolean,reflect:!0})],Fl.prototype,`wrapContent`,void 0),N([P({type:Boolean,reflect:!0})],Fl.prototype,`fullWidth`,void 0),N([P({type:Boolean})],Fl.prototype,`sharpEdgeTopLeft`,void 0),N([P({type:Boolean})],Fl.prototype,`sharpEdgeTopRight`,void 0),N([P({type:Boolean})],Fl.prototype,`sharpEdgeBottomLeft`,void 0),N([P({type:Boolean})],Fl.prototype,`sharpEdgeBottomRight`,void 0),N([P({type:String})],Fl.prototype,`textSize`,void 0),N([P({type:Boolean})],Fl.prototype,`showIcon`,void 0),N([P({type:Boolean,attribute:!1})],Fl.prototype,`showAlertCategoryIcon`,void 0),Fl=N([M(`obc-alert-frame`)],Fl);function Il(e,t,n=!1){return typeof e!=`object`||!e?t:O`<obc-alert-frame
    .type=${e.type??`small-side-flip`}
    .thickness=${e.thickness??`small`}
    .status=${e.status??B.Alarm}
    .mode=${e.mode??`acked-active`}
    .flashingSpeed=${e.flashingSpeed??V.Default}
    .showIcon=${e.showIcon??!1}
    .showAlertCategoryIcon=${e.showAlertCategoryIcon??!0}
    .wrapContent=${!0}
    .fullWidth=${n}
    >${t}</obc-alert-frame
  >`}var Ll=o`* {
  -webkit-tap-highlight-color: transparent;
}

:host {
  display: inline-block;
  line-height: 0;
}

.wrapper {
  display: inline-flex;
  flex-direction: column;
  width: fit-content;
  --height: 24px;
  --padding: 4px;
  font-family: var(--font-family-main);
  letter-spacing: var(--global-typography-generic-l-letter-spacing);
}

/* The inner-wrapper is the box: its height (--height) is the full textbox
   height, padding included. The content is sized to the cap height and
   vertically centered, which leaves the padding as equal space above and
   below. In engines that support text-box-trim the content box collapses to
   the cap height exactly; in Firefox (no text-box-trim) the content keeps its
   natural line box, so align-items:center + overflow:hidden crops it to the
   same height instead. No padding here – the centering provides it.
   (A small top padding could be added later to nudge the text up in Firefox.) */
.inner-wrapper {
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: var(--alignment-justify, flex-end);
  height: var(--height);
  overflow: hidden;
  /* Opt-in: animate a \`size\` change (height + font-size below). Defaults to 0s
     (instant, current behavior) so existing usages and snapshots are unchanged;
     a consumer sets \`--obc-textbox-size-transition\` (e.g. 300ms) to animate the
     swap — used by readout-list-item's setpoint flip-flop. */
  transition: height var(--obc-textbox-size-transition, 0s) ease;
}

/* The spacer must share the content's exact font metrics so the width it
   reserves equals the rendered content width. font-size-adjust scales the
   font, so it has to match too. */
.content,
.length-spacer {
  font-size: calc(var(--height) - 2 * var(--padding));
  font-size-adjust: cap-height 1;
  white-space: nowrap;
  /* Opt-in size animation — see \`.inner-wrapper\`. */
  transition: font-size var(--obc-textbox-size-transition, 0s) ease;
}

.content {
  text-box-trim: trim-both;
  text-box-edge: cap alphabetic;
}

/* Opt-in numeric mode: fixed-width lining numerals so values stay
   column-aligned and width-stable. Applied to the spacer too so the reserved
   width matches the rendered digits exactly. */
.wrapper.tabular-nums .content,
.wrapper.tabular-nums .length-spacer {
  font-variant-numeric: tabular-nums lining-nums;
  font-feature-settings:
    "ss04" on,
    "tnum" on,
    "lnum" on;
}

/* Size override is set on \`.wrapper\` (not \`.inner-wrapper\`) so it reaches BOTH
   the visible \`.content\` AND the sibling \`.length-spacer\`; otherwise the spacer
   keeps the default (m) \`--height\` and reserves width at the wrong font size. */
.wrapper.size-xs {
  --height: 16px;
}

.wrapper.size-s {
  --height: 20px;
}

.wrapper.size-m {
  --height: 24px;
}

.wrapper.size-l {
  --height: 32px;
}

.wrapper.size-xl {
  --height: 40px;
}

.wrapper.font-weight-regular {
  font-weight: var(--global-typography-generic-l-font-weight-regular);
}

.wrapper.font-weight-semibold {
  font-weight: var(--global-typography-generic-l-font-weight-medium);
}

.wrapper.font-weight-bold {
  font-weight: var(--global-typography-generic-l-font-weight-bold);
}

.wrapper.alignment-left {
  --alignment-justify: flex-start;
}

.wrapper.alignment-center {
  --alignment-justify: center;
}

.wrapper.alignment-right {
  --alignment-justify: flex-end;
}

/* Reserves the box width from the \`length\` slot without occupying vertical
   space. Acts as a minimum width so the box does not resize as visible
   text changes. */
.length-spacer {
  height: 0;
  opacity: 0;
  visibility: hidden;
  overflow: hidden;
}
`,Rl,zl=function(e){return e.Left=`left`,e.Center=`center`,e.Right=`right`,e}({}),Bl=function(e){return e.xs=`xs`,e.s=`s`,e.m=`m`,e.l=`l`,e.xl=`xl`,e}({}),Vl=function(e){return e.regular=`regular`,e.semibold=`semibold`,e.bold=`bold`,e}({}),Hl=(Rl=class extends j{constructor(...e){super(...e),this.alignment=`right`,this.size=`m`,this.fontWeight=`regular`,this.tabularNums=!1}render(){return O`
      <div
        class=${F({wrapper:!0,[`alignment-${this.alignment}`]:!0,[`size-${this.size}`]:!0,[`font-weight-${this.fontWeight}`]:!0,"tabular-nums":this.tabularNums})}
      >
        <div class="inner-wrapper">
          <div class="content">
            <slot></slot>
          </div>
        </div>
        <div class="length-spacer" aria-hidden="true">
          <slot name="length"></slot>
        </div>
      </div>
    `}},Rl.styles=a(Ll),Rl);N([P({type:String})],Hl.prototype,`alignment`,void 0),N([P({type:String})],Hl.prototype,`size`,void 0),N([P({type:String})],Hl.prototype,`fontWeight`,void 0),N([P({type:Boolean})],Hl.prototype,`tabularNums`,void 0),Hl=N([M(`obc-textbox`)],Hl);var Ul=function(e){return e.number=`number`,e.text=`text`,e}({}),Wl=Object.values(Ul);function Gl(e){return typeof e==`string`&&Wl.includes(e)}function Kl(e){return e==null||Number.isNaN(e)?0:Math.trunc(e)}function ql(e,t){let n=Kl(t);if(!(Number.isFinite(n)&&n>=0&&n<=100))throw RangeError(`<${e}>: fractionDigits must be between 0 and 100 (got ${String(t)}).`)}function Jl(e){let t=Math.trunc(e??0);return Number.isNaN(t)||t<=0?0:Math.min(t,100)}function Yl(e){return e==null||Number.isNaN(e)}function Xl(e){return e.trim()===``}function Zl(e,t,n){let r=n??`number`;if(!Gl(r))throw TypeError(`<${e}>: valueType must be ${Wl.map(e=>`"${e}"`).join(` or `)} (got ${JSON.stringify(n)}).`);if(!(r!==`number`||typeof t!=`string`||Xl(t))&&!Number.isFinite(Number(t)))throw TypeError(`<${e}>: value must be a number when valueType is "number" (got ${JSON.stringify(t)}). Set valueType="text" to render text.`)}function Ql(e,t){if(t===`text`||e==null)return;if(typeof e==`number`)return Number.isFinite(e)?e:void 0;if(Xl(e))return;let n=Number(e);return Number.isFinite(n)?n:void 0}function $l(e,t){if(t!==`text`||e==null)return;let n=typeof e==`number`?String(e):e;return Xl(n)?void 0:n}function eu({showZeroPadding:e,minValueLength:t,fractionDigits:n}){let r=e?Math.max(t,1):1,i=Number.isNaN(n)?0:n;return i<1?`‒`.repeat(r):`‒`.repeat(r)+`.`+`‒`.repeat(i)}function tu(e,t){return e===void 0||!Number.isFinite(e)||Number.isNaN(t.fractionDigits)?eu(t):e.toFixed(t.fractionDigits)}function nu(e){let t=e.trim();if(!t)return 0;let n=t.startsWith(`-`)?t.slice(1):t,r=n.indexOf(`.`);return r===-1?n.length:r}function ru(e,t){if(!/\d/.test(e))return{sign:``,hinted:``,magnitude:e};let n=e.startsWith(`-`),r=n?e.slice(1):e,i=Math.max(t-nu(r),0);return{sign:n?`-`:``,hinted:i>0?`0`.repeat(i):``,magnitude:r}}var iu=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M11.5586 1.76758C11.7461 1.41138 12.2559 1.41137 12.4434 1.76758L22.4414 20.7666C22.6167 21.0998 22.3748 21.4998 21.999 21.5H2.00098C1.62518 21.4998 1.38327 21.0998 1.55859 20.7666L11.5586 1.76758Z" fill="currentColor" stroke="currentColor"/>
<path d="M7.5 15.7V13.3C7.5 13.02 7.5 12.88 7.5545 12.7731C7.60243 12.679 7.67892 12.6025 7.773 12.5545C7.87996 12.5 8.01997 12.5 8.3 12.5H10.6686C10.7909 12.5 10.8521 12.5 10.9096 12.4862C10.9606 12.474 11.0094 12.4538 11.0541 12.4264C11.1046 12.3954 11.1478 12.3522 11.2343 12.2657L13.6343 9.86573C14.0627 9.43736 14.2769 9.22317 14.4608 9.2087C14.6203 9.19614 14.7763 9.26073 14.8802 9.38243C15 9.5227 15 9.8256 15 10.4314V18.5687C15 19.1745 15 19.4774 14.8802 19.6177C14.7763 19.7394 14.6203 19.804 14.4608 19.7914C14.2769 19.7769 14.0627 19.5627 13.6343 19.1344L11.2343 16.7344C11.1478 16.6479 11.1046 16.6047 11.0541 16.5737C11.0094 16.5463 10.9606 16.5261 10.9096 16.5139C10.8521 16.5 10.7909 16.5 10.6686 16.5H8.3C8.01997 16.5 7.87996 16.5 7.773 16.4456C7.67892 16.3976 7.60243 16.3211 7.5545 16.227C7.5 16.1201 7.5 15.9801 7.5 15.7Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M11.5586 1.76758C11.7461 1.41138 12.2559 1.41137 12.4434 1.76758L22.4414 20.7666C22.6167 21.0998 22.3748 21.4998 21.999 21.5H2.00098C1.62518 21.4998 1.38327 21.0998 1.55859 20.7666L11.5586 1.76758Z" style="fill: var(--alert-alarm-color); stroke: var(--alert-alarm-outline-color)"/>
<path d="M7.5 15.7V13.3C7.5 13.02 7.5 12.88 7.5545 12.7731C7.60243 12.679 7.67892 12.6025 7.773 12.5545C7.87996 12.5 8.01997 12.5 8.3 12.5H10.6686C10.7909 12.5 10.8521 12.5 10.9096 12.4862C10.9606 12.474 11.0094 12.4538 11.0541 12.4264C11.1046 12.3954 11.1478 12.3522 11.2343 12.2657L13.6343 9.86573C14.0627 9.43736 14.2769 9.22317 14.4608 9.2087C14.6203 9.19614 14.7763 9.26073 14.8802 9.38243C15 9.5227 15 9.8256 15 10.4314V18.5687C15 19.1745 15 19.4774 14.8802 19.6177C14.7763 19.7394 14.6203 19.804 14.4608 19.7914C14.2769 19.7769 14.0627 19.5627 13.6343 19.1344L11.2343 16.7344C11.1478 16.6479 11.1046 16.6047 11.0541 16.5737C11.0094 16.5463 10.9606 16.5261 10.9096 16.5139C10.8521 16.5 10.7909 16.5 10.6686 16.5H8.3C8.01997 16.5 7.87996 16.5 7.773 16.4456C7.67892 16.3976 7.60243 16.3211 7.5545 16.227C7.5 16.1201 7.5 15.9801 7.5 15.7Z" style="fill: var(--on-alarm-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},au=(iu.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,iu);N([P({type:Boolean})],au.prototype,`useCssColor`,void 0),au=N([M(`obi-alarm-unacknowledged-iec`)],au);var ou=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M20.3426 20L12.0005 4.14753L3.65752 20L20.3426 20ZM11.1158 1.53427L1.11648 20.5339C0.765943 21.1999 1.24879 22 2.00128 22L21.9987 22C22.7512 22 23.234 21.1999 22.8835 20.5339L12.8854 1.53432C12.5105 0.821913 11.4907 0.821889 11.1158 1.53427Z" fill="currentColor"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M10.9995 8.99999H12.9995V14H10.9995V8.99999ZM12.9995 16V18H10.9995V16H12.9995Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M20.3426 20L12.0005 4.14753L3.65752 20L20.3426 20ZM11.1158 1.53427L1.11648 20.5339C0.765943 21.1999 1.24879 22 2.00128 22L21.9987 22C22.7512 22 23.234 21.1999 22.8835 20.5339L12.8854 1.53432C12.5105 0.821913 11.4907 0.821889 11.1158 1.53427Z" style="fill: var(--element-active-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M10.9995 8.99999H12.9995V14H10.9995V8.99999ZM12.9995 16V18H10.9995V16H12.9995Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},su=(ou.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,ou);N([P({type:Boolean})],su.prototype,`useCssColor`,void 0),su=N([M(`obi-alarm`)],su);var cu=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M4 2C2.89543 2 2 2.89543 2 4V20C2 21.1046 2.89543 22 4 22H20C21.1046 22 22 21.1046 22 20V4C22 2.89543 21.1046 2 20 2H4Z" fill="currentColor"/>
<path d="M4 2.5H20C20.8284 2.5 21.5 3.17157 21.5 4V20C21.5 20.8284 20.8284 21.5 20 21.5H4C3.17157 21.5 2.5 20.8284 2.5 20V4C2.5 3.17157 3.17157 2.5 4 2.5Z" stroke="currentColor"/>
<path d="M11 14V6H13V14H11Z" fill="currentColor"/>
<path d="M13 16H11V18H13V16Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M4 2C2.89543 2 2 2.89543 2 4V20C2 21.1046 2.89543 22 4 22H20C21.1046 22 22 21.1046 22 20V4C22 2.89543 21.1046 2 20 2H4Z" style="fill: var(--alert-caution-color)"/>
<path d="M4 2.5H20C20.8284 2.5 21.5 3.17157 21.5 4V20C21.5 20.8284 20.8284 21.5 20 21.5H4C3.17157 21.5 2.5 20.8284 2.5 20V4C2.5 3.17157 3.17157 2.5 4 2.5Z" style="stroke: var(--alert-caution-outline-color)"/>
<path d="M11 14V6H13V14H11Z" style="fill: var(--on-caution-active-color)"/>
<path d="M13 16H11V18H13V16Z" style="fill: var(--on-caution-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},lu=(cu.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,cu);N([P({type:Boolean})],lu.prototype,`useCssColor`,void 0),lu=N([M(`obi-caution-color-iec`)],lu);var uu=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M4 4V20H20V4L4 4ZM2 4C2 2.89543 2.89543 2 4 2H20C21.1046 2 22 2.89543 22 4V20C22 21.1046 21.1046 22 20 22H4C2.89543 22 2 21.1046 2 20V4Z" fill="currentColor"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M11 6H13V14H11V6ZM13 16V18H11V16H13Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M4 4V20H20V4L4 4ZM2 4C2 2.89543 2.89543 2 4 2H20C21.1046 2 22 2.89543 22 4V20C22 21.1046 21.1046 22 20 22H4C2.89543 22 2 21.1046 2 20V4Z" style="fill: var(--element-active-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M11 6H13V14H11V6ZM13 16V18H11V16H13Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},du=(uu.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,uu);N([P({type:Boolean})],du.prototype,`useCssColor`,void 0),du=N([M(`obi-caution-google`)],du);var fu=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M7 7.20382C7 6.21532 8.17595 5.65107 9 6.24417L16.2777 11.1724C16.8633 11.5689 16.8634 12.4315 16.2779 12.8282L9 17.76C8.17595 18.3531 7 17.7888 7 16.8003L7 7.20382Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M7 7.20382C7 6.21532 8.17595 5.65107 9 6.24417L16.2777 11.1724C16.8633 11.5689 16.8634 12.4315 16.2779 12.8282L9 17.76C8.17595 18.3531 7 17.7888 7 16.8003L7 7.20382Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},pu=(fu.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,fu);N([P({type:Boolean})],pu.prototype,`useCssColor`,void 0),pu=N([M(`obi-input-right`)],pu);var mu=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M4 19C2.89543 19 2 18.1046 2 17V5C2 3.89543 2.89543 3 4 3H20C21.1046 3 22 3.89543 22 5V17C22 18.1046 21.1046 19 20 19H15L12 22L9 19H4ZM11.9999 13.5759L9.32009 15.1495C8.93971 15.3728 8.47753 15.03 8.58083 14.6012L9.28416 11.6815L6.93972 9.7184C6.5962 9.43075 6.77528 8.87125 7.22199 8.83654L10.3263 8.59537L11.5414 5.80017C11.7157 5.39929 12.2842 5.39929 12.4585 5.80017L13.6736 8.59537L16.7779 8.83654C17.2246 8.87125 17.4037 9.43075 17.0602 9.7184L14.7157 11.6815L15.4191 14.6012C15.5224 15.03 15.0602 15.3728 14.6798 15.1495L11.9999 13.5759Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M4 19C2.89543 19 2 18.1046 2 17V5C2 3.89543 2.89543 3 4 3H20C21.1046 3 22 3.89543 22 5V17C22 18.1046 21.1046 19 20 19H15L12 22L9 19H4ZM11.9999 13.5759L9.32009 15.1495C8.93971 15.3728 8.47753 15.03 8.58083 14.6012L9.28416 11.6815L6.93972 9.7184C6.5962 9.43075 6.77528 8.87125 7.22199 8.83654L10.3263 8.59537L11.5414 5.80017C11.7157 5.39929 12.2842 5.39929 12.4585 5.80017L13.6736 8.59537L16.7779 8.83654C17.2246 8.87125 17.4037 9.43075 17.0602 9.7184L14.7157 11.6815L15.4191 14.6012C15.5224 15.03 15.0602 15.3728 14.6798 15.1495L11.9999 13.5759Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},hu=(mu.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,mu);N([P({type:Boolean})],hu.prototype,`useCssColor`,void 0),hu=N([M(`obi-notification-advice-active`)],hu);var gu=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M9 19L12 22L15 19H20C21.1046 19 22 18.1046 22 17V5C22 3.89543 21.1046 3 20 3H4C2.89543 3 2 3.89543 2 5V17C2 18.1046 2.89543 19 4 19H9ZM12 19.1716L14.1716 17H20V5H4L4 17H9.82843L12 19.1716Z" fill="currentColor"/>
<path d="M9.73374 14.6603L11.9999 13.3297L14.2661 14.6603C14.5878 14.8492 14.9786 14.5593 14.8912 14.1967L14.2965 11.7277L16.279 10.0676C16.5695 9.82438 16.4181 9.35125 16.0403 9.32191L13.4152 9.11796L12.3877 6.75425C12.2403 6.41525 11.7595 6.41525 11.6122 6.75425L10.5846 9.11796L7.95951 9.32191C7.58176 9.35125 7.43032 9.82438 7.72082 10.0676L9.70335 11.7277L9.10859 14.1967C9.02124 14.5593 9.41208 14.8492 9.73374 14.6603Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M9 19L12 22L15 19H20C21.1046 19 22 18.1046 22 17V5C22 3.89543 21.1046 3 20 3H4C2.89543 3 2 3.89543 2 5V17C2 18.1046 2.89543 19 4 19H9ZM12 19.1716L14.1716 17H20V5H4L4 17H9.82843L12 19.1716Z" style="fill: var(--element-active-color)"/>
<path d="M9.73374 14.6603L11.9999 13.3297L14.2661 14.6603C14.5878 14.8492 14.9786 14.5593 14.8912 14.1967L14.2965 11.7277L16.279 10.0676C16.5695 9.82438 16.4181 9.35125 16.0403 9.32191L13.4152 9.11796L12.3877 6.75425C12.2403 6.41525 11.7595 6.41525 11.6122 6.75425L10.5846 9.11796L7.95951 9.32191C7.58176 9.35125 7.43032 9.82438 7.72082 10.0676L9.70335 11.7277L9.10859 14.1967C9.02124 14.5593 9.41208 14.8492 9.73374 14.6603Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},_u=(gu.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,gu);N([P({type:Boolean})],_u.prototype,`useCssColor`,void 0),_u=N([M(`obi-notification-advice`)],_u);var vu=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.0005 20C16.4188 20 20.0005 16.4183 20.0005 12C20.0005 7.58172 16.4188 4 12.0005 4C7.58221 4 4.00049 7.58172 4.00049 12C4.00049 16.4183 7.58221 20 12.0005 20ZM12.0005 22C17.5233 22 22.0005 17.5228 22.0005 12C22.0005 6.47715 17.5233 2 12.0005 2C6.47764 2 2.00049 6.47715 2.00049 12C2.00049 17.5228 6.47764 22 12.0005 22Z" fill="currentColor"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M17.7072 9.70706L10.5001 16.9142L6.29297 12.7071L7.70718 11.2928L10.5001 14.0857L16.293 8.29285L17.7072 9.70706Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.0005 20C16.4188 20 20.0005 16.4183 20.0005 12C20.0005 7.58172 16.4188 4 12.0005 4C7.58221 4 4.00049 7.58172 4.00049 12C4.00049 16.4183 7.58221 20 12.0005 20ZM12.0005 22C17.5233 22 22.0005 17.5228 22.0005 12C22.0005 6.47715 17.5233 2 12.0005 2C6.47764 2 2.00049 6.47715 2.00049 12C2.00049 17.5228 6.47764 22 12.0005 22Z" style="fill: var(--element-active-color)"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M17.7072 9.70706L10.5001 16.9142L6.29297 12.7071L7.70718 11.2928L10.5001 14.0857L16.293 8.29285L17.7072 9.70706Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},yu=(vu.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,vu);N([P({type:Boolean})],yu.prototype,`useCssColor`,void 0),yu=N([M(`obi-running`)],yu);var bu=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z" fill="currentColor"/>
<path d="M12 2.5C17.2467 2.5 21.5 6.75329 21.5 12C21.5 17.2467 17.2467 21.5 12 21.5C6.75329 21.5 2.5 17.2467 2.5 12C2.5 6.75329 6.75329 2.5 12 2.5Z" stroke="currentColor"/>
<path d="M7.5 13.1999V10.7999C7.5 10.5199 7.5 10.3799 7.5545 10.2729C7.60243 10.1789 7.67892 10.1024 7.773 10.0544C7.87996 9.99993 8.01997 9.99993 8.3 9.99993H10.6686C10.7909 9.99993 10.8521 9.99993 10.9096 9.98611C10.9606 9.97386 11.0094 9.95366 11.0541 9.92625C11.1046 9.89533 11.1478 9.85209 11.2343 9.76561L13.6343 7.36561C14.0627 6.93724 14.2769 6.72305 14.4608 6.70858C14.6203 6.69602 14.7763 6.76061 14.8802 6.88231C15 7.02257 15 7.32548 15 7.9313V16.0686C15 16.6744 15 16.9773 14.8802 17.1175C14.7763 17.2392 14.6203 17.3038 14.4608 17.2913C14.2769 17.2768 14.0627 17.0626 13.6343 16.6342L11.2343 14.2342C11.1478 14.1478 11.1046 14.1045 11.0541 14.0736C11.0094 14.0462 10.9606 14.026 10.9096 14.0137C10.8521 13.9999 10.7909 13.9999 10.6686 13.9999H8.3C8.01997 13.9999 7.87996 13.9999 7.773 13.9454C7.67892 13.8975 7.60243 13.821 7.5545 13.7269C7.5 13.62 7.5 13.48 7.5 13.1999Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z" style="fill: var(--alert-warning-color)"/>
<path d="M12 2.5C17.2467 2.5 21.5 6.75329 21.5 12C21.5 17.2467 17.2467 21.5 12 21.5C6.75329 21.5 2.5 17.2467 2.5 12C2.5 6.75329 6.75329 2.5 12 2.5Z" style="stroke: var(--alert-warning-outline-color)"/>
<path d="M7.5 13.1999V10.7999C7.5 10.5199 7.5 10.3799 7.5545 10.2729C7.60243 10.1789 7.67892 10.1024 7.773 10.0544C7.87996 9.99993 8.01997 9.99993 8.3 9.99993H10.6686C10.7909 9.99993 10.8521 9.99993 10.9096 9.98611C10.9606 9.97386 11.0094 9.95366 11.0541 9.92625C11.1046 9.89533 11.1478 9.85209 11.2343 9.76561L13.6343 7.36561C14.0627 6.93724 14.2769 6.72305 14.4608 6.70858C14.6203 6.69602 14.7763 6.76061 14.8802 6.88231C15 7.02257 15 7.32548 15 7.9313V16.0686C15 16.6744 15 16.9773 14.8802 17.1175C14.7763 17.2392 14.6203 17.3038 14.4608 17.2913C14.2769 17.2768 14.0627 17.0626 13.6343 16.6342L11.2343 14.2342C11.1478 14.1478 11.1046 14.1045 11.0541 14.0736C11.0094 14.0462 10.9606 14.026 10.9096 14.0137C10.8521 13.9999 10.7909 13.9999 10.6686 13.9999H8.3C8.01997 13.9999 7.87996 13.9999 7.773 13.9454C7.67892 13.8975 7.60243 13.821 7.5545 13.7269C7.5 13.62 7.5 13.48 7.5 13.1999Z" style="fill: var(--on-warning-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},xu=(bu.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,bu);N([P({type:Boolean})],xu.prototype,`useCssColor`,void 0),xu=N([M(`obi-warning-unacknowledged-iec`)],xu);var Su=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12 21C16.9706 21 21 16.9706 21 12C21 7.02944 16.9706 3 12 3C7.02944 3 3 7.02944 3 12C3 16.9706 7.02944 21 12 21ZM12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" fill="currentColor"/>
<path d="M7.5 13.1999V10.7999C7.5 10.5199 7.5 10.3799 7.5545 10.2729C7.60243 10.1789 7.67892 10.1024 7.773 10.0544C7.87996 9.99993 8.01997 9.99993 8.3 9.99993H11L13.6343 7.36561C14.0627 6.93724 14.2769 6.72305 14.4608 6.70858C14.6203 6.69602 14.7763 6.7606 14.8802 6.88231C15 7.02257 15 7.32548 15 7.9313V16.0686C15 16.6744 15 16.9773 14.8802 17.1175C14.7763 17.2392 14.6203 17.3038 14.4608 17.2913C14.2769 17.2768 14.0627 17.0626 13.6343 16.6342L11 13.9999H8.3C8.01997 13.9999 7.87996 13.9999 7.773 13.9454C7.67892 13.8975 7.60243 13.821 7.5545 13.7269C7.5 13.62 7.5 13.48 7.5 13.1999Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M12 21C16.9706 21 21 16.9706 21 12C21 7.02944 16.9706 3 12 3C7.02944 3 3 7.02944 3 12C3 16.9706 7.02944 21 12 21ZM12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" style="fill: var(--element-active-color)"/>
<path d="M7.5 13.1999V10.7999C7.5 10.5199 7.5 10.3799 7.5545 10.2729C7.60243 10.1789 7.67892 10.1024 7.773 10.0544C7.87996 9.99993 8.01997 9.99993 8.3 9.99993H11L13.6343 7.36561C14.0627 6.93724 14.2769 6.72305 14.4608 6.70858C14.6203 6.69602 14.7763 6.7606 14.8802 6.88231C15 7.02257 15 7.32548 15 7.9313V16.0686C15 16.6744 15 16.9773 14.8802 17.1175C14.7763 17.2392 14.6203 17.3038 14.4608 17.2913C14.2769 17.2768 14.0627 17.0626 13.6343 16.6342L11 13.9999H8.3C8.01997 13.9999 7.87996 13.9999 7.773 13.9454C7.67892 13.8975 7.60243 13.821 7.5545 13.7269C7.5 13.62 7.5 13.48 7.5 13.1999Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Cu=(Su.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Su);N([P({type:Boolean})],Cu.prototype,`useCssColor`,void 0),Cu=N([M(`obi-warning-unacknowledged-outlined`)],Cu);var wu=o`* {
  -webkit-tap-highlight-color: transparent;
}

* {
  box-sizing: border-box;
}

:host {
  display: inline-flex;
  align-items: flex-end;
}

/* ---------- Readout building block (advice / setpoint / value) ---------- */
.block {
  display: inline-flex;
  align-items: flex-end;
}

/* Number + its (setpoint/advice) degree glyph, hugging with no gap — the
   \`.block\` gap only separates the icon from this group. */
.block-content {
  display: inline-flex;
  align-items: flex-end;
}

.block-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex: none;
  color: inherit;
  /* Centre the icon against the block's text rather than bottom-aligning it (the
     block is flex-end). Matters for the value block, whose text is taller than
     the icon, so the value icon lines up with the number like the smaller
     setpoint/advice icons do. */
  align-self: center;
}

.block-icon obi-input-right,
.block-icon obi-notification-advice,
.block-icon ::slotted(*) {
  display: block;
  inline-size: 100%;
  block-size: 100%;
}

.hinted-zero {
  /* Figma 6.1 review (node 95:24490): hinted zeros are lighter than the old
     inactive tone and NEVER inherit the value's weight — a bold value must not
     bold its hints. */
  color: var(--obc-readout-block-hinted-color, var(--element-disabled-color));
  font-weight: var(--global-typography-generic-l-font-weight-regular);
}

.sign-spacer {
  /* visibility, not display: the hidden \`-\` must keep its box so the sign
     column stays open while the value is non-negative (\`hasSignSpacer\`). */
  visibility: hidden;
}

/* ---------- Text colours (overridable via custom properties) ----------
 * obc-textbox does not set its own colour, so it inherits these. */
.block-value {
  color: var(--obc-readout-block-value-color, var(--element-neutral-color));
}
.block-value.tone-enhanced {
  color: var(
    --obc-readout-block-value-enhanced-color,
    var(--element-neutral-enhanced-color)
  );
}
/* The setpoint shares the value's colour state: neutral by default, enhanced
   (blue) only when the row is enhanced — never a blue setpoint next to a grey
   value. \`--instrument-enhanced-secondary-color\` is the same #2d548b as the
   value's \`--element-neutral-enhanced-color\`. */
.block-setpoint {
  color: var(--obc-readout-block-setpoint-color, var(--element-neutral-color));
  /* Flip-flop emphasis + pop-up fade animate at 100ms. */
  transition:
    opacity 100ms ease,
    color 100ms ease;
}
.block-setpoint.tone-enhanced {
  color: var(
    --obc-readout-block-setpoint-enhanced-color,
    var(--instrument-enhanced-secondary-color)
  );
}
/* Pop-up: fade the setpoint out once value === setpoint, keeping its space so
   the value stays column-aligned. */
.block-setpoint.is-hiding {
  opacity: 0;
}
.block-setpoint.is-hidden {
  opacity: 0;
  visibility: hidden;
}
/* Touching / focus state: the setpoint triangle takes the marker's focus look — a
   pale fill (--base-blue-100) with a dark 1px edge (--element-neutral-enhanced),
   mirroring \`svghelpers/setpoint.ts\` focus (fill base-blue-100 + 2px stroke).
   The glyph icon is \`fill: currentColor\` and can't take a CSS \`stroke\`, so the
   edge is layered drop-shadows. The setpoint number keeps its normal, readable
   colour. */
.block-setpoint.touching {
  --_touching-outline: var(
    --obc-readout-block-setpoint-touching-outline-color,
    var(--element-neutral-enhanced-color)
  );
}
.block-setpoint.touching .block-icon {
  color: var(--obc-readout-block-setpoint-touching-color, var(--base-blue-100));
  filter: drop-shadow(1px 0 0 var(--_touching-outline))
    drop-shadow(-1px 0 0 var(--_touching-outline))
    drop-shadow(0 1px 0 var(--_touching-outline))
    drop-shadow(0 -1px 0 var(--_touching-outline));
}
.block-advice {
  color: var(--obc-readout-block-advice-color, var(--element-neutral-color));
}

/* ---------- Advice categories (Figma 6.1 Readout-block-advice) ----------
 * Resting categories are neutral; \`advice-active\` (triggered) tints the
 * regular/optimal/eco diamond via currentColor (the IEC status icons of the
 * alert categories carry fixed fills and ignore this) and switches the alert
 * categories' number to the active text colour. */
.block-advice.advice-active.advice-optimal .block-icon {
  color: var(--element-neutral-enhanced-color);
}
.block-advice.advice-active.advice-eco .block-icon {
  color: var(--base-mint-400);
}
.block-advice.advice-active.advice-caution,
.block-advice.advice-active.advice-warning,
.block-advice.advice-active.advice-alarm,
.block-advice.advice-active.advice-running {
  color: var(--element-active-color);
}

/* ---------- Per-block data quality ----------
 * Uses \`outline\` (not \`border\`) so the chip never shifts the block's width — the
 * value stays column-aligned across rows. */
.block.data-low-integrity,
.block.data-invalid {
  outline: 1px solid;
  border-radius: var(--global-border-radius-border-radius-check);
}
.block.data-low-integrity {
  background: var(--alert-low-integrity-background-color);
  outline-color: var(--alert-low-integrity-border-color);
}
.block.data-invalid {
  background: var(--alert-invalid-background-color);
  outline-color: var(--alert-invalid-border-color);
}

/* ---------- Degree column ----------
 * A cap-height \`°\` column whose width scales with the number size; it inherits
 * the block's colour. */
.degree-column {
  flex: none;
  display: inline-flex;
  align-items: flex-end;
  justify-content: center;
  inline-size: var(--_obc-readout-block-degree-width, 0);
  overflow: clip;
}
.degree-column.degree-inherit {
  color: inherit;
}
.degree-column.degree-xs {
  --_obc-readout-block-degree-width: var(
    --global-typography-instrument-value-small-degree-unit-width
  );
}
.degree-column.degree-s {
  --_obc-readout-block-degree-width: var(
    --global-typography-instrument-value-regular-degree-unit-width
  );
}
.degree-column.degree-m {
  --_obc-readout-block-degree-width: var(
    --global-typography-instrument-value-medium-degree-unit-width
  );
}
.degree-column.degree-l,
.degree-column.degree-xl {
  --_obc-readout-block-degree-width: var(
    --global-typography-instrument-value-large-degree-unit-width
  );
}

/* ---------- Size tiers ----------
 * Public small/medium/large map to the design token regular/medium/large
 * tiers. The icon↔number gap follows the tier; the marker ICON size follows
 * the block's rendered number size (\`value-size-*\`) instead — Figma 6.1
 * (Readout-block-setpoint, review node 95:26891): a de-emphasised S setpoint
 * carries the 16px arrow while an emphasised L one carries the 24px arrow,
 * even though both sit in the same large-tier readout.
 * \`--obc-readout-block-icon-size\` is the consumer escape hatch. */
.block.size-small {
  gap: var(--instrument-components-readout-general-regular-icon-gap);
}
.block.size-medium {
  gap: var(--instrument-components-readout-general-medium-icon-gap);
}
.block.size-large {
  gap: var(--instrument-components-readout-general-large-icon-gap);
}

.block.value-size-xs,
.block.value-size-s {
  --_block-icon-size: var(
    --instrument-components-readout-general-regular-icon-size
  );
}
.block.value-size-m {
  --_block-icon-size: var(
    --instrument-components-readout-general-medium-icon-size
  );
}
.block.value-size-l,
.block.value-size-xl {
  --_block-icon-size: var(
    --instrument-components-readout-general-large-icon-size
  );
}
.block .block-icon {
  inline-size: var(--obc-readout-block-icon-size, var(--_block-icon-size));
  block-size: var(--obc-readout-block-icon-size, var(--_block-icon-size));
}
`,Tu,Eu=function(e){return e.value=`value`,e.setpoint=`setpoint`,e.advice=`advice`,e}({}),Du=function(e){return e.small=`small`,e.medium=`medium`,e.large=`large`,e}({}),Ou=function(e){return e.lowIntegrity=`low-integrity`,e.invalid=`invalid`,e}({}),ku=function(e){return e.regular=`regular`,e.optimal=`optimal`,e.eco=`eco`,e.caution=`caution`,e.warning=`warning`,e.alarm=`alarm`,e.running=`running`,e}({}),q=function(e){return e.none=`none`,e.hiding=`hiding`,e.hidden=`hidden`,e}({}),J=(Tu=class extends j{constructor(...e){super(...e),this.variant=`value`,this.value=null,this.valueType=Ul.number,this.size=`small`,this.enhanced=!1,this.weight=Vl.regular,this.hasDegree=!1,this.hasIcon=!1,this.fractionDigits=0,this.maxDigits=0,this.hintedZeros=!1,this.hasSignSpacer=!1,this.off=!1,this.offText=`OFF`,this.alignment=zl.Right,this.category=`regular`,this.active=!1,this.alert=!1,this.touching=!1,this.hidePhase=`none`,this.hasAssignedIcon=!1,this.onIconSlotChange=e=>{this.hasAssignedIcon=e.target.assignedElements({flatten:!0}).length>0}}get resolvedValueSize(){if(this.valueSize)return this.valueSize;switch(this.size){case`large`:return Bl.l;case`medium`:return Bl.m;default:return Bl.s}}get resolvedMaxDigits(){return Jl(this.maxDigits)}get digitCountsMissing(){return Yl(this.fractionDigits)||Yl(this.maxDigits)}get numericFormatOptions(){return{showZeroPadding:this.hintedZeros,minValueLength:this.resolvedMaxDigits,fractionDigits:Yl(this.fractionDigits)?0:this.fractionDigits}}get reserverText(){let e=this.resolvedMaxDigits;if(e<=0)return``;let t=`0`.repeat(e);return this.fractionDigits>0?`${t}.${`0`.repeat(this.fractionDigits)}`:t}widerReserver(e,t){return e?t?e.length>=t.length?e:t:e:t}dataQualityClasses(){return{"data-low-integrity":this.dataQuality===`low-integrity`,"data-invalid":this.dataQuality===`invalid`}}renderIcon(){if(!(this.variant!==`value`||this.hasIcon))return A;let e=A;return this.variant===`setpoint`?e=O`<obi-input-right></obi-input-right>`:this.variant===`advice`&&(e=this.adviceFallbackIcon()),O`<span class="block-icon" part="block-icon" aria-hidden="true">
      <slot name="icon" @slotchange=${this.onIconSlotChange}></slot>
      ${this.hasAssignedIcon?A:e}
    </span>`}adviceFallbackIcon(){let e=this.active;switch(this.category){case`caution`:return e?O`<obi-caution-color-iec useCssColor></obi-caution-color-iec>`:O`<obi-caution-google></obi-caution-google>`;case`warning`:return e?O`<obi-warning-unacknowledged-iec
              useCssColor
            ></obi-warning-unacknowledged-iec>`:O`<obi-warning-unacknowledged-outlined></obi-warning-unacknowledged-outlined>`;case`alarm`:return e?O`<obi-alarm-unacknowledged-iec
              useCssColor
            ></obi-alarm-unacknowledged-iec>`:O`<obi-alarm></obi-alarm>`;case`running`:return e?O`<obi-running-color-iec useCssColor></obi-running-color-iec>`:O`<obi-running></obi-running>`;default:return e?O`<obi-notification-advice-active></obi-notification-advice-active>`:O`<obi-notification-advice></obi-notification-advice>`}}renderDegreeGlyph(e){return O`
      <span
        class=${F({"degree-column":!0,[`degree-${e}`]:!0,"degree-inherit":!0})}
        part="degree"
      >
        <obc-textbox class="degree-glyph" .size=${e} alignment="center"
          >°</obc-textbox
        >
      </span>
    `}willUpdate(e){super.willUpdate(e),Zl(`obc-readout-block`,this.value,this.valueType),ql(`obc-readout-block`,this.fractionDigits)}render(){let e=this.resolvedValueSize,t=this.variant===`advice`,n=t&&this.active&&(this.category===`regular`||this.category===`optimal`||this.category===`eco`)?Vl.semibold:this.weight,r=this.numericFormatOptions,i=this.valueType===Ul.text,a=this.digitCountsMissing?void 0:Ql(this.value,this.valueType),o=$l(this.value,this.valueType),s=this.off?this.offText:i?o??`‒`:tu(a,r),{sign:c,hinted:l,magnitude:u}=!this.off&&!i&&this.hintedZeros&&a!==void 0?ru(s,this.resolvedMaxDigits):{sign:``,hinted:``,magnitude:s},d=this.hasSignSpacer&&!i&&c===``&&!u.startsWith(`-`),f=i?this.spaceReserver??``:this.widerReserver(this.spaceReserver,this.reserverText),p=!i&&this.hasSignSpacer&&!f.startsWith(`-`)?`-${f}`:f,m=O`
      <div
        class=${F({block:!0,[`block-${this.variant}`]:!0,[`size-${this.size}`]:!0,[`value-size-${e}`]:!0,[`advice-${this.category}`]:t,"advice-active":t&&this.active,"tone-enhanced":this.enhanced,touching:this.touching,"is-hiding":this.hidePhase===`hiding`,"is-hidden":this.hidePhase===`hidden`,...this.dataQualityClasses()})}
        part="block block-${this.variant}"
      >
        ${this.renderIcon()}
        <span class="block-content" part="block-content">
          <obc-textbox
            class="block-text"
            part="block-text"
            .size=${e}
            .fontWeight=${n}
            .alignment=${this.alignment}
            .tabularNums=${!0}
          >
            ${c}${d?O`<span class="sign-spacer" aria-hidden="true">-</span>`:A}${l?O`<span class="hinted-zero" aria-hidden="true"
                    >${l}</span
                  >`:A}${u}
            ${p?O`<span slot="length">${p}</span>`:A}
          </obc-textbox>
          ${this.hasDegree?this.renderDegreeGlyph(e):A}
        </span>
      </div>
    `;return Il(this.alert??!1,m)}},Tu.styles=a(wu),Tu);N([P({type:String})],J.prototype,`variant`,void 0),N([P({type:String})],J.prototype,`value`,void 0),N([P({type:String})],J.prototype,`valueType`,void 0),N([P({type:String})],J.prototype,`size`,void 0),N([P({type:String})],J.prototype,`valueSize`,void 0),N([P({type:Boolean})],J.prototype,`enhanced`,void 0),N([P({type:String})],J.prototype,`weight`,void 0),N([P({type:Boolean})],J.prototype,`hasDegree`,void 0),N([P({type:Boolean})],J.prototype,`hasIcon`,void 0),N([P({type:Number})],J.prototype,`fractionDigits`,void 0),N([P({type:Number})],J.prototype,`maxDigits`,void 0),N([P({type:Boolean})],J.prototype,`hintedZeros`,void 0),N([P({type:Boolean})],J.prototype,`hasSignSpacer`,void 0),N([P({type:String})],J.prototype,`spaceReserver`,void 0),N([P({type:Boolean})],J.prototype,`off`,void 0),N([P({type:String})],J.prototype,`offText`,void 0),N([P({type:String})],J.prototype,`alignment`,void 0),N([P({type:String})],J.prototype,`category`,void 0),N([P({type:Boolean})],J.prototype,`active`,void 0),N([P({type:String})],J.prototype,`dataQuality`,void 0),N([P({type:Object})],J.prototype,`alert`,void 0),N([P({type:Boolean})],J.prototype,`touching`,void 0),N([P({type:String})],J.prototype,`hidePhase`,void 0),N([ze()],J.prototype,`hasAssignedIcon`,void 0),J=N([M(`obc-readout-block`)],J);var Au=o`* {
  -webkit-tap-highlight-color: transparent;
}

* {
  box-sizing: border-box;
}

:host {
  display: inline-flex;
  position: relative;
}

obc-readout-block {
  --obc-readout-block-value-color: var(
    --obc-readout-value-color,
    var(--element-neutral-color)
  );
  --obc-readout-block-value-enhanced-color: var(
    --obc-readout-value-enhanced-color,
    var(--element-neutral-enhanced-color)
  );
  --obc-readout-block-setpoint-color: var(
    --obc-readout-setpoint-color,
    var(--element-neutral-color)
  );
  --obc-readout-block-setpoint-enhanced-color: var(
    --obc-readout-setpoint-enhanced-color,
    var(--instrument-enhanced-secondary-color)
  );
  --obc-readout-block-setpoint-touching-outline-color: var(
    --obc-readout-setpoint-touching-outline-color,
    var(--element-neutral-enhanced-color)
  );
  --obc-readout-block-setpoint-touching-color: var(
    --obc-readout-setpoint-touching-color,
    var(--base-blue-100)
  );
  --obc-readout-block-advice-color: var(
    --obc-readout-advice-color,
    var(--element-neutral-color)
  );
  --obc-readout-block-hinted-color: var(
    --obc-readout-hinted-color,
    var(--element-disabled-color)
  );
}

::slotted([slot="value-icon"]),
  ::slotted([slot="setpoint-icon"]),
  ::slotted([slot="advice-icon"]) {
    display: block;
    inline-size: 100%;
    block-size: 100%;
  }

/* ---------- Root ----------
 * The root is an inline flex column (vertical) or row (horizontal). Private
 * \`--_readout-*\` variables are resolved per layout × size tier below; every
 * layout rule reads only the private variables. A readout is as tall as its
 * rows: the design's container-min-height tokens are not applied (#1252). */
.readout {
  display: inline-flex;
  position: relative;
  padding-inline: var(--_readout-pad-h);
  padding-block: var(--_readout-pad-v);
  border-radius: var(--global-border-radius-border-radius-base);
}

.readout.direction-vertical {
  flex-direction: column;
  align-items: flex-end;
}

.readout.direction-horizontal {
  flex-direction: row;
  align-items: flex-end;
}

/* Flip-flop: animate the value↔setpoint cap-height swap by forwarding
   obc-textbox's opt-in size-transition var. 300ms matches the instrument
   setpoint marker (svghelpers/setpoint.ts). Override via
   \`--obc-readout-flip-flop-duration\`. */
.readout.flip-flop {
  --obc-textbox-size-transition: var(--obc-readout-flip-flop-duration, 300ms);
}

/* ---------- Alignment (vertical stacks) ----------
 * \`vertical\` (default) is a right-aligned column; \`left\` and \`center\`
 * re-align every row. */
.readout.direction-vertical.alignment-left {
  align-items: flex-start;
}

.readout.direction-vertical.alignment-center {
  align-items: center;
}

.readout.direction-vertical.alignment-left
  :is(.value-cluster, .advice-row, .setpoint-row, .value-row) {
  align-items: flex-start;
  justify-content: flex-start;
}

.readout.direction-vertical.alignment-center
  :is(.value-cluster, .advice-row, .setpoint-row, .value-row) {
  align-items: center;
  justify-content: center;
}

/* ---------- Value cluster (advice / setpoint / value rows) ---------- */
.value-cluster {
  display: inline-flex;
  flex-direction: column;
  align-items: flex-end;
  gap: var(--_readout-value-gap);
  padding-block: var(--_readout-value-pad-v);
}

.advice-row,
.setpoint-row,
.value-row {
  display: inline-flex;
  align-items: flex-end;
  justify-content: flex-end;
  padding-inline: var(--_readout-trim);
}

/* Dynamic setpoint interactions (flip-flop and pop-up — \`.setpoint-dynamic\`)
   swap the value/setpoint cap heights (flip-flop / touch) or fade the setpoint
   out (pop-up); pin both rows to the primary tier height so the readout's
   total height stays constant throughout. (Pop-up additionally keeps its
   space via the block's visibility-hidden hide phase.) */
.readout.direction-vertical.setpoint-dynamic :is(.setpoint-row, .value-row) {
  min-block-size: var(--_readout-primary-height);
}

/* Width reservation (vertical only): each dynamic setpoint row grid-stacks an
   invisible primary-size duplicate of its own content behind the visible
   block, so both rows permanently hold their emphasised width and the widest
   row — the readout's total width — stays constant through the flip-flop
   swap, the touch swap and the pop-up fade-out (nothing around the pair
   shifts). The horizontal direction needs no reservation: there the pair
   shares one row and its summed width is constant by construction. */
.readout.direction-vertical.setpoint-dynamic :is(.setpoint-row, .value-row) {
  display: inline-grid;
  align-items: end;
  justify-items: end;
}

.readout.direction-vertical.setpoint-dynamic
  :is(.setpoint-row, .value-row)
  > * {
  grid-area: 1 / 1;
}

.readout.direction-vertical.alignment-left.setpoint-dynamic
  :is(.setpoint-row, .value-row) {
  justify-items: start;
}

.readout.direction-vertical.alignment-center.setpoint-dynamic
  :is(.setpoint-row, .value-row) {
  justify-items: center;
}

.setpoint-width-reserve {
  visibility: hidden;
  display: inline-flex;
  align-items: flex-end;
}

/* ---------- Horizontal inline row ---------- */
.inline-row {
  display: inline-flex;
  align-items: flex-end;
  gap: var(--_readout-value-gap);
  min-block-size: var(--_readout-primary-height);
  padding-block: var(--_readout-value-pad-v);
}

.inline-row .advice-row,
.inline-row .setpoint-row,
.inline-row .value-row {
  align-items: flex-end;
}

/* ---------- Value reading (value + degree) ----------
 * Groups the value block and its degree column so the value alert frame and
 * the value data-quality chip can wrap both. Layout-neutral: it adds no gap. */
.value-reading {
  position: relative;
  display: inline-flex;
  align-items: flex-end;
}

/* ---------- Value data quality (low-integrity / invalid) ----------
 * Same look as the block/source chip (1px outline, check radius). Uses
 * \`outline\` (not \`border\`) so it never shifts the value's width. */
.value-reading.data-low-integrity,
.value-reading.data-invalid {
  outline: 1px solid;
  border-radius: var(--global-border-radius-border-radius-check);
}

.value-reading.data-low-integrity {
  background: var(--alert-low-integrity-background-color);
  outline-color: var(--alert-low-integrity-border-color);
}

.value-reading.data-invalid {
  background: var(--alert-invalid-background-color);
  outline-color: var(--alert-invalid-border-color);
}

/* ---------- Value alert overlay ----------
 * Reserves no space, so toggling the frame never shifts content. The box sits
 * on the 4px/2px padding line, where obc-alert-frame centres its stroke. */
.value-alert-overlay {
  --_readout-value-frame-padding-horizontal: 4px;
  --_readout-value-frame-padding-vertical: 2px;
  position: absolute;
  inset-inline: calc(-1 * var(--_readout-value-frame-padding-horizontal));
  inset-block: calc(-1 * var(--_readout-value-frame-padding-vertical));
  pointer-events: none;
}

/* ---------- Meta zone (label + unit) ----------
 * \`.meta\` is a row hosting the optional leading icon and \`.meta-labels\`; the
 * inline/stacked arrangement applies to \`.meta-labels\` (the label/unit pair). */
.meta {
  display: inline-flex;
  flex-direction: row;
  align-items: center;
  gap: var(--instrument-components-readout-general-regular-icon-gap);
  padding-inline: var(--_readout-trim);
}

.meta .leading-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex: none;
  color: var(--element-neutral-color);
}
.meta .leading-icon ::slotted(*) {
  display: block;
  inline-size: 100%;
  block-size: 100%;
}
.readout.size-small .meta .leading-icon {
  inline-size: var(--instrument-components-readout-general-regular-icon-size);
  block-size: var(--instrument-components-readout-general-regular-icon-size);
}
.readout.size-medium .meta .leading-icon {
  inline-size: var(--instrument-components-readout-general-medium-icon-size);
  block-size: var(--instrument-components-readout-general-medium-icon-size);
}
.readout.size-large .meta .leading-icon {
  inline-size: var(--instrument-components-readout-general-large-icon-size);
  block-size: var(--instrument-components-readout-general-large-icon-size);
}

.meta-labels {
  display: inline-flex;
}

.meta-inline .meta-labels {
  flex-direction: row;
  /* Bottom-align so an \`s\` label and its \`xs\` unit share a baseline (the
     Figma title block is items-end). */
  align-items: flex-end;
  gap: var(--global-size-spacing-target-padding);
}

.meta-stacked .meta-labels {
  flex-direction: column;
  align-items: flex-end;
}

.readout.direction-vertical.alignment-left .meta-stacked .meta-labels {
  align-items: flex-start;
}

.readout.direction-vertical.alignment-center .meta-stacked .meta-labels {
  align-items: center;
}

/* Horizontal: the label/unit column sits beside the value, top-aligned within
   the row so the label reads first. */
.readout.direction-horizontal .meta.meta-stacked {
  align-self: center;
}
:is(.readout.direction-horizontal .meta.meta-stacked) .meta-labels {
    align-items: flex-start;
  }
.label-only:is(.readout.direction-horizontal .meta.meta-stacked) {
    align-self: flex-start;
  }
.unit-only:is(.readout.direction-horizontal .meta.meta-stacked) {
    align-self: flex-end;
  }

/* Cap alignment beside the value (Figma 6.1 review): the label's cap TOP and
   the unit's cap BOTTOM line up with the value's cap edges. The stack is
   pinned to the value's container height with space-between — every textbox
   carries a fixed 4px pad above/below its cap, exactly like the value box, so
   pinning the boxes to the container edges aligns the caps for any label/unit
   size. Only when both lines exist: a single line keeps its edge alignment
   from the rules above. */
.readout.direction-horizontal
  .meta.meta-stacked:not(.label-only):not(.unit-only)
  .meta-labels {
  block-size: var(--_readout-primary-height);
  justify-content: space-between;
}

.label {
  color: var(--obc-readout-label-color, var(--element-neutral-color));
}

.unit {
  color: var(--obc-readout-unit-color, var(--element-neutral-color));
}

.source {
  color: var(--obc-readout-source-color, var(--element-neutral-color));
}

/* ---------- Source data quality ----------
 * Independent of (and nests inside) the readout-level data-quality frame. Uses
 * \`outline\` (not \`border\`) so the chip never shifts the source's width. The
 * same chip applies to the interactive source button (picker / flyout). */
.source.data-low-integrity,
.source.data-invalid,
.source-button.data-low-integrity,
.source-button.data-invalid {
  outline: 1px solid;
  border-radius: var(--global-border-radius-border-radius-check);
}

.source.data-low-integrity,
.source-button.data-low-integrity {
  background: var(--alert-low-integrity-background-color);
  outline-color: var(--alert-low-integrity-border-color);
}

.source.data-invalid,
.source-button.data-invalid {
  background: var(--alert-invalid-background-color);
  outline-color: var(--alert-invalid-border-color);
}

/* ---------- Source state chip & deviation (Figma 6.1 Readout-block-source)
 * \`enhanced\` renders the amplified chip, \`caution\`/\`warning\` the alert chip.
 * Like the data-quality chip these use \`outline\`, so toggling a state never
 * shifts the layout. TODO(designer): Figma pads the chip 4px; a padding here
 * would shift the layout on live state changes, so the chip hugs the text
 * like the data-quality chip does. */
.source-block {
  display: inline-flex;
  flex-direction: column;
  align-items: flex-start;
}
.source-block.source-state-enhanced,
.source-block.source-state-caution,
.source-block.source-state-warning {
  outline: 1px solid;
  border-radius: var(--global-border-radius-border-radius-check);
}
.source-block.source-state-enhanced {
  background: var(--amplified-enabled-background-color);
  outline-color: var(--amplified-enabled-border-color);
}
.source-block.source-state-enhanced .source,
.source-block.source-state-enhanced .source-deviation {
  color: var(--on-amplified-active-color);
}
.source-block.source-state-caution {
  background: var(--alert-caution-color);
  outline-color: var(--alert-caution-outline-color);
}
.source-block.source-state-caution .source,
.source-block.source-state-caution .source-deviation {
  color: var(--on-caution-active-color);
}
.source-block.source-state-warning {
  background: var(--alert-warning-color);
  outline-color: var(--alert-warning-outline-color);
}
.source-block.source-state-warning .source,
.source-block.source-state-warning .source-deviation {
  color: var(--on-warning-active-color);
}

.source-deviation {
  display: inline-flex;
  align-items: center;
  gap: 2px;
  color: var(--element-inactive-color);
}
.source-deviation obi-delta {
  display: block;
  inline-size: 12px;
  block-size: 12px;
}

/* ---------- Source row & auto divider ---------- */
.source-row {
  display: inline-flex;
  align-items: center;
  padding-inline: var(--_readout-trim);
}

.divider {
  flex: none;
  background-color: var(--border-divider-color);
}

/* Only the horizontal direction draws a source divider (Figma 6.1: vertical
   readouts have no rule above the source). */
.divider.divider-vertical {
  inline-size: 1px;
  align-self: stretch;
  margin-inline: var(--_readout-divider-pad);
}

/* The interactive source variants (picker / flyout) render as a flat button. */
.source-button {
  --obc-button-padding-block: 0;
}

.source-picker-content {
  position: absolute;
  inset-block-start: 100%;
  inset-inline-end: 0;
  z-index: 2;
}

/* ---------- Degree column & spacer ----------
 * A cap-height \`°\` column after the value whose width scales with the value
 * size; \`hasDegreeSpacer\` reserves the same width invisibly so non-degree
 * readouts stay column-aligned with degree readouts. */
.degree-column {
  flex: none;
  display: inline-flex;
  align-items: flex-end;
  justify-content: center;
  inline-size: var(--_readout-degree-width, 0);
  overflow: clip;
  color: var(--obc-readout-value-color, var(--element-neutral-color));
}

.degree-column.tone-enhanced {
  color: var(
    --obc-readout-value-enhanced-color,
    var(--element-neutral-enhanced-color)
  );
}

.degree-column.degree-xs {
  --_readout-degree-width: var(
    --global-typography-instrument-value-small-degree-unit-width
  );
}

.degree-column.degree-s {
  --_readout-degree-width: var(
    --global-typography-instrument-value-regular-degree-unit-width
  );
}

.degree-column.degree-m {
  --_readout-degree-width: var(
    --global-typography-instrument-value-medium-degree-unit-width
  );
}

.degree-column.degree-l,
.degree-column.degree-xl {
  --_readout-degree-width: var(
    --global-typography-instrument-value-large-degree-unit-width
  );
}

.degree-spacer {
  flex: none;
  align-self: stretch;
  inline-size: var(--_readout-degree-spacer-width, 0);
}

.size-small .degree-spacer {
  --_readout-degree-spacer-width: var(
    --instrument-components-readout-general-regular-degree-compensation-padding
  );
}

.size-medium .degree-spacer {
  --_readout-degree-spacer-width: var(
    --instrument-components-readout-general-medium-degree-compensation-padding
  );
}

.size-large .degree-spacer {
  --_readout-degree-spacer-width: var(
    --instrument-components-readout-general-large-degree-compensation-padding
  );
}

/* ---------- Data quality (whole readout) ----------
 * Orthogonal to the alert frame — both can apply at once. \`outline\` (not
 * \`border\`) so the frame does not inset the content by 1px. */
.readout.data-low-integrity,
.readout.data-invalid {
  outline: 1px solid var(--_readout-data-border);
  background: var(--_readout-data-background);
  border-radius: var(--global-border-radius-border-radius-check);
}

.readout.data-low-integrity {
  --_readout-data-background: var(--alert-low-integrity-background-color);
  --_readout-data-border: var(--alert-low-integrity-border-color);
}

.readout.data-invalid {
  --_readout-data-background: var(--alert-invalid-background-color);
  --_readout-data-border: var(--alert-invalid-border-color);
}

/* ---------- Layout × size design tokens ----------
 * Public small/medium/large map to the design-token regular/medium/enhanced
 * tiers (the token set names the large tier "enhanced"). Three layout
 * families: group-vertical (direction-vertical + stacking-inline), stack
 * (direction-vertical + stacking-stacked) and group-horizontal
 * (direction-horizontal — stacking is ignored there). */

/* Typography container heights shared by the flip-flop row reservation. */
.readout.size-small {
  --_readout-primary-height: var(
    --global-typography-instrument-value-regular-container-height
  );
}

.readout.size-medium {
  --_readout-primary-height: var(
    --global-typography-instrument-value-medium-container-height
  );
}

.readout.size-large {
  --_readout-primary-height: var(
    --global-typography-instrument-value-large-container-height
  );
}

/* Group vertical */
.readout.direction-vertical.stacking-inline.size-small {
  --_readout-pad-h: var(
    --instrument-components-readout-group-vertical-regular-container-padding-horizontal
  );
  --_readout-pad-v: var(
    --instrument-components-readout-group-vertical-regular-container-padding-vertical
  );
  --_readout-trim: var(
    --instrument-components-readout-group-vertical-regular-horizontal-trim-padding
  );
  --_readout-value-gap: var(
    --instrument-components-readout-group-vertical-regular-vertical-value-container-gap
  );
  --_readout-value-pad-v: var(
    --instrument-components-readout-group-vertical-regular-value-container-padding-vertical
  );
}

.readout.direction-vertical.stacking-inline.size-medium {
  --_readout-pad-h: var(
    --instrument-components-readout-group-vertical-medium-container-padding-horizontal
  );
  --_readout-pad-v: var(
    --instrument-components-readout-group-vertical-medium-container-padding-vertical
  );
  --_readout-trim: var(
    --instrument-components-readout-group-vertical-medium-horizontal-trim-padding
  );
  --_readout-value-gap: var(
    --instrument-components-readout-group-vertical-medium-vertical-value-container-gap
  );
  --_readout-value-pad-v: var(
    --instrument-components-readout-group-vertical-medium-value-container-padding-vertical
  );
}

.readout.direction-vertical.stacking-inline.size-large {
  --_readout-pad-h: var(
    --instrument-components-readout-group-vertical-enhanced-container-padding-horizontal
  );
  --_readout-pad-v: var(
    --instrument-components-readout-group-vertical-enhanced-container-padding-vertical
  );
  --_readout-trim: var(
    --instrument-components-readout-group-vertical-enhanced-horizontal-trim-padding
  );
  --_readout-value-gap: var(
    --instrument-components-readout-group-vertical-enhanced-vertical-value-container-gap
  );
  --_readout-value-pad-v: var(
    --instrument-components-readout-group-vertical-enhanced-vertical-value-container-padding-vertical
  );
}

/* Stack (vertical, stacked meta) */
.readout.direction-vertical.stacking-stacked.size-small {
  --_readout-pad-h: var(
    --instrument-components-readout-stack-regular-container-padding-horizontal
  );
  --_readout-pad-v: var(
    --instrument-components-readout-stack-regular-container-padding-vertical
  );
  --_readout-trim: var(
    --instrument-components-readout-stack-regular-horizontal-trim-padding
  );
  --_readout-value-gap: var(
    --instrument-components-readout-stack-regular-vertical-value-container-gap
  );
  --_readout-value-pad-v: var(
    --instrument-components-readout-stack-regular-value-container-padding-vertical
  );
}

.readout.direction-vertical.stacking-stacked.size-medium {
  --_readout-pad-h: var(
    --instrument-components-readout-stack-medium-container-padding-horizontal
  );
  --_readout-pad-v: var(
    --instrument-components-readout-stack-medium-container-padding-vertical
  );
  --_readout-trim: var(
    --instrument-components-readout-stack-medium-horizontal-trim-padding
  );
  --_readout-value-gap: var(
    --instrument-components-readout-stack-medium-vertical-value-container-gap
  );
  --_readout-value-pad-v: var(
    --instrument-components-readout-stack-medium-value-container-padding-vertical
  );
}

.readout.direction-vertical.stacking-stacked.size-large {
  --_readout-pad-h: var(
    --instrument-components-readout-stack-enhanced-container-padding-horizontal
  );
  --_readout-pad-v: var(
    --instrument-components-readout-stack-enhanced-container-padding-vertical
  );
  --_readout-trim: var(
    --instrument-components-readout-stack-enhanced-horizontal-trim-padding
  );
  --_readout-value-gap: var(
    --instrument-components-readout-stack-enhanced-vertical-value-container-gap
  );
  --_readout-value-pad-v: var(
    --instrument-components-readout-stack-enhanced-vertical-value-container-padding-vertical
  );
}

/* Group horizontal */
.readout.direction-horizontal.size-small {
  --_readout-pad-h: var(
    --instrument-components-readout-group-horizontal-regular-container-padding-horizontal
  );
  --_readout-pad-v: var(
    --instrument-components-readout-group-horizontal-regular-container-padding-vertical
  );
  --_readout-trim: var(
    --instrument-components-readout-group-horizontal-regular-horizontal-trim-padding
  );
  /* TODO(designer): verify this gap */
  --_readout-value-gap: 0;
  --_readout-value-pad-v: var(
    --instrument-components-readout-group-horizontal-regular-value-container-padding-vertical
  );
  --_readout-divider-pad: var(
    --instrument-components-readout-group-horizontal-regular-divider-padding
  );
}

.readout.direction-horizontal.size-medium {
  --_readout-pad-h: var(
    --instrument-components-readout-group-horizontal-medium-container-padding-horizontal
  );
  --_readout-pad-v: var(
    --instrument-components-readout-group-horizontal-medium-container-padding-vertical
  );
  --_readout-trim: var(
    --instrument-components-readout-group-horizontal-medium-horizontal-trim-padding
  );
  /* TODO(designer): verify this gap */
  --_readout-value-gap: 0;
  --_readout-value-pad-v: var(
    --instrument-components-readout-group-horizontal-medium-value-container-padding-vertical
  );
  --_readout-divider-pad: var(
    --instrument-components-readout-group-horizontal-medium-divider-padding
  );
}

.readout.direction-horizontal.size-large {
  --_readout-pad-h: var(
    --instrument-components-readout-group-horizontal-enhanced-container-padding-horizontal
  );
  --_readout-pad-v: var(
    --instrument-components-readout-group-horizontal-enhanced-container-padding-vertical
  );
  --_readout-trim: var(
    --instrument-components-readout-group-horizontal-enhanced-horizontal-trim-padding
  );
  /* TODO(designer): verify this gap */
  --_readout-value-gap: 4px;
  --_readout-value-pad-v: var(
    --instrument-components-readout-group-horizontal-enhanced-value-container-padding
  );
  --_readout-divider-pad: var(
    --instrument-components-readout-group-horizontal-enhanced-divider-padding
  );
}

/* ---------- Debug overlay ----------
 * \`showDebugOverlay\` outlines each readout building block (red), the degree
 * columns (blue) and the degree spacer (green) so reserver widths / alignment
 * are visible. A development aid; off by default. */
:host([showDebugOverlay]) obc-readout-block::part(block) {
  outline: 1px solid rgba(220, 0, 0, 0.7);
  outline-offset: -1px;
}

:host([showDebugOverlay]) obc-readout-block::part(degree),
:host([showDebugOverlay]) .degree-column {
  outline: 1px solid rgba(0, 0, 220, 0.7);
  outline-offset: -1px;
}

:host([showDebugOverlay]) .degree-spacer {
  outline: 1px solid rgba(0, 160, 0, 0.8);
  outline-offset: -1px;
}
`;function ju(e,t){return{showZeroPadding:!1,minValueLength:e,fractionDigits:t}}function Mu(e,t,n){return e===null||t===void 0||!Number.isFinite(e)||!Number.isFinite(t)?!1:tu(e,n)===tu(t,n)}function Nu(e){switch(e){case Du.large:return Bl.l;case Du.medium:return Bl.m;default:return Bl.s}}function Pu(e){switch(e){case Du.large:return Bl.s;case Du.medium:return Bl.s;default:return Bl.xs}}function Fu(e){return e.emphasized||e.equalSize?e.primary:e.secondary}function Iu(e){return e.setpointEmphasized&&!e.equalSize?e.secondary:e.primary}function Lu(e){return e?Vl.semibold:Vl.regular}function Ru(e){return{"data-low-integrity":e===Ou.lowIntegrity,"data-invalid":e===Ou.invalid}}function zu(e,t){return e?t:q.none}var Bu=o`* {
  -webkit-tap-highlight-color: transparent;
}

* {
  box-sizing: border-box;
}

:host {
  display: block;
  width: 100%;
}

obc-readout-block {
  --obc-readout-block-value-color: var(
    --obc-readout-list-item-value-color,
    var(--element-neutral-color)
  );
  --obc-readout-block-value-enhanced-color: var(
    --obc-readout-list-item-value-enhanced-color,
    var(--element-neutral-enhanced-color)
  );
  --obc-readout-block-setpoint-color: var(
    --obc-readout-list-item-setpoint-color,
    var(--element-neutral-color)
  );
  --obc-readout-block-setpoint-enhanced-color: var(
    --obc-readout-list-item-setpoint-enhanced-color,
    var(--instrument-enhanced-secondary-color)
  );
  --obc-readout-block-setpoint-touching-outline-color: var(
    --obc-readout-list-item-setpoint-touching-outline-color,
    var(--element-neutral-enhanced-color)
  );
  --obc-readout-block-setpoint-touching-color: var(
    --obc-readout-list-item-setpoint-touching-color,
    var(--base-blue-100)
  );
  --obc-readout-block-advice-color: var(
    --obc-readout-list-item-advice-color,
    var(--element-neutral-color)
  );
  --obc-readout-block-hinted-color: var(
    --obc-readout-list-item-hinted-color,
    var(--element-disabled-color)
  );
}

::slotted([slot="value-icon"]),
  ::slotted([slot="setpoint-icon"]),
  ::slotted([slot="advice-icon"]) {
    display: block;
    inline-size: 100%;
    block-size: 100%;
  }

/* ---------- Root / surface ----------
 * \`.root\` is the touch target (a <button> when clickable, otherwise a <div>).
 * \`.surface\` is the visible box that carries padding, corner radius, the
 * data-quality background/border, and — when clickable — the flat interaction
 * states. */
.root {
  display: block;
  inline-size: 100%;
  margin: 0;
  /* Neutralise the native <button> chrome (default padding + appearance) when
     \`.root\` is the clickable touch target, so clickable rows don't inset their
     \`.surface\` and misalign with non-clickable \`<div>\` rows. */
  padding: 0;
  border: none;
  background: none;
  appearance: none;
  font: inherit;
  color: inherit;
  text-align: inherit;
}

.root.clickable {
  cursor: pointer;
  /* prettier-ignore */
}

.root.clickable {
  cursor: pointer;
}

.root.clickable:focus {
  outline: none;
}

.root.clickable .surface {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.root.clickable.activated .surface {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

.root.clickable:hover .surface {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.root.clickable:active .surface {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

.root.clickable:focus-visible .surface {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.root.clickable:disabled .surface {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.root.clickable.disabled .surface {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.root.clickable:disabled {
  cursor: not-allowed;
}

.root.clickable.disabled {
  cursor: not-allowed;
}

.root.clickable:focus {
  outline: none;
}

/* Flip-flop: animate the value↔setpoint cap-height swap by forwarding obc-textbox's
   opt-in size-transition var. 300ms matches the instrument setpoint marker
   (svghelpers/setpoint.ts). Override via \`--obc-readout-list-item-flip-flop-duration\`. */
.root.flip-flop {
  --obc-textbox-size-transition: var(
    --obc-readout-list-item-flip-flop-duration,
    300ms
  );
}

.surface {
  display: block;
  inline-size: 100%;
  border-radius: var(--global-border-radius-border-radius-base);
}

/* Clickable corner variants. The \`.clickable\` qualifier is redundant for
   matching (a \`border-*\` class is only ever set alongside \`.clickable\`) but
   raises specificity to (0,4,0) so the interactive corner shape wins over the
   data-quality rules below — which also target \`.surface\` at (0,3,0) — when a
   row is both clickable and low-integrity/invalid. Standalone data-quality rows
   keep their own radius. */
.root.clickable.border-squared .surface {
  border-radius: 0;
}
.root.clickable.border-round-corners .surface {
  border-radius: var(--global-border-radius-border-radius-floating);
}
.root.clickable.border-round .surface {
  border-radius: var(--global-border-radius-border-radius-round);
}

/* ---------- Content row ----------
 * Label on the left, value/unit cluster on the right, optional source after a
 * trailing divider. All segments bottom-align so cap heights sit on a shared
 * baseline. */
.content {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  inline-size: 100%;
  min-inline-size: 0;
}

/* Reserve the value cap-height per tier so the row height and the bottom
   baseline stay constant regardless of which parts (label / value / unit / src /
   setpoint / advice / icons) are present. */
.size-small .content {
  min-block-size: var(
    --global-typography-instrument-value-regular-container-height
  );
}
.size-medium .content {
  min-block-size: var(
    --global-typography-instrument-value-medium-container-height
  );
}
.size-large .content {
  min-block-size: var(
    --global-typography-instrument-value-large-container-height
  );
}

/* The value is the primary data, so under width pressure the label side yields
   first: the label-container shrinks (and clips a too-long label) while
   \`.value-area\` keeps its intrinsic width. */
.label-container {
  display: inline-flex;
  align-items: flex-end;
  gap: var(--global-size-spacing-target-padding);
  flex: 1 1 auto;
  min-inline-size: 0;
  overflow: clip;
  /* a leading-src chip's 1px outline is drawn outside its box at the container edge */
  overflow-clip-margin: 1px;
}

.label-stack {
  display: inline-flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-end;
  min-inline-size: 0;
}

.value-area {
  margin-inline-start: auto; /* right-aligns a label-less row's value, which has no label container to push it */
  display: inline-flex;
  align-items: flex-end;
  justify-content: flex-end;
  flex: 0 0 auto;
  min-inline-size: 0;
}

.value-cluster {
  display: inline-flex;
  align-items: flex-end;
  justify-content: flex-end;
}

.unit-area {
  display: inline-flex;
  align-items: flex-end;
}

/* ---------- Value reading (value + degree + unit) ----------
 * Groups the value block, its degree column and the trailing unit so the value
 * alert frame can wrap all three. Layout-neutral: it adds no gap, so the content
 * sits exactly where it did when these were siblings of \`.value-area\`. */
.value-reading {
  position: relative;
  display: inline-flex;
  align-items: flex-end;
}

/* ---------- Value data quality (low-integrity / invalid) ----------
 * The value's per-block data-quality chip, applied to the whole reading (value +
 * degree + unit) rather than hugging the value alone — the same logic as the
 * value alert frame, minus its custom padding. Same look as the block/source
 * chip (1px outline, check radius, alert-quality colours). Uses \`outline\` (not
 * \`border\`) so it never shifts the value's width / cross-row column alignment.
 * Setpoint/advice keep their own in-block chip; the row-level data quality on
 * \`.surface\` is unchanged. */
.value-reading.data-low-integrity,
.value-reading.data-invalid {
  outline: 1px solid;
  border-radius: var(--global-border-radius-border-radius-check);
}
.value-reading.data-low-integrity {
  background: var(--alert-low-integrity-background-color);
  outline-color: var(--alert-low-integrity-border-color);
}
.value-reading.data-invalid {
  background: var(--alert-invalid-background-color);
  outline-color: var(--alert-invalid-border-color);
}

/* ---------- Value alert overlay ----------
 * Reserves no space, so the frame never changes the row height or the column
 * alignment. The box sits on the 4px/2px padding line, where obc-alert-frame
 * centres its stroke (Figma 58:10120). */
.value-alert-overlay {
  --_obc-readout-value-frame-padding-horizontal: 4px;
  --_obc-readout-value-frame-padding-vertical: 2px;
  position: absolute;
  inset-inline: calc(-1 * var(--_obc-readout-value-frame-padding-horizontal));
  inset-block: calc(-1 * var(--_obc-readout-value-frame-padding-vertical));
  /* Display-only: never intercept clicks on a clickable row. */
  pointer-events: none;
}

/* The readout building blocks (advice / setpoint / value) now render inside
   \`obc-readout-block\`; their layout / colour / hinted-zero / data-quality CSS
   lives there. The list-item only bridges the public colour vars (see top) and
   keeps the surrounding row layout below. */

.label {
  color: var(
    --obc-readout-list-item-label-color,
    var(--element-inactive-color)
  );
}
.unit {
  color: var(--obc-readout-list-item-unit-color, var(--element-inactive-color));
}
.source {
  color: var(
    --obc-readout-list-item-source-color,
    var(--element-neutral-color)
  );
}

/* ---------- Source data quality ----------
 * Independent of (and nests inside) the row-level data-quality frame. Uses
 * \`outline\` (not \`border\`) so the chip never shifts the source's width. (The
 * per-block value/setpoint/advice chips live in \`obc-readout-block\`.) */
.source.data-low-integrity,
.source.data-invalid {
  outline: 1px solid;
  border-radius: var(--global-border-radius-border-radius-check);
}
.source.data-low-integrity {
  background: var(--alert-low-integrity-background-color);
  outline-color: var(--alert-low-integrity-border-color);
}
.source.data-invalid {
  background: var(--alert-invalid-background-color);
  outline-color: var(--alert-invalid-border-color);
}

/* ---------- Source state chip & deviation (Figma 6.1 Readout-block-source)
 * \`enhanced\` renders the amplified chip, \`caution\`/\`warning\` the alert chip.
 * Like the data-quality chip these use \`outline\`, so toggling a state never
 * shifts the row. TODO(designer): Figma pads the chip 4px; a padding here
 * would shift the row on live state changes, so the chip hugs the text like
 * the data-quality chip does. */
.source-block {
  display: inline-flex;
  flex-direction: column;
  align-items: flex-start;
}
.source-block.source-state-enhanced,
.source-block.source-state-caution,
.source-block.source-state-warning {
  outline: 1px solid;
  border-radius: var(--global-border-radius-border-radius-check);
}
.source-block.source-state-enhanced {
  background: var(--amplified-enabled-background-color);
  outline-color: var(--amplified-enabled-border-color);
}
.source-block.source-state-enhanced .source,
.source-block.source-state-enhanced .source-deviation {
  color: var(--on-amplified-active-color);
}
.source-block.source-state-caution {
  background: var(--alert-caution-color);
  outline-color: var(--alert-caution-outline-color);
}
.source-block.source-state-caution .source,
.source-block.source-state-caution .source-deviation {
  color: var(--on-caution-active-color);
}
.source-block.source-state-warning {
  background: var(--alert-warning-color);
  outline-color: var(--alert-warning-outline-color);
}
.source-block.source-state-warning .source,
.source-block.source-state-warning .source-deviation {
  color: var(--on-warning-active-color);
}

.source-deviation {
  display: inline-flex;
  align-items: center;
  gap: 2px;
  color: var(--element-inactive-color);
}
.source-deviation obi-delta {
  display: block;
  inline-size: 12px;
  block-size: 12px;
}

.leading-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex: none;
  color: var(--element-neutral-color);
}
.leading-icon ::slotted(*) {
  display: block;
  inline-size: 100%;
  block-size: 100%;
}

.divider {
  flex: none;
  inline-size: 1px;
  background-color: var(--border-outline-color);
  align-self: stretch;
}

/* ---------- Value↔unit gap & degree column ----------
 * Default 2px between the value digits and the unit. A degree (or a
 * hasDegreeSpacer reserve) replaces the 2px with a cap-height degree column
 * whose width scales with the value size, so value digits + units align across
 * degree / no-degree rows of the same value size. */
.value-unit-gap {
  flex: none;
  inline-size: var(
    --instrument-components-readout-general-horizontal-trim-padding
  );
}

.degree-column {
  flex: none;
  display: inline-flex;
  align-items: flex-end;
  justify-content: center;
  inline-size: var(--_obc-readout-list-item-degree-width, 0);
  overflow: clip;
  color: var(--obc-readout-list-item-value-color, var(--element-neutral-color));
}
.degree-column.tone-enhanced {
  color: var(
    --obc-readout-list-item-value-enhanced-color,
    var(--element-neutral-enhanced-color)
  );
}
/* Setpoint/advice degree glyphs inherit their block's colour. */
.degree-column.degree-inherit {
  color: inherit;
}
.degree-column.degree-xs {
  --_obc-readout-list-item-degree-width: var(
    --global-typography-instrument-value-small-degree-unit-width
  );
}
.degree-column.degree-s {
  --_obc-readout-list-item-degree-width: var(
    --global-typography-instrument-value-regular-degree-unit-width
  );
}
.degree-column.degree-m {
  --_obc-readout-list-item-degree-width: var(
    --global-typography-instrument-value-medium-degree-unit-width
  );
}
.degree-column.degree-l,
.degree-column.degree-xl {
  --_obc-readout-list-item-degree-width: var(
    --global-typography-instrument-value-large-degree-unit-width
  );
}

/* Degree spacer: rendered AFTER the unit on a non-degree row that sets
   hasDegreeSpacer. Its width (degree-compensation-padding = degree-column width
   minus the 2px value↔unit gap) shifts the unit left so the row's value digits
   stay aligned with degree rows in the same column. */
.degree-spacer {
  flex: none;
  align-self: stretch;
  inline-size: var(--_obc-readout-list-item-degree-spacer-width, 0);
}
.size-small .degree-spacer {
  --_obc-readout-list-item-degree-spacer-width: var(
    --instrument-components-readout-list-item-regular-degree-compensation-padding
  );
}
.size-medium .degree-spacer {
  --_obc-readout-list-item-degree-spacer-width: var(
    --instrument-components-readout-list-item-medium-degree-compensation-padding
  );
}
.size-large .degree-spacer {
  --_obc-readout-list-item-degree-spacer-width: var(
    --instrument-components-readout-list-item-large-degree-compensation-padding
  );
}

/* ---------- Size tiers ----------
 * Public small/medium/large map to the design token regular/medium/large
 * tiers. */
.size-small .surface {
  padding-inline: var(
    --instrument-components-readout-list-item-regular-container-padding-horizontal
  );
  padding-block: var(
    --instrument-components-readout-list-item-regular-container-padding-vertical
  );
}
.size-small .content {
  gap: var(
    --instrument-components-readout-list-item-regular-content-container-gap
  );
}
.size-small .value-cluster {
  gap: var(
    --instrument-components-readout-list-item-regular-value-container-gap
  );
}
.size-small .leading-icon {
  inline-size: var(--instrument-components-readout-general-regular-icon-size);
  block-size: var(--instrument-components-readout-general-regular-icon-size);
}
.size-small .divider {
  block-size: var(
    --global-typography-instrument-value-regular-container-height
  );
}

.size-medium .surface {
  padding-inline: var(
    --instrument-components-readout-list-item-medium-container-padding-horizontal
  );
  padding-block: var(
    --instrument-components-readout-list-item-medium-container-padding-vertical
  );
}
.size-medium .content {
  gap: var(
    --instrument-components-readout-list-item-medium-content-container-gap
  );
}
.size-medium .value-cluster {
  gap: var(
    --instrument-components-readout-list-item-medium-value-container-gap
  );
}
.size-medium .leading-icon {
  inline-size: var(--instrument-components-readout-general-medium-icon-size);
  block-size: var(--instrument-components-readout-general-medium-icon-size);
}
.size-medium .divider {
  block-size: var(--global-typography-instrument-value-medium-container-height);
}

.size-large .surface {
  padding-inline: var(
    --instrument-components-readout-list-item-large-container-padding-horizontal
  );
  padding-block: var(
    --instrument-components-readout-list-item-large-container-padding-vertical
  );
  min-block-size: var(
    --instrument-components-readout-list-item-large-min-height
  );
}
.size-large .content {
  gap: var(--instrument-components-readout-list-item-large-content-gap);
}
.size-large .value-cluster {
  gap: var(--instrument-components-readout-list-item-large-value-gap);
}
.size-large .leading-icon {
  inline-size: var(--instrument-components-readout-general-large-icon-size);
  block-size: var(--instrument-components-readout-general-large-icon-size);
}
.size-large .divider {
  block-size: var(--global-typography-instrument-value-large-container-height);
}

/* ---------- Stacking ----------
 * leading-unit / leading-src move the unit / source up beside the label and
 * suppress the trailing variant. (Handled in markup; these rules tighten the
 * label-stack gap.) */
.stacking-leading-src .content {
  gap: var(--global-size-spacing-target-padding);
}

/* leading-src-inline: the source follows the label on one line, bottom-aligned
   so the \`xs\` source and the label share a cap baseline. The label↔source gap
   reuses the tier's content gap (8px, matching Figma 46596:102880). */
.stacking-leading-src-inline .label-stack {
  flex-direction: row;
  align-items: flex-end;
}
.size-small.stacking-leading-src-inline .label-stack {
  gap: var(
    --instrument-components-readout-list-item-regular-content-container-gap
  );
}
.size-medium.stacking-leading-src-inline .label-stack {
  gap: var(
    --instrument-components-readout-list-item-medium-content-container-gap
  );
}
.size-large.stacking-leading-src-inline .label-stack {
  gap: var(--instrument-components-readout-list-item-large-content-gap);
}

/* ---------- Data quality ----------
 * Orthogonal to the alert frame — both can apply at once. */
.root.data-low-integrity .surface,
.root.data-invalid .surface {
  /* \`outline\` (not \`border\`) so the data-quality frame does not inset the
     content by 1px — keeps the row's value column-aligned with unframed rows.
     Matches the per-block data-quality rules. */
  outline: 1px solid var(--_obc-readout-list-item-data-border);
  background: var(--_obc-readout-list-item-data-background);
  border-radius: var(--global-border-radius-border-radius-check);
}
.root.data-low-integrity {
  --_obc-readout-list-item-data-background: var(
    --alert-low-integrity-background-color
  );
  --_obc-readout-list-item-data-border: var(--alert-low-integrity-border-color);
}
.root.data-invalid {
  --_obc-readout-list-item-data-background: var(
    --alert-invalid-background-color
  );
  --_obc-readout-list-item-data-border: var(--alert-invalid-border-color);
}

/* ---------- Debug overlay ----------
 * \`showDebugOverlay\` outlines each readout building block (red), the degree
 * columns (blue) and the degree spacer (green) so reserver widths / alignment
 * are visible. A development aid (mirrors the donut chart's \`showDebugOverlay\`);
 * off by default. */
:host([showDebugOverlay]) obc-readout-block::part(block) {
  outline: 1px solid rgba(220, 0, 0, 0.7);
  outline-offset: -1px;
}
:host([showDebugOverlay]) obc-readout-block::part(degree),
:host([showDebugOverlay]) .degree-column {
  outline: 1px solid rgba(0, 0, 220, 0.7);
  outline-offset: -1px;
}
:host([showDebugOverlay]) .degree-spacer {
  outline: 1px solid rgba(0, 160, 0, 0.8);
  outline-offset: -1px;
}
`,Vu,Hu=Du,Uu=Ou,Wu=function(e){return e.alwaysVisible=`always-visible`,e.equalSize=`equal-size`,e.flipFlop=`flip-flop`,e.popUp=`pop-up`,e}({}),Gu=function(e){return e.regular=`regular`,e.enhanced=`enhanced`,e.caution=`caution`,e.warning=`warning`,e}({}),Y=(Vu=class extends j{constructor(...e){super(...e),this.hasValue=!0,this.value=null,this.valueType=Ul.number,this.off=!1,this.offText=`OFF`,this.hasSetpoint=!1,this.hasAdvice=!1,this.clickable=!1,this.hasLeadingIcon=!1,this.hasDegree=!1,this.hasDegreeSpacer=!1,this.fractionDigits=0,this.maxDigits=0,this.alert=!1,this.showDebugOverlay=!1,this.deferredSetpointHidePhase=q.none,this.hasCompletedFirstUpdate=!1}get resolvedSize(){return this.size??Hu.small}get resolvedStacking(){return this.stacking??`trailing-unit`}get hasLeadingSrc(){let e=this.resolvedStacking;return e===`leading-src`||e===`leading-src-inline`}get resolvedPriority(){return this.priority??`regular`}get hasTrailingUnitBox(){return this.resolvedStacking!==`leading-unit`&&(!!this.unit||!!this.unitOptions?.spaceReserver)}get resolvedFractionDigits(){return this.fractionDigits??0}get resolvedMaxDigits(){return Jl(this.maxDigits)}get digitCountsMissing(){return Yl(this.fractionDigits)||Yl(this.maxDigits)}get resolvedClickable(){let e=this.clickable;return e?e===!0?{border:`squared`}:{border:e.border??`squared`}:!1}get isAtSetpoint(){return!this.hasSetpoint||this.digitCountsMissing?!1:Mu(Ql(this.value,this.valueType)??null,this.setpoint,this.numericFormatOptions(this.resolvedMaxDigits))}get resolvedSetpointInteraction(){return this.setpointOptions?.interaction??`always-visible`}get isFlipFlop(){return this.resolvedSetpointInteraction===`flip-flop`}get isEqualSize(){return this.resolvedSetpointInteraction===`equal-size`}get isPopUp(){return this.resolvedSetpointInteraction===`pop-up`}get setpointTouching(){return this.setpointOptions?.touching??!1}get isSetpointEmphasized(){return this.hasSetpoint?this.setpointTouching?!0:this.isFlipFlop&&!this.isAtSetpoint:!1}get rowEnhanced(){return this.resolvedPriority===`enhanced`}get primarySize(){return Nu(this.resolvedSize)}get secondarySize(){return Pu(this.resolvedSize)}get valueSize(){return Iu({primary:this.primarySize,secondary:this.secondarySize,setpointEmphasized:this.isSetpointEmphasized,equalSize:this.isEqualSize})}get setpointSize(){return Fu({primary:this.primarySize,secondary:this.secondarySize,emphasized:this.isSetpointEmphasized,equalSize:this.isEqualSize})}get valueWeight(){return this.valueOptions?.weight??Vl.regular}get labelSize(){return this.labelOptions?.size??Bl.xs}get labelWeight(){return this.rowEnhanced?Vl.semibold:Vl.regular}get setpointWeight(){return Lu(this.isSetpointEmphasized)}numericFormatOptions(e){return ju(e,this.resolvedFractionDigits)}dataQualityClasses(e){return Ru(e)}renderForwardedIcon(e){return e===Eu.setpoint?O`<slot name="setpoint-icon" slot="icon"></slot>`:e===Eu.advice?O`<slot name="advice-icon" slot="icon"></slot>`:O`<slot name="value-icon" slot="icon"></slot>`}renderBlock(e){return O`
      <obc-readout-block
        exportparts="block, block-content, block-text, block-icon, degree"
        .variant=${e.variant}
        .value=${e.value??null}
        .valueType=${e.valueType??Ul.number}
        .size=${this.resolvedSize}
        .valueSize=${e.valueSize}
        .enhanced=${e.enhanced}
        .weight=${e.weight}
        .hasDegree=${e.hasDegree??!1}
        .hasIcon=${e.hasIcon??!1}
        .fractionDigits=${this.fractionDigits}
        .maxDigits=${this.maxDigits}
        .hintedZeros=${e.hintedZeros}
        .hasSignSpacer=${e.hasSignSpacer??!1}
        .spaceReserver=${e.spaceReserver}
        .off=${e.off??!1}
        .offText=${this.offText}
        .touching=${e.touching??!1}
        .hidePhase=${e.hidePhase??q.none}
        .dataQuality=${e.dataQuality}
        .alert=${e.alert??!1}
        .category=${e.category??ku.regular}
        .active=${e.active??!1}
      >
        ${this.renderForwardedIcon(e.variant)}
      </obc-readout-block>
    `}renderDegreeGlyph(e,t={}){return O`
      <span
        class=${F({"degree-column":!0,[`degree-${e}`]:!0,"tone-enhanced":!t.inherit&&!!t.enhanced,"degree-inherit":!!t.inherit})}
        part="degree"
      >
        <obc-textbox class="degree-glyph" .size=${e} alignment="center"
          >°</obc-textbox
        >
      </span>
    `}renderValueUnitGap(){return this.hasValue?(this.hasDegree??!1)&&!this.off?this.renderDegreeGlyph(this.valueSize,{enhanced:this.rowEnhanced}):this.hasTrailingUnitBox?O`<span class="value-unit-gap" aria-hidden="true"></span>`:A:A}renderDegreeSpacer(){let e=this.hasDegree??!1,t=this.hasDegreeSpacer??!1;return e||!t?A:O`<span
      class="degree-spacer"
      part="degree-spacer"
      aria-hidden="true"
    ></span>`}renderTextbox(e,t,n,r){let i=e===`label`?this.labelWeight:Vl.regular,a=e===`label`?this.labelSize:Bl.xs,o=O`
      <obc-textbox
        class=${F({[e]:!0,...this.dataQualityClasses(r?.dataQuality)})}
        part=${e}
        .size=${a}
        .fontWeight=${i}
        alignment="left"
      >
        ${t}
        ${n?O`<span slot="length">${n}</span>`:A}
      </obc-textbox>
    `;return Il(r?.alert??!1,o)}renderValueCluster(){let e=zu(this.isPopUp&&this.isAtSetpoint&&!this.setpointTouching,this.deferredSetpointHidePhase);return O`
      <div class="value-cluster" part="value-cluster">
        ${this.hasAdvice?this.renderBlock({variant:Eu.advice,value:this.advice,valueSize:this.secondarySize,enhanced:!1,weight:Vl.regular,hintedZeros:this.adviceOptions?.hintedZeros??!1,hasSignSpacer:this.adviceOptions?.hasSignSpacer??!1,spaceReserver:this.adviceOptions?.spaceReserver,hasDegree:this.hasDegree??!1,dataQuality:this.adviceOptions?.dataQuality,alert:this.adviceOptions?.alert,category:this.adviceOptions?.category,active:this.adviceOptions?.active}):A}
        ${this.hasSetpoint?this.renderBlock({variant:Eu.setpoint,value:this.setpoint,valueSize:this.setpointSize,enhanced:this.rowEnhanced,weight:this.setpointWeight,hintedZeros:this.setpointOptions?.hintedZeros??!1,hasSignSpacer:this.setpointOptions?.hasSignSpacer??!1,spaceReserver:this.setpointOptions?.spaceReserver,hasDegree:this.hasDegree??!1,touching:this.setpointTouching,hidePhase:e,dataQuality:this.setpointOptions?.dataQuality,alert:this.setpointOptions?.alert}):A}
        ${this.renderValueReading()}
      </div>
    `}renderValueReading(){return O`
      <div
        class=${F({"value-reading":!0,...this.dataQualityClasses(this.valueOptions?.dataQuality)})}
        part="value-reading"
      >
        ${this.hasValue?this.renderBlock({variant:Eu.value,value:this.value,valueType:this.valueType,valueSize:this.valueSize,enhanced:this.rowEnhanced,weight:this.valueWeight,hintedZeros:this.valueOptions?.hintedZeros??!1,hasSignSpacer:this.valueOptions?.hasSignSpacer??!1,spaceReserver:this.valueOptions?.spaceReserver,off:this.off,hasIcon:this.valueOptions?.hasIcon??!1}):A}
        ${this.renderValueUnitGap()}
        <div class="unit-area" part="unit-area">
          ${this.renderTrailingUnit()} ${this.renderDegreeSpacer()}
        </div>
        ${this.renderValueAlertOverlay()}
      </div>
    `}renderValueAlertOverlay(){let e=this.valueOptions?.alert;if(typeof e!=`object`||!e)return A;let t=e.thickness??jl.Small;return O`
      <div class="value-alert-overlay" aria-hidden="true">
        <obc-alert-frame
          part="value-alert-frame"
          .type=${e.type??Al.Regular}
          .thickness=${t}
          .status=${e.status??B.Alarm}
          .mode=${e.mode??Ml.ackedActive}
          .flashingSpeed=${e.flashingSpeed??V.Default}
          .showIcon=${e.showIcon??!1}
          .showAlertCategoryIcon=${e.showAlertCategoryIcon??!0}
          .wrapContent=${!1}
          .fullWidth=${!1}
        ></obc-alert-frame>
      </div>
    `}renderLabelContainer(){let e=this.resolvedStacking===`leading-unit`&&!!this.unit,t=this.hasLeadingSrc&&!!this.src;return!this.hasLeadingIcon&&!this.label&&!e&&!t?A:O`
      <div class="label-container" part="label-container">
        ${this.hasLeadingIcon?O`<span class="leading-icon" aria-hidden="true"
                ><slot name="leading-icon"></slot
              ></span>`:A}
        <div class="label-stack" part="label-stack">
          ${this.label?this.renderTextbox(`label`,this.label,this.labelOptions?.spaceReserver):A}
          ${e?this.renderTextbox(`unit`,this.unit??``,this.unitOptions?.spaceReserver):A}
          ${t?this.renderSourceBlock():A}
        </div>
      </div>
    `}renderTrailingUnit(){return this.hasTrailingUnitBox?this.renderTextbox(`unit`,this.unit??``,this.unitOptions?.spaceReserver):A}renderSourceBlock(){let e=this.srcOptions?.state??`regular`,t=this.srcOptions?.deviation,n=t!==void 0&&Number.isFinite(t),r=this.renderTextbox(`source`,this.src??``,this.srcOptions?.spaceReserver,this.srcOptions);return e===`regular`&&!n?r:O`
      <div
        class=${F({"source-block":!0,[`source-state-${e}`]:e!==`regular`})}
        part="source-block"
      >
        ${r}
        ${n?O`<span class="source-deviation">
                <obi-delta aria-hidden="true"></obi-delta>
                <obc-textbox
                  class="source-deviation-value"
                  .size=${Bl.xs}
                  .tabularNums=${!0}
                  alignment="left"
                  >${t}</obc-textbox
                >
              </span>`:A}
      </div>
    `}renderTrailingSource(){return this.hasLeadingSrc||!this.src?A:O`
      <div class="divider" part="divider" aria-hidden="true"></div>
      ${this.renderSourceBlock()}
    `}renderContent(){return O`
      <div class="content" part="content">
        ${this.renderLabelContainer()}
        <div class="value-area" part="value-area">
          ${this.renderValueCluster()}
        </div>
        ${this.renderTrailingSource()}
      </div>
    `}willUpdate(e){super.willUpdate(e),Zl(`obc-readout-list-item`,this.value,this.valueType),ql(`obc-readout-list-item`,this.fractionDigits)}updated(e){super.updated(e);let t=!this.hasCompletedFirstUpdate;if(this.hasCompletedFirstUpdate=!0,!this.isPopUp||this.setpointTouching){this.clearDeferredSetpointHide();return}let n=this.hasSetpoint&&this.isAtSetpoint;if(t){this.deferredSetpointHidePhase=n?q.hidden:q.none;return}if(!n){this.clearDeferredSetpointHide();return}this.deferredSetpointHidePhase===q.none&&(this.deferredSetpointHidePhase=q.hiding,window.clearTimeout(this.deferredSetpointHideTimer),this.deferredSetpointHideTimer=window.setTimeout(()=>{this.deferredSetpointHidePhase=q.hidden,this.deferredSetpointHideTimer=void 0},100))}clearDeferredSetpointHide(){this.deferredSetpointHidePhase!==q.none&&(this.deferredSetpointHidePhase=q.none),window.clearTimeout(this.deferredSetpointHideTimer),this.deferredSetpointHideTimer=void 0}disconnectedCallback(){window.clearTimeout(this.deferredSetpointHideTimer),this.deferredSetpointHideTimer=void 0,this.deferredSetpointHidePhase===q.hiding&&(this.deferredSetpointHidePhase=q.hidden),super.disconnectedCallback()}render(){let e=this.resolvedClickable,t=this.dataQuality,n=F({root:!0,[`size-${this.resolvedSize}`]:!0,[`stacking-${this.resolvedStacking}`]:!0,[`priority-${this.resolvedPriority}`]:!0,"data-low-integrity":t===Uu.lowIntegrity,"data-invalid":t===Uu.invalid,"flip-flop":this.isFlipFlop,clickable:!!e,[`border-${e?e.border:`squared`}`]:!!e}),r=O`<div class="surface" part="surface">
      ${this.renderContent()}
    </div>`,i=e?O`<button class=${n} part="root" type="button">
          ${r}
        </button>`:O`<div class=${n} part="root">${r}</div>`;return Il(this.alert===!0?{}:this.alert,i,!0)}},Vu.styles=a(Bu),Vu);N([P({type:String})],Y.prototype,`label`,void 0),N([P({type:String})],Y.prototype,`unit`,void 0),N([P({type:String})],Y.prototype,`src`,void 0),N([P({type:Boolean,attribute:!1})],Y.prototype,`hasValue`,void 0),N([P({type:String})],Y.prototype,`value`,void 0),N([P({type:String})],Y.prototype,`valueType`,void 0),N([P({type:Boolean})],Y.prototype,`off`,void 0),N([P({type:String})],Y.prototype,`offText`,void 0),N([P({type:Boolean})],Y.prototype,`hasSetpoint`,void 0),N([P({type:Number})],Y.prototype,`setpoint`,void 0),N([P({type:Boolean})],Y.prototype,`hasAdvice`,void 0),N([P({type:Number})],Y.prototype,`advice`,void 0),N([P({type:String})],Y.prototype,`size`,void 0),N([P({type:String})],Y.prototype,`priority`,void 0),N([P({type:String})],Y.prototype,`stacking`,void 0),N([P({type:Object})],Y.prototype,`clickable`,void 0),N([P({type:Boolean})],Y.prototype,`hasLeadingIcon`,void 0),N([P({type:Boolean})],Y.prototype,`hasDegree`,void 0),N([P({type:Boolean})],Y.prototype,`hasDegreeSpacer`,void 0),N([P({type:Number})],Y.prototype,`fractionDigits`,void 0),N([P({type:Number})],Y.prototype,`maxDigits`,void 0),N([P({type:String})],Y.prototype,`dataQuality`,void 0),N([P({type:Object})],Y.prototype,`alert`,void 0),N([P({type:Object})],Y.prototype,`valueOptions`,void 0),N([P({type:Object})],Y.prototype,`setpointOptions`,void 0),N([P({type:Object})],Y.prototype,`adviceOptions`,void 0),N([P({type:Object})],Y.prototype,`labelOptions`,void 0),N([P({type:Object})],Y.prototype,`unitOptions`,void 0),N([P({type:Object})],Y.prototype,`srcOptions`,void 0),N([P({type:Boolean,reflect:!0})],Y.prototype,`showDebugOverlay`,void 0),N([ze()],Y.prototype,`deferredSetpointHidePhase`,void 0),Y=N([M(`obc-readout-list-item`)],Y);var Ku=o`* {
    -webkit-tap-highlight-color: transparent;
}

:host([popover]) {
    /* The browser pins a popover to all four edges and lets the automatic
       margins centre it. Unpinning drops it back where it would normally sit,
       for the consumer to position from. */
    inset: auto;
    margin: 0;

    padding: 0;
    border: none;
    background: none;
    color: inherit;

    /* The menus scroll their own content. */
    overflow: visible;

    /* The browser shrink-wraps a popover to its contents. */
    width: auto;
    height: auto;
  }

/* Context Menu Base Styles */
.context-menu {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  background: var(--container-global-color);
  border-radius: var(--ui-components-context-menu-border-radius);
  box-shadow: var(--shadow-floating-x) var(--shadow-floating-y)
    var(--shadow-floating-blur) var(--shadow-raised-spread)
    var(--shadow-floating-color);
  padding: var(--ui-components-context-menu-margin-vertical)
    var(--ui-components-context-menu-margin-horizontal);
  overflow-y: auto;
  min-width: 160px;
  width: fit-content;
  box-sizing: border-box;
}

.title-container {
  display: flex;
  align-items: center;
  align-self: stretch;
  border-bottom: 1px solid var(--border-divider-color);
}

.title-container obc-icon-button::part(icon) {
  color: var(--element-neutral-color);
}

.title-content {
  display: flex;
  padding: 0px var(--ui-components-context-menu-title-label-spacing);
  justify-content: center;
  align-items: center;
  gap: 10px;
  flex: 1 0 0;
}

.title-text {
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-overline-font-weight);
  font-size: var(--global-typography-ui-overline-font-size);
  line-height: var(--global-typography-ui-overline-line-height);
  letter-spacing: var(--global-typography-ui-overline-letter-spacing);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  color: var(--element-neutral-color);
  flex: 1 0 0;
}

/* Menu Content Container */
.menu-content {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.context-menu.type-multi,
.context-menu.type-multi-with-subtitles {
  padding: 0;
  width: max-content;
}

/* Base Menu Item Wrapper Styles */
.menu-item {
  width: 100%;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* Nested Checkbox Styles */
.checkbox-item-wrapper.nested {
  padding-left: var(--ui-components-checkbox-nested-item-padding-left);
}

/* Multi-Column Styles */
.multi-content {
  width: 100%;
  display: flex;
  flex-direction: column;
}

.multi-columns {
  display: flex;
  flex-direction: row;
  width: 100%;
}

.columns-container {
  display: flex;
  align-items: flex-start;
  width: max-content;
  flex: 1;
}

/* Standard multi-column layout */
.type-multi .column {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: var(--ui-components-context-menu-margin-vertical)
    var(--ui-components-context-menu-margin-horizontal);
  min-width: 240px;
  width: fit-content;
}

.type-multi .column.column-divider {
  border-left: 1px solid var(--border-divider-color);
}

.type-multi-with-subtitles .columns-container {
  display: flex;
  align-items: stretch;
  width: max-content;
  flex: 1;
}

.type-multi-with-subtitles .column-with-header {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex: none;
  min-width: 240px;
  padding: 0;
  height: 100%; /* Ensure full height */
}

.type-multi-with-subtitles .column-header {
  display: flex;
  height: var(--ui-components-context-menu-touch-target-size);
  align-items: center;
  align-self: stretch;
  width: 100%;
  box-shadow: inset 1px 0 0 0 var(--border-divider-color);
}

.type-multi-with-subtitles .column-header .subtitle-container {
  display: flex;
  padding: 0px var(--ui-components-context-menu-title-label-spacing);
  justify-content: flex-start;
  align-items: center;
  gap: 10px;
  flex: 1 0 0;
}

.type-multi-with-subtitles .column-header-spacer {
  height: var(--ui-components-context-menu-touch-target-size);
  width: 100%;
  user-select: none;
}

/* Remove border from the first column header and spacer */
.type-multi-with-subtitles .column-with-header:first-child .column-header,
.type-multi-with-subtitles
  .column-with-header:first-child
  .column-header-spacer {
  border-left: none;
}

.type-multi-with-subtitles .column-content {
  flex: 1; /* This makes the content area fill remaining space */
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  width: fit-content;
  min-width: 240px;
  padding: var(--ui-components-context-menu-margin-vertical)
    var(--ui-components-context-menu-margin-horizontal);
  box-shadow: inset 1px 0 0 0 var(--border-divider-color);
}

/* Remove border from the first column */
.type-multi-with-subtitles .column-with-header:first-child .column-content {
  border-left: none;
}

/* Ensure navigation items don't truncate text */
.type-multi-with-subtitles .menu-item {
  width: 100%;
  min-width: 0; /* Allow shrinking */
}

.type-multi-with-subtitles .column-header .subtitle-text {
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-overline-font-weight);
  font-size: var(--global-typography-ui-overline-font-size);
  line-height: var(--global-typography-ui-overline-line-height);
  letter-spacing: var(--global-typography-ui-overline-letter-spacing);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  color: var(--element-neutral-color);
  white-space: nowrap;
}

/* You might need to add styles for navigation groups */
obc-navigation-item-group {
  width: 100%;
}

obc-navigation-item-group::part(flyout) {
  /* Style the flyout part if needed */
  width: fit-content;
  min-width: 160px;
}
`,qu=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M18 9.41L16.59 8L12 12.58L7.41 8L6 9.41L12 15.41L18 9.41Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M18 9.41L16.59 8L12 12.58L7.41 8L6 9.41L12 15.41L18 9.41Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Ju=(qu.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,qu);N([P({type:Boolean})],Ju.prototype,`useCssColor`,void 0),Ju=N([M(`obi-chevron-down-google`)],Ju);var Yu=o`* {
  -webkit-tap-highlight-color: transparent;
}

:host {
  display: block;
}

* {
  box-sizing: border-box;
}

.checkbox-item-container {
  display: flex;
  width: 100%;
  height: var(--ui-components-checkbox-touch-target-size);
  padding: 0px var(--ui-components-checkbox-margin);
  align-items: center;
  flex-shrink: 0;
  user-select: none;
  cursor: pointer;
}

.checkbox-item-container.has-description {
    /* a second text line outgrows the fixed row; the hover surface follows */
    height: auto;
    min-height: var(--ui-components-checkbox-touch-target-size);
  }

.checkbox-item-container.disabled {
    cursor: not-allowed;
  }

.checkbox-item-container .chevron-container {
    display: flex;
    width: var(--global-size-spacing-touch-target-min);
    min-width: var(--global-size-spacing-touch-target-min);
    height: var(--global-size-spacing-touch-target-min);
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

.checkbox-item-container .nested-spacer {
    /* one indent step per level above 1; --checkbox-item-depth is set inline */
    width: calc(
      var(--checkbox-item-depth, 0) *
        var(--ui-components-checkbox-nested-item-padding-left)
    );
    flex-shrink: 0;
    align-self: stretch;
  }

:is(.checkbox-item-container .chevron-button) {
  cursor: pointer;
}

:is(.checkbox-item-container .chevron-button):focus {
  outline: none;
}

:is(.checkbox-item-container .chevron-button) .chevron-visible {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.activated:is(.checkbox-item-container .chevron-button) .chevron-visible {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

:is(.checkbox-item-container .chevron-button):hover .chevron-visible {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

:is(.checkbox-item-container .chevron-button):active .chevron-visible {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

:is(.checkbox-item-container .chevron-button):focus-visible .chevron-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

:is(.checkbox-item-container .chevron-button):disabled .chevron-visible {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.disabled:is(.checkbox-item-container .chevron-button) .chevron-visible {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

:is(.checkbox-item-container .chevron-button):disabled {
  cursor: not-allowed;
}

.disabled:is(.checkbox-item-container .chevron-button) {
  cursor: not-allowed;
}

.checkbox-item-container .chevron-button {
    appearance: none;
    border: none;
    background: transparent;
    padding: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    color: var(--on-flat-neutral-color);
  }

:is(.checkbox-item-container .chevron-button):disabled {
      cursor: not-allowed;
    }

.checkbox-item-container .chevron-visible {
    /* same visible box as obc-icon-button so the two align in one list */
    width: var(--ui-components-icon-button-visual-target-size);
    height: var(--ui-components-icon-button-visual-target-size);
    border-radius: var(--ui-components-button-border-radius-top-left);
    display: flex;
    align-items: center;
    justify-content: center;
  }

.checkbox-item-container .chevron-icon {
    width: var(--global-size-spacing-icon-icon-size-regular);
    height: var(--global-size-spacing-icon-icon-size-regular);
  }

.checkbox-item-container .checkbox-label-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-width: 0; /* lets the label ellipsis instead of widening the row */
    padding: 0 var(--global-size-spacing-list-item-padding-vertical) 0 0;
    margin-left: calc(
      var(--global-size-spacing-list-item-padding-vertical) / -2
    );
    flex-grow: 1;
  }

.checkbox-item-container .checkbox-label {
    color: var(--element-active-color);
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-body-font-weight);
    font-size: var(--global-typography-ui-body-font-size);
    line-height: var(--global-typography-ui-body-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

:is(.status-checked,.status-mixed) :is(.checkbox-item-container .checkbox-label) {
      color: var(--element-active-color);
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-body-active-font-weight);
      font-size: var(--global-typography-ui-body-active-font-size);
      line-height: var(--global-typography-ui-body-active-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    }

.disabled :is(.checkbox-item-container .checkbox-label) {
      color: var(--element-disabled-color);
    }

.checkbox-item-container .checkbox-description {
    color: var(--element-active-color);
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-label-font-weight);
    font-size: var(--global-typography-ui-label-font-size);
    line-height: var(--global-typography-ui-label-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

.disabled :is(.checkbox-item-container .checkbox-description) {
      color: var(--element-disabled-color);
    }

.checkbox-item-container.hover-style-touch-target {
  cursor: pointer;
}

.checkbox-item-container.hover-style-touch-target:focus {
  outline: none;
}

.checkbox-item-container.hover-style-touch-target .content-container {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.checkbox-item-container.hover-style-touch-target.activated .content-container {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

.checkbox-item-container.hover-style-touch-target:hover .content-container {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.checkbox-item-container.hover-style-touch-target:active .content-container {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

.checkbox-item-container.hover-style-touch-target:focus-visible .content-container {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.checkbox-item-container.hover-style-touch-target:disabled .content-container {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.checkbox-item-container.hover-style-touch-target.disabled .content-container {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.checkbox-item-container.hover-style-touch-target:disabled {
  cursor: not-allowed;
}

.checkbox-item-container.hover-style-touch-target.disabled {
  cursor: not-allowed;
}

.checkbox-item-container.hover-style-visual-target .content-container {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.content-container {
  display: flex;
  width: 100%;
  height: 100%;
  margin-left: 0px;
  gap: 0;
  padding: 0;
  align-items: center;
  box-shadow: none;
  border-radius: var(--ui-components-checkbox-list-item-border-radius);
}

.checkbox-item-container.hover-style-visual-target:not(.is-nested) .content-container {
    margin-left: calc(var(--ui-components-checkbox-padding-horizontal) * -1);
  }

.checkbox-item-container.hover-style-visual-target:hover .content-container,.checkbox-item-container.hover-style-visual-target:active .content-container,.checkbox-item-container.hover-style-visual-target:focus-within .content-container {
    background: transparent;
    box-shadow: none;
  }

.checkbox-item-container.hover-style-touch-target:not(.disabled):has(obc-checkbox[data-focus-visible]) .content-container {
    box-shadow: inset 0 0 0 var(--global-size-spacing-border-weight-focusframe)
      var(--border-focus-color);
  }
`,Xu=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path d="M8.99991 16.17L4.82991 12L3.40991 13.41L8.99991 19L20.9999 7L19.5899 5.59L8.99991 16.17Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M8.99991 16.17L4.82991 12L3.40991 13.41L8.99991 19L20.9999 7L19.5899 5.59L8.99991 16.17Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},Zu=(Xu.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Xu);N([P({type:Boolean})],Zu.prototype,`useCssColor`,void 0),Zu=N([M(`obi-check-google`)],Zu);var Qu=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M18.9998 13.0002H4.99976V11.0002H18.9998V13.0002Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M18.9998 13.0002H4.99976V11.0002H18.9998V13.0002Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},$u=(Qu.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,Qu);N([P({type:Boolean})],$u.prototype,`useCssColor`,void 0),$u=N([M(`obi-check-mixed`)],$u);var ed=o`* {
  -webkit-tap-highlight-color: transparent;
}

.visually-hidden {
  box-sizing: border-box;
  display: flex;
  height: var(--ui-components-checkbox-touch-target-size);
  min-width: var(--ui-components-checkbox-touch-target-size);
  min-height: var(--ui-components-checkbox-touch-target-size);
  padding: 0px var(--ui-components-checkbox-margin);
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  user-select: none;
  cursor: pointer;
  outline: none;
}

.visually-hidden.state-loading {
    cursor: progress;
  }

.visually-hidden.disabled {
    cursor: not-allowed;
  }

.checkbox-container {
  display: flex;
  padding: 0px;
  align-items: center;
  justify-content: center;
}

.checkbox-loading-spinner {
  width: var(--global-size-spacing-icon-icon-size-small);
  height: var(--global-size-spacing-icon-icon-size-small);
  align-self: center;
  margin: auto;
  animation: checkbox-loading-spin 1000ms linear infinite;
}

.checkbox-loading-spinner circle {
    fill: none;
    stroke: currentColor;
    stroke-width: var(
      --ui-components-progressbars-progress-bar--circular-bar-weight-small
    );
    stroke-linecap: round;
    stroke-dasharray: 24 14;
  }

.state-loading.status-unchecked .checkbox-loading-spinner {
    color: var(--element-neutral-color);
  }

.state-loading.status-checked .checkbox-loading-spinner {
    color: var(--element-active-inverted-color);
  }

.state-loading.status-mixed .checkbox-loading-spinner {
    color: var(--instrument-enhanced-secondary-color);
  }

.checkbox-container.status-unchecked:not(.disabled):hover .checkbox-box {
  background: var(--indent-hover-background-color);
  border-color: var(--indent-hover-border-color);
}

.checkbox-container.status-unchecked:not(.disabled):active .checkbox-box {
  background: var(--indent-pressed-background-color);
  border-color: var(--indent-pressed-border-color);
}

.checkbox-container.status-unchecked:not(.disabled):focus-visible
  .checkbox-box {
  background: var(--indent-focused-background-color);
  border-color: var(--indent-focused-border-color);
}

.checkbox-container.status-checked:not(.disabled):hover .checkbox-box,
.checkbox-container.status-mixed:not(.disabled):hover .checkbox-box {
  background: var(--selected-hover-background-color);
  border-color: var(--selected-hover-border-color);
}

.checkbox-container.status-checked:not(.disabled):active .checkbox-box,
.checkbox-container.status-mixed:not(.disabled):active .checkbox-box {
  background: var(--selected-pressed-background-color);
  border-color: var(--selected-pressed-border-color);
}

.checkbox-container.status-checked:not(.disabled):focus-visible .checkbox-box,
.checkbox-container.status-mixed:not(.disabled):focus-visible .checkbox-box {
  background: var(--selected-focused-background-color);
  border-color: var(--selected-focused-border-color);
}

.checkbox-icon {
  width: var(--global-size-spacing-icon-icon-size-regular);
  height: var(--global-size-spacing-icon-icon-size-regular);
  flex-shrink: 0;
}

.status-checked .checkbox-icon {
    color: var(--on-selected-active-color);
  }

.status-unchecked:not(.no-hover-effects) {
  cursor: pointer;
}

.status-unchecked:not(.no-hover-effects):focus {
  outline: none;
}

.status-unchecked:not(.no-hover-effects) .checkbox-box {
  border-color: var(--indent-enabled-border-color);
  background-color: var(--indent-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--indent-enabled-border-color);
  --base-background-color: var(--indent-enabled-background-color);
}

.status-unchecked.activated:not(.no-hover-effects) .checkbox-box {
  border-color: var(--indent-activated-border-color);
  background-color: var(--indent-activated-background-color);
  --base-border-color: var(--indent-activated-border-color);
  --base-background-color: var(--indent-activated-background-color);
}

@media (hover:hover) {

.status-unchecked:not(.no-hover-effects):hover .checkbox-box {
    border-color: color-mix(in srgb, var(--indent-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--indent-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.status-unchecked:not(.no-hover-effects):active .checkbox-box {
  border-color: var(--indent-pressed-border-color);
  background-color: var(--indent-pressed-background-color);
}

.status-unchecked:not(.no-hover-effects):focus-visible .checkbox-box {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.status-unchecked:not(.no-hover-effects):disabled .checkbox-box {
  border-color: var(--indent-disabled-border-color);
  background-color: var(--indent-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-indent-disabled-color) !important;
}

.status-unchecked.disabled:not(.no-hover-effects) .checkbox-box {
  border-color: var(--indent-disabled-border-color);
  background-color: var(--indent-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-indent-disabled-color) !important;
}

.status-unchecked:not(.no-hover-effects):disabled {
  cursor: not-allowed;
}

.status-unchecked.disabled:not(.no-hover-effects) {
  cursor: not-allowed;
}

.status-unchecked:not(.no-hover-effects):not(.disabled) .checkbox-box,.status-unchecked:not(.no-hover-effects):not(.disabled):hover .checkbox-box {
    border-color: var(--element-symbol-color);
  }

.status-unchecked.no-hover-effects .checkbox-box {
  border-color: var(--indent-enabled-border-color);
  background-color: var(--indent-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  --base-border-color: var(--indent-enabled-border-color);
  --base-background-color: var(--indent-enabled-background-color);
}

.status-checked.no-hover-effects .checkbox-box {
  border-color: var(--selected-enabled-border-color);
  background-color: var(--selected-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  --base-border-color: var(--selected-enabled-border-color);
  --base-background-color: var(--selected-enabled-background-color);
}

.status-mixed.no-hover-effects .checkbox-box {
  border-color: var(--amplified-enabled-border-color);
  background-color: var(--amplified-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  --base-border-color: var(--amplified-enabled-border-color);
  --base-background-color: var(--amplified-enabled-background-color);
}

.status-checked:not(.no-hover-effects) {
  cursor: pointer;
}

.status-checked:not(.no-hover-effects):focus {
  outline: none;
}

.status-checked:not(.no-hover-effects) .checkbox-box {
  border-color: var(--selected-enabled-border-color);
  background-color: var(--selected-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--selected-enabled-border-color);
  --base-background-color: var(--selected-enabled-background-color);
}

.status-checked.activated:not(.no-hover-effects) .checkbox-box {
  border-color: var(--selected-activated-border-color);
  background-color: var(--selected-activated-background-color);
  --base-border-color: var(--selected-activated-border-color);
  --base-background-color: var(--selected-activated-background-color);
}

@media (hover:hover) {

.status-checked:not(.no-hover-effects):hover .checkbox-box {
    border-color: color-mix(in srgb, var(--selected-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--selected-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.status-checked:not(.no-hover-effects):active .checkbox-box {
  border-color: var(--selected-pressed-border-color);
  background-color: var(--selected-pressed-background-color);
}

.status-checked:not(.no-hover-effects):focus-visible .checkbox-box {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.status-checked:not(.no-hover-effects):disabled .checkbox-box {
  border-color: var(--selected-disabled-border-color);
  background-color: var(--selected-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-selected-disabled-color) !important;
}

.status-checked.disabled:not(.no-hover-effects) .checkbox-box {
  border-color: var(--selected-disabled-border-color);
  background-color: var(--selected-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-selected-disabled-color) !important;
}

.status-checked:not(.no-hover-effects):disabled {
  cursor: not-allowed;
}

.status-checked.disabled:not(.no-hover-effects) {
  cursor: not-allowed;
}

.status-mixed:not(.no-hover-effects) {
  cursor: pointer;
}

.status-mixed:not(.no-hover-effects):focus {
  outline: none;
}

.status-mixed:not(.no-hover-effects) .checkbox-box {
  border-color: var(--amplified-enabled-border-color);
  background-color: var(--amplified-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--amplified-enabled-border-color);
  --base-background-color: var(--amplified-enabled-background-color);
}

.status-mixed.activated:not(.no-hover-effects) .checkbox-box {
  border-color: var(--amplified-activated-border-color);
  background-color: var(--amplified-activated-background-color);
  --base-border-color: var(--amplified-activated-border-color);
  --base-background-color: var(--amplified-activated-background-color);
}

@media (hover:hover) {

.status-mixed:not(.no-hover-effects):hover .checkbox-box {
    border-color: color-mix(in srgb, var(--amplified-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--amplified-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.status-mixed:not(.no-hover-effects):active .checkbox-box {
  border-color: var(--amplified-pressed-border-color);
  background-color: var(--amplified-pressed-background-color);
}

.status-mixed:not(.no-hover-effects):focus-visible .checkbox-box {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.status-mixed:not(.no-hover-effects):disabled .checkbox-box {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

.status-mixed.disabled:not(.no-hover-effects) .checkbox-box {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

.status-mixed:not(.no-hover-effects):disabled {
  cursor: not-allowed;
}

.status-mixed.disabled:not(.no-hover-effects) {
  cursor: not-allowed;
}

.checkbox-box {
  box-sizing: border-box;
  position: relative;
  display: flex;
  width: var(--ui-components-checkbox-visual-target-size);
  height: var(--ui-components-checkbox-visual-target-size);
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: var(--ui-components-checkbox-border-radius);
  border: 1px solid transparent;
  background: transparent;
}

.status-mixed:not(.disabled) .checkbox-box,.status-mixed:not(.disabled):hover .checkbox-box,.status-mixed:not(.disabled):active .checkbox-box {
    border-color: var(--instrument-enhanced-secondary-color);
  }

:is(.status-unchecked.no-hover-effects .checkbox-box) {
  border-color: var(--indent-enabled-border-color);
  background-color: var(--indent-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  --base-border-color: var(--indent-enabled-border-color);
  --base-background-color: var(--indent-enabled-background-color);
}

.status-unchecked.no-hover-effects .checkbox-box {
    border-color: var(--element-symbol-color);
  }

.status-unchecked.state-enabled:not(.disabled):not(
    .no-hover-effects
  ):focus-visible
  .checkbox-box {
  border-color: transparent;
}

@keyframes checkbox-loading-spin {
  to {
    transform: rotate(360deg);
  }
}
`,td,nd=function(e){return e.unchecked=`unchecked`,e.checked=`checked`,e.mixed=`mixed`,e}({}),rd=function(e){return e.enabled=`enabled`,e.loading=`loading`,e}({}),id=(td=class extends j{constructor(...e){super(...e),this.status=`unchecked`,this.state=`enabled`,this.disabled=!1,this.hasHoverEffects=!0,this.focusable=!0}get _isInteractionLocked(){return this.disabled||this.state===`loading`}updated(e){e.has(`disabled`)&&this.dispatchEvent(new CustomEvent(`disabled`,{detail:{status:this.status,disabled:this.disabled}}))}toggleStatus(){this._isInteractionLocked||(this.status=this.status===`checked`?`unchecked`:`checked`,this.dispatchEvent(new CustomEvent(`change`,{detail:{status:this.status,disabled:this.disabled}})))}handleKeydown(e){(e.key===` `||e.key===`Space`||e.key===`Enter`)&&(e.preventDefault(),this.toggleStatus())}get _computedAriaChecked(){switch(this.status){case`checked`:return`true`;case`mixed`:return`mixed`;default:return`false`}}focus(e){this.checkboxControl?.focus(e)}syncFocusVisibleAttribute(){let e=this.checkboxControl?.matches(`:focus-visible`);this.toggleAttribute(`data-focus-visible`,!!e)}handleControlFocus(){queueMicrotask(()=>this.syncFocusVisibleAttribute())}handleControlBlur(){this.removeAttribute(`data-focus-visible`)}render(){let e=this.getAttribute(`aria-label`)??void 0,t=this.getAttribute(`aria-labelledby`)??void 0,n=this.getAttribute(`aria-describedby`)??void 0,r=t?void 0:e??`Checkbox item`;return O`
      <div
        class=${F({"visually-hidden":!0,[`status-${this.status}`]:!0,[`state-${this.state}`]:!0,disabled:this.disabled,"no-hover-effects":!this.hasHoverEffects})}
        role="checkbox"
        aria-checked=${this._computedAriaChecked}
        aria-label=${I(r)}
        aria-labelledby=${I(t)}
        aria-describedby=${I(n)}
        aria-disabled=${this._isInteractionLocked?`true`:`false`}
        aria-busy=${this.state===`loading`?`true`:`false`}
        tabindex=${this._isInteractionLocked||!this.focusable?`-1`:`0`}
        @click=${this.toggleStatus}
        @keydown=${this.handleKeydown}
        @focus=${this.handleControlFocus}
        @blur=${this.handleControlBlur}
      >
        <div class="checkbox-container">
          <div class="checkbox-box">
            ${this.state===`loading`?O`
                    <svg
                      class="checkbox-loading-spinner type-indeterminate size-small style-regular"
                      viewBox="0 0 16 16"
                      aria-hidden="true"
                    >
                      <circle cx="8" cy="8" r="6"></circle>
                    </svg>
                  `:this.status===`checked`?O`<obi-check-google
                      class="checkbox-icon"
                    ></obi-check-google>`:this.status===`mixed`?O`<obi-check-mixed
                        class="checkbox-icon"
                      ></obi-check-mixed>`:O`<span class="checkbox-icon"></span>`}
          </div>
        </div>
      </div>
    `}},td.styles=[a(ed)],td);N([P({type:String})],id.prototype,`status`,void 0),N([P({type:String})],id.prototype,`state`,void 0),N([P({type:Boolean})],id.prototype,`disabled`,void 0),N([P({type:Boolean,attribute:!1})],id.prototype,`hasHoverEffects`,void 0),N([P({type:Boolean,attribute:!1})],id.prototype,`focusable`,void 0),N([Ve(`.visually-hidden`)],id.prototype,`checkboxControl`,void 0),id=N([M(`obc-checkbox`)],id);var ad=class extends j{constructor(...e){super(...e),this.status=nd.unchecked,this.state=`enabled`,this.disabled=!1,this.focusable=!0,this.label=``,this.description=``,this.level=0,this.expandable=!1,this.expanded=!1,this.hoverStyle=`touch-target`,this.ariaDescribedBy=``}get isDisabled(){return this.disabled||this.state===`disabled`}toggleStatusFromItem(){this.status=this.status===nd.checked?nd.unchecked:nd.checked,this.dispatchEvent(new CustomEvent(`change`,{detail:{status:this.status,disabled:this.isDisabled}}))}handleItemClick(e){if(this.isDisabled)return;let t=e.composedPath();this.checkboxElement&&t.includes(this.checkboxElement)||this.chevronButton&&t.includes(this.chevronButton)||this.toggleStatusFromItem()}handleChevronClick(e){e.stopPropagation(),this.dispatchEvent(new CustomEvent(`expand-toggle`,{detail:!this.expanded,bubbles:!0,composed:!0}))}handleCheckboxChange(e){let t=e;this.status=t.detail.status,this.dispatchEvent(new CustomEvent(`change`,{detail:t.detail}))}focus(e){this.checkboxElement?.focus(e)}renderChevron(){return this.expandable?O`<button
      type="button"
      class="chevron-button"
      aria-expanded=${this.expanded?`true`:`false`}
      aria-label=${I(this.label.trim()||void 0)}
      ?disabled=${this.isDisabled}
      @click=${this.handleChevronClick}
    >
      <span class="chevron-visible">
        ${this.expanded?O`<obi-chevron-down-google
                class="chevron-icon"
              ></obi-chevron-down-google>`:O`<obi-chevron-right-google
                class="chevron-icon"
              ></obi-chevron-right-google>`}
      </span>
    </button>`:A}render(){let e=this.isDisabled,t=!(this.hoverStyle===`touch-target`&&!e),n=Math.max(0,Math.floor(this.level)-1),r=this.level>=1||this.expandable,i=this.label.trim().length>0?this.label:void 0;return O`
      <div
        class=${F({"checkbox-item-container":!0,[`status-${this.status}`]:!0,[`hover-style-${this.hoverStyle}`]:!0,"is-nested":r,"has-description":this.description!==``,disabled:e})}
        @click=${this.handleItemClick}
      >
        ${n>0?O`<div
                class="nested-spacer"
                aria-hidden="true"
                style=${yr({"--checkbox-item-depth":String(n)})}
              ></div>`:A}
        ${r?O`<div class="chevron-container">${this.renderChevron()}</div>`:A}
        <div class="content-container">
          <obc-checkbox
            .focusable=${this.focusable}
            .status=${this.status}
            .state=${rd.enabled}
            .disabled=${e}
            .hasHoverEffects=${t}
            aria-label=${I(i)}
            aria-describedby=${I(this.ariaDescribedBy||void 0)}
            @change=${this.handleCheckboxChange}
          ></obc-checkbox>
          <div class="checkbox-label-container">
            <span class="checkbox-label">${this.label}</span>
            ${this.description?O`<span class="checkbox-description"
                    >${this.description}</span
                  >`:A}
          </div>
        </div>
      </div>
    `}},od=(ad.styles=a(Yu),ad);N([P({type:String})],od.prototype,`status`,void 0),N([P({type:String})],od.prototype,`state`,void 0),N([P({type:Boolean})],od.prototype,`disabled`,void 0),N([P({type:Boolean,attribute:!1})],od.prototype,`focusable`,void 0),N([P({type:String})],od.prototype,`label`,void 0),N([P({type:String})],od.prototype,`description`,void 0),N([P({type:Number,reflect:!0})],od.prototype,`level`,void 0),N([P({type:Boolean,reflect:!0})],od.prototype,`expandable`,void 0),N([P({type:Boolean,reflect:!0})],od.prototype,`expanded`,void 0),N([P({type:String})],od.prototype,`hoverStyle`,void 0),N([P({type:String,attribute:`aria-describedby`,reflect:!0})],od.prototype,`ariaDescribedBy`,void 0),N([Ve(`obc-checkbox`)],od.prototype,`checkboxElement`,void 0),N([Ve(`.chevron-button`)],od.prototype,`chevronButton`,void 0),od=N([M(`obc-checkbox-item`)],od);var sd=o`* {
  -webkit-tap-highlight-color: transparent;
}

#group-item {
  anchor-name: --group-item;
}

* {
  box-sizing: border-box;
}

#flyout-wrapper {
  display: none;
  position: fixed;
  position-anchor: --group-item;
  left: calc(
    anchor(right) +
      var(--app-components-navigation-menu-footer-margin-horizontal)
  );
  min-width: 320px;
  top: var(--obc-navigation-item-flyout-top, 0px);
  bottom: 0;
  height: auto;
  margin: 0;
  border: none;
  outline: none;
}

#flyout-wrapper .content {
    display: flex;
    flex-direction: column;
    background: var(--container-global-color);
    padding: var(--app-components-navigation-menu-margin-vertical)
      var(--app-components-navigation-menu-margin-horizontal);
    height: 100%;
  }

#flyout-wrapper.open {
    display: block;
  }

#flyout-wrapper:not(.hug) {
    border-left: 1px solid var(--border-outline-color);
  }

#flyout-wrapper.hug {
    position: absolute;
    top: calc(anchor(top) - var(--ui-components-context-menu-margin-vertical));
    bottom: auto;
    height: auto;
    left: calc(
      anchor(right) +
        var(--app-components-navigation-menu-footer-margin-horizontal) + 1px
    );
  }

#flyout-wrapper.hug .content {
      padding: var(--ui-components-context-menu-margin-vertical)
        var(--ui-components-context-menu-margin-horizontal);
      border-radius: var(--ui-components-context-menu-border-radius);
    }

#flyout-wrapper.hug.compact {
      left: calc(anchor(right) + 1px);
    }

#flyout-wrapper.hug.compact {
    top: calc(
      anchor(top) - var(--ui-components-context-menu-margin-vertical) +
        var(
          --menu-navigation-components-navigation-item-margin-vertical-icon-button
        )
    );
  }

#flyout-wrapper:not(.hug)::after {
    content: "";
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    width: 1px;
    box-shadow: var(--shadow-flat);
    z-index: -1;
  }

#flyout-wrapper {

  anchor-name: --flyout-wrapper;
}

.shadow.open.hug {
  position-anchor: --flyout-wrapper;
  content: "";
  position: absolute;
  top: anchor(top);
  left: anchor(left);
  right: anchor(right);
  bottom: anchor(bottom);
  box-shadow: var(--shadow-floating);
  border-radius: var(--ui-components-context-menu-border-radius);
  z-index: -1;
}

.content {
  display: flex;
  flex-direction: column;
}

[part="children"] {
  display: block;
}

[part="children"][hidden] {
  display: none;
}
`,cd=class extends j{constructor(...e){super(...e),this.label=`Label`,this.checked=!1,this.variant=On.Full,this.hug=!1,this.hasIcon=!1,this.treeMode=!1,this.treeBranches=[],this.terminalType=xn.regular,this.defaultOpen=!1,this.focusable=!0,this.openContainer=!1}firstUpdated(){this.defaultOpen&&(this.openContainer=!0)}get expanded(){return this.openContainer}onClickGroup(){this.openContainer?this.close():this.open()}open(){this.openContainer=!0,this.dispatchEvent(new CustomEvent(`open`))}close(){this.openContainer=!1,this.querySelectorAll(`obc-navigation-item-group`).forEach(e=>{e.close()})}focus(e){this.groupItem?.focus(e)}render(){return this.treeMode?O`
        <obc-tree-navigation-item
          part="header"
          .label=${this.label}
          .branches=${this.treeBranches}
          expandable
          ?expanded=${this.openContainer}
          ?checked=${this.checked}
          .hasLeadingIcon=${this.hasIcon}
          .terminalType=${this.terminalType}
          .alerts=${this.expanded?void 0:this.alerts}
          @expand-toggle=${this.onClickGroup}
        >
          ${this.hasIcon?O`<slot name="icon" slot="icon"></slot>`:A}
        </obc-tree-navigation-item>
        <div part="children" role="group" ?hidden=${!this.openContainer}>
          <slot></slot>
        </div>
      `:O`
      <obc-navigation-item
        @click=${this.onClickGroup}
        .focusable=${this.focusable}
        .checked=${this.checked}
        .groupSelected=${this.openContainer}
        .href=${this.href}
        .label=${this.label}
        .variant=${this.variant}
        group
        id="group-item"
        ?hasIcon=${this.hasIcon}
      >
        ${this.hasIcon?O`<slot name="icon" slot="icon"></slot>`:A}
      </obc-navigation-item>
      <div
        part="flyout"
        id="flyout-wrapper"
        class=${F({hug:this.hug,[this.variant]:!0,open:this.openContainer})}
      >
        <div class="content">
          <slot></slot>
        </div>
      </div>
      <div
        class=${F({shadow:!0,open:this.openContainer,hug:this.hug})}
      ></div>
    `}},ld=(cd.styles=a(sd),cd);N([P({type:String})],ld.prototype,`label`,void 0),N([P({type:String})],ld.prototype,`href`,void 0),N([P({type:Boolean})],ld.prototype,`checked`,void 0),N([P({type:String})],ld.prototype,`variant`,void 0),N([P({type:Boolean})],ld.prototype,`hug`,void 0),N([P({type:Boolean})],ld.prototype,`hasIcon`,void 0),N([P({type:Boolean})],ld.prototype,`treeMode`,void 0),N([P({type:Array})],ld.prototype,`treeBranches`,void 0),N([P({type:String})],ld.prototype,`terminalType`,void 0),N([P({type:Object})],ld.prototype,`alerts`,void 0),N([P({type:Boolean})],ld.prototype,`defaultOpen`,void 0),N([P({type:Boolean,attribute:!1})],ld.prototype,`focusable`,void 0),N([ze()],ld.prototype,`openContainer`,void 0),N([Ve(`obc-navigation-item, obc-tree-navigation-item`)],ld.prototype,`groupItem`,void 0),ld=N([M(`obc-navigation-item-group`)],ld);var ud,dd=function(e){return e.Regular=`regular`,e.Checkboxes=`checkboxes`,e.NestedCheckboxes=`nested-checkboxes`,e.Flyout=`flyout`,e.Multi=`multi`,e.MultiWithSubtitles=`multi-with-subtitles`,e}({}),fd=(ud=class extends j{constructor(...e){super(...e),this.softDismiss=!1,this.open=!1,this.softDismissController=new Ht(this),this.type=`regular`,this.options=[],this.selectedValues=[],this.hasTitleBar=!1,this.title=``,this.columnGroups=[],this.itemsPerColumn=5,this.navigator=new Wt({items:()=>this.getMenuItems(),preferred:()=>this.selectedMenuItem(),setFocusable:(e,t)=>{e.focusable=t}},{orientation:`vertical`,wrap:!1})}updated(){this.navigator.refresh()}getMenuItems(){return Array.from(this.renderRoot.querySelectorAll(`[data-menu-item="true"]`)).filter(e=>e.getClientRects().length>0)}selectedMenuItem(){let e=this.getMenuItems();return this.selectedValues.map(t=>e.find(e=>e.getAttribute(`data-menu-value`)===t)).find(e=>e!==void 0)}focusMenuItem(e){let t=this.getMenuItems();if(t.length===0)return;let n=t[st(e,0,t.length-1)];this.navigator.setActive(n,!0),n.scrollIntoView({block:`nearest`})}focusFirstItem(){this.focusMenuItem(0)}focusLastItem(){let e=this.getMenuItems();e.length!==0&&this.focusMenuItem(e.length-1)}focusSelectedItem(){if(this.getMenuItems().length===0)return;let e=this.selectedMenuItem();if(e!==void 0){this.navigator.setActive(e,!0),e.scrollIntoView({block:`nearest`});return}this.focusFirstItem()}handleKeydown(e){if(this.navigator.handleKeydown(e)){e.preventDefault(),this.navigator.activeItem?.scrollIntoView({block:`nearest`});return}if(this.getMenuItems().length!==0)switch(e.key){case`ArrowDown`:e.preventDefault(),this.focusFirstItem();break;case`ArrowUp`:e.preventDefault(),this.focusLastItem();break;case`Home`:e.preventDefault(),this.focusFirstItem();break;case`End`:e.preventDefault(),this.focusLastItem();break;case`Escape`:if(this.softDismiss)break;e.preventDefault(),this.dispatchEvent(new CustomEvent(`close`))}}get isMultiSelect(){return this.multiSelect===void 0?[`checkboxes`,`nested-checkboxes`,`multi`,`multi-with-subtitles`].includes(this.type):this.multiSelect}get isPerGroupSingleSelect(){return this.isMultiSelect?!1:this.selectPerGroup===void 0?this.type===`flyout`:this.selectPerGroup}getGroupForValue(e){if(this.type===`multi-with-subtitles`&&this.columnGroups.length){for(let t of this.columnGroups){let n=Math.max(t.columns,Math.ceil(t.options.length/this.itemsPerColumn)),r=this.chunkArray(t.options,this.itemsPerColumn,n);for(let n=0;n<r.length;++n)if(r[n].some(t=>t.value===e))return`${t.title}___${n}`}return}if(this.type===`multi`&&this.itemsPerColumn>0){let t=this.chunkArray(this.options,this.itemsPerColumn);for(let n=0;n<t.length;++n)if(t[n].some(t=>t.value===e))return`column-${n}`;return}if(this.type===`flyout`&&this.options.length){for(let t of this.options)if(t.children?.some(t=>t.value===e)||t.value===e)return t.value;return}}handleCheckboxChange(e,t){let{status:n}=t.detail,r;if(this.selectPerGroup&&(this.type===`multi`||this.type===`multi-with-subtitles`)){let t=this.getGroupForValue(e.value);r=[...this.selectedValues.filter(e=>this.getGroupForValue(e)!==t),...n===`checked`?[e.value]:[]]}else r=n===`checked`?[...this.selectedValues,e.value]:this.selectedValues.filter(t=>t!==e.value);pd(this.selectedValues,r)||this.updateSelection(r)}handleMenuItemClick(e,t){if(t.preventDefault(),this.dispatchEvent(new CustomEvent(`item-click`,{detail:{value:e.value,option:e}})),e.children?.length)return;let n;if(this.isPerGroupSingleSelect){let t=this.getGroupForValue?this.getGroupForValue(e.value):void 0;n=this.selectedValues.find(e=>this.getGroupForValue(e)===t)===e.value?this.selectedValues.filter(t=>t!==e.value):[...this.selectedValues.filter(e=>this.getGroupForValue(e)!==t),e.value]}else n=this.selectedValues.includes(e.value)?[]:[e.value];pd(this.selectedValues,n)||this.updateSelection(n)}updateSelection(e){this.selectedValues=e;let t=[],n=r=>r.forEach(r=>{e.includes(r.value)&&t.push(r),r.children&&n(r.children)});n(this.options),this.dispatchEvent(new CustomEvent(`change`,{detail:{selectedValues:e,selectedOptions:t}}))}handleCloseClick(e){e.preventDefault(),this.dispatchEvent(new CustomEvent(`close`))}isOptionSelected(e){return this.selectedValues.includes(e)}renderTitleBar(){return this.hasTitleBar?O`
      <div class="title-container">
        <div class="title-content">
          <div class="title-text">${this.title}</div>
        </div>
        <obc-icon-button
          variant="flat"
          @click=${this.handleCloseClick}
          aria-label="Close menu"
          .focusable=${!1}
        >
          <obi-close-google></obi-close-google>
        </obc-icon-button>
      </div>
    `:A}renderRegularItems(){return this.options.map(e=>this.renderNavItem(e))}renderCheckboxItems(){return this.options.map(e=>{let t=this.isOptionSelected(e.value),n=this.type===`nested-checkboxes`&&e.level&&e.level>1?(e.level-1)*16:0;return O`<div
        class="menu-item checkbox-item-wrapper"
        style=${n?`padding-left:${n}px`:``}
      >
        <obc-checkbox-item
          data-menu-item="true"
          data-menu-value=${e.value}
          .label=${e.label}
          .status=${t?`checked`:`unchecked`}
          @expand-toggle=${or}
          @change=${t=>this.handleCheckboxChange(e,t)}
        ></obc-checkbox-item>
      </div>`})}renderNavItem(e){let t=this.isOptionSelected(e.value),n=e.level?(e.level-1)*16:0;return O`<div
      class="menu-item navigation-item-wrapper"
      style=${n?`padding-left:${n}px`:``}
    >
      <obc-navigation-item
        data-menu-item="true"
        data-menu-value=${e.value}
        .label=${e.label}
        .checked=${t}
        .variant=${On.Full}
        @click=${t=>this.handleMenuItemClick(e,t)}
        .itemRole=${Pn.MenuItemRadio}
        ?hasIcon=${!!e.icon}
      >
        ${e.icon?O`<div slot="icon">${e.icon}</div>`:A}
      </obc-navigation-item>
    </div>`}renderFlyoutChildren(e){return this.isMultiSelect?e.map(e=>{let t=this.isOptionSelected(e.value);return O`<div class="menu-item checkbox-item-wrapper">
          <obc-checkbox-item
            data-menu-item="true"
            data-menu-value=${e.value}
            .label=${e.label}
            .status=${t?`checked`:`unchecked`}
            @expand-toggle=${or}
            @change=${t=>this.handleCheckboxChange(e,t)}
          ></obc-checkbox-item>
        </div>`}):e.map(e=>{let t=this.isOptionSelected(e.value);return O`<obc-navigation-item
        data-menu-item="true"
        data-menu-value=${e.value}
        .label=${e.label}
        .checked=${t}
        .variant=${On.Full}
        @click=${t=>this.handleMenuItemClick(e,t)}
        .itemRole=${Pn.MenuItemRadio}
        ?hasIcon=${!!e.icon}
      >
        ${e.icon?O`<div slot="icon">${e.icon}</div>`:A}
      </obc-navigation-item>`})}async refreshAfterDisclosure(e){await e.updateComplete,await this.updateComplete,this.navigator.refresh()}handleFlyoutGroupClick(e,t){t.preventDefault(),this.refreshAfterDisclosure(t.currentTarget),this.dispatchEvent(new CustomEvent(`item-click`,{detail:{value:e.value,option:e}}))}renderFlyoutItems(){return this.options.map(e=>{let t=this.isOptionSelected(e.value);return e.children?.length?O`<obc-navigation-item-group
          data-menu-item="true"
          data-menu-value=${e.value}
          .label=${e.label}
          .checked=${t}
          .variant=${On.Full}
          .hug=${!0}
          .hasIcon=${!!e.icon}
          @click=${t=>this.handleFlyoutGroupClick(e,t)}
          @open=${t=>{this.shadowRoot?.querySelectorAll(`obc-navigation-item-group`).forEach(t=>{let n=t;n.label!==e.label&&n.close()}),this.refreshAfterDisclosure(t.currentTarget)}}
        >
          ${e.icon?O`<div slot="icon">${e.icon}</div>`:A}
          ${this.renderFlyoutChildren(e.children)}
        </obc-navigation-item-group>`:this.renderNavItem(e)})}renderMultiColumnItems(){let e=e=>e.length?this.isMultiSelect&&!this.selectPerGroup?e.map(e=>{let t=this.isOptionSelected(e.value);return O`<div class="menu-item checkbox-item-wrapper">
            <obc-checkbox-item
              data-menu-item="true"
              data-menu-value=${e.value}
              .label=${e.label}
              .status=${t?`checked`:`unchecked`}
              @expand-toggle=${or}
              @change=${t=>this.handleCheckboxChange(e,t)}
            ></obc-checkbox-item>
          </div>`}):e.map(e=>this.renderNavItem(e)):A;if(this.type===`multi-with-subtitles`){if(!this.columnGroups.length)return O`<div class="multi-content">
          <div class="multi-columns">
            <div class="columns-container">
              ${this.chunkArray(this.options,this.itemsPerColumn).map((t,n)=>O`<div
                    class="column-with-header ${n?`column-divider`:``}"
                  >
                    <div class="column-header">
                      <div class="subtitle-container">
                        <div class="subtitle-text">Group ${n+1}</div>
                      </div>
                    </div>
                    <div class="column-content">${e(t)}</div>
                  </div>`)}
            </div>
          </div>
        </div>`;let t=[];return this.columnGroups.forEach((e,n)=>{let r=Math.ceil(e.options.length/this.itemsPerColumn),i=Math.max(e.columns,r);this.chunkArray(e.options,this.itemsPerColumn,i).forEach((r,i)=>{t.push({options:r,groupTitle:e.title,isFirstInGroup:i===0,isFirstGroup:n===0,colIdx:i})})}),O`<div class="multi-content">
        <div class="multi-columns">
          <div class="columns-container">
            ${t.map(t=>O`<div
                  class="column-with-header ${!t.isFirstGroup&&t.isFirstInGroup?`column-divider`:``}"
                >
                  ${t.isFirstInGroup?O`<div class="column-header">
                          <div class="subtitle-container">
                            <div class="subtitle-text">${t.groupTitle}</div>
                          </div>
                        </div>`:O`<div class="column-header-spacer"></div>`}
                  <div class="column-content">${e(t.options)}</div>
                </div>`)}
          </div>
        </div>
      </div>`}return O`<div class="multi-content">
      <div class="multi-columns">
        ${this.chunkArray(this.options,this.itemsPerColumn).map((t,n)=>O`<div class="column ${n?`column-divider`:``}">
              ${e(t)}
            </div>`)}
      </div>
    </div>`}chunkArray(e,t,n){if(n){let r=Array.from({length:n},()=>[]);return e.forEach((e,n)=>r[Math.floor(n/t)].push(e)),r}let r=[];for(let n=0;n<e.length;n+=t)r.push(e.slice(n+0,n+t));return r}renderMenuContent(){switch(this.type){case`checkboxes`:case`nested-checkboxes`:return this.renderCheckboxItems();case`flyout`:return this.renderFlyoutItems();case`multi`:case`multi-with-subtitles`:return this.renderMultiColumnItems();default:return this.renderRegularItems()}}render(){return O`<div
      class=${F({"context-menu":!0,[`type-${this.type}`]:!0,"has-title":this.hasTitleBar})}
      tabindex="-1"
      role="menu"
      aria-label=${this.hasTitleBar?this.title:`Context menu`}
      @keydown=${this.handleKeydown}
      @focusin=${e=>this.navigator.handleFocusin(e)}
    >
      ${this.renderTitleBar()}
      <div class="menu-content">${this.renderMenuContent()}</div>
    </div>`}},ud.styles=a(Ku),ud);N([P({type:Boolean})],fd.prototype,`softDismiss`,void 0),N([P({type:Boolean})],fd.prototype,`open`,void 0),N([P({type:String})],fd.prototype,`type`,void 0),N([P({type:Array})],fd.prototype,`options`,void 0),N([P({type:Array})],fd.prototype,`selectedValues`,void 0),N([P({type:Boolean})],fd.prototype,`hasTitleBar`,void 0),N([P({type:String})],fd.prototype,`title`,void 0),N([P({type:Array})],fd.prototype,`columnGroups`,void 0),N([P({type:Number})],fd.prototype,`itemsPerColumn`,void 0),N([P({type:Boolean})],fd.prototype,`multiSelect`,void 0),N([P({type:Boolean,reflect:!0})],fd.prototype,`selectPerGroup`,void 0),fd=N([M(`obc-context-menu-input`)],fd);function pd(e,t){if(e.length!==t.length)return!1;let n=new Set(e);return t.every(e=>n.has(e))}var md,hd=Du,gd=W,_d=Ou,vd=Wu,yd=function(e){return e.vertical=`vertical`,e.horizontal=`horizontal`,e}({}),bd=function(e){return e.inline=`inline`,e.stacked=`stacked`,e}({}),xd=function(e){return e.vertical=`vertical`,e.left=`left`,e.center=`center`,e}({}),X=(md=class extends j{constructor(...e){super(...e),this.hasValue=!0,this.value=null,this.valueType=Ul.number,this.off=!1,this.offText=`OFF`,this.hasSetpoint=!1,this.hasAdvice=!1,this.hasDegree=!1,this.hasDegreeSpacer=!1,this.hasLeadingIcon=!1,this.fractionDigits=0,this.maxDigits=0,this.alert=!1,this.showDebugOverlay=!1,this.deferredSetpointHidePhase=q.none,this.hasCompletedFirstUpdate=!1,this.hasWarnedHorizontalSize=!1,this.sourcePickerContentVisible=!1,this.sourcePickerOptions=[],this.onWindowPointerDown=e=>{this.sourcePickerContentVisible&&(e.composedPath().includes(this)||(this.sourcePickerContentVisible=!1))},this.syncSourcePickerOptions=()=>{this.sourcePickerOptions=this.getSourcePickerNavigationItems().map((e,t)=>{let{itemLabel:n,itemValue:r}=this.getSourcePickerItemInfo(e,t);return{value:r,label:n,icon:this.createSourcePickerOptionIcon(e)}})}}get resolvedSize(){return this.isHorizontal?hd.large:this.size??hd.small}get resolvedPriority(){return this.priority??gd.regular}get resolvedDirection(){return this.direction??`vertical`}get resolvedStacking(){return this.stacking??`inline`}get resolvedAlignment(){return this.alignment??`vertical`}get isHorizontal(){return this.resolvedDirection===`horizontal`}get resolvedFractionDigits(){return this.fractionDigits??0}get resolvedMaxDigits(){return Jl(this.maxDigits)}get digitCountsMissing(){return Yl(this.fractionDigits)||Yl(this.maxDigits)}get hasSrc(){return this.src!==void 0&&this.src.trim()!==``}get resolvedSourceInteraction(){return this.srcOptions?.interaction??`none`}get isAtSetpoint(){return!this.hasSetpoint||this.digitCountsMissing?!1:Mu(Ql(this.value,this.valueType)??null,this.setpoint,this.numericFormatOptions(this.resolvedMaxDigits))}get resolvedSetpointInteraction(){return this.setpointOptions?.interaction??vd.alwaysVisible}get isFlipFlop(){return this.resolvedSetpointInteraction===vd.flipFlop}get isEqualSize(){return this.resolvedSetpointInteraction===vd.equalSize}get isPopUp(){return this.resolvedSetpointInteraction===vd.popUp}get setpointTouching(){return this.setpointOptions?.touching??!1}get hasDynamicSetpoint(){return this.hasSetpoint&&(this.isFlipFlop||this.isPopUp)}get isSetpointEmphasized(){return this.hasSetpoint?this.setpointTouching?!0:this.isFlipFlop&&!this.isAtSetpoint:!1}get rowEnhanced(){return this.resolvedPriority===gd.enhanced}get primarySize(){return Nu(this.resolvedSize)}get secondarySize(){return Pu(this.resolvedSize)}get valueSize(){return Iu({primary:this.primarySize,secondary:this.secondarySize,setpointEmphasized:this.isSetpointEmphasized,equalSize:this.isEqualSize})}get setpointSize(){return Fu({primary:this.primarySize,secondary:this.secondarySize,emphasized:this.isSetpointEmphasized,equalSize:this.isEqualSize})}get valueWeight(){return this.valueOptions?.weight??Vl.regular}get labelSize(){return this.labelOptions?.size??(this.resolvedSize===hd.large?Bl.s:Bl.xs)}get labelWeight(){return this.rowEnhanced?Vl.semibold:Vl.regular}get setpointWeight(){return Lu(this.isSetpointEmphasized)}numericFormatOptions(e){return ju(e,this.resolvedFractionDigits)}dataQualityClasses(e){return Ru(e)}renderForwardedIcon(e){return e===Eu.setpoint?O`<slot name="setpoint-icon" slot="icon"></slot>`:e===Eu.advice?O`<slot name="advice-icon" slot="icon"></slot>`:O`<slot name="value-icon" slot="icon"></slot>`}renderBlock(e){return O`
      <obc-readout-block
        exportparts="block, block-content, block-text, block-icon, degree"
        .variant=${e.variant}
        .value=${e.value??null}
        .valueType=${e.valueType??Ul.number}
        .size=${this.resolvedSize}
        .valueSize=${e.valueSize}
        .enhanced=${e.enhanced}
        .weight=${e.weight}
        .hasDegree=${e.hasDegree??!1}
        .hasIcon=${e.hasIcon??!1}
        .fractionDigits=${this.fractionDigits}
        .maxDigits=${this.maxDigits}
        .hintedZeros=${e.hintedZeros}
        .hasSignSpacer=${e.hasSignSpacer??!1}
        .spaceReserver=${e.spaceReserver}
        .off=${e.off??!1}
        .offText=${this.offText}
        .touching=${e.touching??!1}
        .hidePhase=${e.hidePhase??q.none}
        .dataQuality=${e.dataQuality}
        .alert=${e.alert??!1}
        .category=${e.category??ku.regular}
        .active=${e.active??!1}
      >
        ${e.ghost?A:this.renderForwardedIcon(e.variant)}
      </obc-readout-block>
    `}renderDegreeGlyph(e){return O`
      <span
        class=${F({"degree-column":!0,[`degree-${e}`]:!0,"tone-enhanced":this.rowEnhanced})}
        part="degree"
      >
        <obc-textbox class="degree-glyph" .size=${e} alignment="center"
          >°</obc-textbox
        >
      </span>
    `}renderDegreeColumn(e=this.valueSize){return(this.hasDegree??!1)&&!this.off?this.renderDegreeGlyph(e):this.hasDegreeSpacer??!1?O`<span
        class="degree-spacer"
        part="degree-spacer"
        aria-hidden="true"
      ></span>`:A}renderTextbox(e,t,n,r){let i=e===`label`?this.labelWeight:Vl.regular,a=e===`label`?this.labelSize:Bl.xs,o=O`
      <obc-textbox
        class=${F({[e]:!0,...this.dataQualityClasses(r?.dataQuality)})}
        part=${e}
        .size=${a}
        .fontWeight=${i}
        alignment="left"
      >
        ${t}
        ${n?O`<span slot="length">${n}</span>`:A}
      </obc-textbox>
    `;return Il(r?.alert??!1,o)}get setpointHidePhase(){return zu(this.isPopUp&&this.isAtSetpoint&&!this.setpointTouching,this.deferredSetpointHidePhase)}renderAdviceBlock(){return this.renderBlock({variant:Eu.advice,value:this.advice,valueSize:this.secondarySize,enhanced:!1,weight:Vl.regular,hintedZeros:this.adviceOptions?.hintedZeros??!1,hasSignSpacer:this.adviceOptions?.hasSignSpacer??!1,spaceReserver:this.adviceOptions?.spaceReserver,dataQuality:this.adviceOptions?.dataQuality,alert:this.adviceOptions?.alert,category:this.adviceOptions?.category,active:this.adviceOptions?.active})}renderSetpointBlock(){return this.renderBlock({variant:Eu.setpoint,value:this.setpoint,valueSize:this.setpointSize,enhanced:this.rowEnhanced,weight:this.setpointWeight,hintedZeros:this.setpointOptions?.hintedZeros??!1,hasSignSpacer:this.setpointOptions?.hasSignSpacer??!1,spaceReserver:this.setpointOptions?.spaceReserver,touching:this.setpointTouching,hidePhase:this.setpointHidePhase,dataQuality:this.setpointOptions?.dataQuality,alert:this.setpointOptions?.alert})}renderValueReading(){return O`
      <div
        class=${F({"value-reading":!0,...this.dataQualityClasses(this.valueOptions?.dataQuality)})}
        part="value-reading"
      >
        ${this.renderBlock({variant:Eu.value,value:this.value,valueType:this.valueType,valueSize:this.valueSize,enhanced:this.rowEnhanced,weight:this.valueWeight,hintedZeros:this.valueOptions?.hintedZeros??!1,hasSignSpacer:this.valueOptions?.hasSignSpacer??!1,spaceReserver:this.valueOptions?.spaceReserver,off:this.off,hasIcon:this.valueOptions?.hasIcon??!1})}
        ${this.renderDegreeColumn()} ${this.renderValueAlertOverlay()}
      </div>
    `}renderValueAlertOverlay(){let e=this.valueOptions?.alert;if(typeof e!=`object`||!e)return A;let t=e.thickness??jl.Small;return O`
      <div class="value-alert-overlay" aria-hidden="true">
        <obc-alert-frame
          part="value-alert-frame"
          .type=${e.type??Al.Regular}
          .thickness=${t}
          .status=${e.status??B.Alarm}
          .mode=${e.mode??Ml.ackedActive}
          .flashingSpeed=${e.flashingSpeed??V.Default}
          .showIcon=${e.showIcon??!1}
          .showAlertCategoryIcon=${e.showAlertCategoryIcon??!0}
          .wrapContent=${!1}
          .fullWidth=${!1}
        ></obc-alert-frame>
      </div>
    `}renderMetaZone(){if(!this.label&&!this.unit)return A;let e=this.isHorizontal||this.resolvedStacking===`stacked`;return O`
      <div
        class=${F({meta:!0,"meta-inline":!e,"meta-stacked":e,"label-only":!!this.label&&!this.unit,"unit-only":!!this.unit&&!this.label})}
        part="meta-wrapper"
      >
        ${this.hasLeadingIcon?O`<span class="leading-icon" aria-hidden="true"
                ><slot name="leading-icon"></slot
              ></span>`:A}
        <div class="meta-labels" part="meta-labels">
          ${this.label?this.renderTextbox(`label`,this.label,this.labelOptions?.spaceReserver):A}
          ${this.unit?this.renderTextbox(`unit`,this.unit,this.unitOptions?.spaceReserver):A}
        </div>
      </div>
    `}renderSourceContent(){let e=this.resolvedSourceInteraction,t=this.src??``,n=F({"source-button":!0,...this.dataQualityClasses(this.srcOptions?.dataQuality)});if(e===`picker`){let e=O`
        <obc-button
          class=${n}
          variant="flat"
          .fullWidth=${!1}
          showTrailingIcon
          @click=${()=>{this.sourcePickerContentVisible=!this.sourcePickerContentVisible}}
        >
          <obi-drop-down-google slot="trailing-icon"></obi-drop-down-google>
          ${t}
        </obc-button>
      `;return Il(this.srcOptions?.alert??!1,e)}if(e===`flyout`){let e=O`
        <obc-button
          class=${n}
          variant="flat"
          .fullWidth=${!1}
          showTrailingIcon
          @click=${()=>{this.dispatchEvent(new CustomEvent(`source-flyout-click`,{bubbles:!0,composed:!0,detail:{src:t}}))}}
        >
          <obi-chevron-right-google
            slot="trailing-icon"
          ></obi-chevron-right-google>
          ${t}
        </obc-button>
      `;return Il(this.srcOptions?.alert??!1,e)}return this.renderSourceBlock(t)}renderSourceBlock(e){let t=this.srcOptions?.state??Gu.regular,n=this.srcOptions?.deviation,r=n!==void 0&&Number.isFinite(n),i=this.renderTextbox(`source`,e,this.srcOptions?.spaceReserver,this.srcOptions);return t===Gu.regular&&!r?i:O`
      <div
        class=${F({"source-block":!0,[`source-state-${t}`]:t!==Gu.regular})}
        part="source-block"
      >
        ${i}
        ${r?O`<span class="source-deviation">
                <obi-delta aria-hidden="true"></obi-delta>
                <obc-textbox
                  class="source-deviation-value"
                  .size=${Bl.xs}
                  .tabularNums=${!0}
                  alignment="left"
                  >${n}</obc-textbox
                >
              </span>`:A}
      </div>
    `}renderSource(){return this.hasSrc?O`
      ${this.isHorizontal?O`<div
              class="divider divider-vertical"
              part="divider"
              aria-hidden="true"
            ></div>`:A}
      <div class="source-row" part="source-wrapper">
        ${this.renderSourceContent()}
      </div>
    `:A}getSourcePickerNavigationItems(){return(this.sourcePickerSlot?.assignedElements({flatten:!0})??[]).flatMap(e=>e instanceof HTMLElement?e.localName===`obc-navigation-item`?[e]:Array.from(e.querySelectorAll(`obc-navigation-item`)):[])}createSourcePickerOptionIcon(e){let t=e.querySelector(`[slot="icon"]`);if(t instanceof HTMLElement)return O`${t.cloneNode(!0)}`}getSourcePickerItemInfo(e,t){let n=e,r=n.label||e.getAttribute(`label`)||``;return{itemLabel:r,itemValue:e.getAttribute(`data-value`)||n.value||e.getAttribute(`value`)||r||`source-option-${t}`}}findSourcePickerOptionElement(e){let t=this.getSourcePickerNavigationItems();for(let[n,r]of t.entries()){let{itemValue:t}=this.getSourcePickerItemInfo(r,n);if(t===e)return r}}handleSourcePickerItemClick(e){this.dispatchEvent(new CustomEvent(`source-change`,{bubbles:!0,composed:!0,detail:{value:e.detail.value,label:e.detail.option?.label}})),this.findSourcePickerOptionElement(e.detail.value)?.click(),this.sourcePickerContentVisible=!1}get selectedSourceValues(){return this.src?[this.sourcePickerOptions.find(e=>e.value===this.src||e.label===this.src)?.value??this.src]:[]}renderSourcePickerContent(){return this.resolvedSourceInteraction!==`picker`||!this.sourcePickerContentVisible?A:O`
      <obc-context-menu-input
        .type=${dd.Regular}
        .options=${this.sourcePickerOptions}
        .selectedValues=${this.selectedSourceValues}
        class="source-picker-content"
        @item-click=${this.handleSourcePickerItemClick}
        @close=${()=>{this.sourcePickerContentVisible=!1}}
      ></obc-context-menu-input>
    `}renderSourcePickerSlot(){return O`
      <slot
        name="src-picker-content"
        hidden
        @slotchange=${this.syncSourcePickerOptions}
      ></slot>
    `}renderSetpointWidthReserve(e){return!this.hasDynamicSetpoint||this.isHorizontal?A:O`<div class="setpoint-width-reserve" aria-hidden="true">
      ${e===`setpoint`?this.renderBlock({variant:Eu.setpoint,value:this.setpoint,valueSize:this.primarySize,enhanced:!1,weight:Vl.semibold,hintedZeros:this.setpointOptions?.hintedZeros??!1,hasSignSpacer:this.setpointOptions?.hasSignSpacer??!1,spaceReserver:this.setpointOptions?.spaceReserver,alert:this.setpointOptions?.alert,ghost:!0}):O`${this.renderBlock({variant:Eu.value,value:this.value,valueType:this.valueType,valueSize:this.primarySize,enhanced:!1,weight:this.valueWeight,hintedZeros:this.valueOptions?.hintedZeros??!1,hasSignSpacer:this.valueOptions?.hasSignSpacer??!1,spaceReserver:this.valueOptions?.spaceReserver,off:this.off,hasIcon:this.valueOptions?.hasIcon??!1,ghost:!0})}${this.renderDegreeColumn(this.primarySize)}`}
    </div>`}renderVerticalLayout(){return O`
      <div class="value-cluster" part="value-cluster">
        ${this.hasAdvice?O`<div class="advice-row" part="advice-wrapper">
                ${this.renderAdviceBlock()}
              </div>`:A}
        ${this.hasSetpoint?O`<div class="setpoint-row" part="setpoint-wrapper">
                ${this.renderSetpointBlock()}
                ${this.renderSetpointWidthReserve(`setpoint`)}
              </div>`:A}
        ${this.hasValue?O`<div class="value-row" part="value-wrapper">
                ${this.renderValueReading()}
                ${this.renderSetpointWidthReserve(`value`)}
              </div>`:A}
      </div>
      ${this.renderMetaZone()} ${this.renderSource()}
    `}renderHorizontalLayout(){return O`
      <div class="inline-row" part="value-cluster">
        ${this.hasAdvice?O`<div class="advice-row" part="advice-wrapper">
                ${this.renderAdviceBlock()}
              </div>`:A}
        ${this.hasSetpoint?O`<div class="setpoint-row" part="setpoint-wrapper">
                ${this.renderSetpointBlock()}
              </div>`:A}
        ${this.hasValue?O`<div class="value-row" part="value-wrapper">
                ${this.renderValueReading()}
              </div>`:A}
        ${this.renderMetaZone()} ${this.renderSource()}
      </div>
    `}willUpdate(e){super.willUpdate(e),Zl(`obc-readout`,this.value,this.valueType),ql(`obc-readout`,this.fractionDigits),this.warnHorizontalSizeIgnored()}warnHorizontalSizeIgnored(){!this.hasWarnedHorizontalSize&&this.isHorizontal&&this.size&&this.size!==hd.large&&(this.hasWarnedHorizontalSize=!0,console.warn(`[obc-readout] size="${this.size}" is ignored when direction="horizontal": the horizontal arrangement exists in the large tier only. Remove the size, or use direction="vertical" for the small / medium tiers.`,this))}updated(e){super.updated(e),e.has(`sourcePickerContentVisible`)&&(this.sourcePickerContentVisible?window.addEventListener(`pointerdown`,this.onWindowPointerDown,!0):window.removeEventListener(`pointerdown`,this.onWindowPointerDown,!0));let t=!this.hasCompletedFirstUpdate;if(this.hasCompletedFirstUpdate=!0,!this.isPopUp||this.setpointTouching){this.clearDeferredSetpointHide();return}let n=this.hasSetpoint&&this.isAtSetpoint;if(t){this.deferredSetpointHidePhase=n?q.hidden:q.none;return}if(!n){this.clearDeferredSetpointHide();return}this.deferredSetpointHidePhase===q.none&&(this.deferredSetpointHidePhase=q.hiding,window.clearTimeout(this.deferredSetpointHideTimer),this.deferredSetpointHideTimer=window.setTimeout(()=>{this.deferredSetpointHidePhase=q.hidden,this.deferredSetpointHideTimer=void 0},100))}clearDeferredSetpointHide(){this.deferredSetpointHidePhase!==q.none&&(this.deferredSetpointHidePhase=q.none),window.clearTimeout(this.deferredSetpointHideTimer),this.deferredSetpointHideTimer=void 0}disconnectedCallback(){window.removeEventListener(`pointerdown`,this.onWindowPointerDown,!0),window.clearTimeout(this.deferredSetpointHideTimer),this.deferredSetpointHideTimer=void 0,this.deferredSetpointHidePhase===q.hiding&&(this.deferredSetpointHidePhase=q.hidden),super.disconnectedCallback()}render(){let e=this.dataQuality,t=O`
      <div class=${F({readout:!0,[`size-${this.resolvedSize}`]:!0,[`direction-${this.resolvedDirection}`]:!0,[`stacking-${this.resolvedStacking}`]:!0,[`alignment-${this.resolvedAlignment}`]:!0,[`priority-${this.resolvedPriority}`]:!0,"data-low-integrity":e===_d.lowIntegrity,"data-invalid":e===_d.invalid,"flip-flop":this.isFlipFlop,"setpoint-dynamic":this.hasDynamicSetpoint})} part="root">
        ${this.isHorizontal?this.renderHorizontalLayout():this.renderVerticalLayout()}
        ${this.renderSourcePickerSlot()}
      </div>
      ${this.renderSourcePickerContent()}
    `;return Il(this.alert===!0?{}:this.alert,t)}},md.styles=a(Au),md);N([P({type:String})],X.prototype,`label`,void 0),N([P({type:String})],X.prototype,`unit`,void 0),N([P({type:String})],X.prototype,`src`,void 0),N([P({type:Boolean,attribute:!1})],X.prototype,`hasValue`,void 0),N([P({type:String})],X.prototype,`value`,void 0),N([P({type:String})],X.prototype,`valueType`,void 0),N([P({type:Boolean})],X.prototype,`off`,void 0),N([P({type:String})],X.prototype,`offText`,void 0),N([P({type:Boolean})],X.prototype,`hasSetpoint`,void 0),N([P({type:Number})],X.prototype,`setpoint`,void 0),N([P({type:Boolean})],X.prototype,`hasAdvice`,void 0),N([P({type:Number})],X.prototype,`advice`,void 0),N([P({type:String})],X.prototype,`size`,void 0),N([P({type:String})],X.prototype,`priority`,void 0),N([P({type:String})],X.prototype,`direction`,void 0),N([P({type:String})],X.prototype,`stacking`,void 0),N([P({type:String})],X.prototype,`alignment`,void 0),N([P({type:Boolean})],X.prototype,`hasDegree`,void 0),N([P({type:Boolean})],X.prototype,`hasDegreeSpacer`,void 0),N([P({type:Boolean})],X.prototype,`hasLeadingIcon`,void 0),N([P({type:Number})],X.prototype,`fractionDigits`,void 0),N([P({type:Number})],X.prototype,`maxDigits`,void 0),N([P({type:String})],X.prototype,`dataQuality`,void 0),N([P({type:Object})],X.prototype,`alert`,void 0),N([P({type:Object})],X.prototype,`valueOptions`,void 0),N([P({type:Object})],X.prototype,`setpointOptions`,void 0),N([P({type:Object})],X.prototype,`adviceOptions`,void 0),N([P({type:Object})],X.prototype,`labelOptions`,void 0),N([P({type:Object})],X.prototype,`unitOptions`,void 0),N([P({type:Object})],X.prototype,`srcOptions`,void 0),N([P({type:Boolean,reflect:!0})],X.prototype,`showDebugOverlay`,void 0),N([ze()],X.prototype,`deferredSetpointHidePhase`,void 0),N([ze()],X.prototype,`sourcePickerContentVisible`,void 0),N([ze()],X.prototype,`sourcePickerOptions`,void 0),N([Ve(`slot[name="src-picker-content"]`)],X.prototype,`sourcePickerSlot`,void 0),X=N([M(`obc-readout`)],X);function Sd(e){let{value:t,label:n=``,unit:r=``,fractionDigits:i=0,priority:a,size:o=hd.large,direction:s=yd.vertical,stacking:c=bd.inline,alignment:l=xd.vertical,hasValue:u=!0,centerValue:d=!1,centerMeta:f=!1,className:p,hintedZeros:m=!1,maxDigits:h=0}=e;return O`
    <obc-readout
      class=${F({[p??``]:!!p,"instrument-readout-center-value":d,"instrument-readout-center-meta":f})}
      .size=${o}
      .priority=${a}
      .direction=${s}
      .stacking=${c}
      .alignment=${l}
      .hasValue=${u}
      .hasSetpoint=${!1}
      .hasAdvice=${!1}
      .value=${t??null}
      .fractionDigits=${i}
      .label=${n}
      .unit=${r}
      .valueOptions=${m?{hintedZeros:m}:void 0}
      .maxDigits=${h}
      @source-flyout-click=${or}
      @source-change=${or}
    ></obc-readout>
  `}var Cd=function(e){return e.hdg=`hdg`,e.cog=`cog`,e.rot=`rot`,e}({}),wd={hdg:{label:`HDG`,unit:`DEG`},cog:{label:`COG`,unit:`DEG`},rot:{label:`ROT`,unit:`°/min`}};function Td(e,t){return e.map((e,n)=>{let r=wd[e.source],i;switch(e.source){case`hdg`:i=t.heading;break;case`cog`:i=t.courseOverGround;break;case`rot`:i=t.rateOfTurnDegreesPerMinute??null}return{value:i,label:e.label??r.label,unit:e.unit??r.unit,fractionDigits:e.fractionDigits??0,size:e.size??(n===0?hd.large:hd.medium),priority:t.priorityFor(e.source)}})}function Ed(e){let t=e.size??hd.large;return Sd({value:e.value??void 0,label:e.label,unit:e.unit,fractionDigits:e.fractionDigits,priority:e.priority,size:t,stacking:t===hd.large?bd.inline:bd.stacked,centerValue:e.centerValue??!1,centerMeta:e.centerMeta??!1})}function Dd(e,t=`primary-secondary`){let[n,...r]=e;return n?t===`row`?O`
      <div class="center-readout-row">
        ${Ed(n)}
        ${r.map(e=>O`
            <div class="center-readout-vertical-divider"></div>
            ${Ed(e)}
          `)}
      </div>
    `:t===`stacked`?O`
      <div class="center-readout-group">
        ${Ed(n)}
        ${r.map(e=>O`
            <div class="center-readout-divider"></div>
            ${Ed(e)}
          `)}
      </div>
    `:O`
    <div class="center-readout-group">
      ${Ed(n)}
      ${r.length>0?O`
              <div class="center-readout-divider"></div>
              <div class="center-readout-secondary-row">
                ${r.map(e=>Ed(e))}
              </div>
            `:A}
    </div>
  `:O`${A}`}var Od=o`
  .center-readout-group {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: fit-content;
    gap: 8px;
  }

  .center-readout-divider {
    align-self: stretch;
    height: 1px;
    background: var(--border-divider-color);
  }

  .center-readout-secondary-row {
    display: flex;
    align-items: flex-start;
    justify-content: center;
    gap: 8px;
  }

  .center-readout-row {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .center-readout-vertical-divider {
    width: 1px;
    height: 48px;
    background: var(--border-divider-color);
  }
`;function kd(e){return k`<g transform="translate(221.97, 94.99)"><g id="shape">
<mask id="hdg-vector-outline" maskUnits="userSpaceOnUse" x="0" y="3.57628e-07" width="68" height="319" fill="black">
<rect fill="white" y="3.57628e-07" width="68" height="319"/>
<path d="M35 318H33V316H35V318ZM35 314H33V312H35V314ZM35 310H33V308H35V310ZM35 306H33V304H35V306ZM35 302H33V300H35V302ZM35 298H33V296H35V298ZM35 294H33V292H35V294ZM35 290H33V288H35V290ZM35 286H33V284H35V286ZM35 282H33V280H35V282ZM35 278H33V276H35V278ZM35 274H33V272H35V274ZM35 270H33V268H35V270ZM35 266H33V264H35V266ZM35 262H33V260H35V262ZM35 258H33V256H35V258ZM35 254H33V252H35V254ZM35 250H33V248H35V250ZM35 246H33V244H35V246ZM35 242H33V240H35V242ZM35 238H33V236H35V238ZM35 234H33V232H35V234ZM35 230H33V228H35V230ZM35 226H33V224H35V226ZM35 222H33V220H35V222ZM35 218H33V216H35V218ZM35 214H33V212H35V214ZM35 210H33V208H35V210ZM35 206H33V204H35V206ZM35 202H33V200H35V202ZM35 198H33V196H35V198ZM35 194H33V192H35V194ZM35 190H33V188H35V190ZM35 186H33V184H35V186ZM35 182H33V180H35V182ZM35 178H33V176H35V178ZM35 174H33V172H35V174ZM35 170H33V168H35V170ZM33.0664 1.62109C33.4035 0.792969 34.5965 0.792968 34.9336 1.62109L49.8486 38.2803C50.5669 40.0456 48.5838 41.6925 46.9336 40.7012L35 33.5947V157.126C36.4056 157.488 37.5122 158.594 37.874 160H66C66.5522 160 66.9999 160.448 67 161C67 161.552 66.5523 162 66 162H37.874C37.5123 163.406 36.4056 164.512 35 164.874V166H33V164.874C31.5944 164.512 30.4877 163.406 30.126 162H2C1.44772 162 1 161.552 1 161C1.00006 160.448 1.44775 160 2 160H30.126C30.4878 158.594 31.5944 157.488 33 157.126V33.5947L21.0664 40.7012C19.4162 41.6925 17.4331 40.0456 18.1514 38.2803L33.0664 1.62109ZM32.2695 162C32.6155 162.597 33.26 163 34 163C34.74 163 35.3845 162.597 35.7305 162H32.2695ZM33 159.27C32.697 159.445 32.445 159.697 32.2695 160H33V159.27ZM35 160H35.7305C35.555 159.697 35.303 159.445 35 159.27V160Z"/>
</mask>
<path d="M35 318H33V316H35V318ZM35 314H33V312H35V314ZM35 310H33V308H35V310ZM35 306H33V304H35V306ZM35 302H33V300H35V302ZM35 298H33V296H35V298ZM35 294H33V292H35V294ZM35 290H33V288H35V290ZM35 286H33V284H35V286ZM35 282H33V280H35V282ZM35 278H33V276H35V278ZM35 274H33V272H35V274ZM35 270H33V268H35V270ZM35 266H33V264H35V266ZM35 262H33V260H35V262ZM35 258H33V256H35V258ZM35 254H33V252H35V254ZM35 250H33V248H35V250ZM35 246H33V244H35V246ZM35 242H33V240H35V242ZM35 238H33V236H35V238ZM35 234H33V232H35V234ZM35 230H33V228H35V230ZM35 226H33V224H35V226ZM35 222H33V220H35V222ZM35 218H33V216H35V218ZM35 214H33V212H35V214ZM35 210H33V208H35V210ZM35 206H33V204H35V206ZM35 202H33V200H35V202ZM35 198H33V196H35V198ZM35 194H33V192H35V194ZM35 190H33V188H35V190ZM35 186H33V184H35V186ZM35 182H33V180H35V182ZM35 178H33V176H35V178ZM35 174H33V172H35V174ZM35 170H33V168H35V170ZM33.0664 1.62109C33.4035 0.792969 34.5965 0.792968 34.9336 1.62109L49.8486 38.2803C50.5669 40.0456 48.5838 41.6925 46.9336 40.7012L35 33.5947V157.126C36.4056 157.488 37.5122 158.594 37.874 160H66C66.5522 160 66.9999 160.448 67 161C67 161.552 66.5523 162 66 162H37.874C37.5123 163.406 36.4056 164.512 35 164.874V166H33V164.874C31.5944 164.512 30.4877 163.406 30.126 162H2C1.44772 162 1 161.552 1 161C1.00006 160.448 1.44775 160 2 160H30.126C30.4878 158.594 31.5944 157.488 33 157.126V33.5947L21.0664 40.7012C19.4162 41.6925 17.4331 40.0456 18.1514 38.2803L33.0664 1.62109ZM32.2695 162C32.6155 162.597 33.26 163 34 163C34.74 163 35.3845 162.597 35.7305 162H32.2695ZM33 159.27C32.697 159.445 32.445 159.697 32.2695 160H33V159.27ZM35 160H35.7305C35.555 159.697 35.303 159.445 35 159.27V160Z" fill=${e}/>
<path d="M35 318V319H36V318H35ZM33 318H32V319H33V318ZM33 316V315H32V316H33ZM35 316H36V315H35V316ZM35 314V315H36V314H35ZM33 314H32V315H33V314ZM33 312V311H32V312H33ZM35 312H36V311H35V312ZM35 310V311H36V310H35ZM33 310H32V311H33V310ZM33 308V307H32V308H33ZM35 308H36V307H35V308ZM35 306V307H36V306H35ZM33 306H32V307H33V306ZM33 304V303H32V304H33ZM35 304H36V303H35V304ZM35 302V303H36V302H35ZM33 302H32V303H33V302ZM33 300V299H32V300H33ZM35 300H36V299H35V300ZM35 298V299H36V298H35ZM33 298H32V299H33V298ZM33 296V295H32V296H33ZM35 296H36V295H35V296ZM35 294V295H36V294H35ZM33 294H32V295H33V294ZM33 292V291H32V292H33ZM35 292H36V291H35V292ZM35 290V291H36V290H35ZM33 290H32V291H33V290ZM33 288V287H32V288H33ZM35 288H36V287H35V288ZM35 286V287H36V286H35ZM33 286H32V287H33V286ZM33 284V283H32V284H33ZM35 284H36V283H35V284ZM35 282V283H36V282H35ZM33 282H32V283H33V282ZM33 280V279H32V280H33ZM35 280H36V279H35V280ZM35 278V279H36V278H35ZM33 278H32V279H33V278ZM33 276V275H32V276H33ZM35 276H36V275H35V276ZM35 274V275H36V274H35ZM33 274H32V275H33V274ZM33 272V271H32V272H33ZM35 272H36V271H35V272ZM35 270V271H36V270H35ZM33 270H32V271H33V270ZM33 268V267H32V268H33ZM35 268H36V267H35V268ZM35 266V267H36V266H35ZM33 266H32V267H33V266ZM33 264V263H32V264H33ZM35 264H36V263H35V264ZM35 262V263H36V262H35ZM33 262H32V263H33V262ZM33 260V259H32V260H33ZM35 260H36V259H35V260ZM35 258V259H36V258H35ZM33 258H32V259H33V258ZM33 256V255H32V256H33ZM35 256H36V255H35V256ZM35 254V255H36V254H35ZM33 254H32V255H33V254ZM33 252V251H32V252H33ZM35 252H36V251H35V252ZM35 250V251H36V250H35ZM33 250H32V251H33V250ZM33 248V247H32V248H33ZM35 248H36V247H35V248ZM35 246V247H36V246H35ZM33 246H32V247H33V246ZM33 244V243H32V244H33ZM35 244H36V243H35V244ZM35 242V243H36V242H35ZM33 242H32V243H33V242ZM33 240V239H32V240H33ZM35 240H36V239H35V240ZM35 238V239H36V238H35ZM33 238H32V239H33V238ZM33 236V235H32V236H33ZM35 236H36V235H35V236ZM35 234V235H36V234H35ZM33 234H32V235H33V234ZM33 232V231H32V232H33ZM35 232H36V231H35V232ZM35 230V231H36V230H35ZM33 230H32V231H33V230ZM33 228V227H32V228H33ZM35 228H36V227H35V228ZM35 226V227H36V226H35ZM33 226H32V227H33V226ZM33 224V223H32V224H33ZM35 224H36V223H35V224ZM35 222V223H36V222H35ZM33 222H32V223H33V222ZM33 220V219H32V220H33ZM35 220H36V219H35V220ZM35 218V219H36V218H35ZM33 218H32V219H33V218ZM33 216V215H32V216H33ZM35 216H36V215H35V216ZM35 214V215H36V214H35ZM33 214H32V215H33V214ZM33 212V211H32V212H33ZM35 212H36V211H35V212ZM35 210V211H36V210H35ZM33 210H32V211H33V210ZM33 208V207H32V208H33ZM35 208H36V207H35V208ZM35 206V207H36V206H35ZM33 206H32V207H33V206ZM33 204V203H32V204H33ZM35 204H36V203H35V204ZM35 202V203H36V202H35ZM33 202H32V203H33V202ZM33 200V199H32V200H33ZM35 200H36V199H35V200ZM35 198V199H36V198H35ZM33 198H32V199H33V198ZM33 196V195H32V196H33ZM35 196H36V195H35V196ZM35 194V195H36V194H35ZM33 194H32V195H33V194ZM33 192V191H32V192H33ZM35 192H36V191H35V192ZM35 190V191H36V190H35ZM33 190H32V191H33V190ZM33 188V187H32V188H33ZM35 188H36V187H35V188ZM35 186V187H36V186H35ZM33 186H32V187H33V186ZM33 184V183H32V184H33ZM35 184H36V183H35V184ZM35 182V183H36V182H35ZM33 182H32V183H33V182ZM33 180V179H32V180H33ZM35 180H36V179H35V180ZM35 178V179H36V178H35ZM33 178H32V179H33V178ZM33 176V175H32V176H33ZM35 176H36V175H35V176ZM35 174V175H36V174H35ZM33 174H32V175H33V174ZM33 172V171H32V172H33ZM35 172H36V171H35V172ZM35 170V171H36V170H35ZM33 170H32V171H33V170ZM33 168V167H32V168H33ZM35 168H36V167H35V168ZM33.0664 1.62109L32.1402 1.24406L32.1401 1.24423L33.0664 1.62109ZM34.9336 1.62109L35.8599 1.24423L35.8598 1.24406L34.9336 1.62109ZM49.8486 38.2803L48.9224 38.6571L48.9224 38.6571L49.8486 38.2803ZM46.9336 40.7012L47.4486 39.844L47.4452 39.842L46.9336 40.7012ZM35 33.5947L35.5117 32.7355L34 31.8353V33.5947H35ZM35 157.126H34V157.901L34.7508 158.094L35 157.126ZM37.874 160L36.9056 160.249L37.0988 161H37.874V160ZM67 161H68V161L67 161ZM37.874 162V161H37.0988L36.9056 161.751L37.874 162ZM35 164.874L34.7507 163.906L34 164.099V164.874H35ZM35 166V167H36V166H35ZM33 166H32V167H33V166ZM33 164.874H34V164.099L33.2493 163.906L33 164.874ZM30.126 162L31.0944 161.751L30.9012 161H30.126V162ZM1 161L0 161V161H1ZM30.126 160V161H30.9012L31.0944 160.249L30.126 160ZM33 157.126L33.2492 158.094L34 157.901V157.126H33ZM33 33.5947H34V31.8353L32.4883 32.7355L33 33.5947ZM21.0664 40.7012L20.5548 39.842L20.5514 39.844L21.0664 40.7012ZM18.1514 38.2803L19.0776 38.6571L19.0776 38.6571L18.1514 38.2803ZM32.2695 162V161H30.5349L31.4042 162.501L32.2695 162ZM34 163V164V164V163ZM35.7305 162L36.5959 162.501L37.4651 161H35.7305V162ZM33 159.27H34V157.535L32.4989 158.404L33 159.27ZM32.2695 160L31.4042 159.499L30.5347 161H32.2695V160ZM33 160V161H34V160H33ZM35 160H34V161H35V160ZM35.7305 160V161H37.4653L36.5958 159.499L35.7305 160ZM35 159.27L35.5011 158.404L34 157.535V159.27H35ZM35 318V317H33V318V319H35V318ZM33 318H34V316H33H32V318H33ZM33 316V317H35V316V315H33V316ZM35 316H34V318H35H36V316H35ZM35 314V313H33V314V315H35V314ZM33 314H34V312H33H32V314H33ZM33 312V313H35V312V311H33V312ZM35 312H34V314H35H36V312H35ZM35 310V309H33V310V311H35V310ZM33 310H34V308H33H32V310H33ZM33 308V309H35V308V307H33V308ZM35 308H34V310H35H36V308H35ZM35 306V305H33V306V307H35V306ZM33 306H34V304H33H32V306H33ZM33 304V305H35V304V303H33V304ZM35 304H34V306H35H36V304H35ZM35 302V301H33V302V303H35V302ZM33 302H34V300H33H32V302H33ZM33 300V301H35V300V299H33V300ZM35 300H34V302H35H36V300H35ZM35 298V297H33V298V299H35V298ZM33 298H34V296H33H32V298H33ZM33 296V297H35V296V295H33V296ZM35 296H34V298H35H36V296H35ZM35 294V293H33V294V295H35V294ZM33 294H34V292H33H32V294H33ZM33 292V293H35V292V291H33V292ZM35 292H34V294H35H36V292H35ZM35 290V289H33V290V291H35V290ZM33 290H34V288H33H32V290H33ZM33 288V289H35V288V287H33V288ZM35 288H34V290H35H36V288H35ZM35 286V285H33V286V287H35V286ZM33 286H34V284H33H32V286H33ZM33 284V285H35V284V283H33V284ZM35 284H34V286H35H36V284H35ZM35 282V281H33V282V283H35V282ZM33 282H34V280H33H32V282H33ZM33 280V281H35V280V279H33V280ZM35 280H34V282H35H36V280H35ZM35 278V277H33V278V279H35V278ZM33 278H34V276H33H32V278H33ZM33 276V277H35V276V275H33V276ZM35 276H34V278H35H36V276H35ZM35 274V273H33V274V275H35V274ZM33 274H34V272H33H32V274H33ZM33 272V273H35V272V271H33V272ZM35 272H34V274H35H36V272H35ZM35 270V269H33V270V271H35V270ZM33 270H34V268H33H32V270H33ZM33 268V269H35V268V267H33V268ZM35 268H34V270H35H36V268H35ZM35 266V265H33V266V267H35V266ZM33 266H34V264H33H32V266H33ZM33 264V265H35V264V263H33V264ZM35 264H34V266H35H36V264H35ZM35 262V261H33V262V263H35V262ZM33 262H34V260H33H32V262H33ZM33 260V261H35V260V259H33V260ZM35 260H34V262H35H36V260H35ZM35 258V257H33V258V259H35V258ZM33 258H34V256H33H32V258H33ZM33 256V257H35V256V255H33V256ZM35 256H34V258H35H36V256H35ZM35 254V253H33V254V255H35V254ZM33 254H34V252H33H32V254H33ZM33 252V253H35V252V251H33V252ZM35 252H34V254H35H36V252H35ZM35 250V249H33V250V251H35V250ZM33 250H34V248H33H32V250H33ZM33 248V249H35V248V247H33V248ZM35 248H34V250H35H36V248H35ZM35 246V245H33V246V247H35V246ZM33 246H34V244H33H32V246H33ZM33 244V245H35V244V243H33V244ZM35 244H34V246H35H36V244H35ZM35 242V241H33V242V243H35V242ZM33 242H34V240H33H32V242H33ZM33 240V241H35V240V239H33V240ZM35 240H34V242H35H36V240H35ZM35 238V237H33V238V239H35V238ZM33 238H34V236H33H32V238H33ZM33 236V237H35V236V235H33V236ZM35 236H34V238H35H36V236H35ZM35 234V233H33V234V235H35V234ZM33 234H34V232H33H32V234H33ZM33 232V233H35V232V231H33V232ZM35 232H34V234H35H36V232H35ZM35 230V229H33V230V231H35V230ZM33 230H34V228H33H32V230H33ZM33 228V229H35V228V227H33V228ZM35 228H34V230H35H36V228H35ZM35 226V225H33V226V227H35V226ZM33 226H34V224H33H32V226H33ZM33 224V225H35V224V223H33V224ZM35 224H34V226H35H36V224H35ZM35 222V221H33V222V223H35V222ZM33 222H34V220H33H32V222H33ZM33 220V221H35V220V219H33V220ZM35 220H34V222H35H36V220H35ZM35 218V217H33V218V219H35V218ZM33 218H34V216H33H32V218H33ZM33 216V217H35V216V215H33V216ZM35 216H34V218H35H36V216H35ZM35 214V213H33V214V215H35V214ZM33 214H34V212H33H32V214H33ZM33 212V213H35V212V211H33V212ZM35 212H34V214H35H36V212H35ZM35 210V209H33V210V211H35V210ZM33 210H34V208H33H32V210H33ZM33 208V209H35V208V207H33V208ZM35 208H34V210H35H36V208H35ZM35 206V205H33V206V207H35V206ZM33 206H34V204H33H32V206H33ZM33 204V205H35V204V203H33V204ZM35 204H34V206H35H36V204H35ZM35 202V201H33V202V203H35V202ZM33 202H34V200H33H32V202H33ZM33 200V201H35V200V199H33V200ZM35 200H34V202H35H36V200H35ZM35 198V197H33V198V199H35V198ZM33 198H34V196H33H32V198H33ZM33 196V197H35V196V195H33V196ZM35 196H34V198H35H36V196H35ZM35 194V193H33V194V195H35V194ZM33 194H34V192H33H32V194H33ZM33 192V193H35V192V191H33V192ZM35 192H34V194H35H36V192H35ZM35 190V189H33V190V191H35V190ZM33 190H34V188H33H32V190H33ZM33 188V189H35V188V187H33V188ZM35 188H34V190H35H36V188H35ZM35 186V185H33V186V187H35V186ZM33 186H34V184H33H32V186H33ZM33 184V185H35V184V183H33V184ZM35 184H34V186H35H36V184H35ZM35 182V181H33V182V183H35V182ZM33 182H34V180H33H32V182H33ZM33 180V181H35V180V179H33V180ZM35 180H34V182H35H36V180H35ZM35 178V177H33V178V179H35V178ZM33 178H34V176H33H32V178H33ZM33 176V177H35V176V175H33V176ZM35 176H34V178H35H36V176H35ZM35 174V173H33V174V175H35V174ZM33 174H34V172H33H32V174H33ZM33 172V173H35V172V171H33V172ZM35 172H34V174H35H36V172H35ZM35 170V169H33V170V171H35V170ZM33 170H34V168H33H32V170H33ZM33 168V169H35V168V167H33V168ZM35 168H34V170H35H36V168H35ZM33.0664 1.62109L33.9926 1.99813C33.9942 1.99419 33.9953 1.99243 33.9953 1.99232C33.9954 1.99219 33.9949 1.99303 33.9937 1.99444C33.9911 1.99759 33.9879 2.00016 33.9855 2.00166C33.9835 2.00295 33.9835 2.0025 33.9865 2.00168C33.9895 2.00082 33.9942 2 34 2C34.0058 2 34.0105 2.00082 34.0135 2.00168C34.0165 2.0025 34.0165 2.00295 34.0145 2.00166C34.0121 2.00016 34.0089 1.99759 34.0063 1.99444C34.0051 1.99303 34.0046 1.99219 34.0047 1.99231C34.0047 1.99243 34.0058 1.99418 34.0074 1.99813L34.9336 1.62109L35.8598 1.24406C35.1846 -0.414691 32.8154 -0.41468 32.1402 1.24406L33.0664 1.62109ZM34.9336 1.62109L34.0073 1.99795L48.9224 38.6571L49.8486 38.2803L50.7749 37.9034L35.8599 1.24423L34.9336 1.62109ZM49.8486 38.2803L48.9224 38.6571C49.2546 39.4736 48.3296 40.3732 47.4486 39.844L46.9336 40.7012L46.4186 41.5584C48.8381 43.0119 51.8792 40.6176 50.7749 37.9034L49.8486 38.2803ZM46.9336 40.7012L47.4452 39.842L35.5117 32.7355L35 33.5947L34.4883 34.4539L46.4219 41.5604L46.9336 40.7012ZM35 33.5947H34V157.126H35H36V33.5947H35ZM35 157.126L34.7508 158.094C35.8035 158.365 36.6346 159.197 36.9056 160.249L37.874 160L38.8425 159.751C38.3898 157.992 37.0077 156.61 35.2492 156.158L35 157.126ZM37.874 160V161H66V160V159H37.874V160ZM66 160V161V161L67 161L68 161C67.9999 159.896 67.1046 159 66 159V160ZM67 161H66V162V163C67.1046 163 68 162.105 68 161H67ZM66 162V161H37.874V162V163H66V162ZM37.874 162L36.9056 161.751C36.6346 162.804 35.8036 163.635 34.7507 163.906L35 164.874L35.2493 165.842C37.0077 165.39 38.3899 164.008 38.8425 162.249L37.874 162ZM35 164.874H34V166H35H36V164.874H35ZM35 166V165H33V166V167H35V166ZM33 166H34V164.874H33H32V166H33ZM33 164.874L33.2493 163.906C32.1964 163.635 31.3654 162.804 31.0944 161.751L30.126 162L29.1575 162.249C29.6101 164.008 30.9923 165.39 32.7507 165.842L33 164.874ZM30.126 162V161H2V162V163H30.126V162ZM2 162V161H1H0C0 162.105 0.89543 163 2 163V162ZM1 161L2 161V161V160V159C0.895362 159 0.000115454 159.896 0 161L1 161ZM2 160V161H30.126V160V159H2V160ZM30.126 160L31.0944 160.249C31.3654 159.197 32.1965 158.365 33.2492 158.094L33 157.126L32.7507 156.158C30.9923 156.61 29.6102 157.992 29.1575 159.751L30.126 160ZM33 157.126H34V33.5947H33H32V157.126H33ZM33 33.5947L32.4883 32.7355L20.5548 39.842L21.0664 40.7012L21.5781 41.5604L33.5117 34.4539L33 33.5947ZM21.0664 40.7012L20.5514 39.844C19.6704 40.3732 18.7454 39.4736 19.0776 38.6571L18.1514 38.2803L17.2251 37.9034C16.1208 40.6176 19.1619 43.0119 21.5814 41.5584L21.0664 40.7012ZM18.1514 38.2803L19.0776 38.6571L33.9927 1.99795L33.0664 1.62109L32.1401 1.24423L17.2251 37.9034L18.1514 38.2803ZM32.2695 162L31.4042 162.501C31.9207 163.393 32.8872 164 34 164V163V162C33.6329 162 33.3102 161.802 33.1349 161.499L32.2695 162ZM34 163V164C35.1128 164 36.0793 163.393 36.5959 162.501L35.7305 162L34.8651 161.499C34.6898 161.802 34.3671 162 34 162V163ZM35.7305 162V161H32.2695V162V163H35.7305V162ZM33 159.27L32.4989 158.404C32.0447 158.667 31.6671 159.045 31.4042 159.499L32.2695 160L33.1349 160.501C33.2228 160.349 33.3494 160.223 33.5011 160.135L33 159.27ZM32.2695 160V161H33V160V159H32.2695V160ZM33 160H34V159.27H33H32V160H33ZM35 160V161H35.7305V160V159H35V160ZM35.7305 160L36.5958 159.499C36.3329 159.045 35.9553 158.667 35.5011 158.404L35 159.27L34.4989 160.135C34.6506 160.223 34.7772 160.349 34.8651 160.501L35.7305 160ZM35 159.27H34V160H35H36V159.27H35Z" fill="var(--border-silhouette-color)" mask="url(#hdg-vector-outline)"/>
</g></g>`}function Ad(e){return k`<g transform="translate(221.97, 100.02)"><g id="shape">
<mask id="hdg-beam-line-outline" maskUnits="userSpaceOnUse" x="0" y="0" width="68" height="314" fill="black">
<rect fill="white" width="68" height="314"/>
<path d="M35 313H33V311H35V313ZM35 309H33V307H35V309ZM35 305H33V303H35V305ZM35 301H33V299H35V301ZM35 297H33V295H35V297ZM35 293H33V291H35V293ZM35 289H33V287H35V289ZM35 285H33V283H35V285ZM35 281H33V279H35V281ZM35 277H33V275H35V277ZM35 273H33V271H35V273ZM35 269H33V267H35V269ZM35 265H33V263H35V265ZM35 261H33V259H35V261ZM35 257H33V255H35V257ZM35 253H33V251H35V253ZM35 249H33V247H35V249ZM35 245H33V243H35V245ZM35 241H33V239H35V241ZM35 237H33V235H35V237ZM35 233H33V231H35V233ZM35 229H33V227H35V229ZM35 225H33V223H35V225ZM35 221H33V219H35V221ZM35 217H33V215H35V217ZM35 213H33V211H35V213ZM35 209H33V207H35V209ZM35 205H33V203H35V205ZM35 201H33V199H35V201ZM35 197H33V195H35V197ZM35 193H33V191H35V193ZM35 189H33V187H35V189ZM35 185H33V183H35V185ZM35 181H33V179H35V181ZM35 177H33V175H35V177ZM35 173H33V171H35V173ZM35 169H33V167H35V169ZM35 165H33V163H35V165ZM34 1C34.5523 1 35 1.44772 35 2V152.126C36.4056 152.488 37.5122 153.594 37.874 155H66C66.5523 155 67 155.448 67 156C67 156.552 66.5523 157 66 157H37.874C37.5122 158.406 36.4056 159.512 35 159.874V161H33V159.874C31.5944 159.512 30.4878 158.406 30.126 157H2C1.44772 157 1 156.552 1 156C1 155.448 1.44772 155 2 155H30.126C30.4878 153.594 31.5944 152.488 33 152.126V2C33 1.44772 33.4477 1 34 1ZM32.2695 157C32.6155 157.597 33.2601 158 34 158C34.7399 158 35.3845 157.597 35.7305 157H32.2695ZM33 154.27C32.697 154.445 32.445 154.697 32.2695 155H33V154.27ZM35 155H35.7305C35.555 154.697 35.303 154.445 35 154.27V155Z"/>
</mask>
<path d="M35 313H33V311H35V313ZM35 309H33V307H35V309ZM35 305H33V303H35V305ZM35 301H33V299H35V301ZM35 297H33V295H35V297ZM35 293H33V291H35V293ZM35 289H33V287H35V289ZM35 285H33V283H35V285ZM35 281H33V279H35V281ZM35 277H33V275H35V277ZM35 273H33V271H35V273ZM35 269H33V267H35V269ZM35 265H33V263H35V265ZM35 261H33V259H35V261ZM35 257H33V255H35V257ZM35 253H33V251H35V253ZM35 249H33V247H35V249ZM35 245H33V243H35V245ZM35 241H33V239H35V241ZM35 237H33V235H35V237ZM35 233H33V231H35V233ZM35 229H33V227H35V229ZM35 225H33V223H35V225ZM35 221H33V219H35V221ZM35 217H33V215H35V217ZM35 213H33V211H35V213ZM35 209H33V207H35V209ZM35 205H33V203H35V205ZM35 201H33V199H35V201ZM35 197H33V195H35V197ZM35 193H33V191H35V193ZM35 189H33V187H35V189ZM35 185H33V183H35V185ZM35 181H33V179H35V181ZM35 177H33V175H35V177ZM35 173H33V171H35V173ZM35 169H33V167H35V169ZM35 165H33V163H35V165ZM34 1C34.5523 1 35 1.44772 35 2V152.126C36.4056 152.488 37.5122 153.594 37.874 155H66C66.5523 155 67 155.448 67 156C67 156.552 66.5523 157 66 157H37.874C37.5122 158.406 36.4056 159.512 35 159.874V161H33V159.874C31.5944 159.512 30.4878 158.406 30.126 157H2C1.44772 157 1 156.552 1 156C1 155.448 1.44772 155 2 155H30.126C30.4878 153.594 31.5944 152.488 33 152.126V2C33 1.44772 33.4477 1 34 1ZM32.2695 157C32.6155 157.597 33.2601 158 34 158C34.7399 158 35.3845 157.597 35.7305 157H32.2695ZM33 154.27C32.697 154.445 32.445 154.697 32.2695 155H33V154.27ZM35 155H35.7305C35.555 154.697 35.303 154.445 35 154.27V155Z" fill=${e}/>
<path d="M35 313V314H36V313H35ZM33 313H32V314H33V313ZM33 311V310H32V311H33ZM35 311H36V310H35V311ZM35 309V310H36V309H35ZM33 309H32V310H33V309ZM33 307V306H32V307H33ZM35 307H36V306H35V307ZM35 305V306H36V305H35ZM33 305H32V306H33V305ZM33 303V302H32V303H33ZM35 303H36V302H35V303ZM35 301V302H36V301H35ZM33 301H32V302H33V301ZM33 299V298H32V299H33ZM35 299H36V298H35V299ZM35 297V298H36V297H35ZM33 297H32V298H33V297ZM33 295V294H32V295H33ZM35 295H36V294H35V295ZM35 293V294H36V293H35ZM33 293H32V294H33V293ZM33 291V290H32V291H33ZM35 291H36V290H35V291ZM35 289V290H36V289H35ZM33 289H32V290H33V289ZM33 287V286H32V287H33ZM35 287H36V286H35V287ZM35 285V286H36V285H35ZM33 285H32V286H33V285ZM33 283V282H32V283H33ZM35 283H36V282H35V283ZM35 281V282H36V281H35ZM33 281H32V282H33V281ZM33 279V278H32V279H33ZM35 279H36V278H35V279ZM35 277V278H36V277H35ZM33 277H32V278H33V277ZM33 275V274H32V275H33ZM35 275H36V274H35V275ZM35 273V274H36V273H35ZM33 273H32V274H33V273ZM33 271V270H32V271H33ZM35 271H36V270H35V271ZM35 269V270H36V269H35ZM33 269H32V270H33V269ZM33 267V266H32V267H33ZM35 267H36V266H35V267ZM35 265V266H36V265H35ZM33 265H32V266H33V265ZM33 263V262H32V263H33ZM35 263H36V262H35V263ZM35 261V262H36V261H35ZM33 261H32V262H33V261ZM33 259V258H32V259H33ZM35 259H36V258H35V259ZM35 257V258H36V257H35ZM33 257H32V258H33V257ZM33 255V254H32V255H33ZM35 255H36V254H35V255ZM35 253V254H36V253H35ZM33 253H32V254H33V253ZM33 251V250H32V251H33ZM35 251H36V250H35V251ZM35 249V250H36V249H35ZM33 249H32V250H33V249ZM33 247V246H32V247H33ZM35 247H36V246H35V247ZM35 245V246H36V245H35ZM33 245H32V246H33V245ZM33 243V242H32V243H33ZM35 243H36V242H35V243ZM35 241V242H36V241H35ZM33 241H32V242H33V241ZM33 239V238H32V239H33ZM35 239H36V238H35V239ZM35 237V238H36V237H35ZM33 237H32V238H33V237ZM33 235V234H32V235H33ZM35 235H36V234H35V235ZM35 233V234H36V233H35ZM33 233H32V234H33V233ZM33 231V230H32V231H33ZM35 231H36V230H35V231ZM35 229V230H36V229H35ZM33 229H32V230H33V229ZM33 227V226H32V227H33ZM35 227H36V226H35V227ZM35 225V226H36V225H35ZM33 225H32V226H33V225ZM33 223V222H32V223H33ZM35 223H36V222H35V223ZM35 221V222H36V221H35ZM33 221H32V222H33V221ZM33 219V218H32V219H33ZM35 219H36V218H35V219ZM35 217V218H36V217H35ZM33 217H32V218H33V217ZM33 215V214H32V215H33ZM35 215H36V214H35V215ZM35 213V214H36V213H35ZM33 213H32V214H33V213ZM33 211V210H32V211H33ZM35 211H36V210H35V211ZM35 209V210H36V209H35ZM33 209H32V210H33V209ZM33 207V206H32V207H33ZM35 207H36V206H35V207ZM35 205V206H36V205H35ZM33 205H32V206H33V205ZM33 203V202H32V203H33ZM35 203H36V202H35V203ZM35 201V202H36V201H35ZM33 201H32V202H33V201ZM33 199V198H32V199H33ZM35 199H36V198H35V199ZM35 197V198H36V197H35ZM33 197H32V198H33V197ZM33 195V194H32V195H33ZM35 195H36V194H35V195ZM35 193V194H36V193H35ZM33 193H32V194H33V193ZM33 191V190H32V191H33ZM35 191H36V190H35V191ZM35 189V190H36V189H35ZM33 189H32V190H33V189ZM33 187V186H32V187H33ZM35 187H36V186H35V187ZM35 185V186H36V185H35ZM33 185H32V186H33V185ZM33 183V182H32V183H33ZM35 183H36V182H35V183ZM35 181V182H36V181H35ZM33 181H32V182H33V181ZM33 179V178H32V179H33ZM35 179H36V178H35V179ZM35 177V178H36V177H35ZM33 177H32V178H33V177ZM33 175V174H32V175H33ZM35 175H36V174H35V175ZM35 173V174H36V173H35ZM33 173H32V174H33V173ZM33 171V170H32V171H33ZM35 171H36V170H35V171ZM35 169V170H36V169H35ZM33 169H32V170H33V169ZM33 167V166H32V167H33ZM35 167H36V166H35V167ZM35 165V166H36V165H35ZM33 165H32V166H33V165ZM33 163V162H32V163H33ZM35 163H36V162H35V163ZM34 1V0V0V1ZM35 2H36V2L35 2ZM35 152.126H34V152.901L34.7507 153.094L35 152.126ZM37.874 155L36.9056 155.249L37.0988 156H37.874V155ZM37.874 157V156H37.0988L36.9056 156.751L37.874 157ZM35 159.874L34.7507 158.906L34 159.099V159.874H35ZM35 161V162H36V161H35ZM33 161H32V162H33V161ZM33 159.874H34V159.099L33.2493 158.906L33 159.874ZM30.126 157L31.0944 156.751L30.9012 156H30.126V157ZM30.126 155V156H30.9012L31.0944 155.249L30.126 155ZM33 152.126L33.2493 153.094L34 152.901V152.126H33ZM33 2H34H33ZM32.2695 157V156H30.5348L31.4042 157.501L32.2695 157ZM34 158V159V159V158ZM35.7305 157L36.5958 157.501L37.4652 156H35.7305V157ZM33 154.27H34V152.535L32.4988 153.404L33 154.27ZM32.2695 155L31.4042 154.499L30.5348 156H32.2695V155ZM33 155V156H34V155H33ZM35 155H34V156H35V155ZM35.7305 155V156H37.4652L36.5958 154.499L35.7305 155ZM35 154.27L35.5012 153.404L34 152.535V154.27H35ZM35 313V312H33V313V314H35V313ZM33 313H34V311H33H32V313H33ZM33 311V312H35V311V310H33V311ZM35 311H34V313H35H36V311H35ZM35 309V308H33V309V310H35V309ZM33 309H34V307H33H32V309H33ZM33 307V308H35V307V306H33V307ZM35 307H34V309H35H36V307H35ZM35 305V304H33V305V306H35V305ZM33 305H34V303H33H32V305H33ZM33 303V304H35V303V302H33V303ZM35 303H34V305H35H36V303H35ZM35 301V300H33V301V302H35V301ZM33 301H34V299H33H32V301H33ZM33 299V300H35V299V298H33V299ZM35 299H34V301H35H36V299H35ZM35 297V296H33V297V298H35V297ZM33 297H34V295H33H32V297H33ZM33 295V296H35V295V294H33V295ZM35 295H34V297H35H36V295H35ZM35 293V292H33V293V294H35V293ZM33 293H34V291H33H32V293H33ZM33 291V292H35V291V290H33V291ZM35 291H34V293H35H36V291H35ZM35 289V288H33V289V290H35V289ZM33 289H34V287H33H32V289H33ZM33 287V288H35V287V286H33V287ZM35 287H34V289H35H36V287H35ZM35 285V284H33V285V286H35V285ZM33 285H34V283H33H32V285H33ZM33 283V284H35V283V282H33V283ZM35 283H34V285H35H36V283H35ZM35 281V280H33V281V282H35V281ZM33 281H34V279H33H32V281H33ZM33 279V280H35V279V278H33V279ZM35 279H34V281H35H36V279H35ZM35 277V276H33V277V278H35V277ZM33 277H34V275H33H32V277H33ZM33 275V276H35V275V274H33V275ZM35 275H34V277H35H36V275H35ZM35 273V272H33V273V274H35V273ZM33 273H34V271H33H32V273H33ZM33 271V272H35V271V270H33V271ZM35 271H34V273H35H36V271H35ZM35 269V268H33V269V270H35V269ZM33 269H34V267H33H32V269H33ZM33 267V268H35V267V266H33V267ZM35 267H34V269H35H36V267H35ZM35 265V264H33V265V266H35V265ZM33 265H34V263H33H32V265H33ZM33 263V264H35V263V262H33V263ZM35 263H34V265H35H36V263H35ZM35 261V260H33V261V262H35V261ZM33 261H34V259H33H32V261H33ZM33 259V260H35V259V258H33V259ZM35 259H34V261H35H36V259H35ZM35 257V256H33V257V258H35V257ZM33 257H34V255H33H32V257H33ZM33 255V256H35V255V254H33V255ZM35 255H34V257H35H36V255H35ZM35 253V252H33V253V254H35V253ZM33 253H34V251H33H32V253H33ZM33 251V252H35V251V250H33V251ZM35 251H34V253H35H36V251H35ZM35 249V248H33V249V250H35V249ZM33 249H34V247H33H32V249H33ZM33 247V248H35V247V246H33V247ZM35 247H34V249H35H36V247H35ZM35 245V244H33V245V246H35V245ZM33 245H34V243H33H32V245H33ZM33 243V244H35V243V242H33V243ZM35 243H34V245H35H36V243H35ZM35 241V240H33V241V242H35V241ZM33 241H34V239H33H32V241H33ZM33 239V240H35V239V238H33V239ZM35 239H34V241H35H36V239H35ZM35 237V236H33V237V238H35V237ZM33 237H34V235H33H32V237H33ZM33 235V236H35V235V234H33V235ZM35 235H34V237H35H36V235H35ZM35 233V232H33V233V234H35V233ZM33 233H34V231H33H32V233H33ZM33 231V232H35V231V230H33V231ZM35 231H34V233H35H36V231H35ZM35 229V228H33V229V230H35V229ZM33 229H34V227H33H32V229H33ZM33 227V228H35V227V226H33V227ZM35 227H34V229H35H36V227H35ZM35 225V224H33V225V226H35V225ZM33 225H34V223H33H32V225H33ZM33 223V224H35V223V222H33V223ZM35 223H34V225H35H36V223H35ZM35 221V220H33V221V222H35V221ZM33 221H34V219H33H32V221H33ZM33 219V220H35V219V218H33V219ZM35 219H34V221H35H36V219H35ZM35 217V216H33V217V218H35V217ZM33 217H34V215H33H32V217H33ZM33 215V216H35V215V214H33V215ZM35 215H34V217H35H36V215H35ZM35 213V212H33V213V214H35V213ZM33 213H34V211H33H32V213H33ZM33 211V212H35V211V210H33V211ZM35 211H34V213H35H36V211H35ZM35 209V208H33V209V210H35V209ZM33 209H34V207H33H32V209H33ZM33 207V208H35V207V206H33V207ZM35 207H34V209H35H36V207H35ZM35 205V204H33V205V206H35V205ZM33 205H34V203H33H32V205H33ZM33 203V204H35V203V202H33V203ZM35 203H34V205H35H36V203H35ZM35 201V200H33V201V202H35V201ZM33 201H34V199H33H32V201H33ZM33 199V200H35V199V198H33V199ZM35 199H34V201H35H36V199H35ZM35 197V196H33V197V198H35V197ZM33 197H34V195H33H32V197H33ZM33 195V196H35V195V194H33V195ZM35 195H34V197H35H36V195H35ZM35 193V192H33V193V194H35V193ZM33 193H34V191H33H32V193H33ZM33 191V192H35V191V190H33V191ZM35 191H34V193H35H36V191H35ZM35 189V188H33V189V190H35V189ZM33 189H34V187H33H32V189H33ZM33 187V188H35V187V186H33V187ZM35 187H34V189H35H36V187H35ZM35 185V184H33V185V186H35V185ZM33 185H34V183H33H32V185H33ZM33 183V184H35V183V182H33V183ZM35 183H34V185H35H36V183H35ZM35 181V180H33V181V182H35V181ZM33 181H34V179H33H32V181H33ZM33 179V180H35V179V178H33V179ZM35 179H34V181H35H36V179H35ZM35 177V176H33V177V178H35V177ZM33 177H34V175H33H32V177H33ZM33 175V176H35V175V174H33V175ZM35 175H34V177H35H36V175H35ZM35 173V172H33V173V174H35V173ZM33 173H34V171H33H32V173H33ZM33 171V172H35V171V170H33V171ZM35 171H34V173H35H36V171H35ZM35 169V168H33V169V170H35V169ZM33 169H34V167H33H32V169H33ZM33 167V168H35V167V166H33V167ZM35 167H34V169H35H36V167H35ZM35 165V164H33V165V166H35V165ZM33 165H34V163H33H32V165H33ZM33 163V164H35V163V162H33V163ZM35 163H34V165H35H36V163H35ZM34 1V2V2H35L36 2C36 0.895431 35.1046 0 34 0V1ZM35 2H34V152.126H35H36V2H35ZM35 152.126L34.7507 153.094C35.8035 153.365 36.6346 154.196 36.9056 155.249L37.874 155L38.8425 154.751C38.3899 152.992 37.0077 151.61 35.2493 151.158L35 152.126ZM37.874 155V156H66V155V154H37.874V155ZM66 155V156H67H68C68 154.895 67.1046 154 66 154V155ZM67 156H66V157V158C67.1046 158 68 157.105 68 156H67ZM66 157V156H37.874V157V158H66V157ZM37.874 157L36.9056 156.751C36.6346 157.804 35.8035 158.635 34.7507 158.906L35 159.874L35.2493 160.842C37.0077 160.39 38.3899 159.008 38.8425 157.249L37.874 157ZM35 159.874H34V161H35H36V159.874H35ZM35 161V160H33V161V162H35V161ZM33 161H34V159.874H33H32V161H33ZM33 159.874L33.2493 158.906C32.1965 158.635 31.3654 157.804 31.0944 156.751L30.126 157L29.1575 157.249C29.6101 159.008 30.9923 160.39 32.7507 160.842L33 159.874ZM30.126 157V156H2V157V158H30.126V157ZM2 157V156H1H0C0 157.105 0.89543 158 2 158V157ZM1 156H2V155V154C0.89543 154 0 154.895 0 156H1ZM2 155V156H30.126V155V154H2V155ZM30.126 155L31.0944 155.249C31.3654 154.196 32.1965 153.365 33.2493 153.094L33 152.126L32.7507 151.158C30.9923 151.61 29.6101 152.992 29.1575 154.751L30.126 155ZM33 152.126H34V2H33H32V152.126H33ZM33 2H34V2V1V0C32.8954 5.96046e-08 32 0.89543 32 2H33ZM32.2695 157L31.4042 157.501C31.9207 158.393 32.8872 159 34 159V158V157C33.6329 157 33.3102 156.802 33.1349 156.499L32.2695 157ZM34 158V159C35.1128 159 36.0793 158.393 36.5958 157.501L35.7305 157L34.8651 156.499C34.6898 156.802 34.3671 157 34 157V158ZM35.7305 157V156H32.2695V157V158H35.7305V157ZM33 154.27L32.4988 153.404C32.0448 153.667 31.6671 154.045 31.4042 154.499L32.2695 155L33.1349 155.501C33.2228 155.349 33.3493 155.223 33.5012 155.135L33 154.27ZM32.2695 155V156H33V155V154H32.2695V155ZM33 155H34V154.27H33H32V155H33ZM35 155V156H35.7305V155V154H35V155ZM35.7305 155L36.5958 154.499C36.3329 154.045 35.9552 153.667 35.5012 153.404L35 154.27L34.4988 155.135C34.6507 155.223 34.7772 155.349 34.8651 155.501L35.7305 155ZM35 154.27H34V155H35H36V154.27H35Z" fill="var(--border-silhouette-color)" mask="url(#hdg-beam-line-outline)"/>
</g></g>`}function jd(e){return k`<g transform="translate(239.02, 94.99)"><g id="Shape">
<mask id="cog-vector-outline" maskUnits="userSpaceOnUse" x="-0.991658" y="3.57628e-07" width="36" height="164" fill="black">
<rect fill="white" x="-0.991658" y="3.57628e-07" width="36" height="164"/>
<path d="M19.0083 163H15.0083V150.25H19.0083V163ZM19.0083 145.95H15.0083V124.45H19.0083V145.95ZM19.0083 120.15H15.0083V98.6504H19.0083V120.15ZM19.0083 94.3496H15.0083V72.8496H19.0083V94.3496ZM19.0083 68.5498H15.0083V47.0498H19.0083V68.5498ZM16.0747 1.62109C16.4119 0.792983 17.6048 0.792954 17.9419 1.62109L32.857 38.2803C33.5752 40.0456 31.5922 41.6925 29.9419 40.7012L19.0083 34.1904V42.75H15.0083V34.1904L4.07475 40.7012C2.4245 41.6926 0.441442 40.0456 1.15971 38.2803L16.0747 1.62109ZM7.14115 34.1924L17.0083 28.334L26.8755 34.1924L17.0083 9.94141L7.14115 34.1924Z"/>
</mask>
<path d="M19.0083 163H15.0083V150.25H19.0083V163ZM19.0083 145.95H15.0083V124.45H19.0083V145.95ZM19.0083 120.15H15.0083V98.6504H19.0083V120.15ZM19.0083 94.3496H15.0083V72.8496H19.0083V94.3496ZM19.0083 68.5498H15.0083V47.0498H19.0083V68.5498ZM16.0747 1.62109C16.4119 0.792983 17.6048 0.792954 17.9419 1.62109L32.857 38.2803C33.5752 40.0456 31.5922 41.6925 29.9419 40.7012L19.0083 34.1904V42.75H15.0083V34.1904L4.07475 40.7012C2.4245 41.6926 0.441442 40.0456 1.15971 38.2803L16.0747 1.62109ZM7.14115 34.1924L17.0083 28.334L26.8755 34.1924L17.0083 9.94141L7.14115 34.1924Z" fill=${e}/>
<path d="M19.0083 163V164H20.0083V163H19.0083ZM15.0083 163H14.0083V164H15.0083V163ZM15.0083 150.25V149.25H14.0083V150.25H15.0083ZM19.0083 150.25H20.0083V149.25H19.0083V150.25ZM19.0083 145.95V146.95H20.0083V145.95H19.0083ZM15.0083 145.95H14.0083V146.95H15.0083V145.95ZM15.0083 124.45V123.45H14.0083V124.45H15.0083ZM19.0083 124.45H20.0083V123.45H19.0083V124.45ZM19.0083 120.15V121.15H20.0083V120.15H19.0083ZM15.0083 120.15H14.0083V121.15H15.0083V120.15ZM15.0083 98.6504V97.6504H14.0083V98.6504H15.0083ZM19.0083 98.6504H20.0083V97.6504H19.0083V98.6504ZM19.0083 94.3496V95.3496H20.0083V94.3496H19.0083ZM15.0083 94.3496H14.0083V95.3496H15.0083V94.3496ZM15.0083 72.8496V71.8496H14.0083V72.8496H15.0083ZM19.0083 72.8496H20.0083V71.8496H19.0083V72.8496ZM19.0083 68.5498V69.5498H20.0083V68.5498H19.0083ZM15.0083 68.5498H14.0083V69.5498H15.0083V68.5498ZM15.0083 47.0498V46.0498H14.0083V47.0498H15.0083ZM19.0083 47.0498H20.0083V46.0498H19.0083V47.0498ZM16.0747 1.62109L15.1486 1.24404L15.1485 1.24423L16.0747 1.62109ZM17.9419 1.62109L18.8682 1.24423L18.8681 1.24408L17.9419 1.62109ZM32.857 38.2803L31.9307 38.6571L31.9307 38.6571L32.857 38.2803ZM29.9419 40.7012L30.4569 39.8439L30.4536 39.842L29.9419 40.7012ZM19.0083 34.1904L19.52 33.3312L18.0083 32.4311V34.1904H19.0083ZM19.0083 42.75V43.75H20.0083V42.75H19.0083ZM15.0083 42.75H14.0083V43.75H15.0083V42.75ZM15.0083 34.1904H16.0083V32.4311L14.4967 33.3312L15.0083 34.1904ZM4.07475 40.7012L3.56311 39.842L3.55977 39.844L4.07475 40.7012ZM1.15971 38.2803L2.08598 38.6571L2.08598 38.6571L1.15971 38.2803ZM7.14115 34.1924L6.21489 33.8155L5.09376 36.5709L7.65168 35.0522L7.14115 34.1924ZM17.0083 28.334L17.5189 27.4741L17.0083 27.171L16.4978 27.4741L17.0083 28.334ZM26.8755 34.1924L26.365 35.0522L28.9229 36.5709L27.8018 33.8155L26.8755 34.1924ZM17.0083 9.94141L17.9346 9.56453L17.0083 7.28802L16.0821 9.56453L17.0083 9.94141ZM19.0083 163V162H15.0083V163V164H19.0083V163ZM15.0083 163H16.0083V150.25H15.0083H14.0083V163H15.0083ZM15.0083 150.25V151.25H19.0083V150.25V149.25H15.0083V150.25ZM19.0083 150.25H18.0083V163H19.0083H20.0083V150.25H19.0083ZM19.0083 145.95V144.95H15.0083V145.95V146.95H19.0083V145.95ZM15.0083 145.95H16.0083V124.45H15.0083H14.0083V145.95H15.0083ZM15.0083 124.45V125.45H19.0083V124.45V123.45H15.0083V124.45ZM19.0083 124.45H18.0083V145.95H19.0083H20.0083V124.45H19.0083ZM19.0083 120.15V119.15H15.0083V120.15V121.15H19.0083V120.15ZM15.0083 120.15H16.0083V98.6504H15.0083H14.0083V120.15H15.0083ZM15.0083 98.6504V99.6504H19.0083V98.6504V97.6504H15.0083V98.6504ZM19.0083 98.6504H18.0083V120.15H19.0083H20.0083V98.6504H19.0083ZM19.0083 94.3496V93.3496H15.0083V94.3496V95.3496H19.0083V94.3496ZM15.0083 94.3496H16.0083V72.8496H15.0083H14.0083V94.3496H15.0083ZM15.0083 72.8496V73.8496H19.0083V72.8496V71.8496H15.0083V72.8496ZM19.0083 72.8496H18.0083V94.3496H19.0083H20.0083V72.8496H19.0083ZM19.0083 68.5498V67.5498H15.0083V68.5498V69.5498H19.0083V68.5498ZM15.0083 68.5498H16.0083V47.0498H15.0083H14.0083V68.5498H15.0083ZM15.0083 47.0498V48.0498H19.0083V47.0498V46.0498H15.0083V47.0498ZM19.0083 47.0498H18.0083V68.5498H19.0083H20.0083V47.0498H19.0083ZM16.0747 1.62109L17.0009 1.99815C17.0025 1.9942 17.0036 1.99245 17.0037 1.99233C17.0037 1.99221 17.0032 1.99304 17.0021 1.99445C16.9994 1.9976 16.9963 2.00017 16.9939 2.00167C16.9918 2.00296 16.9919 2.0025 16.9948 2.00168C16.9979 2.00082 17.0026 2 17.0084 2C17.0141 2 17.0188 2.00082 17.0219 2.00168C17.0248 2.00249 17.0249 2.00295 17.0228 2.00166C17.0204 2.00015 17.0173 1.99758 17.0146 1.99442C17.0134 1.99301 17.0129 1.99217 17.013 1.9923C17.0131 1.99241 17.0141 1.99416 17.0157 1.99811L17.9419 1.62109L18.8681 1.24408C18.1929 -0.414789 15.8238 -0.414582 15.1486 1.24404L16.0747 1.62109ZM17.9419 1.62109L17.0157 1.99795L31.9307 38.6571L32.857 38.2803L33.7832 37.9034L18.8682 1.24423L17.9419 1.62109ZM32.857 38.2803L31.9307 38.6571C32.2629 39.4735 31.3379 40.3732 30.4569 39.8439L29.9419 40.7012L29.427 41.5584C31.8464 43.0118 34.8876 40.6177 33.7832 37.9034L32.857 38.2803ZM29.9419 40.7012L30.4536 39.842L19.52 33.3312L19.0083 34.1904L18.4967 35.0496L29.4303 41.5604L29.9419 40.7012ZM19.0083 34.1904H18.0083V42.75H19.0083H20.0083V34.1904H19.0083ZM19.0083 42.75V41.75H15.0083V42.75V43.75H19.0083V42.75ZM15.0083 42.75H16.0083V34.1904H15.0083H14.0083V42.75H15.0083ZM15.0083 34.1904L14.4967 33.3312L3.56311 39.842L4.07475 40.7012L4.58639 41.5604L15.52 35.0496L15.0083 34.1904ZM4.07475 40.7012L3.55977 39.844C2.67881 40.3732 1.75376 39.4737 2.08598 38.6571L1.15971 38.2803L0.233442 37.9034C-0.870876 40.6176 2.17019 43.012 4.58973 41.5584L4.07475 40.7012ZM1.15971 38.2803L2.08598 38.6571L17.001 1.99795L16.0747 1.62109L15.1485 1.24423L0.233439 37.9034L1.15971 38.2803ZM7.14115 34.1924L7.65168 35.0522L17.5189 29.1938L17.0083 28.334L16.4978 27.4741L6.63063 33.3325L7.14115 34.1924ZM17.0083 28.334L16.4978 29.1938L26.365 35.0522L26.8755 34.1924L27.3861 33.3325L17.5189 27.4741L17.0083 28.334ZM26.8755 34.1924L27.8018 33.8155L17.9346 9.56453L17.0083 9.94141L16.0821 10.3183L25.9493 34.5693L26.8755 34.1924ZM17.0083 9.94141L16.0821 9.56453L6.21489 33.8155L7.14115 34.1924L8.06742 34.5693L17.9346 10.3183L17.0083 9.94141Z" fill="var(--border-silhouette-color)" mask="url(#cog-vector-outline)"/>
</g></g>`}function Md(e){return k`<g transform="translate(245.45, 97.01)"><g id="Shape">
<mask id="cog-velocity-vector-outline" maskUnits="userSpaceOnUse" x="-0.513564" y="-4.86374e-05" width="22" height="162" fill="black">
<rect fill="white" x="-0.513564" y="-4.86374e-05" width="22" height="162"/>
<path d="M12.5489 161H8.54894V149.25H12.5489V161ZM12.5489 145.35H8.54894V125.85H12.5489V145.35ZM12.5489 121.95H8.54894V102.45H12.5489V121.95ZM12.5489 98.5498H8.54894V79.0498H12.5489V98.5498ZM12.5489 75.1503H8.54894V55.6503H12.5489V75.1503ZM12.5489 51.75H8.54894V40H12.5489V51.75ZM9.61534 19.621C9.95247 18.7929 11.1454 18.7929 11.4825 19.621L19.6114 39.6015H15.2931L10.5489 27.9414L5.80479 39.6015H1.48644L9.61534 19.621ZM9.61534 1.62105C9.9525 0.793007 11.1454 0.792963 11.4825 1.62105L19.6114 21.6015H15.2931L10.5489 9.94136L5.80479 21.6015H1.48644L9.61534 1.62105Z"/>
</mask>
<path d="M12.5489 161H8.54894V149.25H12.5489V161ZM12.5489 145.35H8.54894V125.85H12.5489V145.35ZM12.5489 121.95H8.54894V102.45H12.5489V121.95ZM12.5489 98.5498H8.54894V79.0498H12.5489V98.5498ZM12.5489 75.1503H8.54894V55.6503H12.5489V75.1503ZM12.5489 51.75H8.54894V40H12.5489V51.75ZM9.61534 19.621C9.95247 18.7929 11.1454 18.7929 11.4825 19.621L19.6114 39.6015H15.2931L10.5489 27.9414L5.80479 39.6015H1.48644L9.61534 19.621ZM9.61534 1.62105C9.9525 0.793007 11.1454 0.792963 11.4825 1.62105L19.6114 21.6015H15.2931L10.5489 9.94136L5.80479 21.6015H1.48644L9.61534 1.62105Z" fill=${e}/>
<path d="M12.5489 161V162H13.5489V161H12.5489ZM8.54894 161H7.54894V162H8.54894V161ZM8.54894 149.25V148.25H7.54894V149.25H8.54894ZM12.5489 149.25H13.5489V148.25H12.5489V149.25ZM12.5489 145.35V146.35H13.5489V145.35H12.5489ZM8.54894 145.35H7.54894V146.35H8.54894V145.35ZM8.54894 125.85V124.85H7.54894V125.85H8.54894ZM12.5489 125.85H13.5489V124.85H12.5489V125.85ZM12.5489 121.95V122.95H13.5489V121.95H12.5489ZM8.54894 121.95H7.54894V122.95H8.54894V121.95ZM8.54894 102.45V101.45H7.54894V102.45H8.54894ZM12.5489 102.45H13.5489V101.45H12.5489V102.45ZM12.5489 98.5498V99.5498H13.5489V98.5498H12.5489ZM8.54894 98.5498H7.54894V99.5498H8.54894V98.5498ZM8.54894 79.0498V78.0498H7.54894V79.0498H8.54894ZM12.5489 79.0498H13.5489V78.0498H12.5489V79.0498ZM12.5489 75.1503V76.1503H13.5489V75.1503H12.5489ZM8.54894 75.1503H7.54894V76.1503H8.54894V75.1503ZM8.54894 55.6503V54.6503H7.54894V55.6503H8.54894ZM12.5489 55.6503H13.5489V54.6503H12.5489V55.6503ZM12.5489 51.75V52.75H13.5489V51.75H12.5489ZM8.54894 51.75H7.54894V52.75H8.54894V51.75ZM8.54894 40V39H7.54894V40H8.54894ZM12.5489 40H13.5489V39H12.5489V40ZM9.61534 19.621L8.68915 19.244L8.68907 19.2442L9.61534 19.621ZM11.4825 19.621L12.4088 19.2442L12.4087 19.244L11.4825 19.621ZM19.6114 39.6015V40.6015H21.0979L20.5377 39.2247L19.6114 39.6015ZM15.2931 39.6015L14.3668 39.9784L14.6203 40.6015H15.2931V39.6015ZM10.5489 27.9414L11.4752 27.5645L10.5489 25.2879L9.62267 27.5645L10.5489 27.9414ZM5.80479 39.6015V40.6015H6.47753L6.73106 39.9784L5.80479 39.6015ZM1.48644 39.6015L0.56016 39.2247L0 40.6015H1.48644V39.6015ZM9.61534 1.62105L8.68917 1.24393L8.68907 1.2442L9.61534 1.62105ZM11.4825 1.62105L12.4088 1.2442L12.4087 1.24399L11.4825 1.62105ZM19.6114 21.6015V22.6015H21.0979L20.5377 21.2247L19.6114 21.6015ZM15.2931 21.6015L14.3668 21.9784L14.6203 22.6015H15.2931V21.6015ZM10.5489 9.94136L11.4752 9.56449L10.5489 7.28791L9.62267 9.56449L10.5489 9.94136ZM5.80479 21.6015V22.6015H6.47753L6.73106 21.9784L5.80479 21.6015ZM1.48644 21.6015L0.56016 21.2247L0 22.6015H1.48644V21.6015ZM12.5489 161V160H8.54894V161V162H12.5489V161ZM8.54894 161H9.54894V149.25H8.54894H7.54894V161H8.54894ZM8.54894 149.25V150.25H12.5489V149.25V148.25H8.54894V149.25ZM12.5489 149.25H11.5489V161H12.5489H13.5489V149.25H12.5489ZM12.5489 145.35V144.35H8.54894V145.35V146.35H12.5489V145.35ZM8.54894 145.35H9.54894V125.85H8.54894H7.54894V145.35H8.54894ZM8.54894 125.85V126.85H12.5489V125.85V124.85H8.54894V125.85ZM12.5489 125.85H11.5489V145.35H12.5489H13.5489V125.85H12.5489ZM12.5489 121.95V120.95H8.54894V121.95V122.95H12.5489V121.95ZM8.54894 121.95H9.54894V102.45H8.54894H7.54894V121.95H8.54894ZM8.54894 102.45V103.45H12.5489V102.45V101.45H8.54894V102.45ZM12.5489 102.45H11.5489V121.95H12.5489H13.5489V102.45H12.5489ZM12.5489 98.5498V97.5498H8.54894V98.5498V99.5498H12.5489V98.5498ZM8.54894 98.5498H9.54894V79.0498H8.54894H7.54894V98.5498H8.54894ZM8.54894 79.0498V80.0498H12.5489V79.0498V78.0498H8.54894V79.0498ZM12.5489 79.0498H11.5489V98.5498H12.5489H13.5489V79.0498H12.5489ZM12.5489 75.1503V74.1503H8.54894V75.1503V76.1503H12.5489V75.1503ZM8.54894 75.1503H9.54894V55.6503H8.54894H7.54894V75.1503H8.54894ZM8.54894 55.6503V56.6503H12.5489V55.6503V54.6503H8.54894V55.6503ZM12.5489 55.6503H11.5489V75.1503H12.5489H13.5489V55.6503H12.5489ZM12.5489 51.75V50.75H8.54894V51.75V52.75H12.5489V51.75ZM8.54894 51.75H9.54894V40H8.54894H7.54894V51.75H8.54894ZM8.54894 40V41H12.5489V40V39H8.54894V40ZM12.5489 40H11.5489V51.75H12.5489H13.5489V40H12.5489ZM9.61534 19.621L10.5415 19.9981C10.5431 19.9941 10.5442 19.9924 10.5443 19.9923C10.5443 19.9921 10.5438 19.993 10.5427 19.9944C10.54 19.9975 10.5369 20.0001 10.5345 20.0016C10.5324 20.0029 10.5325 20.0024 10.5354 20.0016C10.5385 20.0008 10.5432 19.9999 10.549 19.9999C10.5547 19.9999 10.5594 20.0008 10.5625 20.0016C10.5654 20.0024 10.5655 20.0029 10.5634 20.0016C10.561 20.0001 10.5579 19.9975 10.5552 19.9944C10.554 19.9929 10.5535 19.9921 10.5536 19.9922C10.5537 19.9923 10.5547 19.9941 10.5563 19.998L11.4825 19.621L12.4087 19.244C11.7335 17.5851 9.36437 17.5854 8.68915 19.244L9.61534 19.621ZM11.4825 19.621L10.5563 19.9979L18.6852 39.9784L19.6114 39.6015L20.5377 39.2247L12.4088 19.2442L11.4825 19.621ZM19.6114 39.6015V38.6015H15.2931V39.6015V40.6015H19.6114V39.6015ZM15.2931 39.6015L16.2193 39.2246L11.4752 27.5645L10.5489 27.9414L9.62267 28.3182L14.3668 39.9784L15.2931 39.6015ZM10.5489 27.9414L9.62267 27.5645L4.87853 39.2246L5.80479 39.6015L6.73106 39.9784L11.4752 28.3182L10.5489 27.9414ZM5.80479 39.6015V38.6015H1.48644V39.6015V40.6015H5.80479V39.6015ZM1.48644 39.6015L2.41271 39.9784L10.5416 19.9979L9.61534 19.621L8.68907 19.2442L0.56016 39.2247L1.48644 39.6015ZM9.61534 1.62105L10.5415 1.99816C10.5431 1.99421 10.5442 1.99246 10.5442 1.99235C10.5443 1.99222 10.5438 1.99306 10.5426 1.99447C10.54 1.99762 10.5368 2.00018 10.5345 2.00168C10.5324 2.00296 10.5325 2.0025 10.5354 2.00168C10.5385 2.00082 10.5432 2 10.549 2C10.5547 2 10.5595 2.00082 10.5625 2.00168C10.5654 2.0025 10.5655 2.00295 10.5634 2.00166C10.561 2.00015 10.5579 1.99758 10.5552 1.99442C10.554 1.99301 10.5535 1.99217 10.5536 1.99229C10.5537 1.9924 10.5547 1.99415 10.5563 1.9981L11.4825 1.62105L12.4087 1.24399C11.7334 -0.414815 9.36445 -0.414494 8.68917 1.24393L9.61534 1.62105ZM11.4825 1.62105L10.5563 1.99789L18.6852 21.9784L19.6114 21.6015L20.5377 21.2247L12.4088 1.2442L11.4825 1.62105ZM19.6114 21.6015V20.6015H15.2931V21.6015V22.6015H19.6114V21.6015ZM15.2931 21.6015L16.2193 21.2246L11.4752 9.56449L10.5489 9.94136L9.62267 10.3182L14.3668 21.9784L15.2931 21.6015ZM10.5489 9.94136L9.62267 9.56449L4.87853 21.2246L5.80479 21.6015L6.73106 21.9784L11.4752 10.3182L10.5489 9.94136ZM5.80479 21.6015V20.6015H1.48644V21.6015V22.6015H5.80479V21.6015ZM1.48644 21.6015L2.41271 21.9784L10.5416 1.99789L9.61534 1.62105L8.68907 1.2442L0.56016 21.2247L1.48644 21.6015Z" fill="var(--border-silhouette-color)" mask="url(#cog-velocity-vector-outline)"/>
</g></g>`}var Nd=function(e){return e.arrowHead=`arrowHead`,e.needle=`needle`,e.vector=`vector`,e.beamLine=`beamLine`,e}({}),Pd=function(e){return e.arrowHead=`arrowHead`,e.needle=`needle`,e.vector=`vector`,e.velocityVector=`velocityVector`,e}({});function Fd(e){return e===W.enhanced?`var(--instrument-enhanced-secondary-color)`:`var(--instrument-regular-secondary-color)`}function Id(e,t,n){return k`
      <g transform="rotate(${e}) translate(-256, ${-256-n})">

<path d="M254.654 100.32C255.219 99.1903 256.906 99.2277 257.396 100.433L272.312 137.092L272.388 137.301C273.067 139.455 270.647 141.314 268.676 140.13V140.129L256 132.582L243.323 140.129L243.324 140.13C241.289 141.352 238.777 139.332 239.688 137.092L254.604 100.433L254.654 100.32Z"
 fill=${t} stroke="var(--border-silhouette-color)" stroke-width="1" vector-effect="non-scaling-stroke"/>
      </g>
    `}function Ld(e,t,n){return k`
      <g transform="rotate(${e}) translate(-256, ${-256-n})">
<mask id="path-1-outside-1_133_32856" maskUnits="userSpaceOnUse" x="238" y="99" width="36" height="42" fill="black">
<rect fill="white" x="238" y="99" width="36" height="42"/>
<path fill-rule="evenodd" clip-rule="evenodd" vector-effect="non-scaling-stroke" d="M256 127.334L265.867 133.192L256 108.941L246.133 133.192L256 127.334ZM255.067 100.621C255.404 99.7929 256.596 99.7929 256.933 100.621L271.849 137.28C272.567 139.046 270.584 140.693 268.933 139.701L256 132L243.067 139.701C241.416 140.693 239.433 139.046 240.151 137.28L255.067 100.621Z"/>
</mask>
<path fill-rule="evenodd" clip-rule="evenodd" d="M256 127.334L265.867 133.192L256 108.941L246.133 133.192L256 127.334ZM255.067 100.621C255.404 99.7929 256.596 99.7929 256.933 100.621L271.849 137.28C272.567 139.046 270.584 140.693 268.933 139.701L256 132L243.067 139.701C241.416 140.693 239.433 139.046 240.151 137.28L255.067 100.621Z"
   fill=${t} />
<path d="M256 127.334L256.511 126.474L256 126.171L255.489 126.474L256 127.334ZM265.867 133.192L265.357 134.052L267.914 135.571L266.793 132.816L265.867 133.192ZM256 108.941L256.926 108.564L256 106.288L255.074 108.564L256 108.941ZM246.133 133.192L245.207 132.816L244.086 135.571L246.643 134.052L246.133 133.192ZM255.067 100.621L254.14 100.244L255.067 100.621ZM256.933 100.621L257.86 100.244L256.933 100.621ZM271.849 137.28L270.922 137.657L271.849 137.28ZM268.933 139.701L269.448 138.844L269.445 138.842L268.933 139.701ZM256 132L256.512 131.141L256 130.836L255.488 131.141L256 132ZM243.067 139.701L242.555 138.842L242.552 138.844L243.067 139.701ZM240.151 137.28L241.078 137.657L240.151 137.28ZM255.489 128.193L265.357 134.052L266.378 132.333L256.511 126.474L255.489 128.193ZM266.793 132.816L256.926 108.564L255.074 109.318L264.941 133.569L266.793 132.816ZM255.074 108.564L245.207 132.816L247.059 133.569L256.926 109.318L255.074 108.564ZM246.643 134.052L256.511 128.193L255.489 126.474L245.622 132.333L246.643 134.052ZM255.993 100.998C255.994 100.994 255.996 100.992 255.996 100.992C255.996 100.992 255.995 100.993 255.994 100.994C255.991 100.997 255.988 101 255.986 101.002C255.984 101.003 255.984 101.002 255.987 101.002C255.99 101.001 255.994 101 256 101C256.006 101 256.01 101.001 256.013 101.002C256.016 101.002 256.016 101.003 256.014 101.002C256.012 101 256.009 100.997 256.006 100.994C256.005 100.993 256.004 100.992 256.004 100.992C256.004 100.992 256.006 100.994 256.007 100.998L257.86 100.244C257.185 98.5852 254.815 98.5852 254.14 100.244L255.993 100.998ZM256.007 100.998L270.922 137.657L272.775 136.903L257.86 100.244L256.007 100.998ZM270.922 137.657C271.255 138.473 270.33 139.373 269.448 138.844L268.418 140.558C270.838 142.012 273.879 139.618 272.775 136.903L270.922 137.657ZM269.445 138.842L256.512 131.141L255.488 132.859L268.422 140.56L269.445 138.842ZM255.488 131.141L242.555 138.842L243.578 140.56L256.512 132.859L255.488 131.141ZM242.552 138.844C241.67 139.373 240.745 138.473 241.078 137.657L239.225 136.903C238.121 139.618 241.162 142.012 243.582 140.558L242.552 138.844ZM241.078 137.657L255.993 100.998L254.14 100.244L239.225 136.903L241.078 137.657Z"
fill="var(--border-silhouette-color)" vector-effect="non-scaling-stroke" mask="url(#path-1-outside-1_133_32856)"/>

      </g>
    `}function Rd(e,t){return k`
    <g transform="translate(-256, -256) rotate(${e}) scale(0.98)" transform-origin="256 256">
      <mask id="path-1-outside-1_18306_91613" maskUnits="userSpaceOnUse" x="238" y="94.9999" width="36" height="318" fill="black">
        <rect fill="white" x="238" y="94.9999" width="36" height="318"/>
        <path fill-rule="evenodd" clip-rule="evenodd" d="M256.934 96.621C256.596 95.7928 255.403 95.7929 255.066 96.621L240.151 133.28C239.433 135.046 241.416 136.692 243.066 135.701L252 130.381V249.072C249.609 250.455 248 253.039 248 256C248 259.728 250.549 262.86 254 263.748V410C254 411.104 254.895 412 256 412C257.104 412 258 411.104 258 410V263.747C261.45 262.859 264 259.727 264 256C264 253.039 262.391 250.456 260 249.072V130.381L268.934 135.701C270.584 136.692 272.567 135.045 271.849 133.28L256.934 96.621ZM256 260C258.209 260 260 258.209 260 256C260 253.791 258.209 252 256 252C253.791 252 252 253.791 252 256C252 258.209 253.791 260 256 260Z"/>
      </mask>
      <path fill-rule="evenodd" clip-rule="evenodd" d="M256.934 96.621C256.596 95.7928 255.403 95.7929 255.066 96.621L240.151 133.28C239.433 135.046 241.416 136.692 243.066 135.701L252 130.381V249.072C249.609 250.455 248 253.039 248 256C248 259.728 250.549 262.86 254 263.748V410C254 411.104 254.895 412 256 412C257.104 412 258 411.104 258 410V263.747C261.45 262.859 264 259.727 264 256C264 253.039 262.391 250.456 260 249.072V130.381L268.934 135.701C270.584 136.692 272.567 135.045 271.849 133.28L256.934 96.621ZM256 260C258.209 260 260 258.209 260 256C260 253.791 258.209 252 256 252C253.791 252 252 253.791 252 256C252 258.209 253.791 260 256 260Z" fill=${t}/>
      <path d="M255.066 96.621L254.14 96.2439L254.14 96.2441L255.066 96.621ZM256.934 96.621L257.86 96.2441L257.86 96.244L256.934 96.621ZM240.151 133.28L241.078 133.657L241.078 133.657L240.151 133.28ZM243.066 135.701L242.555 134.842L242.551 134.844L243.066 135.701ZM252 130.381H253V128.621L251.488 129.522L252 130.381ZM252 249.072L252.501 249.938L253 249.649V249.072H252ZM248 256L247 256V256H248ZM254 263.748H255V262.973L254.249 262.779L254 263.748ZM256 412V413H256L256 412ZM258 263.747L257.751 262.779L257 262.972V263.747H258ZM264 256H265V256L264 256ZM260 249.072H259V249.649L259.499 249.938L260 249.072ZM260 130.381L260.512 129.522L259 128.621V130.381H260ZM268.934 135.701L269.448 134.844L269.445 134.842L268.934 135.701ZM271.849 133.28L270.922 133.657L270.922 133.657L271.849 133.28ZM255.066 96.621L255.993 96.998C255.994 96.9941 255.995 96.9923 255.995 96.9922C255.995 96.9921 255.995 96.9929 255.994 96.9943C255.991 96.9975 255.988 97 255.985 97.0015C255.983 97.0028 255.983 97.0024 255.986 97.0016C255.989 97.0007 255.994 96.9999 256 96.9999C256.006 96.9999 256.01 97.0007 256.014 97.0016C256.016 97.0024 256.016 97.0028 256.014 97.0015C256.012 97 256.009 96.9975 256.006 96.9943C256.005 96.9929 256.005 96.9921 256.005 96.9922C256.005 96.9923 256.006 96.994 256.007 96.998L256.934 96.621L257.86 96.244C257.184 94.5851 254.815 94.5853 254.14 96.2439L255.066 96.621ZM240.151 133.28L241.078 133.657L255.993 96.9978L255.066 96.621L254.14 96.2441L239.225 132.903L240.151 133.28ZM243.066 135.701L242.551 134.844C241.67 135.373 240.745 134.474 241.078 133.657L240.151 133.28L239.225 132.903C238.121 135.617 241.162 138.012 243.581 136.558L243.066 135.701ZM252 130.381L251.488 129.522L242.555 134.842L243.066 135.701L243.578 136.56L252.512 131.24L252 130.381ZM252 249.072H253V130.381H252H251V249.072H252ZM248 256L249 256C249 253.411 250.406 251.15 252.501 249.938L252 249.072L251.499 248.207C248.812 249.761 247 252.667 247 256L248 256ZM254 263.748L254.249 262.779C251.23 262.002 249 259.26 249 256H248H247C247 260.195 249.869 263.717 253.751 264.716L254 263.748ZM254 410H255V263.748H254H253V410H254ZM256 412V411C255.448 411 255 410.552 255 410H254H253C253 411.657 254.343 413 256 413V412ZM258 410H257C257 410.552 256.552 411 256 411L256 412L256 413C257.657 413 259 411.657 259 410H258ZM258 263.747H257V410H258H259V263.747H258ZM264 256H263C263 259.26 260.77 262.001 257.751 262.779L258 263.747L258.249 264.715C262.13 263.716 265 260.195 265 256H264ZM260 249.072L259.499 249.938C261.594 251.15 263 253.411 263 256L264 256L265 256C265 252.667 263.187 249.761 260.501 248.207L260 249.072ZM260 130.381H259V249.072H260H261V130.381H260ZM268.934 135.701L269.445 134.842L260.512 129.522L260 130.381L259.488 131.24L268.422 136.56L268.934 135.701ZM271.849 133.28L270.922 133.657C271.254 134.473 270.33 135.373 269.448 134.844L268.934 135.701L268.419 136.558C270.838 138.012 273.879 135.618 272.775 132.903L271.849 133.28ZM256.934 96.621L256.007 96.9978L270.922 133.657L271.849 133.28L272.775 132.903L257.86 96.2441L256.934 96.621ZM260 256H259C259 257.657 257.657 259 256 259V260V261C258.761 261 261 258.761 261 256H260ZM256 252V253C257.657 253 259 254.343 259 256H260H261C261 253.239 258.761 251 256 251V252ZM252 256H253C253 254.343 254.343 253 256 253V252V251C253.239 251 251 253.239 251 256H252ZM256 260V259C254.343 259 253 257.657 253 256H252H251C251 258.761 253.239 261 256 261V260Z" fill="var(--border-silhouette-color)" mask="url(#path-1-outside-1_18306_91613)"/>
    </g>
    `}function zd(e,t){return k`
      <g transform="translate(-256, -256) rotate(${e}) scale(0.98)" transform-origin="256 256">
<mask id="path-1-outside-1_18306_91642" maskUnits="userSpaceOnUse" x="238" y="94.9999" width="36" height="170" fill="black">
<rect fill="white" x="238" y="94.9999" width="36" height="170"/>
<path d="M255.066 96.621C255.404 95.7929 256.596 95.7928 256.934 96.621L271.849 133.28C272.567 135.046 270.584 136.692 268.934 135.701L258 129.19V248.252C261.45 249.14 264 252.272 264 256C264 260.418 260.418 264 256 264C251.582 264 248 260.418 248 256C248 252.272 250.55 249.14 254 248.252V129.19L243.066 135.701C241.416 136.692 239.433 135.046 240.151 133.28L255.066 96.621ZM256 252C253.791 252 252 253.791 252 256C252 258.209 253.791 260 256 260C258.209 260 260 258.209 260 256C260 253.791 258.209 252 256 252ZM246.133 129.192L256 123.334L265.867 129.192L256 104.941L246.133 129.192Z"/>
</mask>
<path d="M255.066 96.621C255.404 95.7929 256.596 95.7928 256.934 96.621L271.849 133.28C272.567 135.046 270.584 136.692 268.934 135.701L258 129.19V248.252C261.45 249.14 264 252.272 264 256C264 260.418 260.418 264 256 264C251.582 264 248 260.418 248 256C248 252.272 250.55 249.14 254 248.252V129.19L243.066 135.701C241.416 136.692 239.433 135.046 240.151 133.28L255.066 96.621ZM256 252C253.791 252 252 253.791 252 256C252 258.209 253.791 260 256 260C258.209 260 260 258.209 260 256C260 253.791 258.209 252 256 252ZM246.133 129.192L256 123.334L265.867 129.192L256 104.941L246.133 129.192Z" fill="${t}"/>
<path d="M255.066 96.621L254.14 96.2439L254.14 96.2441L255.066 96.621ZM256.934 96.621L257.86 96.2441L257.86 96.244L256.934 96.621ZM271.849 133.28L270.922 133.657L270.922 133.657L271.849 133.28ZM268.934 135.701L269.449 134.844L269.445 134.842L268.934 135.701ZM258 129.19L258.512 128.331L257 127.431V129.19H258ZM258 248.252H257V249.027L257.751 249.22L258 248.252ZM264 256H265V256L264 256ZM256 264V265H256L256 264ZM248 256L247 256V256H248ZM254 248.252L254.249 249.22L255 249.027V248.252H254ZM254 129.19H255V127.431L253.488 128.331L254 129.19ZM243.066 135.701L242.555 134.842L242.551 134.844L243.066 135.701ZM240.151 133.28L241.078 133.657L241.078 133.657L240.151 133.28ZM256 252L256 251H256V252ZM252 256L251 256V256H252ZM256 260V261H256L256 260ZM260 256H261V256L260 256ZM246.133 129.192L245.207 128.815L244.085 131.571L246.643 130.052L246.133 129.192ZM256 123.334L256.511 122.474L256 122.171L255.489 122.474L256 123.334ZM265.867 129.192L265.357 130.052L267.915 131.571L266.793 128.815L265.867 129.192ZM256 104.941L256.926 104.564L256 102.288L255.074 104.564L256 104.941ZM255.066 96.621L255.993 96.998C255.994 96.9941 255.995 96.9923 255.995 96.9922C255.995 96.9921 255.995 96.9929 255.994 96.9943C255.991 96.9975 255.988 97.0001 255.986 97.0016C255.983 97.0028 255.984 97.0024 255.986 97.0016C255.99 97.0007 255.994 96.9999 256 96.9999C256.006 96.9999 256.01 97.0007 256.014 97.0016C256.016 97.0024 256.017 97.0028 256.014 97.0015C256.012 97 256.009 96.9975 256.006 96.9943C256.005 96.9929 256.005 96.9921 256.005 96.9922C256.005 96.9923 256.006 96.9941 256.007 96.998L256.934 96.621L257.86 96.244C257.185 94.5851 254.815 94.5853 254.14 96.2439L255.066 96.621ZM256.934 96.621L256.007 96.9978L270.922 133.657L271.849 133.28L272.775 132.903L257.86 96.2441L256.934 96.621ZM271.849 133.28L270.922 133.657C271.255 134.473 270.33 135.373 269.449 134.844L268.934 135.701L268.419 136.558C270.838 138.012 273.879 135.618 272.775 132.903L271.849 133.28ZM268.934 135.701L269.445 134.842L258.512 128.331L258 129.19L257.488 130.05L268.422 136.56L268.934 135.701ZM258 129.19H257V248.252H258H259V129.19H258ZM258 248.252L257.751 249.22C260.77 249.997 263 252.74 263 256L264 256L265 256C265 251.805 262.131 248.283 258.249 247.283L258 248.252ZM264 256H263C263 259.866 259.866 263 256 263L256 264L256 265C260.97 265 265 260.97 265 256H264ZM256 264V263C252.134 263 249 259.866 249 256H248H247C247 260.97 251.029 265 256 265V264ZM248 256L249 256C249 252.74 251.23 249.997 254.249 249.22L254 248.252L253.751 247.283C249.869 248.282 247 251.805 247 256L248 256ZM254 248.252H255V129.19H254H253V248.252H254ZM254 129.19L253.488 128.331L242.555 134.842L243.066 135.701L243.578 136.56L254.512 130.05L254 129.19ZM243.066 135.701L242.551 134.844C241.67 135.373 240.745 134.474 241.078 133.657L240.151 133.28L239.225 132.903C238.121 135.618 241.162 138.012 243.581 136.558L243.066 135.701ZM240.151 133.28L241.078 133.657L255.993 96.9978L255.066 96.621L254.14 96.2441L239.225 132.903L240.151 133.28ZM256 252V251C253.239 251 251 253.239 251 256L252 256L253 256C253 254.343 254.343 253 256 253V252ZM252 256H251C251 258.761 253.239 261 256 261V260V259C254.343 259 253 257.657 253 256H252ZM256 260L256 261C258.761 261 261 258.761 261 256H260H259C259 257.657 257.657 259 256 259L256 260ZM260 256L261 256C261 253.239 258.761 251 256 251L256 252L256 253C257.657 253 259 254.343 259 256L260 256ZM246.133 129.192L246.643 130.052L256.511 124.194L256 123.334L255.489 122.474L245.622 128.332L246.133 129.192ZM256 123.334L255.489 124.194L265.357 130.052L265.867 129.192L266.378 128.332L256.511 122.474L256 123.334ZM265.867 129.192L266.793 128.815L256.926 104.564L256 104.941L255.074 105.318L264.941 129.569L265.867 129.192ZM256 104.941L255.074 104.564L245.207 128.815L246.133 129.192L247.059 129.569L256.926 105.318L256 104.941Z" fill="var(--border-silhouette-color)" mask="url(#path-1-outside-1_18306_91642)"/>


      </g>
    `}function Bd(e,t,n=W.regular,r=0){let i=Fd(n);switch(e){case`arrowHead`:return Id(t,i,r);case`needle`:return Rd(t,i);case`vector`:return k`
      <g transform="rotate(${t}) translate(-256, -256)">
        ${kd(i)}
        <circle cx="256" cy="256" r="2" fill="var(--border-silhouette-color)"/>
      </g>
    `;case`beamLine`:return k`
      <g transform="rotate(${t}) translate(-256, -256)">
        ${Ad(i)}
        <circle cx="256" cy="256" r="2" fill="var(--border-silhouette-color)"/>
      </g>
    `}}function Vd(e,t,n=W.regular,r=0){let i=Fd(n);switch(e){case`arrowHead`:return Ld(t,i,r);case`needle`:return zd(t,i);case`vector`:return k`
      <g transform="rotate(${t}) translate(-256, -256)">
        ${jd(i)}
      </g>
    `;case`velocityVector`:return k`
      <g transform="rotate(${t}) translate(-256, -256)">
        ${Md(i)}
      </g>
    `}}var Hd=class extends j{constructor(...e){super(...e),this.heading=0,this.courseOverGround=0,this.headingSetpoint=null,this.atHeadingSetpoint=!1,this.headingSetpointAtZeroDeadband=.5,this.headingSetpointOverride=!1,this.autoAtHeadingSetpoint=!0,this.autoAtHeadingSetpointDeadband=2,this.animateSetpoint=!1,this.touching=!1,this.headingAdvices=[],this.currentWindSpeedKnots=null,this.windFromDirection=null,this.currentSpeed=null,this.currentFromDirection=null,this.vesselImage=wo.genericTop,this.centerReadouts=[],this.hdgArrowStyle=Nd.arrowHead,this.cogArrowStyle=Pd.arrowHead,this.rotDotAnimationFactor=18,this.rotationsPerMinute=1,this.rotType=Fo.dots,this.rotPosition=Io.innerCircle,this.rotMaxValue=60,this.rotArcExtent=60,this.rotPortStarboard=!1,this.rotAtZeroDeadband=Uo,this.direction=`northUp`,this.state=gi.active,this.priority=W.regular,this.priorityElements=[`hdg`],this.showLabels=!1,this.tickmarksInside=!1,this._headingSp=new Ii({angularWraparound:!0,onAnimationEnd:()=>this.requestUpdate()}),this._resizeController=new rl(this,{}),this._hostSizePinned=!1}willUpdate(e){super.willUpdate(e),this._headingSp.sync({setpoint:this.headingSetpoint??void 0,newSetpoint:this.newHeadingSetpoint,atSetpoint:this.atHeadingSetpoint,touching:this.touching,autoAtSetpoint:this.autoAtHeadingSetpoint,autoAtSetpointDeadband:this.autoAtHeadingSetpointDeadband,setpointAtZeroDeadband:this.headingSetpointAtZeroDeadband,setpointOverride:this.headingSetpointOverride,animateSetpoint:this.animateSetpoint})}disconnectedCallback(){super.disconnectedCallback(),this._headingSp.dispose()}get _effectiveRotDegPerMin(){return this.rateOfTurnDegreesPerMinute??this.rotationsPerMinute}getOutsideDecorPx(){return this.tickmarksInside?0:16+(this.showLabels?16:0)}updated(e){super.updated(e),this._hostSizePinned=Yi(this,this._frame,this._hostSizePinned)}get angleAdviceRaw(){return this.headingAdvices.map(({minAngle:e,maxAngle:t,hinted:n,type:r})=>({minAngle:e,maxAngle:t,type:r,state:this.heading>=e&&this.heading<=t?jo.triggered:n?jo.hinted:jo.regular}))}priorityFor(e){return(Array.isArray(this.priorityElements)?this.priorityElements:[]).includes(e)?this.priority:W.regular}colorFor(e){return this.priorityFor(e)===W.enhanced?`var(--instrument-enhanced-secondary-color)`:void 0}readoutPriorityFor(e){switch(e){case Cd.hdg:return this.priorityFor(`hdg`);case Cd.cog:return this.priorityFor(`cog`);case Cd.rot:return this.priorityFor(`rot`)}}get hasCenterReadouts(){return this.centerReadouts.length>0}getRotation(){if(this.direction!==`northUp`){if(this.direction===`headingUp`)return-this.heading;if(this.direction===`courseUp`)return-this.courseOverGround}}render(){let e=[{angle:0,type:G.main},{angle:90,type:G.main},{angle:180,type:G.main},{angle:270,type:G.main}],t=oa({basePadding:72,labelWidthPx:this.getOutsideDecorPx(),containerPx:Ji(this),faceDiameter:this.faceDiameter});this._frame=t;let n=t.viewBox;return O`
      <div class="container">
        <obc-watch
          .touching=${this.touching}
          .arcFrame=${t}
          .advices=${this.angleAdviceRaw}
          .tickmarks=${e}
          .state=${this.state}
          .watchCircleType=${ol.triple}
          .showLabels=${this.showLabels&&!t.labelsHidden}
          .tickmarksInside=${this.tickmarksInside}
          .crosshairEnabled=${!0}
          .crosshairCenterCutout=${this.hasCenterReadouts}
          .northArrow=${!0}
          .angleSetpoint=${this.headingSetpoint??void 0}
          .newAngleSetpoint=${this.newHeadingSetpoint}
          .atAngleSetpoint=${this._headingSp.computeAtSetpoint(this.heading)}
          .angleSetpointAtZeroDeadband=${this.headingSetpointAtZeroDeadband}
          .setpointOverride=${this.headingSetpointOverride}
          .priority=${this.priority}
          .animateSetpoint=${this.animateSetpoint}
          .vessels=${this.hasCenterReadouts?[]:[{size:Co.medium,vesselImage:this.vesselImage,transform:`rotate(${this.heading}deg)`}]}
          .windKnots=${this.currentWindSpeedKnots}
          .windFromDirectionDeg=${this.windFromDirection}
          .windColor=${this.colorFor(`wind`)}
          .current=${this.currentSpeed}
          .currentFromDirectionDeg=${this.currentFromDirection}
          .currentColor=${this.colorFor(`current`)}
          .rotation=${this.getRotation()}
          .rotType=${this.rotType}
          .rotPosition=${this.rotPosition}
          .rotStartAngle=${this.heading+(this.getRotation()??0)}
          .rotEndAngle=${this.heading+this._effectiveRotDegPerMin/(this.rotMaxValue||1)*this.rotArcExtent+(this.getRotation()??0)}
          .rotPriority=${this.priorityFor(`rot`)}
          .rotPortStarboard=${this.rotPortStarboard}
          .rotAtZeroDeadband=${this.rotAtZeroDeadband}
          .rateOfTurnDegreesPerMinute=${this.rateOfTurnDegreesPerMinute}
          .rotDotAnimationFactor=${this.rotDotAnimationFactor}
          .rotationsPerMinute=${this.rotationsPerMinute}
        >
        </obc-watch>
        <svg viewBox="${n}">
          ${Bd(this.hdgArrowStyle,this.heading+(this.getRotation()??0),this.priorityFor(`hdg`))}
          ${Vd(this.cogArrowStyle,this.courseOverGround+(this.getRotation()??0),this.priorityFor(`cog`))}
        </svg>
        ${this.hasCenterReadouts?O`<div class="center-readout-overlay">
                ${Dd(Td(this.centerReadouts,{heading:this.heading,courseOverGround:this.courseOverGround,rateOfTurnDegreesPerMinute:this.rateOfTurnDegreesPerMinute,priorityFor:e=>this.readoutPriorityFor(e)}))}
              </div>`:A}
      </div>
    `}},Z=(Hd.styles=[Od,o`
      * {
        box-sizing: border-box;
      }

      .container {
        position: relative;
        width: 100%;
        height: 100%;
      }

      .container > * {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
      }

      .center-readout-overlay {
        display: flex;
        align-items: center;
        justify-content: center;
        pointer-events: none;
      }

      :host {
        display: block;
        width: 100%;
        height: 100%;
      }
    `],Hd);N([P({type:Number})],Z.prototype,`heading`,void 0),N([P({type:Number})],Z.prototype,`courseOverGround`,void 0),N([P({type:Number})],Z.prototype,`headingSetpoint`,void 0),N([P({type:Number})],Z.prototype,`newHeadingSetpoint`,void 0),N([P({type:Boolean})],Z.prototype,`atHeadingSetpoint`,void 0),N([P({type:Number})],Z.prototype,`headingSetpointAtZeroDeadband`,void 0),N([P({type:Boolean})],Z.prototype,`headingSetpointOverride`,void 0),N([P({type:Boolean,attribute:!1})],Z.prototype,`autoAtHeadingSetpoint`,void 0),N([P({type:Number})],Z.prototype,`autoAtHeadingSetpointDeadband`,void 0),N([P({type:Boolean})],Z.prototype,`animateSetpoint`,void 0),N([P({type:Boolean})],Z.prototype,`touching`,void 0),N([P({type:Array,attribute:!1})],Z.prototype,`headingAdvices`,void 0),N([P({type:Number})],Z.prototype,`currentWindSpeedKnots`,void 0),N([P({type:Number})],Z.prototype,`windFromDirection`,void 0),N([P({type:Number})],Z.prototype,`currentSpeed`,void 0),N([P({type:Number})],Z.prototype,`currentFromDirection`,void 0),N([P({type:String})],Z.prototype,`vesselImage`,void 0),N([P({type:Array,attribute:!1})],Z.prototype,`centerReadouts`,void 0),N([P({type:String})],Z.prototype,`hdgArrowStyle`,void 0),N([P({type:String})],Z.prototype,`cogArrowStyle`,void 0),N([P({type:Number})],Z.prototype,`rateOfTurnDegreesPerMinute`,void 0),N([P({type:Number})],Z.prototype,`rotDotAnimationFactor`,void 0),N([P({type:Number})],Z.prototype,`rotationsPerMinute`,void 0),N([P({type:String})],Z.prototype,`rotType`,void 0),N([P({type:String})],Z.prototype,`rotPosition`,void 0),N([P({type:Number})],Z.prototype,`rotMaxValue`,void 0),N([P({type:Number})],Z.prototype,`rotArcExtent`,void 0),N([P({type:Boolean})],Z.prototype,`rotPortStarboard`,void 0),N([P({type:Number})],Z.prototype,`rotAtZeroDeadband`,void 0),N([P({type:String})],Z.prototype,`direction`,void 0),N([P({type:String})],Z.prototype,`state`,void 0),N([P({type:String})],Z.prototype,`priority`,void 0),N([P({type:Array,attribute:!1})],Z.prototype,`priorityElements`,void 0),N([P({type:Boolean})],Z.prototype,`showLabels`,void 0),N([P({type:Boolean})],Z.prototype,`tickmarksInside`,void 0),N([P({type:Number,attribute:`face-diameter`})],Z.prototype,`faceDiameter`,void 0),Z=N([M(`obc-compass`)],Z);var Ud=o`* {
  -webkit-tap-highlight-color: transparent;
}

/* Shared obc-readout part overrides for readouts embedded inside radial
   navigation instruments. Imported via \`?inline\` into each consuming
   component's \`static styles\`, and applied by the class names that
   \`renderInstrumentReadout\` adds (see instrument-readout.ts).

   Positioning of the readout stays local to each instrument (top%, CSS
   variables, anchors); only these part-centering overrides are shared. */

.instrument-readout-center-value::part(value-cluster) {
  align-self: stretch;
}

.instrument-readout-center-value::part(value-wrapper) {
  align-self: center;
}

.instrument-readout-center-meta::part(meta-wrapper) {
  align-self: center;
}
`,Wd=class extends j{constructor(...e){super(...e),this.rotDotAnimationFactor=18,this.rotationsPerMinute=1,this.rotType=Fo.dots,this.rotPosition=Io.scale,this.priority=W.regular,this.barStartAngle=0,this.barEndAngle=30,this.watchCircleType=ol.single,this.rotPortStarboard=!1,this.rotAtZeroDeadband=Uo,this.hasTrackBar=!1,this.rotMaxValue=60,this.rotArcExtent=60,this.hasReadout=!1,this.label=`ROT`,this.unit=`DEG/min`,this.fractionDigits=0}get trackBarAngle(){let e=this.rotMaxValue||1;return st((this.rateOfTurnDegreesPerMinute??0)/e,-1,1)*this.rotArcExtent}get trackBarColor(){if(this.rotPortStarboard){let e=this.rateOfTurnDegreesPerMinute??0;if(e>0)return`var(--instrument-starboard-secondary-color)`;if(e<0)return`var(--instrument-port-secondary-color)`}return this.priority===W.enhanced?`var(--instrument-enhanced-tertiary-color)`:`var(--instrument-regular-tertiary-color)`}get trackNeedleColor(){if(this.rotPortStarboard){let e=this.rateOfTurnDegreesPerMinute??0;return e>0?`var(--instrument-starboard-primary-color)`:e<0?`var(--instrument-port-primary-color)`:`var(--instrument-regular-secondary-color)`}return this.priority===W.enhanced?`var(--instrument-enhanced-secondary-color)`:`var(--instrument-regular-secondary-color)`}get trackTickmarks(){let e=[{angle:0,type:G.main}];for(let t=30;t<=this.rotArcExtent;t+=30)e.push({angle:t,type:G.primary}),e.push({angle:-t,type:G.primary});return e}render(){return O`<div class="container">
      <obc-watch
        .watchCircleType=${this.watchCircleType}
        .priority=${this.priority}
        .tickmarks=${this.hasTrackBar?this.trackTickmarks:[]}
        .barAreas=${this.hasTrackBar?[{startAngle:0,endAngle:this.trackBarAngle,fillColor:this.trackBarColor}]:[]}
        .needles=${this.hasTrackBar?[{angle:this.trackBarAngle,fillColor:this.trackNeedleColor,strokeColor:`var(--border-silhouette-color)`}]:[]}
        .rotType=${this.rotType}
        .rotPosition=${this.rotPosition}
        .rotStartAngle=${this.barStartAngle}
        .rotEndAngle=${this.barEndAngle}
        .rateOfTurnDegreesPerMinute=${this.rateOfTurnDegreesPerMinute}
        .rotDotAnimationFactor=${this.rotDotAnimationFactor}
        .rotationsPerMinute=${this.rotationsPerMinute}
        .rotPortStarboard=${this.rotPortStarboard}
        .rotAtZeroDeadband=${this.rotAtZeroDeadband}
      ></obc-watch>
      ${this.hasReadout?O`<div class="center-readout-overlay">
              ${Dd([{value:this.rateOfTurnDegreesPerMinute??null,label:this.label,unit:this.unit,fractionDigits:this.fractionDigits,size:hd.large,priority:this.priority,centerValue:!0,centerMeta:!0}])}
            </div>`:A}
    </div>`}},Gd=(Wd.styles=[a(Ud),Od,o`
      * {
        box-sizing: border-box;
      }

      .container {
        position: relative;
        width: 100%;
        height: 100%;
      }

      .container > * {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
      }

      .center-readout-overlay {
        display: flex;
        align-items: center;
        justify-content: center;
        pointer-events: none;
      }
    `],Wd);N([P({type:Number})],Gd.prototype,`rateOfTurnDegreesPerMinute`,void 0),N([P({type:Number})],Gd.prototype,`rotDotAnimationFactor`,void 0),N([P({type:Number})],Gd.prototype,`rotationsPerMinute`,void 0),N([P({type:String})],Gd.prototype,`rotType`,void 0),N([P({type:String})],Gd.prototype,`rotPosition`,void 0),N([P({type:String})],Gd.prototype,`priority`,void 0),N([P({type:Number})],Gd.prototype,`barStartAngle`,void 0),N([P({type:Number})],Gd.prototype,`barEndAngle`,void 0),N([P({type:String})],Gd.prototype,`watchCircleType`,void 0),N([P({type:Boolean})],Gd.prototype,`rotPortStarboard`,void 0),N([P({type:Number})],Gd.prototype,`rotAtZeroDeadband`,void 0),N([P({type:Boolean})],Gd.prototype,`hasTrackBar`,void 0),N([P({type:Number})],Gd.prototype,`rotMaxValue`,void 0),N([P({type:Number})],Gd.prototype,`rotArcExtent`,void 0),N([P({type:Boolean})],Gd.prototype,`hasReadout`,void 0),N([P({type:String})],Gd.prototype,`label`,void 0),N([P({type:String})],Gd.prototype,`unit`,void 0),N([P({type:Number})],Gd.prototype,`fractionDigits`,void 0),Gd=N([M(`obc-rate-of-turn`)],Gd);var Kd=class extends as(j){constructor(...e){super(...e),this.speed=0,this.maxSpeed=100,this.minSpeed=0,this.showLabels=!1,this.tickmarksInside=!1,this.tickmarkInterval=20,this.priority=W.regular,this.needleType=`full`,this.speedAdvices=[],this.tickmarkStyle=Eo.regular,this.hasReadout=!1,this.label=`STW`,this.unit=`KN`,this.fractionDigits=1,this._hostSizePinned=!1,this._resizeController=new rl(this,{}),this.maxAngle=135}firstUpdated(e){super.firstUpdated(e),Xi(this._resizeController,this.renderRoot)}updated(e){super.updated(e),this._hostSizePinned=Yi(this,this._frame,this._hostSizePinned)}getAngle(e){return e/this.maxSpeed*225-90}get minAngle(){return this.getAngle(this.minSpeed)-360}render(){let e=this.priority===W.enhanced?`var(--instrument-enhanced-tertiary-color)`:`var(--instrument-regular-tertiary-color)`,t=this.setpoint===void 0?void 0:this.getAngle(this.setpoint),n=this.tickmarks,r=oa({basePadding:48,labelWidthPx:this.tickmarksInside?0:Zi(n.map(e=>e.text)),containerPx:Ji(this),faceDiameter:this.faceDiameter});this._frame=r;let i=r.labelsHidden?n.map(e=>({...e,text:void 0})):n;return O`
      <div class="container">
        <obc-watch
          .touching=${this.touching}
          .angleSetpoint=${t}
          .newAngleSetpoint=${this.newSetpoint===void 0?void 0:this.getAngle(this.newSetpoint)}
          .atAngleSetpoint=${this.computeAtSetpoint(this.speed)}
          .angleSetpointAtZeroDeadband=${this.setpointAtZeroDeadband}
          .setpointOverride=${this.setpointOverride}
          .animateSetpoint=${this.animateSetpoint}
          .arcFrame=${r}
          .tickmarks=${i}
          .tickmarksInside=${this.tickmarksInside}
          .tickmarkStyle=${this.tickmarkStyle}
          .advices=${this._advices}
          .areas=${[{startAngle:this.minAngle,endAngle:this.maxAngle,roundInsideCut:!0,roundOutsideCut:!0}]}
          .watchCircleType=${ol.double}
          .barAreas=${[{startAngle:this.getAngle(0),endAngle:this.getAngle(this.speed),fillColor:e}]}
        ></obc-watch>
        <svg class="rudder" viewBox=${r.viewBox}>${this.needle}</svg>
        ${this.hasReadout?O`
                ${Sd({className:`speed-gauge-value`,direction:yd.horizontal,value:this.speed,label:this.label,unit:this.unit,fractionDigits:this.fractionDigits,maxDigits:1,priority:this.priority})}
              `:A}
      </div>
    `}get needle(){let e=this.priority===W.enhanced?`var(--instrument-enhanced-secondary-color)`:`var(--instrument-regular-secondary-color)`;return this.needleType===`full`?k`<g transform="rotate(${this.getAngle(this.speed)}) translate(-256, -256)">
      <circle cx="256" cy="256" r="14" fill=${e}/>
      <rect x="250" y="96" width="12" height="192" rx="6" fill=${e}/>
      <rect x="252" y="98" width="8" height="188" rx="4" stroke=${e} fill=${e} stroke-width="4"/>
      </svg> 
`:k`<g transform="rotate(${this.getAngle(this.speed)}) translate(-256, -256)">
<rect x="252" y="96" width="8" height="48" rx="4" fill=${e} stroke="var(--border-silhouette-color)"/>
</svg>
      `}get tickmarks(){let e=[],t=this.tickmarkInterval;if(t!==void 0&&t>0&&Number.isFinite(t)){for(let n=t;n<this.maxSpeed;n+=t)e.push({angle:this.getAngle(n),type:G.primary,text:this.showLabels?n.toString():void 0});this.showLabels&&this.maxSpeed%t===0&&e.push({angle:this.getAngle(this.maxSpeed),type:G.textOnly,text:this.showLabels?this.maxSpeed.toString():void 0});for(let n=-t;n>this.minSpeed;n-=t)e.push({angle:this.getAngle(n),type:G.main,text:this.showLabels?n.toString():void 0});this.showLabels&&this.minSpeed%t===0&&e.push({angle:this.getAngle(this.minSpeed),type:G.textOnly,text:this.showLabels?this.minSpeed.toString():void 0})}return e.push({angle:this.getAngle(0),type:this.minSpeed<0?G.main:G.textOnly,text:this.showLabels?`0`:void 0}),e}get _advices(){return this.speedAdvices.map(e=>{let t=this.getAngle(e.minSpeed),n=this.getAngle(e.maxSpeed),r=e.hinted?jo.hinted:jo.regular;return this.speed>=e.minSpeed&&this.speed<=e.maxSpeed&&(r=jo.triggered),{minAngle:t,maxAngle:n,type:e.type,state:r,hideMinTickmark:e.minSpeed===this.minSpeed,hideMaxTickmark:e.maxSpeed===this.maxSpeed}})}},qd=(Kd.styles=o`
    * {
      box-sizing: border-box;
    }

    .container {
      position: relative;
      width: 100%;
      height: 100%;
    }

    .container > * {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
    }

    obc-watch {
      anchor-name: --watch;
    }

    .speed-gauge-value {
      position: absolute;
      top: clamp(
        70%,
        calc(80% - (anchor-size(--watch height) - 200px) * 0.2),
        80%
      );
      left: 50%;
      transform: translateX(-50%);
      width: fit-content;
      height: fit-content;
    }
  `,Kd);N([P({type:Number})],qd.prototype,`speed`,void 0),N([P({type:Number})],qd.prototype,`maxSpeed`,void 0),N([P({type:Number})],qd.prototype,`minSpeed`,void 0),N([P({type:Boolean})],qd.prototype,`showLabels`,void 0),N([P({type:Boolean})],qd.prototype,`tickmarksInside`,void 0),N([P({type:Number})],qd.prototype,`tickmarkInterval`,void 0),N([P({type:String})],qd.prototype,`priority`,void 0),N([P({type:String})],qd.prototype,`needleType`,void 0),N([P({type:Array,attribute:!1})],qd.prototype,`speedAdvices`,void 0),N([P({type:String})],qd.prototype,`tickmarkStyle`,void 0),N([P({type:Boolean})],qd.prototype,`hasReadout`,void 0),N([P({type:String})],qd.prototype,`label`,void 0),N([P({type:String})],qd.prototype,`unit`,void 0),N([P({type:Number})],qd.prototype,`fractionDigits`,void 0),N([P({type:Number,attribute:`face-diameter`})],qd.prototype,`faceDiameter`,void 0),qd=N([M(`obc-speed-gauge`)],qd);var Jd=o`* {
  -webkit-tap-highlight-color: transparent;
}

* {
  box-sizing: border-box;
}

.container {
  position: relative;
  width: 100%;
  height: 100%;
}

.container > * {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

:host {
  display: block;
  /* The element is the cropped canvas, not a square holding one, so the
     aspect comes from the frame each render — the top crop and zoom both move
     it. 448 / 269 is the un-zoomed box (448 wide × 448·(1 − 40%) tall); keep
     in sync with the \`clips\` top in rudder.ts. */
  width: auto;
  height: auto;
  max-width: 100%;
  max-height: 100%;
  aspect-ratio: var(--obc-rudder-aspect, 448 / 269);
}
`,Yd=class extends as(j){constructor(...e){super(...e),this.angle=0,this.variant=`bar`,this.maxAngle=90,this.showLabels=!1,this.tickmarksInside=!1,this.state=gi.active,this.priority=W.regular,this.tickmarkStyle=Eo.regular,this.advices=[],this.zoomToFitArc=!1,this._radiusOffset=0,this._hostSizePinned=!1,this._resizeController=new rl(this,{})}firstUpdated(e){super.firstUpdated(e),Xi(this._resizeController,this.renderRoot)}updated(e){super.updated(e);let t=this._frame;t&&this.style.setProperty(`--obc-rudder-aspect`,`${t.width} / ${t.height}`),this._hostSizePinned=Yi(this,this._frame,this._hostSizePinned)}_needleIncludeBox(e){if(this.variant!==`needle`)return;let t=lt(this.getAngle(this.angle)),n={x:Math.sin(t),y:-Math.cos(t)},r=Xd.NEEDLE_INNER_RADIUS+e,i=Xd.NEEDLE_OUTER_RADIUS+e,a=Xd.NEEDLE_HALF_WIDTH;return{xMin:Math.min(r*n.x,i*n.x)-a,xMax:Math.max(r*n.x,i*n.x)+a,yMin:Math.min(r*n.y,i*n.y)-a,yMax:Math.max(r*n.y,i*n.y)+a}}get _needleTransform(){let e=this._radiusOffset;return e>0?`translate(-256, -256) rotate(${-this.angle} 256 256) translate(0, ${e})`:`translate(-256, -256) rotate(${-this.angle} 256 256)`}getAngle(e){return 180-e}get barColor(){return this.variant===`needle`?this.state===gi.loading||this.state===gi.off?`var(--instrument-frame-tertiary-color)`:this.priority===W.enhanced?`var(--instrument-enhanced-tertiary-color)`:`var(--instrument-regular-tertiary-color)`:this.state===gi.loading||this.state===gi.off?`var(--instrument-frame-tertiary-color)`:this.priority===W.enhanced?`var(--instrument-enhanced-secondary-color)`:`var(--instrument-regular-secondary-color)`}renderNeedle(){if(this.variant===`bar`)return A;let e;return e=this.state===gi.loading||this.state===gi.off?`var(--instrument-frame-tertiary-color)`:this.priority===W.enhanced?`var(--instrument-enhanced-secondary-color)`:`var(--instrument-regular-secondary-color)`,k`
      <path
        transform="${this._needleTransform}"
        d="M260.462 411.447C259.81 416.73 251.933 416.645 251.514 411.191L239.826 259.24C239.618 258.192 239.508 257.109 239.508 256C239.508 255.764 239.514 255.528 239.524 255.294L239.503 255.039L239.462 254.5H239.576C240.334 246.09 247.401 239.5 256.008 239.5C264.615 239.5 271.681 246.09 272.439 254.5H272.542L272.5 255.039L272.488 255.196C272.501 255.462 272.508 255.731 272.508 256C272.508 257.144 272.391 258.261 272.169 259.339L260.487 411.191L260.462 411.447Z"
        fill="${e}"
        stroke="var(--border-silhouette-color)"
      />
    `}render(){let e=Math.max(2,this.maxAngle),t=[{startAngle:180-e,endAngle:180+e,roundInsideCut:!0,roundOutsideCut:!0}],n=[{startAngle:this.getAngle(0),endAngle:this.getAngle(this.angle),fillColor:this.barColor}],r=this.setpoint===void 0?void 0:180-this.setpoint,i=[{angle:180,type:G.primary,text:this.showLabels?`0`:void 0},{angle:180,type:G.zeroLineThick,color:this.barColor},{angle:180-e,type:G.secondary,text:this.showLabels?e.toFixed(0):void 0},{angle:180+e,type:G.secondary,text:this.showLabels?(-e).toFixed(0):void 0}],a=null;e>70?a=45:e>50?a=30:e>40&&(a=22.5),a!==null&&(i.push({angle:180-a,type:G.primary}),i.push({angle:180+a,type:G.primary}));let o=this.advices.map(e=>{let t=180-e.maxAngle,n=180-e.minAngle,r=this.setpoint!==void 0&&this.setpoint>=e.minAngle&&this.setpoint<=e.maxAngle,i;return i=r?jo.triggered:e.hinted?jo.hinted:jo.regular,{minAngle:t,maxAngle:n,type:e.type,state:i}}),s={basePadding:48,labelWidthPx:this.tickmarksInside?0:Zi(i.map(e=>e.text)),clips:this.zoomToFitArc?void 0:{top:40,bottom:0,left:0,right:0},containerPx:Ji(this),faceDiameter:this.faceDiameter,zoomToFitArc:this.zoomToFitArc,zoomFit:Li.bbox,areas:t,innerRadius:dl(ol.double)},c=oa(s),l=this.zoomToFitArc?this._needleIncludeBox(c.radiusOffset):void 0,u=l?oa({...s,zoomIncludeBox:l}):c;this._radiusOffset=u.radiusOffset,this._frame=u;let d=u.labelsHidden?i.map(e=>({...e,text:void 0})):i,f=u.viewBox;return O`
      <div class="container">
        <obc-watch
          .touching=${this.touching}
          .arcFrame=${u}
          .areas=${t}
          .angleSetpoint=${r}
          .newAngleSetpoint=${this.newSetpoint===void 0?void 0:180-this.newSetpoint}
          .atAngleSetpoint=${this.computeAtSetpoint(this.angle)}
          .angleSetpointAtZeroDeadband=${this.setpointAtZeroDeadband}
          .setpointOverride=${this.setpointOverride}
          .animateSetpoint=${this.animateSetpoint}
          .tickmarks=${d}
          .tickmarksInside=${this.tickmarksInside}
          .tickmarkStyle=${this.tickmarkStyle}
          .watchCircleType=${ol.double}
          .barAreas=${n}
          .state=${this.state}
          .priority=${this.priority}
          .advices=${o}
        ></obc-watch>
        <svg viewBox="${f}">${this.renderNeedle()}</svg>
      </div>
    `}},Xd=Yd,Zd=(Yd.NEEDLE_INNER_RADIUS=-16.5,Yd.NEEDLE_OUTER_RADIUS=160.65,Yd.NEEDLE_HALF_WIDTH=16.5,Yd.styles=a(Jd),Yd);N([P({type:Number})],Zd.prototype,`angle`,void 0),N([P({type:String})],Zd.prototype,`variant`,void 0),N([P({type:Number})],Zd.prototype,`maxAngle`,void 0),N([P({type:Boolean})],Zd.prototype,`showLabels`,void 0),N([P({type:Boolean})],Zd.prototype,`tickmarksInside`,void 0),N([P({type:String})],Zd.prototype,`state`,void 0),N([P({type:String})],Zd.prototype,`priority`,void 0),N([P({type:String})],Zd.prototype,`tickmarkStyle`,void 0),N([P({type:Array,attribute:!1})],Zd.prototype,`advices`,void 0),N([P({type:Boolean})],Zd.prototype,`zoomToFitArc`,void 0),N([P({type:Number,attribute:`face-diameter`})],Zd.prototype,`faceDiameter`,void 0),Zd=Xd=N([M(`obc-rudder`)],Zd);var Qd=o`* {
  -webkit-tap-highlight-color: transparent;
}

:host {
  display: block;
  width: 100%;
}

/* Vertical stack of rows. The 8px default row gap leaves room for a value alert
   frame, which overhangs ~3px above and below each row — so two stacked rows that
   both carry an alarm frame never collide. Override via
   \`--obc-readout-list-row-gap\`. */
.list {
  display: flex;
  flex-direction: column;
  gap: var(--obc-readout-list-row-gap, 8px);
  width: 100%;
}
`,$d,ef=`obc-readout-list-item`,tf=[`unit`,`src`,`value`,`valuetype`,`setpoint`,`advice`,`max-digits`,`fraction-digits`,`has-degree`,`has-setpoint`,`has-advice`];function nf(e){return e.valueType===Ul.text}function rf(e){return e==null||Number.isNaN(e)?0:String(Math.trunc(Math.abs(e))).length}var af=($d=class extends j{constructor(...e){super(...e),this.showDebugOverlay=!1,this.handleSlotChange=()=>{this.align(),this.observeChildren()}}updated(e){super.updated(e),e.has(`showDebugOverlay`)&&this.align()}disconnectedCallback(){this.mutationObserver?.disconnect(),this.mutationObserver=void 0,super.disconnectedCallback()}get items(){return((this.shadowRoot?.querySelector(`slot`))?.assignedElements({flatten:!0})??[]).flatMap(e=>e.tagName.toLowerCase()===ef?[e]:Array.from(e.querySelectorAll(ef)))}align(){let e=this.items;if(e.length===0)return;let t=0,n=0,r=``,i=``,a=!1,o=!1;for(let s of e){let e=!nf(s)||s.hasSetpoint||s.hasAdvice;e&&(n=Math.max(n,Jl(s.fractionDigits)),t=Math.max(t,Jl(s.maxDigits)));let c=Ql(s.value,s.valueType??Ul.number);t=Math.max(t,rf(c),s.hasSetpoint?rf(s.setpoint):0,s.hasAdvice?rf(s.advice):0);let l=(c??0)<0||s.hasSetpoint&&(s.setpoint??0)<0||s.hasAdvice&&(s.advice??0)<0,u=(e&&(s.valueOptions?.hasSignSpacer||s.setpointOptions?.hasSignSpacer||s.adviceOptions?.hasSignSpacer))??!1;(l||u)&&(o=!0),s.unit&&s.unit.length>r.length&&(r=s.unit),s.src&&s.src.length>i.length&&(i=s.src),s.hasDegree&&(a=!0)}let s=t>0?(o?`-`:``)+`0`.repeat(t)+(n>0?`.${`0`.repeat(n)}`:``):void 0;this.mutationObserver?.disconnect();for(let t of e)t.valueOptions={...t.valueOptions,spaceReserver:nf(t)?void 0:s},t.setpointOptions={...t.setpointOptions,spaceReserver:s},t.adviceOptions={...t.adviceOptions,spaceReserver:s},t.unitOptions={...t.unitOptions,spaceReserver:r||void 0},t.srcOptions={...t.srcOptions,spaceReserver:i||void 0},t.hasDegreeSpacer=a&&!t.hasDegree,t.showDebugOverlay=this.showDebugOverlay;this.observeChildren()}observeChildren(){this.mutationObserver||=new MutationObserver(()=>this.align()),this.mutationObserver.observe(this,{childList:!0,subtree:!0,attributes:!0,attributeFilter:tf})}render(){return O`
      <div class="list" part="list">
        <slot @slotchange=${this.handleSlotChange}></slot>
      </div>
    `}},$d.styles=a(Qd),$d);N([P({type:Boolean,reflect:!0})],af.prototype,`showDebugOverlay`,void 0),af=N([M(`obc-readout-list`)],af);var of=1.943844,sf=180/Math.PI,cf,lf=e=>e===null?null:(e*sf%360+360)%360,uf=class extends j{constructor(){super(),this.vessel=null,this.current=!0}render(){let e=this.vessel;if(!e)return O`<div class="empty">Select an own ship to show its conning.</div>`;let t=lf(e.heading),n=lf(e.cog),r=e.rot===null?void 0:e.rot*sf*60,i=e.sog*of,a=this.current?``:`stale`,o=e.rudder===null?null:e.rudder*sf,s=e.rudder_order===null?null:e.rudder_order*sf,c=e.rudder_source===`estimated`;return O`
      <div class="panel ${a}">
        <h2>Heading and course</h2>
        <div class="instrument">
          <obc-compass
            .heading=${t??0}
            .courseOverGround=${n??t??0}
            .rateOfTurnDegreesPerMinute=${r}
          ></obc-compass>
        </div>
        ${t===null?O`<span class="note">Heading unavailable while the vessel is stationary.</span>`:A}
      </div>
      <div class="small ${a}">
        <div class="panel">
          <h2>Rate of turn</h2>
          <div class="instrument">
            <obc-rate-of-turn .rateOfTurnDegreesPerMinute=${r} hasReadout unit="°/min" label="ROT"></obc-rate-of-turn>
          </div>
        </div>
        <div class="panel">
          <h2>Speed over ground</h2>
          <div class="instrument">
            <obc-speed-gauge .speed=${i} .maxSpeed=${Math.max(20,Math.ceil(i/5)*5)} hasReadout unit="kn" label="SOG"></obc-speed-gauge>
          </div>
        </div>
        <div class="panel">
          <h2>Rudder${c?` (estimated from turn)`:``}</h2>
          ${o===null?O`<span class="note">Rudder angle unavailable until the vessel is under way and turning data has arrived.</span>`:O`<div class="instrument rudder">
                <obc-rudder .angle=${o} .setpoint=${s??void 0} .maxAngle=${45} showLabels></obc-rudder>
              </div>
              ${c?O`<span class="note">Not measured: inferred from rate of turn and speed (Nomoto model). Bar: angle; marker: order.</span>`:A}`}
        </div>
      </div>
      <div class="panel ${a}" style="grid-column: 1 / -1">
        <obc-readout-list>
          ${this.item(`HDG`,t,``,1,!0)}
          ${this.item(`COG`,n,``,1,!0)}
          ${this.item(`SOG`,i,`kn`,1)}
          ${this.item(`ROT`,r??null,`°/min`,1)}
          ${this.item(c?`RUD (est.)`:`RUD`,o,``,1,!0)}
          ${this.item(c?`RUD ORD (est.)`:`RUD ORD`,s,``,1,!0)}
          ${this.item(`X`,e.x,`m`,0)}
          ${this.item(`Y`,e.y,`m`,0)}
        </obc-readout-list>
      </div>
    `}item(e,t,n,r,i=!1){return O`<obc-readout-list-item
      label=${e}
      unit=${n}
      .value=${t===null?null:Number(t.toFixed(r))}
      .hasValue=${t!==null}
      .hasDegree=${i}
      .fractionDigits=${r}
      .off=${t===null}
      offText="n/a"
    ></obc-readout-list-item>`}};cf=uf,cf.properties={vessel:{attribute:!1},current:{type:Boolean}},cf.styles=o`
    :host { display: grid; grid-template-columns: minmax(300px, 3fr) minmax(240px, 2fr); grid-template-rows: auto auto; gap: 16px; padding: 16px; box-sizing: border-box; }
    .panel { background: var(--container-section-color); border-radius: 8px; padding: 12px; display: flex; flex-direction: column; gap: 8px; min-height: 0; }
    .panel h2 { margin: 0; font: var(--ui-label-active-font, 600 14px 'Noto Sans'); color: var(--element-neutral-color); }
    .instrument { flex: 1; min-height: 0; display: flex; align-items: center; justify-content: center; }
    .instrument > * { width: 100%; aspect-ratio: 1; max-width: 460px; }
    .small { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-content: start; }
    .small .panel:last-child { grid-column: 1 / -1; }
    .small .instrument > * { max-width: 220px; }
    .small .instrument.rudder > * { aspect-ratio: 2; max-width: 360px; }
    .stale { opacity: 0.45; }
    .note { color: var(--element-neutral-color); font-size: 12px; }
    .empty { grid-column: 1 / -1; display: flex; align-items: center; justify-content: center; color: var(--element-neutral-color); }
  `,customElements.define(`cos-conning-view`,uf);var df=function(e){return e.vertical=`vertical`,e.horizontal=`horizontal`,e}({}),ff=function(e){return e.left=`left`,e.right=`right`,e.top=`top`,e.bottom=`bottom`,e}({}),pf=function(e){return e.regular=`regular`,e.condensed=`condensed`,e}({}),mf=function(e){return e.fill=`fill`,e.tint=`tint`,e}({}),hf=function(e){return e.center=`center`,e.inner=`inner`,e.outer=`outer`,e}({}),gf=`--instrument-components-watchface-frame-regular-border-radius`;function _f(e,t){if(!e)return;let n=e.trim(),r=Number.parseFloat(n);if(!Number.isFinite(r))return;if(n.endsWith(`px`))return r;let i=typeof getComputedStyle==`function`;if(n.endsWith(`rem`)){if(!i)return;let e=t?.documentElement??(typeof document<`u`?document.documentElement:void 0);if(!e)return;let n=Number.parseFloat(getComputedStyle(e).fontSize);return Number.isFinite(n)?r*n:void 0}if(n.endsWith(`em`)){if(!i)return;let e=t?.element;if(!e)return;let n=Number.parseFloat(getComputedStyle(e).fontSize);return Number.isFinite(n)?r*n:void 0}return r}function vf(e,t,n=gf){let r=t===`condensed`?4:8;return typeof getComputedStyle==`function`?_f(getComputedStyle(e).getPropertyValue(n).trim(),{element:e,documentElement:e.ownerDocument?.documentElement??(typeof document<`u`?document.documentElement:void 0)})??r:r}function yf(e,t){if(typeof MutationObserver>`u`)return;let n=new MutationObserver(()=>t()),r=[e],i=e.parentElement;for(;i;)r.push(i),i=i.parentElement;let a=e.ownerDocument?.documentElement;a&&r.push(a);for(let e of r)n.observe(e,{attributes:!0,attributeFilter:[`class`,`style`]});return n}function bf(e){return e===`condensed`?4:8}function xf(e){let t=bf(e.scaleType),n=e.borderRadius;return typeof n==`number`&&Number.isFinite(n)&&n>=0?n:t}function Sf(e){let t=Number.isFinite(e.barThickness)?e.barThickness:0;if(!e.hasBar)return t;let n=xf(e);return Math.max(t,n*2)}function Cf(e){let t=Number.isFinite(e.tickThickness)?e.tickThickness:0;return e.scaleType===`condensed`?Math.min(t,14):t}function wf(e){return{orientation:e.orientation,side:e.side,hasBar:e.hasBar,hasScale:e.hasScale,labels:e.labels,barThickness:Sf(e),tickThickness:Cf(e),labelThickness:e.labelThickness,length:e.length,scaleType:e.scaleType,advicePosition:e.advicePosition,hasAdvice:!!e.advices&&e.advices.length>0,hasSetpoint:e.setpoint!==void 0||e.newSetpoint!==void 0||e.departingNewSetpoint!==void 0}}function Tf(e,t){return e.orientation===`vertical`?{x:t.viewBoxPerpStart,y:-e.length/2,width:t.viewBoxThickness,height:e.length}:{x:0,y:t.viewBoxPerpStart,width:e.length,height:t.viewBoxThickness}}function Ef(e){let{containerMainAxisSize:t,scaleReferenceSize:n}=e;return t<=0||n<=0?1:t/n}function Df(e){let t=e.hasBar?e.barThickness:0,n=Cf(e),r=e.hasScale?n:0,i=e.labels?e.labelThickness:0,a=Of(e),o=kf(e),s=t+Math.max(r+i,a,o);return{thickness:s,viewBoxPerpStart:e.orientation===`vertical`&&e.side===`right`||e.orientation===`horizontal`&&e.side===`bottom`?0:-s,viewBoxLength:e.length,viewBoxThickness:s}}function Of(e){if(!e.hasAdvice)return 0;let t=e.hasBar?e.advicePosition??`inner`:`inner`;return t===`center`?0:t===`outer`?24:16}function kf(e){return e.hasSetpoint?Jf()+8+21:0}function Af(e){return e.orientation===`vertical`}function Q(e){return e.orientation===`vertical`&&e.side===`right`||e.orientation===`horizontal`&&e.side===`bottom`}function jf(e,t){return e<=0&&t>=0}function Mf(e){let t=e.mainTickmarks?.length?e.mainTickmarks:[e.minValue,0,e.maxValue];return[...new Set(t)].filter(t=>t>=e.minValue&&t<=e.maxValue).sort((e,t)=>e-t)}var Nf=1e3,Pf=64,Ff=new Set;function If(e,t){let n=Math.floor((e.maxValue-e.minValue)/t)+1;if(!(n>1e3))return!1;let r=`${e.minValue}/${e.maxValue}/${t}`;return Ff.has(r)||(Ff.size>=Pf&&Ff.clear(),Ff.add(r),console.warn(`[external-scale] tick interval ${t} over the range ${e.minValue}…${e.maxValue} is ${n} ticks; the ladder is not drawn (limit ${Nf}). A range in epoch milliseconds needs an interval in milliseconds.`)),!0}function Lf(e){let t=e.touching??!1;return Fi({value:e.value,setpoint:e.setpoint,touching:t,auto:e.autoAtSetpoint,deadband:e.autoAtSetpointDeadband,atSetpointManual:e.atSetpoint})}function Rf(e){return(e.touching??!1)&&e.newSetpoint===void 0?yi.focus:Lf(e)?e.setpoint!==void 0&&Math.abs(e.setpoint)<e.setpointAtZeroDeadband?yi.equalZero:yi.equal:yi.notEqual}function zf(e){return e.priority===W.enhanced?bi.enhanced:bi.regular}function Bf(e){return e.setpointDisabled===void 0?e.setpointOverride?!1:e.state===gi.loading||e.state===gi.off:e.setpointDisabled}function Vf(e){let t=e.priority===W.enhanced,n=e.fillMode===`tint`?t?`var(--instrument-enhanced-tertiary-color)`:`var(--instrument-regular-tertiary-color)`:t?`var(--instrument-enhanced-secondary-color)`:`var(--instrument-regular-secondary-color)`,r=t?`var(--instrument-enhanced-secondary-color)`:`var(--instrument-regular-secondary-color)`,i=t?`var(--instrument-enhanced-tertiary-color)`:`var(--instrument-regular-tertiary-color)`,a=t?`var(--instrument-enhanced-primary-color)`:`var(--instrument-regular-primary-color)`;return(e.state===gi.loading||e.state===gi.off)&&(n=`transparent`,r=`var(--instrument-frame-tertiary-color)`,i=`var(--instrument-frame-tertiary-color)`,a=`var(--instrument-frame-tertiary-color)`),{barFillColor:n,markerFillColor:r,markerStrokeColor:i,setpointColor:a}}function Hf(e,t){return e.map(e=>{let n=t!==void 0&&t>=e.min&&t<=e.max?jo.triggered:e.hinted?jo.hinted:jo.regular;return{min:e.min,max:e.max,type:e.type,state:n}})}function Uf(e){return Af(e)?(e.paddingStart-e.paddingEnd)/2:e.paddingStart}function Wf(e){return Math.max(0,e.length-e.paddingStart-e.paddingEnd)}function Gf(e,t){let n=Wf(e),r=e.reverse?e.minValue+e.maxValue-t:t;return Af(e)?ts(r,e.minValue,e.maxValue,n)+Uf(e):ns(r,e.minValue,e.maxValue,n)+Uf(e)}function Kf(e){let t=e===`condensed`;return{primary:t?10:20,secondary:t?4:8,tertiary:t?2:4,main:t?10:20}}function qf(e){return e.hasBar?Q(e)?e.barThickness:-e.barThickness:0}function Jf(){return 4}function Yf(){return 8}function Xf(e,t,n,r){let i=`var(--instrument-frame-tertiary-color)`;if(Af(e)){let e=n,a=n+r,o=t;return k`<line x1=${e} x2=${a} y1=${o} y2=${o} stroke=${i} stroke-width=${1} vector-effect="non-scaling-stroke"/>`}let a=n,o=n+r,s=t;return k`<line x1=${s} x2=${s} y1=${a} y2=${o} stroke=${i} stroke-width=${1} vector-effect="non-scaling-stroke"/>`}function Zf(e,t,n,r,i){let a=[],o=[];if(t<=0||!Number.isFinite(t)||If(e,t))return{svgs:a,values:o};let s=jf(e.minValue,e.maxValue),c=t=>{i.includes(t)||(o.push(t),a.push(Xf(e,Gf(e,t),n,r)))};if(s){for(let n=t;n<=e.maxValue;n+=t)c(n);for(let n=-t;n>=e.minValue;n-=t)c(n)}else{let n=Math.ceil(e.minValue/t)*t;for(let r=n;r<=e.maxValue;r+=t)c(r)}return{svgs:a,values:o}}function Qf(e){if(!e.hasScale)return[];let t=[],n=[],r=qf(e),i=Jf(),a=Q(e)?r+i:r-i,{primary:o,secondary:s,tertiary:c,main:l}=Kf(e.scaleType);if(jf(e.minValue,e.maxValue)){let r=e.minValue===0||e.maxValue===0;if(!(e.scaleBackground&&r)){let n=o,r=a;t.push(Xf(e,Gf(e,0),r,Q(e)?n:-n))}n.push(0)}if(e.mainTickmarks){let i=e.frameStyle===`flat`?r:a,o=e.frameStyle===`flat`?l+4:l,s=Q(e)?o:-o;for(let r of Mf(e)){if(e.scaleBackground&&(r===e.minValue||r===e.maxValue)){n.push(r);continue}t.push(Xf(e,Gf(e,r),i,s)),n.push(r)}}if(e.primaryTickmarkInterval!==void 0&&e.primaryTickmarkInterval>0){let{svgs:r,values:i}=Zf(e,e.primaryTickmarkInterval,a,Q(e)?o:-o,n);t.push(...r),n.push(...i)}if(e.secondaryTickmarkInterval!==void 0&&e.secondaryTickmarkInterval>0){let{svgs:r}=Zf(e,e.secondaryTickmarkInterval,a,Q(e)?s:-s,n);t.push(...r)}if(e.tertiaryTickmarkInterval!==void 0&&e.tertiaryTickmarkInterval>0){let{svgs:r}=Zf(e,e.tertiaryTickmarkInterval,a,Q(e)?c:-c,n);t.push(...r)}return t}function $f(e){if(!e.labels)return[];let t=`var(--font-family-main)`,n=`var(--instrument-tick-mark-label-secondary-color)`,r=`calc(var(--global-typography-ui-label-font-size) / var(--scale, 1))`,i=qf(e),a=Cf(e),o=Q(e)?i+(e.hasScale?a:0)+Yf():i-(e.hasScale?a:0)-Yf(),s=[],c=(i,a)=>{let c=Gf(e,i);if(Af(e)){let l=o,u=c,d=Q(e)?`start`:`end`,f=a?.baseline??`middle`;s.push(k`<text x=${l} y=${u} text-anchor=${d} dominant-baseline=${f} font-family=${t} style="font-size: ${r}" fill=${n}>${i}</text>`);return}let l=o,u=c,d=Q(e)?`hanging`:`auto`,f=a?.anchor??`middle`;s.push(k`<text x=${u} y=${l} text-anchor=${f} dominant-baseline=${d} font-family=${t} style="font-size: ${r}" fill=${n}>${i}</text>`)};if(e.mainTickmarkLabels){for(let t of Mf(e))c(t,t===e.minValue?{anchor:`start`,baseline:`auto`}:t===e.maxValue?{anchor:`end`,baseline:`hanging`}:void 0);return s}let l=e.primaryTickmarkInterval;if(l===void 0||l<=0||!Number.isFinite(l)||If(e,l))return[];if(jf(e.minValue,e.maxValue)){for(let t=0;t<=e.maxValue;t+=l)c(t);for(let t=-l;t>=e.minValue;t-=l)c(t)}else{let t=Math.ceil(e.minValue/l)*l;for(let n=t;n<=e.maxValue;n+=l)c(n)}return s}function ep(e){if(!e.hasBar)return A;let t=e.scaleType===`condensed`?4:8,n=e.borderRadius??t,r;r=e.barContainerStyle===void 0?e.scaleBackground?`var(--instrument-frame-secondary-color)`:`var(--instrument-frame-primary-color)`:e.barContainerStyle===`secondary`?`var(--instrument-frame-secondary-color)`:`var(--instrument-frame-primary-color)`;let i=`var(--instrument-frame-tertiary-color)`,a=Wf(e),o=Uf(e),s=!0,c=!0,l=!0,u=!0;if(e.borderRadiusPosition){if(e.borderRadiusPosition===vi.middleChild||e.borderRadiusPosition===vi.middleRoundedChild)s=!1,c=!1,l=!1,u=!1;else if(Af(e)){let t=e.side===`right`,n=e.borderRadiusPosition===vi.innerFirstChild;t?(s=n,l=n,c=!n,u=!n):(s=!n,l=!n,c=n,u=n)}else{let t=e.side===`bottom`,n=e.borderRadiusPosition===vi.innerFirstChild;t?(s=n,c=n,l=!n,u=!n):(s=!n,c=!n,l=n,u=n)}}let d=n,f=s&&c&&l&&u,p=!s&&!c&&!l&&!u;if(Af(e)){let t=Q(e)?0:-e.barThickness,n=-a/2+o,m=e.barThickness,h=a,g=e.side===`right`,_,v;e.scaleBackground?g?(_=0,v=e.barThickness+1):(_=-e.barThickness-1,v=0):(_=g?0:-e.barThickness,v=g?e.barThickness:0);let y=rs(t,m,_,v,1);t=y.x,m=y.width;let b=is(n,h,-a/2+o,a/2+o,1);if(n=b.y,h=b.height,f||p){let a=f?d:0,o=f?d:0;if(e.scaleBackground){let s=e.side===`right`,c;return s?(c=`M ${t} ${n+(p?0:d)} L ${t} ${n+h-(p?0:d)}`,p||(c+=` Q ${t} ${n+h} ${t+d} ${n+h}`),c+=` L ${t+m-(p?0:d)} ${n+h}`,p||(c+=` Q ${t+m} ${n+h} ${t+m} ${n+h-d}`),c+=` M ${t+m} ${n+(p?0:d)}`,p||(c+=` Q ${t+m} ${n} ${t+m-d} ${n}`),c+=` L ${t+(p?0:d)} ${n}`,p||(c+=` Q ${t} ${n} ${t} ${n+d}`)):(c=`M ${t+(p?0:d)} ${n}`,c+=` L ${t+m-(p?0:d)} ${n}`,p||(c+=` Q ${t+m} ${n} ${t+m} ${n+d}`),c+=` L ${t+m} ${n+h-(p?0:d)}`,p||(c+=` Q ${t+m} ${n+h} ${t+m-d} ${n+h}`),c+=` L ${t+(p?0:d)} ${n+h}`,p||(c+=` Q ${t} ${n+h} ${t} ${n+h-d}`),c+=` M ${t} ${n+(p?0:d)}`,p||(c+=` Q ${t} ${n} ${t+d} ${n}`)),k`
          <rect x=${t} y=${n} width=${m} height=${h} rx=${a} ry=${o} fill=${r} stroke="none"/>
          <path d="${c}" fill="none" stroke=${i} stroke-width=${1} vector-effect="non-scaling-stroke"/>
        `}return k`<rect x=${t} y=${n} width=${m} height=${h} rx=${a} ry=${o} fill=${r} stroke=${i} vector-effect="non-scaling-stroke"/>`}let x=t,S=n,C=m,w=h,T=`M ${x+(s?d:0)} ${S}`;if(T+=` L ${x+C-(c?d:0)} ${S}`,c&&(T+=` Q ${x+C} ${S} ${x+C} ${S+d}`),T+=` L ${x+C} ${S+w-(u?d:0)}`,u&&(T+=` Q ${x+C} ${S+w} ${x+C-d} ${S+w}`),T+=` L ${x+(l?d:0)} ${S+w}`,l&&(T+=` Q ${x} ${S+w} ${x} ${S+w-d}`),T+=` L ${x} ${S+(s?d:0)}`,s&&(T+=` Q ${x} ${S} ${x+d} ${S}`),T+=` Z`,e.scaleBackground){let t=e.side===`right`,n;return t?(n=`M ${x} ${S+(s?d:0)}`,s&&(n+=` Q ${x} ${S} ${x+d} ${S}`),n+=` L ${x+C-(c?d:0)} ${S}`,c&&(n+=` Q ${x+C} ${S} ${x+C} ${S+d}`),n+=` M ${x+C} ${S+w-(u?d:0)}`,u&&(n+=` Q ${x+C} ${S+w} ${x+C-d} ${S+w}`),n+=` L ${x+(l?d:0)} ${S+w}`,l&&(n+=` Q ${x} ${S+w} ${x} ${S+w-d}`),n+=` L ${x} ${S+(s?d:0)}`):(n=`M ${x+(s?d:0)} ${S}`,n+=` L ${x+C-(c?d:0)} ${S}`,c&&(n+=` Q ${x+C} ${S} ${x+C} ${S+d}`),n+=` L ${x+C} ${S+w-(u?d:0)}`,u&&(n+=` Q ${x+C} ${S+w} ${x+C-d} ${S+w}`),n+=` L ${x+(l?d:0)} ${S+w}`,l&&(n+=` Q ${x} ${S+w} ${x} ${S+w-d}`),n+=` M ${x} ${S+(s?d:0)}`,s&&(n+=` Q ${x} ${S} ${x+d} ${S}`)),k`
        <path d=${T} fill=${r} stroke="none"/>
        <path d="${n}" fill="none" stroke=${i} stroke-width=${1} vector-effect="non-scaling-stroke"/>
      `}return k`<path d=${T} fill=${r} stroke=${i} stroke-width=${1} vector-effect="non-scaling-stroke"/>`}let m=Uf(e),h=Q(e)?0:-e.barThickness,g=a,_=e.barThickness,v=e.side===`bottom`,y,b;e.scaleBackground?v?(y=0,b=e.barThickness+1):(y=-e.barThickness-1,b=0):(y=v?0:-e.barThickness,b=v?e.barThickness:0);let x=rs(m,g,m,m+g,1);m=x.x,g=x.width;let S=is(h,_,y,b,1);if(h=S.y,_=S.height,f||p){let t=f?d:0,n=f?d:0;if(e.scaleBackground){let a=e.side===`bottom`,o;return a?(o=`M ${m+(p?0:d)} ${h}`,o+=` L ${m+g-(p?0:d)} ${h}`,p||(o+=` Q ${m+g} ${h} ${m+g} ${h+d}`),o+=` L ${m+g} ${h+_-(p?0:d)}`,p||(o+=` Q ${m+g} ${h+_} ${m+g-d} ${h+_}`),o+=` M ${m+(p?0:d)} ${h+_}`,p||(o+=` Q ${m} ${h+_} ${m} ${h+_-d}`),o+=` L ${m} ${h+(p?0:d)}`,p||(o+=` Q ${m} ${h} ${m+d} ${h}`)):(o=`M ${m} ${h+(p?0:d)}`,o+=` L ${m} ${h+_-(p?0:d)}`,p||(o+=` Q ${m} ${h+_} ${m+d} ${h+_}`),o+=` L ${m+g-(p?0:d)} ${h+_}`,p||(o+=` Q ${m+g} ${h+_} ${m+g} ${h+_-d}`),o+=` L ${m+g} ${h+(p?0:d)}`,p||(o+=` Q ${m+g} ${h} ${m+g-d} ${h}`),o+=` M ${m+(p?0:d)} ${h}`,p||(o+=` Q ${m} ${h} ${m} ${h+d}`)),k`
        <rect x=${m} y=${h} width=${g} height=${_} rx=${t} ry=${n} fill=${r} stroke="none"/>
        <path d="${o}" fill="none" stroke=${i} stroke-width=${1} vector-effect="non-scaling-stroke"/>
      `}return k`<rect x=${m} y=${h} width=${g} height=${_} rx=${t} ry=${n} fill=${r} stroke=${i} vector-effect="non-scaling-stroke"/>`}let C=m,w=h,T=g,E=_,D=`M ${C+(s?d:0)} ${w}`;if(D+=` L ${C+T-(c?d:0)} ${w}`,c&&(D+=` Q ${C+T} ${w} ${C+T} ${w+d}`),D+=` L ${C+T} ${w+E-(u?d:0)}`,u&&(D+=` Q ${C+T} ${w+E} ${C+T-d} ${w+E}`),D+=` L ${C+(l?d:0)} ${w+E}`,l&&(D+=` Q ${C} ${w+E} ${C} ${w+E-d}`),D+=` L ${C} ${w+(s?d:0)}`,s&&(D+=` Q ${C} ${w} ${C+d} ${w}`),D+=` Z`,e.scaleBackground){let t=e.side===`bottom`,n;return t?(n=`M ${C+(s?d:0)} ${w}`,n+=` L ${C+T-(c?d:0)} ${w}`,c&&(n+=` Q ${C+T} ${w} ${C+T} ${w+d}`),n+=` L ${C+T} ${w+E-(u?d:0)}`,u&&(n+=` Q ${C+T} ${w+E} ${C+T-d} ${w+E}`),n+=` M ${C+(l?d:0)} ${w+E}`,l&&(n+=` Q ${C} ${w+E} ${C} ${w+E-d}`),n+=` L ${C} ${w+(s?d:0)}`,s&&(n+=` Q ${C} ${w} ${C+d} ${w}`)):(n=`M ${C} ${w+(s?d:0)}`,s&&(n+=` Q ${C} ${w} ${C+d} ${w}`),n+=` M ${C+T-(c?d:0)} ${w}`,c&&(n+=` Q ${C+T} ${w} ${C+T} ${w+d}`),n+=` L ${C+T} ${w+E-(u?d:0)}`,u&&(n+=` Q ${C+T} ${w+E} ${C+T-d} ${w+E}`),n+=` L ${C+(l?d:0)} ${w+E}`,l&&(n+=` Q ${C} ${w+E} ${C} ${w+E-d}`),n+=` L ${C} ${w+(s?d:0)}`),k`
      <path d=${D} fill=${r} stroke="none"/>
      <path d="${n}" fill="none" stroke=${i} stroke-width=${1} vector-effect="non-scaling-stroke"/>
    `}return k`<path d=${D} fill=${r} stroke=${i} stroke-width=${1} vector-effect="non-scaling-stroke"/>`}function tp(e){if(!e.hasBar||e.value===void 0)return A;let t=`obc-bar-fill-clip-${Math.random().toString(36).slice(2)}`,n=e.scaleType===`condensed`?4:8,r=e.borderRadius??n,i=Vf(e),a=e.fillMin??0,o=e.fillMax??e.value,s=st(a,e.minValue,Math.max(e.minValue,e.maxValue)),c=st(o,e.minValue,Math.max(e.minValue,e.maxValue)),l=Gf(e,s),u=Gf(e,c),d=Wf(e),f=Uf(e),p=!0,m=!0,h=!0,g=!0;if(e.borderRadiusPosition){if(e.borderRadiusPosition===vi.middleChild||e.borderRadiusPosition===vi.middleRoundedChild)p=!1,m=!1,h=!1,g=!1;else if(Af(e)){let t=e.side===`right`,n=e.borderRadiusPosition===vi.innerFirstChild;t?(p=n,h=n,m=!n,g=!n):(p=!n,h=!n,m=n,g=n)}else{let t=e.side===`bottom`,n=e.borderRadiusPosition===vi.innerFirstChild;t?(p=n,m=n,h=!n,g=!n):(p=!n,m=!n,h=n,g=n)}}let _=p&&m&&h&&g,v=!p&&!m&&!h&&!g;if(Af(e)){let n=Q(e)?0:-e.barThickness,a=e.barThickness,o=Math.min(l,u),s=Math.abs(u-l),c=Q(e)?0:-e.barThickness,y=-d/2+f,b=e.barThickness,x=d,S=v?k`<rect x=${c} y=${y} width=${b} height=${x} rx=${0} ry=${0}/>`:_?k`<rect x=${c} y=${y} width=${b} height=${x} rx=${r} ry=${r}/>`:k`<path d=${(()=>{let e=c,t=y,n=b,i=x,a=`M ${e+(p?r:0)} ${t}`;return a+=` L ${e+n-(m?r:0)} ${t}`,m&&(a+=` Q ${e+n} ${t} ${e+n} ${t+r}`),a+=` L ${e+n} ${t+i-(g?r:0)}`,g&&(a+=` Q ${e+n} ${t+i} ${e+n-r} ${t+i}`),a+=` L ${e+(h?r:0)} ${t+i}`,h&&(a+=` Q ${e} ${t+i} ${e} ${t+i-r}`),a+=` L ${e} ${t+(p?r:0)}`,p&&(a+=` Q ${e} ${t} ${e+r} ${t}`),a+=` Z`,a})()}/>`,C=k`<rect x=${n} y=${o} width=${a} height=${s} fill=${i.barFillColor} stroke="none"/>`;if(e.fillMode===`tint`){let r=k`<rect x=${n} y=${Gf(e,e.value)-4} width=${a} height=${8} rx=${4} fill=${i.markerFillColor} stroke=${i.markerStrokeColor} vector-effect="non-scaling-stroke"/>`;return k`<defs>
        <clipPath id=${t} clipPathUnits="userSpaceOnUse">${S}</clipPath>
      </defs>
      <g clip-path=${`url(#${t})`}>
        ${C}
        ${r}
      </g>`}return k`<defs>
      <clipPath id=${t} clipPathUnits="userSpaceOnUse">${S}</clipPath>
    </defs>
    <g clip-path=${`url(#${t})`}>
      ${C}
    </g>`}let y=Q(e)?0:-e.barThickness,b=e.barThickness,x=Math.min(l,u),S=Math.abs(u-l),C=Uf(e),w=Q(e)?0:-e.barThickness,T=d,E=e.barThickness,D=v?k`<rect x=${C} y=${w} width=${T} height=${E} rx=${0} ry=${0}/>`:_?k`<rect x=${C} y=${w} width=${T} height=${E} rx=${r} ry=${r}/>`:k`<path d=${(()=>{let e=C,t=w,n=T,i=E,a=`M ${e+(p?r:0)} ${t}`;return a+=` L ${e+n-(m?r:0)} ${t}`,m&&(a+=` Q ${e+n} ${t} ${e+n} ${t+r}`),a+=` L ${e+n} ${t+i-(g?r:0)}`,g&&(a+=` Q ${e+n} ${t+i} ${e+n-r} ${t+i}`),a+=` L ${e+(h?r:0)} ${t+i}`,h&&(a+=` Q ${e} ${t+i} ${e} ${t+i-r}`),a+=` L ${e} ${t+(p?r:0)}`,p&&(a+=` Q ${e} ${t} ${e+r} ${t}`),a+=` Z`,a})()}/>`,ee=k`<rect x=${x} y=${y} width=${S} height=${b} fill=${i.barFillColor} stroke="none"/>`;if(e.fillMode===`tint`){let n=k`<rect x=${Gf(e,e.value)-4} y=${y} width=${8} height=${b} rx=${4} fill=${i.markerFillColor} stroke=${i.markerStrokeColor} vector-effect="non-scaling-stroke"/>`;return k`<defs>
      <clipPath id=${t} clipPathUnits="userSpaceOnUse">${D}</clipPath>
    </defs>
    <g clip-path=${`url(#${t})`}>
      ${ee}
      ${n}
    </g>`}return k`<defs>
    <clipPath id=${t} clipPathUnits="userSpaceOnUse">${D}</clipPath>
  </defs>
  <g clip-path=${`url(#${t})`}>
    ${ee}
  </g>`}function np(e){if(!e.scaleBackground)return A;let t=e.scaleType===`condensed`?4:8,n=e.borderRadius??t,r=`var(--instrument-frame-primary-color)`,i=`var(--instrument-frame-tertiary-color)`,{main:a}=Kf(e.scaleType),o=a+Jf(),s=Wf(e),c=Uf(e),l=e.orientation===`vertical`&&e.side===`left`||e.orientation===`horizontal`&&e.side===`top`,u=e.orientation===`vertical`&&e.side===`right`||e.orientation===`horizontal`&&e.side===`top`,d=e.orientation===`vertical`&&e.side===`left`||e.orientation===`horizontal`&&e.side===`bottom`,f=e.orientation===`vertical`&&e.side===`right`||e.orientation===`horizontal`&&e.side===`bottom`,p=n;if(Af(e)){let t=e.hasBar?Q(e)?e.barThickness:-e.barThickness:0,n=Q(e)?t:t-o,a=-s/2+c,m=o,h=s,g=e.side===`right`,_,v;e.hasBar?g?(_=n-1,v=n+m):(_=n,v=n+m+1):(_=n,v=n+m);let y=rs(n,m,_,v,1);n=y.x,m=y.width;let b=is(a,h,-s/2+c,s/2+c,1);a=b.y,h=b.height;let x=n,S=a,C=m,w=h,T=`M ${x+(l?p:0)} ${S}`;T+=` L ${x+C-(u?p:0)} ${S}`,u&&(T+=` Q ${x+C} ${S} ${x+C} ${S+p}`),T+=` L ${x+C} ${S+w-(f?p:0)}`,f&&(T+=` Q ${x+C} ${S+w} ${x+C-p} ${S+w}`),T+=` L ${x+(d?p:0)} ${S+w}`,d&&(T+=` Q ${x} ${S+w} ${x} ${S+w-p}`),T+=` L ${x} ${S+(l?p:0)}`,l&&(T+=` Q ${x} ${S} ${x+p} ${S}`),T+=` Z`;let E=g?x:x+C,D=1/2;return k`<path d=${T} fill=${r} stroke=${i} stroke-width=${1} vector-effect="non-scaling-stroke"/>
      <line x1=${E} x2=${E} y1=${S+D} y2=${S+w-D} stroke=${r} stroke-width=${1.5} vector-effect="non-scaling-stroke"/>`}let m=e.hasBar?Q(e)?e.barThickness:-e.barThickness:0,h=Uf(e),g=Q(e)?m:m-o,_=s,v=o,y=e.side===`bottom`,b,x;e.hasBar?y?(b=g-1,x=g+v):(b=g,x=g+v+1):(b=g,x=g+v);let S=rs(h,_,h,h+_,1);h=S.x,_=S.width;let C=is(g,v,b,x,1);g=C.y,v=C.height;let w=h,T=g,E=_,D=v,ee=`M ${w+(l?p:0)} ${T}`;ee+=` L ${w+E-(u?p:0)} ${T}`,u&&(ee+=` Q ${w+E} ${T} ${w+E} ${T+p}`),ee+=` L ${w+E} ${T+D-(f?p:0)}`,f&&(ee+=` Q ${w+E} ${T+D} ${w+E-p} ${T+D}`),ee+=` L ${w+(d?p:0)} ${T+D}`,d&&(ee+=` Q ${w} ${T+D} ${w} ${T+D-p}`),ee+=` L ${w} ${T+(l?p:0)}`,l&&(ee+=` Q ${w} ${T} ${w+p} ${T}`),ee+=` Z`;let te=y?T:T+D,ne=1/2;return k`<path d=${ee} fill=${r} stroke=${i} stroke-width=${1} vector-effect="non-scaling-stroke"/>
    <line x1=${w+ne} x2=${w+E-ne} y1=${te} y2=${te} stroke=${r} stroke-width=${1.5} vector-effect="non-scaling-stroke"/>`}function rp(e){return Af(e)?e.side===`right`?90:-90:e.side===`bottom`?180:0}function ip(e,t,n,r,i,a,o=1,s=!1){let c=Mi(`external-scale-setpoint-${a}`),l=ji(n),u=Math.abs(t)<e.setpointAtZeroDeadband?Gf(e,0):Gf(e,t),d=qf(e),f=Jf()+l,p=Q(e)?d+f:d-f,m=rp(e),h=Af(e)?p:u,g=Af(e)?u:p;if(s){let e=`var(${Ci}, ${wi})`;return k`
      <g style="transform: translate(${h}px, ${g}px) rotate(${m}deg); opacity: ${o}; transition: transform ${e} ease-out, opacity ${e} ease-out;">
        ${Ni({visualState:n,colorMode:r,disabled:i,id:c})}
      </g>
    `}return k`
    <g transform="translate(${h}, ${g}) rotate(${m})" opacity="${o}">
      ${Ni({visualState:n,colorMode:r,disabled:i,id:c})}
    </g>
  `}function ap(e){let t=e.setpoint!==void 0,n=e.newSetpoint!==void 0,r=e.departingNewSetpoint!==void 0,i=e.animateSetpoint===!0;if(!t&&!n&&!r)return A;let a=[];if(t){let t=Rf(e),r=zf(e),o=Bf(e),s=n?.75:1;a.push(ip(e,e.setpoint,t,r,o,`original`,s,i))}if(n||r){let t=n,r=t?e.newSetpoint:e.departingNewSetpoint,o=+!!t,s=yi.focus,c=zf(e);a.push(ip(e,r,s,c,!1,`new`,o,i))}return k`${a}`}function op(e){if(!e.highlightCurrentValue||e.value===void 0||!e.hasScale)return A;let t=Gf(e,e.value),n=qf(e),r=Q(e)?n+7:n-7,i=Vf(e).markerFillColor,a=`var(--instrument-frame-primary-color)`;return Af(e)?k`
      <circle
        cx=${r}
        cy=${t}
        r=${6}
        fill=${i}
        stroke=${a}
        stroke-width=${2}
        vector-effect="non-scaling-stroke"
      />
    `:k`
    <circle
      cx=${t}
      cy=${r}
      r=${6}
      fill=${i}
      stroke=${a}
      stroke-width=${2}
      vector-effect="non-scaling-stroke"
    />
  `}function sp(e,t,n,r){if(t>=e.maxValue||t<=e.minValue)return null;let i=Do(n),a=Gf(e,t),o=Jf(),s=Q(e)?r+o:r-o,c=Cf(e),l=Q(e)?s+c:s-c;return Af(e)?k`<line x1=${s} x2=${l} y1=${a} y2=${a} stroke=${i} stroke-width="1" vector-effect="non-scaling-stroke"/>`:k`<line x1=${a} x2=${a} y1=${s} y2=${l} stroke=${i} stroke-width="1" vector-effect="non-scaling-stroke"/>`}function cp(e,t,n,r,i){if(Af(e)){let a=Gf(e,t.min),o=Gf(e,t.max),s=Math.min(a,o),c=Math.max(a,o);return k`<rect x=${n+4} y=${s+4} width=${8} height=${Math.max(0,c-s-8)} rx=${4} ry=${4} fill=${r} stroke=${i} stroke-width="1" vector-effect="non-scaling-stroke"/>`}let a=Gf(e,t.min),o=Gf(e,t.max),s=Math.min(a,o),c=Math.max(a,o);return k`<rect x=${s+4} y=${n+4} width=${Math.max(0,c-s-8)} height=${8} rx=${4} ry=${4} fill=${r} stroke=${i} stroke-width="1" vector-effect="non-scaling-stroke"/>`}function lp(e,t){let n=qf(e),r=e.hasBar?e.advicePosition:`inner`,i;if(r===`center`){let t=e.barThickness/2-4;i=(Af(e),Q(e)?t-4:-e.barThickness+t-4)}else i=r===`inner`?Q(e)?n:n-16:Q(e)?e.barThickness+10:-e.barThickness-Cf(e)+14;let a=[],o=`var(--instrument-frame-tertiary-color)`,s=t.min>e.minValue,c=t.max<e.maxValue,l=Q(e)?0:-e.barThickness,u=Q(e)?e.barThickness:0,d=t=>{let n=Gf(e,t);Af(e)?a.push(k`<line x1=${l} x2=${u} y1=${n} y2=${n} stroke=${o} stroke-width="1" vector-effect="non-scaling-stroke" stroke-dasharray="4 4"/>`):a.push(k`<line x1=${n} x2=${n} y1=${l} y2=${u} stroke=${o} stroke-width="1" vector-effect="non-scaling-stroke" stroke-dasharray="4 4"/>`)};if(s&&d(t.min),c&&d(t.max),t.type===Ao.caution){let r,o=`var(--instrument-frame-primary-color)`;t.state===jo.hinted?r=`var(--instrument-frame-tertiary-color)`:t.state===jo.regular?r=`var(--instrument-tick-mark-tertiary-color)`:(r=`var(--on-caution-active-color)`,o=`var(--alert-caution-color)`);let s=[],c=Gf(e,t.min),l=Gf(e,t.max),u=Math.min(c,l),d=Math.max(c,l)-u;if(Af(e)){let e=i+8-25,t=u-25;for(let n=-64;n<d+64;n+=16){let i=`translate(${e} ${t+n})`;s.push(k`<g transform=${i}><path d=${`M 50 0 L 0 50`} stroke=${r} stroke-width="6"/></g>`)}}else{let e=i+8-25,t=u-25;for(let n=-64;n<d+64;n+=16){let i=`translate(${t+n} ${e})`;s.push(k`<g transform=${i}><path d=${`M 0 50 L 50 0`} stroke=${r} stroke-width="6"/></g>`)}}let f=`externalScaleAdviceMask-${t.min}-${t.max}-${Math.random().toString(36).slice(2)}`,p=Eo.regular;return t.state===jo.regular?p=Eo.regular:t.state===jo.triggered&&(p=Eo.enhanced),k`
      <defs>
        <mask id=${f} maskUnits="userSpaceOnUse" maskContentUnits="userSpaceOnUse" x="-4096" y="-4096" width="8192" height="8192">
          ${cp(e,t,i,`white`,`none`)}
        </mask>
      </defs>
      <g mask="url(#${f})">
        ${o?k`<rect x="-2048" y="-2048" width="4096" height="4096" fill=${o}/>`:A}
        ${s}
      </g>
      ${cp(e,t,i,`none`,r)}
      ${sp(e,t.min,p,n)??A}
      ${sp(e,t.max,p,n)??A}
      ${a}
    `}let f,p,m;return t.state===jo.hinted?(f=`var(--instrument-frame-tertiary-color)`,m=`var(--instrument-frame-primary-color)`,p=Eo.regular):t.state===jo.regular?(f=`var(--instrument-regular-secondary-color)`,m=`var(--instrument-frame-primary-color)`,p=Eo.regular):(f=`var(--instrument-enhanced-secondary-color)`,m=f,p=Eo.regular),k`
    ${cp(e,t,i,m,f)}
    ${sp(e,t.min,p,n)??A}
    ${sp(e,t.max,p,n)??A}
    ${a}
  `}function up(e){return!e.advices||!e.advices.length?[]:Hf(e.advices,e.setpoint).map(t=>lp(e,t))}function dp(e){let t=Df(e),n=Tf({orientation:e.orientation,length:e.length},t),r=e.orientation===`vertical`?n.width:n.height;return{side:e.side,thickness:r}}function fp(e){let t=Sf(e),n=t===e.barThickness?e:{...e,barThickness:t};return{barContainer:ep(n),barFill:tp(n),scaleBackground:np(n),tickmarks:Qf(n),labels:$f(n),adviceOverlays:up(n),currentValueDot:op(n),setpoint:ap(n)}}var pp={CANVAS_PADDING:32,CHART_WIDTH:256,MIN_CHART_WIDTH:48,MIN_HEIGHT_WITH_LABELS:192},$=class extends as(j,{defaultDeadband:1}){constructor(...e){super(...e),this.minValue=0,this.maxValue=100,this.reverse=!1,this.width=320,this.paddingLeft=pp.CANVAS_PADDING,this.paddingRight=pp.CANVAS_PADDING,this.side=ff.bottom,this.fixedAspectRatio=!1,this.scaleReferenceSize=384,this._scale=1,this._resizeController=new rl(this,{callback:e=>{if(!this.fixedAspectRatio)return;let t=e[0];if(!t)return;let n=t.contentRect.width;this._scale=Ef({orientation:df.horizontal,containerMainAxisSize:n,scaleReferenceSize:this.scaleReferenceSize}),this.reportDimensions()}}),this.hasScale=!0,this.showLabels=!0,this.showMainTickmarkLabels=!1,this.hasBar=!1,this.scaleBackground=!1,this.barContainerStyle=void 0,this.barThickness=24,this.tickThickness=24,this.labelThickness=60,this.mainTickmarks=[],this.primaryTickmarkInterval=void 0,this.secondaryTickmarkInterval=void 0,this.tertiaryTickmarkInterval=void 0,this.scaleType=pf.regular,this.frameStyle=_i.regular,this.borderRadiusPosition=void 0,this.instrumentMode=!1,this.borderRadius=void 0,this._borderRadiusResizeController=new rl(this,{callback:()=>{this.instrumentMode||this._refreshBorderRadiusFromCssVar()}}),this.priority=W.regular,this.fillMode=mf.fill,this.fillMin=void 0,this.fillMax=void 0,this.value=void 0,this.state=gi.active,this.advicePosition=hf.inner,this.advices=[],this.highlightCurrentValue=!1}render(){let e=this.fixedAspectRatio?this.scaleReferenceSize:this.width,t={orientation:df.horizontal,side:this.side,length:e,paddingStart:this.paddingLeft,paddingEnd:this.paddingRight,minValue:this.minValue,maxValue:this.maxValue,reverse:this.reverse,hasScale:this.hasScale,labels:this.showLabels,mainTickmarkLabels:this.showMainTickmarkLabels,hasBar:this.hasBar,scaleBackground:this.scaleBackground,barContainerStyle:this.barContainerStyle,barThickness:this.barThickness,tickThickness:this.tickThickness,labelThickness:this.labelThickness,borderRadius:this._getEffectiveBorderRadius(),mainTickmarks:this.mainTickmarks,primaryTickmarkInterval:this.primaryTickmarkInterval,secondaryTickmarkInterval:this.secondaryTickmarkInterval,tertiaryTickmarkInterval:this.tertiaryTickmarkInterval,scaleType:this.scaleType,frameStyle:this.frameStyle,borderRadiusPosition:this.borderRadiusPosition,priority:this.priority,setpointOverride:this.setpointOverride,fillMode:this.fillMode,fillMin:this.fillMin,fillMax:this.fillMax,value:this.value,setpoint:this.setpoint,newSetpoint:this.newSetpoint,atSetpoint:this.atSetpoint,autoAtSetpoint:this.autoAtSetpoint,autoAtSetpointDeadband:this.autoAtSetpointDeadband,setpointAtZeroDeadband:this.setpointAtZeroDeadband,animateSetpoint:this.animateSetpoint,departingNewSetpoint:this.departingNewSetpoint,state:this.state,touching:this.touching,advicePosition:this.advicePosition,advices:this.advices,fixedAspectRatio:this.fixedAspectRatio,instrumentMode:this.instrumentMode,highlightCurrentValue:this.highlightCurrentValue},n=Df(wf(t)),r=fp(t),i=Tf({orientation:t.orientation,length:e},n),a=this.fixedAspectRatio?`xMidYMid meet`:`none`;return O`
      <svg
        width=${this.fixedAspectRatio?`100%`:`${this.width}px`}
        height=${this.fixedAspectRatio?`100%`:`${i.height}px`}
        viewBox="${i.x} ${i.y} ${i.width} ${i.height}"
        preserveAspectRatio="${a}"
        style="--scale: ${this.fixedAspectRatio?this._scale:1};"
        part="svg"
      >
        ${r.barContainer} ${r.barFill} ${r.scaleBackground}
        ${r.tickmarks} ${r.labels} ${r.adviceOverlays}
        ${r.currentValueDot} ${r.setpoint}
      </svg>
    `}updated(e){super.updated(e),e.has(`scaleType`)&&this._refreshBorderRadiusFromCssVar(),e.has(`fixedAspectRatio`)&&(this.fixedAspectRatio?(this._applyFixedAspectRatioStyles(),this._updateScaleFromCurrentSize()):(this._removeFixedAspectRatioStyles(),this._scale=1)),e.has(`scaleReferenceSize`)&&this.fixedAspectRatio&&this._updateScaleFromCurrentSize();let t=e.has(`side`)||e.has(`showLabels`)||e.has(`showMainTickmarkLabels`)||e.has(`hasScale`)||e.has(`hasBar`)||e.has(`barThickness`)||e.has(`tickThickness`)||e.has(`labelThickness`)||e.has(`scaleType`)||e.has(`borderRadiusPosition`)||e.has(`borderRadius`)||e.has(`advices`)||e.has(`advicePosition`)||this.setpointPresenceChanged(e);(!this.fixedAspectRatio||t)&&this.reportDimensions()}reportDimensions(){let e=Sf({hasBar:this.hasBar,barThickness:this.barThickness,borderRadius:this._getEffectiveBorderRadius(),scaleType:this.scaleType}),t=this.fixedAspectRatio?this.scaleReferenceSize:this.width,n=dp({orientation:df.horizontal,side:this.side,hasBar:this.hasBar,hasScale:this.hasScale,labels:this.showLabels,barThickness:e,tickThickness:this.tickThickness,labelThickness:this.labelThickness,length:t,scaleType:this.scaleType,advicePosition:this.advicePosition,hasAdvice:!!this.advices&&this.advices.length>0,hasSetpoint:this.setpoint!==void 0||this.newSetpoint!==void 0||this.departingNewSetpoint!==void 0}),r=this.fixedAspectRatio?{...n,thickness:Math.round(n.thickness*this._scale)}:n;this.dispatchEvent(new CustomEvent(`scale-dimensions-changed`,{detail:r,bubbles:!0}))}createRenderRoot(){return this}connectedCallback(){super.connectedCallback(),this.instrumentMode||(this._refreshBorderRadiusFromCssVar(),this._startBorderRadiusObserver()),this.fixedAspectRatio&&this._applyFixedAspectRatioStyles()}disconnectedCallback(){this._borderRadiusObserver?.disconnect(),this._borderRadiusObserver=void 0,super.disconnectedCallback()}_startBorderRadiusObserver(){this._borderRadiusObserver?.disconnect(),this._borderRadiusObserver=yf(this,()=>this._refreshBorderRadiusFromCssVar())}_applyFixedAspectRatioStyles(){this.style.display=`block`,this.style.width=`100%`,this.style.height=`auto`}_removeFixedAspectRatioStyles(){this.style.display=``,this.style.width=``,this.style.height=``}_updateScaleFromCurrentSize(){requestAnimationFrame(()=>{let e=this.clientWidth;e>0&&(this._scale=Ef({orientation:df.horizontal,containerMainAxisSize:e,scaleReferenceSize:this.scaleReferenceSize}),this.requestUpdate(),this.reportDimensions())})}_refreshBorderRadiusFromCssVar(){if(this.instrumentMode)return;let e=vf(this,this.scaleType);if(this._computedBorderRadius!==e&&(this._computedBorderRadius=e),this.fixedAspectRatio){let e=this.getBoundingClientRect();e.width>0&&(this._scale=Ef({orientation:df.horizontal,containerMainAxisSize:e.width,scaleReferenceSize:this.scaleReferenceSize}),this.reportDimensions())}}_getEffectiveBorderRadius(){return this.instrumentMode?this.borderRadius===void 0?this.scaleType===pf.condensed?4:8:this.borderRadius:this._computedBorderRadius??(this.scaleType===pf.condensed?4:8)}};N([P({type:Number})],$.prototype,`minValue`,void 0),N([P({type:Number})],$.prototype,`maxValue`,void 0),N([P({type:Boolean})],$.prototype,`reverse`,void 0),N([P({type:Number})],$.prototype,`width`,void 0),N([P({type:Number})],$.prototype,`paddingLeft`,void 0),N([P({type:Number})],$.prototype,`paddingRight`,void 0),N([P({type:String})],$.prototype,`side`,void 0),N([P({type:Boolean})],$.prototype,`fixedAspectRatio`,void 0),N([P({type:Number})],$.prototype,`scaleReferenceSize`,void 0),N([ze()],$.prototype,`_scale`,void 0),N([P({type:Boolean,attribute:!1})],$.prototype,`hasScale`,void 0),N([P({type:Boolean,attribute:!1})],$.prototype,`showLabels`,void 0),N([P({type:Boolean})],$.prototype,`showMainTickmarkLabels`,void 0),N([P({type:Boolean})],$.prototype,`hasBar`,void 0),N([P({type:Boolean})],$.prototype,`scaleBackground`,void 0),N([P({type:String})],$.prototype,`barContainerStyle`,void 0),N([P({type:Number})],$.prototype,`barThickness`,void 0),N([P({type:Number})],$.prototype,`tickThickness`,void 0),N([P({type:Number})],$.prototype,`labelThickness`,void 0),N([P({type:Array,attribute:!1})],$.prototype,`mainTickmarks`,void 0),N([P({type:Number})],$.prototype,`primaryTickmarkInterval`,void 0),N([P({type:Number})],$.prototype,`secondaryTickmarkInterval`,void 0),N([P({type:Number})],$.prototype,`tertiaryTickmarkInterval`,void 0),N([P({type:String})],$.prototype,`scaleType`,void 0),N([P({type:String})],$.prototype,`frameStyle`,void 0),N([P({type:String})],$.prototype,`borderRadiusPosition`,void 0),N([P({type:Boolean})],$.prototype,`instrumentMode`,void 0),N([P({type:Number})],$.prototype,`borderRadius`,void 0),N([ze()],$.prototype,`_computedBorderRadius`,void 0),N([P({type:String})],$.prototype,`priority`,void 0),N([P({type:String})],$.prototype,`fillMode`,void 0),N([P({type:Number})],$.prototype,`fillMin`,void 0),N([P({type:Number})],$.prototype,`fillMax`,void 0),N([P({type:Number})],$.prototype,`value`,void 0),N([P({type:String})],$.prototype,`state`,void 0),N([P({type:String})],$.prototype,`advicePosition`,void 0),N([P({type:Array,attribute:!1})],$.prototype,`advices`,void 0),N([P({type:Boolean})],$.prototype,`highlightCurrentValue`,void 0),$=N([M(`obc-bar-horizontal`)],$);var mp=o`* {
  -webkit-tap-highlight-color: transparent;
}

* {
  box-sizing: border-box;
}

:host {
  display: block;
  user-select: none;
}

.grid-container {
  display: grid;
  height: 100%;
  grid-template-columns: repeat(var(--grid-columns, 1), auto);
  align-content: start;
  grid-template-rows: min-content min-content 1fr;
}

.grid-container.has-selection-column {
    grid-template-columns:
      var(
        --selection-column-width,
        var(--menu-navigation-components-table-item-touch-target-size)
      )
      repeat(var(--grid-columns-rest, 1), minmax(0, 1fr));
  }

.grid-container .grid-header {
    grid-row: 1;
    display: grid;
    grid-column: 1/-1;
    grid-template-columns: subgrid;
    padding: 0 var(--menu-navigation-components-table-header-row-margin);
  }

.grid-container .grid-header .selection-header {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0;
    min-width: var(
      --selection-column-width,
      var(--menu-navigation-components-table-item-touch-target-size)
    );
    min-height: var(
      --menu-navigation-components-table-header-item-touch-target-size
    );
  }

.grid-container .grid-header-divider {
    grid-row: 2;
    grid-column: 1/-1;
    margin: 0 8px;
    border-bottom: 1px solid var(--border-divider-color);
  }

.grid-container .grid-column-divider {
    grid-row: 1/-1;
    width: 1px;
    background: var(--border-divider-color);
    height: 100%;
    right: 0;
    margin-left: auto;
    z-index: 1;
    pointer-events: none;
  }

.grid-container {

  --offset: calc(
    (
        var(--obc-scrollbar-touch-target-size) -
          var(--obc-scrollbar-visual-target-size)
      ) /
      2
  );
}

.grid-container ::-webkit-scrollbar {
    width: var(--obc-scrollbar-touch-target-size);
    height: var(--obc-scrollbar-touch-target-size);
  }

.grid-container ::-webkit-scrollbar-track-piece {
    border: var(--offset) solid transparent;
    border-radius: 9999px;
    background-color: var(--indent-enabled-background-color);
    margin-top: calc(-1 * var(--offset));
    margin-bottom: calc(-1 * var(--offset));
    box-sizing: border-box;
    background-clip: content-box;
  }

.grid-container ::-webkit-scrollbar-track-piece:vertical:start {
    border-bottom-width: 0;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
  }

.grid-container ::-webkit-scrollbar-track-piece:vertical:end {
    border-top-width: 0;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }

.grid-container ::-webkit-scrollbar-track-piece:hover {
    outline-color: var(--indent-hover-border-color);
    background-color: var(--indent-hover-background-color);
  }

.grid-container ::-webkit-scrollbar-track-piece:active {
    outline-color: var(--indent-pressed-border-color);
    background-color: var(--indent-pressed-background-color);
  }

.grid-container ::-webkit-scrollbar-thumb {
    border: calc(var(--offset) + 1px) solid transparent;
    outline: 1px solid var(--obc-scrollbar-thumb-border-color);
    outline-offset: calc(-1 * var(--offset) - 1px);
    background-clip: content-box;
    border-radius: 9999px;
    background-color: var(--obc-scrollbar-thumb-background-color);
    min-height: calc(var(--obc-scrollbar-touch-target-size) * 1.5);
  }

.grid-container ::-webkit-scrollbar-thumb:hover {
    outline-color: var(--obc-scrollbar-thumb-hover-border-color);
    background-color: var(--obc-scrollbar-thumb-hover-background-color);
  }

.grid-container ::-webkit-scrollbar-thumb:active {
    outline-color: var(--obc-scrollbar-thumb-active-border-color);
    background-color: var(--obc-scrollbar-thumb-active-background-color);
  }

.grid-container ::-webkit-scrollbar-button:start:decrement,.grid-container ::-webkit-scrollbar-button:end:increment {
    display: var(--obc-scrollbar-button-display);
    height: var(--obc-scrollbar-button-size);
    width: var(--obc-scrollbar-button-size);
    box-sizing: border-box;
    background-clip: content-box;
    background-repeat: no-repeat;
    background-position: center;
    border: var(--obc-scrollbar-button-margin) solid transparent;
    border-radius: var(--obc-scrollbar-button-radius);
    background-clip: padding-box;
    background-color: var(--flat-enabled-background-color);
  }

.grid-container ::-webkit-scrollbar-button:start:decrement:hover,.grid-container ::-webkit-scrollbar-button:end:increment:hover {
    background-color: var(--flat-hover-background-color);
  }

.grid-container ::-webkit-scrollbar-button:start:decrement:active,.grid-container ::-webkit-scrollbar-button:end:increment:active {
    background-color: var(--flat-pressed-background-color);
  }

.grid-container ::-webkit-scrollbar-button:vertical:start:decrement {
    background-image: var(--icon-02-chevron-up);
  }

.grid-container ::-webkit-scrollbar-button:vertical:end:increment {
    background-image: var(--icon-02-chevron-down);
  }

.grid-container .grid-body {
    grid-row: 3;
    overflow: auto;
    scrollbar-gutter: stable;
    display: grid;
    grid-column: 1/-1;
    grid-template-columns: subgrid;
    padding: 0 var(--menu-navigation-components-table-header-row-margin);
  }

.grid-container .grid-row {
    display: grid;
    grid-column: 1/-1;
    grid-template-columns: subgrid;
    min-height: var(--menu-navigation-components-table-item-touch-target-size);
    will-change: transform, opacity;
    position: relative;
    padding: 0;
  }

.striped:is(.grid-container .grid-row) {
      background: var(--container-section-color);
    }

:is(.grid-container .grid-row) {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

:is(.grid-container .grid-row):focus {
  outline: none;
}

.activated:is(.grid-container .grid-row) {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

:is(.grid-container .grid-row):hover {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

:is(.grid-container .grid-row):active {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

:is(.grid-container .grid-row):focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

:is(.grid-container .grid-row):disabled {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.disabled:is(.grid-container .grid-row) {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.grid-container .grid-row {
    border: 1px solid transparent;
    --flat-active-background-color: transparent;
  }

:is(.grid-container .grid-row):focus-visible {
    outline-offset: -2px;
  }

.grid-container .grid-row {
    border-radius: var(--global-border-radius-border-radius-base);
  }

.selected:is(.grid-container .grid-row) {
  border-color: var(--amplified-enabled-border-color);
  background-color: var(--amplified-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--amplified-enabled-border-color);
  --base-background-color: var(--amplified-enabled-background-color);
}

.selected:is(.grid-container .grid-row):focus {
  outline: none;
}

.selected.activated:is(.grid-container .grid-row) {
  border-color: var(--amplified-activated-border-color);
  background-color: var(--amplified-activated-background-color);
  --base-border-color: var(--amplified-activated-border-color);
  --base-background-color: var(--amplified-activated-background-color);
}

@media (hover:hover) {

.selected:is(.grid-container .grid-row):hover {
    border-color: color-mix(in srgb, var(--amplified-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--amplified-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.selected:is(.grid-container .grid-row):active {
  border-color: var(--amplified-pressed-border-color);
  background-color: var(--amplified-pressed-background-color);
}

.selected:is(.grid-container .grid-row):focus-visible {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.selected:is(.grid-container .grid-row):disabled {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

.selected.disabled:is(.grid-container .grid-row) {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

.selected-with-prev:is(.grid-container .grid-row) {
      border-top-color: transparent;
      border-top-left-radius: 0;
      border-top-right-radius: 0;
    }

.selected-with-next:is(.grid-container .grid-row) {
      border-bottom-color: transparent;
      border-bottom-left-radius: 0;
      border-bottom-right-radius: 0;
    }

.selected-with-next:is(.grid-container .grid-row) .grid-row-divider {
      display: none;
    }

.animating:is(.grid-container .grid-row) {
      pointer-events: none;
    }

:is(.grid-container .grid-row) .grid-cell {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: flex-start;
      padding: 0 var(--menu-navigation-components-table-item-padding-horizontal);
      min-height: 100%;
      min-width: var(--menu-navigation-components-table-item-touch-target-size);
      gap: var(--menu-navigation-components-table-item-label-spacing);
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-body-font-weight);
      font-size: var(--global-typography-ui-body-font-size);
      line-height: var(--global-typography-ui-body-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
      color: var(--on-flat-active-color);
    }

.selection:is(:is(.grid-container .grid-row) .grid-cell) {
        min-width: var(
          --selection-column-width,
          var(--menu-navigation-components-table-item-touch-target-size)
        );
        width: var(
          --selection-column-width,
          var(--menu-navigation-components-table-item-touch-target-size)
        );
        max-width: var(
          --selection-column-width,
          var(--menu-navigation-components-table-item-touch-target-size)
        );
        padding: 0;
      }

.neutral:is(:is(.grid-container .grid-row) .grid-cell) {
        color: var(--on-flat-neutral-color);
      }

.vertical:is(:is(.grid-container .grid-row) .grid-cell) {
        flex-direction: column;
        align-items: flex-start;
        justify-content: flex-start;
        gap: 0;
        padding-top: var(--menu-navigation-components-table-item-label-spacing);
        padding-bottom: var(
          --menu-navigation-components-table-item-label-spacing
        );
      }

.align-center:is(:is(.grid-container .grid-row) .grid-cell) {
        justify-content: center;
      }

.align-right:is(:is(.grid-container .grid-row) .grid-cell) {
        justify-content: flex-end;
      }

.align-left:is(:is(.grid-container .grid-row) .grid-cell) {
        justify-content: flex-start;
      }

.no-wrap:is(:is(.grid-container .grid-row) .grid-cell) > * {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }

.no-wrap:is(:is(.grid-container .grid-row) .grid-cell) {
        width: 100%;
      }

.no-wrap:is(:is(.grid-container .grid-row) .grid-cell) .title {
          flex-shrink: 0;
        }

.no-wrap:is(:is(.grid-container .grid-row) .grid-cell) .text {
          flex-shrink: 10000;
        }

:is(:is(.grid-container .grid-row) .grid-cell) .icon {
        width: var(--menu-navigation-components-table-item-icon-size);
        height: var(--menu-navigation-components-table-item-icon-size);
        flex-shrink: 0;
      }

/* ---- Hierarchy ---- */

/*
       * Indent gutter for a hierarchical row. One step per level plus one for
       * the chevron itself, so a leaf and a group at the same level align.
       */

:is(:is(.grid-container .grid-row) .grid-cell) .row-expander {
        --row-indent-step: var(
          --menu-navigation-components-table-item-icon-size
        );
        /* Depth of this row; the row's inline style overrides it. */
        --row-level: 0;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        flex-shrink: 0;
        align-self: stretch;
        width: calc((var(--row-level) + 1) * var(--row-indent-step));
      }

:is(:is(.grid-container .grid-row) .grid-cell) .row-expander .chevron {
        display: flex;
        align-items: center;
        justify-content: center;
        /* Pointer target floor, and the gutter is only one step wide. */
        min-width: var(--row-indent-step);
        min-height: var(--row-indent-step);
        align-self: stretch;
        color: var(--on-flat-neutral-color);
        transition: transform 100ms ease-in-out;
      }

:is(:is(.grid-container .grid-row) .grid-cell) .row-expander .chevron.expanded {
        transform: rotate(90deg);
      }

@media (prefers-reduced-motion: reduce) {
        :is(:is(.grid-container .grid-row) .grid-cell) .row-expander .chevron {
          transition: none;
        }
      }

.large-icon:is(:is(.grid-container .grid-row) .grid-cell) .icon {
        min-width: var(--menu-navigation-components-table-item-icon-size-large);
        min-height: var(
          --menu-navigation-components-table-item-icon-size-large
        );
        width: fit-content;
        height: fit-content;
        display: grid;
      }

:is(:is(.grid-container .grid-row) .grid-cell) .title {
        font-family: var(--global-typography-font-family);
        font-weight: var(--global-typography-ui-body-active-font-weight);
        font-size: var(--global-typography-ui-body-active-font-size);
        line-height: var(--global-typography-ui-body-active-line-height);
        font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
      }

.button:is(:is(.grid-container .grid-row) .grid-cell) obc-button {
          width: 100%;
        }

.checkbox:is(:is(.grid-container .grid-row) .grid-cell) {
        min-width: 0;
      }

.checkbox:is(:is(.grid-container .grid-row) .grid-cell) {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
        background: transparent;
        --flat-active-background-color: transparent;
        --flat-hover-background-color: transparent;
}

.horizontal-bar:is(:is(.grid-container .grid-row) .grid-cell) {
        padding: 0
          var(--menu-navigation-components-table-item-padding-horizontal);
      }

.horizontal-bar:is(:is(.grid-container .grid-row) .grid-cell) obc-bar-horizontal {
        display: block;
        width: 100%;
        height: 100%;
      }

.tags:is(:is(.grid-container .grid-row) .grid-cell) {
        gap: calc(
          var(--menu-navigation-components-table-item-badge-spacing) * 2
        );
      }

.tags:is(:is(.grid-container .grid-row) .grid-cell) .tag-overflow {
          font-family: var(--global-typography-font-family);
          font-weight: var(--global-typography-ui-label-font-weight);
          font-size: var(--global-typography-ui-label-font-size);
          line-height: var(--global-typography-ui-label-line-height);
          font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
          color: var(--on-flat-neutral-color);
          white-space: nowrap;
          margin: 0;
        }

.tags.wrap:is(:is(.grid-container .grid-row) .grid-cell) {
          flex-wrap: wrap;
          align-content: center;
        }

.grid-container .grid-row-divider {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    margin: 0 8px;
    border-radius: 100px;
    background: var(--border-divider-color);
    height: 1px;
    margin-bottom: -1.5px;
    z-index: -1;
  }
`,hp=class extends j{constructor(...e){super(...e),this.useCssColor=!1,this.icon=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M6 14.0002L7.41 15.4102L12 10.8302L16.59 15.4102L18 14.0002L12 8.00016L6 14.0002Z" fill="currentColor"/>
</svg>
`,this.iconCss=k`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M6 14.0002L7.41 15.4102L12 10.8302L16.59 15.4102L18 14.0002L12 8.00016L6 14.0002Z" style="fill: var(--element-active-color)"/>
</svg>
`}render(){return O`
      <div class="wrapper">${this.useCssColor?this.iconCss:this.icon}</div>
    `}},gp=(hp.styles=o`
    .wrapper {
      height: 100%;
      width: 100%;
      line-height: 0;
    }
    .wrapper > * {
      height: 100%;
      width: 100%;
    }
  `,hp);N([P({type:Boolean})],gp.prototype,`useCssColor`,void 0),gp=N([M(`obi-chevron-up-google`)],gp);var _p=o`* {
  -webkit-tap-highlight-color: transparent;
}

* {
  box-sizing: border-box;
}

:host {
  display: flex;
  width: 100%;
}

.wrapper {
  width: 100%;
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: stretch;
  user-select: none;
  -webkit-user-select: none;
  appearance: none;
  border: none;
  background: transparent;
  font-family: var(--global-typography-font-family);
  font-weight: var(--global-typography-ui-overline-font-weight);
  font-size: var(--global-typography-ui-overline-font-size);
  line-height: var(--global-typography-ui-overline-line-height);
  letter-spacing: var(--global-typography-ui-overline-letter-spacing);
  font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  height: var(--menu-navigation-components-table-header-item-touch-target-size);
  padding: 0
    var(--menu-navigation-components-table-header-item-margin-horizontal);

  color: var(--element-neutral-color);
}

.wrapper.sortable {
  cursor: pointer;
}

.wrapper.sortable:focus {
  outline: none;
}

.wrapper.sortable .visible-wrapper {
  border-color: var(--flat-enabled-border-color);
  background-color: var(--flat-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--flat-enabled-border-color);
  --base-background-color: var(--flat-enabled-background-color);
}

.wrapper.sortable.activated .visible-wrapper {
  border-color: var(--flat-activated-border-color);
  background-color: var(--flat-activated-background-color);
  --base-border-color: var(--flat-activated-border-color);
  --base-background-color: var(--flat-activated-background-color);
}

@media (hover:hover) {

.wrapper.sortable:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--flat-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--flat-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.sortable:active .visible-wrapper {
  border-color: var(--flat-pressed-border-color);
  background-color: var(--flat-pressed-background-color);
}

.wrapper.sortable:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.sortable:disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.sortable.disabled .visible-wrapper {
  border-color: var(--flat-disabled-border-color);
  background-color: var(--flat-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-flat-disabled-color) !important;
}

.wrapper.sortable:disabled {
  cursor: not-allowed;
}

.wrapper.sortable.disabled {
  cursor: not-allowed;
}

.wrapper.checked {
  cursor: pointer;
}

.wrapper.checked:focus {
  outline: none;
}

.wrapper.checked .visible-wrapper {
  border-color: var(--amplified-enabled-border-color);
  background-color: var(--amplified-enabled-background-color);
  border-width: 1px;
  border-style: solid;
  cursor: pointer;
  --base-border-color: var(--amplified-enabled-border-color);
  --base-background-color: var(--amplified-enabled-background-color);
}

.wrapper.checked.activated .visible-wrapper {
  border-color: var(--amplified-activated-border-color);
  background-color: var(--amplified-activated-background-color);
  --base-border-color: var(--amplified-activated-border-color);
  --base-background-color: var(--amplified-activated-background-color);
}

@media (hover:hover) {

.wrapper.checked:hover .visible-wrapper {
    border-color: color-mix(in srgb, var(--amplified-hover-border-color) calc(var(--obc-can-hover) * 100%), var(--base-border-color));
    background-color: color-mix(in srgb, var(--amplified-hover-background-color) calc(var(--obc-can-hover) * 100%), var(--base-background-color));
  }
}

.wrapper.checked:active .visible-wrapper {
  border-color: var(--amplified-pressed-border-color);
  background-color: var(--amplified-pressed-background-color);
}

.wrapper.checked:focus-visible .visible-wrapper {
  outline-color: var(--border-focus-color);
  outline-width: var(--global-size-spacing-border-weight-focusframe);
  outline-style: solid;
  border-color: var(--container-global-color);
  z-index: 1;
}

.wrapper.checked:disabled .visible-wrapper {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

.wrapper.checked.disabled .visible-wrapper {
  border-color: var(--amplified-disabled-border-color);
  background-color: var(--amplified-disabled-background-color);
  cursor: not-allowed;
  color: var(--on-amplified-disabled-color) !important;
}

.wrapper.checked:disabled {
  cursor: not-allowed;
}

.wrapper.checked.disabled {
  cursor: not-allowed;
}

.wrapper.checked {
  color: var(--instrument-enhanced-secondary-color);
}

.wrapper.style-narrow {
  padding: 0;
  height: var(--menu-navigation-components-table-header-item-icon-size);
}

.wrapper.style-narrow .visible-wrapper {
    border-radius: 0;
    border-width: 0;
    min-height: var(--menu-navigation-components-table-header-item-icon-size);
  }

.wrapper .visible-wrapper {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  min-height: var(
    --menu-navigation-components-table-header-item-visual-target-size
  );
  border-radius: var(
    --menu-navigation-components-table-header-item-border-radius
  );
  padding: 0
    var(--menu-navigation-components-table-header-item-padding-horizontal);
}

.wrapper .label {
  padding: 0 var(--menu-navigation-components-table-header-item-label-spacing);
  white-space: nowrap;
  flex-grow: 1;
  text-align: left;
}

/* Icon containers */
.wrapper .leading,
.wrapper .trailing,
.wrapper .sort-icon {
  display: inline-flex;
  align-items: center;
}

.wrapper.has-leading-icon .leading,
.wrapper .sort-icon {
  width: var(--menu-navigation-components-table-header-item-icon-size);
  height: var(--menu-navigation-components-table-header-item-icon-size);
}

/* Disabled text color alignment */
.wrapper:disabled .label,
.wrapper.disabled .label {
  color: var(--element-disabled-color);
}

.divider {
  display: flex;
  height: 24px;
  align-items: center;
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  margin: auto;
  width: 1px;
  background-color: var(--border-divider-color);
}
`,vp,yp=function(e){return e.Regular=`Regular`,e.IconOnly=`IconOnly`,e.Narrow=`Narrow`,e}({}),bp=(vp=class extends j{constructor(...e){super(...e),this.type=`Regular`,this.disabled=!1,this.hasLeadingIcon=!1,this.sortDirection=`none`,this.showDivider=!1,this.checked=!1,this.sortable=!1}render(){let e={wrapper:!0,[`style-${(this.type??`Regular`).toLowerCase()}`]:!0,sortable:this.sortable,disabled:this.disabled,"has-leading-icon":this.hasLeadingIcon,"sorted-asc":this.sortDirection===`asc`,"sorted-desc":this.sortDirection===`desc`,checked:this.checked},t=this.sortable?Ot`button`:Ot`div`;return L`
      <${t}
        class=${F(e)}
        ?disabled=${this.disabled}
        part="wrapper"
      >
        <div class="visible-wrapper" part="visible-wrapper">
          ${this.hasLeadingIcon?L`<span class="leading" part="leading"
                  ><slot name="leading-icon"></slot
                ></span>`:A}
          ${this.type===`IconOnly`?A:L`<span class="label" part="label"><slot></slot></span>`}
          ${this.sortable?L`<span class="trailing sort-icon" part="sort-icon"
                  >${this._renderSortIcon()}</span
                >`:A}
        </div>
        ${this.showDivider?L`<div class="divider" part="divider"></div>`:A}
      </${t}>
    `}_renderSortIcon(){switch(this.sortDirection){case`asc`:return L`<obi-chevron-up-google></obi-chevron-up-google>`;case`desc`:return L`<obi-chevron-down-google></obi-chevron-down-google>`;default:return A}}},vp.styles=a(_p),vp);N([P({type:String})],bp.prototype,`type`,void 0),N([P({type:Boolean})],bp.prototype,`disabled`,void 0),N([P({type:Boolean})],bp.prototype,`hasLeadingIcon`,void 0),N([P({type:String})],bp.prototype,`sortDirection`,void 0),N([P({type:Boolean})],bp.prototype,`showDivider`,void 0),N([P({type:Boolean})],bp.prototype,`checked`,void 0),N([P({type:Boolean})],bp.prototype,`sortable`,void 0),bp=N([M(`obc-table-header-item`)],bp);var xp=o`* {
  -webkit-tap-highlight-color: transparent;
}

:host {
  display: inline-block;
}

.wrapper {
  box-sizing: border-box;
  display: inline-flex;
  align-items: center;
  gap: var(--ui-components-tag-label-spacing-large);
  height: var(--ui-components-tag-visual-target);
  padding: var(--global-size-spacing-target-padding)
    var(--ui-components-tag-padding-horizontal);
  border: var(--ui-components-badge-icon-size-flat-border-weight) solid
    var(--indent-enabled-border-color);
  border-radius: var(--ui-components-tag-border-radius);
  background: var(--indent-enabled-background-color);
}

.wrapper .tag-icon-wrapper {
    display: flex;
    width: var(--ui-components-tag-icon-size);
    height: var(--ui-components-tag-icon-size);
    max-width: calc(
      var(--ui-components-tag-visual-target) -
        var(--global-size-spacing-target-padding) * 2 -
        var(--ui-components-badge-icon-size-flat-border-weight) * 2
    );
    max-height: calc(
      var(--ui-components-tag-visual-target) -
        var(--global-size-spacing-target-padding) * 2 -
        var(--ui-components-badge-icon-size-flat-border-weight) * 2
    );
  }

:is(.wrapper .tag-icon-wrapper) ::slotted(*) {
      display: block;
      width: 100%;
      height: 100%;
    }

.wrapper .tag-label-container {
    display: flex;
  }

.wrapper .tag-label {
    font-family: var(--global-typography-font-family);
    font-weight: var(--global-typography-ui-label-font-weight);
    font-size: var(--global-typography-ui-label-font-size);
    line-height: var(--global-typography-ui-label-line-height);
    font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
  }

.wrapper.size-large {
    height: var(--ui-components-tag-visual-target-large);
    padding: var(--global-size-spacing-target-padding)
      var(--ui-components-tag-padding-horizontal-large);
  }

.wrapper.size-large .tag-icon-wrapper {
      width: var(--ui-components-tag-icon-size-large);
      height: var(--ui-components-tag-icon-size-large);
      max-width: calc(
        var(--ui-components-tag-visual-target-large) -
          var(--global-size-spacing-target-padding) * 2 -
          var(--ui-components-badge-icon-size-flat-border-weight) * 2
      );
      max-height: calc(
        var(--ui-components-tag-visual-target-large) -
          var(--global-size-spacing-target-padding) * 2 -
          var(--ui-components-badge-icon-size-flat-border-weight) * 2
      );
    }

.wrapper.size-large .tag-label {
      font-family: var(--global-typography-font-family);
      font-weight: var(--global-typography-ui-body-font-weight);
      font-size: var(--global-typography-ui-body-font-size);
      line-height: var(--global-typography-ui-body-line-height);
      font-feature-settings:
    "liga" off,
    "clig" off,
    "ss04" on;
    }

.wrapper.color-gray {
    color: var(--on-indent-active-color);
    background: var(--indent-enabled-background-color);
    border-color: var(--indent-enabled-border-color);
  }

.wrapper.color-gray .tag-icon-wrapper {
      color: var(--on-indent-neutral-color);
    }

.wrapper.color-blue {
    color: var(--base-blue-600);
    background-color: var(--base-blue-050);
    border-color: var(--base-blue-100);
  }

.wrapper.color-blue .tag-icon-wrapper {
      color: var(--base-blue-500);
    }

.wrapper.color-cyan {
    color: var(--base-cyan-600);
    background-color: var(--base-cyan-050);
    border-color: var(--base-cyan-100);
  }

.wrapper.color-cyan .tag-icon-wrapper {
      color: var(--base-cyan-500);
    }

.wrapper.color-teal {
    color: var(--base-teal-600);
    background-color: var(--base-teal-050);
    border-color: var(--base-teal-100);
  }

.wrapper.color-teal .tag-icon-wrapper {
      color: var(--base-teal-500);
    }

.wrapper.color-green {
    color: var(--base-mint-600);
    background-color: var(--base-mint-050);
    border-color: var(--base-mint-100);
  }

.wrapper.color-green .tag-icon-wrapper {
      color: var(--base-mint-500);
    }

.wrapper.color-yellow {
    color: var(--base-yellow-600);
    background-color: var(--base-yellow-050);
    border-color: var(--base-yellow-100);
  }

.wrapper.color-yellow .tag-icon-wrapper {
      color: var(--base-yellow-500);
    }

.wrapper.color-orange {
    color: var(--base-orange-600);
    background-color: var(--base-orange-050);
    border-color: var(--base-orange-100);
  }

.wrapper.color-orange .tag-icon-wrapper {
      color: var(--base-orange-500);
    }

.wrapper.color-red {
    color: var(--base-red-600);
    background-color: var(--base-red-050);
    border-color: var(--base-red-100);
  }

.wrapper.color-red .tag-icon-wrapper {
      color: var(--base-red-500);
    }

.wrapper.color-purple {
    color: var(--base-purple-600);
    background-color: var(--base-purple-050);
    border-color: var(--base-purple-100);
  }

.wrapper.color-purple .tag-icon-wrapper {
      color: var(--base-purple-500);
    }

.wrapper.color-indigo {
    color: var(--base-indigo-600);
    background-color: var(--base-indigo-050);
    border-color: var(--base-indigo-100);
  }

.wrapper.color-indigo .tag-icon-wrapper {
      color: var(--base-indigo-500);
    }
`,Sp,Cp=function(e){return e.gray=`gray`,e.blue=`blue`,e.cyan=`cyan`,e.teal=`teal`,e.green=`green`,e.yellow=`yellow`,e.orange=`orange`,e.red=`red`,e.purple=`purple`,e.indigo=`indigo`,e}({}),wp=(Sp=class extends j{constructor(...e){super(...e),this.label=`Label`,this.color=`gray`,this.size=`regular`,this.hasIcon=!1}renderLeadingIcon(){return this.hasIcon?O`
      <div class="tag-icon-wrapper">
        <slot></slot>
      </div>
    `:A}render(){return O`
      <div
        class=${F({wrapper:!0,[`color-`+this.color]:!0,[`size-`+this.size]:!0})}
      >
        ${this.renderLeadingIcon()}
        <div class="tag-label-container">
          <span class="tag-label">${this.label}</span>
        </div>
      </div>
    `}},Sp.styles=a(xp),Sp);N([P({type:String})],wp.prototype,`label`,void 0),N([P({type:String})],wp.prototype,`color`,void 0),N([P({type:String})],wp.prototype,`size`,void 0),N([P({type:Boolean})],wp.prototype,`hasIcon`,void 0),wp=N([M(`obc-tag`)],wp);function*Tp(e,t){if(e!==void 0){let n=0;for(let r of e)yield t(r,n++)}}var Ep,Dp=function(e){return e.Regular=`regular`,e.Button=`button`,e.Checkbox=`checkbox`,e.Tag=`tag`,e.HorizontalBar=`horizontal-bar`,e}({}),Op=`button, a[href], input, select, textarea, [role="button"], [role="link"], [role="checkbox"]`;function kp(e,t){if(e.cssPart)return`${e.cssPart} ${t}`}var Ap=(Ep=class extends j{constructor(...e){super(...e),this.ariaLabel=null,this.data=[],this.columns=[],this.rowDivider=!1,this.narrowHeader=!1,this.showHeader=!0,this.striped=!1,this.selectable=!1,this.selectAllAriaLabel=`Select all rows`,this._sortByColumnIdx=void 0,this._sortDirection=`asc`,this._selectedRowIds=new Set,this._previousPositions=[],this._hasRenderedRows=!1}get hasHierarchy(){return this.data.some(e=>e.parentId!==void 0||(e.level??0)>0||e.expandable===!0)}sortWithinSiblings(e,t){let n=new Set(e.map(e=>e.id)),r=new Map,i=[];for(let t of e){let e=t.parentId;if(e!==void 0&&e!==t.id&&n.has(e)){let n=r.get(e)??[];n.push(t),r.set(e,n)}else i.push(t)}let a=[],o=new Set,s=e=>{for(let n of[...e].sort(t))o.has(n.id)||(o.add(n.id),a.push(n),s(r.get(n.id)??[]))};return s(i),s(e.filter(e=>!o.has(e.id))),a}get sortedData(){if(this._sortByColumnIdx===void 0)return this.data;let e=this.columns[this._sortByColumnIdx];if(e===void 0)return console.warn(`Sort by column is undefined`),this.data;let t=this._sortDirection,n=(n,r)=>{let i=n[e.key],a=r[e.key];return t===`asc`?e.compareFunction(i,a,n,r):e.compareFunction(a,i,r,n)};if(this.hasHierarchy)return this.sortWithinSiblings(this.data,n);let r=[...this.data];return r.sort(n),r}_handleSortClick(e){if(!e.sortable)return;let t=this.columns.indexOf(e);t===this._sortByColumnIdx?this._sortDirection=this._sortDirection===`asc`?`desc`:`asc`:(this._sortByColumnIdx=t,this._sortDirection=`asc`)}_handleRowClick(e,t){let n=e.currentTarget;for(let t of e.composedPath()){if(t===n)break;if(t instanceof Element&&t.matches(Op))return}this.dispatchEvent(new CustomEvent(`row-click`,{detail:{row:t}}))}_handleExpandToggle(e,t){e.expandable&&this.dispatchEvent(new CustomEvent(`expand-toggle`,{detail:{rowId:e.id,expanded:t}}))}_renderRowExpander(e){return this.hasHierarchy?O`<span
      class="row-expander"
      style="--row-level: ${e.level??0}"
      aria-hidden="true"
    >
      ${e.expandable?O`<span
              class=${F({chevron:!0,expanded:e.expanded??!1})}
              @click=${t=>{t.preventDefault(),t.stopPropagation(),this._handleExpandToggle(e,!(e.expanded??!1))}}
            >
              <obi-chevron-right-google></obi-chevron-right-google>
            </span>`:A}
    </span>`:A}_focusFirstRow(){this.renderRoot.querySelector(`button[role="row"].grid-row`)?.focus()}_focusLeftHeaderItem(){this._focusHeaderByIndex(0)}_focusHeaderByIndex(e){let t=Array.from(this.renderRoot.querySelectorAll(`.grid-header [role="columnheader"]`));if(t.length===0)return;let n=t[st(e,0,t.length-1)];(n.shadowRoot?.querySelector(`button`)??null??n).focus()}_handleHeaderKeyDown(e){let t=e.key;if(t===`ArrowDown`){this._focusFirstRow(),e.preventDefault(),e.stopPropagation();return}if(t!==`ArrowLeft`&&t!==`ArrowRight`)return;let n=Array.from(this.renderRoot.querySelectorAll(`.grid-header [role="columnheader"]`));if(n.length===0)return;let r=e.currentTarget,i=r?n.indexOf(r):-1;if(i===-1)return;let a=t===`ArrowRight`?Math.min(i+1,n.length-1):Math.max(i-1,0);a!==i&&(this._focusHeaderByIndex(a),e.preventDefault(),e.stopPropagation())}_handleRowKeyDown(e){let t=e.key;if(this.hasHierarchy&&(t===`ArrowRight`||t===`ArrowLeft`)&&this._handleRowExpandKey(e,t)||t!==`ArrowDown`&&t!==`ArrowUp`&&t!==`Home`&&t!==`End`)return;let n=e.currentTarget;if(!n)return;let r=Array.from(this.renderRoot.querySelectorAll(`button[role="row"].grid-row`)),i=r.indexOf(n);if(i===-1)return;let a=i;switch(t){case`ArrowDown`:a=Math.min(i+1,r.length-1);break;case`ArrowUp`:if(i===0){this._focusLeftHeaderItem(),e.preventDefault(),e.stopPropagation();return}a=Math.max(i-1,0);break;case`Home`:a=0;break;case`End`:a=r.length-1}a===i?(t===`Home`||t===`End`)&&(e.preventDefault(),e.stopPropagation()):(r[a]?.focus(),e.preventDefault(),e.stopPropagation())}_handleRowExpandKey(e,t){let n=e.currentTarget?.dataset.rowId,r=this.sortedData.find(e=>e.id===n);if(!r)return!1;let i=r.expanded??!1;if(t===`ArrowRight`&&r.expandable&&!i)this._handleExpandToggle(r,!0);else if(t===`ArrowLeft`&&r.expandable&&i)this._handleExpandToggle(r,!1);else if(t===`ArrowLeft`){let e=this.renderRoot.querySelector(`button[role="row"].grid-row[data-row-id="${CSS.escape(r.parentId??``)}"]`);if(!e)return!1;e.focus()}else return!1;return e.preventDefault(),e.stopPropagation(),!0}_getAllPositions(){let e=Array.from(this.renderRoot.querySelectorAll(`button[role="row"].grid-row`)),t=e[0];if(!t)return[];let n=t.getBoundingClientRect().height,r=getComputedStyle(t),i=parseFloat(r.height)/n;return e.map(e=>{let t=e.getBoundingClientRect();return{top:t.top*i,height:t.height*i,index:e.getAttribute(`data-row-id`)??``,element:e}})}_animateRowChanges(){let e=this._previousPositions,t=this._getAllPositions();t.forEach(t=>{let n=e.find(e=>e.index===t.index);n?t.element.style.transform=`translateY(${n.top-t.top}px)`:(t.element.style.transform=`translateY(-${t.height}px)`,t.element.style.opacity=`0`),t.element.style.transition=`none`,t.element.offsetHeight,t.element.style.transition=`transform 100ms ease-in-out, opacity 100ms ease-in-out`,t.element.style.transform=`translateY(0px)`,t.element.style.opacity=`1`}),this._previousPositions=t}willUpdate(e){if(e.has(`defaultSelectedRowIds`)&&this.selectedRowIds===void 0&&this._selectedRowIds.size===0&&(this._selectedRowIds=new Set(this.defaultSelectedRowIds??[])),e.has(`selectedRowIds`)&&this.selectedRowIds!==void 0&&(this._selectedRowIds=new Set(this.selectedRowIds)),e.has(`data`)){let e=new Set(this.data.map(e=>e.id));this._selectedRowIds.forEach(t=>{e.has(t)||this._selectedRowIds.delete(t)})}(e.has(`data`)||e.has(`_sortByColumnIdx`)||e.has(`_sortDirection`))&&(this._hasRenderedRows?this._updatePositions():this.updateComplete.then(()=>{this._hasRenderedRows=!0}))}updated(e){e.has(`columns`)&&(this._sortByColumnIdx=this.columns.findIndex(e=>`sortDirection`in e&&e.sortDirection!==void 0),this._sortByColumnIdx===-1?(this._sortByColumnIdx=void 0,this._sortDirection=`asc`):this._sortDirection=this.columns[this._sortByColumnIdx]?.sortDirection??`asc`),(e.has(`data`)||e.has(`_sortByColumnIdx`)||e.has(`_sortDirection`))&&this._hasRenderedRows&&this._animateRowChanges()}_updatePositions(){let e=this._getAllPositions();this._previousPositions=e}render(){let e=this.selectable?[{label:``,key:`__selection__`},...this.columns]:this.columns,t=this.selectable?Math.max(0,e.length-1):e.length;return O`
      <div
        class=${F({"grid-container":!0,"has-selection-column":this.selectable})}
        part="grid"
        style="
          --grid-columns: ${e.length};
          --grid-columns-rest: ${t};
          --selection-column-width: var(--menu-navigation-components-table-item-touch-target-size);
        "
        role=${this.hasHierarchy?`treegrid`:`table`}
        aria-label=${I(this.ariaLabel??void 0)}
      >
        ${this.showHeader?O`
                <div class="grid-header" role="row">
                  ${e.map(t=>{let n=this.selectable&&t.key===`__selection__`,r=e.indexOf(t)!==e.length-1,i=t.renderHeaderIcon?O`<span slot="leading-icon"
                          >${t.renderHeaderIcon()}</span
                        >`:A,a=this.columns.findIndex(e=>e.key===t.key),o=`sortable`in t&&t.sortable&&this._sortByColumnIdx===a?this._sortDirection:`none`,s=t.headerType??(this.narrowHeader?yp.Narrow:yp.Regular);return`sortable`in t&&t.sortable&&!n?O`<obc-table-header-item
                        role="columnheader"
                        class=${n?`selection-header`:``}
                        .showDivider=${r}
                        ?hasLeadingIcon=${i!==A}
                        .sortDirection=${o}
                        .sortable=${!0}
                        type=${s}
                        @click=${()=>this._handleSortClick(t)}
                        @keydown=${this._handleHeaderKeyDown}
                        >${i}${t.label}</obc-table-header-item
                      > `:n?O`<div
                          role="columnheader"
                          class=${F({"selection-header":!0})}
                          tabindex="0"
                          @keydown=${this._handleHeaderKeyDown}
                        >
                          <obc-checkbox
                            .status=${this._getSelectionStatus()}
                            .disabled=${!1}
                            aria-label=${this.selectAllAriaLabel}
                            @click=${e=>{e.preventDefault(),e.stopPropagation()}}
                            @change=${()=>this._toggleAllSelection()}
                          ></obc-checkbox>
                        </div>`:O`<obc-table-header-item
                        role="columnheader"
                        class=${n?`selection-header`:``}
                        .showDivider=${r}
                        ?hasLeadingIcon=${i!==A}
                        type=${s}
                        >${i}${t.label}</obc-table-header-item
                      >`})}
                </div>
                <div class="grid-header-divider"></div>
              `:A}
        <div
          class="grid-body"
          part="body"
          style="grid-template-rows: repeat(${this.sortedData.length}, min-content)"
        >
          ${ni(this.sortedData,e=>e.id,(t,n)=>{let r=this.rowDivider&&this.data.length-1!==n,i=this.striped&&n%2==1,a=(t.selected??!1)||this.selectable&&this._selectedRowIds.has(t.id),o=n>0?this.sortedData[n-1]:void 0,s=n<this.sortedData.length-1?this.sortedData[n+1]:void 0,c=o!==void 0&&((o.selected??!1)||this.selectable&&this._selectedRowIds.has(o.id)),l=s!==void 0&&((s.selected??!1)||this.selectable&&this._selectedRowIds.has(s.id));return O`
                <button
                  role="row"
                  class=${F({"grid-row":!0,selected:a,"selected-with-prev":a&&c,"selected-with-next":a&&l,striped:i})}
                  @click=${e=>this._handleRowClick(e,t)}
                  @keydown=${this._handleRowKeyDown}
                  data-row-id=${t.id}
                  style="grid-row: ${n+1}"
                  part="row"
                  aria-level=${I(this.hasHierarchy?(t.level??0)+1:void 0)}
                  aria-expanded=${I(t.expandable?t.expanded??!1:void 0)}
                >
                  ${Tp(e,(e,n)=>{let r=n===+!!this.selectable?this._renderRowExpander(t):A;if(this.selectable&&e.key===`__selection__`)return O`<div
                        class="grid-cell checkbox align-center selection"
                        role="cell"
                      >
                        <obc-checkbox
                          .status=${this._selectedRowIds.has(t.id)?nd.checked:nd.unchecked}
                          .disabled=${!1}
                          aria-label=${`Select row ${t.id}`}
                          @click=${e=>{e.preventDefault(),e.stopPropagation()}}
                          @change=${()=>this._toggleRowSelection(t.id)}
                        ></obc-checkbox>
                      </div>`;let i=t[e.key];return i===void 0?O`<div class="grid-cell" role="cell">
                        ${r}
                      </div>`:e.renderCell?O`<div
                        class="grid-cell ${e.dividerRight?`divider-right`:``}"
                        role="cell"
                        part=${I(i.cssPart)}
                      >
                        ${r}${e.renderCell(i,t,t.id)}
                      </div>`:this._renderCell(i,t,e,r)})}
                  ${r?O`<div class="grid-row-divider"></div>`:A}
                </button>
              `})}
          ${ni(e,e=>e.key,(e,t)=>e.dividerRight?O`<div
                    class="grid-column-divider"
                    style="grid-column: ${t+1}; grid-row: 1/${this.sortedData.length+1}"
                  ></div>`:A)}
        </div>
      </div>
    `}getAllVisibleRows(){let e=Array.from(this.renderRoot.querySelectorAll(`button[role="row"].grid-row`)),t=this.renderRoot.querySelector(`.grid-body`)?.getBoundingClientRect();if(!t)return[];let n=t.top,r=n+t.height;return e.filter(e=>e.checkVisibility()).filter(e=>e.getBoundingClientRect().top>=n&&e.getBoundingClientRect().bottom<=r).map(e=>e.getAttribute(`data-row-id`)).filter(e=>e!==null)}_handleCellButtonClick(e,t,n){e.preventDefault(),e.stopPropagation();let r=new CustomEvent(`cell-button-click`,{detail:{rowId:t.id,columnKey:n}});this.dispatchEvent(r)}_handleCellTagClick(e,t,n,r){e.preventDefault(),e.stopPropagation();let i=new CustomEvent(`cell-tag-click`,{detail:{rowId:t.id,columnKey:n,tagId:r}});this.dispatchEvent(i)}_handleCellCheckboxChange(e,t,n){e.preventDefault(),e.stopPropagation();let r=new CustomEvent(`cell-checkbox-change`,{detail:{rowId:t.id,columnKey:n,status:e.detail.status,disabled:e.detail.disabled}});this.dispatchEvent(r)}_getSelectableRowIds(){return this.data.map(e=>e.id)}_getSelectionStatus(){let e=this._getSelectableRowIds();if(e.length===0)return nd.unchecked;let t=e.filter(e=>this._selectedRowIds.has(e)).length;return t===0?nd.unchecked:t===e.length?nd.checked:nd.mixed}_emitSelectionChange(e,t){let n=this.data.filter(t=>e.includes(t.id)),r=new CustomEvent(`selection-change`,{detail:{selectedRowIds:e,selectedRows:n,source:t}});this.dispatchEvent(r)}_applySelectionChange(e,t){let n=Array.from(e);this._emitSelectionChange(n,t),this.selectedRowIds===void 0&&(this._selectedRowIds=e,this.requestUpdate())}_toggleRowSelection(e){let t=new Set(this._selectedRowIds);t.has(e)?t.delete(e):t.add(e),this._applySelectionChange(t,`row`)}_toggleAllSelection(){let e=this._getSelectableRowIds(),t=this._getSelectionStatus()===nd.checked?new Set:new Set(e);this._applySelectionChange(t,`header`)}_renderCell(e,t,n,r=A){if(e.type===`regular`)return O`<div
        class=${F({"grid-cell":!0,regular:!0,neutral:e.neutral??!1,"large-icon":e.largeIcon??!1,"no-wrap":e.noWrap??!1,[`align-${e.align??`left`}`]:!0,"divider-right":n.dividerRight??!1,vertical:e.vertical??!1})}
        role="cell"
        part=${I(kp(e,`cell`))}
      >
        ${r}${e.icon3?O`<span class="icon" part=${I(kp(e,`icon3`))}
                >${e.icon3}</span
              >`:A}
        ${e.icon2?O`<span class="icon" part=${I(kp(e,`icon2`))}
                >${e.icon2}</span
              >`:A}
        ${e.icon?O`<span class="icon" part=${I(kp(e,`icon`))}
                >${e.icon}</span
              >`:A}
        ${e.title?O`<span
                class="title"
                part=${I(kp(e,`title`))}
                >${e.title}</span
              >`:A}
        ${e.text?O`<span part=${I(kp(e,`text`))}
                >${e.text}</span
              >`:A}
      </div>`;if(e.type===`button`)return O`<div
        class="grid-cell button ${n.dividerRight?`divider-right`:``}"
        role="cell"
      >
        ${r}
        <obc-button
          variant="normal"
          fullWidth
          .disabled=${e.disabled??!1}
          ?showLeadingIcon=${e.icon!==void 0}
          part=${I(kp(e,`button`))}
          @click=${e=>this._handleCellButtonClick(e,t,n.key)}
        >
          ${e.icon?O`<span
                  slot="leading-icon"
                  part=${I(kp(e,`icon`))}
                  >${e.icon}</span
                >`:A}
          ${e.text?O`<span part=${I(kp(e,`text`))}
                  >${e.text}</span
                >`:A}
        </obc-button>
      </div>`;if(e.type===`checkbox`){let i=(e.label??e.text??``).trim()||n.label?.trim()||`Checkbox`;return O`<div
        class=${F({"grid-cell":!0,checkbox:!0,[`align-${e.align??`center`}`]:!0,"divider-right":n.dividerRight??!1})}
        role="cell"
        part=${I(kp(e,`cell`))}
      >
        ${r}
        <obc-checkbox
          .status=${e.status??nd.unchecked}
          .disabled=${e.disabled??!1}
          aria-describedby=${I(e.ariaDescribedBy)}
          aria-label=${i}
          part=${I(kp(e,`checkbox`))}
          @click=${e=>{e.preventDefault(),e.stopPropagation()}}
          @change=${e=>this._handleCellCheckboxChange(e,t,n.key)}
        ></obc-checkbox>
      </div>`}if(e.type===`tag`){let i=e.tags??(e.tag?[e.tag]:void 0)??[{id:e.tagId??`tag`,label:e.label??e.text??`Label`,color:e.color,hasIcon:e.hasIcon,icon:e.icon}],a=e.wrap??e.tags!==void 0,o=e.tags?2:void 0,s=(e.maxTags??o)===void 0?void 0:Math.max(0,Math.floor(e.maxTags??o??0)),c=s===void 0?i:i.slice(0,s),l=s===void 0?0:Math.max(0,i.length-s),u=e.overflowLabel??`+${l.toString()}`;return O`<div
        class=${F({"grid-cell":!0,tags:i.length>1,wrap:a,[`align-${e.align??`left`}`]:!0,"divider-right":n.dividerRight??!1})}
        role="cell"
        part=${I(kp(e,`cell`))}
      >
        ${r}${c.map(r=>{let i=r.hasIcon??r.icon!==void 0;return O`<obc-tag
            .label=${r.label}
            color=${r.color??Cp.gray}
            ?hasIcon=${i}
            part=${I([kp(e,`tag`),r.cssPart].filter(Boolean).join(` `)||void 0)}
            @click=${e=>this._handleCellTagClick(e,t,n.key,r.id)}
          >
            ${i&&r.icon?r.icon:A}
          </obc-tag>`})}
        ${l>0?O`<span
                class="tag-overflow"
                part=${I(kp(e,`tag-overflow`))}
                >${u}</span
              >`:A}
      </div>`}if(e.type===`horizontal-bar`){let t=e.hasBar??!0,i=e.hasScale??!1,a=!(e.hideLabels??!0),o=e.fixedAspectRatio??!0;return O`<div
        class=${F({"grid-cell":!0,"horizontal-bar":!0,[`align-${e.align??`left`}`]:!0,"divider-right":n.dividerRight??!1})}
        role="cell"
        part=${I(kp(e,`cell`))}
      >
        ${r}
        <obc-bar-horizontal
          .minValue=${e.minValue??0}
          .maxValue=${e.maxValue??100}
          .value=${e.value}
          .setpoint=${e.setpoint}
          .hasBar=${t}
          .hasScale=${i}
          .showLabels=${a}
          .priority=${e.priority??W.regular}
          .fillMode=${e.fillMode??mf.fill}
          .fillMin=${e.fillMin}
          .fillMax=${e.fillMax}
          .barThickness=${e.barThickness??24}
          .scaleType=${e.scaleType??pf.regular}
          .frameStyle=${e.frameStyle??_i.regular}
          .side=${e.side??ff.bottom}
          .state=${e.state??gi.active}
          .fixedAspectRatio=${o}
          .scaleReferenceSize=${e.scaleReferenceSize??384}
          part=${I(kp(e,`bar`))}
        ></obc-bar-horizontal>
      </div>`}return A}},Ep.styles=a(mp),Ep);N([P({type:String,attribute:`aria-label`})],Ap.prototype,`ariaLabel`,void 0),N([P({type:Array})],Ap.prototype,`data`,void 0),N([P({type:Array})],Ap.prototype,`columns`,void 0),N([P({type:Boolean})],Ap.prototype,`rowDivider`,void 0),N([P({type:Boolean})],Ap.prototype,`narrowHeader`,void 0),N([P({type:Boolean,attribute:!1})],Ap.prototype,`showHeader`,void 0),N([P({type:Boolean})],Ap.prototype,`striped`,void 0),N([P({type:Boolean})],Ap.prototype,`selectable`,void 0),N([P({type:Array})],Ap.prototype,`selectedRowIds`,void 0),N([P({type:Array})],Ap.prototype,`defaultSelectedRowIds`,void 0),N([P({type:String})],Ap.prototype,`selectAllAriaLabel`,void 0),N([ze()],Ap.prototype,`_sortByColumnIdx`,void 0),N([ze()],Ap.prototype,`_sortDirection`,void 0),N([ze()],Ap.prototype,`_selectedRowIds`,void 0),Ap=N([M(`obc-table`)],Ap);var jp,Mp=1852;function Np(e){return e.cog===null?[0,0]:[e.sog*Math.sin(e.cog),-e.sog*Math.cos(e.cog)]}function Pp(e,t){let n=t.x-e.x,r=t.y-e.y,[i,a]=Np(e),[o,s]=Np(t),c=o-i,l=s-a,u=c*c+l*l,d=Math.hypot(n,r),f=(Math.atan2(n,-r)*sf%360+360)%360;if(u<1e-9)return{vessel:t,range:d,bearing:f,cpa:null,tcpa:null};let p=-(n*c+r*l)/u;return{vessel:t,range:d,bearing:f,cpa:Math.hypot(n+c*p,r+l*p),tcpa:p}}var Fp=e=>({type:Dp.Regular,text:e}),Ip=class extends j{constructor(){super(),this.columns=[{label:`Vessel`,key:`name`},{label:`Range (NM)`,key:`range`},{label:`Bearing (°)`,key:`bearing`},{label:`CPA (NM)`,key:`cpa`},{label:`TCPA (min)`,key:`tcpa`},{label:`SOG (kn)`,key:`sog`},{label:`COG (°)`,key:`cog`}],this.own=null,this.vessels=[],this.cpaLimit=.5*Mp}render(){if(!this.own)return O`<div class="empty">Select an own ship to show the traffic around it.</div>`;let e=this.vessels.filter(e=>e.guid!==this.own.guid).map(e=>Pp(this.own,e)).sort((e,t)=>e.range-t.range).map(e=>{let t=e.cpa!==null&&e.tcpa!==null&&e.tcpa>0&&e.cpa<this.cpaLimit;return{id:e.vessel.guid,name:Fp(`${t?`⚠ `:``}${e.vessel.name??e.vessel.guid}`),range:Fp((e.range/Mp).toFixed(2)),bearing:Fp(e.bearing.toFixed(0).padStart(3,`0`)),cpa:Fp(e.cpa===null?`—`:(e.cpa/Mp).toFixed(2)),tcpa:Fp(e.tcpa===null?`—`:(e.tcpa/60).toFixed(1)),sog:Fp((e.vessel.sog*of).toFixed(1)),cog:Fp(e.vessel.cog===null?`—`:((e.vessel.cog*sf+360)%360).toFixed(0).padStart(3,`0`))}});return O`
      <span class="note">
        CPA and TCPA are estimated by this display by extrapolating each vessel's current course and speed.
        ⚠ marks a target closing to within ${(this.cpaLimit/Mp).toFixed(1)} NM.
      </span>
      <obc-table .columns=${this.columns} .data=${e} rowDivider></obc-table>
    `}};jp=Ip,jp.properties={own:{attribute:!1},vessels:{attribute:!1},cpaLimit:{type:Number}},jp.styles=o`
    :host { display: flex; flex-direction: column; gap: 8px; padding: 16px; height: 100%; box-sizing: border-box; overflow: auto; }
    .note { color: var(--element-neutral-color); font-size: 12px; }
    .empty { margin: auto; color: var(--element-neutral-color); }
  `,customElements.define(`cos-traffic-view`,Ip);var Lp=5e3,Rp=class extends EventTarget{constructor(e){super(),this.url=e,this.socket=null,this.pending=new Map,this.nextId=1}get connected(){return this.socket?.readyState===WebSocket.OPEN}connect(){return new Promise((e,t)=>{let n=new WebSocket(this.url);n.onopen=()=>{this.socket=n,this.dispatchEvent(new Event(`open`)),e()},n.onerror=()=>t(Error(`Cannot connect to ${this.url}`)),n.onclose=()=>{this.socket=null,this.failAll(Error(`Connection closed`)),this.dispatchEvent(new Event(`close`))},n.onmessage=e=>this.onMessage(String(e.data))})}close(){this.socket?.close()}call(e,t,n=[]){if(!this.socket||!this.connected)return Promise.reject(Error(`Not connected`));let r=this.nextId++;return new Promise((i,a)=>{let o=window.setTimeout(()=>{this.pending.delete(r),a(Error(`Timed out: ${e}.${t}`))},Lp);this.pending.set(r,{resolve:i,reject:a,timer:o}),this.socket.send(JSON.stringify({id:r,path:e,m:t,a:n}))})}onMessage(e){let t=JSON.parse(e),n=this.pending.get(t.id);n&&(this.pending.delete(t.id),window.clearTimeout(n.timer),t.e===void 0?n.resolve(t.r):n.reject(Error(t.e)))}failAll(e){for(let[,t]of this.pending)window.clearTimeout(t.timer),t.reject(e);this.pending.clear()}},zp=`/Services/API/Topic`,Bp=200,Vp=512,Hp=2e3,Up=[1e3,2e3,5e3],Wp=class extends EventTarget{constructor(e){super(),this.vessels=new Map,this.status=`connecting`,this.dropped=0,this.simTime=null,this.sub=null,this.lastData=0,this.attempt=0,this.stopped=!1,this.rpc=new Rp(e),this.rpc.addEventListener(`close`,()=>this.onLost())}start(){this.stopped=!1,this.open()}stop(){this.stopped=!0,window.clearTimeout(this.timer),this.sub&&this.rpc.connected&&this.rpc.call(zp,`unsubscribe`,[this.sub.client]).catch(()=>void 0),this.rpc.close()}async open(){this.setStatus(`connecting`);try{await this.rpc.connect(),this.sub=await this.rpc.call(zp,`subscribe`),this.attempt=0,this.lastData=Date.now(),this.setStatus(`connected`),this.schedule(0)}catch{this.onLost()}}onLost(){if(window.clearTimeout(this.timer),this.sub=null,this.stopped)return;this.setStatus(`disconnected`);let e=Up[Math.min(this.attempt++,Up.length-1)];this.timer=window.setTimeout(()=>void this.open(),e)}schedule(e){window.clearTimeout(this.timer),this.timer=window.setTimeout(()=>void this.poll(),e)}async poll(){if(!this.sub||this.stopped)return;let e=Date.now();try{let e=await this.rpc.call(zp,`drain`,[this.sub.path,Vp]);this.apply(e)}catch(e){if(String(e).includes(`subscribe again`)&&(this.sub=await this.rpc.call(zp,`subscribe`).catch(()=>null)),!this.rpc.connected)return}let t=Date.now()-this.lastData>Hp?`stale`:`connected`;this.setStatus(t),this.schedule(Math.max(0,Bp-(Date.now()-e)))}apply(e){this.dropped+=e.dropped;let t=!1;for(let n of e.events)if(n.m===`vessel.state`)for(let e of n.d)this.vessels.set(e.guid,e),this.simTime=e.time,t=!0;t&&(this.lastData=Date.now(),this.dispatchEvent(new Event(`update`)))}setStatus(e){e!==this.status&&(this.status=e,this.dispatchEvent(new Event(`status`)))}},Gp,Kp={conning:`Conning`,traffic:`Traffic`},qp={connecting:{indicator:`inactive`,label:`Connecting to the simulation…`},connected:{indicator:`running`,label:`Live`},stale:{indicator:`caution`,label:`No new data — values not current`},disconnected:{indicator:`alarm`,label:`Disconnected — reconnecting`}};function Jp(){return new URLSearchParams(location.search).get(`ws`)||`${location.protocol===`https:`?`wss`:`ws`}://${location.host}/ws`}var Yp=class extends j{constructor(){super(),this.feed=new Wp(Jp());let e=new URLSearchParams(location.search);this.page=e.get(`page`)in Kp?e.get(`page`):`conning`,this.own=e.get(`own`),this.menuOpen=!1,this.brillianceOpen=!1,this.tick=0,this.feed.addEventListener(`update`,()=>this.tick++),this.feed.addEventListener(`status`,()=>this.tick++)}connectedCallback(){super.connectedCallback(),this.feed.start()}disconnectedCallback(){this.feed.stop(),super.disconnectedCallback()}render(){let e=[...this.feed.vessels.values()].sort((e,t)=>(e.name??e.guid).localeCompare(t.name??t.guid)),t=this.own?this.feed.vessels.get(this.own)??null:null,n=qp[this.feed.status],r=this.feed.status===`connected`;return O`
      <obc-top-bar
        appTitle="COS Bridge"
        pageName=${Kp[this.page]}
        showDimmingButton
        showClock
        .menuButtonActivated=${this.menuOpen}
        .dimmingButtonActivated=${this.brillianceOpen}
        @menu-button-clicked=${()=>this.menuOpen=!this.menuOpen}
        @dimming-button-clicked=${()=>this.brillianceOpen=!this.brillianceOpen}
      >
        ${this.feed.simTime?O`<obc-clock slot="clock" .date=${this.feed.simTime} showSeconds></obc-clock>`:A}
      </obc-top-bar>

      <div class="row">
        ${this.menuOpen?this.renderMenu():A}
        ${this.brillianceOpen?O`<obc-brilliance-menu
              .palette=${document.documentElement.dataset.obcTheme??`day`}
              @palette-changed=${e=>document.documentElement.dataset.obcTheme=e.detail.value}
            ></obc-brilliance-menu>`:A}

        <main>
          <div class="strip">
            <span class="label">Own ship</span>
            <obc-dropdown-button
              .options=${e.map(e=>({value:e.guid,label:e.name??e.guid}))}
              .value=${this.own??void 0}
              placeholder=${e.length?`Select a vessel`:`Waiting for vessels…`}
              @change=${e=>this.select(e.detail.value)}
            ></obc-dropdown-button>
            <span class="grow"></span>
            <obc-status-indicator .status=${n.indicator}>${n.label}</obc-status-indicator>
            ${this.feed.dropped?O`<span class="label">${this.feed.dropped} events dropped</span>`:A}
            <span class="label">Simulation time is shown in the top bar</span>
          </div>
          <div class="view">
            ${this.page===`conning`?O`<cos-conning-view .vessel=${t} .current=${r}></cos-conning-view>`:O`<cos-traffic-view .own=${t} .vessels=${e}></cos-traffic-view>`}
          </div>
        </main>
      </div>
    `}renderMenu(){return O`<obc-navigation-menu>
      ${Object.keys(Kp).map(e=>O`<obc-navigation-item
          slot="main"
          label=${Kp[e]}
          ?checked=${this.page===e}
          @click=${()=>this.go(e)}
        ></obc-navigation-item>`)}
    </obc-navigation-menu>`}go(e){this.page=e,this.menuOpen=!1,this.updateUrl()}select(e){this.own=e,this.updateUrl()}updateUrl(){let e=new URLSearchParams(location.search);e.set(`page`,this.page),this.own&&e.set(`own`,this.own),history.replaceState(null,``,`?${e}`)}};Gp=Yp,Gp.properties={page:{state:!0},own:{state:!0},menuOpen:{state:!0},brillianceOpen:{state:!0},tick:{state:!0}},Gp.styles=o`
    :host { display: flex; flex-direction: column; height: 100vh; }
    .row { flex: 1; display: flex; min-height: 0; position: relative; }
    main { flex: 1; min-width: 0; display: flex; flex-direction: column; }
    .strip { display: flex; align-items: center; gap: 16px; padding: 8px 16px; background: var(--container-section-color); border-bottom: 1px solid var(--border-divider-color, transparent); flex-wrap: wrap; }
    .strip .grow { flex: 1; }
    .label { color: var(--element-neutral-color); font-size: 12px; }
    .view { flex: 1; min-height: 0; overflow: auto; }
    obc-navigation-menu { position: absolute; inset: 0 auto 0 0; z-index: 2; }
    obc-brilliance-menu { position: absolute; top: 0; right: 8px; z-index: 2; }
    obc-dropdown-button { min-width: 220px; }
  `,customElements.define(`cos-bridge-app`,Yp);