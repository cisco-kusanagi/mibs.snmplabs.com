#
# PySNMP MIB module CISCO-MPLS-LSR-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MPLS-LSR-EXT-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:07:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsOutSegmentGroup, mplsPerfGroup, mplsInSegmentGroup, mplsXCGroup, mplsLsrNotificationGroup, mplsXCInSegmentIndex, mplsXCIndex, mplsXCOutSegmentIndex = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup", "mplsPerfGroup", "mplsInSegmentGroup", "mplsXCGroup", "mplsLsrNotificationGroup", "mplsXCInSegmentIndex", "mplsXCIndex", "mplsXCOutSegmentIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, ModuleIdentity, Integer32, IpAddress, Counter64, NotificationType, Gauge32, Bits, Counter32, ObjectIdentity, TimeTicks, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Integer32", "IpAddress", "Counter64", "NotificationType", "Gauge32", "Bits", "Counter32", "ObjectIdentity", "TimeTicks", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowPointer")
cmplsLsrExtStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 145))
cmplsLsrExtStdMIB.setRevisions(('2012-02-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setRevisionsDescriptions(('MPLS LSR specific mib objects extension',))
if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setLastUpdated('201204300000Z')
if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setContactInfo('Venkatesan Mahalingam Dell Inc, 350 Holger way, San Jose, CA, USA Email: venkat.mahalingams@gmail.com Kannan KV Sampath Aricent, India Email: Kannan.Sampath@aricent.com Sam Aldrin Huawei Technologies 2330 Central Express Way, Santa Clara, CA 95051, USA Email: aldrin.ietf@gmail.com Thomas D. Nadeau CA Technologies 273 Corporate Drive, Portsmouth, NH, USA Email: thomas.nadeau@ca.com')
if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setDescription('Copyright (c) 2012 IETF Trust and the persons identified as the document authors. All rights reserved. This MIB module contains generic object definitions for MPLS LSR in transport networks.')
cmplsLsrExtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 0))
cmplsLsrExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 1))
cmplsLsrExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 2))
cmplsXCExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1), )
if mibBuilder.loadTexts: cmplsXCExtTable.setReference('1. Multiprotocol Label Switching (MPLS) Label Switching Router (LSR) Management Information Base (MIB), RFC 3813.')
if mibBuilder.loadTexts: cmplsXCExtTable.setStatus('current')
if mibBuilder.loadTexts: cmplsXCExtTable.setDescription('This table sparse augments the mplsXCTable of MPLS-LSR-STD-MIB [RFC3813] to provide MPLS-TP specific information about associated tunnel information')
cmplsXCExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1), ).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsXCIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCInSegmentIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCOutSegmentIndex"))
if mibBuilder.loadTexts: cmplsXCExtEntry.setReference('1. Multiprotocol Label Switching (MPLS) Label Switching Router (LSR) Management Information Base (MIB), RFC 3813.')
if mibBuilder.loadTexts: cmplsXCExtEntry.setStatus('current')
if mibBuilder.loadTexts: cmplsXCExtEntry.setDescription('An entry in this table extends the cross connect information represented by an entry in the mplsXCTable in MPLS-LSR-STD-MIB [RFC3813] through a sparse augmentation. An entry can be created by a network administrator via SNMP SET commands, or in response to signaling protocol events.')
cmplsXCExtTunnelPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1, 1), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsXCExtTunnelPointer.setReference('1. Multiprotocol Label Switching (MPLS) Label Switching Router (LSR) Management Information Base (MIB), RFC 3813.')
if mibBuilder.loadTexts: cmplsXCExtTunnelPointer.setStatus('current')
if mibBuilder.loadTexts: cmplsXCExtTunnelPointer.setDescription('This object indicates the back pointer to the tunnel entry segment. This object cannot be modified if mplsXCRowStatus for the corresponding entry in the mplsXCTable is active(1).')
cmplsXCOppositeDirXCPtr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1, 2), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsXCOppositeDirXCPtr.setReference('1. Multiprotocol Label Switching (MPLS) Label Switching Router (LSR) Management Information Base (MIB), RFC 3813.')
if mibBuilder.loadTexts: cmplsXCOppositeDirXCPtr.setStatus('current')
if mibBuilder.loadTexts: cmplsXCOppositeDirXCPtr.setDescription('This object indicates the pointer to the opposite direction XC entry. This object cannot be modified if mplsXCRowStatus for the corresponding entry in the mplsXCTable is active(1).')
cmplsLsrExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 1))
cmplsLsrExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2))
cmplsLsrExtModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2, 1)).setObjects(("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsPerfGroup"), ("MPLS-LSR-STD-MIB", "mplsLsrNotificationGroup"), ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsLsrExtModuleFullCompliance = cmplsLsrExtModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: cmplsLsrExtModuleFullCompliance.setDescription('Compliance statement for agents that provide full support for MPLS-LSR-EXT-STD-MIB. The mandatory group has to be implemented by all LSRs that originate, terminate, or act as transit for TE-LSPs/tunnels. In addition, depending on the type of tunnels supported, other groups become mandatory as explained below.')
cmplsLsrExtModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2, 2)).setObjects(("MPLS-LSR-STD-MIB", "mplsInterfaceGroup"), ("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsPerfGroup"), ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsLsrExtModuleReadOnlyCompliance = cmplsLsrExtModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: cmplsLsrExtModuleReadOnlyCompliance.setDescription('Compliance requirement for implementations that only provide read-only support for MPLS-LSR-EXT-STD-MIB. Such devices can then be monitored but cannot be configured using this MIB module.')
cmplsXCExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 1, 1)).setObjects(("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtTunnelPointer"), ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCOppositeDirXCPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsXCExtGroup = cmplsXCExtGroup.setStatus('current')
if mibBuilder.loadTexts: cmplsXCExtGroup.setDescription('This object should be supported in order to access the tunnel entry from XC entry.')
mibBuilder.exportSymbols("CISCO-MPLS-LSR-EXT-STD-MIB", PYSNMP_MODULE_ID=cmplsLsrExtStdMIB, cmplsLsrExtNotifications=cmplsLsrExtNotifications, cmplsLsrExtModuleReadOnlyCompliance=cmplsLsrExtModuleReadOnlyCompliance, cmplsXCExtGroup=cmplsXCExtGroup, cmplsLsrExtCompliances=cmplsLsrExtCompliances, cmplsXCOppositeDirXCPtr=cmplsXCOppositeDirXCPtr, cmplsXCExtTable=cmplsXCExtTable, cmplsLsrExtStdMIB=cmplsLsrExtStdMIB, cmplsLsrExtModuleFullCompliance=cmplsLsrExtModuleFullCompliance, cmplsLsrExtConformance=cmplsLsrExtConformance, cmplsXCExtEntry=cmplsXCExtEntry, cmplsXCExtTunnelPointer=cmplsXCExtTunnelPointer, cmplsLsrExtGroups=cmplsLsrExtGroups, cmplsLsrExtObjects=cmplsLsrExtObjects)
