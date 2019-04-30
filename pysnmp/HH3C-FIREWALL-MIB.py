#
# PySNMP MIB module HH3C-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-FIREWALL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, Bits, iso, ObjectIdentity, Integer32, Counter32, Unsigned32, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Bits", "iso", "ObjectIdentity", "Integer32", "Counter32", "Unsigned32", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cFireWall = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 88))
if mibBuilder.loadTexts: hh3cFireWall.setLastUpdated('200801171450Z')
if mibBuilder.loadTexts: hh3cFireWall.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cFirewallobject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 88, 1))
hh3cFirewallSpecs = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 1))
hh3cFWMaxConnNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFWMaxConnNum.setStatus('current')
hh3cFirewallGlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 2))
hh3cFWConnNumCurr = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFWConnNumCurr.setStatus('current')
mibBuilder.exportSymbols("HH3C-FIREWALL-MIB", hh3cFirewallSpecs=hh3cFirewallSpecs, hh3cFirewallobject=hh3cFirewallobject, hh3cFWMaxConnNum=hh3cFWMaxConnNum, hh3cFWConnNumCurr=hh3cFWConnNumCurr, hh3cFireWall=hh3cFireWall, hh3cFirewallGlobalStats=hh3cFirewallGlobalStats, PYSNMP_MODULE_ID=hh3cFireWall)
