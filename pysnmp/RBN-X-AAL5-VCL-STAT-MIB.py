#
# PySNMP MIB module RBN-X-AAL5-VCL-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-X-AAL5-VCL-STAT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:43:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
atmVclVpi, atmVclVci = mibBuilder.importSymbols("ATM-MIB", "atmVclVpi", "atmVclVci")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rbnExperiment, = mibBuilder.importSymbols("RBN-SMI", "rbnExperiment")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, IpAddress, MibIdentifier, iso, Counter64, TimeTicks, NotificationType, Gauge32, Bits, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "IpAddress", "MibIdentifier", "iso", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "Bits", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnXAal5VclStatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 3, 1))
if mibBuilder.loadTexts: rbnXAal5VclStatMIB.setLastUpdated('9804171645Z')
if mibBuilder.loadTexts: rbnXAal5VclStatMIB.setOrganization('RedBack Networks, Inc.')
rbnXAal5VclStatMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1))
rbnXAtmAal5VclStatTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1), )
if mibBuilder.loadTexts: rbnXAtmAal5VclStatTable.setStatus('current')
rbnXAtmAal5VclStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: rbnXAtmAal5VclStatEntry.setStatus('current')
rbnXAtmAal5VclInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnXAtmAal5VclInPkts.setStatus('current')
rbnXAtmAal5VclOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnXAtmAal5VclOutPkts.setStatus('current')
rbnXAtmAal5VclInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnXAtmAal5VclInOctets.setStatus('current')
rbnXAtmAal5VclOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnXAtmAal5VclOutOctets.setStatus('current')
rbnXAal5VclStatMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 1, 2))
rbnXAal5VclStatMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 1))
rbnXAal5VclStatMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 2))
rbnXAal5VclStatMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 2, 1)).setObjects(("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAal5VclStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnXAal5VclStatMIBCompliance = rbnXAal5VclStatMIBCompliance.setStatus('current')
rbnXAal5VclStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 1, 1)).setObjects(("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclInPkts"), ("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclOutPkts"), ("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclInOctets"), ("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnXAal5VclStatGroup = rbnXAal5VclStatGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-X-AAL5-VCL-STAT-MIB", PYSNMP_MODULE_ID=rbnXAal5VclStatMIB, rbnXAtmAal5VclStatEntry=rbnXAtmAal5VclStatEntry, rbnXAal5VclStatMIBConformance=rbnXAal5VclStatMIBConformance, rbnXAtmAal5VclStatTable=rbnXAtmAal5VclStatTable, rbnXAal5VclStatMIBCompliance=rbnXAal5VclStatMIBCompliance, rbnXAal5VclStatMIB=rbnXAal5VclStatMIB, rbnXAtmAal5VclOutPkts=rbnXAtmAal5VclOutPkts, rbnXAtmAal5VclInOctets=rbnXAtmAal5VclInOctets, rbnXAal5VclStatMIBCompliances=rbnXAal5VclStatMIBCompliances, rbnXAal5VclStatMIBObjects=rbnXAal5VclStatMIBObjects, rbnXAtmAal5VclInPkts=rbnXAtmAal5VclInPkts, rbnXAal5VclStatGroup=rbnXAal5VclStatGroup, rbnXAtmAal5VclOutOctets=rbnXAtmAal5VclOutOctets, rbnXAal5VclStatMIBGroups=rbnXAal5VclStatMIBGroups)
