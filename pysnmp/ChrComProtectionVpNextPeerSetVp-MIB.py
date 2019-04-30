#
# PySNMP MIB module ChrComProtectionVpNextPeerSetVp-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComProtectionVpNextPeerSetVp-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:20:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
chrComProtectionVp, = mibBuilder.importSymbols("Chromatis-MIB", "chrComProtectionVp")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Unsigned32, ModuleIdentity, iso, TimeTicks, IpAddress, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, ObjectIdentity, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "ModuleIdentity", "iso", "TimeTicks", "IpAddress", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "ObjectIdentity", "MibIdentifier", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComProtectionVpNextPeerSetVpTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 12, 2, 3), )
if mibBuilder.loadTexts: chrComProtectionVpNextPeerSetVpTable.setStatus('current')
chrComProtectionVpNextPeerSetVpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 12, 2, 3, 1), ).setIndexNames((0, "ChrComProtectionVpNextPeerSetVp-MIB", "chrComProtectionVpNextVPPeerSetID"))
if mibBuilder.loadTexts: chrComProtectionVpNextPeerSetVpEntry.setStatus('current')
chrComProtectionVpNextVPPeerSetID = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 12, 2, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComProtectionVpNextVPPeerSetID.setStatus('current')
mibBuilder.exportSymbols("ChrComProtectionVpNextPeerSetVp-MIB", chrComProtectionVpNextVPPeerSetID=chrComProtectionVpNextVPPeerSetID, chrComProtectionVpNextPeerSetVpEntry=chrComProtectionVpNextPeerSetVpEntry, chrComProtectionVpNextPeerSetVpTable=chrComProtectionVpNextPeerSetVpTable)
