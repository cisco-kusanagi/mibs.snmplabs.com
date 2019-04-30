#
# PySNMP MIB module ASCEND-MCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MCAST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
mCastGroup, = mibBuilder.importSymbols("ASCEND-MIB", "mCastGroup")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, NotificationType, Unsigned32, Bits, ModuleIdentity, Gauge32, MibIdentifier, ObjectIdentity, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "NotificationType", "Unsigned32", "Bits", "ModuleIdentity", "Gauge32", "MibIdentifier", "ObjectIdentity", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
heartBeatMulticastGroupAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 14, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartBeatMulticastGroupAddress.setStatus('mandatory')
heartBeatSourceAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 14, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartBeatSourceAddress.setStatus('mandatory')
heartBeatSlotTimeInterval = MibScalar((1, 3, 6, 1, 4, 1, 529, 14, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartBeatSlotTimeInterval.setStatus('mandatory')
heartBeatSlotCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 14, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartBeatSlotCount.setStatus('mandatory')
heartBeatPacketCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 14, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heartBeatPacketCount.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MCAST-MIB", heartBeatSlotCount=heartBeatSlotCount, heartBeatPacketCount=heartBeatPacketCount, heartBeatSlotTimeInterval=heartBeatSlotTimeInterval, heartBeatMulticastGroupAddress=heartBeatMulticastGroupAddress, heartBeatSourceAddress=heartBeatSourceAddress)
