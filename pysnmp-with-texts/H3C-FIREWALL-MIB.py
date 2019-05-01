#
# PySNMP MIB module H3C-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-FIREWALL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:22:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, Bits, ObjectIdentity, Counter64, NotificationType, IpAddress, TimeTicks, MibIdentifier, ModuleIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "Bits", "ObjectIdentity", "Counter64", "NotificationType", "IpAddress", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cFireWall = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88))
if mibBuilder.loadTexts: h3cFireWall.setLastUpdated('200801171450Z')
if mibBuilder.loadTexts: h3cFireWall.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: h3cFireWall.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: h3cFireWall.setDescription('The MIB is designed to manage H3C Firewall products.')
h3cFirewallobject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1))
h3cFirewallSpecs = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 1))
h3cFWMaxConnNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFWMaxConnNum.setStatus('current')
if mibBuilder.loadTexts: h3cFWMaxConnNum.setDescription('Max connection number of system.')
h3cFirewallGlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 2))
h3cFWConnNumCurr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFWConnNumCurr.setStatus('current')
if mibBuilder.loadTexts: h3cFWConnNumCurr.setDescription('The number of connections that currently exist.')
mibBuilder.exportSymbols("H3C-FIREWALL-MIB", h3cFirewallSpecs=h3cFirewallSpecs, h3cFWMaxConnNum=h3cFWMaxConnNum, h3cFirewallobject=h3cFirewallobject, PYSNMP_MODULE_ID=h3cFireWall, h3cFireWall=h3cFireWall, h3cFWConnNumCurr=h3cFWConnNumCurr, h3cFirewallGlobalStats=h3cFirewallGlobalStats)
