#
# PySNMP MIB module OA-SL-STATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OA-SL-STATISTICS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:22:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, IpAddress, enterprises, Counter64, ModuleIdentity, MibIdentifier, Bits, Integer32, ObjectIdentity, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "IpAddress", "enterprises", "Counter64", "ModuleIdentity", "MibIdentifier", "Bits", "Integer32", "ObjectIdentity", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oaSlStatistics = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9))
oaSlStatistics.setRevisions(('2007-03-18 00:00',))
if mibBuilder.loadTexts: oaSlStatistics.setLastUpdated('200703180000Z')
if mibBuilder.loadTexts: oaSlStatistics.setOrganization('MRV Communications, Inc.')
nbase = MibIdentifier((1, 3, 6, 1, 4, 1, 629))
nbSwitchG1 = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1))
nbSwitchG1Il = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50))
nbPortParams = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 10))
oaSlStatConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 101))
oaSlStatGenSupport = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notSupported", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSlStatGenSupport.setStatus('current')
oaSlStatTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 2), )
if mibBuilder.loadTexts: oaSlStatTable.setStatus('current')
oaSlStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 2, 1), ).setIndexNames((0, "OA-SL-STATISTICS-MIB", "oaSlStatPortIndex"), (0, "OA-SL-STATISTICS-MIB", "oaSlStatServiceLevel"))
if mibBuilder.loadTexts: oaSlStatEntry.setStatus('current')
oaSlStatPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSlStatPortIndex.setStatus('current')
oaSlStatServiceLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSlStatServiceLevel.setStatus('current')
oaSlStatAggrOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSlStatAggrOctets.setStatus('current')
oaSlStatMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 101, 1))
oaSlStatMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 101, 2))
oaSlStatMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 101, 1, 1)).setObjects(("OA-SL-STATISTICS-MIB", "oaSlStatMandatoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oaSlStatMIBCompliance = oaSlStatMIBCompliance.setStatus('current')
oaSlStatMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 101, 2, 1)).setObjects(("OA-SL-STATISTICS-MIB", "oaSlStatGenSupport"), ("OA-SL-STATISTICS-MIB", "oaSlStatPortIndex"), ("OA-SL-STATISTICS-MIB", "oaSlStatServiceLevel"), ("OA-SL-STATISTICS-MIB", "oaSlStatAggrOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oaSlStatMandatoryGroup = oaSlStatMandatoryGroup.setStatus('current')
mibBuilder.exportSymbols("OA-SL-STATISTICS-MIB", nbPortParams=nbPortParams, oaSlStatMIBGroups=oaSlStatMIBGroups, oaSlStatGenSupport=oaSlStatGenSupport, oaSlStatConformance=oaSlStatConformance, oaSlStatMandatoryGroup=oaSlStatMandatoryGroup, oaSlStatMIBCompliances=oaSlStatMIBCompliances, oaSlStatistics=oaSlStatistics, nbSwitchG1=nbSwitchG1, oaSlStatEntry=oaSlStatEntry, nbSwitchG1Il=nbSwitchG1Il, oaSlStatAggrOctets=oaSlStatAggrOctets, oaSlStatServiceLevel=oaSlStatServiceLevel, nbase=nbase, oaSlStatMIBCompliance=oaSlStatMIBCompliance, oaSlStatPortIndex=oaSlStatPortIndex, oaSlStatTable=oaSlStatTable, PYSNMP_MODULE_ID=oaSlStatistics)
