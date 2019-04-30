#
# PySNMP MIB module RBN-TACACS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-TACACS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:44:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, iso, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, Gauge32, Bits, ModuleIdentity, NotificationType, MibIdentifier, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "Gauge32", "Bits", "ModuleIdentity", "NotificationType", "MibIdentifier", "TimeTicks", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnTacacsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 33))
rbnTacacsMib.setRevisions(('2004-03-01 18:00',))
if mibBuilder.loadTexts: rbnTacacsMib.setLastUpdated('200403011800Z')
if mibBuilder.loadTexts: rbnTacacsMib.setOrganization('RedBack Networks, Inc.')
rbnTacacsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 0))
rbnTacacsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1))
rbnTacacsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2))
rbnTacacsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 1))
rbnTacacsAcctObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 2))
rbnTacacsNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3))
class RbnTacacsState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("up", 2), ("down", 3))

class RbnTacacsReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("responding", 1), ("packetTimeout", 2), ("serverTimeout", 3), ("serverError", 4))

rbnTacacsContext = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsContext.setStatus('current')
rbnTacacsServerIndex = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerIndex.setStatus('current')
rbnTacacsServerAddressType = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 3), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerAddressType.setStatus('current')
rbnTacacsServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 4), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerAddress.setStatus('current')
rbnTacacsServerPort = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerPort.setStatus('current')
rbnTacacsServerState = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 6), RbnTacacsState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerState.setStatus('current')
rbnTacacsServerReason = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 7), RbnTacacsReason()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerReason.setStatus('current')
rbnTacacsUserName = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsUserName.setStatus('current')
rbnTacacsServerMsg = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 33, 1, 3, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnTacacsServerMsg.setStatus('current')
rbnTacacsStateChange = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 33, 0, 1)).setObjects(("RBN-TACACS-MIB", "rbnTacacsContext"), ("RBN-TACACS-MIB", "rbnTacacsServerIndex"), ("RBN-TACACS-MIB", "rbnTacacsServerAddressType"), ("RBN-TACACS-MIB", "rbnTacacsServerAddress"), ("RBN-TACACS-MIB", "rbnTacacsServerPort"), ("RBN-TACACS-MIB", "rbnTacacsServerState"), ("RBN-TACACS-MIB", "rbnTacacsServerReason"), ("RBN-TACACS-MIB", "rbnTacacsUserName"), ("RBN-TACACS-MIB", "rbnTacacsServerMsg"))
if mibBuilder.loadTexts: rbnTacacsStateChange.setStatus('current')
rbnTacacsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 1))
rbnTacacsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 2))
rbnTacacsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 1, 1)).setObjects(("RBN-TACACS-MIB", "rbnTacacsNotifyObjectsGroup"), ("RBN-TACACS-MIB", "rbnTacacsNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnTacacsCompliance = rbnTacacsCompliance.setStatus('current')
rbnTacacsNotifyObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 2, 2)).setObjects(("RBN-TACACS-MIB", "rbnTacacsContext"), ("RBN-TACACS-MIB", "rbnTacacsServerIndex"), ("RBN-TACACS-MIB", "rbnTacacsServerAddressType"), ("RBN-TACACS-MIB", "rbnTacacsServerAddress"), ("RBN-TACACS-MIB", "rbnTacacsServerPort"), ("RBN-TACACS-MIB", "rbnTacacsServerState"), ("RBN-TACACS-MIB", "rbnTacacsServerReason"), ("RBN-TACACS-MIB", "rbnTacacsUserName"), ("RBN-TACACS-MIB", "rbnTacacsServerMsg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnTacacsNotifyObjectsGroup = rbnTacacsNotifyObjectsGroup.setStatus('current')
rbnTacacsNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 33, 2, 2, 3)).setObjects(("RBN-TACACS-MIB", "rbnTacacsStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnTacacsNotifyGroup = rbnTacacsNotifyGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-TACACS-MIB", PYSNMP_MODULE_ID=rbnTacacsMib, rbnTacacsUserName=rbnTacacsUserName, rbnTacacsObjects=rbnTacacsObjects, rbnTacacsServerState=rbnTacacsServerState, rbnTacacsMIBConformance=rbnTacacsMIBConformance, rbnTacacsServerAddressType=rbnTacacsServerAddressType, rbnTacacsMIBObjects=rbnTacacsMIBObjects, rbnTacacsGroups=rbnTacacsGroups, rbnTacacsServerPort=rbnTacacsServerPort, rbnTacacsContext=rbnTacacsContext, rbnTacacsNotifyObjects=rbnTacacsNotifyObjects, RbnTacacsReason=RbnTacacsReason, rbnTacacsServerMsg=rbnTacacsServerMsg, rbnTacacsNotifyObjectsGroup=rbnTacacsNotifyObjectsGroup, rbnTacacsServerAddress=rbnTacacsServerAddress, rbnTacacsMIBNotifications=rbnTacacsMIBNotifications, rbnTacacsServerIndex=rbnTacacsServerIndex, rbnTacacsCompliance=rbnTacacsCompliance, rbnTacacsAcctObjects=rbnTacacsAcctObjects, rbnTacacsNotifyGroup=rbnTacacsNotifyGroup, rbnTacacsServerReason=rbnTacacsServerReason, rbnTacacsStateChange=rbnTacacsStateChange, rbnTacacsCompliances=rbnTacacsCompliances, RbnTacacsState=RbnTacacsState, rbnTacacsMib=rbnTacacsMib)
