#
# PySNMP MIB module HUAWEI-IPV6-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-IPV6-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:33:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ipv6IfIndex, = mibBuilder.importSymbols("IPV6-MIB", "ipv6IfIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, iso, NotificationType, Gauge32, IpAddress, ModuleIdentity, Integer32, TimeTicks, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "iso", "NotificationType", "Gauge32", "IpAddress", "ModuleIdentity", "Integer32", "TimeTicks", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hwIpv6Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 153))
if mibBuilder.loadTexts: hwIpv6Mib.setLastUpdated('200705241610Z')
if mibBuilder.loadTexts: hwIpv6Mib.setOrganization('IPv6-Team of Huawei Technologies')
hwIpv6MibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 1))
hwIpv6IfTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 1, 1), )
if mibBuilder.loadTexts: hwIpv6IfTable.setStatus('current')
hwIpv6IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 1, 1, 1), ).setIndexNames((0, "IPV6-MIB", "ipv6IfIndex"))
if mibBuilder.loadTexts: hwIpv6IfEntry.setStatus('current')
hwIpv6IfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIpv6IfDescr.setStatus('current')
hwIpv6IfEnableFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 1, 1, 1, 2), EnabledStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwIpv6IfEnableFlag.setStatus('current')
hwIpv6MibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 2))
hwIpv6Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 2, 1))
hwIpv6Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 2, 1, 1)).setObjects(("HUAWEI-IPV6-MIB", "hwIpv6Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIpv6Compliance = hwIpv6Compliance.setStatus('current')
hwIpv6Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 2, 2))
hwIpv6Group = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 2, 2, 1)).setObjects(("HUAWEI-IPV6-MIB", "hwIpv6IfDescr"), ("HUAWEI-IPV6-MIB", "hwIpv6IfEnableFlag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIpv6Group = hwIpv6Group.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-IPV6-MIB", hwIpv6IfTable=hwIpv6IfTable, hwIpv6MibConformance=hwIpv6MibConformance, hwIpv6Groups=hwIpv6Groups, hwIpv6IfEnableFlag=hwIpv6IfEnableFlag, hwIpv6IfDescr=hwIpv6IfDescr, hwIpv6Compliance=hwIpv6Compliance, PYSNMP_MODULE_ID=hwIpv6Mib, hwIpv6Group=hwIpv6Group, hwIpv6MibObjects=hwIpv6MibObjects, hwIpv6IfEntry=hwIpv6IfEntry, hwIpv6Compliances=hwIpv6Compliances, hwIpv6Mib=hwIpv6Mib)
