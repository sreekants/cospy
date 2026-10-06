#!/usr/bin/python
# Filename: BridgeServer.py
# Description: Serves the OpenBridge bridge display and its JSON RPC endpoint from the simulation

from cos.core.simulation.SimulationThread import SimulationThread
from cos.core.kernel.Subsystem import Subsystem
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList
from cos.core.service.Topic import plain

from aiohttp import web, WSMsgType
import asyncio, json, os, pathlib

DEFAULT_HOST		= '127.0.0.1'
DEFAULT_PORT		= 8756
DEFAULT_MAX_CLIENTS	= 16
DEFAULT_ROOT		= pathlib.Path(__file__).resolve().parents[4] / 'samples' / 'simulation' / 'openbridge' / 'dist'
EXPIRY_INTERVAL		= 10.0		# Wall seconds between sweeps for idle bridge queues

TOPIC				= '/Services/API/Topic'

# Calls a browser may make: read-only services plus its own bridge queue (BR-RPC-05)
ALLOWED	= {
	TOPIC							: { 'subscribe', 'drain', 'unsubscribe' },
	'/Services/API/World'			: { 'describe' },
	'/Services/API/Vessel'			: { 'describe' },
	'/Services/API/ObjectManager'	: { 'get', 'find', 'exists' },
}

NOT_BUILT	= """<!doctype html><html><head><meta charset="utf-8"><title>COS Bridge</title></head>
<body style="font-family:sans-serif;padding:2em"><h1>COS Bridge</h1>
<p>The bridge front end has not been built. Run <code>npm run build</code> in
<code>samples/simulation/openbridge</code>, or set <code>root=</code> on the BridgeServer entry in
<code>network.yaml</code>.</p><p>The RPC endpoint <code>/ws</code> is running.</p></body></html>"""

class Request:
	def __init__(self, method):
		""" Minimal request object for broker.invoke_service, which reads req.d["m"]
		Arguments
			method -- Method name
		"""
		self.d	= { "m": method }
		return

class BridgeServerThread(SimulationThread):
	def __init__(self, sim, server):
		""" Constructor
		Arguments
			sim -- Reference to the simulation
			server -- Owning BridgeServer subsystem
		"""
		SimulationThread.__init__(self, sim)
		self.daemon		= True
		self.server		= server
		self.loop		= None
		self.stopping	= None
		self.ready		= False
		return

	def run(self):
		""" Runs the asyncio loop hosting the web server until stop()
		"""
		self.loop	= asyncio.new_event_loop()
		asyncio.set_event_loop( self.loop )
		try:
			self.loop.run_until_complete( self.serve() )
		except Exception as e:
			self.server.sim.log.error( 'Bridge', f'Bridge server stopped: {str(e)}' )
		finally:
			self.loop.close()
		return

	async def serve(self):
		""" Starts the site, sweeps idle queues, and shuts down on stop()
		"""
		self.stopping	= asyncio.Event()
		runner	= web.AppRunner( self.server.app() )
		await runner.setup()
		site	= web.TCPSite( runner, self.server.host, self.server.port )
		await site.start()
		self.ready	= True
		self.server.sim.log.info( 'Bridge', f'Serving the bridge on [http://{self.server.host}:{self.server.port}/] from [{self.server.root}]' )

		while not self.stopping.is_set():
			try:
				await asyncio.wait_for( self.stopping.wait(), EXPIRY_INTERVAL )
			except asyncio.TimeoutError:
				self.server.expire()

		for ws in list(self.server.sockets):
			await ws.close( code=1001, message=b'Simulation stopped' )
		await runner.cleanup()
		return

	def stop(self):
		""" Signals the server to close its connections and stop
		"""
		if self.loop is not None and self.stopping is not None:
			self.loop.call_soon_threadsafe( self.stopping.set )
		return

class BridgeServer(Subsystem):
	def __init__(self):
		""" Constructor
		"""
		Subsystem.__init__(self, "Network", "Bridge")
		self.thread			= None
		self.sockets		= set()
		self.host			= DEFAULT_HOST
		self.port			= DEFAULT_PORT
		self.root			= DEFAULT_ROOT
		self.max_clients	= DEFAULT_MAX_CLIENTS
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Module configuration
		"""
		Subsystem.on_start( self, ctxt, config )
		args	= ArgList( ctxt.sim.config.resolve_argv(config.get("config", "") or "") )

		self.host			= args['host'] or DEFAULT_HOST
		self.port			= ctxt.sim.options.get('bridge_port') or args.ToInt('port', DEFAULT_PORT)
		self.root			= pathlib.Path( args['root'] ).resolve() if args['root'] else DEFAULT_ROOT
		self.max_clients	= args.ToInt('max_clients', DEFAULT_MAX_CLIENTS)

		topic	= self.sim.objects.get( TOPIC )
		if topic is not None:
			topic.queue_size	= args.ToInt('queue_size', topic.queue_size)
			topic.idle_expiry	= args.ToFloat('idle_expiry', topic.idle_expiry)

		self.thread	= BridgeServerThread( ctxt.sim, self )
		self.thread.start()
		return

	def on_stop(self, ctxt:Context, config):
		""" Callback for simulation shutdown
		Arguments
			ctxt -- Simulation context
			config -- Module configuration
		"""
		if self.thread is not None:
			self.thread.stop()
			self.thread.join( timeout=5 )
			self.thread	= None
		return

	def app(self):
		""" Builds the aiohttp application: /ws for RPC, everything else from the content root
		"""
		app	= web.Application()
		app.router.add_get( '/ws', self.on_socket )
		app.router.add_get( '/{path:.*}', self.on_file )
		return app

	def expire(self):
		""" Removes bridge queues that have not been drained within the idle expiry
		"""
		topic	= self.sim.objects.get( TOPIC )
		if topic is not None:
			topic.expire()
		return

	async def on_file(self, request):
		""" Serves a static file from the content root
		Arguments
			request -- HTTP request
		"""
		if not self.root.is_dir():
			return web.Response( text=NOT_BUILT, content_type='text/html' )

		rel		= request.match_info.get('path', '') or 'index.html'
		path	= (self.root / rel).resolve()
		if self.root not in path.parents and path != self.root:
			raise web.HTTPForbidden()
		if path.is_dir():
			path	= path / 'index.html'
		if not path.is_file():
			raise web.HTTPNotFound()

		# index.html must not be cached; hashed assets may be (BR-SRV-06)
		cache	= 'public, max-age=31536000, immutable' if 'assets' in path.relative_to(self.root).parts else 'no-cache'
		return web.FileResponse( path, headers={ 'Cache-Control': cache } )

	async def on_socket(self, request):
		""" Serves JSON RPC over a WebSocket: {"id","path","m","a"} -> {"id","r"} or {"id","e"}
		Arguments
			request -- HTTP request
		"""
		ws	= web.WebSocketResponse( heartbeat=20 )
		if len(self.sockets) >= self.max_clients:
			await ws.prepare( request )
			await ws.close( code=1013, message=b'Too many bridge clients' )
			return ws

		await ws.prepare( request )
		self.sockets.add( ws )
		try:
			async for frame in ws:
				if frame.type != WSMsgType.TEXT:
					continue
				await ws.send_str( self.dispatch(frame.data) )
		finally:
			self.sockets.discard( ws )
		return ws

	def dispatch(self, text):
		""" Decodes, checks and invokes one request; never raises
		Arguments
			text -- JSON request
		"""
		rid	= None
		try:
			req		= json.loads( text )
			rid		= req.get('id')
			path	= req['path']
			method	= req['m']
			args	= req.get('a') or []
			args	= list(args.values()) if isinstance(args, dict) else list(args)

			if method not in ALLOWED.get(path, ()):
				raise PermissionError( f'Call not allowed from the bridge: {path}.{method}' )
			if path == TOPIC and method == 'drain' and not str(args[0]).startswith(self.sim.ipc.bridge + '/'):
				raise PermissionError( 'The bridge may only drain its own queue' )

			result	= self.invoke( path, method, args )
			return json.dumps( { "id": rid, "r": plain(result) } )
		except Exception as e:
			return json.dumps( { "id": rid, "e": f'ERROR : {str(e)}' } )

	def invoke(self, path, method, args):
		""" Invokes a service method through the RPC broker, as ZeroMQ clients do (BR-RPC-04)
		Arguments
			path -- Object path
			method -- Method name
			args -- Positional arguments
		"""
		broker	= self.sim.ipc.broker
		if broker is not None:
			return broker.invoke_service( path, Request(method), args )

		inst	= self.sim.objects.get( path )
		if inst is None:
			raise Exception( f'Object not found: {path}' )
		return getattr( inst, method )( *args )


if __name__ == "__main__":
	test = BridgeServer()
