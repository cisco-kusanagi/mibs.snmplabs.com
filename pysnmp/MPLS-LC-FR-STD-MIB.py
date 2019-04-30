#
# PySNMP MIB module MPLS-LC-FR-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MPLS-LC-FR-STD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:04:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
DLCI, = mibBuilder.importSymbols("FRAME-RELAY-DTE-MIB", "DLCI")
mplsInterfaceIndex, = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsInterfaceIndex")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Unsigned32, MibIdentifier, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, TimeTicks, Counter32, Counter64, IpAddress, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "TimeTicks", "Counter32", "Counter64", "IpAddress", "NotificationType", "Gauge32")
DisplayString, TextualConvention, RowStatus, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "StorageType")
mplsLcFrStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 10))
mplsLcFrStdMIB.setRevisions(('2006-01-12 00:00',))
if mibBuilder.loadTexts: mplsLcFrStdMIB.setLastUpdated('200601120000Z')
if mibBuilder.loadTexts: mplsLcFrStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
mplsLcFrStdNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 10, 0))
mplsLcFrStdObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 10, 1))
mplsLcFrStdConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 10, 2))
mplsLcFrStdInterfaceConfTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1), )
if mibBuilder.loadTexts: mplsLcFrStdInterfaceConfTable.setStatus('current')
mplsLcFrStdInterfaceConfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1), ).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsInterfaceIndex"))
if mibBuilder.loadTexts: mplsLcFrStdInterfaceConfEntry.setStatus('current')
mplsLcFrStdTrafficMinDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 1), DLCI()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdTrafficMinDlci.setStatus('current')
mplsLcFrStdTrafficMaxDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 2), DLCI()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdTrafficMaxDlci.setStatus('current')
mplsLcFrStdCtrlMinDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 3), DLCI()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdCtrlMinDlci.setStatus('current')
mplsLcFrStdCtrlMaxDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 4), DLCI()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdCtrlMaxDlci.setStatus('current')
mplsLcFrStdInterfaceConfRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdInterfaceConfRowStatus.setStatus('current')
mplsLcFrStdInterfaceConfStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 6), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdInterfaceConfStorageType.setStatus('current')
mplsLcFrStdCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 1))
mplsLcFrStdGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 2))
mplsLcFrStdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 1, 1)).setObjects(("MPLS-LC-FR-STD-MIB", "mplsLcFrStdIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLcFrStdModuleFullCompliance = mplsLcFrStdModuleFullCompliance.setStatus('current')
mplsLcFrStdModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 1, 2)).setObjects(("MPLS-LC-FR-STD-MIB", "mplsLcFrStdIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLcFrStdModuleReadOnlyCompliance = mplsLcFrStdModuleReadOnlyCompliance.setStatus('current')
mplsLcFrStdIfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 2, 1)).setObjects(("MPLS-LC-FR-STD-MIB", "mplsLcFrStdTrafficMinDlci"), ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdTrafficMaxDlci"), ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdCtrlMinDlci"), ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdCtrlMaxDlci"), ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdInterfaceConfRowStatus"), ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdInterfaceConfStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLcFrStdIfGroup = mplsLcFrStdIfGroup.setStatus('current')
mibBuilder.exportSymbols("MPLS-LC-FR-STD-MIB", mplsLcFrStdModuleFullCompliance=mplsLcFrStdModuleFullCompliance, PYSNMP_MODULE_ID=mplsLcFrStdMIB, mplsLcFrStdCtrlMinDlci=mplsLcFrStdCtrlMinDlci, mplsLcFrStdCompliances=mplsLcFrStdCompliances, mplsLcFrStdModuleReadOnlyCompliance=mplsLcFrStdModuleReadOnlyCompliance, mplsLcFrStdCtrlMaxDlci=mplsLcFrStdCtrlMaxDlci, mplsLcFrStdIfGroup=mplsLcFrStdIfGroup, mplsLcFrStdConformance=mplsLcFrStdConformance, mplsLcFrStdInterfaceConfEntry=mplsLcFrStdInterfaceConfEntry, mplsLcFrStdNotifications=mplsLcFrStdNotifications, mplsLcFrStdInterfaceConfTable=mplsLcFrStdInterfaceConfTable, mplsLcFrStdObjects=mplsLcFrStdObjects, mplsLcFrStdTrafficMinDlci=mplsLcFrStdTrafficMinDlci, mplsLcFrStdTrafficMaxDlci=mplsLcFrStdTrafficMaxDlci, mplsLcFrStdInterfaceConfStorageType=mplsLcFrStdInterfaceConfStorageType, mplsLcFrStdGroups=mplsLcFrStdGroups, mplsLcFrStdInterfaceConfRowStatus=mplsLcFrStdInterfaceConfRowStatus, mplsLcFrStdMIB=mplsLcFrStdMIB)
