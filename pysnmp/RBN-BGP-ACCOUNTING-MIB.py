#
# PySNMP MIB module RBN-BGP-ACCOUNTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-BGP-ACCOUNTING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:44:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, ModuleIdentity, ObjectIdentity, Counter64, Bits, IpAddress, Gauge32, Unsigned32, Integer32, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "ModuleIdentity", "ObjectIdentity", "Counter64", "Bits", "IpAddress", "Gauge32", "Unsigned32", "Integer32", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnBgpPolAcctMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 20))
rbnBgpPolAcctMIB.setRevisions(('2005-09-20 00:00', '2002-03-15 00:00',))
if mibBuilder.loadTexts: rbnBgpPolAcctMIB.setLastUpdated('200203150000Z')
if mibBuilder.loadTexts: rbnBgpPolAcctMIB.setOrganization('RedBack Networks, Inc.')
rbnBgpPolAcctMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1))
rbnBpaTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1), )
if mibBuilder.loadTexts: rbnBpaTable.setStatus('current')
rbnBpaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RBN-BGP-ACCOUNTING-MIB", "rbnBpaBucketIndex"))
if mibBuilder.loadTexts: rbnBpaEntry.setStatus('current')
rbnBpaBucketIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBpaBucketIndex.setStatus('current')
rbnBpaInPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBpaInPacketCount.setStatus('current')
rbnBpaInOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBpaInOctetCount.setStatus('current')
rbnBpaCircuitDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 192))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBpaCircuitDescr.setStatus('current')
rbnBpaInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBpaInterfaceName.setStatus('current')
rbnBpaContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBpaContextName.setStatus('current')
rbnBgpPolAcctMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 20, 3))
rbnBgpPolAcctMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 1))
rbnBgpPolAcctMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 2))
rbnBgpPolAcctMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 1, 1)).setObjects(("RBN-BGP-ACCOUNTING-MIB", "rbnBpaTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBgpPolAcctMIBCompliance = rbnBgpPolAcctMIBCompliance.setStatus('deprecated')
rbnBgpPolAcctMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 1, 2)).setObjects(("RBN-BGP-ACCOUNTING-MIB", "rbnBpaTableGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBgpPolAcctMIBCompliance1 = rbnBgpPolAcctMIBCompliance1.setStatus('current')
rbnBpaTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 2, 1)).setObjects(("RBN-BGP-ACCOUNTING-MIB", "rbnBpaBucketIndex"), ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaInPacketCount"), ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaInOctetCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBpaTableGroup = rbnBpaTableGroup.setStatus('deprecated')
rbnBpaTableGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 2, 2)).setObjects(("RBN-BGP-ACCOUNTING-MIB", "rbnBpaBucketIndex"), ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaInPacketCount"), ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaInOctetCount"), ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaCircuitDescr"), ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaInterfaceName"), ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaContextName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBpaTableGroup1 = rbnBpaTableGroup1.setStatus('current')
mibBuilder.exportSymbols("RBN-BGP-ACCOUNTING-MIB", rbnBpaInPacketCount=rbnBpaInPacketCount, rbnBgpPolAcctMIBCompliance=rbnBgpPolAcctMIBCompliance, rbnBgpPolAcctMIB=rbnBgpPolAcctMIB, rbnBgpPolAcctMIBGroups=rbnBgpPolAcctMIBGroups, rbnBpaContextName=rbnBpaContextName, rbnBpaTableGroup=rbnBpaTableGroup, rbnBpaCircuitDescr=rbnBpaCircuitDescr, rbnBgpPolAcctMIBObjects=rbnBgpPolAcctMIBObjects, rbnBpaBucketIndex=rbnBpaBucketIndex, rbnBpaInOctetCount=rbnBpaInOctetCount, rbnBpaInterfaceName=rbnBpaInterfaceName, rbnBgpPolAcctMIBConformance=rbnBgpPolAcctMIBConformance, rbnBpaTableGroup1=rbnBpaTableGroup1, rbnBpaTable=rbnBpaTable, PYSNMP_MODULE_ID=rbnBgpPolAcctMIB, rbnBgpPolAcctMIBCompliance1=rbnBgpPolAcctMIBCompliance1, rbnBpaEntry=rbnBpaEntry, rbnBgpPolAcctMIBCompliances=rbnBgpPolAcctMIBCompliances)
