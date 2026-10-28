(function(){
 function Q(t){ this.t=t; this.f=[]; this.op='select'; this.payload=null; this._single=false; this._maybe=false; }
 ['select','order','limit','gte','lte','neq','or','range','lt','gt','ilike','like','is','not','filter','match','contains'].forEach(function(m){ Q.prototype[m]=function(){ return this; }; });
 Q.prototype.eq=function(c,v){ this.f.push(function(r){ return String(r[c])===String(v); }); return this; };
 Q.prototype.in=function(c,vs){ this.f.push(function(r){ return vs.map(String).indexOf(String(r[c]))>=0; }); return this; };
 Q.prototype.insert=function(p){ this.op='insert'; this.payload=p; return this; };
 Q.prototype.update=function(p){ this.op='update'; this.payload=p; return this; };
 Q.prototype.upsert=function(p){ this.op='upsert'; this.payload=p; return this; };
 Q.prototype.delete=function(){ this.op='delete'; return this; };
 Q.prototype.single=function(){ this._single=true; return this; };
 Q.prototype.maybeSingle=function(){ this._maybe=true; return this; };
 Q.prototype.then=function(res, rej){ var self=this; return new Promise(function(r){ setTimeout(function(){ r(self._run()); }, 5); }).then(res, rej); };
 Q.prototype._run=function(){ var DB=window.__DB; DB.log=DB.log||[]; DB.log.push(this.op+':'+this.t);
   if (DB.missing && DB.missing.indexOf(this.t)>=0) return { data:null, error:{ message:'relation "public.'+this.t+'" does not exist' } };
   var T = DB.tables[this.t] = DB.tables[this.t] || []; var f=this.f; var match=function(r){ return f.every(function(fn){ return fn(r); }); };
   if (this.op==='select'){ var rows=T.filter(match); if(this._single) return rows.length===1?{data:rows[0],error:null}:{data:null,error:{message:'not single'}}; if(this._maybe) return {data:rows[0]||null,error:null}; return {data:rows,error:null}; }
   if (this.op==='insert'){ var ins=(Array.isArray(this.payload)?this.payload:[this.payload]).map(function(r){ return Object.assign({id:'id'+Math.random().toString(36).slice(2)}, r); }); T.push.apply(T, ins); return {data:this._single?ins[0]:ins,error:null}; }
   if (this.op==='upsert'){ var r=this.payload, key=this.t==='student_plan'?'student_id':'id'; var i=T.findIndex(function(x){ return x[key]===r[key]; }); if(i>=0) T[i]=Object.assign({},T[i],r); else T.push(Object.assign({},r)); return {data:this._single?T.find(function(x){ return x[key]===r[key]; }):[r], error:null}; }
   if (this.op==='update'){ var up=T.filter(match), p=this.payload; up.forEach(function(x){ Object.assign(x,p); }); return {data:this._single?up[0]:up,error:null}; }
   if (this.op==='delete'){ DB.tables[this.t]=T.filter(function(x){ return !match(x); }); return {data:null,error:null}; }
 };
 window.supabase={ createClient:function(){ return { from:function(t){ return new Q(t); }, rpc:function(){ return Promise.resolve({data:null,error:null}); },
   auth:{ getSession:function(){ return Promise.resolve({data:{session:{user:{id:'u1',email:'clara@example.com'}}}}); }, getUser:function(){ return Promise.resolve({data:{user:{id:'u1'}}}); }, onAuthStateChange:function(){ return {data:{subscription:{unsubscribe:function(){}}}}; }, signOut:function(){ return Promise.resolve({}); } } }; } };
})();
