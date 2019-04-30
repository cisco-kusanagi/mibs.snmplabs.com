#
# PySNMP MIB module CISCO-DS0BUNDLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DS0BUNDLE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, Counter64, Integer32, Unsigned32, NotificationType, Gauge32, MibIdentifier, Bits, ModuleIdentity, ObjectIdentity, TimeTicks, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Integer32", "Unsigned32", "NotificationType", "Gauge32", "MibIdentifier", "Bits", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TestAndIncr, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TestAndIncr", "TextualConvention", "RowStatus", "DisplayString")
ds0Bundle = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 32))
if mibBuilder.loadTexts: ds0Bundle.setLastUpdated('9805242010Z')
if mibBuilder.loadTexts: ds0Bundle.setOrganization('Cisco Systems, Inc.')
dsx0BundleNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 32, 2), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx0BundleNextIndex.setStatus('current')
dsx0BundleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 32, 3), )
if mibBuilder.loadTexts: dsx0BundleTable.setStatus('current')
dsx0BundleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1), ).setIndexNames((0, "CISCO-DS0BUNDLE-MIB", "dsx0BundleIndex"))
if mibBuilder.loadTexts: dsx0BundleEntry.setStatus('current')
dsx0BundleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: dsx0BundleIndex.setStatus('current')
dsx0BundleIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx0BundleIfIndex.setStatus('current')
dsx0BundleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dsx0BundleRowStatus.setStatus('current')
ds0BundleConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 32, 4))
ds0BundleGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 1))
ds0BundleCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 2))
ds0BundleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 2, 1)).setObjects(("CISCO-DS0BUNDLE-MIB", "ds0BundleConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds0BundleCompliance = ds0BundleCompliance.setStatus('current')
ds0BundleConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 1, 2)).setObjects(("CISCO-DS0BUNDLE-MIB", "dsx0BundleNextIndex"), ("CISCO-DS0BUNDLE-MIB", "dsx0BundleIfIndex"), ("CISCO-DS0BUNDLE-MIB", "dsx0BundleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds0BundleConfigGroup = ds0BundleConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DS0BUNDLE-MIB", dsx0BundleTable=dsx0BundleTable, ds0Bundle=ds0Bundle, PYSNMP_MODULE_ID=ds0Bundle, ds0BundleConformance=ds0BundleConformance, ds0BundleGroups=ds0BundleGroups, ds0BundleCompliance=ds0BundleCompliance, dsx0BundleEntry=dsx0BundleEntry, ds0BundleCompliances=ds0BundleCompliances, dsx0BundleNextIndex=dsx0BundleNextIndex, dsx0BundleRowStatus=dsx0BundleRowStatus, dsx0BundleIndex=dsx0BundleIndex, ds0BundleConfigGroup=ds0BundleConfigGroup, dsx0BundleIfIndex=dsx0BundleIfIndex)
