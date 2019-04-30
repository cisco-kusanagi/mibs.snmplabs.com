#
# PySNMP MIB module RBN-AAL5-VCL-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-AAL5-VCL-STAT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:43:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
atmVclVpi, atmVclVci = mibBuilder.importSymbols("ATM-MIB", "atmVclVpi", "atmVclVci")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
rbnXAtmAal5VclStatEntry, = mibBuilder.importSymbols("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclStatEntry")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, IpAddress, MibIdentifier, iso, Counter64, TimeTicks, NotificationType, Gauge32, Bits, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "IpAddress", "MibIdentifier", "iso", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "Bits", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnAal5VclStatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 1))
if mibBuilder.loadTexts: rbnAal5VclStatMIB.setLastUpdated('9804171645Z')
if mibBuilder.loadTexts: rbnAal5VclStatMIB.setOrganization('RedBack Networks, Inc.')
rbnAal5VclStatMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 1, 1))
rbnAtmAal5VclStatTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 1, 1, 1), )
if mibBuilder.loadTexts: rbnAtmAal5VclStatTable.setStatus('current')
rbnAtmAal5VclStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 1, 1, 1, 1), )
rbnXAtmAal5VclStatEntry.registerAugmentions(("RBN-AAL5-VCL-STAT-MIB", "rbnAtmAal5VclStatEntry"))
rbnAtmAal5VclStatEntry.setIndexNames(*rbnXAtmAal5VclStatEntry.getIndexNames())
if mibBuilder.loadTexts: rbnAtmAal5VclStatEntry.setStatus('current')
rbnAtmAal5VclOutDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAtmAal5VclOutDrops.setStatus('current')
rbnAal5VclStatMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 1, 2))
rbnAal5VclStatMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 1, 2, 1))
rbnAal5VclStatMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 1, 2, 2))
rbnAal5VclStatMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 1, 2, 2, 1)).setObjects(("RBN-AAL5-VCL-STAT-MIB", "rbnAal5VclStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAal5VclStatMIBCompliance = rbnAal5VclStatMIBCompliance.setStatus('current')
rbnAal5VclStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 1, 2, 1, 1)).setObjects(("RBN-AAL5-VCL-STAT-MIB", "rbnAtmAal5VclOutDrops"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAal5VclStatGroup = rbnAal5VclStatGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-AAL5-VCL-STAT-MIB", rbnAtmAal5VclOutDrops=rbnAtmAal5VclOutDrops, rbnAal5VclStatMIBCompliances=rbnAal5VclStatMIBCompliances, rbnAal5VclStatMIBGroups=rbnAal5VclStatMIBGroups, rbnAal5VclStatMIBCompliance=rbnAal5VclStatMIBCompliance, rbnAtmAal5VclStatEntry=rbnAtmAal5VclStatEntry, rbnAal5VclStatMIBObjects=rbnAal5VclStatMIBObjects, rbnAal5VclStatMIB=rbnAal5VclStatMIB, rbnAtmAal5VclStatTable=rbnAtmAal5VclStatTable, PYSNMP_MODULE_ID=rbnAal5VclStatMIB, rbnAal5VclStatGroup=rbnAal5VclStatGroup, rbnAal5VclStatMIBConformance=rbnAal5VclStatMIBConformance)
