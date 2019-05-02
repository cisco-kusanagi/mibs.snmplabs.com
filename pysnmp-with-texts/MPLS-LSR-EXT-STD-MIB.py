#
# PySNMP MIB module MPLS-LSR-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MPLS-LSR-EXT-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:14:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
mplsXCGroup, mplsInSegmentGroup, mplsXCIndex, mplsLsrNotificationGroup, mplsInterfaceGroup, mplsOutSegmentGroup, mplsXCOutSegmentIndex, mplsXCInSegmentIndex = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsXCGroup", "mplsInSegmentGroup", "mplsXCIndex", "mplsLsrNotificationGroup", "mplsInterfaceGroup", "mplsOutSegmentGroup", "mplsXCOutSegmentIndex", "mplsXCInSegmentIndex")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Integer32, IpAddress, TimeTicks, ModuleIdentity, NotificationType, MibIdentifier, ObjectIdentity, Bits, Counter64, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Integer32", "IpAddress", "TimeTicks", "ModuleIdentity", "NotificationType", "MibIdentifier", "ObjectIdentity", "Bits", "Counter64", "iso", "Counter32")
RowPointer, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "DisplayString", "TextualConvention")
mplsLsrExtStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 19))
mplsLsrExtStdMIB.setRevisions(('2015-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mplsLsrExtStdMIB.setRevisionsDescriptions(('MPLS LSR-specific MIB objects extension',))
if mibBuilder.loadTexts: mplsLsrExtStdMIB.setLastUpdated('201502020000Z')
if mibBuilder.loadTexts: mplsLsrExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: mplsLsrExtStdMIB.setContactInfo(' Venkatesan Mahalingam Dell Inc, 5450 Great America Parkway, Santa Clara, CA 95054, USA Email: venkat.mahalingams@gmail.com Kannan KV Sampath Redeem, India Email: kannankvs@gmail.com Sam Aldrin Huawei Technologies 2330 Central Express Way, Santa Clara, CA 95051, USA Email: aldrin.ietf@gmail.com Thomas D. Nadeau Email: tnadeau@lucidvision.com ')
if mibBuilder.loadTexts: mplsLsrExtStdMIB.setDescription("This MIB module contains generic object definitions for MPLS LSRs in transport networks. Copyright (c) 2015 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info).")
mplsLsrExtNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 19, 0))
mplsLsrExtObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 19, 1))
mplsLsrExtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 19, 2))
mplsXCExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1), )
if mibBuilder.loadTexts: mplsXCExtTable.setReference('Multiprotocol Label Switching (MPLS) Label Switching Router (LSR) Management Information Base (MIB), RFC 3813.')
if mibBuilder.loadTexts: mplsXCExtTable.setStatus('current')
if mibBuilder.loadTexts: mplsXCExtTable.setDescription('This table sparse augments the mplsXCTable of MPLS-LSR-STD-MIB (RFC 3813) to provide MPLS-TP-specific information about associated tunnel information')
mplsXCExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1, 1), ).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsXCIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCInSegmentIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCOutSegmentIndex"))
if mibBuilder.loadTexts: mplsXCExtEntry.setReference('Multiprotocol Label Switching (MPLS) Label Switching Router (LSR) Management Information Base (MIB), RFC 3813.')
if mibBuilder.loadTexts: mplsXCExtEntry.setStatus('current')
if mibBuilder.loadTexts: mplsXCExtEntry.setDescription('An entry in this table sparsely extends the cross-connect information represented by an entry in the mplsXCTable in MPLS-LSR-STD-MIB (RFC 3813) through a sparse augmentation. An entry can be created by a network operator via SNMP SET commands or in response to signaling protocol events.')
mplsXCExtTunnelPointer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1, 1, 1), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsXCExtTunnelPointer.setReference('Multiprotocol Label Switching (MPLS) Label Switching Router (LSR) Management Information Base (MIB), RFC 3813.')
if mibBuilder.loadTexts: mplsXCExtTunnelPointer.setStatus('current')
if mibBuilder.loadTexts: mplsXCExtTunnelPointer.setDescription('This read-only object indicates the back pointer to the tunnel entry segment. The only valid value for Tunnel Pointer is mplsTunnelTable entry.')
mplsXCExtOppositeDirXCPtr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1, 1, 2), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsXCExtOppositeDirXCPtr.setReference('Multiprotocol Label Switching (MPLS) Label Switching Router (LSR) Management Information Base (MIB), RFC 3813.')
if mibBuilder.loadTexts: mplsXCExtOppositeDirXCPtr.setStatus('current')
if mibBuilder.loadTexts: mplsXCExtOppositeDirXCPtr.setDescription('This object indicates the pointer to the opposite- direction XC entry. This object cannot be modified if mplsXCRowStatus for the corresponding entry in the mplsXCTable is active(1). If this pointer is not set or removed, mplsXCOperStatus should be set to down(2).')
mplsLsrExtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 1))
mplsLsrExtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 2))
mplsLsrExtModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 1, 1)).setObjects(("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsLsrNotificationGroup"), ("MPLS-LSR-EXT-STD-MIB", "mplsXCExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLsrExtModuleFullCompliance = mplsLsrExtModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: mplsLsrExtModuleFullCompliance.setDescription('Compliance statement for agents that provide full support for MPLS-LSR-EXT-STD-MIB. The mandatory group has to be implemented by all LSRs that originate, terminate, or act as transit for TE-LSPs/tunnels. In addition, depending on the type of tunnels supported, other groups become mandatory as explained below.')
mplsLsrExtModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 1, 2)).setObjects(("MPLS-LSR-STD-MIB", "mplsInterfaceGroup"), ("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-EXT-STD-MIB", "mplsXCExtReadOnlyObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLsrExtModuleReadOnlyCompliance = mplsLsrExtModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: mplsLsrExtModuleReadOnlyCompliance.setDescription('Compliance requirement for implementations that only provide read-only support for MPLS-LSR-EXT-STD-MIB. Such devices can then be monitored but cannot be configured using this MIB module.')
mplsXCExtGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 2, 1)).setObjects(("MPLS-LSR-EXT-STD-MIB", "mplsXCExtTunnelPointer"), ("MPLS-LSR-EXT-STD-MIB", "mplsXCExtOppositeDirXCPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsXCExtGroup = mplsXCExtGroup.setStatus('current')
if mibBuilder.loadTexts: mplsXCExtGroup.setDescription('This object should be supported in order to access the tunnel entry from the XC entry.')
mplsXCExtReadOnlyObjectsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 2, 2)).setObjects(("MPLS-LSR-EXT-STD-MIB", "mplsXCExtTunnelPointer"), ("MPLS-LSR-EXT-STD-MIB", "mplsXCExtOppositeDirXCPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsXCExtReadOnlyObjectsGroup = mplsXCExtReadOnlyObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: mplsXCExtReadOnlyObjectsGroup.setDescription('This Object is needed to associate the opposite-direction (forward/reverse) XC entry.')
mibBuilder.exportSymbols("MPLS-LSR-EXT-STD-MIB", mplsLsrExtModuleReadOnlyCompliance=mplsLsrExtModuleReadOnlyCompliance, mplsLsrExtConformance=mplsLsrExtConformance, mplsLsrExtModuleFullCompliance=mplsLsrExtModuleFullCompliance, PYSNMP_MODULE_ID=mplsLsrExtStdMIB, mplsLsrExtObjects=mplsLsrExtObjects, mplsLsrExtStdMIB=mplsLsrExtStdMIB, mplsXCExtEntry=mplsXCExtEntry, mplsXCExtOppositeDirXCPtr=mplsXCExtOppositeDirXCPtr, mplsXCExtGroup=mplsXCExtGroup, mplsLsrExtGroups=mplsLsrExtGroups, mplsXCExtTable=mplsXCExtTable, mplsXCExtTunnelPointer=mplsXCExtTunnelPointer, mplsXCExtReadOnlyObjectsGroup=mplsXCExtReadOnlyObjectsGroup, mplsLsrExtCompliances=mplsLsrExtCompliances, mplsLsrExtNotifications=mplsLsrExtNotifications)
