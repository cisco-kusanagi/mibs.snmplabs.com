#
# PySNMP MIB module RBN-TACACS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-TACACS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:53:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter64, TimeTicks, Bits, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, Unsigned32, NotificationType, IpAddress, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "TimeTicks", "Bits", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "Unsigned32", "NotificationType", "IpAddress", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnTacacsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 33))
rbnTacacsMib.setRevisions(('2004-03-01 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnTacacsMib.setRevisionsDescriptions(('Initial verison.',))
if mibBuilder.loadTexts: rbnTacacsMib.setLastUpdated('200403011800Z')
if mibBuilder.loadTexts: rbnTacacsMib.setOrganization('RedBack Networks, Inc.')
if mibBuilder.loadTexts: rbnTacacsMib.setContactInfo(' RedBack Networks, Inc. Postal: 300 Holger Way San Jose, CA 95134-1362 USA Phone: +1 408 750-5000 Fax: +1 408 750-5599 E-mail: mib-info@redback.com')
if mibBuilder.loadTexts: rbnTacacsMib.setDescription('This Redback MIB defines a notification for the state of the TACACS+ server.')
rbnTacacsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 0))
rbnTacacsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1))
rbnTacacsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2))
rbnTacacsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 1))
rbnTacacsAcctObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 2))
rbnTacacsNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3))
class RbnTacacsState(TextualConvention, Integer32):
    description = "The current state of a TACACS+ server. When a server is initially configured its state is 'unknown'. When requests are sent to this server it will transition to either 'up' or 'down', depending on whether the server replies to the requests. It will then transition between 'up' and 'down' accordingly. It will never transition back to 'unknown'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("up", 2), ("down", 3))

class RbnTacacsReason(TextualConvention, Integer32):
    description = 'When a TACACS+ server transitions to a new state, this identifies the reason for the transition. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("responding", 1), ("packetTimeout", 2), ("serverTimeout", 3), ("serverError", 4))

rbnTacacsContext = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsContext.setStatus('current')
if mibBuilder.loadTexts: rbnTacacsContext.setDescription('The name of the context in which this server is configured.')
rbnTacacsServerIndex = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerIndex.setStatus('current')
if mibBuilder.loadTexts: rbnTacacsServerIndex.setDescription('A unique index value assigned to each TACACS server')
rbnTacacsServerAddressType = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 3), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerAddressType.setStatus('current')
if mibBuilder.loadTexts: rbnTacacsServerAddressType.setDescription('The type of address contained in rbnTacacsServerAddress.')
rbnTacacsServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 4), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerAddress.setStatus('current')
if mibBuilder.loadTexts: rbnTacacsServerAddress.setDescription('The TACACS+ server address.')
rbnTacacsServerPort = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerPort.setStatus('current')
if mibBuilder.loadTexts: rbnTacacsServerPort.setDescription('The TCP port number.')
rbnTacacsServerState = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 6), RbnTacacsState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerState.setStatus('current')
if mibBuilder.loadTexts: rbnTacacsServerState.setDescription('The current state of the TACACS+ server.')
rbnTacacsServerReason = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 7), RbnTacacsReason()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerReason.setStatus('current')
if mibBuilder.loadTexts: rbnTacacsServerReason.setDescription("The reason for the server's last state change.")
rbnTacacsUserName = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsUserName.setStatus('current')
if mibBuilder.loadTexts: rbnTacacsUserName.setDescription("The name of the user the system was trying to authenticate or send accouting information for when the TACACS+ server transitioned to 'down'. Note: the 'username' is only valid when transitioning due to a packet-level timeout. When transitioning due to any other reason the value for this object will be a zero-length string.")
rbnTacacsServerMsg = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerMsg.setStatus('current')
if mibBuilder.loadTexts: rbnTacacsServerMsg.setDescription("A text string optionally provided by the TACACS+ server when rbnTacacsServerReason is 'serverError'. In all other cases this is a zero-length string.")
rbnTacacsStateChange = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 33, 0, 1)).setObjects(("RBN-TACACS-MIB", "rbnTacacsContext"), ("RBN-TACACS-MIB", "rbnTacacsServerIndex"), ("RBN-TACACS-MIB", "rbnTacacsServerAddressType"), ("RBN-TACACS-MIB", "rbnTacacsServerAddress"), ("RBN-TACACS-MIB", "rbnTacacsServerPort"), ("RBN-TACACS-MIB", "rbnTacacsServerState"), ("RBN-TACACS-MIB", "rbnTacacsServerReason"), ("RBN-TACACS-MIB", "rbnTacacsUserName"), ("RBN-TACACS-MIB", "rbnTacacsServerMsg"))
if mibBuilder.loadTexts: rbnTacacsStateChange.setStatus('current')
if mibBuilder.loadTexts: rbnTacacsStateChange.setDescription("This notification signifies that a TACACS+ authorization server has transitioned to 'up' or 'down'. Note: if rbnTacacsState's value is 'down' and rbnTacacsReason's value is 'packetTimeout', then rbnTacacsUserName's value will be a username. For all other cases, rbnTacacsUserName's value will be a zero-length string. If rbnTacacsServerReason is 'serverError', then rbnTacacsServerMsg may contain a string from the server, otherwise the value is a zero-length string.")
rbnTacacsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 1))
rbnTacacsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 2))
rbnTacacsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 1, 1)).setObjects(("RBN-TACACS-MIB", "rbnTacacsNotifyObjectsGroup"), ("RBN-TACACS-MIB", "rbnTacacsNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnTacacsCompliance = rbnTacacsCompliance.setStatus('current')
if mibBuilder.loadTexts: rbnTacacsCompliance.setDescription('The compliance statement for SNMP entities which implement the Redback TACACS+ MIB.')
rbnTacacsNotifyObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 2, 2)).setObjects(("RBN-TACACS-MIB", "rbnTacacsContext"), ("RBN-TACACS-MIB", "rbnTacacsServerIndex"), ("RBN-TACACS-MIB", "rbnTacacsServerAddressType"), ("RBN-TACACS-MIB", "rbnTacacsServerAddress"), ("RBN-TACACS-MIB", "rbnTacacsServerPort"), ("RBN-TACACS-MIB", "rbnTacacsServerState"), ("RBN-TACACS-MIB", "rbnTacacsServerReason"), ("RBN-TACACS-MIB", "rbnTacacsUserName"), ("RBN-TACACS-MIB", "rbnTacacsServerMsg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnTacacsNotifyObjectsGroup = rbnTacacsNotifyObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: rbnTacacsNotifyObjectsGroup.setDescription('The collection of objects used only in notifications.')
rbnTacacsNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 2, 3)).setObjects(("RBN-TACACS-MIB", "rbnTacacsStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnTacacsNotifyGroup = rbnTacacsNotifyGroup.setStatus('current')
if mibBuilder.loadTexts: rbnTacacsNotifyGroup.setDescription('Notification for tracking the status of TACACS+ servers.')
mibBuilder.exportSymbols("RBN-TACACS-MIB", rbnTacacsMIBConformance=rbnTacacsMIBConformance, rbnTacacsObjects=rbnTacacsObjects, RbnTacacsState=RbnTacacsState, rbnTacacsUserName=rbnTacacsUserName, rbnTacacsMIBObjects=rbnTacacsMIBObjects, rbnTacacsMib=rbnTacacsMib, PYSNMP_MODULE_ID=rbnTacacsMib, rbnTacacsServerIndex=rbnTacacsServerIndex, rbnTacacsCompliances=rbnTacacsCompliances, rbnTacacsGroups=rbnTacacsGroups, rbnTacacsServerPort=rbnTacacsServerPort, rbnTacacsServerAddressType=rbnTacacsServerAddressType, rbnTacacsServerMsg=rbnTacacsServerMsg, rbnTacacsAcctObjects=rbnTacacsAcctObjects, rbnTacacsServerAddress=rbnTacacsServerAddress, rbnTacacsServerReason=rbnTacacsServerReason, rbnTacacsContext=rbnTacacsContext, rbnTacacsNotifyGroup=rbnTacacsNotifyGroup, RbnTacacsReason=RbnTacacsReason, rbnTacacsNotifyObjects=rbnTacacsNotifyObjects, rbnTacacsCompliance=rbnTacacsCompliance, rbnTacacsServerState=rbnTacacsServerState, rbnTacacsMIBNotifications=rbnTacacsMIBNotifications, rbnTacacsNotifyObjectsGroup=rbnTacacsNotifyObjectsGroup, rbnTacacsStateChange=rbnTacacsStateChange)
