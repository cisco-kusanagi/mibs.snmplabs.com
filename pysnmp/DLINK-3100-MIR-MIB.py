#
# PySNMP MIB module DLINK-3100-MIR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-MIR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:33:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter32, iso, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Integer32, MibIdentifier, ModuleIdentity, ObjectIdentity, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "iso", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Integer32", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Counter64")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
rlMir = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61))
rlMir.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlMir.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlMir.setOrganization('Dlink, Inc. Dlink Semiconductor, Inc.')
rlMirMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMirMibVersion.setStatus('current')
rlMirMaxNumOfMRIsAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 2), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMirMaxNumOfMRIsAfterReset.setStatus('current')
rlMirMaxNumOfMRIs = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMirMaxNumOfMRIs.setStatus('current')
rlMirCurMriNum = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMirCurMriNum.setStatus('current')
rlMirInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 5), )
if mibBuilder.loadTexts: rlMirInterfaceTable.setStatus('current')
rlMirInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 5, 1), ).setIndexNames((0, "DLINK-3100-MIR-MIB", "rlMirInterfaceIfIndex"))
if mibBuilder.loadTexts: rlMirInterfaceEntry.setStatus('current')
rlMirInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 5, 1, 1), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMirInterfaceIfIndex.setStatus('current')
rlMirInterfaceMrid = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 5, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMirInterfaceMrid.setStatus('current')
rlMirVlanBaseReservedPortsTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 6), )
if mibBuilder.loadTexts: rlMirVlanBaseReservedPortsTable.setStatus('current')
rlMirVlanBaseReservedPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 6, 1), ).setIndexNames((0, "DLINK-3100-MIR-MIB", "rlMirVlanBaseReservedPortsIfIndex"))
if mibBuilder.loadTexts: rlMirVlanBaseReservedPortsEntry.setStatus('current')
rlMirVlanBaseReservedPortsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 6, 1, 1), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMirVlanBaseReservedPortsIfIndex.setStatus('current')
rlMirVlanBaseReservedPortsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 6, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMirVlanBaseReservedPortsStatus.setStatus('current')
rlMirVlanBaseLogicalPortsTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 7), )
if mibBuilder.loadTexts: rlMirVlanBaseLogicalPortsTable.setStatus('current')
rlMirVlanBaseLogicalPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 7, 1), ).setIndexNames((0, "DLINK-3100-MIR-MIB", "rlMirVlanBaseLogicalPortsIfIndex"))
if mibBuilder.loadTexts: rlMirVlanBaseLogicalPortsEntry.setStatus('current')
rlMirVlanBaseLogicalPortsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 7, 1, 1), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMirVlanBaseLogicalPortsIfIndex.setStatus('current')
rlMirVlanBaseLogicalPortsReservedIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 7, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMirVlanBaseLogicalPortsReservedIfIndex.setStatus('current')
rlMirVlanBaseLogicalPortsVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMirVlanBaseLogicalPortsVlanTag.setStatus('current')
rlMirVlanBaseLogicalPortsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 61, 7, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMirVlanBaseLogicalPortsStatus.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-MIR-MIB", rlMirCurMriNum=rlMirCurMriNum, rlMirVlanBaseLogicalPortsEntry=rlMirVlanBaseLogicalPortsEntry, rlMirVlanBaseReservedPortsIfIndex=rlMirVlanBaseReservedPortsIfIndex, rlMirVlanBaseLogicalPortsReservedIfIndex=rlMirVlanBaseLogicalPortsReservedIfIndex, rlMirMaxNumOfMRIsAfterReset=rlMirMaxNumOfMRIsAfterReset, rlMirInterfaceTable=rlMirInterfaceTable, rlMirInterfaceIfIndex=rlMirInterfaceIfIndex, rlMirVlanBaseLogicalPortsStatus=rlMirVlanBaseLogicalPortsStatus, rlMirVlanBaseLogicalPortsIfIndex=rlMirVlanBaseLogicalPortsIfIndex, rlMirInterfaceEntry=rlMirInterfaceEntry, PYSNMP_MODULE_ID=rlMir, rlMirVlanBaseReservedPortsStatus=rlMirVlanBaseReservedPortsStatus, rlMirMaxNumOfMRIs=rlMirMaxNumOfMRIs, rlMirMibVersion=rlMirMibVersion, rlMirVlanBaseLogicalPortsVlanTag=rlMirVlanBaseLogicalPortsVlanTag, rlMirVlanBaseReservedPortsTable=rlMirVlanBaseReservedPortsTable, rlMirVlanBaseReservedPortsEntry=rlMirVlanBaseReservedPortsEntry, rlMirVlanBaseLogicalPortsTable=rlMirVlanBaseLogicalPortsTable, rlMir=rlMir, rlMirInterfaceMrid=rlMirInterfaceMrid)
