#
# PySNMP MIB module BIANCA-BRICK-PROXY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-PROXY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:38:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
DisplayString, = mibBuilder.importSymbols("RFC1158-MIB", "DisplayString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, Counter32, enterprises, TimeTicks, Unsigned32, Gauge32, IpAddress, NotificationType, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "Counter32", "enterprises", "TimeTicks", "Unsigned32", "Gauge32", "IpAddress", "NotificationType", "Bits", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
biboip = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 5))
media = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 50))
ipProxyTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 5, 50), )
if mibBuilder.loadTexts: ipProxyTable.setStatus('mandatory')
if mibBuilder.loadTexts: ipProxyTable.setDescription('Contains all settings of supported proxy applications.')
ipProxyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1), ).setIndexNames((0, "BIANCA-BRICK-PROXY-MIB", "ipProxyDescr"))
if mibBuilder.loadTexts: ipProxyEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ipProxyEntry.setDescription('This table defines proxy settings of Application Level Gateway (dynamic NAT rules for special media protocols).')
ipProxyDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipProxyDescr.setStatus('mandatory')
if mibBuilder.loadTexts: ipProxyDescr.setDescription('User defined description of a proxy entry.')
ipProxyAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("delete", 3))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipProxyAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ipProxyAdminStatus.setDescription('Available values are: enable(1) disable(2) delete(3) Enable or disable functionality of given proxy entry. Entry can also be deleted by setting this variable to value delete. Default value is enable.')
ipProxyApplication = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 8, 15))).clone(namedValues=NamedValues(("sip", 1), ("mgcp", 2), ("rtsp", 3), ("h323udp", 4), ("h323tcp", 8), ("none", 15))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipProxyApplication.setStatus('mandatory')
if mibBuilder.loadTexts: ipProxyApplication.setDescription("Predefined application (media protocol) ID for this transparent proxy: 'sip' -> represents a SIP proxy Application Level Gateway (ALG); 'mgcp' -> represents a MGCP proxy ALG; 'rtsp' -> represents a multimedia proxy ALG; 'h323udp', 'h323tcp' -> represents a H323 UDP or TCP ALG.")
ipProxyProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6, 17))).clone(namedValues=NamedValues(("tcp", 6), ("udp", 17))).clone('udp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipProxyProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: ipProxyProtocol.setDescription("Transport layer protocol used by this proxy: 'udp' -> handles UDP based transport; 'tcp' -> hanldes TCP based transport. Default value is udp.")
ipProxyIntPort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipProxyIntPort.setStatus('mandatory')
if mibBuilder.loadTexts: ipProxyIntPort.setDescription('Reroute to internal port: This setting is obsolete. Its functionality is now handled by mediaTerminalTable.')
ipProxyExtPort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipProxyExtPort.setStatus('mandatory')
if mibBuilder.loadTexts: ipProxyExtPort.setDescription("Listen for packages from and to a port on an external device (located in WAN): In case of outgoing packages (to devices in WAN) this is the destination port, in case of incoming packages (from WAN) this is the source port. 'ExtPort' has to be unique for all ipProxyTable entries with the same 'Protocol' setting.")
ipProxyIntAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipProxyIntAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ipProxyIntAddr.setDescription('Rerouted internal address: This setting is obsolete. Its functionality is now handled by mediaTerminalTable.')
ipProxyPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("default", 1), ("low-latency", 2), ("high", 3), ("medium", 4), ("low", 5))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipProxyPriority.setStatus('mandatory')
if mibBuilder.loadTexts: ipProxyPriority.setDescription("QOS priority for sessions controlled by this proxy entry: 'default' -> use source priority, do not make any changes; 'low-latency' -> mark all packets in related sessions (also RTP) as high priority; 'high', 'medium', 'low' -> not used in currently implemented proxy applications.")
ipProxyTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400)).clone(7200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipProxyTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: ipProxyTimeout.setDescription('Proxy session idle timeout in seconds: if no packages were received within the time frame defined by this timeout the session will be killed.')
mediaConnTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 50, 1), )
if mibBuilder.loadTexts: mediaConnTable.setStatus('mandatory')
if mibBuilder.loadTexts: mediaConnTable.setDescription('Describes a currently active RTP session created by a SIP proxy entry.')
mediaConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1), ).setIndexNames((0, "BIANCA-BRICK-PROXY-MIB", "mediaConnIndex"))
if mibBuilder.loadTexts: mediaConnEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mediaConnEntry.setDescription('Lists RTP session parameters for monitoring usage.')
mediaConnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mediaConnIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mediaConnIndex.setDescription('Unique ID of entry.')
mediaConnIntAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mediaConnIntAddr.setStatus('mandatory')
if mibBuilder.loadTexts: mediaConnIntAddr.setDescription('Internal address of RTP stream.')
mediaConnIntPort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mediaConnIntPort.setStatus('mandatory')
if mibBuilder.loadTexts: mediaConnIntPort.setDescription('Internal port of RTP stream.')
mediaConnExtAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mediaConnExtAddr.setStatus('mandatory')
if mibBuilder.loadTexts: mediaConnExtAddr.setDescription('External (public) address of RTP stream.')
mediaConnExtPort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mediaConnExtPort.setStatus('mandatory')
if mibBuilder.loadTexts: mediaConnExtPort.setDescription('External (public) port of RTP stream.')
mediaConnRemoteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mediaConnRemoteAddr.setStatus('mandatory')
if mibBuilder.loadTexts: mediaConnRemoteAddr.setDescription('Destination address of RTP stream.')
mediaConnRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mediaConnRemotePort.setStatus('mandatory')
if mibBuilder.loadTexts: mediaConnRemotePort.setDescription('Destination port of RTP stream.')
mediaConnAge = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mediaConnAge.setStatus('mandatory')
if mibBuilder.loadTexts: mediaConnAge.setDescription('Age of RTP session.')
mediaTerminalTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 50, 2), )
if mibBuilder.loadTexts: mediaTerminalTable.setStatus('mandatory')
if mibBuilder.loadTexts: mediaTerminalTable.setDescription('Describes NAT access to proxy controlled terminals (devices) in LAN.')
mediaTerminalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1), ).setIndexNames((0, "BIANCA-BRICK-PROXY-MIB", "mediaTerminalIntAddr"), (0, "BIANCA-BRICK-PROXY-MIB", "mediaTerminalIntPort"))
if mibBuilder.loadTexts: mediaTerminalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mediaTerminalEntry.setDescription('Definition of a NAT access rules to a SIP terminal (device) located in LAN.')
mediaTerminalIntAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mediaTerminalIntAddr.setStatus('mandatory')
if mibBuilder.loadTexts: mediaTerminalIntAddr.setDescription("The terminal's internal address (address of a device in LAN).")
mediaTerminalIntPort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mediaTerminalIntPort.setStatus('mandatory')
if mibBuilder.loadTexts: mediaTerminalIntPort.setDescription("The terminal's internal port (port of a device in LAN).")
mediaTerminalExtPort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mediaTerminalExtPort.setStatus('mandatory')
if mibBuilder.loadTexts: mediaTerminalExtPort.setDescription("The terminal's external port (a port on the WAN side of the gateway used for NAT access to a device in LAN).")
mediaTerminalRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mediaTerminalRemotePort.setStatus('mandatory')
if mibBuilder.loadTexts: mediaTerminalRemotePort.setDescription("The port of a remote device (located in WAN): this entry is only useful for 'Type' = 'client'. In all other cases this value has to be '0' (disabled).")
mediaTerminalLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mediaTerminalLifetime.setStatus('mandatory')
if mibBuilder.loadTexts: mediaTerminalLifetime.setDescription("The lifetime of sessions (s) defined by this terminal entry: this parameter is only useful for 'Type' = 'client'. In this case 'Lifetime' is set to 86400 seconds by default. So if the terminal did not send or receive any data within this timeout, this terminal entry will be deleted. For 'Type' = 'server' the lifetime has to be '0' (disabled).")
mediaTerminalAge = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mediaTerminalAge.setStatus('mandatory')
if mibBuilder.loadTexts: mediaTerminalAge.setDescription("Current age of terminal's last action.")
mediaTerminalProto = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6, 17))).clone(namedValues=NamedValues(("tcp", 6), ("udp", 17))).clone('udp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mediaTerminalProto.setStatus('mandatory')
if mibBuilder.loadTexts: mediaTerminalProto.setDescription("The terminal's transport protocol: 'udp' -> terminal uses UDP as transport; 'tcp' -> terminal uses TCP as transport. Default value is udp.")
mediaTerminalType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 8))).clone(namedValues=NamedValues(("client", 1), ("server", 2), ("delete", 8))).clone('client')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mediaTerminalType.setStatus('mandatory')
if mibBuilder.loadTexts: mediaTerminalType.setDescription("The type of the terminal entry: 'client' -> autodetected (and thus listed here automatically) or manually added IP phone or softclient; 'server' -> manually added internal rerouted SIP server; 'delete' -> delete flag. Manually added clients are usually obsolete as they are autodetected by the Application Level Gateway anyways (see ipProxyTable for definition of dynamic NAT rules). 'Type' = 'server' is used in order to enable access from WAN to a SIP registrar or SIP proxy located in LAN.")
mediaTerminalSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mediaTerminalSessions.setStatus('mandatory')
if mibBuilder.loadTexts: mediaTerminalSessions.setDescription("Terminal's currently active RTP sessions.")
mibBuilder.exportSymbols("BIANCA-BRICK-PROXY-MIB", ipProxyProtocol=ipProxyProtocol, biboip=biboip, ipProxyIntPort=ipProxyIntPort, mediaConnExtPort=mediaConnExtPort, ipProxyExtPort=ipProxyExtPort, mediaTerminalEntry=mediaTerminalEntry, mediaConnExtAddr=mediaConnExtAddr, mediaConnAge=mediaConnAge, ipProxyTable=ipProxyTable, mediaConnRemoteAddr=mediaConnRemoteAddr, ipProxyPriority=ipProxyPriority, mediaTerminalRemotePort=mediaTerminalRemotePort, mediaConnIndex=mediaConnIndex, mediaConnTable=mediaConnTable, mediaTerminalIntPort=mediaTerminalIntPort, mediaConnEntry=mediaConnEntry, mediaTerminalSessions=mediaTerminalSessions, mediaTerminalAge=mediaTerminalAge, mediaTerminalType=mediaTerminalType, mediaConnIntAddr=mediaConnIntAddr, ipProxyApplication=ipProxyApplication, mediaTerminalTable=mediaTerminalTable, media=media, ipProxyEntry=ipProxyEntry, mediaConnIntPort=mediaConnIntPort, ipProxyIntAddr=ipProxyIntAddr, bintec=bintec, mediaTerminalLifetime=mediaTerminalLifetime, mediaTerminalProto=mediaTerminalProto, ipProxyDescr=ipProxyDescr, ipProxyAdminStatus=ipProxyAdminStatus, mediaConnRemotePort=mediaConnRemotePort, mediaTerminalIntAddr=mediaTerminalIntAddr, ipProxyTimeout=ipProxyTimeout, mediaTerminalExtPort=mediaTerminalExtPort, bibo=bibo)