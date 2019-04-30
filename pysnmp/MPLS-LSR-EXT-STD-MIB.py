#
# PySNMP MIB module MPLS-LSR-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MPLS-LSR-EXT-STD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:04:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
mplsLsrNotificationGroup, mplsInterfaceGroup, mplsXCGroup, mplsOutSegmentGroup, mplsXCOutSegmentIndex, mplsXCIndex, mplsInSegmentGroup, mplsXCInSegmentIndex = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsLsrNotificationGroup", "mplsInterfaceGroup", "mplsXCGroup", "mplsOutSegmentGroup", "mplsXCOutSegmentIndex", "mplsXCIndex", "mplsInSegmentGroup", "mplsXCInSegmentIndex")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, IpAddress, MibIdentifier, NotificationType, Integer32, ObjectIdentity, Unsigned32, ModuleIdentity, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "MibIdentifier", "NotificationType", "Integer32", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Bits")
TextualConvention, RowPointer, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowPointer", "DisplayString")
mplsLsrExtStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 19))
mplsLsrExtStdMIB.setRevisions(('2015-02-02 00:00',))
if mibBuilder.loadTexts: mplsLsrExtStdMIB.setLastUpdated('201502020000Z')
if mibBuilder.loadTexts: mplsLsrExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
mplsLsrExtNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 19, 0))
mplsLsrExtObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 19, 1))
mplsLsrExtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 19, 2))
mplsXCExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1), )
if mibBuilder.loadTexts: mplsXCExtTable.setStatus('current')
mplsXCExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1, 1), ).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsXCIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCInSegmentIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCOutSegmentIndex"))
if mibBuilder.loadTexts: mplsXCExtEntry.setStatus('current')
mplsXCExtTunnelPointer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1, 1, 1), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsXCExtTunnelPointer.setStatus('current')
mplsXCExtOppositeDirXCPtr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 19, 1, 1, 1, 2), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsXCExtOppositeDirXCPtr.setStatus('current')
mplsLsrExtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 1))
mplsLsrExtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 2))
mplsLsrExtModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 1, 1)).setObjects(("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsLsrNotificationGroup"), ("MPLS-LSR-EXT-STD-MIB", "mplsXCExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLsrExtModuleFullCompliance = mplsLsrExtModuleFullCompliance.setStatus('current')
mplsLsrExtModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 1, 2)).setObjects(("MPLS-LSR-STD-MIB", "mplsInterfaceGroup"), ("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-EXT-STD-MIB", "mplsXCExtReadOnlyObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLsrExtModuleReadOnlyCompliance = mplsLsrExtModuleReadOnlyCompliance.setStatus('current')
mplsXCExtGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 2, 1)).setObjects(("MPLS-LSR-EXT-STD-MIB", "mplsXCExtTunnelPointer"), ("MPLS-LSR-EXT-STD-MIB", "mplsXCExtOppositeDirXCPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsXCExtGroup = mplsXCExtGroup.setStatus('current')
mplsXCExtReadOnlyObjectsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 19, 2, 2, 2)).setObjects(("MPLS-LSR-EXT-STD-MIB", "mplsXCExtTunnelPointer"), ("MPLS-LSR-EXT-STD-MIB", "mplsXCExtOppositeDirXCPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsXCExtReadOnlyObjectsGroup = mplsXCExtReadOnlyObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("MPLS-LSR-EXT-STD-MIB", mplsXCExtOppositeDirXCPtr=mplsXCExtOppositeDirXCPtr, mplsLsrExtModuleReadOnlyCompliance=mplsLsrExtModuleReadOnlyCompliance, mplsLsrExtObjects=mplsLsrExtObjects, mplsXCExtEntry=mplsXCExtEntry, PYSNMP_MODULE_ID=mplsLsrExtStdMIB, mplsLsrExtNotifications=mplsLsrExtNotifications, mplsLsrExtConformance=mplsLsrExtConformance, mplsLsrExtCompliances=mplsLsrExtCompliances, mplsXCExtGroup=mplsXCExtGroup, mplsXCExtTunnelPointer=mplsXCExtTunnelPointer, mplsLsrExtGroups=mplsLsrExtGroups, mplsLsrExtModuleFullCompliance=mplsLsrExtModuleFullCompliance, mplsLsrExtStdMIB=mplsLsrExtStdMIB, mplsXCExtTable=mplsXCExtTable, mplsXCExtReadOnlyObjectsGroup=mplsXCExtReadOnlyObjectsGroup)
