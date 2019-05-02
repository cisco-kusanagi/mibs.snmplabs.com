#
# PySNMP MIB module SCA-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SCA-TUNNEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:01:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
scanet, = mibBuilder.importSymbols("SCANET-MIB", "scanet")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, TimeTicks, ObjectIdentity, Counter32, Gauge32, Integer32, ModuleIdentity, Bits, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "TimeTicks", "ObjectIdentity", "Counter32", "Gauge32", "Integer32", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tunnel = MibIdentifier((1, 3, 6, 1, 4, 1, 208, 52))
tunnelInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 208, 52, 1))
tunnelInfoTable = MibTable((1, 3, 6, 1, 4, 1, 208, 52, 1, 1), )
if mibBuilder.loadTexts: tunnelInfoTable.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelInfoTable.setDescription('Configuration and monitoring information for tunneling.')
tunnelInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1), ).setIndexNames((0, "SCA-TUNNEL-MIB", "tunnelInfoIfIndex"))
if mibBuilder.loadTexts: tunnelInfoEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelInfoEntry.setDescription('')
tunnelInfoIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelInfoIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelInfoIfIndex.setDescription('Interface index')
tunnelInfoState = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("void", 1), ("create", 2), ("closed", 3), ("openclosing", 4), ("call", 5), ("destroy", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelInfoState.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelInfoState.setDescription('Interface state')
tunnelInfoDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("client", 1), ("server", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelInfoDirection.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelInfoDirection.setDescription('Call direction')
tunnelInfoLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelInfoLocalAddress.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelInfoLocalAddress.setDescription('Local IP address')
tunnelInfoRemoteAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelInfoRemoteAddress.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelInfoRemoteAddress.setDescription('Remote IP address')
tunnelInfoLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelInfoLocalPort.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelInfoLocalPort.setDescription('Local TCP port')
tunnelInfoRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelInfoRemotePort.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelInfoRemotePort.setDescription('Remote TCP port')
tunnelInfoReceiveQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelInfoReceiveQueueSize.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelInfoReceiveQueueSize.setDescription('Number of buffers in receive queue waiting to be processed')
tunnelInfoTransmitQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelInfoTransmitQueueSize.setStatus('mandatory')
if mibBuilder.loadTexts: tunnelInfoTransmitQueueSize.setDescription('Number of buffers in transmit queue waiting to be sent')
mibBuilder.exportSymbols("SCA-TUNNEL-MIB", tunnelInfo=tunnelInfo, tunnelInfoEntry=tunnelInfoEntry, tunnelInfoTable=tunnelInfoTable, tunnelInfoRemotePort=tunnelInfoRemotePort, tunnelInfoLocalPort=tunnelInfoLocalPort, tunnelInfoRemoteAddress=tunnelInfoRemoteAddress, tunnelInfoState=tunnelInfoState, tunnel=tunnel, tunnelInfoLocalAddress=tunnelInfoLocalAddress, tunnelInfoIfIndex=tunnelInfoIfIndex, tunnelInfoReceiveQueueSize=tunnelInfoReceiveQueueSize, tunnelInfoDirection=tunnelInfoDirection, tunnelInfoTransmitQueueSize=tunnelInfoTransmitQueueSize)
