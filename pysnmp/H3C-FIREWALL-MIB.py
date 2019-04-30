#
# PySNMP MIB module H3C-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-FIREWALL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:09:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, MibIdentifier, IpAddress, Unsigned32, TimeTicks, iso, ObjectIdentity, Integer32, Gauge32, Bits, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "MibIdentifier", "IpAddress", "Unsigned32", "TimeTicks", "iso", "ObjectIdentity", "Integer32", "Gauge32", "Bits", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cFireWall = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88))
if mibBuilder.loadTexts: h3cFireWall.setLastUpdated('200801171450Z')
if mibBuilder.loadTexts: h3cFireWall.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cFirewallobject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1))
h3cFirewallSpecs = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 1))
h3cFWMaxConnNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFWMaxConnNum.setStatus('current')
h3cFirewallGlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 2))
h3cFWConnNumCurr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFWConnNumCurr.setStatus('current')
mibBuilder.exportSymbols("H3C-FIREWALL-MIB", h3cFirewallGlobalStats=h3cFirewallGlobalStats, h3cFireWall=h3cFireWall, h3cFirewallSpecs=h3cFirewallSpecs, h3cFirewallobject=h3cFirewallobject, h3cFWMaxConnNum=h3cFWMaxConnNum, PYSNMP_MODULE_ID=h3cFireWall, h3cFWConnNumCurr=h3cFWConnNumCurr)
