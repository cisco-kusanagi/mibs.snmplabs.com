#
# PySNMP MIB module RADLAN-SOCKET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-SOCKET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:40:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, MibIdentifier, iso, IpAddress, NotificationType, Counter32, Bits, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "MibIdentifier", "iso", "IpAddress", "NotificationType", "Counter32", "Bits", "TimeTicks", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlSocket = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 85))
rlSocket.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlSocket.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlSocket.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rlSocketMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 85, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSocketMibVersion.setStatus('current')
rlSocketTable = MibTable((1, 3, 6, 1, 4, 1, 89, 85, 2), )
if mibBuilder.loadTexts: rlSocketTable.setStatus('current')
rlSocketEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 85, 2, 1), ).setIndexNames((0, "RADLAN-SOCKET-MIB", "rlSocketId"))
if mibBuilder.loadTexts: rlSocketEntry.setStatus('current')
rlSocketId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 85, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSocketId.setStatus('current')
rlSocketType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 85, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("stream", 1), ("dgram", 2), ("raw", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSocketType.setStatus('current')
rlSocketState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 85, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("connected", 1), ("notConnected", 2), ("recvClosed", 3), ("sendClosed", 4), ("closed", 5), ("peerClosed", 6), ("sendRecvClosed", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSocketState.setStatus('current')
rlSocketBlockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 85, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("blocking", 1), ("nonBlocking", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSocketBlockMode.setStatus('current')
rlSocketUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 85, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSocketUpTime.setStatus('current')
mibBuilder.exportSymbols("RADLAN-SOCKET-MIB", rlSocketMibVersion=rlSocketMibVersion, rlSocketBlockMode=rlSocketBlockMode, rlSocketTable=rlSocketTable, rlSocketId=rlSocketId, PYSNMP_MODULE_ID=rlSocket, rlSocketType=rlSocketType, rlSocketEntry=rlSocketEntry, rlSocketState=rlSocketState, rlSocketUpTime=rlSocketUpTime, rlSocket=rlSocket)