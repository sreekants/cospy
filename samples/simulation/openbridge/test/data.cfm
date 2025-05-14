<cfparam name="URL.objid" default="/World/Vehicle/Vessel/POWER_DRIVEN/bedc897f-512b-45a2-aea4-bcfc248d2a87">
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>WebSocket Client</title>
</head>
<body>
  <h3>WebSocket Client</h3>
  <table>
        <tr>
            <td width="100px">Status</td><td id="messages"></td>
        </tr>
        <tr>
            <td width="100px">target</td><td id="target"></td>
        </tr>
        <tr>
            <td width="100px">angle</td><td id="angle"></td>
        </tr>
        <tr>
            <td width="100px">angleSetpoint</td><td id="angleSetpoint"></td>
        </tr>
        <tr>
            <td width="100px">thrust</td><td id="thrust"></td>
        </tr>
        <tr>
            <td width="100px">thrustSetpoint</td><td id="thrustSetpoint"></td>
        </tr>
    </table>
	
	<div id="data"></div>
  </div>

  <script>
    function set(prop, value){
        elem    = document.getElementById(prop)
        elem.innerHTML = value;
        //prop.value = value
    }

    function init(socket, type){
      // Display connection status
      socket.onopen = () => {
        console.log('Connected to WebSocket server:'+type);
        document.getElementById('messages').innerHTML = 'Connected to WebSocket server';
      };

      socket.onclose = () => {
        console.log('Disconnected from WebSocket server:'+type);
        document.getElementById('messages').innerHTML = 'Disconnected from WebSocket server';
        window.ipc = null;
      };

      socket.onerror = (error) => {
        console.error('WebSocket error:', error);
        document.getElementById('messages').innerHTML = `<p style="color: red;">Error: ${error.message}`;
      };

      // Display messages from the server
      socket.onmessage = (event) => {
        // TODO: Integrate with frontend eg:OpenBridge 
        try {
			const output = event.data.replaceAll(', ', ',<br/>')
			set('data', output);
			
            const data = JSON.parse(event.data).r.data
            if (data.target !== undefined) set('target', data.target)
            if (data.angle !== undefined) set('angle', data.angle)
            if (data.angleSetpoint !== undefined) set('angleSetpoint', data.angleSetpoint)
            if (data.thrust !== undefined) set('thrust', data.thrust)
            if (data.thrustSetpoint !== undefined) set('thrustSetpoint', data.thrustSetpoint)
        } 
        catch (error) {
          console.error('Error parsing WebSocket message:', error)
        }


      };

    }

    // Connect to the WebSocket server
<cfoutput>
    function run(socket, type){
      sock = new WebSocket('ws://localhost:8756#URL.objid#'); // Replace with your WebSocket server URL
      init(sock,'RPC')
      return sock
    }
</cfoutput>
  function checkconn(){
    if( window.ipc == null )
      window.ipc = run();

    setTimeout( checkconn, 1000 )
  }

  window.ipc = run();
  setTimeout( checkconn, 1000 )
  </script>
</body>

</html>
