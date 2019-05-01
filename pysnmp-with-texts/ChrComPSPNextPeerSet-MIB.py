#
# PySNMP MIB module ChrComPSPNextPeerSet-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPSPNextPeerSet-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:35:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
chrComProtectSinglePath, = mibBuilder.importSymbols("Chromatis-MIB", "chrComProtectSinglePath")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Unsigned32, IpAddress, NotificationType, Counter32, iso, Integer32, Gauge32, ModuleIdentity, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Unsigned32", "IpAddress", "NotificationType", "Counter32", "iso", "Integer32", "Gauge32", "ModuleIdentity", "TimeTicks", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPSPNextPeerSetTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 12, 4, 3), )
if mibBuilder.loadTexts: chrComPSPNextPeerSetTable.setStatus('current')
if mibBuilder.loadTexts: chrComPSPNextPeerSetTable.setDescription('')
chrComPSPNextPeerSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 12, 4, 3, 1), ).setIndexNames((0, "ChrComPSPNextPeerSet-MIB", "chrComPSPNextPathPeerSetID"))
if mibBuilder.loadTexts: chrComPSPNextPeerSetEntry.setStatus('current')
if mibBuilder.loadTexts: chrComPSPNextPeerSetEntry.setDescription('')
chrComPSPNextPathPeerSetID = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 12, 4, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPSPNextPathPeerSetID.setStatus('current')
if mibBuilder.loadTexts: chrComPSPNextPathPeerSetID.setDescription('The next vacant PeerSet ID in the Path Protection PeerSet Table This field enables the NMS to create new Path protection PeerSet ')
mibBuilder.exportSymbols("ChrComPSPNextPeerSet-MIB", chrComPSPNextPeerSetEntry=chrComPSPNextPeerSetEntry, chrComPSPNextPathPeerSetID=chrComPSPNextPathPeerSetID, chrComPSPNextPeerSetTable=chrComPSPNextPeerSetTable)
