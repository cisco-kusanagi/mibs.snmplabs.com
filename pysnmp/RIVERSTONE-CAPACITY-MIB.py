#
# PySNMP MIB module RIVERSTONE-CAPACITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-CAPACITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:49:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
riverstoneMibs, = mibBuilder.importSymbols("RIVERSTONE-SMI-MIB", "riverstoneMibs")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, TimeTicks, ModuleIdentity, NotificationType, Bits, Counter64, MibIdentifier, Counter32, IpAddress, ObjectIdentity, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "TimeTicks", "ModuleIdentity", "NotificationType", "Bits", "Counter64", "MibIdentifier", "Counter32", "IpAddress", "ObjectIdentity", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsCapacityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 2, 270))
rsCapacityMIB.setRevisions(('2003-04-04 13:00',))
if mibBuilder.loadTexts: rsCapacityMIB.setLastUpdated('200304041300Z')
if mibBuilder.loadTexts: rsCapacityMIB.setOrganization('Riverstone Networks, Inc')
rsCpu = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 2, 270, 5))
if mibBuilder.loadTexts: rsCpu.setStatus('current')
rsCapConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 2, 270, 35))
if mibBuilder.loadTexts: rsCapConformance.setStatus('current')
rsCapCPUTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 270, 5, 1), )
if mibBuilder.loadTexts: rsCapCPUTable.setStatus('current')
rsCapCPUEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 270, 5, 1, 1), ).setIndexNames((0, "RIVERSTONE-CAPACITY-MIB", "rsCapCPUModuleIndex"))
if mibBuilder.loadTexts: rsCapCPUEntry.setStatus('current')
rsCapCPUModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 270, 5, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: rsCapCPUModuleIndex.setStatus('current')
rsCapCPUCurrentUtilization5Sec = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 270, 5, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCapCPUCurrentUtilization5Sec.setStatus('current')
rsCapCPUCurrentUtilization60Sec = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 270, 5, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCapCPUCurrentUtilization60Sec.setStatus('current')
rsCapCPUCurrentUtilization5Min = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 270, 5, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsCapCPUCurrentUtilization5Min.setStatus('current')
rsCapCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 270, 35, 1))
rsCapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 270, 35, 2))
rsCapComplianceV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5567, 2, 270, 35, 1, 1)).setObjects(("RIVERSTONE-CAPACITY-MIB", "rsCapConfGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsCapComplianceV1 = rsCapComplianceV1.setStatus('current')
rsCapConfGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 270, 35, 2, 1)).setObjects(("RIVERSTONE-CAPACITY-MIB", "rsCapCPUCurrentUtilization5Sec"), ("RIVERSTONE-CAPACITY-MIB", "rsCapCPUCurrentUtilization60Sec"), ("RIVERSTONE-CAPACITY-MIB", "rsCapCPUCurrentUtilization5Min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsCapConfGroupV1 = rsCapConfGroupV1.setStatus('current')
mibBuilder.exportSymbols("RIVERSTONE-CAPACITY-MIB", rsCapCPUTable=rsCapCPUTable, rsCpu=rsCpu, rsCapCPUEntry=rsCapCPUEntry, rsCapConfGroupV1=rsCapConfGroupV1, rsCapCPUCurrentUtilization60Sec=rsCapCPUCurrentUtilization60Sec, rsCapacityMIB=rsCapacityMIB, PYSNMP_MODULE_ID=rsCapacityMIB, rsCapCompliances=rsCapCompliances, rsCapComplianceV1=rsCapComplianceV1, rsCapConformance=rsCapConformance, rsCapCPUCurrentUtilization5Min=rsCapCPUCurrentUtilization5Min, rsCapCPUModuleIndex=rsCapCPUModuleIndex, rsCapCPUCurrentUtilization5Sec=rsCapCPUCurrentUtilization5Sec, rsCapGroups=rsCapGroups)
