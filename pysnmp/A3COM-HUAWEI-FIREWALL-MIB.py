#
# PySNMP MIB module A3COM-HUAWEI-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-FIREWALL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:50:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Bits, IpAddress, MibIdentifier, NotificationType, ObjectIdentity, ModuleIdentity, Gauge32, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "IpAddress", "MibIdentifier", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Gauge32", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cFireWall = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 88))
if mibBuilder.loadTexts: h3cFireWall.setLastUpdated('200801171450Z')
if mibBuilder.loadTexts: h3cFireWall.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cFirewallobject = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 88, 1))
h3cFirewallSpecs = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 88, 1, 1))
h3cFWMaxConnNum = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 88, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFWMaxConnNum.setStatus('current')
h3cFirewallGlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 88, 1, 2))
h3cFWConnNumCurr = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 88, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFWConnNumCurr.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-FIREWALL-MIB", h3cFWConnNumCurr=h3cFWConnNumCurr, h3cFirewallSpecs=h3cFirewallSpecs, h3cFirewallobject=h3cFirewallobject, h3cFireWall=h3cFireWall, h3cFirewallGlobalStats=h3cFirewallGlobalStats, PYSNMP_MODULE_ID=h3cFireWall, h3cFWMaxConnNum=h3cFWMaxConnNum)
