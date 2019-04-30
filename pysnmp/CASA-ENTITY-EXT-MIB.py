#
# PySNMP MIB module CASA-ENTITY-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CASA-ENTITY-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
casa, = mibBuilder.importSymbols("CASA-MIB", "casa")
entPhysicalEntry, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalEntry")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, Counter64, Integer32, Gauge32, ObjectIdentity, MibIdentifier, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Unsigned32, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Unsigned32", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
casaModuleCpuMemMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 20858, 10, 13))
if mibBuilder.loadTexts: casaModuleCpuMemMib.setLastUpdated('200809040922Z')
if mibBuilder.loadTexts: casaModuleCpuMemMib.setOrganization('Casa Systems Inc')
casaMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10))
casaModuleCpuMemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 13, 1))
casaModuleCpuMemTable = MibTable((1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1), )
if mibBuilder.loadTexts: casaModuleCpuMemTable.setStatus('current')
casaModuleCpuMemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1, 1), )
entPhysicalEntry.registerAugmentions(("CASA-ENTITY-EXT-MIB", "casaModuleCpuMemEntry"))
casaModuleCpuMemEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
if mibBuilder.loadTexts: casaModuleCpuMemEntry.setStatus('current')
casaModuleTotalAllocatableMem = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1, 1, 1), Unsigned32()).setUnits('KBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaModuleTotalAllocatableMem.setStatus('current')
casaModuleTotalMemAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1, 1, 2), Unsigned32()).setUnits('KBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaModuleTotalMemAllocated.setStatus('current')
casaModuleTotalFreeMem = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1, 1, 3), Unsigned32()).setUnits('KBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaModuleTotalFreeMem.setStatus('current')
casaModuleTotalCpuUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1, 1, 4), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaModuleTotalCpuUtilization.setStatus('current')
casaCmtsCpuMemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 13, 2))
casaCmtsCpuMemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 20858, 10, 13, 2, 1)).setObjects(("CASA-ENTITY-EXT-MIB", "casaModuleTotalAllocatableMem"), ("CASA-ENTITY-EXT-MIB", "casaModuleTotalMemAllocated"), ("CASA-ENTITY-EXT-MIB", "casaModuleTotalFreeMem"), ("CASA-ENTITY-EXT-MIB", "casaModuleTotalCpuUtilization"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casaCmtsCpuMemGroup = casaCmtsCpuMemGroup.setStatus('current')
casaCmtsCpuMemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 13, 3))
casaCmtsCpuMemCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 20858, 10, 13, 3, 1)).setObjects(("CASA-CABLE-CPUMEMINFO-MIB", "casaCmtsCpuMemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casaCmtsCpuMemCompliance = casaCmtsCpuMemCompliance.setStatus('current')
mibBuilder.exportSymbols("CASA-ENTITY-EXT-MIB", casaModuleCpuMemEntry=casaModuleCpuMemEntry, casaModuleCpuMemTable=casaModuleCpuMemTable, casaModuleCpuMemObjects=casaModuleCpuMemObjects, casaCmtsCpuMemGroup=casaCmtsCpuMemGroup, casaCmtsCpuMemGroups=casaCmtsCpuMemGroups, casaCmtsCpuMemCompliance=casaCmtsCpuMemCompliance, casaModuleCpuMemMib=casaModuleCpuMemMib, casaModuleTotalMemAllocated=casaModuleTotalMemAllocated, casaModuleTotalCpuUtilization=casaModuleTotalCpuUtilization, casaModuleTotalAllocatableMem=casaModuleTotalAllocatableMem, casaModuleTotalFreeMem=casaModuleTotalFreeMem, casaCmtsCpuMemCompliances=casaCmtsCpuMemCompliances, PYSNMP_MODULE_ID=casaModuleCpuMemMib, casaMgmt=casaMgmt)
