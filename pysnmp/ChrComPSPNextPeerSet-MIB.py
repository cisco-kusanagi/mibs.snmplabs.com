#
# PySNMP MIB module ChrComPSPNextPeerSet-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPSPNextPeerSet-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:19:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
chrComProtectSinglePath, = mibBuilder.importSymbols("Chromatis-MIB", "chrComProtectSinglePath")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, MibIdentifier, IpAddress, Unsigned32, TimeTicks, iso, NotificationType, Bits, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "IpAddress", "Unsigned32", "TimeTicks", "iso", "NotificationType", "Bits", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComPSPNextPeerSetTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 12, 4, 3), )
if mibBuilder.loadTexts: chrComPSPNextPeerSetTable.setStatus('current')
chrComPSPNextPeerSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 12, 4, 3, 1), ).setIndexNames((0, "ChrComPSPNextPeerSet-MIB", "chrComPSPNextPathPeerSetID"))
if mibBuilder.loadTexts: chrComPSPNextPeerSetEntry.setStatus('current')
chrComPSPNextPathPeerSetID = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 12, 4, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPSPNextPathPeerSetID.setStatus('current')
mibBuilder.exportSymbols("ChrComPSPNextPeerSet-MIB", chrComPSPNextPeerSetEntry=chrComPSPNextPeerSetEntry, chrComPSPNextPathPeerSetID=chrComPSPNextPathPeerSetID, chrComPSPNextPeerSetTable=chrComPSPNextPeerSetTable)
