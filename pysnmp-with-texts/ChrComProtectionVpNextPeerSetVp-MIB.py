#
# PySNMP MIB module ChrComProtectionVpNextPeerSetVp-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComProtectionVpNextPeerSetVp-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:36:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
chrComProtectionVp, = mibBuilder.importSymbols("Chromatis-MIB", "chrComProtectionVp")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, iso, NotificationType, IpAddress, Unsigned32, Counter32, Bits, MibIdentifier, ObjectIdentity, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "NotificationType", "IpAddress", "Unsigned32", "Counter32", "Bits", "MibIdentifier", "ObjectIdentity", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComProtectionVpNextPeerSetVpTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 12, 2, 3), )
if mibBuilder.loadTexts: chrComProtectionVpNextPeerSetVpTable.setStatus('current')
if mibBuilder.loadTexts: chrComProtectionVpNextPeerSetVpTable.setDescription('')
chrComProtectionVpNextPeerSetVpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 12, 2, 3, 1), ).setIndexNames((0, "ChrComProtectionVpNextPeerSetVp-MIB", "chrComProtectionVpNextVPPeerSetID"))
if mibBuilder.loadTexts: chrComProtectionVpNextPeerSetVpEntry.setStatus('current')
if mibBuilder.loadTexts: chrComProtectionVpNextPeerSetVpEntry.setDescription('')
chrComProtectionVpNextVPPeerSetID = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 12, 2, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComProtectionVpNextVPPeerSetID.setStatus('current')
if mibBuilder.loadTexts: chrComProtectionVpNextVPPeerSetID.setDescription('The next vacant PeerSet ID in the VP Protection PeerSet Table This field enables the NMS to create new VP protection PeerSet ')
mibBuilder.exportSymbols("ChrComProtectionVpNextPeerSetVp-MIB", chrComProtectionVpNextVPPeerSetID=chrComProtectionVpNextVPPeerSetID, chrComProtectionVpNextPeerSetVpEntry=chrComProtectionVpNextPeerSetVpEntry, chrComProtectionVpNextPeerSetVpTable=chrComProtectionVpNextPeerSetVpTable)
