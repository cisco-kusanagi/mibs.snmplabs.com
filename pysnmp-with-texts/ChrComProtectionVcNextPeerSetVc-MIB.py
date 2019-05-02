#
# PySNMP MIB module ChrComProtectionVcNextPeerSetVc-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComProtectionVcNextPeerSetVc-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:36:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
chrComProtectionVc, = mibBuilder.importSymbols("Chromatis-MIB", "chrComProtectionVc")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, NotificationType, ModuleIdentity, Gauge32, Bits, ObjectIdentity, IpAddress, MibIdentifier, Counter64, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "NotificationType", "ModuleIdentity", "Gauge32", "Bits", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter64", "Counter32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComProtectionVcNextPeerSetVcTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 12, 3, 3), )
if mibBuilder.loadTexts: chrComProtectionVcNextPeerSetVcTable.setStatus('current')
if mibBuilder.loadTexts: chrComProtectionVcNextPeerSetVcTable.setDescription('')
chrComProtectionVcNextPeerSetVcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 12, 3, 3, 1), ).setIndexNames((0, "ChrComProtectionVcNextPeerSetVc-MIB", "chrComProtectionVcNextVCPeerSetID"))
if mibBuilder.loadTexts: chrComProtectionVcNextPeerSetVcEntry.setStatus('current')
if mibBuilder.loadTexts: chrComProtectionVcNextPeerSetVcEntry.setDescription('')
chrComProtectionVcNextVCPeerSetID = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 12, 3, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComProtectionVcNextVCPeerSetID.setStatus('current')
if mibBuilder.loadTexts: chrComProtectionVcNextVCPeerSetID.setDescription('The next vacant PeerSet ID in the VC Protection PeerSet Table This field enables the NMS to create new VC protection Peers ')
mibBuilder.exportSymbols("ChrComProtectionVcNextPeerSetVc-MIB", chrComProtectionVcNextVCPeerSetID=chrComProtectionVcNextVCPeerSetID, chrComProtectionVcNextPeerSetVcTable=chrComProtectionVcNextPeerSetVcTable, chrComProtectionVcNextPeerSetVcEntry=chrComProtectionVcNextPeerSetVcEntry)
